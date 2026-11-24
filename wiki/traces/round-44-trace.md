# Round 44 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-44`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 44 Target Scope
  1. `www-chriswilliamsart-com` — *Chris Williams Art Gallery · Contemporary painting in London*
  2. `www-codeofsagar-in` — *Sagar K. Ghosh — Full-stack Developer & Designer*
  3. `www-concretemanagement-fr` — *Concrete.*
  4. `www-cybear-it_world` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  5. `www-danielebuser-com` — *Daniele Buser · Creative Developer*
  6. `www-davidecarusio-it` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*
  7. `www-dbydt-space` — *Deebak Tamilmani · Design Portfolio*
  8. `www-deathtorobots-com` — *Death to Robots*
  9. `www-designbomb-it` — *Design Bomb Festival*
  10. `www-discoverforgiveness-org` — *Discover Forgiveness · Templeton World Charity Foundation*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-chriswilliamsart-com` | `tier1_fast` | `1280×6624px` (377,202 B) | `390×872px` (2,106 B) | 7 | 16 | 341 | 112 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-codeofsagar-in` | `tier1_fast` | `1280×828px` (63,396 B) | `390×2616px` (29,722 B) | 126 | 16 | 312 | 109 | `0.11` / `0.52` | **25.0 / 25.0** |
| `www-concretemanagement-fr` | `tier1_fast` | `1280×1656px` (105,490 B) | `390×872px` (3,346 B) | 25 | 16 | 337 | 115 | `0.12` / `0.52` | **25.0 / 25.0** |
| `www-danielebuser-com` | `tier1_fast` | `1280×2484px` (135,870 B) | `390×2616px` (48,754 B) | 79 | 16 | 338 | 114 | `0.11` / `0.52` | **25.0 / 25.0** |
| `www-dbydt-space` | `tier2_webgl` | `1280×828px` (3,626 B) | `390×872px` (1,942 B) | 12 | 16 | 309 | 109 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-deathtorobots-com` | `tier1_fast` | `1280×6624px` (298,274 B) | `390×2616px` (57,380 B) | 31 | 16 | 329 | 111 | `0.12` / `0.57` | **25.0 / 25.0** |
| `www-designbomb-it` | `tier2_webgl` | `1280×6624px` (297,316 B) | `390×1744px` (23,144 B) | 36 | 16 | 330 | 112 | `0.12` / `0.57` | **25.0 / 25.0** |
| `www-discoverforgiveness-org` | `tier1_fast` | `1280×6624px` (319,826 B) | `390×2616px` (68,298 B) | 28 | 16 | 359 | 121 | `0.12` / `0.52` | **25.0 / 25.0** |
| `www-cybear-it_world` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `www-davidecarusio-it` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
