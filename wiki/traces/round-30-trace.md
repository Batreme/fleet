# Round 30 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-30`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 30 Target Scope
  1. `productionportugal-com` — *Production Portugal: Your trusted film production company in Portugal an...*
  2. `pyzhevsky-estate` — *Pyzhevsky — official website of a deluxe residence five minutes from the...*
  3. `re-cycle-org` — *Re-Cycle · Changing Lives Through Bicycle Reuse*
  4. `realevate-agency` — *Realevate · Exceptional Real Estate Investments in Cyprus, Montenegro &...*
  5. `reapi-ai_models-gpt-image-2-5` — *GPT Image 2.5 — Sharper Detail, Precise Editing*
  6. `recurziv-com` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 35000ms exceeded. Call log: - navigating to 'https://recurziv.com/', waiting until 'domcontentloaded' )`)*
  7. `reelmotion-fit` — *Reel Motion: Turn Workout Videos Into Exercise Routines*
  8. `relevovinco-com` — *Relevo & Vinco — inkless packaging, pressed into the board*
  9. `residences-loamhouse-com-au` — *Loam House — Sandringham*
  10. `revelatio-studio` — *Revelatio · Branding, Product Design & Code*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `productionportugal-com` | `tier1_fast` | `1440×2400px` (860,700 B) | `390×2400px` (291,250 B) | 23 | 16 | 292 | 111 | `0.14` / `0.62` | **25.0 / 25.0** |
| `pyzhevsky-estate` | `tier1_fast` | `1440×900px` (737,997 B) | `390×844px` (298,548 B) | 484 | 16 | 284 | 107 | `0.08` / `0.50` | **25.0 / 25.0** |
| `re-cycle-org` | `tier1_fast` | `1440×2400px` (2,229,150 B) | `390×2400px` (636,157 B) | 132 | 16 | 296 | 113 | `0.09` / `0.47` | **25.0 / 25.0** |
| `realevate-agency` | `tier1_fast` | `1440×900px` (156,849 B) | `390×844px` (79,200 B) | 305 | 16 | 298 | 114 | `0.08` / `0.49` | **25.0 / 25.0** |
| `reapi-ai_models-gpt-image-2-5` | `tier2_webgl` | `1440×900px` (217,466 B) | `390×844px` (70,793 B) | 363 | 16 | 292 | 111 | `0.08` / `0.48` | **25.0 / 25.0** |
| `reelmotion-fit` | `tier1_fast` | `1440×2400px` (1,037,638 B) | `390×2400px` (397,824 B) | 249 | 16 | 300 | 115 | `0.09` / `0.47` | **25.0 / 25.0** |
| `relevovinco-com` | `tier1_fast` | `1440×2400px` (2,037,391 B) | `390×2400px` (793,639 B) | 29 | 16 | 288 | 109 | `0.10` / `0.49` | **25.0 / 25.0** |
| `residences-loamhouse-com-au` | `tier1_fast` | `1440×2400px` (1,481,718 B) | `390×2400px` (448,147 B) | 17 | 16 | 288 | 109 | `0.10` / `0.49` | **25.0 / 25.0** |
| `revelatio-studio` | `tier2_webgl` | `1440×900px` (11,994 B) | `390×2400px` (31,140 B) | 22 | 16 | 282 | 106 | `0.14` / `0.62` | **25.0 / 25.0** |
| `recurziv-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 35000ms exceeded. Call `)** |
