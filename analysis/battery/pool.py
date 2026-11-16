#!/usr/bin/env python3
"""Pool the 15 probe inventories: probe families, finding clusters, answer-key exposure.

usage: pool.py            (run from analysis/battery, after verify_probes.py)

Reads derived/probes_verified.json. The two codebooks below (FAMILIES, CLUSTERS) were written
by hand after reading all 15 inventories; they are ordered regex rules, first match wins.
Writes derived/pool_probes.tsv, derived/pool_findings.tsv and derived/pool_tables.md.
"""
import json, re, collections

d = json.load(open("derived/probes_verified.json"))
runs = sorted(d)
short = lambda r: r.split("-")[-1][-6:]

# ---- probe families: (code, label, regex over "name | method | target") ----
FAMILIES = [
 ("planned",   "planned, not run",                               r"planned|not run\b"),
 ("canary",    "synthetic outputs fed to the shipped eval scorer", r"synthetic|canar|fixtures? f1|scorer (controls|negation|author|url)|aggregate table|done-criterion|blindspot|through the scorer|with the upstream scorer|scorer audit"),
 ("results",   "re-analysis of upstream's committed eval results / release notes", r"committed|published (eval|result)|release.?(note|claim)|re-?analysis|re-parse|git (history|provenance)|commit version|vendor"),
 ("scorer_read","static read of the upstream eval suite",          r"(evals?/|eval suite|run\.mjs|public eval|official eval|own eval)"),
 ("verifier",  "seeded-defect draft given to the verifier",       r"verifier|treatment arm|control arm|notesfree|unsupported|no-audit|default-contract|reconciliation|independent verification|probe wave|wave 2|wave 3|no-hint|typed gate"),
 ("fakepaper", "researcher asked about a paper that does not exist", r"non-?existent|fabricated paper|fake.?paper|false-premise|hallucination|does not exist|dead link|pressure on fake|clean rerun"),
 ("researcher","other researcher behaviour probes",                r"researcher|citation fidelity|recency|numeric|eval-claim|mbpp|sycophancy|lora"),
 ("reviewer",  "reviewer sub-agent run",                           r"reviewer"),
 ("tool",      "direct calls to a search or fetch tool",           r"crossref|fetch_content|science.?database|metadata fidelity|retrieval probe|tool.?failure|not-found|fabricated id|spot.?check"),
 ("trace",     "audit of session traces (own or children): cost, tools, structure", r"trace|session audit|token cost|cost and tool|execution trace"),
 ("telemetry", "telemetry code read or exercised",                 r"telemetry"),
 ("tests_ci",  "package tests / CI",                               r"npm test|test files|\bci\b|test and ci|self-checks"),
 ("cli",       "live feynman CLI or workflow run",                 r"feynman cli|cli probe|smoke|determinism|confabulation|ground-truth retrieval|workflow-1|status/doctor|task-less"),
 ("static",    "static read of the installed package (prompts, agents, skills)", r"static|read|audit|term-frequency|contract|grep"),
]
def family(p):
    t = " | ".join(str(p.get(k) or "") for k in ("name", "method", "target")).lower()
    for code, _, rx in FAMILIES:
        if re.search(rx, t): return code
    return "other"

