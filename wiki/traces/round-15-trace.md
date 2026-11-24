# Round 15 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-15`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `6` live (`4` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 15 Target Scope
  1. `fitosauna-com` — *Blocked (`Upstream HTTP 520 — Cloudflare Origin/WAF Error`)*
  2. `flycrooked-com` — *Crow · Trip planner and flight finder for iPhone*
  3. `fondation-canadiens-com` — *Montreal Canadiens Children's Foundation - Play to thrive*
  4. `fontsight-xyz` — *Fontsight: What Font Is That? Font Finder for Chrome*
  5. `forgeautomotive-co-uk` — *Blocked (`Headless Preloader / Blank Viewport Capture (solid blank desktop viewport)`)*
  6. `foxvaluations-com-au` — *Property valuations Brisbane · Fox Valuations*
  7. `fromearth-love` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call log: - navigating to 'http://fromearth.love/', waiting until 'domcontentloaded' )`)*
  8. `gallery-play-be` — *Home - Gallery Play*
  9. `giallostudio-it_en-the-experience` — *The Experience: Milan lights up in yellow · Giallo*
  10. `giga-ai` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 30000ms exceeded. Call log: - navigating to 'https://giga.ai/', waiting until 'domcontentloaded' )`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `flycrooked-com` | `tier1_fast` | `1280×6624px` (921,336 B) | `390×2616px` (102,780 B) | 80 | 16 | 359 | 122 | `0.09` / `0.50` | **25.0 / 25.0** |
| `fondation-canadiens-com` | `tier1_fast` | `1280×6624px` (466,060 B) | `390×2616px` (90,024 B) | 320 | 16 | 349 | 111 | `0.10` / `0.44` | **25.0 / 25.0** |
| `fontsight-xyz` | `tier1_fast` | `1280×6624px` (341,584 B) | `390×2616px` (85,006 B) | 42 | 16 | 365 | 120 | `0.09` / `0.50` | **25.0 / 25.0** |
| `foxvaluations-com-au` | `tier1_fast` | `1280×4968px` (290,536 B) | `390×2616px` (65,340 B) | 29 | 16 | 357 | 121 | `0.08` / `0.50` | **25.0 / 25.0** |
| `gallery-play-be` | `tier1_fast` | `1280×828px` (89,806 B) | `390×2616px` (95,848 B) | 182 | 16 | 311 | 109 | `0.09` / `0.46` | **25.0 / 25.0** |
| `giallostudio-it_en-the-experience` | `tier1_fast` | `1280×6624px` (267,028 B) | `390×2616px` (68,076 B) | 118 | 16 | 350 | 112 | `0.10` / `0.45` | **25.0 / 25.0** |
| `fitosauna-com` | `blocked` (`520`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 520 — Cloudflare Origin/WAF Error`)** |
| `forgeautomotive-co-uk` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Headless Preloader / Blank Viewport Capture (solid blank desktop viewp`)** |
| `fromearth-love` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call `)** |
| `giga-ai` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 30000ms exceeded. Call `)** |
