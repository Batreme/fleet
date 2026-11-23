# Round 34 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-34`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 34 Target Scope
  1. `spykercars-com` — *Hand-Built Super Sports Cars Since 1880 · Spyker Cars*
  2. `stateofaidesign-com` — *AI in Design Report 2026*
  3. `statusisup-com` — *Status Is UP — Index für Service-Uptime, Performance & Zuverlässigkeit*
  4. `stillform-homes` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  5. `stillhere-hdfund-org` — *STILL HERE. · Three Years in Gaza · HDF*
  6. `straw-page` — *Straw.Page - Extremely simple website builder*
  7. `structureengineering-com-au` — *Structure Consulting Engineers · Structural Engineering Sydney*
  8. `studyhall-design` — *Home · Study Hall ✶ Built to move you.*
  9. `suho-studio` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  10. `superlogica-com` — *Blocked (`Upstream HTTP 403 — Cloudflare Origin/WAF Error`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `spykercars-com` | `tier1_fast` | `1440×2400px` (878,895 B) | `390×2400px` (577,524 B) | 169 | 16 | 282 | 106 | `0.10` / `0.51` | **25.0 / 25.0** |
| `stateofaidesign-com` | `tier1_fast` | `1440×2400px` (1,439,743 B) | `390×2400px` (193,243 B) | 42 | 16 | 292 | 111 | `0.10` / `0.50` | **25.0 / 25.0** |
| `statusisup-com` | `tier1_fast` | `1440×2400px` (780,730 B) | `390×2400px` (345,414 B) | 153 | 16 | 296 | 113 | `0.09` / `0.48` | **25.0 / 25.0** |
| `stillhere-hdfund-org` | `tier1_fast` | `1440×2400px` (1,072,791 B) | `390×2400px` (375,192 B) | 74 | 16 | 294 | 112 | `0.10` / `0.50` | **25.0 / 25.0** |
| `straw-page` | `tier1_fast` | `1440×2400px` (843,732 B) | `390×2400px` (269,692 B) | 4 | 16 | 282 | 106 | `0.10` / `0.51` | **25.0 / 25.0** |
| `structureengineering-com-au` | `tier1_fast` | `1440×2400px` (1,574,008 B) | `390×2400px` (318,090 B) | 5 | 16 | 288 | 109 | `0.09` / `0.51` | **25.0 / 25.0** |
| `studyhall-design` | `tier1_fast` | `1440×2400px` (844,257 B) | `390×2400px` (302,515 B) | 213 | 16 | 283 | 106 | `0.10` / `0.51` | **25.0 / 25.0** |
| `stillform-homes` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `suho-studio` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `superlogica-com` | `blocked` (`403`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 403 — Cloudflare Origin/WAF Error`)** |
