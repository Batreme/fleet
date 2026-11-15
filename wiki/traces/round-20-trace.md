# Round 20 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-20`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 20 Target Scope
  1. `kamdalej-sk_en` — *Mastercard · Where Next* (`https://kamdalej.sk/en`)
  2. `karma-tracks-com` — *karma tracks* (`https://karma-tracks.com/`)
  3. `kelvin-8b-com` — *Kelvin — three nights of music, filmed in heat* (`https://kelvin.8b.com/`)
  4. `key-co` — *KEY.co · Luxury Vacation Home Rentals + Concierge Services* (`https://key.co/`)
  5. `kindi-land` — *Kindi & Kitir — a confectionery manufacturer in Turkmenistan* (`https://kindi.land/`)
  6. `kingriver-com-au` — *Australian Wagyu Beef · King River Legendary Wagyu* (`https://kingriver.com.au/`)
  7. `kinoria-studio` — *KINORIA* (`https://kinoria.studio/`)
  8. `kissbranding-co-uk` — *Kiss · Brands that Kiss* (`https://kissbranding.co.uk/`)
  9. `klad-design` — *Multidisciplinary Design Syndicate – KLAD* (`https://klad.design/`)
  10. `kohenavocats-com_avocats-droit-famille-paris` — *Avocat Droit de la Famille Paris · Divorce, Garde d'Enfants, Succession* (`https://kohenavocats.com/avocats-droit-famille-paris/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `kamdalej-sk_en` | `1440×5687px` (1,343,627 B) | `390×2400px` (164,879 B) | 149 | 16 | 256 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `karma-tracks-com` | `1440×2400px` (658,275 B) | `390×2400px` (300,967 B) | 77 | 16 | 272 | 114 | `0.09` / `0.56` | **25.0 / 25.0** |
| `kelvin-8b-com` | `1440×17000px` (2,384,209 B) | `390×2400px` (134,703 B) | 23 | 16 | 266 | 111 | `0.09` / `0.51` | **25.0 / 25.0** |
| `key-co` | `1440×2400px` (53,068 B) | `390×2400px` (36,462 B) | 118 | 16 | 256 | 106 | `0.11` / `0.49` | **25.0 / 25.0** |
| `kindi-land` | `1440×2400px` (1,067,854 B) | `390×2400px` (415,898 B) | 167 | 16 | 256 | 106 | `0.09` / `0.56` | **25.0 / 25.0** |
| `kingriver-com-au` | `1440×10193px` (597,246 B) | `390×2400px` (436,862 B) | 51 | 16 | 256 | 106 | `0.10` / `0.54` | **25.0 / 25.0** |
| `kinoria-studio` | `1440×2400px` (1,517,156 B) | `390×2400px` (552,589 B) | 1 | 13 | 249 | 102 | `0.10` / `0.50` | **25.0 / 25.0** |
| `kissbranding-co-uk` | `1440×2400px` (411,797 B) | `390×2400px` (236,157 B) | 95 | 16 | 256 | 106 | `0.13` / `0.56` | **25.0 / 25.0** |
| `klad-design` | `1440×6793px` (1,577,816 B) | `390×2400px` (194,397 B) | 68 | 16 | 256 | 106 | `0.13` / `0.56` | **25.0 / 25.0** |
| `kohenavocats-com_avocats-droit-famille-paris` | `1440×2400px` (331,323 B) | `390×2400px` (270,895 B) | 298 | 16 | 256 | 106 | `0.10` / `0.48` | **25.0 / 25.0** |
