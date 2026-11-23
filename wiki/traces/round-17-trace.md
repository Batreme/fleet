# Round 17 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-17`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 17 Target Scope
  1. `heirest-com` — *HEIREST · Fine Jewellery, Authored By You*
  2. `helmetverse-ai` — *Helmetverse · Design yours*
  3. `henrietta-wearetattoodigital-com` — *Henrietta Said : Scandalously Spicy*
  4. `henwoodcourt-co-uk` — *Henwood Court · Where financial freedom meets fulfilment*
  5. `herasymenkox-com` — *Blocked (`Headless Preloader / Blank Viewport Capture (cannot hydrate without interactive/GPU session)`)*
  6. `heronaiapp-com` — *Heron AI · Works inside your design tools*
  7. `hole-money` — *Money Hole*
  8. `holmchrome-byholm-co` — *Blocked (`Headless Preloader / Blank Viewport Capture (cannot hydrate without interactive/GPU session)`)*
  9. `hopecancerresources-org` — *Hope Cancer Resources - Support. Educate. Prevent.*
  10. `hotelaurelia-online` — *Villa Aurelia — Butik Lüks Otel & Rezervasyon*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `heirest-com` | `tier1_fast` | `1440×2400px` (2,503,610 B) | `390×2400px` (791,363 B) | 1469 | 16 | 284 | 107 | `0.09` / `0.48` | **25.0 / 25.0** |
| `helmetverse-ai` | `tier1_fast` | `1440×900px` (457,324 B) | `390×2400px` (146,405 B) | 193 | 16 | 298 | 114 | `0.08` / `0.50` | **25.0 / 25.0** |
| `henrietta-wearetattoodigital-com` | `tier1_fast` | `1440×2400px` (546,174 B) | `390×2400px` (338,170 B) | 21 | 16 | 300 | 115 | `0.09` / `0.53` | **25.0 / 25.0** |
| `henwoodcourt-co-uk` | `tier1_fast` | `1440×2400px` (1,841,094 B) | `390×2400px` (598,701 B) | 61 | 16 | 284 | 107 | `0.09` / `0.46` | **25.0 / 25.0** |
| `heronaiapp-com` | `tier1_fast` | `1440×900px` (850,300 B) | `390×844px` (230,129 B) | 43 | 16 | 286 | 107 | `0.09` / `0.53` | **25.0 / 25.0** |
| `hole-money` | `tier1_fast` | `1440×900px` (1,173,085 B) | `390×844px` (387,932 B) | 59 | 16 | 290 | 110 | `0.09` / `0.50` | **25.0 / 25.0** |
| `hopecancerresources-org` | `tier1_fast` | `1440×2400px` (254,005 B) | `390×2400px` (158,473 B) | 20 | 16 | 294 | 112 | `0.09` / `0.46` | **25.0 / 25.0** |
| `hotelaurelia-online` | `tier1_fast` | `1440×2400px` (2,130,308 B) | `390×2400px` (706,619 B) | 86 | 16 | 282 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `herasymenkox-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (cannot hydrate without in`)** |
| `holmchrome-byholm-co` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (cannot hydrate without in`)** |
