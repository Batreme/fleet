# Round 45 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-45`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
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
  10. `www-fiabamia-com` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-dontlookup-app` | `tier1_fast` | `1280×828px` (35,904 B) | `390×872px` (8,570 B) | 24 | 16 | 321 | 115 | `0.08` / `0.51` | **25.0 / 25.0** |
| `www-east64films-com` | `tier1_fast` | `1280×6624px` (314,130 B) | `390×872px` (13,582 B) | 111 | 16 | 357 | 120 | `0.10` / `0.49` | **25.0 / 25.0** |
| `www-easyseller-it` | `tier1_fast` | `1280×4140px` (192,692 B) | `390×872px` (23,140 B) | 451 | 16 | 348 | 118 | `0.10` / `0.53` | **25.0 / 25.0** |
| `www-emblematica-agency` | `tier1_fast` | `1280×6624px` (584,006 B) | `390×2616px` (83,986 B) | 60 | 16 | 353 | 114 | `0.09` / `0.54` | **25.0 / 25.0** |
| `www-enigmascult-com` | `tier1_fast` | `1280×6624px` (499,952 B) | `390×2616px` (89,576 B) | 102 | 16 | 355 | 119 | `0.10` / `0.53` | **25.0 / 25.0** |
| `www-era-residence-com` | `tier1_fast` | `1280×6624px` (627,360 B) | `390×872px` (8,972 B) | 201 | 16 | 336 | 110 | `0.11` / `0.58` | **25.0 / 25.0** |
| `www-esrbespoke-au` | `tier1_fast` | `1280×6624px` (376,478 B) | `390×2616px` (36,786 B) | 8 | 16 | 348 | 111 | `0.09` / `0.54` | **25.0 / 25.0** |
| `www-extrafazant-nl` | `tier1_fast` | `1280×6624px` (403,914 B) | `390×2616px` (82,062 B) | 166 | 16 | 341 | 110 | `0.11` / `0.58` | **25.0 / 25.0** |
| `www-feelreformed-com` | `tier1_fast` | `1280×4968px` (320,448 B) | `390×2616px` (75,814 B) | 1258 | 16 | 342 | 111 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-fiabamia-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
