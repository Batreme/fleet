# Venture: Agent Trace & Telemetry HUD (`trace-dashboard`)

- **Date**: 2026-11-16
- **Status**: Completed (Obsidian Darkmode HUD, Multi-View Left Rail, Grade 9.5/10 on Claude Sonnet 5.5 High)
- **Branch**: `feat/anthropic-trace-dashboard`
- **PR**: [Batreme/fleet#2](https://github.com/Batreme/fleet/pull/2)

## 1. Objective
Build an open, live developer observability control plane and telemetry dashboard inside Fleet to monitor Antigravity agent runs: per-prompt token streams (input, thinking, tool IO, and output), realistic dollar cost modeling, model ceilings and context saturation alerts, deep execution trace drawer with lazy-loaded reasoning and payloads, interactive Trace Flow Map (execution DAG), real-time live duration clocks, and live scoped Git diffs.

## 2. Key Deliverables
1. **New Skill (`skills/trace-dashboard/`)**:
   - `skills/trace-dashboard/SKILL.md`: Detailed capability and CLI reference.
   - `skills/trace-dashboard/scripts/trace-dashboard`: Zero-dependency, pure Python 3 standard library daemon (`ThreadingHTTPServer`) and CLI tool.
   - Symlinked to `.agents/skills/trace-dashboard`.
2. **Obsidian Darkmode Design System (HUD)**:
   - Modeled after elite design engineering targets from Fleet's Knowledge Base (Linear, Anduril, Vercel, Revelatio, Stripe).
   - Canvas: Pure Obsidian Black (`#060708`), deep slate panels (`#10141D`), elevated cards (`#161D2A`), hairline borders (`#1E2638`).
   - Accents: Electric Cyan / Sky (`#38BDF8`), Phosphor Emerald (`#10B981`) live status beacon, Telemetry Amber (`#F59E0B`), Alert Crimson (`#EF4444`), Electric Violet (`#A855F7`).
   - Pure SVG technical icons (1.5px stroke), zero emoji in UI chrome, full WCAG AA contrast.
3. **Multi-View Left Navigation Rail (`~220px`, collapsible to `64px`)**:
   - **Command Overview**: Fleet-wide KPIs, active working sessions grid with second-by-second live ticking duration clocks (`01:24:18`), model token allocation bar, top invoked tools histogram, and comprehensive historical sessions audit table.
   - **Traces Inspector (Dual-Pane)**: Searchable session selector drawer, turn-by-turn trace viewer with raw turn payload inspection (`<USER_REQUEST>`, `<ADDITIONAL_METADATA>`, `<USER_SETTINGS_CHANGE>`, `<CONTEXT_SUMMARY>`), 4-segment token breakdown progress bar, and System Prompt & Agent Config tab.
   - **Trace Flow Map & Execution DAG**: Interactive spatial execution graph connecting Prompts -> Reasoning -> Tools -> Files, with a turn scrubber (`All Turns Combined`, `Turn #1`...) and slide-over telemetry inspector drawer.
   - **Analytics & Performance Curves**: Context saturation trajectory, cumulative spend curve against model ceilings, and tool invocation frequency histogram.
4. **Server Hardening & Production Hygiene**:
   - `ThreadingHTTPServer` to handle high concurrency and large trace logs without blocking.
   - Robust `try/except` returning clean HTTP 500 on unexpected errors.
   - Strict route whitelist returning HTTP 404 for unknown endpoints.
   - Idempotent GET operations (zero file mutations on GET requests; explicit `/api/sync` endpoint for Markdown synchronization).
   - Safe directory traversal verification in `/api/step_output`.
5. **Two-Way Obsidian Sync**:
   - Real-time synchronization to `wiki/AGENT_TRACES_DASHBOARD.md`.

## 3. Lessons Learned
- **Pure Standard Library Feasibility**: A complete, reactive, multi-view developer tool can be built in pure Python standard library without npm, React, Tailwind, or bundling steps, maintaining total portable zero-dependency compliance.
- **GET Request Idempotency**: Decoupling markdown file synchronization from HTTP GET requests prevents dirty working trees during automated dashboard polling.
- **High-Craft UI Without AI-Slop**: Avoiding emoji-heavy UI chrome in favor of precision 1.5px stroke inline SVGs elevates the developer tool into an industrial, mission-critical HUD.
