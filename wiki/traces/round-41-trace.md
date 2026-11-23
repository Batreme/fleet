# Round 41 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-41`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 41 Target Scope
  1. `www-3moons-it` — *3Moons Studio · App mobile, software enterprise e AI su misura*
  2. `www-aaronbrimhall-com` — *Aaron Brimhall · Action & Automotive Photographer*
  3. `www-aat-architecten-be` — *AAT Architecten*
  4. `www-agencejacquesparis-fr` — *Jacques Paris - Agence à impact positif*
  5. `www-agrumeafarm-it_en` — *Agrumea Farm · Jams, pestos and flavours of Sicily*
  6. `www-alexadevaney-com` — *North County San Diego Luxury Homes – Alexa Devaney*
  7. `www-allerstudio-com` — *ALLER Studio — Product design and development studio*
  8. `www-alpineguides-co-nz` — *Alpine Guides Aoraki · NZ Mountain Guiding Since 1966*
  9. `www-amberjs-dev` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 35000ms exceeded. Call log: - navigating to 'https://www.amberjs.dev/', waiting until 'domcontentloaded' )`)*
  10. `www-andriimur-com` — *Andrii Mur*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-3moons-it` | `tier1_fast` | `1440×2400px` (1,338,989 B) | `390×2400px` (767,203 B) | 17 | 16 | 294 | 112 | `0.10` / `0.51` | **25.0 / 25.0** |
| `www-aaronbrimhall-com` | `tier1_fast` | `1440×2400px` (606,682 B) | `390×2400px` (217,558 B) | 26 | 16 | 282 | 106 | `0.11` / `0.54` | **25.0 / 25.0** |
| `www-aat-architecten-be` | `tier1_fast` | `1440×2400px` (1,652,678 B) | `390×2400px` (629,689 B) | 151 | 16 | 282 | 106 | `0.10` / `0.48` | **25.0 / 25.0** |
| `www-agencejacquesparis-fr` | `tier1_fast` | `1440×2400px` (892,812 B) | `390×2400px` (218,568 B) | 21 | 16 | 290 | 110 | `0.10` / `0.52` | **25.0 / 25.0** |
| `www-agrumeafarm-it_en` | `tier1_fast` | `1440×900px` (372,904 B) | `390×844px` (95,308 B) | 66 | 16 | 284 | 107 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-alexadevaney-com` | `tier1_fast` | `1440×2400px` (1,929,467 B) | `390×2400px` (450,381 B) | 17 | 16 | 290 | 110 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-allerstudio-com` | `tier1_fast` | `1440×2400px` (668,039 B) | `390×2400px` (217,785 B) | 78 | 16 | 286 | 108 | `0.10` / `0.49` | **25.0 / 25.0** |
| `www-alpineguides-co-nz` | `tier1_fast` | `1440×2400px` (986,319 B) | `390×2400px` (498,319 B) | 236 | 16 | 286 | 108 | `0.11` / `0.54` | **25.0 / 25.0** |
| `www-andriimur-com` | `tier1_fast` | `1440×2400px` (1,140,947 B) | `390×2400px` (671,483 B) | 138 | 16 | 298 | 115 | `0.10` / `0.48` | **25.0 / 25.0** |
| `www-amberjs-dev` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 35000ms exceeded. Call `)** |
