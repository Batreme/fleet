# Round 15 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-15`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `9` (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 15 Target Scope
  1. `fitosauna-com` — *Blocked (`Cloudflare HTTP 520 Origin Error (Web server is returning an unknown error)`)*
  2. `flycrooked-com` — *Crow · Trip planner and flight finder for iPhone* (`https://flycrooked.com/`)
  3. `fondation-canadiens-com` — *Fondation des Canadiens pour l'enfance - Bouger pour grandir* (`https://fondation.canadiens.com/`)
  4. `fontsight-xyz` — *Fontsight: What Font Is That? Font Finder for Chrome* (`https://fontsight.xyz/`)
  5. `forgeautomotive-co-uk` — *Bespoke Vehicle Builds & Styling · Forge Automotive* (`https://forgeautomotive.co.uk/`)
  6. `foxvaluations-com-au` — *Property valuations Brisbane · Fox Valuations* (`https://foxvaluations.com.au`)
  7. `fromearth-love` — *fromearth · 2050 — Explore climate projections* (`http://fromearth.love`)
  8. `gallery-play-be` — *Home - Gallery Play* (`https://gallery-play.be/`)
  9. `giallostudio-it_en-the-experience` — *The Experience: Milan lights up in yellow · Giallo* (`https://giallostudio.it/en/the-experience`)
  10. `giga-ai` — *Giga: AI support agents that improve your metrics* (`https://giga.ai/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `fitosauna-com` | `status: blocked` | `status: blocked` | — | — | — | — | — | **Excluded (`Cloudflare HTTP 520 Origin Error (Web server is returning an unknown error)`)** |
| `flycrooked-com` | `1440×1254px` (311,959 B) | `390×2400px` (293,681 B) | 86 | 16 | 256 | 106 | `0.09` / `0.50` | **25.0 / 25.0** |
| `fondation-canadiens-com` | `1440×10722px` (1,734,065 B) | `390×2400px` (46,077 B) | 190 | 16 | 256 | 106 | `0.09` / `0.46` | **25.0 / 25.0** |
| `fontsight-xyz` | `1440×11776px` (1,696,563 B) | `390×2400px` (174,413 B) | 42 | 16 | 276 | 116 | `0.08` / `0.50` | **25.0 / 25.0** |
| `forgeautomotive-co-uk` | `1440×2400px` (141,443 B) | `390×2400px` (91,978 B) | 20 | 16 | 248 | 102 | `0.10` / `0.47` | **25.0 / 25.0** |
| `foxvaluations-com-au` | `1440×4367px` (1,325,406 B) | `390×2400px` (314,195 B) | 29 | 16 | 270 | 113 | `0.08` / `0.50` | **25.0 / 25.0** |
| `fromearth-love` | `1440×2400px` (653,637 B) | `390×2400px` (516,470 B) | 47 | 16 | 256 | 106 | `0.10` / `0.48` | **25.0 / 25.0** |
| `gallery-play-be` | `1440×10973px` (2,355,250 B) | `390×2400px` (89,699 B) | 182 | 16 | 256 | 106 | `0.09` / `0.47` | **25.0 / 25.0** |
| `giallostudio-it_en-the-experience` | `1440×7400px` (726,357 B) | `390×2400px` (256,150 B) | 118 | 16 | 258 | 107 | `0.09` / `0.47` | **25.0 / 25.0** |
| `giga-ai` | `1440×15714px` (1,515,385 B) | `390×2400px` (41,622 B) | 531 | 16 | 276 | 116 | `0.08` / `0.47` | **25.0 / 25.0** |
