#!/usr/bin/env node
// Score the unverified draft and the verifier's corrected output with Feynman's
// own evals/run.mjs citation scorer, to test whether the metric can see the
// correction. Uses the same generated-import approach as eval-scorer-probe.mjs.

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const repo = resolve(process.argv[2] ?? "/tmp/feynman-src");
const runPath = join(repo, "evals", "run.mjs");
const source = readFileSync(runPath, "utf8");
const generatedPath = join(here, ".tmp-eval-scorer.generated.mjs");
writeFileSync(generatedPath, `${source.replace(/main\(\)\.catch\([\s\S]*$/, "")}\nexport { scoreCitations };\n`);
const saved = process.argv;
process.argv = saved.slice(0, 2);
const { scoreCitations } = await import(pathToFileURL(generatedPath).href);
process.argv = saved;

const files = {
  draft: "/work/outputs/.probes/verifier-probe-draft.md",
  clean_verified: "/tmp/verifier-probe-clean/verified.md",
  contaminated_verified: "/work/outputs/.probes/verifier-probe-verified.md",
};

const silentPath = join(here, ".tmp-verified-silent.md");
writeFileSync(silentPath, readFileSync(files.clean_verified, "utf8").replaceAll("arXiv:2409.99999", "the removed preprint"));
const targets = { ...files, clean_verified_silent: silentPath };

const out = {};
for (const [name, path] of Object.entries(targets)) {
  const text = readFileSync(path, "utf8");
  const r = await scoreCitations(text);
  out[name] = {
    path,
    citations: r.citations,
    citations_checked: r.citations_checked,
    citation_validity: r.citation_validity,
    title_match: r.title_match,
    unresolved: r.unresolved,
    title_mismatch: r.title_mismatch,
  };
  console.log(`${name}: cites=${r.citations} checked=${r.citations_checked} valid=${r.citation_validity} title=${r.title_match} unresolved=${JSON.stringify(r.unresolved)}`);
}
mkdirSync(here, { recursive: true });
writeFileSync(join(here, "verifier-output-score.json"), JSON.stringify(out, null, 2) + "\n");
