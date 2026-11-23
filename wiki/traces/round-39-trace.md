# Round 39 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-39`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 39 Target Scope
  1. `vastworld-ai` — *Blocked (`Headless Preloader / Blank Viewport Capture (cannot hydrate without interactive/GPU session)`)*
  2. `vault-hyperiux-com` — *Hyperiux Vault - React & Next.js Interaction Effects.*
  3. `vc-prty-jp` — *PARTY STARTUP STUDIO FUND*
  4. `velourproductions-com` — *Velour Productions · Vancouver Video & Photography*
  5. `verasfawaz-com` — *Véras Fawaz*
  6. `vivmgmt-com` — *Photographer Agency & Commercial Photo Production — ViV MGMT*
  7. `vploss-com` — *VPLOSS*
  8. `waverunmedia-com` — *WaveRun Media*
  9. `web-smith-de` — *Internetagentur Ostwestfalen: Websites & SEO · Web Smith*
  10. `webdesign-kernjosh-com` — *Josh Kern*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `vault-hyperiux-com` | `tier1_fast` | `1440×2400px` (128,292 B) | `390×2400px` (133,416 B) | 159 | 16 | 296 | 113 | `0.11` / `0.57` | **25.0 / 25.0** |
| `vc-prty-jp` | `tier1_fast` | `1440×2400px` (123,196 B) | `390×2400px` (79,325 B) | 64 | 16 | 292 | 111 | `0.11` / `0.57` | **25.0 / 25.0** |
| `velourproductions-com` | `tier1_fast` | `1440×2400px` (411,532 B) | `390×2400px` (342,460 B) | 79 | 16 | 288 | 109 | `0.09` / `0.50` | **25.0 / 25.0** |
| `verasfawaz-com` | `tier1_fast` | `1440×900px` (383,827 B) | `390×844px` (82,943 B) | 115 | 16 | 287 | 108 | `0.09` / `0.51` | **25.0 / 25.0** |
| `vivmgmt-com` | `tier1_fast` | `1440×900px` (749,046 B) | `390×844px` (177,139 B) | 37 | 16 | 282 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `vploss-com` | `tier1_fast` | `1440×2400px` (282,138 B) | `390×2400px` (378,729 B) | 65 | 16 | 306 | 118 | `0.09` / `0.52` | **25.0 / 25.0** |
| `waverunmedia-com` | `tier1_fast` | `1440×2400px` (1,238,877 B) | `390×2400px` (372,399 B) | 103 | 16 | 282 | 106 | `0.09` / `0.52` | **25.0 / 25.0** |
| `web-smith-de` | `tier1_fast` | `1440×2400px` (615,903 B) | `390×2400px` (235,727 B) | 23 | 16 | 300 | 115 | `0.09` / `0.51` | **25.0 / 25.0** |
| `webdesign-kernjosh-com` | `tier1_fast` | `1440×900px` (991,198 B) | `390×886px` (442,338 B) | 64 | 16 | 290 | 110 | `0.09` / `0.48` | **25.0 / 25.0** |
| `vastworld-ai` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (cannot hydrate without in`)** |
