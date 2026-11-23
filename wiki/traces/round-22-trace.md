# Round 22 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-22`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 22 Target Scope
  1. `layrmedia-com` — *LAYR Media · Creative Photography & Videography Studio*
  2. `lcg-media` — *LCG · The Agency That Fights for American Families*
  3. `legacybridge-software` — *AI Document Entry for AS/400 & Legacy Systems · LegacyBridge*
  4. `lenvalproperties-com` — *Lenval Properties — Creators of Refined Living & Iconic Spaces*
  5. `levigav-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  6. `lfs-org-uk` — *London Film School*
  7. `lifetimepastapass-com` — *LIFETIME PASTA PASS · BRADEN'S INFINITE TOUR OF ITALY*
  8. `lofliballs-com` — *LoFli Balls—Innovative Training Tools for Youth Athletes – Lofli*
  9. `lolawilde-com` — *LOLA WILDE — Learning Me*
  10. `loopsii-com` — *Loopsii: the all-in-one app for freelancers*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `layrmedia-com` | `tier1_fast` | `1440×2400px` (725,915 B) | `390×2400px` (73,963 B) | 37 | 16 | 290 | 110 | `0.09` / `0.50` | **25.0 / 25.0** |
| `lcg-media` | `tier1_fast` | `1440×900px` (217,353 B) | `390×844px` (90,691 B) | 36 | 16 | 282 | 106 | `0.08` / `0.49` | **25.0 / 25.0** |
| `legacybridge-software` | `tier1_fast` | `1440×2400px` (324,292 B) | `390×2400px` (158,573 B) | 46 | 16 | 284 | 107 | `0.09` / `0.49` | **25.0 / 25.0** |
| `lenvalproperties-com` | `tier1_fast` | `1440×2400px` (1,312,851 B) | `390×2400px` (549,581 B) | 178 | 16 | 282 | 106 | `0.10` / `0.50` | **25.0 / 25.0** |
| `lfs-org-uk` | `tier1_fast` | `1440×2400px` (2,017,792 B) | `390×2400px` (764,191 B) | 100 | 16 | 288 | 109 | `0.10` / `0.48` | **25.0 / 25.0** |
| `lifetimepastapass-com` | `tier1_fast` | `1440×2400px` (232,879 B) | `390×2400px` (171,426 B) | 14 | 16 | 298 | 114 | `0.09` / `0.48` | **25.0 / 25.0** |
| `lofliballs-com` | `tier1_fast` | `1440×2400px` (1,332,243 B) | `390×2400px` (389,105 B) | 196 | 16 | 312 | 121 | `0.09` / `0.49` | **25.0 / 25.0** |
| `lolawilde-com` | `tier1_fast` | `1440×2400px` (1,402,004 B) | `390×2400px` (568,696 B) | 183 | 16 | 288 | 109 | `0.09` / `0.47` | **25.0 / 25.0** |
| `loopsii-com` | `tier2_webgl` | `1440×900px` (9,055 B) | `390×2400px` (210,224 B) | 158 | 16 | 282 | 106 | `0.08` / `0.50` | **25.0 / 25.0** |
| `levigav-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
