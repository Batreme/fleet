# Round 32 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-32`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 32 Target Scope
  1. `santalarch-com` — *Santalarch*
  2. `santionispirits-com` — *Blocked (`Browser Compatibility Gate (Not Supported)`)*
  3. `sc-aesthetic-labs-com` — *Digital Systems for Visible Trust – S/C Lab*
  4. `secure-the-unknown-cyera-com` — *Blocked (`Browser Compatibility Gate (Not Supported)`)*
  5. `seedance3-si` — *Seedance 3.0 AI Video Generator: Make Videos from References*
  6. `seedrouter-ai` — *SeedRouter · One API for Image, Video, LLM and Audio Models*
  7. `seemecreative-com` — *SEE ME Creative*
  8. `senawastudio-com` — *Senawa · Architecture & Interior Design Studio in Jakarta*
  9. `serus-ai` — *Serus — Agentic Privacy & Intelligence*
  10. `shorodo-nagoya` — *松露堂 — 手の中の温度 · 明治十年創業・名古屋 円頓寺の和菓子処*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `santalarch-com` | `tier1_fast` | `1440×900px` (33,071 B) | `390×844px` (15,876 B) | 103 | 16 | 286 | 108 | `0.09` / `0.54` | **25.0 / 25.0** |
| `sc-aesthetic-labs-com` | `tier1_fast` | `1440×2400px` (486,083 B) | `390×2400px` (188,244 B) | 36 | 16 | 288 | 109 | `0.09` / `0.50` | **25.0 / 25.0** |
| `seedance3-si` | `tier1_fast` | `1440×2400px` (1,857,984 B) | `390×2400px` (478,824 B) | 431 | 16 | 292 | 111 | `0.09` / `0.55` | **25.0 / 25.0** |
| `seedrouter-ai` | `tier1_fast` | `1440×2400px` (1,554,765 B) | `390×2400px` (680,406 B) | 377 | 16 | 296 | 113 | `0.09` / `0.55` | **25.0 / 25.0** |
| `seemecreative-com` | `tier1_fast` | `1440×2400px` (1,723,310 B) | `390×2400px` (490,785 B) | 26 | 16 | 289 | 108 | `0.09` / `0.49` | **25.0 / 25.0** |
| `senawastudio-com` | `tier1_fast` | `1440×900px` (1,436,566 B) | `390×844px` (238,820 B) | 58 | 16 | 294 | 112 | `0.09` / `0.50` | **25.0 / 25.0** |
| `serus-ai` | `tier1_fast` | `1440×2400px` (543,120 B) | `390×2400px` (256,640 B) | 140 | 16 | 285 | 107 | `0.09` / `0.51` | **25.0 / 25.0** |
| `shorodo-nagoya` | `tier1_fast` | `1440×2230px` (1,665,114 B) | `390×2400px` (547,073 B) | 21 | 16 | 292 | 111 | `0.08` / `0.54` | **25.0 / 25.0** |
| `santionispirits-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Browser Compatibility Gate (Not Supported)`)** |
| `secure-the-unknown-cyera-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Browser Compatibility Gate (Not Supported)`)** |
