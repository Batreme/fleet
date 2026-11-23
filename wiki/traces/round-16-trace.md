# Round 16 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-16`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 16 Target Scope
  1. `giordanobetti-com` — *Giordano Betti - Independent Cinematographer*
  2. `glinto-co-kr` — *Glinto — Creative studio*
  3. `gmxdigital-com_en` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  4. `gpg-dops-agency` — *Garvinpromo*
  5. `gracefashion-ai` — *KI-Fotostudio für Mode: Bilder ohne Shooting · grace ai*
  6. `grail-app-com` — *Grail: Real-world quests, every day*
  7. `grids03-obys-agency` — *Grids — DES Season 03*
  8. `grubogrubo-com` — *GruboGrubo — Creative Ideas & Visual Production Studio · Warsaw*
  9. `guillaumecolombel-fr` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  10. `halloween-ferayna-com` — *Blocked (`Browser/WebGPU Hardware Gate (Every brief has a face | Ferayna)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `giordanobetti-com` | `tier1_fast` | `1440×900px` (31,094 B) | `390×844px` (20,148 B) | 20 | 16 | 280 | 105 | `0.10` / `0.53` | **25.0 / 25.0** |
| `glinto-co-kr` | `tier1_fast` | `1440×2400px` (673,506 B) | `390×2400px` (113,599 B) | 292 | 16 | 312 | 121 | `0.09` / `0.51` | **25.0 / 25.0** |
| `gpg-dops-agency` | `tier1_fast` | `1440×900px` (177,749 B) | `390×2400px` (187,629 B) | 43 | 16 | 286 | 108 | `0.09` / `0.56` | **25.0 / 25.0** |
| `gracefashion-ai` | `tier1_fast` | `1440×2400px` (359,912 B) | `390×2400px` (255,588 B) | 11 | 16 | 288 | 109 | `0.09` / `0.50` | **25.0 / 25.0** |
| `grail-app-com` | `tier1_fast` | `1440×2400px` (291,157 B) | `390×2400px` (121,817 B) | 84 | 16 | 300 | 115 | `0.08` / `0.51` | **25.0 / 25.0** |
| `grids03-obys-agency` | `tier1_fast` | `1440×2400px` (137,140 B) | `390×844px` (7,658 B) | 20 | 16 | 284 | 107 | `0.09` / `0.56` | **25.0 / 25.0** |
| `grubogrubo-com` | `tier2_webgl` | `1440×900px` (84,860 B) | `390×844px` (30,168 B) | 10 | 16 | 288 | 109 | `0.10` / `0.51` | **25.0 / 25.0** |
| `gmxdigital-com_en` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `guillaumecolombel-fr` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `halloween-ferayna-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Browser/WebGPU Hardware Gate (Every brief has a face | Ferayna)`)** |
