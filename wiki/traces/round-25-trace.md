# Round 25 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-25`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 25 Target Scope
  1. `mms-inherited-band` — *INHERITED – ME, MYSELF & SAM (EP DEBUT)*
  2. `moderncraftaz-com` — *Select A Location · AllHaus*
  3. `mont-rural-emblematica-agency` — *MontRural — Private Masia Among the Vineyards of Penedès*
  4. `montarville-ca` — *montarville · Une approche globale et intégrée dans la gestion de vos pr...*
  5. `monument-tv` — *Homepage - Monument*
  6. `morphowater-com` — *MORPHO · Natural Spring Water from Costa Rica*
  7. `mosaic-flabbergast-agency` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  8. `mrcresidencesbocaraton-com` — *Mr. C Residences Boca Raton · New Luxury Residences for Sale*
  9. `mstage-group-jp` — *Blocked (`Upstream HTTP 403 — CloudFront WAF Block`)*
  10. `mubien-com` — *Blocked (`Network/Navigation failure (Page.goto: net::ERR_EMPTY_RESPONSE at https://mubien.com/ Call log: - navigating to 'https://mubien.com/', waiting until 'domcontentloaded)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `mms-inherited-band` | `tier2_webgl` | `1440×900px` (479,253 B) | `390×844px` (439,300 B) | 13 | 16 | 282 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `moderncraftaz-com` | `tier1_fast` | `1440×900px` (1,153,633 B) | `390×844px` (352,927 B) | 32 | 16 | 287 | 107 | `0.09` / `0.52` | **25.0 / 25.0** |
| `mont-rural-emblematica-agency` | `tier1_fast` | `1440×2400px` (2,374,186 B) | `390×2400px` (710,691 B) | 140 | 16 | 282 | 106 | `0.09` / `0.52` | **25.0 / 25.0** |
| `montarville-ca` | `tier1_fast` | `1440×2400px` (1,009,846 B) | `390×2400px` (342,676 B) | 89 | 16 | 284 | 107 | `0.09` / `0.49` | **25.0 / 25.0** |
| `monument-tv` | `tier1_fast` | `1440×2400px` (313,489 B) | `390×2400px` (267,625 B) | 83 | 16 | 290 | 110 | `0.09` / `0.50` | **25.0 / 25.0** |
| `morphowater-com` | `tier1_fast` | `1440×900px` (843,209 B) | `390×2400px` (172,943 B) | 83 | 16 | 290 | 110 | `0.09` / `0.49` | **25.0 / 25.0** |
| `mrcresidencesbocaraton-com` | `tier1_fast` | `1440×2400px` (2,010,100 B) | `390×2400px` (743,609 B) | 14 | 16 | 292 | 111 | `0.09` / `0.52` | **25.0 / 25.0** |
| `mosaic-flabbergast-agency` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `mstage-group-jp` | `blocked` (`403`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 403 — CloudFront WAF Block`)** |
| `mubien-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: net::ERR_EMPTY_RESPONSE at http`)** |
