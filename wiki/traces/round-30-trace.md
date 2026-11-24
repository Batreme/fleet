# Round 30 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-30`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 30 Target Scope
  1. `productionportugal-com` — *Production Portugal: Your trusted film production company in Portugal an...*
  2. `pyzhevsky-estate` — *Pyzhevsky — official website of a deluxe residence five minutes from the...*
  3. `re-cycle-org` — *Re-Cycle · Changing Lives Through Bicycle Reuse*
  4. `realevate-agency` — *Realevate · Exceptional Real Estate Investments in Cyprus, Montenegro &...*
  5. `reapi-ai_models-gpt-image-2-5` — *GPT Image 2.5 — Sharper Detail, Precise Editing*
  6. `recurziv-com` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call log: - navigating to 'https://recurziv.com/', waiting until 'domcontentloaded' )`)*
  7. `reelmotion-fit` — *Reel Motion: Turn Workout Videos Into Exercise Routines*
  8. `relevovinco-com` — *Relevo & Vinco — inkless packaging, pressed into the board*
  9. `residences-loamhouse-com-au` — *Loam House — Sandringham*
  10. `revelatio-studio` — *Blocked (`Live mobile behavioral capture failed (0 valid WebP frames)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `productionportugal-com` | `tier1_fast` | `1280×6624px` (623,428 B) | `390×2616px` (70,804 B) | 24 | 16 | 350 | 115 | `0.10` / `0.50` | **25.0 / 25.0** |
| `pyzhevsky-estate` | `tier1_fast` | `1280×6624px` (725,192 B) | `390×872px` (3,134 B) | 484 | 16 | 336 | 111 | `0.09` / `0.50` | **25.0 / 25.0** |
| `re-cycle-org` | `tier1_fast` | `1280×5796px` (526,160 B) | `390×2616px` (97,562 B) | 178 | 16 | 358 | 117 | `0.08` / `0.47` | **25.0 / 25.0** |
| `realevate-agency` | `tier1_fast` | `1280×2484px` (152,306 B) | `390×872px` (5,984 B) | 305 | 16 | 344 | 118 | `0.08` / `0.50` | **25.0 / 25.0** |
| `reapi-ai_models-gpt-image-2-5` | `tier1_fast` | `1280×6624px` (458,348 B) | `390×2616px` (100,328 B) | 426 | 16 | 338 | 115 | `0.09` / `0.47` | **25.0 / 25.0** |
| `reelmotion-fit` | `tier1_fast` | `1280×4968px` (176,942 B) | `390×2616px` (63,968 B) | 249 | 16 | 351 | 120 | `0.08` / `0.49` | **25.0 / 25.0** |
| `relevovinco-com` | `tier1_fast` | `1280×6624px` (1,025,414 B) | `390×2616px` (177,202 B) | 29 | 16 | 342 | 113 | `0.10` / `0.50` | **25.0 / 25.0** |
| `residences-loamhouse-com-au` | `tier1_fast` | `1280×6624px` (434,728 B) | `390×2616px` (77,988 B) | 17 | 16 | 345 | 114 | `0.10` / `0.50` | **25.0 / 25.0** |
| `recurziv-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call `)** |
| `revelatio-studio` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile behavioral capture failed (0 valid WebP frames)`)** |
