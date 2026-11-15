# Round 10 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-10`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 10 Target Scope
  1. `cue-onebranding-webflow-io` — *Cue - Creating Unforgettable Experiences* (`https://cue-onebranding.webflow.io/`)
  2. `daddyyankee-com` — *Daddy Yankee · Official Website* (`https://daddyyankee.com/`)
  3. `daikifujita-com` — *Daiki Fujita — Web & Interactive Designer* (`https://daikifujita.com`)
  4. `dailymoscow-ru_mirpay` — *Спорт без лишних действий — Mir Pay × Daily Moscow* (`https://dailymoscow.ru/mirpay`)
  5. `dairyfoodbg-com` — *Dairy Food Bulgaria — Private-Label UHT Dairy Manufacturer* (`https://dairyfoodbg.com/`)
  6. `dark-moon-org` — *Darkmoon: Autonomous AI Penetration Testing Platform* (`https://dark-moon.org/`)
  7. `davaris-gr` — *Homepage - Davaris* (`https://davaris.gr/`)
  8. `davidcata-com_en-musica` — *Music — “Queridos todos:” and “Origen”, by David Catá* (`https://davidcata.com/en/musica/`)
  9. `dcspaces-co-uk` — *Chorley Builders · Extensions & Renovations · DC Carpentry* (`https://dcspaces.co.uk/`)
  10. `deadlyponies-com` — *Deadly Ponies - Luxury Leather Bags & Accessories* (`https://deadlyponies.com`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `cue-onebranding-webflow-io` | `1440×2400px` (166,335 B) | `390×2400px` (156,913 B) | 14 | 16 | 260 | 108 | `0.16` / `0.56` | **25.0 / 25.0** |
| `daddyyankee-com` | `1440×2400px` (1,014,825 B) | `390×2400px` (447,713 B) | 101 | 16 | 256 | 106 | `0.16` / `0.56` | **25.0 / 25.0** |
| `daikifujita-com` | `1440×2400px` (508,388 B) | `390×2400px` (258,512 B) | 60 | 16 | 258 | 107 | `0.09` / `0.54` | **25.0 / 25.0** |
| `dailymoscow-ru_mirpay` | `1440×13262px` (1,573,896 B) | `390×2400px` (296,312 B) | 22 | 16 | 268 | 112 | `0.08` / `0.54` | **25.0 / 25.0** |
| `dairyfoodbg-com` | `1440×22545px` (1,524,681 B) | `390×2400px` (35,690 B) | 167 | 16 | 256 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
| `dark-moon-org` | `1440×17311px` (1,096,171 B) | `390×2400px` (74,925 B) | 384 | 16 | 256 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `davaris-gr` | `1440×2400px` (45,031 B) | `390×2400px` (353,675 B) | 223 | 16 | 266 | 111 | `0.09` / `0.50` | **25.0 / 25.0** |
| `davidcata-com_en-musica` | `1440×15917px` (3,902,549 B) | `390×2400px` (98,387 B) | 12 | 16 | 256 | 106 | `0.09` / `0.53` | **25.0 / 25.0** |
| `dcspaces-co-uk` | `1440×11093px` (1,333,497 B) | `390×2400px` (33,602 B) | 29 | 16 | 258 | 107 | `0.09` / `0.53` | **25.0 / 25.0** |
| `deadlyponies-com` | `1440×3346px` (3,114,783 B) | `390×2400px` (223,791 B) | 530 | 16 | 256 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
