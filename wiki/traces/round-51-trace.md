# Round 51 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-51`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 51 Target Scope
  1. `www-ouiwill-com` — *Oui Will · Brand Transformation & Digital Experiences*
  2. `www-paaspop-nl` — *Paaspop 2027 · 26, 27 & 28 maart*
  3. `www-palaraiffeisen-ch` — *Il palazzetto dello sport di Lugano — Palaraiffeisen*
  4. `www-paragonproductions-co` — *PARAGON · Creative Production Studio*
  5. `www-peryton-film-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  6. `www-photiu-ai` — *Remove Background, Upscale & Erase Objects – Photiu.ai*
  7. `www-pistacchioecaffe-it` — *Pistacchio & Caffè*
  8. `www-plugandplaydesign-co-uk` — *Web Design Agency London & Guildford · Plug & Play*
  9. `www-politico-eu_sponsored-content-saving-costs-and-improving-lives` — *Saving costs and improving lives – POLITICO*
  10. `www-polpharmabiologics-com` — *Polpharma Biologics · Global Biosimilar Developer & Manufacturer*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-ouiwill-com` | `tier2_webgl` | `1440×900px` (126,943 B) | `390×844px` (32,951 B) | 106 | 16 | 282 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-paaspop-nl` | `tier1_fast` | `1440×2400px` (2,183,672 B) | `390×2400px` (650,860 B) | 298 | 16 | 282 | 106 | `0.15` / `0.56` | **25.0 / 25.0** |
| `www-palaraiffeisen-ch` | `tier2_webgl` | `1440×900px` (10,970 B) | `390×844px` (4,268 B) | 323 | 16 | 283 | 106 | `0.10` / `0.50` | **25.0 / 25.0** |
| `www-paragonproductions-co` | `tier1_fast` | `1440×2400px` (618,651 B) | `390×2400px` (345,337 B) | 118 | 16 | 284 | 107 | `0.15` / `0.56` | **25.0 / 25.0** |
| `www-photiu-ai` | `tier1_fast` | `1440×2400px` (869,228 B) | `390×2400px` (182,694 B) | 14 | 16 | 286 | 108 | `0.10` / `0.51` | **25.0 / 25.0** |
| `www-pistacchioecaffe-it` | `tier1_fast` | `1440×2400px` (1,351,966 B) | `390×2400px` (629,162 B) | 45 | 16 | 297 | 113 | `0.12` / `0.51` | **25.0 / 25.0** |
| `www-plugandplaydesign-co-uk` | `tier1_fast` | `1440×2400px` (278,645 B) | `390×2400px` (271,810 B) | 380 | 16 | 282 | 106 | `0.10` / `0.51` | **25.0 / 25.0** |
| `www-politico-eu_sponsored-content-saving-costs-and-improving-lives` | `tier1_fast` | `1440×2400px` (937,836 B) | `390×2400px` (327,320 B) | 324 | 16 | 296 | 114 | `0.12` / `0.51` | **25.0 / 25.0** |
| `www-polpharmabiologics-com` | `tier2_webgl` | `1440×900px` (62,092 B) | `390×844px` (30,480 B) | 45 | 16 | 284 | 107 | `0.13` / `0.55` | **25.0 / 25.0** |
| `www-peryton-film-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
