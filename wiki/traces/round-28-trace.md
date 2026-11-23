# Round 28 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-28`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 28 Target Scope
  1. `opportunity-waltonfamilyfoundation-org` — *Access to Opportunity: Gallup Research · Walton Family Foundation*
  2. `overworldaudio-com` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  3. `palaceskateboards-com` — *PALACE SKATEBOARDS*
  4. `palominoprod-com` — *Palomino — Cinematic Sports & Brand Films*
  5. `pankow-band` — *Die Pankow Zeitmaschine - Website der Berliner Rockband PANKOW*
  6. `patmos-studio` — *Patmos · Wahr, Gut, Schön*
  7. `pda-archi_en` — *Architecture firm in Paris: renovation, refurbishment — PDA*
  8. `peabodyhouse-com` — *Peabody House • Digital Brand World Implementation Studio*
  9. `peaches-world` — *Peaches – Webdesign Pratteln, Basel · Websites worth pressing Enter for*
  10. `perappelgren-de` — *Per Appelgren*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `opportunity-waltonfamilyfoundation-org` | `tier1_fast` | `1440×2400px` (692,883 B) | `390×2400px` (123,990 B) | 74 | 16 | 290 | 110 | `0.11` / `0.53` | **25.0 / 25.0** |
| `palaceskateboards-com` | `tier1_fast` | `1440×900px` (884,795 B) | `390×844px` (298,406 B) | 81 | 16 | 283 | 106 | `0.12` / `0.57` | **25.0 / 25.0** |
| `palominoprod-com` | `tier1_fast` | `1440×2400px` (698,206 B) | `390×2400px` (732,843 B) | 71 | 16 | 288 | 109 | `0.11` / `0.56` | **25.0 / 25.0** |
| `pankow-band` | `tier1_fast` | `1440×2400px` (2,823,844 B) | `390×2400px` (1,210,203 B) | 31 | 16 | 288 | 109 | `0.09` / `0.46` | **25.0 / 25.0** |
| `patmos-studio` | `tier2_webgl` | `1440×900px` (58,133 B) | `390×844px` (42,448 B) | 72 | 16 | 280 | 104 | `0.12` / `0.53` | **25.0 / 25.0** |
| `pda-archi_en` | `tier1_fast` | `1440×900px` (1,982,244 B) | `390×844px` (580,088 B) | 133 | 16 | 288 | 109 | `0.09` / `0.54` | **25.0 / 25.0** |
| `peabodyhouse-com` | `tier1_fast` | `1440×2400px` (557,096 B) | `390×2400px` (127,571 B) | 53 | 16 | 292 | 111 | `0.10` / `0.50` | **25.0 / 25.0** |
| `peaches-world` | `tier1_fast` | `1440×900px` (150,407 B) | `390×844px` (87,096 B) | 0 | 12 | 272 | 100 | `0.09` / `0.52` | **25.0 / 25.0** |
| `perappelgren-de` | `tier1_fast` | `1440×900px` (322,583 B) | `390×2400px` (127,982 B) | 30 | 16 | 284 | 107 | `0.11` / `0.57` | **25.0 / 25.0** |
| `overworldaudio-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
