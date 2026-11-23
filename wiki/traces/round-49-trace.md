# Round 49 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-49`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `10` live (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 49 Target Scope
  1. `www-lapl-org` — *Homepage · Los Angeles Public Library*
  2. `www-leadoff-fr` — *Agence digitale à Vannes : web, mobile & acquisition · LEADOFF*
  3. `www-lesgmstudios-com` — *GM Studios — Du contenu qui dépasse les chiffres*
  4. `www-lev-com` — *Lev · The AI platform for commercial real estate*
  5. `www-lingers-it_en` — *Lingers – your hotel in Girlan*
  6. `www-lucaslima-design` — *Lucas Lima · Product designer and design engineer*
  7. `www-mathildedechiara-com` — *Mathilde De Chiara, designer and interior architect*
  8. `www-mbidirectmail-com` — *Direct Mail & Digital Marketing · Customer Acquisition · MBI*
  9. `www-mdscollective-com` — *MDS Collective · China Marketing Agency for Hotels & Tourism*
  10. `www-memedia-de` — *Webdesign München für nachhaltig denkende Unternehmer*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-lapl-org` | `tier1_fast` | `1440×2400px` (1,560,887 B) | `390×2400px` (390,519 B) | 188 | 16 | 312 | 121 | `0.09` / `0.48` | **25.0 / 25.0** |
| `www-leadoff-fr` | `tier1_fast` | `1440×2400px` (96,417 B) | `390×2400px` (65,585 B) | 24 | 16 | 292 | 111 | `0.10` / `0.48` | **25.0 / 25.0** |
| `www-lesgmstudios-com` | `tier1_fast` | `1440×2400px` (1,992,767 B) | `390×2400px` (636,391 B) | 64 | 16 | 284 | 107 | `0.10` / `0.48` | **25.0 / 25.0** |
| `www-lev-com` | `tier1_fast` | `1440×2400px` (1,445,856 B) | `390×2400px` (400,474 B) | 1012 | 16 | 282 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `www-lingers-it_en` | `tier1_fast` | `1440×2400px` (1,786,267 B) | `390×2400px` (616,060 B) | 32 | 16 | 282 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-lucaslima-design` | `tier1_fast` | `1440×2400px` (1,006,390 B) | `390×2400px` (288,200 B) | 143 | 16 | 306 | 118 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-mathildedechiara-com` | `tier1_fast` | `1440×900px` (317,541 B) | `390×844px` (196,573 B) | 30 | 16 | 279 | 103 | `0.10` / `0.52` | **25.0 / 25.0** |
| `www-mbidirectmail-com` | `tier1_fast` | `1440×2400px` (93,658 B) | `390×844px` (23,264 B) | 137 | 16 | 296 | 113 | `0.10` / `0.52` | **25.0 / 25.0** |
| `www-mdscollective-com` | `tier1_fast` | `1440×2400px` (2,228,107 B) | `390×2400px` (444,852 B) | 15 | 16 | 292 | 111 | `0.09` / `0.51` | **25.0 / 25.0** |
| `www-memedia-de` | `tier1_fast` | `1440×2400px` (1,201,350 B) | `390×2400px` (454,857 B) | 62 | 16 | 300 | 115 | `0.09` / `0.50` | **25.0 / 25.0** |
