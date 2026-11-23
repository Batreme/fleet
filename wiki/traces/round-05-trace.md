# Round 05 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-05`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 05 Target Scope
  1. `articles-gamcare-org-uk` — *The Gamification of Everything · GamCare*
  2. `aryabhangybuilders-com` — *Premium Builders In Kochi · Flats & Apartments · Arya Bhangy*
  3. `ascension-pegassi-be` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  4. `atmos-gallery` — *Blocked (`Live desktop screenshot capture failed (0 valid PNG bytes)`)*
  5. `auge-xp-com` — *Digital Experience Studio · AUGE Experience*
  6. `aviator-yakudoo-games` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  7. `awards-racing` — *Awards Racing*
  8. `awmedia-marketing` — *AW Media & Marketing · UK Web Design Studio*
  9. `aya-nl` — *Danstheater AYA - eigenzinnige voorstellingen voor jong publiek*
  10. `azimuteresidencial-com-br` — *Azimute — Seu próximo horizonte · ASL*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `articles-gamcare-org-uk` | `tier1_fast` | `1440×2400px` (1,859,301 B) | `390×2400px` (495,375 B) | 140 | 16 | 282 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `aryabhangybuilders-com` | `tier1_fast` | `1440×2400px` (1,438,903 B) | `390×2400px` (740,091 B) | 171 | 16 | 292 | 111 | `0.09` / `0.48` | **25.0 / 25.0** |
| `auge-xp-com` | `tier1_fast` | `1440×940px` (28,255 B) | `390×884px` (7,397 B) | 37 | 16 | 276 | 103 | `0.09` / `0.52` | **25.0 / 25.0** |
| `awards-racing` | `tier1_fast` | `1440×900px` (1,256,575 B) | `390×844px` (477,601 B) | 57 | 16 | 289 | 108 | `0.08` / `0.52` | **25.0 / 25.0** |
| `awmedia-marketing` | `tier1_fast` | `1440×2400px` (475,931 B) | `390×2400px` (174,314 B) | 65 | 16 | 286 | 108 | `0.09` / `0.49` | **25.0 / 25.0** |
| `aya-nl` | `tier1_fast` | `1440×2400px` (440,888 B) | `390×2400px` (317,066 B) | 66 | 16 | 306 | 118 | `0.08` / `0.48` | **25.0 / 25.0** |
| `azimuteresidencial-com-br` | `tier1_fast` | `1440×2400px` (1,862,577 B) | `390×2400px` (516,998 B) | 20 | 16 | 302 | 116 | `0.09` / `0.49` | **25.0 / 25.0** |
| `ascension-pegassi-be` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
| `atmos-gallery` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop screenshot capture failed (0 valid PNG bytes)`)** |
| `aviator-yakudoo-games` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
