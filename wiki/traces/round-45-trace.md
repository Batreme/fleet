# Round 45 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-45`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `10` live (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 45 Target Scope
  1. `www-dontlookup-app` — *Don't Look Up — a game about keeping everyone looking down*
  2. `www-east64films-com` — *EAST 64 Films · Tokyo-Based International Production Company*
  3. `www-easyseller-it` — *EASYSELLER · Sales Digital Agency*
  4. `www-emblematica-agency` — *emblematica — concept-led brand & web design agency in barcelona*
  5. `www-enigmascult-com` — *Enigma – Sneaker Auctions, Mystery Boxes & Reborn Customs*
  6. `www-era-residence-com` — *ERA Residence — Contemporary Mediterranean Residences in Estepona*
  7. `www-esrbespoke-au` — *ESR*
  8. `www-extrafazant-nl` — *Extrafazant · Social Content, Video's & Animatie*
  9. `www-feelreformed-com` — *Reformed: The biggest thing to happen to Coffee since Coffee.*
  10. `www-fiabamia-com` — *FiabaMia — Personalized bedtime stories for children*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-dontlookup-app` | `tier1_fast` | `1440×900px` (762,884 B) | `390×844px` (240,902 B) | 24 | 16 | 294 | 112 | `0.09` / `0.51` | **25.0 / 25.0** |
| `www-east64films-com` | `tier1_fast` | `1440×900px` (341,874 B) | `390×844px` (185,927 B) | 111 | 16 | 302 | 116 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-easyseller-it` | `tier1_fast` | `1440×900px` (485,719 B) | `390×844px` (132,704 B) | 451 | 16 | 298 | 114 | `0.10` / `0.52` | **25.0 / 25.0** |
| `www-emblematica-agency` | `tier1_fast` | `1440×2400px` (989,372 B) | `390×2400px` (424,571 B) | 61 | 16 | 289 | 109 | `0.10` / `0.52` | **25.0 / 25.0** |
| `www-enigmascult-com` | `tier1_fast` | `1440×2400px` (1,082,670 B) | `390×2400px` (316,113 B) | 102 | 16 | 300 | 115 | `0.10` / `0.52` | **25.0 / 25.0** |
| `www-era-residence-com` | `tier1_fast` | `1440×2400px` (2,340,570 B) | `390×2400px` (275,410 B) | 201 | 16 | 282 | 106 | `0.13` / `0.60` | **25.0 / 25.0** |
| `www-esrbespoke-au` | `tier1_fast` | `1440×2400px` (822,257 B) | `390×2400px` (269,824 B) | 8 | 16 | 282 | 106 | `0.09` / `0.52` | **25.0 / 25.0** |
| `www-extrafazant-nl` | `tier1_fast` | `1440×2400px` (860,248 B) | `390×2400px` (510,822 B) | 166 | 16 | 282 | 106 | `0.13` / `0.60` | **25.0 / 25.0** |
| `www-feelreformed-com` | `tier1_fast` | `1440×2400px` (1,209,458 B) | `390×2400px` (454,467 B) | 779 | 16 | 282 | 106 | `0.10` / `0.49` | **25.0 / 25.0** |
| `www-fiabamia-com` | `tier2_webgl` | `1440×900px` (327,459 B) | `390×844px` (97,218 B) | 186 | 16 | 302 | 116 | `0.09` / `0.48` | **25.0 / 25.0** |
