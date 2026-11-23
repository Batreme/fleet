# Round 33 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-33`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 33 Target Scope
  1. `sibaldesign-com` — *Jeff Sibal — Visual & Digital Designer · SIBALDESIGN*
  2. `siglitos-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  3. `sincro-es_en-us` — *Us - Sincro*
  4. `sinedogma-com-tr` — *sinedogma*
  5. `sixescricket-com` — *Sixes Party Cricket · Let's Play · Nets & Simulator · Sixes Social Cricket*
  6. `skhiladze-com` — *Luka Skhiladze, motion designer and product engineer*
  7. `sleutelaar-xyz` — *Hans Sleutelaar · Officiële website*
  8. `sotz-org` — *Shout out to Zanzibar*
  9. `southandstonestudio-com` — *South & Stone Studio · Web Design & Brand Identity*
  10. `sparkle-ankatms-com` — *Kids Reward Chart & Chore App · Sparkle*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `sibaldesign-com` | `tier2_webgl` | `1440×900px` (273,482 B) | `390×844px` (119,741 B) | 28 | 16 | 294 | 112 | `0.09` / `0.52` | **25.0 / 25.0** |
| `sincro-es_en-us` | `tier1_fast` | `1440×2400px` (1,070,479 B) | `390×2400px` (251,737 B) | 133 | 16 | 284 | 107 | `0.09` / `0.48` | **25.0 / 25.0** |
| `sinedogma-com-tr` | `tier1_fast` | `1440×2400px` (372,578 B) | `390×2400px` (171,131 B) | 203 | 16 | 284 | 107 | `0.09` / `0.49` | **25.0 / 25.0** |
| `sixescricket-com` | `tier1_fast` | `1440×2400px` (952,420 B) | `390×2400px` (327,054 B) | 240 | 16 | 282 | 106 | `0.09` / `0.46` | **25.0 / 25.0** |
| `skhiladze-com` | `tier2_webgl` | `1440×900px` (106,253 B) | `390×844px` (69,958 B) | 36 | 16 | 286 | 108 | `0.09` / `0.52` | **25.0 / 25.0** |
| `sleutelaar-xyz` | `tier1_fast` | `1440×2400px` (263,818 B) | `390×2400px` (130,686 B) | 11 | 16 | 286 | 108 | `0.09` / `0.48` | **25.0 / 25.0** |
| `sotz-org` | `tier1_fast` | `1440×1064px` (1,038,850 B) | `390×844px` (152,059 B) | 13 | 16 | 282 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `southandstonestudio-com` | `tier1_fast` | `1440×2400px` (338,282 B) | `390×2400px` (190,185 B) | 117 | 16 | 296 | 113 | `0.09` / `0.47` | **25.0 / 25.0** |
| `sparkle-ankatms-com` | `tier1_fast` | `1440×2400px` (1,431,796 B) | `390×2400px` (446,334 B) | 31 | 16 | 300 | 115 | `0.09` / `0.48` | **25.0 / 25.0** |
| `siglitos-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
