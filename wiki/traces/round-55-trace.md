# Round 55 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-55`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `10` live (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 55 Target Scope
  1. `www-thecandyvault-com-au` — *The Candy Vault · Buy Sweets Online · Australia*
  2. `www-thedesignsociety-fr` — *The Design Society Lyon — la communauté des designers*
  3. `www-thefriedegg-com` — *Fried Egg Golf*
  4. `www-thelasttango-com` — *The Last Tango / For the one who made us happy.*
  5. `www-tokonoma-xyz` — *Tokonoma Studio — Image Making, Art, AI & Creative Direction*
  6. `www-tomdekoning-work` — *tomdekoning.work — Building brands that turn heads*
  7. `www-unbelievablycrap-com` — *Liubomyr Ulytskyi - Digital Designer*
  8. `www-undplus-com` — *UNDPLUS — Brand Architecture & Spatial Design Studio*
  9. `www-upscayl-app` — *Upscale Image Online Free – Upscale to 8K with AI · Upscayl*
  10. `www-urbik-eu` — *Jakub 'Urbik' Urbanec · Web Developer · DJ · AV artist*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-thecandyvault-com-au` | `tier1_fast` | `1440×2400px` (810,999 B) | `390×2400px` (258,263 B) | 2100 | 16 | 282 | 106 | `0.09` / `0.47` | **25.0 / 25.0** |
| `www-thedesignsociety-fr` | `tier1_fast` | `1440×2400px` (771,140 B) | `390×2400px` (78,381 B) | 60 | 16 | 290 | 110 | `0.15` / `0.59` | **25.0 / 25.0** |
| `www-thefriedegg-com` | `tier1_fast` | `1440×2400px` (2,658,874 B) | `390×2400px` (811,107 B) | 236 | 16 | 282 | 106 | `0.11` / `0.54` | **25.0 / 25.0** |
| `www-thelasttango-com` | `tier1_fast` | `1440×900px` (706,442 B) | `390×844px` (386,380 B) | 119 | 16 | 294 | 112 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-tokonoma-xyz` | `tier1_fast` | `1440×900px` (1,103,699 B) | `390×844px` (352,929 B) | 3 | 15 | 277 | 102 | `0.10` / `0.53` | **25.0 / 25.0** |
| `www-tomdekoning-work` | `tier1_fast` | `1440×2400px` (229,198 B) | `390×2400px` (101,575 B) | 19 | 16 | 288 | 109 | `0.15` / `0.59` | **25.0 / 25.0** |
| `www-unbelievablycrap-com` | `tier2_webgl` | `1440×900px` (369,385 B) | `390×844px` (37,725 B) | 86 | 16 | 292 | 111 | `0.10` / `0.53` | **25.0 / 25.0** |
| `www-undplus-com` | `tier1_fast` | `1440×2400px` (94,796 B) | `390×2400px` (164,863 B) | 29 | 16 | 290 | 110 | `0.10` / `0.52` | **25.0 / 25.0** |
| `www-upscayl-app` | `tier1_fast` | `1440×2400px` (1,230,939 B) | `390×2400px` (502,995 B) | 77 | 16 | 282 | 106 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-urbik-eu` | `tier2_webgl` | `1440×900px` (997,300 B) | `390×844px` (334,432 B) | 127 | 16 | 292 | 111 | `0.09` / `0.50` | **25.0 / 25.0** |
