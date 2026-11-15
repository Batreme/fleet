# Round 40 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-40`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 40 Target Scope
  1. `wedding-s-tmro-com` — *Wedding Invitation · Yuri & Tomoro* (`https://wedding.s-tmro.com/`)
  2. `white-desert-com` — *Luxury Adventures in Antarctica · White Desert* (`https://white-desert.com/`)
  3. `wild-ag-ch` — *Wild AG – Entwicklung von Liegenschaften & Immobilien* (`https://wild-ag.ch/`)
  4. `withwise-com` — *Compliance-First Onboarding Software · Wise* (`https://withwise.com/`)
  5. `wndws-space` — *windows · place is temporary. you are not.* (`https://wndws.space/`)
  6. `woonpact-gent` — *Home - Woonpact* (`https://woonpact.gent/`)
  7. `www-197historiasilustradas-com` — *197 Historias Ilustradas* (`https://www.197historiasilustradas.com/`)
  8. `www-1centre-com` — *1Centre — Trade Credit Software for NZ & Australia* (`https://www.1centre.com/`)
  9. `www-31-for-31-com` — *31 for 31 · One scary movie for every night of October* (`https://www.31-for-31.com/`)
  10. `www-3d-discovery-fr` — *3D Discovery · Exploring New Dimensions* (`https://www.3d-discovery.fr/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `wedding-s-tmro-com` | `1440×11372px` (2,613,478 B) | `390×2400px` (98,037 B) | 16 | 16 | 264 | 110 | `0.09` / `0.55` | **25.0 / 25.0** |
| `white-desert-com` | `1440×2400px` (57,010 B) | `390×2400px` (36,452 B) | 117 | 16 | 258 | 107 | `0.09` / `0.50` | **25.0 / 25.0** |
| `wild-ag-ch` | `1440×9480px` (3,338,658 B) | `390×2400px` (36,768 B) | 40 | 16 | 256 | 106 | `0.09` / `0.47` | **25.0 / 25.0** |
| `withwise-com` | `1440×14756px` (1,351,332 B) | `390×2400px` (112,983 B) | 795 | 16 | 256 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `wndws-space` | `1440×2400px` (198,775 B) | `390×2400px` (201,408 B) | 13 | 16 | 256 | 106 | `0.09` / `0.55` | **25.0 / 25.0** |
| `woonpact-gent` | `1440×11932px` (583,070 B) | `390×2400px` (33,869 B) | 252 | 16 | 256 | 106 | `0.12` / `0.57` | **25.0 / 25.0** |
| `www-197historiasilustradas-com` | `1440×2400px` (424,424 B) | `390×2400px` (252,355 B) | 32 | 16 | 256 | 106 | `0.13` / `0.59` | **25.0 / 25.0** |
| `www-1centre-com` | `1440×18756px` (1,663,992 B) | `390×2400px` (49,681 B) | 87 | 16 | 256 | 106 | `0.13` / `0.59` | **25.0 / 25.0** |
| `www-31-for-31-com` | `1440×2400px` (2,196,457 B) | `390×2400px` (127,517 B) | 18 | 16 | 268 | 112 | `0.08` / `0.48` | **25.0 / 25.0** |
| `www-3d-discovery-fr` | `1440×2400px` (102,725 B) | `390×2400px` (44,230 B) | 81 | 16 | 256 | 106 | `0.09` / `0.55` | **25.0 / 25.0** |
