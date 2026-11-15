# Round 03 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-03`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 03 Target Scope
  1. `ads-apple-com` — *Apple Ads* (`http://ads.apple.com`)
  2. `aestudio-studio_hozon` — *Hozon — Pickle & Fermented Food Recipe App* (`https://aestudio.studio/hozon`)
  3. `aikissfiy-com` — *Free AI Kissing Video Generator: Create AI Kiss Videos Online - AIKissfiy* (`https://aikissfiy.com`)
  4. `aizeitgeist-tv` — *AI Zeitgeist · What the world says about AI* (`https://aizeitgeist.tv`)
  5. `akaiito-ai` — *Akai Ito — Your twin dates millions. You go on one date.* (`https://akaiito.ai`)
  6. `alexandracapitanescu-com` — *Alexandra Căpitănescu - Official Website* (`https://alexandracapitanescu.com/`)
  7. `allsorts-andrew-rip` — *Allsorts · Andrew Robinson* (`https://allsorts.andrew.rip`)
  8. `almadalabel-com` — *ALMADA LABEL - A modern take on a seasonless wardrobe* (`https://almadalabel.com/`)
  9. `almirakho-com` — *Almira Kho - Photographer and Director* (`https://almirakho.com/`)
  10. `altamedfoundation-org` — *AltaMed Foundation · AltaMed Foundation* (`https://altamedfoundation.org/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ads-apple-com` | `1440×7027px` (2,345,481 B) | `390×2400px` (100,394 B) | 540 | 16 | 260 | 108 | `0.09` / `0.47` | **25.0 / 25.0** |
| `aestudio-studio_hozon` | `1440×3448px` (1,482,655 B) | `390×2400px` (115,859 B) | 10 | 16 | 256 | 106 | `0.11` / `0.50` | **25.0 / 25.0** |
| `aikissfiy-com` | `1440×2400px` (685,335 B) | `390×2400px` (315,921 B) | 441 | 16 | 262 | 109 | `0.09` / `0.49` | **25.0 / 25.0** |
| `aizeitgeist-tv` | `1440×13433px` (245,123 B) | `390×2400px` (121,841 B) | 71 | 16 | 256 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
| `akaiito-ai` | `1440×2400px` (741,464 B) | `390×2400px` (366,627 B) | 28 | 16 | 256 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
| `alexandracapitanescu-com` | `1440×11875px` (626,205 B) | `390×2400px` (145,125 B) | 33 | 16 | 256 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
| `allsorts-andrew-rip` | `1440×2400px` (51,930 B) | `390×2400px` (41,889 B) | 1 | 13 | 249 | 102 | `0.11` / `0.51` | **25.0 / 25.0** |
| `almadalabel-com` | `1440×2400px` (1,129,735 B) | `390×2400px` (82,707 B) | 101 | 16 | 256 | 106 | `0.10` / `0.48` | **25.0 / 25.0** |
| `almirakho-com` | `1440×2400px` (67,986 B) | `390×2400px` (36,182 B) | 91 | 16 | 257 | 105 | `0.10` / `0.51` | **25.0 / 25.0** |
| `altamedfoundation-org` | `1440×4182px` (1,715,197 B) | `390×2400px` (79,422 B) | 175 | 16 | 276 | 116 | `0.08` / `0.50` | **25.0 / 25.0** |
