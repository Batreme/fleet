# Round 36 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-36`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 36 Target Scope
  1. `thecontenders-co` — *The Contenders · Strategic Brand & Design Consultancy* (`https://thecontenders.co/`)
  2. `thefwa-net` — *FWA Wire — winners' newswire* (`https://thefwa.net/`)
  3. `theimmortals-world` — *The Immortals* (`https://theimmortals.world/`)
  4. `theinfinitysocks-com` — *Infinity Socks — Performance Basketball Socks* (`https://theinfinitysocks.com/`)
  5. `thenest-pl_en` — *The Nest — a registered business address in central Warsaw* (`https://thenest.pl/en`)
  6. `theobromachocolat-com` — *Cure Your Chocolate Craving · Theobroma Chocolate* (`https://theobromachocolat.com/`)
  7. `theperformancelab-ca` — *The Performance Lab — Sports Science & Athletic Testing in Toronto* (`https://theperformancelab.ca/`)
  8. `therechabite-com-au` — *The Rechabite • Multi-level Palace of Surprise and Delight* (`https://therechabite.com.au/`)
  9. `thesovietflip-com` — *The Soviet Flip* (`https://thesovietflip.com/`)
  10. `thestudiobyjuliegranger-com` — *The Studio by Julie Granger* (`https://thestudiobyjuliegranger.com/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `thecontenders-co` | `1440×1312px` (100,425 B) | `390×2400px` (43,502 B) | 130 | 16 | 268 | 112 | `0.08` / `0.56` | **25.0 / 25.0** |
| `thefwa-net` | `1440×4035px` (592,227 B) | `390×2400px` (195,131 B) | 13 | 16 | 264 | 110 | `0.10` / `0.51` | **25.0 / 25.0** |
| `theimmortals-world` | `1440×2400px` (46,493 B) | `390×2400px` (112,470 B) | 0 | 12 | 244 | 100 | `0.10` / `0.51` | **25.0 / 25.0** |
| `theinfinitysocks-com` | `1440×2400px` (118,018 B) | `390×2400px` (44,887 B) | 174 | 16 | 256 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `thenest-pl_en` | `1440×2400px` (361,735 B) | `390×2400px` (190,107 B) | 138 | 16 | 270 | 113 | `0.09` / `0.49` | **25.0 / 25.0** |
| `theobromachocolat-com` | `1440×9412px` (2,207,521 B) | `390×2400px` (50,391 B) | 52 | 16 | 276 | 116 | `0.09` / `0.47` | **25.0 / 25.0** |
| `theperformancelab-ca` | `1440×10368px` (3,143,943 B) | `390×2400px` (139,677 B) | 37 | 16 | 256 | 106 | `0.10` / `0.58` | **25.0 / 25.0** |
| `therechabite-com-au` | `1440×2400px` (120,632 B) | `390×2400px` (41,305 B) | 73 | 16 | 256 | 106 | `0.10` / `0.58` | **25.0 / 25.0** |
| `thesovietflip-com` | `1440×2400px` (1,072,143 B) | `390×2400px` (457,962 B) | 33 | 16 | 256 | 106 | `0.10` / `0.50` | **25.0 / 25.0** |
| `thestudiobyjuliegranger-com` | `1440×14258px` (1,218,185 B) | `390×2400px` (44,632 B) | 27 | 16 | 256 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
