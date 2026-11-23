# Round 14 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-14`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 14 Target Scope
  1. `explorewashingtonpark-org` — *Explore Washington Park*
  2. `exspeedia-com` — *Official IShowSpeed Travel Site Powered by Expedia*
  3. `f-list-cleancreatives-org` — *F-List 2026*
  4. `fabiantjoeaon-com` — *Fabian Tjoe-A-On — Creative technologist*
  5. `faithibiza-com` — *Faith Ibiza · VIP Ibiza Concierge Services*
  6. `familyservicelincoln-org` — *Family Service Lincoln: Everyone Deserves the Chance to Thrive*
  7. `fighterready-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  8. `filmmaker-framer-media` — *Filmmaker — Portfolio for Directors & Studios*
  9. `findra-art` — *Findra: the AI character feed*
  10. `fineacts-co` — *Blocked (`Network/Navigation failure (Page.goto: net::ERR_EMPTY_RESPONSE at https://fineacts.co/ Call log: - navigating to 'https://fineacts.co/', waiting until 'domcontentload)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `explorewashingtonpark-org` | `tier1_fast` | `1440×2400px` (3,014,554 B) | `390×2400px` (719,496 B) | 1364 | 16 | 283 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `exspeedia-com` | `tier2_webgl` | `1440×900px` (427,864 B) | `390×844px` (132,862 B) | 398 | 16 | 280 | 103 | `0.09` / `0.47` | **25.0 / 25.0** |
| `f-list-cleancreatives-org` | `tier1_fast` | `1440×2400px` (728,673 B) | `390×2400px` (214,109 B) | 56 | 16 | 292 | 111 | `0.09` / `0.48` | **25.0 / 25.0** |
| `fabiantjoeaon-com` | `tier1_fast` | `1440×900px` (73,391 B) | `390×844px` (52,133 B) | 30 | 16 | 282 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `faithibiza-com` | `tier1_fast` | `1440×2400px` (365,926 B) | `390×2400px` (188,391 B) | 89 | 16 | 294 | 112 | `0.11` / `0.52` | **25.0 / 25.0** |
| `familyservicelincoln-org` | `tier1_fast` | `1440×2400px` (1,674,697 B) | `390×2400px` (438,486 B) | 39 | 16 | 292 | 111 | `0.11` / `0.52` | **25.0 / 25.0** |
| `filmmaker-framer-media` | `tier2_webgl` | `1440×900px` (724,732 B) | `390×844px` (215,291 B) | 29 | 16 | 288 | 108 | `0.09` / `0.50` | **25.0 / 25.0** |
| `findra-art` | `tier1_fast` | `1440×2400px` (940,688 B) | `390×2400px` (288,245 B) | 59 | 16 | 296 | 113 | `0.09` / `0.47` | **25.0 / 25.0** |
| `fighterready-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `fineacts-co` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: net::ERR_EMPTY_RESPONSE at http`)** |