# ---- finding clusters: (code, label, regex over claim, my check against upstream v0.5.65) ----
CLUSTERS = [
 ("support",  "Scorer checks id resolution and title overlap, never whether the source supports the claim", r"^(?=.*(scorer|eval|metric|valid|recall|review stating|report claiming)).*(support|negat|false claim|opposite|hygiene|correctness|irrelevant|1000 percent|smoke test|not a research-quality|rejected sources|fabricated arxiv id 2408)", "confirmed in code; 3 runs' canaries re-scored identically"),
 ("done",     "`done` is file existence (report + provenance sidecar), content not read", r"\bdone\b|completion check|file existence|findfinal|sidecar-backed", "confirmed in code (findFinal)"),
 ("denom",    "Lookups that fail on the network are dropped from the validity denominator", r"network|denominator|dropp|undefined", "confirmed in code; upstream README says so openly"),
 ("invisible","Citations without an arXiv id or DOI are not counted", r"invisible|author-year|url-only|bare arxiv|extracts only|pmid", "confirmed in code (extractIds)"),
 ("zerocite", "Zero-citation rows drop out of the summary mean", r"zero-citation|unweighted mean", "confirmed in code (table())"),
 ("titlefp",  "Title check gives false passes and false failures", r"title (check|match)|terse|title_mismatch|title mismatch|line-scoped|removal note|documents a removed|penaliz", "mechanism confirmed in code; mismatches on correct DOIs exist in committed rows"),
 ("notpkg",   "The eval suite is not in the npm package", r"not (shipped|in the npm)|absent from the npm|omitted from package|cannot run the eval|no tests or eval", "confirmed (package.json files; upstream README says so)"),
 ("notci",    "No CI workflow runs the eval", r"\bci\b|workflow references|manual", "confirmed (3 workflow files, none mention evals)"),
 ("subset",   "Committed results cover 4 of 12 questions, /lit only, one run each", r"4 of (the |its )?12|four of the twelve|eight of the 12|only 4|subset|workflow lit|only the /lit|no repeated|12 questions, runs use", "confirmed (22 rows, q01/q04/q07/q10, workflow lit)"),
 ("dirty",    "Headline rows were run on a dirty tree", r"dirty", "confirmed (14 of 22 rows git_dirty)"),
 ("workdir",  "Committed rows store absolute local workdirs, so they cannot be re-scored by others", r"workdir", "confirmed (22 of 22 rows)"),
 ("keyleak",  "The study's own answer key or hints reached the subject", r"answer key|answers|ground_truth|probe fixtures|told the verifier|supplied correct|defect hints|contamination", "about the study, not Feynman; see the exposure table"),
 ("cost",     "Cost is $0 in every committed row", r"cost", "confirmed (0 of 22 rows have cost)"),
 ("version",  "Version / SHA labels in results disagree with the release note", r"0\.5\.0|0\.5\.2|sha|version label|different model", "confirmed (43-citation file is labelled 0.5.0; pre-wait files 0.5.2)"),
 ("stale",    "No committed eval result since 2026-09-24", r"after 2026-09-24|newest public|stale|landed after|post-fix|stop at", "confirmed (latest result file 2026-09-24; installed 0.5.65)"),
 ("ceiling",  "Validity is 100% on every completed committed row (no discrimination)", r"ceiling|100% (for|in all|on completed)|never failed|305", "confirmed (18 of 18 rows with citations; 305 citations)"),
 ("relmatch", "Release-note numbers match the committed files", r"release.?note.*(match|trace|consistent)|match(es)? (the )?committed|under.?11|10\.87", "confirmed (44 citations, max wall 652 s)"),
 ("determin", "Eval scoring is deterministic, no LLM judge", r"deterministic|no llm judge", "confirmed"),
 ("caught",   "The eval caught a real regression / keeps failures", r"caught a real regression|catching a real|failures are kept", "consistent with committed pre-wait rows; not otherwise checked"),
 ("stats",    "Small-n statistics on the committed results", r"wilson|fisher|interval|not statistically|like-for-like|swing", "arithmetic, not checked"),
 ("npmtest",  "`npm test` in the shipped package runs zero tests", r"npm test|zero tests|0 tests|architecture:check|test files", "plausible from package.json (tests/ not shipped); exit code not re-run. Test counts 61/349 are upstream main, not 0.5.65 (60/345)"),
 ("telem",    "Telemetry sends raw error text (home folder redacted), which can carry arguments", r"telemetry", "code confirmed (errorText, 4,000 chars). README does say errors and stack traces are sent; the conflict is with 'never sends tool arguments'"),
 ("sampling", "No temperature / seed control or record", r"temperature|seed|sampling|top_p", "confirmed for src/, extensions/, prompts/ (no 'temperature')"),
 ("enforce",  "Provenance / verification rules are prompt text; no runtime check", r"runtime|policy only|instructions only|machine-checked|validator|not validated|no shipped code|second llm pass|acceptancerole|attestation|hand-written free text", "not exhaustively checked; no counter-example found"),
 ("samemodel","Lead, verifier and reviewer run on the same model", r"same model|share a model|inherit|same-model", "true of these runs by construction"),
 ("vcaught",  "Verifier caught the planted defects", r"(verifier|harness).*(caught|flagged|handled|fixed|addressed|removed|detected|passed|kept|corrected|preserved|repaired)|planted|seeded|\d+/\d+ (defects|probes)|\d+ of \d+ planted|passes|passed 4/4", "behavioural; see answer-key table"),
 ("rrefuse",  "Researcher / lead refused to invent a nonexistent paper", r"refus|nonexistent|no evidence for|did not invent|invented no", "behavioural, n = 1-2 per run"),
 ("crossref", "Crossref lookup is a fuzzy search: a fake DOI returns unrelated records", r"crossref", "not checked"),
 ("fetch",    "fetch_content returns error pages as success", r"fetch_content|soft-404|404", "not checked; runs disagree (see conflicts)"),
 ("alpha",    "Tool lists disagree with the prompts (alpha_* tools, reviewer allowlist)", r"alpha|allowlist|workflow:true|save directory", "confirmed: SYSTEM.md names alpha_* tools, no agent lists them; reviewer has no tools line; /log vs session-log directories differ"),
 ("reviewer", "Reviewer found real problems in the lead's own draft", r"reviewer", "behavioural, n = 1 per run"),
 ("tracefacts","Descriptive counts from session traces", r"token|tool calls|trace|session", "descriptive"),
]
def cluster(f):
    t = str(f.get("claim") or "").lower()
    for code, _, rx, _ in CLUSTERS:
        if re.search(rx, t): return code
    return "other"

