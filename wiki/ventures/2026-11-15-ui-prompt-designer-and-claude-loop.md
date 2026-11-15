# Venture: UI Prompt Designer, Claude-Loop Review & Batch 1 Blueprint Expansion

- **Date**: 2026-11-15
- **Status**: Completed (`VERDICT: APPROVE`, `24/25` on `claude-sonnet-5-5-high`; `25.0/25.0` deterministic `evaluate_batch.py`)
- **Branch**: `feat/ui-prompt-expansion`

## 1. Objective
Upgrade the Fleet Knowledge Base (`wiki/`) from raw technical extraction dossiers into actionable, zero-shot AI UI Prompt Blueprints (`prompt-blueprint.md`) paired with full-page desktop (`1440px`) and mobile (`390px`) visual captures (`assets/desktop.png`, `assets/mobile.png`), an automated truth & consistency evaluation suite (`evaluate_batch.py`), an Obsidian evaluation dashboard (`UI_EVALS_DASHBOARD.md`), and an autonomous multi-round Anthropic review loop (`claude-loop`).

## 2. Key Deliverables
1. **New Skills (`skills/` & `.agents/skills/`)**:
   - `ui-prompt-designer`: 7-part design system & zero-shot prompt blueprint architecture grounded strictly in extracted CSS custom properties, `@media` breakpoints, `cubic-bezier()` transitions, and real DOM landmarks.
   - `claude-loop`: Multi-round autonomous verification loop using `claude-sonnet-5-5-high` on the native Swarm board (`C1, C2...` ledger until `VERDICT: APPROVE`).
2. **Batch 1 Flagship Targets (10 Production Properties)**:
   - `dennypratama-com`, `agnestoth-com`, `www-sigma-imaging-se`, `morrow-valerian-studio`, `wiro-ae`, `www-anduril-com`, `www-avilus-com`, `www-eladiodieste-com`, `www-unimaticwatches-com`, and `seedjewelry-com`.
   - Captured 20 standard full-height PNG screenshots (`1440px` desktop, `390px` mobile) and sanitized all `ui-ux.md` and `prompt-blueprint.md` files (`239–263` lines each, with `94–105` line single unsplit fenced Master Prompts).
3. **Evaluation & Audit Infrastructure**:
   - `/root/projects/reverse-harness/evaluate_batch.py`: 13-check deterministic verification suite (`C1`–`C13`) scoring `25.0/25.0` across all 10 targets.
   - `[[UI_EVALS_DASHBOARD]]` & `[[traces/round-01-trace]]`: Full audit trail and scorecard.

## 3. Lessons Learned
- Raw CSS regex extraction on minified production bundles frequently captures trailing media query or class debris (`0}@media...`) unless explicitly split on `;` and `}` and filtered against `--tw-*` utility noise.
- Fenced Master Prompts in Section 7 must not contain inner triple-backtick code fences (` ```css `) so standard Markdown fence parsers extract the entire 95+ line prompt intact.
