# Round 10 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-10`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 10 Target Scope
  1. `cue-onebranding-webflow-io` — *Cue - Creating Unforgettable Experiences*
  2. `daddyyankee-com` — *Daddy Yankee · Official Website*
  3. `daikifujita-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  4. `dailymoscow-ru_mirpay` — *Спорт без лишних действий — Mir Pay × Daily Moscow*
  5. `dairyfoodbg-com` — *Dairy Food Bulgaria — Private-Label UHT Dairy Manufacturer*
  6. `dark-moon-org` — *Darkmoon: Autonomous AI Penetration Testing Platform*
  7. `davaris-gr` — *Homepage - Davaris*
  8. `davidcata-com_en-musica` — *Music — “Queridos todos:” and “Origen”, by David Catá*
  9. `dcspaces-co-uk` — *Chorley Builders · Extensions & Renovations · DC Carpentry*
  10. `deadlyponies-com` — *Deadly Ponies - Luxury Leather Bags & Accessories*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `cue-onebranding-webflow-io` | `tier1_fast` | `1440×2400px` (469,080 B) | `390×2400px` (340,624 B) | 14 | 16 | 296 | 113 | `0.16` / `0.56` | **25.0 / 25.0** |
| `daddyyankee-com` | `tier1_fast` | `1440×2400px` (1,714,036 B) | `390×2400px` (320,592 B) | 101 | 16 | 282 | 106 | `0.16` / `0.56` | **25.0 / 25.0** |
| `dailymoscow-ru_mirpay` | `tier1_fast` | `1440×2400px` (1,083,281 B) | `390×2400px` (423,576 B) | 22 | 16 | 300 | 115 | `0.10` / `0.51` | **25.0 / 25.0** |
| `dairyfoodbg-com` | `tier1_fast` | `1440×2400px` (1,358,819 B) | `390×2400px` (337,261 B) | 167 | 16 | 284 | 107 | `0.14` / `0.56` | **25.0 / 25.0** |
| `dark-moon-org` | `tier1_fast` | `1440×2400px` (698,545 B) | `390×2400px` (219,441 B) | 387 | 16 | 280 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `davaris-gr` | `tier1_fast` | `1440×2400px` (1,061,290 B) | `390×2400px` (61,617 B) | 223 | 16 | 290 | 110 | `0.09` / `0.45` | **25.0 / 25.0** |
| `davidcata-com_en-musica` | `tier1_fast` | `1440×2400px` (1,529,515 B) | `390×2400px` (515,736 B) | 12 | 16 | 284 | 107 | `0.09` / `0.51` | **25.0 / 25.0** |
| `dcspaces-co-uk` | `tier1_fast` | `1440×2400px` (1,675,605 B) | `390×2400px` (375,568 B) | 29 | 16 | 298 | 114 | `0.10` / `0.51` | **25.0 / 25.0** |
| `deadlyponies-com` | `tier1_fast` | `1440×2400px` (1,732,302 B) | `390×2400px` (679,076 B) | 33 | 16 | 290 | 110 | `0.09` / `0.49` | **25.0 / 25.0** |
| `daikifujita-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
