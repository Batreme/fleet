# Round 07 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-07`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `10` live (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 07 Target Scope
  1. `bettr-academy` — *Bettr Academy · World-Class Barista & Coffee Training*
  2. `biipmk-com` — *biipmk*
  3. `bluntumbrellas-com` — *BLUNT Umbrellas · Built to Resist Every Weather*
  4. `book-sequel-co` — *The First Fifty*
  5. `booleansequence-niceunderground-xyz` — *booleanSequence · generative art by niceunderground*
  6. `boomballtour-com` — *Boom Ball Baseball · The Ultimate Family Sports Experience*
  7. `both-sides-the7eye-org-il_en` — *Extremists on Both Sides*
  8. `brand-helloasso-com` — *Accueil – Brandbook HelloAsso*
  9. `brandonyasin-com` — *Brandon Yasin — Creative Director & Designer*
  10. `bright-avenue-jp` — *株式会社ブライトアベニュー · 不動産買取再販事業・リノベーション事業*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `bettr-academy` | `tier1_fast` | `1440×2400px` (1,199,602 B) | `390×2400px` (343,219 B) | 104 | 16 | 292 | 111 | `0.09` / `0.53` | **25.0 / 25.0** |
| `biipmk-com` | `tier1_fast` | `1440×2400px` (136,413 B) | `390×2400px` (207,757 B) | 45 | 16 | 300 | 114 | `0.09` / `0.53` | **25.0 / 25.0** |
| `bluntumbrellas-com` | `tier1_fast` | `1440×2400px` (1,462,895 B) | `390×2400px` (523,129 B) | 1035 | 16 | 283 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `book-sequel-co` | `tier1_fast` | `1440×900px` (151,364 B) | `390×844px` (26,173 B) | 36 | 16 | 286 | 108 | `0.09` / `0.55` | **25.0 / 25.0** |
| `booleansequence-niceunderground-xyz` | `tier1_fast` | `1440×2400px` (107,567 B) | `390×2400px` (29,935 B) | 10 | 16 | 282 | 106 | `0.09` / `0.53` | **25.0 / 25.0** |
| `boomballtour-com` | `tier1_fast` | `1440×2400px` (2,175,573 B) | `390×2400px` (820,713 B) | 586 | 16 | 295 | 112 | `0.09` / `0.50` | **25.0 / 25.0** |
| `both-sides-the7eye-org-il_en` | `tier2_webgl` | `1440×900px` (34,513 B) | `390×844px` (22,577 B) | 91 | 16 | 284 | 107 | `0.09` / `0.52` | **25.0 / 25.0** |
| `brand-helloasso-com` | `tier2_webgl` | `1440×900px` (38,526 B) | `390×844px` (8,225 B) | 262 | 16 | 306 | 117 | `0.09` / `0.55` | **25.0 / 25.0** |
| `brandonyasin-com` | `tier1_fast` | `1440×900px` (134,936 B) | `390×844px` (61,379 B) | 18 | 16 | 288 | 109 | `0.10` / `0.54` | **25.0 / 25.0** |
| `bright-avenue-jp` | `tier2_webgl` | `1440×900px` (868,549 B) | `390×844px` (348,239 B) | 159 | 16 | 290 | 110 | `0.10` / `0.55` | **25.0 / 25.0** |
