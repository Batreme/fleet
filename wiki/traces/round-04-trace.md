# Round 04 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-04`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `4` live (`6` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 04 Target Scope
  1. `altufanulu-com_en` — *Altufan Ulu Law Office · Istanbul Legal Counsel*
  2. `andreas-vision` — *Andreas Kruszakin, growth-focused design engineer in Europe*
  3. `anemone-mina-massoud-com` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  4. `annnimate-com` — *GSAP Motion Components for React & Vue · Annnimate*
  5. `anokhee-dev_albatross` — *Blocked (`Headless Preloader / Blank Viewport Capture (The Albatross The wind is steady. 6% or WASD to fly • M to mute Made b)`)*
  6. `apricode-agency` — *Blocked (`Live mobile behavioral capture failed (0 valid WebP frames)`)*
  7. `aqualoqa-com` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call log: - navigating to 'https://aqualoqa.com/', waiting until 'domcontentloaded' )`)*
  8. `arcteryx-com_us-en-explore-system0` — *System 0 · Arc’teryx*
  9. `armor-bd-com` — *Blocked (`Headless Preloader / Blank Viewport Capture (LOADING ARMOR EXPERIENCE)`)*
  10. `art-appstate-edu` — *Blocked (`Network/Navigation failure (Page.goto: net::ERR_EMPTY_RESPONSE at https://art.appstate.edu/ Call log: - navigating to 'https://art.appstate.edu/', waiting until 'domc)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `altufanulu-com_en` | `tier1_fast` | `1280×5796px` (461,814 B) | `390×2616px` (77,928 B) | 6 | 16 | 352 | 117 | `0.09` / `0.48` | **25.0 / 25.0** |
| `andreas-vision` | `tier1_fast` | `1280×6624px` (620,284 B) | `390×872px` (48,740 B) | 193 | 16 | 330 | 105 | `0.09` / `0.51` | **25.0 / 25.0** |
| `annnimate-com` | `tier1_fast` | `1280×828px` (39,342 B) | `390×2616px` (50,840 B) | 453 | 16 | 323 | 115 | `0.08` / `0.47` | **25.0 / 25.0** |
| `arcteryx-com_us-en-explore-system0` | `tier1_fast` | `1280×5796px` (305,442 B) | `390×872px` (2,422 B) | 245 | 16 | 336 | 110 | `0.09` / `0.51` | **25.0 / 25.0** |
| `anemone-mina-massoud-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `anokhee-dev_albatross` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (The Albatross The wind is`)** |
| `apricode-agency` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile behavioral capture failed (0 valid WebP frames)`)** |
| `aqualoqa-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call `)** |
| `armor-bd-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (LOADING ARMOR EXPERIENCE)`)** |
| `art-appstate-edu` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: net::ERR_EMPTY_RESPONSE at http`)** |
