# Round 26 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-26`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `10` live (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 26 Target Scope
  1. `mychess-events` — *Find Chess Tournaments Worldwide · MyChess.Events*
  2. `myfrida-com` — *My Frida · Chocolate-Covered Fruit, Smoothies & Cake Bars*
  3. `nader-io` — *Nader Cserny*
  4. `nakagawa-corp-com` — *久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホーム）*
  5. `namaha-healthcare` — *Namaha Healthcare*
  6. `navtec-com` — *Moab Adventure Tours · Navtec Expeditions Since 1896*
  7. `newminds-studio_concept-elune` — *ELUNE — A Private Symptom Diary · New Minds Product Case*
  8. `nickho-motorsports-nl` — *Nick Ho - Dutch Racing Driver · Porsche Carrera Cup*
  9. `no-merci-michel-com` — *No Mercy Michel*
  10. `nodenza-com` — *Home · Nodenza*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `mychess-events` | `tier1_fast` | `1440×2400px` (1,001,998 B) | `390×2400px` (325,127 B) | 263 | 16 | 286 | 108 | `0.10` / `0.51` | **25.0 / 25.0** |
| `myfrida-com` | `tier1_fast` | `1440×2400px` (541,771 B) | `390×2400px` (287,988 B) | 497 | 16 | 306 | 118 | `0.09` / `0.49` | **25.0 / 25.0** |
| `nader-io` | `tier1_fast` | `1440×2400px` (747,563 B) | `390×2400px` (137,663 B) | 75 | 16 | 282 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `nakagawa-corp-com` | `tier1_fast` | `1440×2400px` (757,212 B) | `390×2400px` (397,821 B) | 131 | 16 | 290 | 110 | `0.10` / `0.52` | **25.0 / 25.0** |
| `namaha-healthcare` | `tier1_fast` | `1440×2400px` (1,093,098 B) | `390×2400px` (339,762 B) | 0 | 12 | 275 | 102 | `0.16` / `0.61` | **25.0 / 25.0** |
| `navtec-com` | `tier1_fast` | `1440×2400px` (2,241,984 B) | `390×2400px` (700,063 B) | 95 | 16 | 282 | 106 | `0.12` / `0.59` | **25.0 / 25.0** |
| `newminds-studio_concept-elune` | `tier1_fast` | `1440×2400px` (479,843 B) | `390×2400px` (217,241 B) | 5 | 16 | 280 | 105 | `0.10` / `0.49` | **25.0 / 25.0** |
| `nickho-motorsports-nl` | `tier1_fast` | `1440×2400px` (170,841 B) | `390×2400px` (309,132 B) | 94 | 16 | 282 | 106 | `0.16` / `0.61` | **25.0 / 25.0** |
| `no-merci-michel-com` | `tier2_webgl` | `1440×900px` (237,467 B) | `390×844px` (99,561 B) | 49 | 16 | 280 | 104 | `0.09` / `0.50` | **25.0 / 25.0** |
| `nodenza-com` | `tier1_fast` | `1440×2400px` (923,770 B) | `390×2400px` (230,336 B) | 30 | 16 | 288 | 109 | `0.10` / `0.52` | **25.0 / 25.0** |
