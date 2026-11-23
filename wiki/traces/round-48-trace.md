# Round 48 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-48`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `10` live (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 48 Target Scope
  1. `www-imersion-io` — *Imersion — Get Immersed in the World's Most Beautiful Places*
  2. `www-impastofornoantico-com` — *Handcrafted Bread with Soul - Impasto*
  3. `www-incroy-com` — *Incroy · Webflow Certified Development Agency*
  4. `www-jarnket-com` — *JarnKet · Ketsadaphone Boutpanyda, web engineer in Vientiane*
  5. `www-jasmin-karatas-ch` — *Jasmin Deniz Karatas – Product Designer, Gamification Specialist & Keyno...*
  6. `www-johnbolster-design` — *John Bolster · Brand Identity Designer and Art Director, Saratoga Spring...*
  7. `www-kaviengcreative-com` — *Kavieng Cheng · Art Director and Creative*
  8. `www-killstar-com` — *KILLSTAR*
  9. `www-kubehotel-saint-tropez-com_fr` — *Layne Saint-Tropez, hôtel 5 étoiles : ouverture le 1er mai 2027*
  10. `www-lamagadan-studio` — *La Magadán · Branding y diseño para emprendedoras*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-imersion-io` | `tier1_fast` | `1440×2400px` (3,144,797 B) | `390×2400px` (865,263 B) | 28 | 16 | 304 | 117 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-impastofornoantico-com` | `tier1_fast` | `1440×2400px` (714,584 B) | `390×2400px` (311,913 B) | 236 | 16 | 282 | 106 | `0.11` / `0.57` | **25.0 / 25.0** |
| `www-incroy-com` | `tier2_webgl` | `1440×900px` (129,960 B) | `390×2400px` (81,726 B) | 84 | 16 | 282 | 106 | `0.12` / `0.57` | **25.0 / 25.0** |
| `www-jarnket-com` | `tier2_webgl` | `1440×900px` (265,763 B) | `390×844px` (20,780 B) | 87 | 16 | 282 | 106 | `0.10` / `0.52` | **25.0 / 25.0** |
| `www-jasmin-karatas-ch` | `tier2_webgl` | `1440×900px` (1,801,751 B) | `390×844px` (490,338 B) | 91 | 16 | 288 | 109 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-johnbolster-design` | `tier2_webgl` | `1440×900px` (56,752 B) | `390×844px` (28,624 B) | 22 | 16 | 288 | 109 | `0.10` / `0.53` | **25.0 / 25.0** |
| `www-kaviengcreative-com` | `tier1_fast` | `1440×900px` (127,596 B) | `390×844px` (49,336 B) | 10 | 16 | 288 | 109 | `0.09` / `0.53` | **25.0 / 25.0** |
| `www-killstar-com` | `tier1_fast` | `1440×2400px` (1,830,379 B) | `390×2400px` (549,765 B) | 224 | 16 | 309 | 119 | `0.10` / `0.49` | **25.0 / 25.0** |
| `www-kubehotel-saint-tropez-com_fr` | `tier1_fast` | `1440×900px` (1,481,936 B) | `390×844px` (211,529 B) | 160 | 16 | 283 | 106 | `0.12` / `0.54` | **25.0 / 25.0** |
| `www-lamagadan-studio` | `tier1_fast` | `1440×2400px` (464,296 B) | `390×2400px` (141,568 B) | 0 | 12 | 274 | 102 | `0.10` / `0.52` | **25.0 / 25.0** |
