# Round 56 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-56`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 56 Target Scope
  1. `www-vanderhotel-com` — *Hotel & Restaurant Ljubljana · Vander Urbani Resort*
  2. `www-vanguardinitiative-com` — *Blocked (`Upstream HTTP 402 — Vercel Deployment Paused`)*
  3. `www-velaaprivateisland-com` — *Velaa Private Island Maldives*
  4. `www-vibr-studio` — *Vibr — Figma to code for designers who ship*
  5. `www-villiers-ai` — *Private Jet Charter and Empty Leg Flights · Villiers*
  6. `www-vineyard-co-za` — *The Vineyard Hotel · Hotel & Spa in Newlands, Cape Town*
  7. `www-weisslameraner-com_en` — *Weiss & Lameraner Media Group – Lifestyle Media House Vienna*
  8. `www-worksruthi-com` — *meet Sruthi. a copywriter, marketer and artist with chutzpah.*
  9. `www-xantium-com` — *Xantium*
  10. `www-zagrebwebusluge-com` — *Web agencija i digitalna rješenja · Zagreb Web Usluge*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-vanderhotel-com` | `tier1_fast` | `1440×2400px` (518,718 B) | `390×2400px` (321,655 B) | 25 | 16 | 284 | 107 | `0.10` / `0.47` | **25.0 / 25.0** |
| `www-velaaprivateisland-com` | `tier1_fast` | `1440×2400px` (2,000,758 B) | `390×2400px` (655,925 B) | 48 | 16 | 292 | 111 | `0.10` / `0.46` | **25.0 / 25.0** |
| `www-vibr-studio` | `tier1_fast` | `1440×900px` (774,988 B) | `390×2400px` (302,865 B) | 87 | 16 | 304 | 117 | `0.08` / `0.50` | **25.0 / 25.0** |
| `www-villiers-ai` | `tier1_fast` | `1440×900px` (1,381,996 B) | `390×2400px` (527,956 B) | 103 | 16 | 282 | 106 | `0.09` / `0.54` | **25.0 / 25.0** |
| `www-vineyard-co-za` | `tier1_fast` | `1440×900px` (1,745,257 B) | `390×2400px` (393,969 B) | 139 | 16 | 290 | 110 | `0.09` / `0.48` | **25.0 / 25.0** |
| `www-weisslameraner-com_en` | `tier1_fast` | `1440×2400px` (186,556 B) | `390×2400px` (242,773 B) | 152 | 16 | 290 | 110 | `0.10` / `0.56` | **25.0 / 25.0** |
| `www-worksruthi-com` | `tier1_fast` | `1440×2400px` (378,127 B) | `390×2400px` (204,550 B) | 117 | 16 | 294 | 112 | `0.11` / `0.53` | **25.0 / 25.0** |
| `www-xantium-com` | `tier1_fast` | `1440×2400px` (972,452 B) | `390×2400px` (407,644 B) | 43 | 16 | 284 | 107 | `0.11` / `0.56` | **25.0 / 25.0** |
| `www-zagrebwebusluge-com` | `tier1_fast` | `1440×2400px` (2,009,360 B) | `390×2400px` (504,260 B) | 84 | 16 | 296 | 113 | `0.09` / `0.48` | **25.0 / 25.0** |
| `www-vanguardinitiative-com` | `blocked` (`402`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 402 — Vercel Deployment Paused`)** |
