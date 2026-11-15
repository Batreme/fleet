# Venture: UI Prompt Designer, Claude-Loop Review & Full 575-Target Blueprint Expansion

- **Date**: 2026-11-15
- **Status**: Completed (`VERDICT: APPROVE`, `24/25` on `claude-sonnet-5-5-high` across all 58 rounds; `25.0/25.0` deterministic `evaluate_batch.py --all` across all `556/556` analyzable targets, with `19` WAF/error captures marked `status: blocked`)
- **Branch**: `feat/ui-prompt-expansion`

## 1. Objective
Upgrade the entire Fleet Knowledge Base (`wiki/`) across all **575 cataloged web applications** (58 rounds of 10 targets) from raw technical extraction dossiers into actionable, zero-shot AI UI Prompt Blueprints (`prompt-blueprint.md`) paired with `1440px` desktop and `390px` mobile viewport captures (`assets/desktop.png`, `assets/mobile.png`), an automated truth, entropy & consistency evaluation suite (`evaluate_batch.py`, `C1`–`C14`), an Obsidian evaluation dashboard (`UI_EVALS_DASHBOARD.md`), 58 round execution traces (`traces/round-01-trace.md` .. `round-58-trace.md`), and an autonomous multi-round Anthropic review loop (`claude-loop`).

## 2. Key Deliverables
1. **New Skills (`skills/` & `.agents/skills/`)**:
   - `ui-prompt-designer`: 7-part design system & zero-shot prompt blueprint architecture grounded strictly in extracted CSS custom properties, `@media` breakpoints, `cubic-bezier()` transitions, real typographic scales, and verbatim DOM landmarks.
   - `claude-loop`: Multi-round autonomous verification loop using `claude-sonnet-5-5-high` on the native Swarm board (`C1, C2...` ledger until `VERDICT: APPROVE`).
2. **Full 575-Target Catalog Processed Across 58 Rounds (`wiki/targets/<slug>/`)**:
   - **556 Analyzable Production Targets**: Captured `1,112` verified PNG screenshots (`1440px` desktop `>= 40KB`, `390px` mobile `>= 30KB`, capped at `2400px` or full scroll height, with preloader curtains stripped and specimen sheets rendered for unhydrated WebGL `<canvas>` shells) and generated sanitized `ui-ux.md` and 7-part `prompt-blueprint.md` files (`94–116` line single unsplit fenced Master Prompts).
   - **19 Blocked / WAF-Gated Targets (`status: blocked`)**: Identified and honestly flagged the 19 targets whose raw captures terminated at an Akamai `Access Denied`, Cloudflare `Just a moment...`, Vercel `Security Checkpoint`, CloudFront `403`, HTTP `520`/`404`, or empty `39B` response, excluding them from the `25.0` tally with zero fabricated tokens (`C1`).
3. **Evaluation & Audit Infrastructure**:
   - `/root/projects/reverse-harness/evaluate_batch.py`: 14-check deterministic verification suite (`C1`–`C14`) scoring `25.0/25.0` across all `556/556` analyzable targets.
   - `/root/projects/reverse-harness/run_all_rounds.py` & `/root/projects/reverse-harness/build_full_dashboard.py`: Full-catalog ground-truth pipeline and dashboard generator.
   - [UI_EVALS_DASHBOARD](../UI_EVALS_DASHBOARD.md) & [round-01-trace](../traces/round-01-trace.md) .. [round-58-trace](../traces/round-58-trace.md): Complete 58-round audit trail and scorecard.

## 3. Lessons Learned
- **WAF / Anti-Bot Honesty (`C1`)**: Edge WAF block pages (`Access Denied`, `Checking your browser...`) must be detected and marked `status: blocked` rather than passed through token synthesis.
- **Preloader Curtain Stripping (`C2`)**: Many Awwwards/Webflow properties include fixed `.transition` / `.preloader` overlays or `opacity: 0` initial states that produce flat single-color PNGs unless explicitly neutralized during static DOM rendering.
- **Real Typographic Scale & Icon Font Filtering (`C3`, `C4`)**: Extracting heading/body scales from `:root` variables (`--real-h1`, `--h1`, `--h2`) and filtering out icon fonts (`webflow-icons`, `icomoon`, `FontAwesome`) prevents boilerplate scale strings and icon-font false positives.
- **Traceable Color Citations (`C5`)**: Every semantic color token in Section 3 must cite its exact `:root` variable (`var(--...)`) or `selector { property: value }` rule from the target's stylesheet.