P = [(r, p, family(p)) for r in runs for p in d[r]["probes"]]
F = [(r, f, cluster(f)) for r in runs for f in d[r]["findings"]]

with open("derived/pool_probes.tsv", "w") as o:
    o.write("run\tid\tfamily\tname\ttarget\tn\n")
    for r, p, fam in P: o.write("\t".join([r, str(p.get("id")), fam] + [re.sub(r"\s+", " ", str(p.get(k)))[:160] for k in ("name", "target", "n")]) + "\n")
with open("derived/pool_findings.tsv", "w") as o:
    o.write("run\tid\tcluster\tdirection\tquote_status\tclaim\n")
    for r, f, c in F: o.write("\t".join([r, str(f.get("id")), c, str(f.get("direction"))[:12], str(f.get("status")), re.sub(r"\s+", " ", str(f.get("claim")))]) + "\n")

L = ["# Pooled tables (generated by pool.py)\n"]
L += ["## Probe families by run\n", "Cell = number of probes of that family in the run. Families are assigned by ordered regex rules in pool.py.\n",
      "| family | " + " | ".join(short(r) for r in runs) + " | runs | probes |", "|---|" + "---|" * (len(runs) + 2)]
for code, label, _ in FAMILIES + [("other", "other", "")]:
    c = [sum(1 for r2, _, f in P if r2 == r and f == code) for r in runs]
    if sum(c): L.append(f"| {label} | " + " | ".join(str(x) if x else "" for x in c) + f" | {sum(1 for x in c if x)} | {sum(c)} |")
L += ["\n## Finding clusters by run\n", "Cell = number of findings in that cluster. 'Check' is my own check against upstream v0.5.65, not the coders'.\n",
      "| cluster | runs | findings | check | which runs |", "|---|---|---|---|---|"]
rows = []
for code, label, _, chk in CLUSTERS + [("other", "unclustered", "", "")]:
    rs = [r for r in runs if any(r2 == r and c == code for r2, _, c in F)]
    n = sum(1 for _, _, c in F if c == code)
    if n: rows.append((len(rs), f"| {label} | {len(rs)} | {n} | {chk} | {' '.join(short(r) for r in rs)} |"))
L += [x for _, x in sorted(rows, key=lambda t: -t[0])]
open("derived/pool_tables.md", "w").write("\n".join(L) + "\n")
print("\n".join(L))
print("\nUNCLUSTERED:"); [print(" ", short(r), f.get("id"), str(f.get("claim"))[:110]) for r, f, c in F if c == "other"]
print("\nOTHER PROBES:"); [print(" ", short(r), p.get("id"), str(p.get("name"))[:60], "|", str(p.get("method"))[:40]) for r, p, f in P if f == "other"]
