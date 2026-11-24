# Round 09 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-09`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 09 Target Scope
  1. `clinia-com` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*
  2. `clipdance-ai` — *Seedance 2.0 - Free AI Video Generator · Text/Image to Video*
  3. `clubcharlestown-com-au` — *Home · Club Charlestown*
  4. `cobaltaf-org` — *Cobalt Abortion Fund*
  5. `coloniazacamil-com` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  6. `concretaceramiche-it` — *Concreta Ceramiche Artigianali Fatte a Mano*
  7. `constellations-icilalune-com` — *Constellation(s) — Immersive virtual 3D art exhibitions*
  8. `continuance-ai` — *Continuance - A novel by Chris Bennett*
  9. `crl-2026-webflow-io` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  10. `crun-ai` — *One API for All Top AI Models – Cost-Effective AI API · Crun*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `clipdance-ai` | `tier1_fast` | `1280×6624px` (651,728 B) | `390×872px` (37,462 B) | 287 | 16 | 352 | 115 | `0.08` / `0.48` | **25.0 / 25.0** |
| `clubcharlestown-com-au` | `tier1_fast` | `1280×5796px` (601,816 B) | `390×2616px` (124,332 B) | 429 | 16 | 348 | 115 | `0.12` / `0.57` | **25.0 / 25.0** |
| `cobaltaf-org` | `tier1_fast` | `1280×6624px` (473,530 B) | `390×2616px` (112,234 B) | 249 | 16 | 359 | 117 | `0.12` / `0.57` | **25.0 / 25.0** |
| `concretaceramiche-it` | `tier1_fast` | `1280×6624px` (349,612 B) | `390×2616px` (80,758 B) | 68 | 16 | 353 | 117 | `0.09` / `0.46` | **25.0 / 25.0** |
| `constellations-icilalune-com` | `tier2_webgl` | `1280×3312px` (353,962 B) | `390×2616px` (85,420 B) | 48 | 16 | 341 | 121 | `0.08` / `0.47` | **25.0 / 25.0** |
| `continuance-ai` | `tier1_fast` | `1280×828px` (8,946 B) | `390×872px` (2,566 B) | 46 | 16 | 309 | 109 | `0.08` / `0.50` | **25.0 / 25.0** |
| `crun-ai` | `tier1_fast` | `1280×6624px` (395,970 B) | `390×2616px` (92,678 B) | 878 | 16 | 361 | 120 | `0.10` / `0.48` | **25.0 / 25.0** |
| `clinia-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
| `coloniazacamil-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `crl-2026-webflow-io` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
