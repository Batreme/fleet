# Round 49 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-49`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 49 Target Scope
  1. `www-lapl-org` — *Homepage · Los Angeles Public Library* (`https://www.lapl.org/`)
  2. `www-leadoff-fr` — *Agence digitale à Vannes : web, mobile & acquisition · LEADOFF* (`https://www.leadoff.fr`)
  3. `www-lesgmstudios-com` — *GM Studios — Du contenu qui dépasse les chiffres* (`https://www.lesgmstudios.com/`)
  4. `www-lev-com` — *Lev · The AI platform for commercial real estate* (`https://www.lev.com/`)
  5. `www-lingers-it_en` — *Lingers – your hotel in Girlan* (`https://www.lingers.it/en`)
  6. `www-lucaslima-design` — *Lucas Lima · Product designer and design engineer* (`https://www.lucaslima.design/`)
  7. `www-mathildedechiara-com` — *Mathilde De Chiara, designer and interior architect* (`https://www.mathildedechiara.com/`)
  8. `www-mbidirectmail-com` — *Direct Mail & Digital Marketing · Customer Acquisition · MBI* (`https://www.mbidirectmail.com/`)
  9. `www-mdscollective-com` — *MDS Collective · China Marketing Agency for Hotels & Tourism* (`https://www.mdscollective.com`)
  10. `www-memedia-de` — *Webdesign München für nachhaltig denkende Unternehmer* (`https://www.memedia.de`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-lapl-org` | `1440×7428px` (4,068,158 B) | `390×2400px` (326,406 B) | 186 | 16 | 274 | 115 | `0.08` / `0.50` | **25.0 / 25.0** |
| `www-leadoff-fr` | `1440×10652px` (3,266,599 B) | `390×2400px` (35,995 B) | 24 | 16 | 256 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-lesgmstudios-com` | `1440×7873px` (3,765,295 B) | `390×2400px` (88,318 B) | 62 | 16 | 256 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-lev-com` | `1440×3365px` (1,548,274 B) | `390×2400px` (37,134 B) | 972 | 16 | 256 | 106 | `0.08` / `0.50` | **25.0 / 25.0** |
| `www-lingers-it_en` | `1440×13480px` (1,533,502 B) | `390×2400px` (436,693 B) | 32 | 16 | 256 | 106 | `0.08` / `0.48` | **25.0 / 25.0** |
| `www-lucaslima-design` | `1440×5927px` (141,585 B) | `390×2400px` (53,602 B) | 143 | 16 | 272 | 114 | `0.08` / `0.51` | **25.0 / 25.0** |
| `www-mathildedechiara-com` | `1440×2400px` (527,115 B) | `390×2400px` (243,709 B) | 30 | 16 | 253 | 103 | `0.10` / `0.53` | **25.0 / 25.0** |
| `www-mbidirectmail-com` | `1440×2400px` (65,471 B) | `390×2400px` (351,313 B) | 137 | 16 | 260 | 108 | `0.10` / `0.53` | **25.0 / 25.0** |
| `www-mdscollective-com` | `1440×17018px` (1,769,712 B) | `390×2400px` (80,081 B) | 15 | 16 | 266 | 111 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-memedia-de` | `1440×18690px` (5,534,183 B) | `390×2400px` (258,219 B) | 62 | 16 | 274 | 115 | `0.08` / `0.49` | **25.0 / 25.0** |
