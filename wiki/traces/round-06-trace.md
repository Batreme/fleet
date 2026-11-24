# Round 06 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-06`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 06 Target Scope
  1. `b3xgraphics-com` — *B3X Graphics · Freelance Sports Art Director & Designer*
  2. `baboonbutts-com` — *Baboon Butts - The redder the better!*
  3. `bar-topas-ch` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  4. `baztan-race-com` — *Baztan Race*
  5. `bb-b-net` — *Agence de Communication b2b et Marketing Industriel- bb&b*
  6. `bcgbuildingdesign-com-au` — *Building Designer Gold Coast · BCG Building Design*
  7. `becore-se` — *Becore*
  8. `belgradearbor-rs_en` — *Belgrade Arbor · Residential & Business Complex in New Belgrade*
  9. `bennos-light-org` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call log: - navigating to 'https://bennos-light.org/', waiting until 'domcontentloaded' )`)*
  10. `bespokegroup-io` — *Bespoke Group · Private Wealth & Estate Planning Advisory*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `b3xgraphics-com` | `tier1_fast` | `1280×4968px` (392,328 B) | `390×2616px` (94,070 B) | 192 | 16 | 357 | 118 | `0.08` / `0.49` | **25.0 / 25.0** |
| `baboonbutts-com` | `tier1_fast` | `1280×6624px` (185,098 B) | `390×2616px` (43,612 B) | 769 | 16 | 337 | 115 | `0.09` / `0.45` | **25.0 / 25.0** |
| `baztan-race-com` | `tier1_fast` | `1280×6624px` (476,218 B) | `390×2616px` (85,162 B) | 126 | 16 | 352 | 114 | `0.10` / `0.48` | **25.0 / 25.0** |
| `bb-b-net` | `tier1_fast` | `1280×6624px` (439,032 B) | `390×2616px` (92,916 B) | 70 | 16 | 343 | 111 | `0.10` / `0.45` | **25.0 / 25.0** |
| `bcgbuildingdesign-com-au` | `tier1_fast` | `1280×6624px` (600,846 B) | `390×1744px` (10,478 B) | 159 | 16 | 339 | 110 | `0.08` / `0.47` | **25.0 / 25.0** |
| `becore-se` | `tier1_fast` | `1280×6624px` (317,892 B) | `390×2616px` (92,112 B) | 241 | 16 | 349 | 111 | `0.09` / `0.49` | **25.0 / 25.0** |
| `belgradearbor-rs_en` | `tier1_fast` | `1280×6624px` (285,374 B) | `390×2616px` (39,544 B) | 61 | 16 | 355 | 116 | `0.10` / `0.49` | **25.0 / 25.0** |
| `bespokegroup-io` | `tier1_fast` | `1280×6624px` (319,258 B) | `390×1744px` (27,830 B) | 23 | 16 | 361 | 121 | `0.09` / `0.46` | **25.0 / 25.0** |
| `bar-topas-ch` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `bennos-light-org` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call `)** |
