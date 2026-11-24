# Round 20 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-20`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 20 Target Scope
  1. `kamdalej-sk_en` — *Mastercard · Where Next*
  2. `karma-tracks-com` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*
  3. `kelvin-8b-com` — *Kelvin — three nights of music, filmed in heat*
  4. `key-co` — *KEY.co · Luxury Vacation Home Rentals + Concierge Services*
  5. `kindi-land` — *Kindi & Kitir — a confectionery manufacturer in Turkmenistan*
  6. `kingriver-com-au` — *Blocked (`Headless Preloader / Blank Viewport Capture (solid blank desktop viewport)`)*
  7. `kinoria-studio` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  8. `kissbranding-co-uk` — *Kiss · Brands that Kiss*
  9. `klad-design` — *Multidisciplinary Design Syndicate – KLAD*
  10. `kohenavocats-com_avocats-droit-famille-paris` — *Avocat Droit de la Famille Paris · Divorce, Garde d'Enfants, Succession*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kamdalej-sk_en` | `tier1_fast` | `1280×5796px` (355,376 B) | `390×2616px` (67,868 B) | 168 | 16 | 345 | 111 | `0.10` / `0.47` | **25.0 / 25.0** |
| `kelvin-8b-com` | `tier1_fast` | `1280×6624px` (540,012 B) | `390×2616px` (84,160 B) | 23 | 16 | 344 | 118 | `0.09` / `0.47` | **25.0 / 25.0** |
| `key-co` | `tier1_fast` | `1280×6624px` (494,294 B) | `390×2616px` (81,450 B) | 118 | 16 | 346 | 111 | `0.11` / `0.47` | **25.0 / 25.0** |
| `kindi-land` | `tier1_fast` | `1280×828px` (9,972 B) | `390×1744px` (16,784 B) | 118 | 16 | 324 | 116 | `0.09` / `0.48` | **25.0 / 25.0** |
| `kissbranding-co-uk` | `tier1_fast` | `1280×4140px` (132,906 B) | `390×872px` (18,814 B) | 95 | 16 | 317 | 109 | `0.11` / `0.52` | **25.0 / 25.0** |
| `klad-design` | `tier1_fast` | `1280×6624px` (824,618 B) | `390×2616px` (178,576 B) | 68 | 16 | 343 | 112 | `0.11` / `0.52` | **25.0 / 25.0** |
| `kohenavocats-com_avocats-droit-famille-paris` | `tier1_fast` | `1280×1656px` (113,826 B) | `390×2616px` (74,994 B) | 298 | 16 | 338 | 111 | `0.10` / `0.46` | **25.0 / 25.0** |
| `karma-tracks-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
| `kingriver-com-au` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (solid blank desktop viewp`)** |
| `kinoria-studio` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
