# Round 40 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-40`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 40 Target Scope
  1. `wedding-s-tmro-com` — *Wedding Invitation · Yuri & Tomoro*
  2. `white-desert-com` — *Luxury Adventures in Antarctica · White Desert*
  3. `wild-ag-ch` — *Wild AG – Entwicklung von Liegenschaften & Immobilien*
  4. `withwise-com` — *Compliance-First Onboarding Software · Wise*
  5. `wndws-space` — *windows · place is temporary. you are not.*
  6. `woonpact-gent` — *Blocked (`Live mobile screenshot capture failed (0 valid PNG bytes)`)*
  7. `www-197historiasilustradas-com` — *197 Historias Ilustradas*
  8. `www-1centre-com` — *1Centre — Trade Credit Software for NZ & Australia*
  9. `www-31-for-31-com` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 35000ms exceeded. Call log: - navigating to 'https://www.31-for-31.com/', waiting until 'domcontentloaded' )`)*
  10. `www-3d-discovery-fr` — *3D Discovery · Exploring New Dimensions*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `wedding-s-tmro-com` | `tier1_fast` | `1440×2400px` (1,055,151 B) | `390×2400px` (395,122 B) | 16 | 16 | 284 | 107 | `0.10` / `0.54` | **25.0 / 25.0** |
| `white-desert-com` | `tier1_fast` | `1440×2400px` (766,058 B) | `390×2400px` (304,625 B) | 117 | 16 | 294 | 112 | `0.09` / `0.50` | **25.0 / 25.0** |
| `wild-ag-ch` | `tier1_fast` | `1440×2400px` (1,671,437 B) | `390×2400px` (475,506 B) | 40 | 16 | 288 | 109 | `0.10` / `0.46` | **25.0 / 25.0** |
| `withwise-com` | `tier1_fast` | `1440×2400px` (894,150 B) | `390×2400px` (318,513 B) | 800 | 16 | 282 | 106 | `0.09` / `0.47` | **25.0 / 25.0** |
| `wndws-space` | `tier2_webgl` | `1440×900px` (15,594 B) | `390×844px` (3,887 B) | 13 | 16 | 282 | 106 | `0.10` / `0.54` | **25.0 / 25.0** |
| `www-197historiasilustradas-com` | `tier1_fast` | `1440×900px` (14,509 B) | `390×844px` (8,377 B) | 32 | 16 | 286 | 108 | `0.10` / `0.53` | **25.0 / 25.0** |
| `www-1centre-com` | `tier1_fast` | `1440×2400px` (226,814 B) | `390×2400px` (97,115 B) | 87 | 16 | 290 | 110 | `0.10` / `0.53` | **25.0 / 25.0** |
| `www-3d-discovery-fr` | `tier1_fast` | `1440×2400px` (549,099 B) | `390×2400px` (162,027 B) | 82 | 16 | 284 | 107 | `0.09` / `0.52` | **25.0 / 25.0** |
| `woonpact-gent` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile screenshot capture failed (0 valid PNG bytes)`)** |
| `www-31-for-31-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 35000ms exceeded. Call `)** |
