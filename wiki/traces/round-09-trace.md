# Round 09 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-09`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 09 Target Scope
  1. `clinia-com` — *Patient Context for Healthcare AI · Clinia*
  2. `clipdance-ai` — *Seedance 2.0 - Free AI Video Generator · Text/Image to Video*
  3. `clubcharlestown-com-au` — *Home · Club Charlestown*
  4. `cobaltaf-org` — *Cobalt Abortion Fund*
  5. `coloniazacamil-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  6. `concretaceramiche-it` — *Concreta Ceramiche Artigianali Fatte a Mano*
  7. `constellations-icilalune-com` — *Constellation(s) — Immersive virtual 3D art exhibitions*
  8. `continuance-ai` — *Continuance - A novel by Chris Bennett*
  9. `crl-2026-webflow-io` — *Blocked (`Headless Preloader / Blank Viewport Capture (cannot hydrate without interactive/GPU session)`)*
  10. `crun-ai` — *One API for All Top AI Models – Cost-Effective AI API · Crun*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `clinia-com` | `tier2_webgl` | `1440×900px` (107,174 B) | `390×844px` (42,142 B) | 309 | 16 | 302 | 116 | `0.08` / `0.49` | **25.0 / 25.0** |
| `clipdance-ai` | `tier1_fast` | `1440×900px` (417,339 B) | `390×855px` (150,338 B) | 287 | 16 | 288 | 110 | `0.08` / `0.47` | **25.0 / 25.0** |
| `clubcharlestown-com-au` | `tier1_fast` | `1440×2400px` (1,328,729 B) | `390×2400px` (487,840 B) | 430 | 16 | 292 | 111 | `0.13` / `0.58` | **25.0 / 25.0** |
| `cobaltaf-org` | `tier1_fast` | `1440×2400px` (991,336 B) | `390×2400px` (405,428 B) | 249 | 16 | 294 | 112 | `0.13` / `0.58` | **25.0 / 25.0** |
| `concretaceramiche-it` | `tier1_fast` | `1440×2400px` (757,920 B) | `390×2400px` (95,639 B) | 68 | 16 | 296 | 113 | `0.09` / `0.47` | **25.0 / 25.0** |
| `constellations-icilalune-com` | `tier1_fast` | `1440×2400px` (2,106,437 B) | `390×2400px` (612,248 B) | 48 | 16 | 306 | 118 | `0.09` / `0.47` | **25.0 / 25.0** |
| `continuance-ai` | `tier1_fast` | `1440×900px` (27,732 B) | `390×844px` (22,801 B) | 46 | 16 | 282 | 106 | `0.08` / `0.51` | **25.0 / 25.0** |
| `crun-ai` | `tier1_fast` | `1440×2400px` (870,485 B) | `390×2400px` (581,350 B) | 811 | 16 | 302 | 116 | `0.10` / `0.49` | **25.0 / 25.0** |
| `coloniazacamil-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `crl-2026-webflow-io` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (cannot hydrate without in`)** |
