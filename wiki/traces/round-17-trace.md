# Round 17 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-17`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 17 Target Scope
  1. `heirest-com` — *HEIREST · Fine Jewellery, Authored By You* (`https://heirest.com/`)
  2. `helmetverse-ai` — *Helmetverse · Design yours* (`https://helmetverse.ai/`)
  3. `henrietta-wearetattoodigital-com` — *Henrietta Said : Scandalously Spicy* (`https://henrietta.wearetattoodigital.com/`)
  4. `henwoodcourt-co-uk` — *Henwood Court · Where financial freedom meets fulfilment* (`https://henwoodcourt.co.uk`)
  5. `herasymenkox-com` — *Yehor Herasymenko — Digital Designer* (`https://herasymenkox.com/`)
  6. `heronaiapp-com` — *Heron AI · Works inside your design tools* (`https://heronaiapp.com/`)
  7. `hole-money` — *Money Hole* (`https://hole.money`)
  8. `holmchrome-byholm-co` — *HOLMCHROME · Portrait Photography* (`https://holmchrome.byholm.co/`)
  9. `hopecancerresources-org` — *Hope Cancer Resources - Support. Educate. Prevent.* (`https://hopecancerresources.org/`)
  10. `hotelaurelia-online` — *Villa Aurelia — Butik Lüks Otel & Rezervasyon* (`https://hotelaurelia.online/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `heirest-com` | `1440×2400px` (85,922 B) | `390×2400px` (51,974 B) | 1464 | 16 | 256 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `helmetverse-ai` | `1440×2400px` (165,035 B) | `390×2400px` (101,974 B) | 193 | 16 | 274 | 115 | `0.09` / `0.50` | **25.0 / 25.0** |
| `henrietta-wearetattoodigital-com` | `1440×19740px` (1,036,992 B) | `390×2400px` (152,491 B) | 21 | 16 | 266 | 111 | `0.10` / `0.58` | **25.0 / 25.0** |
| `henwoodcourt-co-uk` | `1440×6820px` (3,965,165 B) | `390×2400px` (120,507 B) | 61 | 16 | 256 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `herasymenkox-com` | `1440×2400px` (1,047,586 B) | `390×2400px` (419,245 B) | 16 | 16 | 256 | 106 | `0.09` / `0.57` | **25.0 / 25.0** |
| `heronaiapp-com` | `1440×2400px` (52,261 B) | `390×2400px` (32,580 B) | 43 | 16 | 260 | 108 | `0.10` / `0.58` | **25.0 / 25.0** |
| `hole-money` | `1440×2400px` (1,463,064 B) | `390×2400px` (44,227 B) | 63 | 16 | 264 | 110 | `0.09` / `0.53` | **25.0 / 25.0** |
| `holmchrome-byholm-co` | `1440×2400px` (608,450 B) | `390×2400px` (287,393 B) | 2 | 14 | 252 | 104 | `0.09` / `0.57` | **25.0 / 25.0** |
| `hopecancerresources-org` | `1440×5575px` (1,664,373 B) | `390×2400px` (212,480 B) | 20 | 16 | 260 | 108 | `0.08` / `0.50` | **25.0 / 25.0** |
| `hotelaurelia-online` | `1440×10048px` (1,862,371 B) | `390×2400px` (47,022 B) | 86 | 16 | 256 | 106 | `0.09` / `0.52` | **25.0 / 25.0** |
