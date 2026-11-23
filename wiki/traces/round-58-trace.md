# Round 58 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-58`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `4` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 58 Target Scope
  1. `zarcerog-com` — *Nicolás Zarcero — Box Office*
  2. `zenobasi-com` — *Zen Obasi — Art Director*
  3. `zeropact-co` — *ZeroPact · LCA, Product Carbon Footprint, DPP, GLEC & EmpCo*
  4. `zeyraglow-com` — *Zeyra Glow · Natural Body Care Products in the UAE*
  5. `zujistudio-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `zarcerog-com` | `tier1_fast` | `1440×900px` (875,963 B) | `390×844px` (298,878 B) | 32 | 16 | 282 | 106 | `0.10` / `0.52` | **25.0 / 25.0** |
| `zenobasi-com` | `tier1_fast` | `1440×900px` (992,381 B) | `390×844px` (260,286 B) | 13 | 16 | 278 | 104 | `0.10` / `0.52` | **25.0 / 25.0** |
| `zeropact-co` | `tier1_fast` | `1440×2400px` (1,730,432 B) | `390×2400px` (383,631 B) | 148 | 16 | 282 | 106 | `0.08` / `0.47` | **25.0 / 25.0** |
| `zeyraglow-com` | `tier1_fast` | `1440×2400px` (1,872,721 B) | `390×2400px` (641,133 B) | 148 | 16 | 302 | 116 | `0.08` / `0.47` | **25.0 / 25.0** |
| `zujistudio-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
