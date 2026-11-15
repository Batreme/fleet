# Round 32 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-32`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `8` (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 32 Target Scope
  1. `santalarch-com` — *Santalarch* (`https://santalarch.com`)
  2. `santionispirits-com` — *Blocked (`Browser Compatibility Gate (Your browser is not supported, 0 external stylesheets)`)*
  3. `sc-aesthetic-labs-com` — *Digital Systems for Visible Trust – S/C Lab* (`https://sc-aesthetic-labs.com/`)
  4. `secure-the-unknown-cyera-com` — *Blocked (`Browser Compatibility Gate (Not Supported, 335-byte DOM, 0 stylesheets)`)*
  5. `seedance3-si` — *Seedance 3.0 AI Video Generator: Make Videos from References* (`https://seedance3.si/`)
  6. `seedrouter-ai` — *SeedRouter · One API for Image, Video, LLM and Audio Models* (`https://seedrouter.ai`)
  7. `seemecreative-com` — *SEE ME Creative* (`https://seemecreative.com/`)
  8. `senawastudio-com` — *Senawa · Architecture & Interior Design Studio in Jakarta* (`https://senawastudio.com`)
  9. `serus-ai` — *Serus — Agentic Privacy & Intelligence* (`https://serus.ai/`)
  10. `shorodo-nagoya` — *松露堂 — 手の中の温度 · 明治十年創業・名古屋 円頓寺の和菓子処* (`https://shorodo.nagoya/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `santalarch-com` | `1440×2400px` (54,847 B) | `390×2400px` (188,841 B) | 103 | 16 | 262 | 109 | `0.09` / `0.56` | **25.0 / 25.0** |
| `santionispirits-com` | `status: blocked` | `status: blocked` | — | — | — | — | — | **Excluded (`Browser Compatibility Gate (Your browser is not supported, 0 external stylesheets)`)** |
| `sc-aesthetic-labs-com` | `1440×15601px` (974,420 B) | `390×2400px` (152,248 B) | 36 | 16 | 256 | 106 | `0.08` / `0.51` | **25.0 / 25.0** |
| `secure-the-unknown-cyera-com` | `status: blocked` | `status: blocked` | — | — | — | — | — | **Excluded (`Browser Compatibility Gate (Not Supported, 335-byte DOM, 0 stylesheets)`)** |
| `seedance3-si` | `1440×10319px` (2,402,740 B) | `390×2400px` (197,209 B) | 431 | 16 | 258 | 107 | `0.09` / `0.53` | **25.0 / 25.0** |
| `seedrouter-ai` | `1440×10504px` (2,376,152 B) | `390×2400px` (450,867 B) | 373 | 16 | 260 | 108 | `0.10` / `0.57` | **25.0 / 25.0** |
| `seemecreative-com` | `1440×2422px` (1,570,185 B) | `390×2400px` (49,810 B) | 26 | 16 | 258 | 107 | `0.08` / `0.50` | **25.0 / 25.0** |
| `senawastudio-com` | `1440×2400px` (63,159 B) | `390×2400px` (32,977 B) | 58 | 16 | 266 | 111 | `0.09` / `0.51` | **25.0 / 25.0** |
| `serus-ai` | `1440×4735px` (625,753 B) | `390×2400px` (49,105 B) | 140 | 16 | 268 | 112 | `0.10` / `0.57` | **25.0 / 25.0** |
| `shorodo-nagoya` | `1440×2400px` (54,868 B) | `390×2400px` (44,606 B) | 21 | 16 | 262 | 109 | `0.09` / `0.56` | **25.0 / 25.0** |
