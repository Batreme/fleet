# Round 29 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-29`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `10` live (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 29 Target Scope
  1. `performeurope-eu` — *Perform Europe - Reimagine International Touring*
  2. `phin-helenadang-work` — *PHIN PHIN · Saigon coffee, stirred by you*
  3. `pinreply-com` — *Website Feedback Tool for Chrome · PinReply*
  4. `pixlpin-com_designs` — *Pixlpin: 64K+ Free UI Designs, App Screens, Motion & Graphics*
  5. `pixvibe-ai` — *PixVibe — Free Background Remover, Converter & Upscaler*
  6. `plastic-audio_dot` — *Record internal audio on Mac, with key and BPM · DOT*
  7. `plastic-ocean-com` — *Plastic Ocean*
  8. `powa-snp-agency` — *Donate to POWA & Stand for Women's Equality · Help End Gender-Based Viol...*
  9. `premotio-com` — *premotio — finished design into polished motion*
  10. `preymaker-com` — *Preymaker*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `performeurope-eu` | `tier1_fast` | `1440×2400px` (508,940 B) | `390×2400px` (177,438 B) | 228 | 16 | 292 | 111 | `0.10` / `0.48` | **25.0 / 25.0** |
| `phin-helenadang-work` | `tier1_fast` | `1440×2400px` (1,332,743 B) | `390×2400px` (428,975 B) | 64 | 16 | 306 | 118 | `0.10` / `0.50` | **25.0 / 25.0** |
| `pinreply-com` | `tier1_fast` | `1440×2400px` (305,821 B) | `390×2400px` (164,315 B) | 11 | 16 | 290 | 110 | `0.10` / `0.51` | **25.0 / 25.0** |
| `pixlpin-com_designs` | `tier1_fast` | `1440×2400px` (2,012,528 B) | `390×2400px` (791,547 B) | 406 | 16 | 302 | 116 | `0.09` / `0.50` | **25.0 / 25.0** |
| `pixvibe-ai` | `tier2_webgl` | `1440×2400px` (738,989 B) | `390×844px` (90,618 B) | 565 | 16 | 296 | 113 | `0.08` / `0.46` | **25.0 / 25.0** |
| `plastic-audio_dot` | `tier1_fast` | `1440×2400px` (656,285 B) | `390×2400px` (243,227 B) | 33 | 16 | 290 | 110 | `0.09` / `0.51` | **25.0 / 25.0** |
| `plastic-ocean-com` | `tier1_fast` | `1440×2400px` (1,320,113 B) | `390×2400px` (348,239 B) | 14 | 16 | 284 | 107 | `0.10` / `0.51` | **25.0 / 25.0** |
| `powa-snp-agency` | `tier1_fast` | `1440×2400px` (1,364,577 B) | `390×2400px` (586,357 B) | 92 | 16 | 280 | 104 | `0.10` / `0.51` | **25.0 / 25.0** |
| `premotio-com` | `tier2_webgl` | `1440×900px` (8,672 B) | `390×2400px` (21,103 B) | 445 | 16 | 286 | 108 | `0.09` / `0.50` | **25.0 / 25.0** |
| `preymaker-com` | `tier1_fast` | `1440×900px` (927,307 B) | `390×844px` (236,405 B) | 34 | 16 | 282 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
