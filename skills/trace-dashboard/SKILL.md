---
name: trace-dashboard
description: Inspect live agent traces, per-prompt token usage (input, thinking, tool calls, output, cumulative context), and active models/subagents across Antigravity conversations. Trigger when the user says 'trace dashboard', 'token dashboard', or 'open dashboard'.
---

# Agent Trace, Token & Dollar Cost Telemetry Dashboard (`trace-dashboard`)

A precision multi-view telemetry engine and agent control plane for Antigravity, modeled after modern high-craft design engineering targets (Linear, Anduril, Vercel, Revelatio, Peaches, Vadim Carazan) from Fleet's Knowledge Base.

Directly ingests local execution streams from `~/.gemini/antigravity-cli/brain/` and `~/.gemini/antigravity-cli/conversations/` to provide real-time token tracking, dollar cost modeling, context window saturation gauges, step-level trace inspection, full system prompt architecture exploration, interactive execution DAG flow mapping, and live Git diffs.

## Multi-View Architecture (Left Navigation Rail)

The dashboard features a persistent left navigation rail (`~220px` width, collapsible to 64px icon-rail mode) dividing the telemetry into 4 specialized views:

1. **Command Overview**:
   - Fleet-wide telemetry cards: Active Running Workers, Cumulative Spend, Token Volume, Total Steps, and Tracked Repositories.
   - **Active & Working Sessions Grid**: Real-time second-by-second ticking duration clocks (`01:24:18`), pulsing emerald status beacons, current model pill, last invoked tool, and 1-click jump buttons (`Inspect Traces ->`, `View Flow Map ->`).
   - Embedded SVG charts for Model Token Allocation and Top Invoked Tools.
   - Comprehensive historical sessions audit table with sorting and filtering.

2. **Traces Inspector (Dual-Pane)**:
   - Integrated collapsible session selector list on the left with instant search filtering.
   - Deep turn-by-turn trace drawer: user prompt, active model badge with model-switch notifications, raw payload drawer (`<USER_REQUEST>`, `<ADDITIONAL_METADATA>`, `<USER_SETTINGS_CHANGE>`, `<CONTEXT_SUMMARY>`), 4-segment token breakdown progress bar, and execution step drawer with terminal `$ cmd` formatting.
   - **System Prompt & Agent Config Inspector**: Agent Identity, parsed rules from `AGENTS.md`, installed skills catalog, subagents roster, native and MCP tool registries, and full reconstructed prompt stream with 1-click copy.
   - Scoped unified Git diffs with line gutters and untracked file detection.
   - Provider rate cards matrix.

3. **Trace Flow Map & Execution DAG**:
   - Interactive spatial execution graph mapping:
     `[User Prompt Node]` -> `[Agent Reasoning Thought]` -> `[Tool Execution Pipeline]` -> `[Response / File Artifacts]`
   - Top Turn Scrubber: Filter between `All Turns Combined` or individual turns (`Turn #1`, `Turn #2`...).
   - Node category color coding:
     - **Shell Execution** (`run_command`) — Electric Cyan
     - **Filesystem Mutations** (`write_file`, `edit_file`) — Phosphor Emerald
     - **Filesystem Reads** (`read_file`) — Slate
     - **Agent Spawning & Swarm** (`invoke_subagent`, `swarm`) — Electric Violet
     - **External MCP Servers** (`gemini_search_docs`, `gemini_get_doc`) — Amber
   - Slide-over telemetry inspector drawer: Clicking any node opens a right drawer with arguments, latency, and stdout.

4. **Analytics & Charts**:
   - Selected session context saturation trajectory and cumulative spend curve against model ceilings.
   - Tool invocation frequency histogram across all sessions.
   - Model pricing and rate limits matrix.

## Visual Design System: Obsidian Telemetry HUD

- **Substrate**: Pure Obsidian Black (`#060708`), deep slate panels (`#10141D`), elevated cards (`#161D2A`), hairline borders (`#1E2638`).
- **Accents**: Electric Cyan / Sky (`#38BDF8`), Phosphor Emerald (`#10B981`) live beacon, Telemetry Amber (`#F59E0B`), Alert Crimson (`#EF4444`), Electric Violet (`#A855F7`).
- **Typography**: Modern geometric sans (`Inter`, `-apple-system`) with tabular monospace numerals (`JetBrains Mono`).

## CLI Usage

### Update Obsidian Markdown Dashboard & Open in Obsidian
```bash
python3 skills/trace-dashboard/scripts/trace-dashboard --sync --open-obsidian
```

### Launch Live Web Dashboard
```bash
python3 skills/trace-dashboard/scripts/trace-dashboard --serve --port 8765
```

### Output Traces as JSON
```bash
python3 skills/trace-dashboard/scripts/trace-dashboard --json
```
