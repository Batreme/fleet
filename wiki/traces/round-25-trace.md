# Round 25 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-25`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `6` live (`4` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 25 Target Scope
  1. `mms-inherited-band` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*
  2. `moderncraftaz-com` — *Select A Location · AllHaus*
  3. `mont-rural-emblematica-agency` — *MontRural — Private Masia Among the Vineyards of Penedès*
  4. `montarville-ca` — *montarville · Une approche globale et intégrée dans la gestion de vos pr...*
  5. `monument-tv` — *Homepage - Monument*
  6. `morphowater-com` — *MORPHO · Natural Spring Water from Costa Rica*
  7. `mosaic-flabbergast-agency` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call log: - navigating to 'https://mosaic.flabbergast.agency/', waiting until 'domcontentloaded' )`)*
  8. `mrcresidencesbocaraton-com` — *Mr. C Residences Boca Raton · New Luxury Residences for Sale*
  9. `mstage-group-jp` — *Blocked (`Upstream HTTP 403 — CloudFront WAF Block`)*
  10. `mubien-com` — *Blocked (`Network/Navigation failure (Page.goto: net::ERR_EMPTY_RESPONSE at https://mubien.com/ Call log: - navigating to 'https://mubien.com/', waiting until 'domcontentloaded)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `moderncraftaz-com` | `tier1_fast` | `1280×6624px` (533,294 B) | `390×872px` (3,346 B) | 34 | 16 | 342 | 111 | `0.09` / `0.53` | **25.0 / 25.0** |
| `mont-rural-emblematica-agency` | `tier1_fast` | `1280×6624px` (535,900 B) | `390×2616px` (66,226 B) | 140 | 16 | 331 | 109 | `0.09` / `0.52` | **25.0 / 25.0** |
| `montarville-ca` | `tier1_fast` | `1280×6624px` (393,198 B) | `390×2616px` (50,140 B) | 89 | 16 | 343 | 112 | `0.09` / `0.49` | **25.0 / 25.0** |
| `monument-tv` | `tier1_fast` | `1280×6624px` (434,220 B) | `390×2616px` (89,458 B) | 83 | 16 | 348 | 114 | `0.09` / `0.50` | **25.0 / 25.0** |
| `morphowater-com` | `tier1_fast` | `1280×1656px` (56,226 B) | `390×2616px` (50,142 B) | 83 | 16 | 326 | 115 | `0.09` / `0.49` | **25.0 / 25.0** |
| `mrcresidencesbocaraton-com` | `tier1_fast` | `1280×6624px` (761,358 B) | `390×2616px` (133,292 B) | 14 | 16 | 351 | 116 | `0.09` / `0.53` | **25.0 / 25.0** |
| `mms-inherited-band` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
| `mosaic-flabbergast-agency` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call `)** |
| `mstage-group-jp` | `blocked` (`403`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 403 — CloudFront WAF Block`)** |
| `mubien-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: net::ERR_EMPTY_RESPONSE at http`)** |
