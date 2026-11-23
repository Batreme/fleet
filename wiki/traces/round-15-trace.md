# Round 15 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-15`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 15 Target Scope
  1. `fitosauna-com` — *Blocked (`Upstream HTTP 520 — Cloudflare Origin/WAF Error`)*
  2. `flycrooked-com` — *Crow · Trip planner and flight finder for iPhone*
  3. `fondation-canadiens-com` — *Montreal Canadiens Children's Foundation - Play to thrive*
  4. `fontsight-xyz` — *Fontsight: What Font Is That? Font Finder for Chrome*
  5. `forgeautomotive-co-uk` — *Blocked (`Headless Preloader / Blank Viewport Capture (cannot hydrate without interactive/GPU session)`)*
  6. `foxvaluations-com-au` — *Property valuations Brisbane · Fox Valuations*
  7. `fromearth-love` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  8. `gallery-play-be` — *Home - Gallery Play*
  9. `giallostudio-it_en-the-experience` — *The Experience: Milan lights up in yellow · Giallo*
  10. `giga-ai` — *Giga: AI support agents that improve your metrics*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `flycrooked-com` | `tier1_fast` | `1440×2400px` (910,426 B) | `390×2400px` (348,740 B) | 61 | 16 | 306 | 118 | `0.09` / `0.50` | **25.0 / 25.0** |
| `fondation-canadiens-com` | `tier1_fast` | `1440×2400px` (1,063,571 B) | `390×2400px` (615,789 B) | 190 | 16 | 282 | 106 | `0.12` / `0.45` | **25.0 / 25.0** |
| `fontsight-xyz` | `tier1_fast` | `1440×2400px` (268,069 B) | `390×2400px` (152,820 B) | 42 | 16 | 300 | 115 | `0.08` / `0.50` | **25.0 / 25.0** |
| `foxvaluations-com-au` | `tier1_fast` | `1440×2400px` (972,518 B) | `390×2400px` (462,258 B) | 29 | 16 | 302 | 116 | `0.08` / `0.50` | **25.0 / 25.0** |
| `gallery-play-be` | `tier1_fast` | `1440×2400px` (1,245,671 B) | `390×2400px` (376,656 B) | 182 | 16 | 282 | 106 | `0.09` / `0.46` | **25.0 / 25.0** |
| `giallostudio-it_en-the-experience` | `tier1_fast` | `1440×2400px` (351,652 B) | `390×2400px` (157,378 B) | 118 | 16 | 288 | 109 | `0.12` / `0.47` | **25.0 / 25.0** |
| `giga-ai` | `tier1_fast` | `1440×900px` (966,729 B) | `390×2400px` (487,151 B) | 1064 | 16 | 288 | 109 | `0.09` / `0.48` | **25.0 / 25.0** |
| `fitosauna-com` | `blocked` (`520`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 520 — Cloudflare Origin/WAF Error`)** |
| `forgeautomotive-co-uk` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (cannot hydrate without in`)** |
| `fromearth-love` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
