#!/usr/bin/env node
// Meta-eval probe: exercise Feynman's own deterministic citation scorer
// (evals/run.mjs) against synthetic outputs with known ground truth.
//
// The scorer is imported from a generated copy of the upstream file with the
// CLI entrypoint removed and the scoring helpers exported. No scoring logic is
// reimplemented here.
//
// Usage: node experiments/eval-scorer-probe.mjs [path-to-feynman-clone]
// Writes: experiments/eval-scorer-probe-results.json

import { readFileSync, writeFileSync, mkdirSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";

const here = dirname(fileURLToPath(import.meta.url));
const repo = resolve(process.argv[2] ?? "/tmp/feynman-src");
const runPath = join(repo, "evals", "run.mjs");
const source = readFileSync(runPath, "utf8");
const sha256 = createHash("sha256").update(source).digest("hex");
const gitSha = execFileSync("git", ["-C", repo, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();

// Strip the unconditional CLI call, then export the pure helpers.
const stripped = source.replace(/main\(\)\.catch\([\s\S]*$/, "");
if (stripped === source) throw new Error("could not strip main() from evals/run.mjs");
const generatedPath = join(here, ".tmp-eval-scorer.generated.mjs");
writeFileSync(
  generatedPath,
  `${stripped}\nexport { scoreCitations, extractIds, table, keyRecall, findFinal };\n`,
);

// evals/run.mjs parses CLI args at module scope. Hide our own positional args
// while importing it; the exported helpers do not use the parsed options.
const savedArgv = process.argv;
process.argv = savedArgv.slice(0, 2);
const { scoreCitations, extractIds, table, findFinal } = await import(pathToFileURL(generatedPath).href);
process.argv = savedArgv;

const probes = [
  {
    id: "P1",
    intent: "valid arXiv citation with matching title",
    text: "Snell et al. (2024), Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters, arXiv:2408.03314.",
    expect: (r) => r.citations === 1 && r.citation_validity === 1 && r.title_match === 1,
    expectation: "resolves and title matches",
  },
  {
    id: "P2",
    intent: "real arXiv ID attached to the wrong paper title",
    text: "Cunningham et al. (2023), Sparse Autoencoders Find Highly Interpretable Features in Language Models, arXiv:2408.03314.",
    expect: (r) => r.citations === 1 && r.citation_validity === 1 && r.title_match === 0,
    expectation: "resolves, title mismatch flagged",
  },
  {
    id: "P3",
    intent: "fabricated arXiv ID",
    text: "[related work], Retrieval Calibration for Long-Context Scientific Synthesis, arXiv:2409.99999.",
    expect: (r) => r.citations === 1 && r.citation_validity === 0 && r.unresolved.includes("arxiv:2409.99999"),
    expectation: "does not resolve; listed in unresolved",
  },
  {
    id: "P4",
    intent: "real ID, matching title, but the sentence negates the paper's central claim",
    text: "Snell et al. (2024), Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters, arXiv:2408.03314, find that test-time compute is never more effective than scaling model parameters.",
    expect: (r) => r.citations === 1 && r.citation_validity === 1 && r.title_match === 1,
    expectation: "scorer passes it (claim-level falsehood is invisible)",
    gap: true,
  },
  {
    id: "P5",
    intent: "author-year citation with no DOI or arXiv ID",
    text: "Komor et al. (2016) showed that programmable base editing avoids double-stranded DNA breaks.",
    expect: (r) => r.citations === 0 && r.citation_validity === null && r.title_match === null,
    expectation: "no citation is counted or checked",
    gap: true,
  },
  {
    id: "P6",
    intent: "resolving DOI attached to an unrelated title",
    text: "Fast Inference from Transformers via Speculative Decoding, doi:10.1038/nature17946.",
    expect: (r) => r.citations === 1 && r.citation_validity === 1 && r.title_match === 0,
    expectation: "resolves, title mismatch flagged",
  },
  {
    id: "P7",
    intent: "same ID cited twice",
    text: "arXiv:2408.03314 ... Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters ... arXiv:2408.03314.",
    expect: (r) => r.citations === 1,
    expectation: "deduplicated to one citation",
  },
  {
    id: "P8",
    intent: "web source cited by URL only (no DOI/arXiv ID)",
    text: "The vendor documents the behavior at https://example.com/docs/retrieval.",
    expect: (r) => r.citations === 0,
    expectation: "web citations are invisible to the scorer",
    gap: true,
  },
];

const results = [];
for (const p of probes) {
  const r = await scoreCitations(p.text);
  const observed = {
    citations: r.citations,
    citations_checked: r.citations_checked,
    citation_validity: r.citation_validity,
    title_match: r.title_match,
    unresolved: r.unresolved,
    title_mismatch: r.title_mismatch?.map((m) => m.id) ?? [],
  };
  results.push({
    id: p.id,
    intent: p.intent,
    expectation: p.expectation,
    gap: Boolean(p.gap),
    pass: Boolean(p.expect(observed)),
    observed,
  });
  console.log(`${p.id} ${observed.citations_checked}/${observed.citations} checked valid=${observed.citation_validity} title=${observed.title_match} ${p.expect(observed) ? "PASS" : "FAIL"} — ${p.intent}`);
}

// Aggregate-table behavior: does a report with zero checkable citations get penalized?
const tableProbe = table([
  { id: "zero-cites", completed: true, citations: 0, citation_validity: null, title_match: null, key_recall: 1, wall_s: 60, usage: { total_tokens: 1000, cost_usd: 0 } },
  { id: "one-cite", completed: true, citations: 1, citation_validity: 1, title_match: 1, key_recall: 1, wall_s: 60, usage: { total_tokens: 1000, cost_usd: 0 } },
]);

// Does the `done` metric check provenance content, or only that a file exists?
const doneRoot = mkdtempSync(join(tmpdir(), "feynman-done-probe-"));
const cases = [
  { name: "final+empty provenance", files: { "outputs/x.md": "A report.\n", "outputs/x.provenance.md": "" } },
  { name: "final, no provenance", files: { "outputs/x.md": "A report.\n" } },
  { name: "empty final+provenance", files: { "outputs/x.md": "", "outputs/x.provenance.md": "" } },
];
const doneProbe = [];
for (const c of cases) {
  const ws = mkdtempSync(join(doneRoot, "ws-"));
  mkdirSync(join(ws, "outputs"), { recursive: true });
  for (const [rel, body] of Object.entries(c.files)) writeFileSync(join(ws, rel), body);
  const found = findFinal(ws);
  doneProbe.push({ case: c.name, done: Boolean(found), picked: found ? found.replace(ws + "/", "") : null });
  console.log(`DONE ${c.name}: done=${Boolean(found)} picked=${found ? found.replace(ws + "/", "") : "-"}`);
}

const out = {
  generated_at: new Date().toISOString(),
  upstream: { repo, git_sha: gitSha, file: "evals/run.mjs", sha256 },
  import_method: "generated copy with main() removed and helpers exported; scoring logic unchanged",
  probes: results,
  table_probe: tableProbe,
  done_probe: doneProbe,
  verdict: {
    passed: results.filter((r) => r.pass).length,
    total: results.length,
    gaps_demonstrated: results.filter((r) => r.gap && r.pass).map((r) => r.id),
  },
};
mkdirSync(here, { recursive: true });
writeFileSync(join(here, "eval-scorer-probe-results.json"), JSON.stringify(out, null, 2) + "\n");
console.log("\n" + tableProbe);
console.log(`\n${out.verdict.passed}/${out.verdict.total} probes matched their expected scorer behavior; gaps demonstrated: ${out.verdict.gaps_demonstrated.join(", ")}`);
