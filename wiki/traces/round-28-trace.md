# Round 28 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-28`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 28 Target Scope
  1. `opportunity-waltonfamilyfoundation-org` — *Access to Opportunity: Gallup Research · Walton Family Foundation* (`https://opportunity.waltonfamilyfoundation.org/`)
  2. `overworldaudio-com` — *Overworld Audio* (`https://overworldaudio.com/`)
  3. `palaceskateboards-com` — *PALACE SKATEBOARDS* (`https://palaceskateboards.com/`)
  4. `palominoprod-com` — *Palomino — Cinematic Sports & Brand Films* (`https://palominoprod.com/`)
  5. `pankow-band` — *Die Pankow Zeitmaschine - Website der Berliner Rockband PANKOW* (`https://pankow.band`)
  6. `patmos-studio` — *Patmos · Wahr, Gut, Schön* (`https://patmos.studio/`)
  7. `pda-archi_en` — *Architecture firm in Paris: renovation, refurbishment — PDA* (`https://pda.archi/en`)
  8. `peabodyhouse-com` — *Peabody House • Digital Brand World Implementation Studio* (`https://peabodyhouse.com`)
  9. `peaches-world` — *Peaches – Webdesign Pratteln, Basel · Websites worth pressing Enter for* (`https://peaches.world/`)
  10. `perappelgren-de` — *Per Appelgren* (`https://perappelgren.de/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `opportunity-waltonfamilyfoundation-org` | `1440×2400px` (410,051 B) | `390×2400px` (224,505 B) | 73 | 16 | 256 | 106 | `0.13` / `0.60` | **25.0 / 25.0** |
| `overworldaudio-com` | `1440×2400px` (988,623 B) | `390×2400px` (450,900 B) | 25 | 16 | 256 | 106 | `0.09` / `0.53` | **25.0 / 25.0** |
| `palaceskateboards-com` | `1440×1276px` (1,012,263 B) | `390×2400px` (223,947 B) | 81 | 16 | 256 | 106 | `0.12` / `0.57` | **25.0 / 25.0** |
| `palominoprod-com` | `1440×8375px` (1,551,050 B) | `390×2400px` (345,631 B) | 68 | 16 | 268 | 112 | `0.10` / `0.55` | **25.0 / 25.0** |
| `pankow-band` | `1440×2400px` (473,427 B) | `390×2400px` (255,259 B) | 31 | 16 | 256 | 106 | `0.10` / `0.47` | **25.0 / 25.0** |
| `patmos-studio` | `1440×2400px` (626,765 B) | `390×2400px` (340,399 B) | 72 | 16 | 255 | 105 | `0.13` / `0.54` | **25.0 / 25.0** |
| `pda-archi_en` | `1440×2400px` (1,240,046 B) | `390×2400px` (75,912 B) | 133 | 16 | 256 | 106 | `0.10` / `0.56` | **25.0 / 25.0** |
| `peabodyhouse-com` | `1440×6542px` (812,918 B) | `390×2400px` (36,344 B) | 53 | 16 | 258 | 107 | `0.09` / `0.53` | **25.0 / 25.0** |
| `peaches-world` | `1440×2400px` (503,070 B) | `390×2400px` (238,088 B) | 0 | 12 | 245 | 99 | `0.10` / `0.53` | **25.0 / 25.0** |
| `perappelgren-de` | `1440×2400px` (635,650 B) | `390×2400px` (229,378 B) | 30 | 16 | 256 | 106 | `0.11` / `0.60` | **25.0 / 25.0** |
