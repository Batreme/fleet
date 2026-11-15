# Round 14 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-14`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `8` (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 14 Target Scope
  1. `explorewashingtonpark-org` — *Explore Washington Park* (`https://explorewashingtonpark.org`)
  2. `exspeedia-com` — *Official IShowSpeed Travel Site Powered by Expedia* (`https://exspeedia.com`)
  3. `f-list-cleancreatives-org` — *F-List 2026* (`https://f-list.cleancreatives.org/`)
  4. `fabiantjoeaon-com` — *Fabian Tjoe-A-On — Creative technologist* (`https://fabiantjoeaon.com`)
  5. `faithibiza-com` — *Faith Ibiza · VIP Ibiza Concierge Services* (`https://faithibiza.com/`)
  6. `familyservicelincoln-org` — *Family Service Lincoln: Everyone Deserves the Chance to Thrive* (`https://familyservicelincoln.org`)
  7. `fighterready-com` — *Fighter Ready — UK Combat Sports Matchmaking Platform* (`https://fighterready.com/`)
  8. `filmmaker-framer-media` — *Blocked (`Upstream HTTP 404 (Site Not Found | Framer)`)*
  9. `findra-art` — *Findra: the AI character feed* (`https://findra.art/`)
  10. `fineacts-co` — *Blocked (`Empty raw DOM capture (39 bytes, 0 stylesheets)`)*

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `explorewashingtonpark-org` | `1440×2400px` (712,416 B) | `390×2400px` (334,951 B) | 1364 | 16 | 264 | 110 | `0.09` / `0.48` | **25.0 / 25.0** |
| `exspeedia-com` | `1440×2400px` (714,944 B) | `390×2400px` (172,412 B) | 398 | 16 | 255 | 105 | `0.12` / `0.47` | **25.0 / 25.0** |
| `f-list-cleancreatives-org` | `1440×9151px` (1,349,892 B) | `390×2400px` (198,503 B) | 56 | 16 | 256 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `fabiantjoeaon-com` | `1440×2400px` (57,075 B) | `390×2400px` (42,526 B) | 30 | 16 | 256 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `faithibiza-com` | `1440×2400px` (162,663 B) | `390×2400px` (252,333 B) | 242 | 16 | 256 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `familyservicelincoln-org` | `1440×4818px` (1,318,530 B) | `390×2400px` (99,129 B) | 39 | 16 | 260 | 108 | `0.09` / `0.48` | **25.0 / 25.0** |
| `fighterready-com` | `1440×12742px` (128,485 B) | `390×2400px` (68,215 B) | 20 | 16 | 270 | 113 | `0.09` / `0.50` | **25.0 / 25.0** |
| `filmmaker-framer-media` | `status: blocked` | `status: blocked` | — | — | — | — | — | **Excluded (`Upstream HTTP 404 (Site Not Found | Framer)`)** |
| `findra-art` | `1440×2400px` (1,253,347 B) | `390×2400px` (396,346 B) | 59 | 16 | 256 | 106 | `0.12` / `0.47` | **25.0 / 25.0** |
| `fineacts-co` | `status: blocked` | `status: blocked` | — | — | — | — | — | **Excluded (`Empty raw DOM capture (39 bytes, 0 stylesheets)`)** |
