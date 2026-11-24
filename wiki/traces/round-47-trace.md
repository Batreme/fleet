# Round 47 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-47`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `7` live (`3` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 47 Target Scope
  1. `www-governorsmansion-org` — *Louisiana's House · Louisiana Governor's Mansion*
  2. `www-gravelleduparc-com` — *Gravelle du Parc · Événement gravel bike — 2-4 octobre 2026*
  3. `www-greenlock-io` — *Independent Wealth Oversight for Family Offices · GreenLock*
  4. `www-halcyon-co-nz` — *Halcyon · Leading Lighting Specialists*
  5. `www-hauntedbouldercity-com` — *Boulder City Ghost & UFO Walking Tour · Haunted Boulder City*
  6. `www-hollywoodexhibit2026-com` — *ELLE & Esquire, The New Hollywood Photography Exhibition*
  7. `www-honeyquote-com` — *Compare Insurance Quotes Worth Trusting · HoneyQuote*
  8. `www-hoteldutassosorrento-com` — *Blocked (`Upstream HTTP 520 — Cloudflare Origin/WAF Error`)*
  9. `www-huxleysaga-com` — *Blocked (`Empty DOM response (0 bytes, 0 visible text)`)*
  10. `www-iamsunnywang-com` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-governorsmansion-org` | `tier1_fast` | `1280×6624px` (500,326 B) | `390×2616px` (117,918 B) | 171 | 16 | 340 | 110 | `0.14` / `0.55` | **25.0 / 25.0** |
| `www-gravelleduparc-com` | `tier1_fast` | `1280×6624px` (459,022 B) | `390×2616px` (76,736 B) | 53 | 16 | 353 | 122 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-greenlock-io` | `tier1_fast` | `1280×4968px` (256,022 B) | `390×2616px` (87,842 B) | 996 | 16 | 361 | 123 | `0.14` / `0.55` | **25.0 / 25.0** |
| `www-halcyon-co-nz` | `tier1_fast` | `1280×828px` (142,372 B) | `390×2616px` (111,200 B) | 775 | 16 | 321 | 114 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-hauntedbouldercity-com` | `tier1_fast` | `1280×6624px` (350,592 B) | `390×2616px` (52,226 B) | 20 | 16 | 339 | 112 | `0.09` / `0.46` | **25.0 / 25.0** |
| `www-hollywoodexhibit2026-com` | `tier1_fast` | `1280×828px` (30,384 B) | `390×872px` (7,330 B) | 44 | 16 | 306 | 106 | `0.09` / `0.49` | **25.0 / 25.0** |
| `www-honeyquote-com` | `tier1_fast` | `1280×6624px` (566,862 B) | `390×2616px` (101,976 B) | 224 | 16 | 339 | 111 | `0.14` / `0.54` | **25.0 / 25.0** |
| `www-hoteldutassosorrento-com` | `blocked` (`520`) | `none` | `none` | — | — | — | — | — | **Excluded (`Upstream HTTP 520 — Cloudflare Origin/WAF Error`)** |
| `www-huxleysaga-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Empty DOM response (0 bytes, 0 visible text)`)** |
| `www-iamsunnywang-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
