# Round 19 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-19`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 19 Target Scope
  1. `janiswanger-ch` — *Janis Wanger — Creative Engineer in Bern*
  2. `jaspreetsingh-xyz` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  3. `jetalto-com` — *JetALto, Private Jet Charter · Fly Anywhere, On Your Schedule*
  4. `jimo-ai_product-ai` — *AI Agent for User Onboarding in SaaS · Jimo*
  5. `jjettas-com` — *Justin Jefferson*
  6. `jld2nd-dev` — *JLD'2nd – Designer & Developer*
  7. `jockey-stuudio-xyz` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  8. `johnhardy-com_collections-billie-eilish-and-finneas` — *Billie Eilish and FINNEAS – John Hardy*
  9. `jonmccormack-com` — *Patterns - Jon McCormack*
  10. `jozue-fr` — *Josué Pichot, freelance art director and photographer in Paris*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `janiswanger-ch` | `tier1_fast` | `1440×2400px` (1,560,576 B) | `390×2400px` (600,611 B) | 76 | 16 | 282 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `jetalto-com` | `tier1_fast` | `1440×2400px` (875,317 B) | `390×2400px` (303,927 B) | 47 | 16 | 300 | 115 | `0.09` / `0.46` | **25.0 / 25.0** |
| `jimo-ai_product-ai` | `tier2_webgl` | `1440×900px` (73,966 B) | `390×844px` (38,781 B) | 315 | 16 | 306 | 118 | `0.09` / `0.47` | **25.0 / 25.0** |
| `jjettas-com` | `tier2_webgl` | `1440×900px` (2,083,839 B) | `390×844px` (9,122 B) | 180 | 16 | 284 | 107 | `0.09` / `0.47` | **25.0 / 25.0** |
| `jld2nd-dev` | `tier1_fast` | `1440×2400px` (72,830 B) | `390×2400px` (50,464 B) | 53 | 16 | 284 | 107 | `0.09` / `0.51` | **25.0 / 25.0** |
| `johnhardy-com_collections-billie-eilish-and-finneas` | `tier1_fast` | `1440×2400px` (1,422,724 B) | `390×844px` (277,144 B) | 496 | 16 | 288 | 109 | `0.09` / `0.46` | **25.0 / 25.0** |
| `jonmccormack-com` | `tier1_fast` | `1440×900px` (1,735,671 B) | `390×2400px` (1,231,978 B) | 30 | 16 | 287 | 107 | `0.09` / `0.48` | **25.0 / 25.0** |
| `jozue-fr` | `tier1_fast` | `1440×2400px` (64,113 B) | `390×2400px` (70,553 B) | 103 | 16 | 282 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
| `jaspreetsingh-xyz` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `jockey-stuudio-xyz` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
