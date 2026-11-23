# Round 03 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-03`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `10` live (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 03 Target Scope
  1. `ads-apple-com` — *Apple Ads*
  2. `aestudio-studio_hozon` — *Hozon — Pickle & Fermented Food Recipe App*
  3. `aikissfiy-com` — *Free AI Kissing Video Generator: Create AI Kiss Videos Online - AIKissfiy*
  4. `aizeitgeist-tv` — *AI Zeitgeist: AI quotes from the people shaping it*
  5. `akaiito-ai` — *Akai Ito — Your twin dates millions. You go on one date.*
  6. `alexandracapitanescu-com` — *Alexandra Căpitănescu - Official Website*
  7. `allsorts-andrew-rip` — *Allsorts · Andrew Robinson*
  8. `almadalabel-com` — *ALMADA LABEL - A modern take on a seasonless wardrobe*
  9. `almirakho-com` — *Almira Kho - Photographer and Director*
  10. `altamedfoundation-org` — *AltaMed Foundation · AltaMed Foundation*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ads-apple-com` | `tier1_fast` | `1440×2400px` (2,153,960 B) | `390×2400px` (621,615 B) | 253 | 16 | 282 | 106 | `0.10` / `0.48` | **25.0 / 25.0** |
| `aestudio-studio_hozon` | `tier1_fast` | `1440×2400px` (1,005,725 B) | `390×2400px` (346,544 B) | 10 | 16 | 284 | 107 | `0.10` / `0.50` | **25.0 / 25.0** |
| `aikissfiy-com` | `tier1_fast` | `1440×2400px` (1,732,669 B) | `390×2400px` (786,605 B) | 251 | 16 | 290 | 111 | `0.09` / `0.46` | **25.0 / 25.0** |
| `aizeitgeist-tv` | `tier2_webgl` | `1440×2400px` (236,987 B) | `390×844px` (22,197 B) | 75 | 16 | 282 | 106 | `0.10` / `0.52` | **25.0 / 25.0** |
| `akaiito-ai` | `tier1_fast` | `1440×900px` (25,515 B) | `390×844px` (20,261 B) | 28 | 16 | 288 | 109 | `0.09` / `0.51` | **25.0 / 25.0** |
| `alexandracapitanescu-com` | `tier1_fast` | `1440×2400px` (1,603,732 B) | `390×2400px` (528,461 B) | 33 | 16 | 284 | 107 | `0.09` / `0.50` | **25.0 / 25.0** |
| `allsorts-andrew-rip` | `tier1_fast` | `1440×900px` (519,663 B) | `390×844px` (280,715 B) | 1 | 13 | 275 | 102 | `0.10` / `0.52` | **25.0 / 25.0** |
| `almadalabel-com` | `tier1_fast` | `1440×2400px` (2,002,937 B) | `390×2400px` (278,303 B) | 108 | 16 | 290 | 110 | `0.10` / `0.51` | **25.0 / 25.0** |
| `almirakho-com` | `tier1_fast` | `1440×900px` (777,686 B) | `390×2400px` (696,014 B) | 91 | 16 | 281 | 104 | `0.09` / `0.52` | **25.0 / 25.0** |
| `altamedfoundation-org` | `tier1_fast` | `1440×2400px` (1,318,794 B) | `390×2400px` (397,182 B) | 175 | 16 | 290 | 110 | `0.10` / `0.50` | **25.0 / 25.0** |
