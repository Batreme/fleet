# Round 36 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-36`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 36 Target Scope
  1. `thecontenders-co` — *The Contenders · Strategic Brand & Design Consultancy*
  2. `thefwa-net` — *FWA Wire — winners' newswire*
  3. `theimmortals-world` — *Blocked (`Headless Preloader / Blank Viewport Capture (cannot hydrate without interactive/GPU session)`)*
  4. `theinfinitysocks-com` — *Infinity Socks — Performance Basketball Socks*
  5. `thenest-pl_en` — *The Nest — a registered business address in central Warsaw*
  6. `theobromachocolat-com` — *Cure Your Chocolate Craving · Theobroma Chocolate*
  7. `theperformancelab-ca` — *The Performance Lab — Sports Science & Athletic Testing in Toronto*
  8. `therechabite-com-au` — *The Rechabite • Multi-level Palace of Surprise and Delight*
  9. `thesovietflip-com` — *The Soviet Flip*
  10. `thestudiobyjuliegranger-com` — *The Studio by Julie Granger*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `thecontenders-co` | `tier2_webgl` | `1440×900px` (21,214 B) | `390×844px` (2,275 B) | 130 | 16 | 282 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
| `thefwa-net` | `tier1_fast` | `1440×2400px` (363,691 B) | `390×2400px` (269,680 B) | 13 | 16 | 290 | 110 | `0.09` / `0.51` | **25.0 / 25.0** |
| `theinfinitysocks-com` | `tier2_webgl` | `1440×900px` (269,919 B) | `390×844px` (65,831 B) | 174 | 16 | 282 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `thenest-pl_en` | `tier1_fast` | `1440×2400px` (686,663 B) | `390×2400px` (356,937 B) | 139 | 16 | 284 | 107 | `0.13` / `0.54` | **25.0 / 25.0** |
| `theobromachocolat-com` | `tier1_fast` | `1440×2400px` (1,607,796 B) | `390×2400px` (343,126 B) | 52 | 16 | 296 | 113 | `0.09` / `0.48` | **25.0 / 25.0** |
| `theperformancelab-ca` | `tier1_fast` | `1440×2400px` (874,000 B) | `390×2400px` (351,475 B) | 37 | 16 | 292 | 111 | `0.10` / `0.53` | **25.0 / 25.0** |
| `therechabite-com-au` | `tier1_fast` | `1440×2400px` (1,485,723 B) | `390×2400px` (528,119 B) | 73 | 16 | 292 | 111 | `0.13` / `0.54` | **25.0 / 25.0** |
| `thesovietflip-com` | `tier1_fast` | `1440×968px` (622,741 B) | `390×908px` (267,663 B) | 40 | 16 | 282 | 106 | `0.08` / `0.50` | **25.0 / 25.0** |
| `thestudiobyjuliegranger-com` | `tier1_fast` | `1440×2400px` (1,139,572 B) | `390×2400px` (332,034 B) | 37 | 16 | 292 | 111 | `0.12` / `0.54` | **25.0 / 25.0** |
| `theimmortals-world` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (cannot hydrate without in`)** |
