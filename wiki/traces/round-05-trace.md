# Round 05 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-05`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `6` live (`4` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 05 Target Scope
  1. `articles-gamcare-org-uk` — *The Gamification of Everything · GamCare*
  2. `aryabhangybuilders-com` — *Premium Builders In Kochi · Flats & Apartments · Arya Bhangy*
  3. `ascension-pegassi-be` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  4. `atmos-gallery` — *Blocked (`Live desktop screenshot capture failed (0 valid PNG bytes)`)*
  5. `auge-xp-com` — *Digital Experience Studio · AUGE Experience*
  6. `aviator-yakudoo-games` — *Blocked (`Hard per-target capture deadline exceeded (160s)`)*
  7. `awards-racing` — *Awards Racing*
  8. `awmedia-marketing` — *AW Media & Marketing · UK Web Design Studio*
  9. `aya-nl` — *Danstheater AYA - eigenzinnige voorstellingen voor jong publiek*
  10. `azimuteresidencial-com-br` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `articles-gamcare-org-uk` | `tier1_fast` | `1280×6624px` (592,834 B) | `390×2616px` (111,458 B) | 140 | 16 | 327 | 110 | `0.09` / `0.48` | **25.0 / 25.0** |
| `aryabhangybuilders-com` | `tier1_fast` | `1280×6624px` (619,268 B) | `390×2616px` (74,648 B) | 171 | 16 | 351 | 116 | `0.09` / `0.48` | **25.0 / 25.0** |
| `auge-xp-com` | `tier2_webgl` | `1280×4140px` (84,598 B) | `390×872px` (4,126 B) | 37 | 16 | 321 | 107 | `0.08` / `0.53` | **25.0 / 25.0** |
| `awards-racing` | `tier1_fast` | `1280×6624px` (516,422 B) | `390×872px` (56,334 B) | 57 | 16 | 330 | 111 | `0.09` / `0.53` | **25.0 / 25.0** |
| `awmedia-marketing` | `tier1_fast` | `1280×6624px` (352,622 B) | `390×2616px` (69,030 B) | 65 | 16 | 353 | 114 | `0.09` / `0.47` | **25.0 / 25.0** |
| `aya-nl` | `tier1_fast` | `1280×6624px` (397,902 B) | `390×2616px` (66,066 B) | 66 | 16 | 369 | 122 | `0.08` / `0.48` | **25.0 / 25.0** |
| `ascension-pegassi-be` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `atmos-gallery` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop screenshot capture failed (0 valid PNG bytes)`)** |
| `aviator-yakudoo-games` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (160s)`)** |
| `azimuteresidencial-com-br` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
