# Round 27 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-27`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 27 Target Scope
  1. `noho-ink` — *Noho*
  2. `noravale-framer-website` — *Blankit – Ultimate Portfolio System for Framer*
  3. `north-cloud` — *North.cloud · Take control of your cloud costs with AI-powered FinOps.*
  4. `oblikworks-com` — *oblikworks · Architectural Visualization & 3D Rendering Studio*
  5. `offform-net` — *Blocked (`Upstream HTTP 502 (502 Bad Gateway)`)*
  6. `offpossible-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  7. `ofrenda-davidlangarica-dev` — *OFRENDA — Create a personal Día de Muertos altar*
  8. `oliviaarents-com` — *OliviaOS 96 — Personal Edition*
  9. `ondocollective-jp` — *Ondo Collective*
  10. `onecoldnight-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `noho-ink` | `tier1_fast` | `1440×2400px` (370,718 B) | `390×2400px` (189,569 B) | 41 | 16 | 286 | 108 | `0.09` / `0.59` | **25.0 / 25.0** |
| `noravale-framer-website` | `tier1_fast` | `1440×900px` (1,116,894 B) | `390×1510px` (246,774 B) | 151 | 16 | 294 | 112 | `0.10` / `0.54` | **25.0 / 25.0** |
| `north-cloud` | `tier1_fast` | `1440×2400px` (970,163 B) | `390×2400px` (182,225 B) | 183 | 16 | 290 | 110 | `0.08` / `0.51` | **25.0 / 25.0** |
| `oblikworks-com` | `tier1_fast` | `1440×2400px` (48,580 B) | `390×1331px` (211,191 B) | 5 | 16 | 284 | 107 | `0.09` / `0.59` | **25.0 / 25.0** |
| `ofrenda-davidlangarica-dev` | `tier2_webgl` | `1440×900px` (12,055 B) | `390×844px` (4,986 B) | 37 | 16 | 290 | 110 | `0.10` / `0.51` | **25.0 / 25.0** |
| `oliviaarents-com` | `tier1_fast` | `1440×900px` (12,105 B) | `390×844px` (10,002 B) | 7 | 16 | 280 | 104 | `0.10` / `0.54` | **25.0 / 25.0** |
| `ondocollective-jp` | `tier1_fast` | `1440×900px` (1,158,533 B) | `390×2400px` (26,296 B) | 56 | 16 | 288 | 109 | `0.09` / `0.52` | **25.0 / 25.0** |
| `offform-net` | `blocked` (`502`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 502 (502 Bad Gateway)`)** |
| `offpossible-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `onecoldnight-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
