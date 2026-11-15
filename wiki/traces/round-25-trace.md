# Round 25 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-25`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `8` (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 25 Target Scope
  1. `mms-inherited-band` — *INHERITED – ME, MYSELF & SAM (EP DEBUT)* (`https://mms.inherited.band/`)
  2. `moderncraftaz-com` — *Select A Location · AllHaus* (`https://moderncraftaz.com/`)
  3. `mont-rural-emblematica-agency` — *MontRural — Private Masia Among the Vineyards of Penedès* (`https://mont-rural.emblematica.agency`)
  4. `montarville-ca` — *montarville · Une approche globale et intégrée dans la gestion de vos pr...* (`https://montarville.ca/`)
  5. `monument-tv` — *Homepage - Monument* (`https://monument.tv/`)
  6. `morphowater-com` — *MORPHO · Natural Spring Water from Costa Rica* (`https://morphowater.com`)
  7. `mosaic-flabbergast-agency` — *Mosaic – Split & Back Up Your Seed Phrase* (`https://mosaic.flabbergast.agency`)
  8. `mrcresidencesbocaraton-com` — *Mr. C Residences Boca Raton · New Luxury Residences for Sale* (`https://mrcresidencesbocaraton.com`)
  9. `mstage-group-jp` — *Blocked (`CloudFront HTTP 403 WAF Block (ERROR: The request could not be satisfied)`)*
  10. `mubien-com` — *Blocked (`Empty raw DOM capture (39 bytes, 0 stylesheets)`)*

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `mms-inherited-band` | `1440×2400px` (948,605 B) | `390×2400px` (375,843 B) | 13 | 16 | 256 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
| `moderncraftaz-com` | `1440×2400px` (117,748 B) | `390×2400px` (56,976 B) | 32 | 16 | 253 | 103 | `0.10` / `0.54` | **25.0 / 25.0** |
| `mont-rural-emblematica-agency` | `1440×2400px` (90,164 B) | `390×2400px` (216,571 B) | 140 | 16 | 256 | 106 | `0.10` / `0.52` | **25.0 / 25.0** |
| `montarville-ca` | `1440×11326px` (1,011,762 B) | `390×2400px` (38,424 B) | 89 | 16 | 256 | 106 | `0.08` / `0.51` | **25.0 / 25.0** |
| `monument-tv` | `1440×16722px` (648,819 B) | `390×2400px` (65,086 B) | 83 | 16 | 256 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `morphowater-com` | `1440×24479px` (1,323,459 B) | `390×2400px` (513,795 B) | 83 | 16 | 256 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `mosaic-flabbergast-agency` | `1440×2400px` (429,057 B) | `390×2400px` (37,751 B) | 67 | 16 | 256 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
| `mrcresidencesbocaraton-com` | `1440×7365px` (1,187,417 B) | `390×2400px` (112,440 B) | 14 | 16 | 258 | 107 | `0.10` / `0.54` | **25.0 / 25.0** |
| `mstage-group-jp` | `status: blocked` | `status: blocked` | — | — | — | — | — | **Excluded (`CloudFront HTTP 403 WAF Block (ERROR: The request could not be satisfied)`)** |
| `mubien-com` | `status: blocked` | `status: blocked` | — | — | — | — | — | **Excluded (`Empty raw DOM capture (39 bytes, 0 stylesheets)`)** |
