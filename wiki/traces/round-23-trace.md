# Round 23 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-23`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `10` live (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 23 Target Scope
  1. `loot-games-ru` — *LOOT – награды в играх за активность в реальной жизни*
  2. `lorenzolottici-it_en` — *Lorenzo Lottici · Order in chaos*
  3. `lpas-com` — *LPAS - Architecture and Interiors*
  4. `m3-pg-de` — *M3 Planungsgruppe*
  5. `macmillan-studio` — *Christian MacMillan · Independent Tech Lead—Developer*
  6. `madetodisrupt-com` — *Disrupt · Creative Brand Experience Agency*
  7. `magicshot-ai` — *AI Image, Video & Audio Generator all in One Plan*
  8. `manifesto-blandina-org` — *Connect, Create, Change: Manifesto of Blandina*
  9. `matchball-today` — *Matchball · Football quiz: name the match ball in flight*
  10. `matthisgarnier-com` — *Matthis Garnier · Head of Creative Engineering, Polymarket*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `loot-games-ru` | `tier2_webgl` | `1440×900px` (604,133 B) | `390×844px` (168,448 B) | 8 | 16 | 283 | 106 | `0.10` / `0.55` | **25.0 / 25.0** |
| `lorenzolottici-it_en` | `tier1_fast` | `1440×2400px` (63,179 B) | `390×844px` (6,864 B) | 211 | 16 | 282 | 106 | `0.09` / `0.47` | **25.0 / 25.0** |
| `lpas-com` | `tier1_fast` | `1440×2400px` (1,224,818 B) | `390×2400px` (365,252 B) | 12 | 16 | 282 | 106 | `0.11` / `0.53` | **25.0 / 25.0** |
| `m3-pg-de` | `tier1_fast` | `1440×2400px` (356,781 B) | `390×2400px` (247,552 B) | 445 | 16 | 304 | 117 | `0.09` / `0.47` | **25.0 / 25.0** |
| `macmillan-studio` | `tier1_fast` | `1440×900px` (1,585,262 B) | `390×844px` (451,998 B) | 32 | 16 | 282 | 106 | `0.11` / `0.55` | **25.0 / 25.0** |
| `madetodisrupt-com` | `tier1_fast` | `1440×2400px` (567,945 B) | `390×2400px` (174,027 B) | 226 | 16 | 286 | 108 | `0.09` / `0.50` | **25.0 / 25.0** |
| `magicshot-ai` | `tier1_fast` | `1440×2400px` (1,283,570 B) | `390×2400px` (401,649 B) | 159 | 16 | 282 | 106 | `0.09` / `0.44` | **25.0 / 25.0** |
| `manifesto-blandina-org` | `tier1_fast` | `1440×2400px` (21,421 B) | `390×2400px` (676,465 B) | 97 | 16 | 294 | 112 | `0.09` / `0.52` | **25.0 / 25.0** |
| `matchball-today` | `tier1_fast` | `1440×900px` (164,062 B) | `390×844px` (78,645 B) | 18 | 16 | 296 | 112 | `0.11` / `0.53` | **25.0 / 25.0** |
| `matthisgarnier-com` | `tier2_webgl` | `1440×900px` (83,989 B) | `390×844px` (22,195 B) | 253 | 16 | 307 | 118 | `0.09` / `0.48` | **25.0 / 25.0** |
