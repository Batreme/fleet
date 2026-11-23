---
title: "Venture: Multi-Category Awwwards Expansion & Qualitative Fleet Analysis"
date: 2026-11-14
status: completed
tags:
  - venture
  - reverse-engineering
  - multi-category
  - playbooks
  - anti-ai-slop
  - subagents
outcome_summary: "Expanded Fleet KB to 197 production targets across 7 major verticals, resolved memory bottlenecks via minimal HAR streaming, and deployed 3 specialized subagents authoring foundational production playbooks."
---

# Venture: Multi-Category Awwwards Expansion & Qualitative Fleet Analysis

## Context & Desired Outcome
- **Problem / Goal**: Following the successful photography reverse-engineering initiative, the user requested expanding Fleet's knowledge base across all primary Awwwards categories (20 targets per category). The goal was to eliminate generic AI boilerplate ("AI slop") across all web engineering domains: design agencies, e-commerce, architecture, fashion, experimental, and technology.
- **Target Outcome**: Discover, capture, and deconstruct 20 live websites per vertical, generate standardized 5-document Obsidian dossiers in `fleet/wiki/targets/`, scale the SQLite vector database, and deploy autonomous subagents to extract deep qualitative architectural patterns and author authoritative playbooks.

## Approach Taken
- **Multi-Category Ingestion Engine**: Developed `orchestrator_multi_category.py` to crawl Awwwards listings with cross-category deduplication, resolving direct live production URLs across verticals.
- **Parallel Headless Workers & Memory Bounding**: Ran parallel Playwright Chromium worker pools. When memory spikes occurred due to massive video/WebGL media payloads in HAR logs, engineered a 90% memory reduction by transitioning from `"record_har_content": "embed"` to `"record_har_mode": "minimal"`, dropping process memory from ~700MB+ to under 100MB.
- **Dossier Generation**: Created 5-document Obsidian dossiers (`overview.md`, `apis.md`, `data-models.md`, `ui-ux.md`, `source-maps.md`) for all captured properties, bringing the total knowledge base from 71 to **197 production targets**.
- **Specialized Qualitative Subagent Fleet**: Dispatched 3 autonomous domain analysts to inspect dossiers and author foundational engineering playbooks:
  1. **Agency & E-Commerce Analyst**: Authored [[agency-and-ecommerce-patterns]].
  2. **Architecture & Spatial Design Analyst**: Authored [[architectural-and-spatial-patterns]].
  3. **Technology & Experimental Systems Analyst**: Authored [[tech-and-experimental-patterns]].

## Challenges & Obstacles
- **Container Memory Limits (Cgroup OOM)**: Simultaneous execution of 3 Chromium instances on media-dense WebGL sites (e.g. `www-avilus-com` with 59MB HAR payload) triggered Linux OOM kills. Resolved by eliminating binary payload embedding in HAR files, bounding V8 old space (`--js-flags=--max-old-space-size=512`), and calling explicit garbage collection.
- **Dynamic Canvas & Infinite Scroll Stalls**: Several creative portfolio sites utilize infinite canvas height calculations that stalled full-page screenshots. Resolved with strict 8s screenshot timeouts and 50s per-target execution cutoffs.

## Final Outcome & Artifacts
- **197 Total Production Targets**: Cataloged and linked in [fleet/wiki/INDEX.md](../INDEX.md).
- **Three New Production Playbooks**:
  - [agency-and-ecommerce-patterns.md](../playbooks/agency-and-ecommerce-patterns.md): Headless Shop Pay v2 cart sync, Remix/Hydrogen edge architectures, CMU phonetic kinetic typography, and aspect-ratio lookbooks.
  - [architectural-and-spatial-patterns.md](../playbooks/architectural-and-spatial-patterns.md): Tectonic framing, viewport-derived grid math, chunked WebP sequence scrubbing, optical difference headers, and lifecycle statuses.
  - [tech-and-experimental-patterns.md](../playbooks/tech-and-experimental-patterns.md): Spatial cockpit layering (`z-index: 0/10/20`), PBR GLSL uniform pipelines, pitch-black/neon phosphor tokens, and telemetry HUD readouts.
- **Updated Knowledge Base MOC**: Registered all playbooks and 197 targets into `fleet/wiki/INDEX.md`.

## Reusable Lessons
- In Playwright reverse-engineering harnesses, never use `"record_har_content": "embed"` when crawling media-rich production sites—use `"record_har_mode": "minimal"` to extract API telemetry without exhausting RAM.
- Pair automated headless scrapers with specialized qualitative subagents: let headless tools handle asset gathering and AST extraction, and delegate synthesis and playbook authoring to autonomous LLM subagents.
- Links to relevant playbooks: [[agent-harness-principles]], [[agency-and-ecommerce-patterns]], [[architectural-and-spatial-patterns]], [[tech-and-experimental-patterns]]
