# Round 12 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-12`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 12 Target Scope
  1. `dream-with-ai-com` — *Dream with AI*
  2. `dreams-paulvl-eu` — *Blocked (`Browser/WebGPU Hardware Gate (I'm having bad dreams)`)*
  3. `drshabri-com` — *Cosmetic Dentist & Facial Aesthetics, Marylebone*
  4. `dsquaredmedia-net` — *South Florida Marketing Agency · Branding, Web & AI · Dsquared Media*
  5. `duda-works` — *Duda Lima*
  6. `dwell-au` — *Dwell · A new way home*
  7. `earthwallet-com` — *Earth Wallet — Real assets for unreal markets*
  8. `edisonfangworkshop-com` — *Edison Fang Workshop*
  9. `effepinnastudio-com` — *Fabio Pinna — Art Director e Graphic Designer · Effepinna Studio*
  10. `ellioteriksson-com` — *Elliot Eriksson — UI/UX, web & brand design, Stockholm & Åland*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `dream-with-ai-com` | `tier1_fast` | `1440×900px` (584,809 B) | `390×844px` (198,734 B) | 16 | 16 | 286 | 108 | `0.09` / `0.52` | **25.0 / 25.0** |
| `drshabri-com` | `tier1_fast` | `1440×2400px` (923,391 B) | `390×2400px` (461,494 B) | 171 | 16 | 286 | 108 | `0.10` / `0.49` | **25.0 / 25.0** |
| `dsquaredmedia-net` | `tier1_fast` | `1440×2400px` (461,744 B) | `390×2400px` (336,803 B) | 78 | 16 | 302 | 116 | `0.09` / `0.50` | **25.0 / 25.0** |
| `duda-works` | `tier1_fast` | `1440×900px` (281,233 B) | `390×2121px` (125,231 B) | 5 | 16 | 280 | 103 | `0.09` / `0.52` | **25.0 / 25.0** |
| `dwell-au` | `tier1_fast` | `1440×900px` (1,408,529 B) | `390×844px` (274,143 B) | 201 | 16 | 282 | 106 | `0.09` / `0.52` | **25.0 / 25.0** |
| `earthwallet-com` | `tier1_fast` | `1440×2400px` (289,549 B) | `390×2400px` (111,172 B) | 26 | 16 | 310 | 120 | `0.09` / `0.50` | **25.0 / 25.0** |
| `edisonfangworkshop-com` | `tier1_fast` | `1440×2400px` (169,364 B) | `390×1795px` (76,000 B) | 125 | 16 | 290 | 110 | `0.09` / `0.49` | **25.0 / 25.0** |
| `effepinnastudio-com` | `tier1_fast` | `1440×2400px` (659,669 B) | `390×2400px` (342,440 B) | 94 | 16 | 286 | 108 | `0.10` / `0.50` | **25.0 / 25.0** |
| `ellioteriksson-com` | `tier1_fast` | `1440×2400px` (1,420,655 B) | `390×2400px` (304,792 B) | 45 | 16 | 286 | 108 | `0.10` / `0.52` | **25.0 / 25.0** |
| `dreams-paulvl-eu` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Browser/WebGPU Hardware Gate (I'm having bad dreams)`)** |
