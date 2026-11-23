# Round 24 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-24`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 24 Target Scope
  1. `mauricemoynihan-com` — *Maurice Moynihan*
  2. `mejuma-tuscany-com` — *Mejuma Tuscany*
  3. `members-play-lacoste-com_ace-breaker-rg` — *Lacoste - Ace breaker*
  4. `michellekayewashington-com` — *Michelle Kaye — Fine Arts · Contemporary Artist, Charleston SC*
  5. `microdose-studio` — *Microdose Studio - Design & Development Agency for Startups*
  6. `midnightvideo-cuchillo-rocks` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  7. `miligram-pt` — *Miligram Brand Agency*
  8. `milky-solar` — *Earth*
  9. `milledollars-fr` — *MilleDollars*
  10. `mindofakira-com` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 35000ms exceeded. Call log: - navigating to 'http://mindofakira.com/', waiting until 'domcontentloaded' )`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `mauricemoynihan-com` | `tier1_fast` | `1440×2400px` (167,688 B) | `390×2400px` (197,685 B) | 25 | 16 | 284 | 107 | `0.09` / `0.51` | **25.0 / 25.0** |
| `mejuma-tuscany-com` | `tier1_fast` | `1440×2400px` (2,505,711 B) | `390×2400px` (692,194 B) | 99 | 16 | 289 | 109 | `0.09` / `0.48` | **25.0 / 25.0** |
| `members-play-lacoste-com_ace-breaker-rg` | `tier2_webgl` | `1440×900px` (26,064 B) | `390×844px` (257,646 B) | 53 | 16 | 281 | 104 | `0.10` / `0.56` | **25.0 / 25.0** |
| `michellekayewashington-com` | `tier1_fast` | `1440×900px` (453,364 B) | `390×844px` (125,024 B) | 42 | 16 | 287 | 108 | `0.10` / `0.53` | **25.0 / 25.0** |
| `microdose-studio` | `tier1_fast` | `1440×2400px` (534,868 B) | `390×2400px` (166,712 B) | 488 | 16 | 296 | 113 | `0.09` / `0.50` | **25.0 / 25.0** |
| `miligram-pt` | `tier1_fast` | `1440×2400px` (1,372,198 B) | `390×2400px` (430,425 B) | 257 | 16 | 300 | 115 | `0.09` / `0.48` | **25.0 / 25.0** |
| `milky-solar` | `tier1_fast` | `1440×900px` (67,511 B) | `390×844px` (50,740 B) | 0 | 12 | 267 | 97 | `0.10` / `0.56` | **25.0 / 25.0** |
| `milledollars-fr` | `tier2_webgl` | `1440×900px` (16,384 B) | `390×844px` (178,274 B) | 120 | 16 | 282 | 106 | `0.09` / `0.52` | **25.0 / 25.0** |
| `midnightvideo-cuchillo-rocks` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `mindofakira-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 35000ms exceeded. Call `)** |
