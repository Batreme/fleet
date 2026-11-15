# Round 41 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-41`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 41 Target Scope
  1. `www-3moons-it` — *3Moons Studio · App mobile, software enterprise e AI su misura* (`https://www.3moons.it`)
  2. `www-aaronbrimhall-com` — *Aaron Brimhall · Action & Automotive Photographer* (`https://www.aaronbrimhall.com/`)
  3. `www-aat-architecten-be` — *AAT Architecten* (`https://www.aat-architecten.be/`)
  4. `www-agencejacquesparis-fr` — *Jacques Paris - Agence à impact positif* (`https://www.agencejacquesparis.fr/`)
  5. `www-agrumeafarm-it_en` — *Agrumea Farm · Jams, pestos and flavours of Sicily* (`https://www.agrumeafarm.it/en`)
  6. `www-alexadevaney-com` — *North County San Diego Luxury Homes – Alexa Devaney* (`https://www.alexadevaney.com/`)
  7. `www-allerstudio-com` — *ALLER Studio — Product design and development studio* (`https://www.allerstudio.com/`)
  8. `www-alpineguides-co-nz` — *Alpine Guides Aoraki · NZ Mountain Guiding Since 1966* (`https://www.alpineguides.co.nz/`)
  9. `www-amberjs-dev` — *Amber — Scroll & Motion Toolkit* (`https://www.amberjs.dev/`)
  10. `www-andriimur-com` — *Andrii Mur* (`https://www.andriimur.com/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-3moons-it` | `1440×7272px` (3,652,811 B) | `390×2400px` (529,068 B) | 17 | 16 | 262 | 109 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-aaronbrimhall-com` | `1440×6239px` (1,565,934 B) | `390×2400px` (242,630 B) | 26 | 16 | 256 | 106 | `0.10` / `0.56` | **25.0 / 25.0** |
| `www-aat-architecten-be` | `1440×4660px` (345,896 B) | `390×2400px` (174,315 B) | 148 | 16 | 256 | 106 | `0.10` / `0.46` | **25.0 / 25.0** |
| `www-agencejacquesparis-fr` | `1440×2400px` (46,500 B) | `390×2400px` (38,637 B) | 21 | 16 | 256 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-agrumeafarm-it_en` | `1440×2400px` (678,341 B) | `390×2400px` (361,529 B) | 66 | 16 | 256 | 106 | `0.10` / `0.49` | **25.0 / 25.0** |
| `www-alexadevaney-com` | `1440×2400px` (112,111 B) | `390×2400px` (58,062 B) | 17 | 16 | 256 | 106 | `0.10` / `0.50` | **25.0 / 25.0** |
| `www-allerstudio-com` | `1440×2400px` (332,545 B) | `390×2400px` (115,100 B) | 78 | 16 | 256 | 106 | `0.10` / `0.53` | **25.0 / 25.0** |
| `www-alpineguides-co-nz` | `1440×2400px` (61,859 B) | `390×2400px` (32,280 B) | 234 | 16 | 256 | 106 | `0.10` / `0.56` | **25.0 / 25.0** |
| `www-amberjs-dev` | `1440×2400px` (85,869 B) | `390×2400px` (400,064 B) | 48 | 16 | 256 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-andriimur-com` | `1440×8019px` (3,390,209 B) | `390×2400px` (37,702 B) | 138 | 16 | 266 | 111 | `0.09` / `0.53` | **25.0 / 25.0** |
