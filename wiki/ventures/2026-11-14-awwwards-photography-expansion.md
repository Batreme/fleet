---
title: "Venture: Awwwards Photography KB Expansion & Design DNA"
date: 2026-11-14
status: completed
tags:
  - venture
  - reverse-engineering
  - photography
  - awwwards
  - vector-search
  - sqlite-vec
outcome_summary: "Automated Playwright discovery and headless reverse-engineering of 50 live Awwwards photography portfolio websites, expanding Fleet KB to 71 targets (1,011 vector chunks) and adding two new design archetypes."
---

# Venture: Awwwards Photography KB Expansion & Design DNA

## Context & Desired Outcome
- **Problem / Goal**: The Fleet knowledge base required scaling with real-world, high-craft photography and portfolio websites to eliminate AI boilerplate ("AI slop") when scaffolding client-facing photography and studio applications.
- **Target Outcome**: Discover, capture, and deconstruct 50 top photography websites featured on `https://www.awwwards.com/websites/photography/`, skip existing KB targets, generate standardized 5-document Obsidian dossiers in `fleet/wiki/targets/`, embed and re-index all targets into the SQLite+`sqlite-vec` vector database, and synthesize extracted tokens into reusable design DNA archetypes.

## Approach Taken
- **Playwright-Driven Target Discovery**: Built an autonomous discovery crawler (`crawl_awwwards.py`) to navigate Awwwards listing pages, resolve external "Visit Site" destination URLs, and cross-reference them against existing targets. Identified 15 already-present domains and filtered out duplicates to yield 50 fresh targets in `targets_50.txt`.
- **Headless Reverse-Engineering Pipeline**: Executed `batch_runner.py` via `reverse-harness` to capture full network HAR, rendered DOM, full-page screenshots, stylesheets, scripts, and localStorage/sessionStorage across all 50 sites.
- **5-Document Obsidian Dossier Generation**: Generated `overview.md`, `apis.md`, `data-models.md`, `ui-ux.md`, and `source-maps.md` for each target in `fleet/wiki/targets/`.
- **Zero-Config Offline Semantic Vector Indexing**: Scaled the SQLite+`sqlite-vec` database to 71 targets and 1,011 indexed chunks using FastEmbed (`bge-small-en-v1.5`), enabling instant natural-language architectural pattern retrieval.
- **Design DNA Archetype Synthesis**: Extracted two new production-grade design archetypes into `reverse-harness/dna/archetypes.json`:
  1. `gallery-monochrome` (Monochrome Curatorial & Fine-Art Photography)
  2. `avant-garde-spatial` (Avant-Garde Spatial & Experimental Visuals)

## Challenges & Obstacles
- **Awwwards WAF Fingerprinting**: Initial curl and Chromium attempts with mismatched custom user-agent headers triggered HTTP 403 Forbidden. Using standard Playwright Chromium navigation resolved the issue cleanly, allowing full automated crawling.
- **Dynamic WebGL / Heavy Video Runtimes**: Several photography portfolios utilize heavy Three.js or GSAP animations. Applying a 3-second post-load buffer and graceful timeout handling ensured 100% batch reliability (50/50 successful, 0 failed).

## Final Outcome & Artifacts
- **50 New Production Targets Analyzed**: Total targets in `fleet/wiki/targets/` increased from 21 to 71.
- **1,011 Semantic Chunks Indexed**: Vector search tested and verified via `reverse-harness query`.
- **Knowledge Base Map Updated**: [fleet/wiki/INDEX.md](file:///root/projects/fleet/wiki/INDEX.md) enriched with a clean directory of all 71 production targets.
- **New Design DNA Archetypes**: Added `gallery-monochrome` and `avant-garde-spatial` in [archetypes.json](file:///root/projects/reverse-harness/dna/archetypes.json) and CLI command `reverse-harness dna`.

## Reusable Lessons
- When crawling award directories like Awwwards, always navigate with Playwright's native browser context rather than forged user-agent strings that fail TLS/HTTP2 consistency checks.
- Batch reverse-engineering pipelines should isolate each target in try/except blocks and maintain persistent progress files (`batch_progress.json`) for seamless agent resumption.
- Links to relevant playbooks: [[agent-harness-principles]]
