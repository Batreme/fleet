---
title: "Full Top-to-Bottom Behavioral Journey Crawl & WebP Migration (575 Targets)"
date: 2026-11-23
status: completed
branch: feat/full-behavioral-journey-webp
repositories:
  - Batreme/reverse-harness
  - Batreme/fleet
---

# Venture: Full Top-to-Bottom Behavioral Journey Crawl & WebP Migration (`behavioral_journey_v2`)

## Goal
Upgrade the entire 575-target reverse-engineering catalog from static top-fold PNG screenshots to full top-to-bottom behavioral journey documentation (`Q1`–`Q14` specification):
- **Dual-Mode Scroll Driver**: Native incremental scrolling (`~850px` steps up to true footer or `14,400px` cap) with automatic mid-scroll fallback to real `mouse.wheel` + `ArrowDown` bursts (`native+wheel`) for Lenis / GSAP / WebGL scroll-jacked sites on both desktop and mobile.
- **Full WebP (`q=82`) Migration**: Up to 8 visually deduplicated desktop keyframes (`1440×900`) stitched into a labeled vertical filmstrip (`desktop-journey.webp`, `1280px` wide), 3-frame mobile journey (`mobile-journey.webp`, `390px` wide), up to 3 internal subpage filmstrips (`subpage-*.webp`), and zero legacy `.png` assets.
- **Safe Non-Destructive UI Probing**: Nav/drawer toggle (`state-nav.webp` with verified Escape/toggle close), hover CSS computed diffs on primary CTA & cards, interactive tab/accordion/carousel probes (`state-interactive.webp`), and SPA vs. MPA navigation transition telemetry.
- **Unified Blueprint Documentation**: Enriched Sections 5–7 (with real URL paths and clean typography hierarchy) plus **Section 8: Full-Page Scroll Journey, Interactive States & Subpage Inventory** in every `prompt-blueprint.md`.
- **Q11-A Scope**: Run across all 494 previously-live targets + retry all 58 `capture-incomplete` sites (552 targets), keeping the 23 dead/WAF `site-blocked` sites strictly untouched.

## Execution, Regressions & `claude-loop` Remediation
1. **Pipeline Implementation (`reverse-harness`)**: Implemented `src/reverse_harness/behavioral_capture.py` and integrated `behavioral_journey_v2` into `run_all_rounds.py`, `evaluate_batch.py`, `verify_visual_catalog.py`, `build_full_dashboard.py`, and `tests/test_catalog_integrity.py`. Passed the 5-site sanity gate (`5/5` at `25.0/25.0`).
2. **Full Sharded Crawl & Interrupted-Run Resume**: Initial 3-shard crawl was interrupted by a host reboot at ~21% (`118/552`). Resumed cleanly across 2 disjoint shards (`--shard 1/2`, `--shard 2/2`) plus an 82-target single-worker `--retry-extended` pass (`220s` deadline), reaching `467` live targets (`+7` recovered from the Q11-A `capture-incomplete` set).
3. **`claude-loop` Round 1 (`VERDICT: CHANGES`, `20/25`) & C1–C12 Remediation**:
   - **C1**: Added mid-scroll `native → native+wheel` fallback (`should_fallback_to_wheel_mid_scroll`) on desktop and wheel fallback on mobile; re-crawled all 83 shallow tall targets + 34 regressed targets + `hopecancerresources-org` (118 targets), cutting shallow `<60%` tall captures by **60%** (`83 → 33`, e.g., `labellavista-es`, `serus-ai`, `sparkle-ankatms-com`, `www-3d-discovery-fr`, `www-incroy-com`, `www-norddeutscher-figuralchor-de`, `diversify-nz`).
   - **C2**: Added `check_behavioral_scroll_coverage` to both `evaluate_batch.py` and `verify_visual_catalog.py` so remaining shallow captures (33 sites) are transparently surfaced as warnings instead of hidden.
   - **C3 (Honest Regression Disclosure)**: Moving from single-frame top-fold captures to full multi-step desktop + mobile behavioral journeys + subpages tightened validity gates (requiring valid desktop keyframes, valid mobile WebP frames, non-blank/non-preloader viewports, and real DOM content). Relative to the prior `494` live / `81` blocked baseline, this campaign yields **`435` live `behavioral_journey_v2` targets** (`+7` Q11-A recoveries, net `-59` where sites failed full mobile/desktop behavioral capture, hit headless preloaders like `armor-bd-com` / `kingriver-com-au`, or returned empty DOM / 30s timeouts) and **`140` `status: blocked` targets** (`65` `site-blocked` + `75` `capture-incomplete`, `140/140` `C15`-clean with zero stray assets and zero fabricated frames).
   - **C4–C12**: Fixed real `urlparse(url).path` route emission across all 435 blueprints, updated `claude-loop-ledger.json` & dashboard status, filtered empty/stub subpages (`hopecancerresources-org` cleanly dropped `/home/shop/` stub), added desktop/mobile sub-budgets, verified nav close after Escape, expanded `SKIP_ROUTE_RE` + `SKIP_QUERY_RE`, filtered generic `#section-N` landmark IDs, fixed single-family font pairing text, and removed unused `hashlib`.

## Final Verified Outcome
- **Total Catalog Audited**: `575 / 575` across `58` rounds.
- **Live Analyzed (`behavioral_journey_v2`)**: **`435 / 435` at `25.0 / 25.0`** (`0` synthetic specimens, `0` duplicate hashes, `0` legacy `.png` files; `407` `tier1_fast`, `28` `tier2_webgl`).
- **Non-Analyzed (`status: blocked`, C15-Clean)**: `140 / 140` clean (`65` `site-blocked` + `75` `capture-incomplete`, strictly zero WAF/CAPTCHA bypasses and zero stray assets).
- **Automated Verification**: `evaluate_batch.py --all --strict` EXIT 0, `verify_visual_catalog.py --all --strict` EXIT 0 (`400` pass, `35` warn [33 shallow coverage + 2 preloader-text], `0` fail), `unittest` **`17/17 OK`**.
- **Dashboard & Traces**: Regenerated [UI_EVALS_DASHBOARD](../UI_EVALS_DASHBOARD.md), [INDEX](../INDEX.md), and all 58 round traces (`round-01-trace.md` .. `round-58-trace.md`).
