# Round 06 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-06`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 06 Target Scope
  1. `b3xgraphics-com` — *B3X Graphics · Freelance Sports Art Director & Designer*
  2. `baboonbutts-com` — *Baboon Butts - The redder the better!*
  3. `bar-topas-ch` — *Tòpas - bar-topas.ch*
  4. `baztan-race-com` — *Baztan Race*
  5. `bb-b-net` — *Agence de Communication b2b et Marketing Industriel- bb&b*
  6. `bcgbuildingdesign-com-au` — *Building Designer Gold Coast · BCG Building Design*
  7. `becore-se` — *Becore*
  8. `belgradearbor-rs_en` — *Belgrade Arbor · Residential & Business Complex in New Belgrade*
  9. `bennos-light-org` — *Blocked (`Headless Preloader / Blank Viewport Capture (LOADING YOU ARE ABOUT TO EXPERIENCE THE PERSONAL TESTIMONY OF HOLOCAUS)`)*
  10. `bespokegroup-io` — *Bespoke Group · Private Wealth & Estate Planning Advisory*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `b3xgraphics-com` | `tier1_fast` | `1440×2400px` (122,705 B) | `390×2400px` (448,397 B) | 192 | 16 | 296 | 113 | `0.09` / `0.48` | **25.0 / 25.0** |
| `baboonbutts-com` | `tier1_fast` | `1440×2400px` (130,139 B) | `390×2400px` (67,331 B) | 769 | 16 | 292 | 111 | `0.09` / `0.46` | **25.0 / 25.0** |
| `bar-topas-ch` | `tier2_webgl` | `1440×900px` (12,753 B) | `390×844px` (6,682 B) | 21 | 16 | 294 | 112 | `0.08` / `0.49` | **25.0 / 25.0** |
| `baztan-race-com` | `tier1_fast` | `1440×2400px` (2,546,910 B) | `390×2400px` (516,697 B) | 126 | 16 | 286 | 108 | `0.10` / `0.46` | **25.0 / 25.0** |
| `bb-b-net` | `tier1_fast` | `1440×2400px` (1,045,499 B) | `390×2400px` (384,562 B) | 70 | 16 | 285 | 107 | `0.10` / `0.46` | **25.0 / 25.0** |
| `bcgbuildingdesign-com-au` | `tier1_fast` | `1440×2400px` (1,668,382 B) | `390×2400px` (605,657 B) | 159 | 16 | 283 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `becore-se` | `tier1_fast` | `1440×2400px` (1,102,774 B) | `390×2400px` (421,957 B) | 240 | 16 | 282 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `belgradearbor-rs_en` | `tier1_fast` | `1440×900px` (609,366 B) | `390×2400px` (278,888 B) | 61 | 16 | 292 | 111 | `0.09` / `0.49` | **25.0 / 25.0** |
| `bespokegroup-io` | `tier1_fast` | `1440×2400px` (518,230 B) | `390×2400px` (258,831 B) | 23 | 16 | 304 | 117 | `0.09` / `0.46` | **25.0 / 25.0** |
| `bennos-light-org` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (LOADING YOU ARE ABOUT TO `)** |
