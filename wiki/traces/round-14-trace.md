# Round 14 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-14`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 14 Target Scope
  1. `explorewashingtonpark-org` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 30000ms exceeded. Call log: - navigating to 'https://explorewashingtonpark.org/', waiting until 'domcontentloaded' )`)*
  2. `exspeedia-com` — *Official IShowSpeed Travel Site Powered by Expedia*
  3. `f-list-cleancreatives-org` — *F-List 2026*
  4. `fabiantjoeaon-com` — *Fabian Tjoe-A-On — Creative technologist*
  5. `faithibiza-com` — *Faith Ibiza · VIP Ibiza Concierge Services*
  6. `familyservicelincoln-org` — *Family Service Lincoln: Everyone Deserves the Chance to Thrive*
  7. `fighterready-com` — *Blocked (`Hard per-target capture deadline exceeded (160s)`)*
  8. `filmmaker-framer-media` — *Filmmaker — Portfolio for Directors & Studios*
  9. `findra-art` — *Findra: the AI character feed*
  10. `fineacts-co` — *Blocked (`Network/Navigation failure (Page.goto: net::ERR_EMPTY_RESPONSE at https://fineacts.co/ Call log: - navigating to 'https://fineacts.co/', waiting until 'domcontentload)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `exspeedia-com` | `tier1_fast` | `1280×828px` (53,300 B) | `390×872px` (18,658 B) | 398 | 16 | 307 | 106 | `0.10` / `0.47` | **25.0 / 25.0** |
| `f-list-cleancreatives-org` | `tier1_fast` | `1280×6624px` (429,352 B) | `390×2616px` (89,062 B) | 56 | 16 | 352 | 116 | `0.09` / `0.48` | **25.0 / 25.0** |
| `fabiantjoeaon-com` | `tier1_fast` | `1280×828px` (38,302 B) | `390×872px` (40,484 B) | 30 | 16 | 319 | 110 | `0.10` / `0.51` | **25.0 / 25.0** |
| `faithibiza-com` | `tier1_fast` | `1280×6624px` (445,342 B) | `390×2616px` (76,626 B) | 242 | 16 | 352 | 116 | `0.11` / `0.50` | **25.0 / 25.0** |
| `familyservicelincoln-org` | `tier1_fast` | `1280×4968px` (335,346 B) | `390×2616px` (77,600 B) | 775 | 16 | 347 | 115 | `0.11` / `0.50` | **25.0 / 25.0** |
| `filmmaker-framer-media` | `tier2_webgl` | `1280×828px` (57,092 B) | `390×872px` (34,374 B) | 29 | 16 | 315 | 111 | `0.10` / `0.51` | **25.0 / 25.0** |
| `findra-art` | `tier1_fast` | `1280×6624px` (841,720 B) | `390×2616px` (81,380 B) | 59 | 16 | 354 | 117 | `0.08` / `0.46` | **25.0 / 25.0** |
| `explorewashingtonpark-org` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 30000ms exceeded. Call `)** |
| `fighterready-com` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (160s)`)** |
| `fineacts-co` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: net::ERR_EMPTY_RESPONSE at http`)** |
