# Round 21 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-21`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 21 Target Scope
  1. `konkelectrical-com` — *Konk Electrical · Eastern Suburbs Electricians, Sydney*
  2. `ksenpanchenko-com` — *Ksen Panchenko — UX/UI & Product Designer in Dublin · FinTech & SaaS*
  3. `labellavista-es` — *LABELLAVISTA — Creative production co.*
  4. `labs-griflan-com` — *Blocked (`Browser/WebGPU Hardware Gate (Griflan Labs)`)*
  5. `ladolfinajumping-com` — *La Dolfina Jumping. World class genetics, breed in Argentina*
  6. `lajoya-foods-com_en` — *LAJOYA GOURMET*
  7. `later-com_made-you-look` — *Made You Look: Campaigns so good you break the algorithm.*
  8. `launch-joinautopilot-com` — *Home*
  9. `layernative-com_tinkeroll` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 35000ms exceeded. Call log: - navigating to 'https://layernative.com/tinkeroll/', waiting until 'domcontentloaded' )`)*
  10. `layersoftime-studio` — *LAYERS OF TIME — The show runs on our clock.*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `konkelectrical-com` | `tier1_fast` | `1440×2400px` (633,878 B) | `390×2400px` (142,472 B) | 41 | 16 | 296 | 113 | `0.10` / `0.52` | **25.0 / 25.0** |
| `ksenpanchenko-com` | `tier1_fast` | `1440×2400px` (394,934 B) | `390×2400px` (198,743 B) | 240 | 16 | 296 | 113 | `0.08` / `0.51` | **25.0 / 25.0** |
| `labellavista-es` | `tier1_fast` | `1440×2400px` (1,624,216 B) | `390×2400px` (949,180 B) | 36 | 16 | 290 | 110 | `0.10` / `0.52` | **25.0 / 25.0** |
| `ladolfinajumping-com` | `tier1_fast` | `1440×900px` (662,483 B) | `390×844px` (484,509 B) | 12 | 16 | 294 | 112 | `0.10` / `0.54` | **25.0 / 25.0** |
| `lajoya-foods-com_en` | `tier1_fast` | `1440×900px` (194,238 B) | `390×844px` (16,316 B) | 13 | 16 | 286 | 108 | `0.10` / `0.54` | **25.0 / 25.0** |
| `later-com_made-you-look` | `tier2_webgl` | `1440×900px` (1,882,173 B) | `390×844px` (535,722 B) | 823 | 16 | 282 | 106 | `0.10` / `0.48` | **25.0 / 25.0** |
| `launch-joinautopilot-com` | `tier2_webgl` | `1440×900px` (45,988 B) | `390×844px` (20,510 B) | 465 | 16 | 282 | 106 | `0.10` / `0.49` | **25.0 / 25.0** |
| `layersoftime-studio` | `tier1_fast` | `1440×2400px` (603,500 B) | `390×2400px` (515,284 B) | 35 | 16 | 296 | 113 | `0.09` / `0.50` | **25.0 / 25.0** |
| `labs-griflan-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Browser/WebGPU Hardware Gate (Griflan Labs)`)** |
| `layernative-com_tinkeroll` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 35000ms exceeded. Call `)** |
