---
title: "Venture: Reverse-Harness & Fleet Integration"
date: 2026-10-31
status: completed
tags:
  - venture
  - reverse-engineering
  - harness
  - obsidian
  - vector-search
outcome_summary: "Built and verified the standalone reverse-harness engine alongside Fleet with automated web capture, SQLite+sqlite-vec pattern search, upstream reverse-skill submodule, and Obsidian dossier sync."
---

# Venture: Reverse-Harness & Fleet Integration

## Context & Desired Outcome
- **Problem / Goal**: AI-generated applications often suffer from "AI slop"—generic, simplistic CRUD boilerplate that fails to reflect real-world domain nuances, optimistic UX states, or robust schema design. We needed a reverse-engineering harness capable of inspecting production web applications (and general security targets from `zhaoxuya520/reverse-skill`), extracting their APIs, data models, and design tokens, and indexing them for fast semantic search.
- **Target Outcome**: A standalone repository (`../reverse-harness`) that manages web capture and vector search, paired with an Obsidian-canonical dossier library in `fleet/wiki/targets/` and a declarative skill in `fleet/skills/reverse-engineer/SKILL.md`.

## Approach Taken
- **Boundary Separation**: Kept `fleet` strictly as a lightweight skills and knowledge harness; created `../reverse-harness` as an independent Git repository managed via `uv`.
- **Upstream Submodule**: Linked `https://github.com/zhaoxuya520/reverse-skill` as a git submodule under `upstream/reverse-skill` to retain full access to its 45+ security routing rules (`R0-R45`).
- **Dual-Layer Automation**: Built a Typer CLI (`reverse-harness`) with Playwright headless capture + CDP network logging (HAR), DOM extraction, and storage dumps.
- **Obsidian-Canonical Knowledge Base**: Generated a 5-document dossier (`overview.md`, `apis.md`, `data-models.md`, `ui-ux.md`, `source-maps.md`) in `fleet/wiki/targets/<app-name>/`.
- **Offline Vector Engine**: Embedded `sqlite-vec` directly in SQLite alongside local embeddings (`fastembed` with `bge-small-en-v1.5`), providing zero-config, 100% offline semantic search across production patterns.

## Challenges & Obstacles
- **macOS SQLite Extension Authorization**: Standard macOS Python `sqlite3` disables extension loading by default, throwing `sqlite3.OperationalError: not authorized`. Resolved by calling `conn.enable_load_extension(True)` prior to loading `sqlite_vec`.
- **Large Model / Browser Assets**: Playwright Chromium and FastEmbed ONNX weights were installed and verified cleanly.

## Final Outcome & Artifacts
- Initialized and tested repository: `../reverse-harness`.
- Created Fleet skill: `fleet/skills/reverse-engineer/SKILL.md`.
- Added target template: `fleet/wiki/templates/target-template.md`.
- Updated `fleet/wiki/INDEX.md` and `fleet/README.md`.
- Smoke-tested live capture, analysis, indexing, and semantic search on a sample target (`example-app`).

## Reusable Lessons
- Use SQLite with `sqlite-vec` when pairing Obsidian vaults with AI agent search: it keeps the human-readable Markdown vault as the single source of truth while giving agents sub-second semantic retrieval.
- Links to relevant playbooks: [[agent-harness-principles]]
