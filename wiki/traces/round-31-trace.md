# Round 31 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-31`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 31 Target Scope
  1. `rialto-com-au` — *Rialto · The icon of Melbourne's skyline*
  2. `ridetorio-com` — *The Ride to Rio · Bicycle documentary, Los Angeles to Rio*
  3. `ringpopcandy-com` — *Ring Pop® — Candy for Every Celebration*
  4. `robertoattanasio-com_en` — *Roberto Attanasio*
  5. `ross-oneill-com` — *Ross O'Neill · Freelance Web Developer and Designer in Perth*
  6. `rozaliabomawrites-com` — *Rozalia Boma — Multicultural Romance Author*
  7. `rubenwalma-nl` — *Ruben Walma – Filmmaker & videoproductie Groningen*
  8. `runtimewire-com` — *RuntimeWire: Breaking tech news. Before everyone else.*
  9. `ruthgriffioen-art` — *Ruth Griffioen – Colourful paintings & art prints*
  10. `sadok-mx` — *Blocked (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call log: - navigating to 'https://sadok.mx/', waiting until 'domcontentloaded' )`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `rialto-com-au` | `tier1_fast` | `1280×6624px` (290,038 B) | `390×2616px` (7,248 B) | 128 | 16 | 355 | 115 | `0.10` / `0.49` | **25.0 / 25.0** |
| `ridetorio-com` | `tier1_fast` | `1280×6624px` (1,137,320 B) | `390×2616px` (122,482 B) | 25 | 16 | 343 | 118 | `0.09` / `0.50` | **25.0 / 25.0** |
| `ringpopcandy-com` | `tier1_fast` | `1280×6624px` (496,984 B) | `390×2616px` (113,164 B) | 975 | 16 | 367 | 121 | `0.09` / `0.46` | **25.0 / 25.0** |
| `robertoattanasio-com_en` | `tier1_fast` | `1280×828px` (23,280 B) | `390×872px` (3,566 B) | 65 | 16 | 321 | 115 | `0.10` / `0.50` | **25.0 / 25.0** |
| `ross-oneill-com` | `tier1_fast` | `1280×4140px` (274,784 B) | `390×2616px` (92,996 B) | 360 | 16 | 341 | 111 | `0.09` / `0.46` | **25.0 / 25.0** |
| `rozaliabomawrites-com` | `tier1_fast` | `1280×6624px` (793,932 B) | `390×2616px` (130,422 B) | 270 | 16 | 340 | 110 | `0.10` / `0.51` | **25.0 / 25.0** |
| `rubenwalma-nl` | `tier1_fast` | `1280×4968px` (193,454 B) | `390×2616px` (75,808 B) | 58 | 16 | 343 | 114 | `0.10` / `0.51` | **25.0 / 25.0** |
| `runtimewire-com` | `tier1_fast` | `1280×6624px` (471,604 B) | `390×2616px` (83,536 B) | 209 | 16 | 348 | 112 | `0.10` / `0.48` | **25.0 / 25.0** |
| `ruthgriffioen-art` | `tier1_fast` | `1280×6624px` (475,490 B) | `390×872px` (30,308 B) | 62 | 16 | 346 | 114 | `0.09` / `0.51` | **25.0 / 25.0** |
| `sadok-mx` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Network/Navigation failure (Page.goto: Timeout 22000ms exceeded. Call `)** |
