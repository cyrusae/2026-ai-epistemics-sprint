import { mkdtempSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

import { registerResearchTelemetry } from "/tmp/feynman-src/extensions/research-tools/telemetry.ts";

const SECRET = "PATIENT_ZERO_SECRET";
const captured: Array<{ event: string; properties: Record<string, unknown> }> = [];

const handlers = new Map<string, Array<(event: any, ctx: any) => unknown>>();
const pi = {
  on(event: string, handler: (event: any, ctx: any) => unknown) {
    handlers.set(event, [...(handlers.get(event) ?? []), handler]);
  },
} as any;

const client = {
  capture(message: { event: string; properties: Record<string, unknown> }) {
    captured.push(message);
  },
  async flush() {},
  async shutdown() {},
} as any;

const env = {
  FEYNMAN_POSTHOG_KEY: "phc_test",
  FEYNMAN_POSTHOG_HOST: "https://posthog.test",
  FEYNMAN_TELEMETRY_DISTINCT_ID: "feynman_test-install",
};

const cwd = mkdtempSync(join(tmpdir(), "feynman-leak-probe-"));
const ctx = {
  cwd,
  mode: "print",
  model: { provider: "test", id: "test-model" },
  sessionManager: { getSessionId: () => "session-leak-probe" },
};

registerResearchTelemetry(pi, { env, shared: {}, createClient: () => client });

async function emit(event: any) {
  for (const handler of handlers.get(event.type) ?? []) await handler(event, ctx);
}

await emit({ type: "session_start", reason: "startup" });
await emit({ type: "agent_start" });
await emit({
  type: "tool_execution_end",
  toolCallId: "t1",
  toolName: "fetch_content",
  isError: true,
  result: {
    content: [
      {
        type: "text",
        text: `Invalid URL: https://example.test/?q=${SECRET}&prompt=summarize+the+patient+record`,
      },
    ],
  },
});
await emit({ type: "session_shutdown", reason: "quit" });

const serialized = JSON.stringify(captured);
const leaked = serialized.includes(SECRET);
const report = {
  secret: SECRET,
  leaked,
  capturedEvents: captured.map((entry) => entry.event),
  toolEvent: captured.find((entry) => entry.event === "feynman_tool_used") ?? null,
};
writeFileSync(join(cwd, "telemetry-error-leak-report.json"), JSON.stringify(report, null, 2));
console.log(JSON.stringify(report, null, 2));
process.exit(leaked ? 1 : 0);
