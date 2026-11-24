# Round 19 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-19`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 19 Target Scope
  1. `janiswanger-ch` — *Janis Wanger — Creative Engineer in Bern*
  2. `jaspreetsingh-xyz` — *Blocked (`Hard per-target capture deadline exceeded (160s)`)*
  3. `jetalto-com` — *JetALto, Private Jet Charter · Fly Anywhere, On Your Schedule*
  4. `jimo-ai_product-ai` — *AI Agent for User Onboarding in SaaS · Jimo*
  5. `jjettas-com` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  6. `jld2nd-dev` — *JLD'2nd – Designer & Developer*
  7. `jockey-stuudio-xyz` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call log: - navigating to 'https://jockey.stuudio.xyz/', waiting until 'domcontentloaded' )`)*
  8. `johnhardy-com_collections-billie-eilish-and-finneas` — *Billie Eilish and FINNEAS – John Hardy*
  9. `jonmccormack-com` — *Patterns - Jon McCormack*
  10. `jozue-fr` — *Josué Pichot, freelance art director and photographer in Paris*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `janiswanger-ch` | `tier1_fast` | `1280×828px` (41,876 B) | `390×2616px` (73,078 B) | 76 | 16 | 311 | 109 | `0.09` / `0.47` | **25.0 / 25.0** |
| `jetalto-com` | `tier1_fast` | `1280×6624px` (419,486 B) | `390×2616px` (79,498 B) | 47 | 16 | 346 | 118 | `0.09` / `0.48` | **25.0 / 25.0** |
| `jimo-ai_product-ai` | `tier1_fast` | `1280×6624px` (273,746 B) | `390×2616px` (46,938 B) | 317 | 16 | 350 | 115 | `0.09` / `0.48` | **25.0 / 25.0** |
| `jld2nd-dev` | `tier1_fast` | `1280×6624px` (165,714 B) | `390×2616px` (33,754 B) | 63 | 16 | 339 | 111 | `0.09` / `0.49` | **25.0 / 25.0** |
| `johnhardy-com_collections-billie-eilish-and-finneas` | `tier1_fast` | `1280×6624px` (395,482 B) | `390×2616px` (53,082 B) | 966 | 16 | 346 | 113 | `0.09` / `0.45` | **25.0 / 25.0** |
| `jonmccormack-com` | `tier1_fast` | `1280×6624px` (861,888 B) | `390×1744px` (46,512 B) | 213 | 16 | 345 | 111 | `0.09` / `0.48` | **25.0 / 25.0** |
| `jozue-fr` | `tier1_fast` | `1280×6624px` (269,672 B) | `390×2616px` (32,792 B) | 104 | 16 | 347 | 111 | `0.09` / `0.49` | **25.0 / 25.0** |
| `jaspreetsingh-xyz` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (160s)`)** |
| `jjettas-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `jockey-stuudio-xyz` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call `)** |
