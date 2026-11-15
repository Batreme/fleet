# Round 46 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-46`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 46 Target Scope
  1. `www-fieldrank-run` — *FieldRank: Trail and ultra rankings* (`https://www.fieldrank.run`)
  2. `www-fixchocolatier-com` — *FIX Dessert Chocolatier · The Original Dubai Chocolate* (`https://www.fixchocolatier.com/`)
  3. `www-flatlineagency-com` — *Shopify, Marketing & AI Agency Amsterdam · Flatline* (`https://www.flatlineagency.com/`)
  4. `www-fragment-im` — *Fragment Studio · Independent Designer for Visual Identity, Websites & P...* (`https://www.fragment.im`)
  5. `www-future-human-de` — *FUTURE HUMAN · A Shared Year of Co-Creation & Presence* (`https://www.future-human.de/`)
  6. `www-genomines-com` — *Home* (`https://www.genomines.com/`)
  7. `www-gerd-web-de` — *Gerd Web 3 Second - Design* (`https://www.gerd-web.de`)
  8. `www-get-daffed-com` — *Dafne Salvatori · Brand, design and marketing, Europe* (`https://www.get-daffed.com/`)
  9. `www-gianpaolotucci-com_work-html` — *Gianpaolo Tucci — Creative Director, Berlin · AI-native experiences* (`https://www.gianpaolotucci.com/work.html`)
  10. `www-glowingcheetah-com` — *Glowing Cheetah Studios · Father & Son Indie Game Studio* (`https://www.glowingcheetah.com/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-fieldrank-run` | `1440×1266px` (153,246 B) | `390×2400px` (150,480 B) | 89 | 16 | 256 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `www-fixchocolatier-com` | `1440×2400px` (461,270 B) | `390×2400px` (243,741 B) | 16 | 16 | 258 | 107 | `0.09` / `0.51` | **25.0 / 25.0** |
| `www-flatlineagency-com` | `1440×7042px` (579,707 B) | `390×2400px` (274,287 B) | 48 | 16 | 266 | 111 | `0.10` / `0.58` | **25.0 / 25.0** |
| `www-fragment-im` | `1440×2400px` (61,773 B) | `390×2400px` (32,172 B) | 35 | 16 | 260 | 108 | `0.09` / `0.61` | **25.0 / 25.0** |
| `www-future-human-de` | `1440×2400px` (485,493 B) | `390×2400px` (224,022 B) | 30 | 16 | 258 | 107 | `0.10` / `0.61` | **25.0 / 25.0** |
| `www-genomines-com` | `1440×2400px` (462,119 B) | `390×2400px` (269,022 B) | 22 | 16 | 256 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
| `www-gerd-web-de` | `1440×2574px` (544,001 B) | `390×2400px` (267,753 B) | 23 | 16 | 258 | 107 | `0.09` / `0.47` | **25.0 / 25.0** |
| `www-get-daffed-com` | `1440×4331px` (337,049 B) | `390×2400px` (116,854 B) | 39 | 16 | 268 | 112 | `0.08` / `0.53` | **25.0 / 25.0** |
| `www-gianpaolotucci-com_work-html` | `1440×2400px` (161,129 B) | `390×2400px` (399,005 B) | 17 | 16 | 258 | 107 | `0.09` / `0.53` | **25.0 / 25.0** |
| `www-glowingcheetah-com` | `1440×2400px` (900,279 B) | `390×2400px` (689,976 B) | 84 | 16 | 260 | 108 | `0.09` / `0.49` | **25.0 / 25.0** |
