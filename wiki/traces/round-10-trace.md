# Round 10 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-10`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 10 Target Scope
  1. `cue-onebranding-webflow-io` — *Cue - Creating Unforgettable Experiences*
  2. `daddyyankee-com` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  3. `daikifujita-com` — *Blocked (`Hard per-target capture deadline exceeded (160s)`)*
  4. `dailymoscow-ru_mirpay` — *Спорт без лишних действий — Mir Pay × Daily Moscow*
  5. `dairyfoodbg-com` — *Dairy Food Bulgaria — Private-Label UHT Dairy Manufacturer*
  6. `dark-moon-org` — *Darkmoon: Autonomous AI Penetration Testing Platform*
  7. `davaris-gr` — *Homepage - Davaris*
  8. `davidcata-com_en-musica` — *Music — “Queridos todos:” and “Origen”, by David Catá*
  9. `dcspaces-co-uk` — *Chorley Builders · Extensions & Renovations · DC Carpentry*
  10. `deadlyponies-com` — *Blocked (`Headless Preloader / Blank Viewport Capture (Loading availability...)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `cue-onebranding-webflow-io` | `tier1_fast` | `1280×6624px` (375,932 B) | `390×2616px` (75,354 B) | 14 | 16 | 354 | 117 | `0.12` / `0.55` | **25.0 / 25.0** |
| `dailymoscow-ru_mirpay` | `tier1_fast` | `1280×6624px` (388,932 B) | `390×2616px` (101,958 B) | 28 | 16 | 351 | 116 | `0.09` / `0.51` | **25.0 / 25.0** |
| `dairyfoodbg-com` | `tier1_fast` | `1280×6624px` (738,146 B) | `390×1744px` (11,414 B) | 167 | 16 | 342 | 112 | `0.12` / `0.55` | **25.0 / 25.0** |
| `dark-moon-org` | `tier1_fast` | `1280×6624px` (519,524 B) | `390×2616px` (54,036 B) | 384 | 16 | 347 | 112 | `0.11` / `0.49` | **25.0 / 25.0** |
| `davaris-gr` | `tier1_fast` | `1280×6624px` (422,628 B) | `390×2616px` (56,516 B) | 223 | 16 | 355 | 115 | `0.09` / `0.46` | **25.0 / 25.0** |
| `davidcata-com_en-musica` | `tier1_fast` | `1280×6624px` (338,122 B) | `390×2616px` (81,308 B) | 12 | 16 | 348 | 111 | `0.11` / `0.51` | **25.0 / 25.0** |
| `dcspaces-co-uk` | `tier1_fast` | `1280×6624px` (538,210 B) | `390×2616px` (88,452 B) | 29 | 16 | 365 | 120 | `0.09` / `0.50` | **25.0 / 25.0** |
| `daddyyankee-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `daikifujita-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (160s)`)** |
| `deadlyponies-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (Loading availability...)`)** |
