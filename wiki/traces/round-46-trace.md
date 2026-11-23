# Round 46 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-46`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 46 Target Scope
  1. `www-fieldrank-run` — *FieldRank: Trail and ultra rankings*
  2. `www-fixchocolatier-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  3. `www-flatlineagency-com` — *Shopify, Marketing & AI Agency Amsterdam · Flatline*
  4. `www-fragment-im` — *Fragment Studio · Independent Designer for Visual Identity, Websites & P...*
  5. `www-future-human-de` — *FUTURE HUMAN · A Shared Year of Co-Creation & Presence*
  6. `www-genomines-com` — *Genomines — We Grow Metal*
  7. `www-gerd-web-de` — *Gerd Web 3 Second - Design*
  8. `www-get-daffed-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  9. `www-gianpaolotucci-com_work-html` — *Gianpaolo Tucci — Creative Director, Berlin · AI-native experiences*
  10. `www-glowingcheetah-com` — *Glowing Cheetah Studios · Father & Son Indie Game Studio*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-fieldrank-run` | `tier1_fast` | `1440×1266px` (151,889 B) | `390×2400px` (136,964 B) | 89 | 16 | 288 | 109 | `0.08` / `0.49` | **25.0 / 25.0** |
| `www-flatlineagency-com` | `tier1_fast` | `1440×2400px` (96,363 B) | `390×2400px` (59,460 B) | 48 | 16 | 298 | 114 | `0.11` / `0.56` | **25.0 / 25.0** |
| `www-fragment-im` | `tier1_fast` | `1440×2400px` (177,029 B) | `390×2400px` (77,579 B) | 35 | 16 | 292 | 111 | `0.11` / `0.56` | **25.0 / 25.0** |
| `www-future-human-de` | `tier1_fast` | `1440×900px` (169,380 B) | `390×844px` (49,465 B) | 30 | 16 | 286 | 108 | `0.10` / `0.56` | **25.0 / 25.0** |
| `www-genomines-com` | `tier2_webgl` | `1440×900px` (705,685 B) | `390×844px` (185,663 B) | 22 | 16 | 282 | 106 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-gerd-web-de` | `tier1_fast` | `1440×2400px` (525,590 B) | `390×2400px` (193,220 B) | 23 | 16 | 290 | 110 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-gianpaolotucci-com_work-html` | `tier2_webgl` | `1440×900px` (83,692 B) | `390×844px` (19,034 B) | 17 | 16 | 290 | 110 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-glowingcheetah-com` | `tier1_fast` | `1440×2400px` (3,310,871 B) | `390×2400px` (1,210,163 B) | 84 | 16 | 292 | 111 | `0.08` / `0.49` | **25.0 / 25.0** |
| `www-fixchocolatier-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `www-get-daffed-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
