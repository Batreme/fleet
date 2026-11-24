# Round 35 Execution Trace: Full Behavioral Journey Crawl (`behavioral_journey_v2`) & WebP Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-24-ROUND-35`  
> **Active Branch**: `feat/full-behavioral-journey-webp`  
> **Analyzed Targets**: `8` live (`2` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 35 Target Scope
  1. `supermodels-phototypelabs-com` — *Blocked (`Live desktop behavioral capture failed (0 valid keyframes)`)*
  2. `switchblade-awwwards-vercel-app` — *Blocked (`Live mobile behavioral capture failed (0 valid WebP frames)`)*
  3. `tabletales-crz-studio` — *Table Tales by CRZ.STUDIO · Board Game Collection & Play Log*
  4. `tamasolajos-com` — *Tamás Olajos — AI Filmmaker & Director · London & Budapest*
  5. `tej-as_story` — *The testimony and autobiography of Tejas Kumar*
  6. `templates-preview-oxvo-app_t-oxvo-original-studio-max-commerce-3d-latest` — *SOLARA HALO S1 · Sound with presence.*
  7. `tengilemalamala-com` — *Luxury Safari Experiences in Greater Kruger & Sabi Sand · Tengile MalaMa...*
  8. `the-family-rice-tray-vercel-app` — *Mâm Cơm — the Vietnamese family rice tray*
  9. `thebranx-com` — *The branding agency for startups, AI & SaaS - The Branx*
  10. `thecassandravale-com` — *Cassandra Vale · Fashion, Stories & Branded Content*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified WebP Filmstrips, Behavioral Telemetry, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop Journey (`assets/desktop-journey.webp`) | Mobile Journey (`assets/mobile-journey.webp`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `tabletales-crz-studio` | `tier1_fast` | `1280×6624px` (436,274 B) | `390×872px` (29,662 B) | 45 | 16 | 342 | 113 | `0.09` / `0.50` | **25.0 / 25.0** |
| `tamasolajos-com` | `tier1_fast` | `1280×828px` (12,836 B) | `390×2616px` (15,014 B) | 1 | 13 | 296 | 100 | `0.10` / `0.51` | **25.0 / 25.0** |
| `tej-as_story` | `tier1_fast` | `1280×6624px` (423,850 B) | `390×2616px` (90,656 B) | 743 | 16 | 360 | 120 | `0.09` / `0.48` | **25.0 / 25.0** |
| `templates-preview-oxvo-app_t-oxvo-original-studio-max-commerce-3d-latest` | `tier1_fast` | `1280×6624px` (193,428 B) | `390×2616px` (51,500 B) | 95 | 16 | 333 | 110 | `0.11` / `0.48` | **25.0 / 25.0** |
| `tengilemalamala-com` | `tier1_fast` | `1280×6624px` (774,942 B) | `390×2616px` (139,068 B) | 5 | 16 | 350 | 111 | `0.10` / `0.50` | **25.0 / 25.0** |
| `the-family-rice-tray-vercel-app` | `tier1_fast` | `1280×6624px` (901,266 B) | `390×2616px` (127,606 B) | 36 | 16 | 351 | 119 | `0.10` / `0.51` | **25.0 / 25.0** |
| `thebranx-com` | `tier1_fast` | `1280×6624px` (402,728 B) | `390×2616px` (42,808 B) | 199 | 16 | 362 | 117 | `0.11` / `0.48` | **25.0 / 25.0** |
| `thecassandravale-com` | `tier1_fast` | `1280×6624px` (469,540 B) | `390×2616px` (90,002 B) | 42 | 16 | 335 | 113 | `0.09` / `0.48` | **25.0 / 25.0** |
| `supermodels-phototypelabs-com` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live desktop behavioral capture failed (0 valid keyframes)`)** |
| `switchblade-awwwards-vercel-app` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile behavioral capture failed (0 valid WebP frames)`)** |
