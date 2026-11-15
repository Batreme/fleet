# Round 22 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-22`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 22 Target Scope
  1. `layrmedia-com` — *LAYR Media · Creative Photography & Videography Studio* (`https://layrmedia.com/`)
  2. `lcg-media` — *LCG · The Agency That Fights for American Families* (`https://lcg.media`)
  3. `legacybridge-software` — *AI Document Entry for AS/400 & Legacy Systems · LegacyBridge* (`https://legacybridge.software/`)
  4. `lenvalproperties-com` — *Lenval Properties — Creators of Refined Living & Iconic Spaces* (`https://lenvalproperties.com`)
  5. `levigav-com` — *Levi Gavrilut · I build what I want to exist* (`https://levigav.com`)
  6. `lfs-org-uk` — *London Film School* (`https://lfs.org.uk/`)
  7. `lifetimepastapass-com` — *LIFETIME PASTA PASS · BRADEN'S INFINITE TOUR OF ITALY* (`https://lifetimepastapass.com`)
  8. `lofliballs-com` — *LoFli Balls—Innovative Training Tools for Youth Athletes – Lofli* (`http://lofliballs.com`)
  9. `lolawilde-com` — *LOLA WILDE — Learning Me* (`https://lolawilde.com/`)
  10. `loopsii-com` — *Loopsii: the all-in-one app for freelancers* (`https://loopsii.com/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `layrmedia-com` | `1440×2400px` (94,156 B) | `390×2400px` (331,024 B) | 37 | 16 | 256 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
| `lcg-media` | `1440×2400px` (49,427 B) | `390×2400px` (37,609 B) | 36 | 16 | 256 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
| `legacybridge-software` | `1440×19851px` (697,912 B) | `390×2400px` (423,538 B) | 46 | 16 | 256 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `lenvalproperties-com` | `1440×2400px` (907,310 B) | `390×2400px` (389,037 B) | 178 | 16 | 256 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `levigav-com` | `1440×2400px` (4,669,804 B) | `390×2400px` (800,891 B) | 153 | 16 | 260 | 108 | `0.09` / `0.50` | **25.0 / 25.0** |
| `lfs-org-uk` | `1440×6928px` (2,049,794 B) | `390×2400px` (47,916 B) | 100 | 16 | 256 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `lifetimepastapass-com` | `1440×5316px` (549,321 B) | `390×2400px` (200,482 B) | 14 | 16 | 268 | 112 | `0.09` / `0.49` | **25.0 / 25.0** |
| `lofliballs-com` | `1440×7969px` (1,469,775 B) | `390×2400px` (43,994 B) | 195 | 16 | 276 | 116 | `0.08` / `0.49` | **25.0 / 25.0** |
| `lolawilde-com` | `1440×5252px` (3,131,170 B) | `390×2400px` (194,758 B) | 176 | 16 | 258 | 107 | `0.08` / `0.48` | **25.0 / 25.0** |
| `loopsii-com` | `1440×2400px` (403,545 B) | `390×2400px` (232,618 B) | 158 | 16 | 256 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
