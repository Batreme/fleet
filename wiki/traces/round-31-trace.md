# Round 31 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-31`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
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
  10. `sadok-mx` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `rialto-com-au` | `tier1_fast` | `1440×2400px` (3,094,099 B) | `390×2400px` (878,087 B) | 128 | 16 | 290 | 110 | `0.10` / `0.49` | **25.0 / 25.0** |
| `ridetorio-com` | `tier1_fast` | `1440×2400px` (2,974,323 B) | `390×2400px` (1,058,403 B) | 25 | 16 | 298 | 114 | `0.09` / `0.50` | **25.0 / 25.0** |
| `ringpopcandy-com` | `tier1_fast` | `1440×2400px` (2,572,850 B) | `390×2400px` (570,530 B) | 489 | 16 | 302 | 116 | `0.09` / `0.46` | **25.0 / 25.0** |
| `robertoattanasio-com_en` | `tier1_fast` | `1440×900px` (174,267 B) | `390×844px` (13,767 B) | 65 | 16 | 294 | 112 | `0.10` / `0.51` | **25.0 / 25.0** |
| `ross-oneill-com` | `tier1_fast` | `1440×2400px` (830,287 B) | `390×2400px` (266,835 B) | 360 | 16 | 282 | 106 | `0.09` / `0.48` | **25.0 / 25.0** |
| `rozaliabomawrites-com` | `tier1_fast` | `1440×2400px` (1,554,254 B) | `390×2400px` (520,368 B) | 270 | 16 | 282 | 106 | `0.10` / `0.50` | **25.0 / 25.0** |
| `rubenwalma-nl` | `tier1_fast` | `1440×2400px` (1,669,516 B) | `390×2400px` (648,455 B) | 58 | 16 | 290 | 110 | `0.10` / `0.50` | **25.0 / 25.0** |
| `runtimewire-com` | `tier1_fast` | `1440×2400px` (1,860,487 B) | `390×2400px` (594,794 B) | 209 | 16 | 282 | 106 | `0.10` / `0.51` | **25.0 / 25.0** |
| `ruthgriffioen-art` | `tier1_fast` | `1440×900px` (945,500 B) | `390×844px` (283,531 B) | 62 | 16 | 290 | 110 | `0.08` / `0.50` | **25.0 / 25.0** |
| `sadok-mx` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
