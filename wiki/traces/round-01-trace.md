# Round 01 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-01`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `10` live (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 01 Target Scope
  1. `dennypratama-com` — *Denny Pratama · Product designer who now builds what he designs*
  2. `agnestoth-com` — *AGNESTOTH · House of Luxurious Embroidery*
  3. `www-sigma-imaging-se` — *SIGMA Imaging Nordics & Baltics · Lenses, Cameras & Cine-lenses - Sigma*
  4. `morrow-valerian-studio` — *MORROW*
  5. `wiro-ae` — *Wiro · Operating System for All Agencies*
  6. `www-anduril-com` — *Transforming U.S. Defense Capabilities with Advanced Technology · Anduril*
  7. `www-avilus-com` — *Avilus · Dual-Use Uncrewed Aircraft for Evacuation, Logistics and Survei...*
  8. `www-eladiodieste-com` — *Eladio Dieste*
  9. `www-unimaticwatches-com` — *UNIMATIC Watches*
  10. `seedjewelry-com` — *Seed Jewelry · Lab-Grown Diamond High Jewelry, Dubai*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `dennypratama-com` | `tier1_fast` | `1440×2400px` (937,718 B) | `390×2400px` (311,368 B) | 94 | 16 | 300 | 115 | `0.09` / `0.48` | **25.0 / 25.0** |
| `agnestoth-com` | `tier1_fast` | `1440×2400px` (1,018,424 B) | `390×2400px` (630,101 B) | 232 | 16 | 282 | 106 | `0.10` / `0.50` | **25.0 / 25.0** |
| `www-sigma-imaging-se` | `tier1_fast` | `1440×2400px` (585,016 B) | `390×2400px` (322,396 B) | 177 | 16 | 284 | 107 | `0.10` / `0.50` | **25.0 / 25.0** |
| `morrow-valerian-studio` | `tier1_fast` | `1440×2400px` (2,936,487 B) | `390×2400px` (876,682 B) | 56 | 16 | 296 | 113 | `0.10` / `0.51` | **25.0 / 25.0** |
| `wiro-ae` | `tier2_webgl` | `1440×900px` (2,962,360 B) | `390×844px` (741,742 B) | 84 | 16 | 292 | 111 | `0.09` / `0.47` | **25.0 / 25.0** |
| `www-anduril-com` | `tier1_fast` | `1440×2400px` (1,027,814 B) | `390×2400px` (515,177 B) | 30 | 16 | 282 | 106 | `0.10` / `0.50` | **25.0 / 25.0** |
| `www-avilus-com` | `tier1_fast` | `1440×2400px` (1,558,744 B) | `390×2400px` (198,832 B) | 164 | 16 | 282 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-eladiodieste-com` | `tier1_fast` | `1440×2400px` (111,852 B) | `390×2400px` (698,733 B) | 46 | 16 | 282 | 106 | `0.10` / `0.51` | **25.0 / 25.0** |
| `www-unimaticwatches-com` | `tier1_fast` | `1440×2400px` (2,543,494 B) | `390×2400px` (973,040 B) | 93 | 16 | 282 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
| `seedjewelry-com` | `tier1_fast` | `1440×2400px` (1,248,826 B) | `390×2400px` (325,573 B) | 271 | 16 | 282 | 106 | `0.10` / `0.51` | **25.0 / 25.0** |
