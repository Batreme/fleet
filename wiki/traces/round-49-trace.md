# Round 49 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-49`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 49 Target Scope
  1. `www-lapl-org` — *Homepage · Los Angeles Public Library*
  2. `www-leadoff-fr` — *Agence digitale à Vannes : web, mobile & acquisition · LEADOFF*
  3. `www-lesgmstudios-com` — *GM Studios — Du contenu qui dépasse les chiffres*
  4. `www-lev-com` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*
  5. `www-lingers-it_en` — *Lingers – your hotel in Girlan*
  6. `www-lucaslima-design` — *Lucas Lima · Product designer and design engineer*
  7. `www-mathildedechiara-com` — *Mathilde De Chiara, designer and interior architect*
  8. `www-mbidirectmail-com` — *Blocked (`Headless Preloader / Blank Viewport Capture (solid blank desktop viewport)`)*
  9. `www-mdscollective-com` — *MDS Collective · China Marketing Agency for Hotels & Tourism*
  10. `www-memedia-de` — *Webdesign München für nachhaltig denkende Unternehmer*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-lapl-org` | `tier1_fast` | `1280×6624px` (734,792 B) | `390×2616px` (132,158 B) | 189 | 16 | 372 | 126 | `0.09` / `0.48` | **25.0 / 25.0** |
| `www-leadoff-fr` | `tier1_fast` | `1280×6624px` (296,802 B) | `390×2616px` (17,772 B) | 23 | 16 | 356 | 116 | `0.10` / `0.48` | **25.0 / 25.0** |
| `www-lesgmstudios-com` | `tier1_fast` | `1280×6624px` (349,800 B) | `390×2616px` (71,984 B) | 87 | 16 | 349 | 111 | `0.10` / `0.49` | **25.0 / 25.0** |
| `www-lingers-it_en` | `tier1_fast` | `1280×6624px` (366,172 B) | `390×2616px` (93,422 B) | 61 | 16 | 347 | 114 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-lucaslima-design` | `tier2_webgl` | `1280×4140px` (102,318 B) | `390×2616px` (55,172 B) | 213 | 16 | 354 | 122 | `0.08` / `0.50` | **25.0 / 25.0** |
| `www-mathildedechiara-com` | `tier1_fast` | `1280×828px` (31,498 B) | `390×872px` (3,802 B) | 30 | 16 | 312 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-mdscollective-com` | `tier1_fast` | `1280×6624px` (296,874 B) | `390×2616px` (44,028 B) | 15 | 16 | 356 | 116 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-memedia-de` | `tier1_fast` | `1280×6624px` (557,588 B) | `390×2616px` (96,906 B) | 62 | 16 | 367 | 120 | `0.09` / `0.48` | **25.0 / 25.0** |
| `www-lev-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
| `www-mbidirectmail-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (solid blank desktop viewp`)** |
