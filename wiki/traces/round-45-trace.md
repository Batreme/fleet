# Round 45 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-45`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 45 Target Scope
  1. `www-dontlookup-app` — *Don't Look Up — a game about keeping everyone looking down* (`https://www.dontlookup.app/`)
  2. `www-east64films-com` — *EAST 64 Films · Tokyo-Based International Production Company* (`https://www.east64films.com/`)
  3. `www-easyseller-it` — *EASYSELLER · Sales Digital Agency* (`https://www.easyseller.it/`)
  4. `www-emblematica-agency` — *emblematica — concept-led brand & web design agency in barcelona* (`https://www.emblematica.agency`)
  5. `www-enigmascult-com` — *Enigma – Sneaker Auctions, Mystery Boxes & Reborn Customs* (`https://www.enigmascult.com/`)
  6. `www-era-residence-com` — *ERA Residence — Contemporary Mediterranean Residences in Estepona* (`https://www.era-residence.com/`)
  7. `www-esrbespoke-au` — *ESR* (`https://www.esrbespoke.au/`)
  8. `www-extrafazant-nl` — *Extrafazant · Social Content, Video's & Animatie* (`https://www.extrafazant.nl/`)
  9. `www-feelreformed-com` — *Reformed: The biggest thing to happen to Coffee since Coffee.* (`https://www.feelreformed.com/`)
  10. `www-fiabamia-com` — *FiabaMia — Personalized bedtime stories for children* (`https://www.fiabamia.com/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-dontlookup-app` | `1440×2400px` (1,656,871 B) | `390×2400px` (560,811 B) | 20 | 16 | 260 | 108 | `0.09` / `0.53` | **25.0 / 25.0** |
| `www-east64films-com` | `1440×2400px` (184,403 B) | `390×2400px` (43,082 B) | 111 | 16 | 266 | 111 | `0.09` / `0.53` | **25.0 / 25.0** |
| `www-easyseller-it` | `1440×2400px` (1,072,403 B) | `390×2400px` (338,858 B) | 451 | 16 | 276 | 116 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-emblematica-agency` | `1440×47561px` (4,183,999 B) | `390×2400px` (437,728 B) | 60 | 16 | 256 | 106 | `0.09` / `0.53` | **25.0 / 25.0** |
| `www-enigmascult-com` | `1440×11069px` (2,670,151 B) | `390×2400px` (67,086 B) | 101 | 16 | 266 | 111 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-era-residence-com` | `1440×2400px` (50,010 B) | `390×2400px` (450,147 B) | 202 | 16 | 256 | 106 | `0.11` / `0.58` | **25.0 / 25.0** |
| `www-esrbespoke-au` | `1440×7770px` (1,053,498 B) | `390×2400px` (246,065 B) | 8 | 16 | 254 | 105 | `0.09` / `0.53` | **25.0 / 25.0** |
| `www-extrafazant-nl` | `1440×9447px` (1,737,941 B) | `390×2400px` (89,878 B) | 166 | 16 | 256 | 106 | `0.11` / `0.58` | **25.0 / 25.0** |
| `www-feelreformed-com` | `1440×4311px` (2,346,094 B) | `390×2400px` (353,210 B) | 1313 | 16 | 256 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-fiabamia-com` | `1440×2400px` (2,866,309 B) | `390×2400px` (899,956 B) | 185 | 16 | 266 | 111 | `0.09` / `0.51` | **25.0 / 25.0** |
