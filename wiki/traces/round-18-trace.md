# Round 18 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-18`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 18 Target Scope
  1. `houseofgiants-com` — *House of Giants · Product engineering partner*
  2. `hoyojerez-com` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  3. `ieqtechnology-com` — *IEQ Technology · Innovation. Experience. Quality.*
  4. `iginusa-com` — *IGIN USA · Official Home of IGIN in the United States*
  5. `imdday-ch` — *IMDDay 2026*
  6. `infinitytechstack-uk_pulsebridge` — *PulseBridge [2026] · AI IDE Mobile Companion (Free)*
  7. `inherited-band` — *INHERITED*
  8. `inks-studio` — *Ink Studio - UI UX Design, CRO & Webflow Development Agency*
  9. `iroom-devinthehood-com` — *iRoom framework 3 · Get started*
  10. `its-tomo-dev` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `houseofgiants-com` | `tier1_fast` | `1280×6624px` (297,950 B) | `390×2616px` (74,102 B) | 188 | 16 | 342 | 111 | `0.09` / `0.47` | **25.0 / 25.0** |
| `ieqtechnology-com` | `tier1_fast` | `1280×6624px` (469,684 B) | `390×2616px` (74,074 B) | 51 | 16 | 360 | 117 | `0.09` / `0.50` | **25.0 / 25.0** |
| `iginusa-com` | `tier1_fast` | `1280×828px` (32,432 B) | `390×1744px` (55,932 B) | 204 | 16 | 310 | 109 | `0.09` / `0.48` | **25.0 / 25.0** |
| `imdday-ch` | `tier1_fast` | `1280×828px` (88,710 B) | `390×2616px` (105,036 B) | 53 | 16 | 311 | 109 | `0.09` / `0.49` | **25.0 / 25.0** |
| `infinitytechstack-uk_pulsebridge` | `tier1_fast` | `1280×6624px` (470,408 B) | `390×2616px` (100,972 B) | 174 | 16 | 372 | 123 | `0.09` / `0.46` | **25.0 / 25.0** |
| `inherited-band` | `tier1_fast` | `1280×4968px` (683,464 B) | `390×2616px` (122,984 B) | 5 | 16 | 320 | 108 | `0.09` / `0.50` | **25.0 / 25.0** |
| `inks-studio` | `tier1_fast` | `1280×6624px` (403,506 B) | `390×2616px` (70,372 B) | 446 | 16 | 369 | 121 | `0.09` / `0.47` | **25.0 / 25.0** |
| `iroom-devinthehood-com` | `tier1_fast` | `1280×4140px` (226,010 B) | `390×2616px` (70,244 B) | 113 | 16 | 348 | 114 | `0.09` / `0.50` | **25.0 / 25.0** |
| `hoyojerez-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `its-tomo-dev` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
