---
title: "Venture: Fleet Harness Setup & Skill Migration"
date: 2026-10-31
status: completed
tags:
  - venture
  - agent-harness
  - tstack
  - agy
outcome_summary: "Established a zero-dependency agent skills harness based on tstack and mattpocock/skills."
---

# Venture: Fleet Harness Setup & Skill Migration

## Context & Desired Outcome
- **Problem / Goal**: Establish a dedicated harness repository for AI coding agents (Antigravity `agy`, Claude Code, Codex) without application bloat.
- **Target Outcome**: A clean, KISS-compliant repository containing reusable skills and a knowledge base to guide future agent work.

## Approach Taken
- Initially considered a Python runner wrapper, but pivoted to native markdown skills based on the [`tstack`](https://github.com/t3dotgg/tstack) pattern.
- Installed `grill-me` and `grilling` from `mattpocock/skills`.
- Cloned PR and agent coordination skills from `t3dotgg/tstack` (`full-send`, `full-stop`, `council`, `sol-loop`, `file-pr`, `babysit-pr`, `takeover`, `modernize`, `leaving-pr-comments`).
- Created an Obsidian-compatible Markdown knowledge base (`wiki/`) for venture recording and playbooks.

## Challenges & Obstacles
- Over-engineered a custom CLI runner in Python initially; user clarified they wanted native skills like `tstack`. Cleaned up the extra code promptly.
- Initial `skills add` command copied 38 skills; pruned to only the requested `grill-me` and `grilling` skills.

## Final Outcome & Artifacts
- Minimalist, production-ready skills harness in `skills/`.
- Symlinked `.agents/skills` for seamless Antigravity compatibility.
- Obsidian-compatible knowledge base under `wiki/`.

## Reusable Lessons
- Follow [[agent-harness-principles]]: Rely on the agent runtime's native skill resolution rather than wrapping everything in external runners.
