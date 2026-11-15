# Round 30 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-30`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 30 Target Scope
  1. `productionportugal-com` — *Production Portugal: Your trusted film production company in Portugal an...* (`https://productionportugal.com/`)
  2. `pyzhevsky-estate` — *Pyzhevsky — official website of a deluxe residence five minutes from the...* (`https://pyzhevsky.estate/`)
  3. `re-cycle-org` — *Re-Cycle · Changing Lives Through Bicycle Reuse* (`https://re-cycle.org/`)
  4. `realevate-agency` — *Realevate · Exceptional Real Estate Investments in Cyprus, Montenegro &...* (`https://realevate.agency/`)
  5. `reapi-ai_models-gpt-image-2-5` — *GPT Image 2.5 — Sharper Detail, Precise Editing* (`https://reapi.ai/models/gpt-image-2-5`)
  6. `recurziv-com` — *Recurziv — Web & App Development Studio in Goa* (`https://recurziv.com`)
  7. `reelmotion-fit` — *Reel Motion: Turn Workout Videos Into Exercise Routines* (`https://reelmotion.fit/`)
  8. `relevovinco-com` — *Relevo & Vinco — inkless packaging, pressed into the board* (`https://relevovinco.com/`)
  9. `residences-loamhouse-com-au` — *Loam House — Sandringham* (`https://residences.loamhouse.com.au`)
  10. `revelatio-studio` — *Revelatio · Branding, Product Design & Code* (`https://revelatio.studio/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `productionportugal-com` | `1440×7800px` (470,018 B) | `390×2400px` (153,239 B) | 23 | 16 | 258 | 107 | `0.15` / `0.58` | **25.0 / 25.0** |
| `pyzhevsky-estate` | `1440×2400px` (123,003 B) | `390×2400px` (43,192 B) | 484 | 16 | 256 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `re-cycle-org` | `1440×5863px` (2,328,922 B) | `390×2400px` (210,420 B) | 132 | 16 | 256 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
| `realevate-agency` | `1440×2400px` (788,835 B) | `390×2400px` (317,557 B) | 305 | 16 | 266 | 111 | `0.09` / `0.50` | **25.0 / 25.0** |
| `reapi-ai_models-gpt-image-2-5` | `1440×14542px` (2,757,094 B) | `390×2400px` (108,280 B) | 425 | 16 | 266 | 111 | `0.09` / `0.51` | **25.0 / 25.0** |
| `recurziv-com` | `1440×2400px` (463,604 B) | `390×2400px` (344,382 B) | 7 | 16 | 256 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `reelmotion-fit` | `1440×4938px` (1,086,767 B) | `390×2400px` (258,368 B) | 249 | 16 | 256 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `relevovinco-com` | `1440×2400px` (3,523,581 B) | `390×2400px` (1,289,861 B) | 29 | 16 | 256 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `residences-loamhouse-com-au` | `1440×9000px` (1,538,800 B) | `390×2400px` (66,835 B) | 17 | 16 | 256 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `revelatio-studio` | `1440×13959px` (1,338,441 B) | `390×2400px` (33,616 B) | 22 | 16 | 276 | 116 | `0.15` / `0.58` | **25.0 / 25.0** |
