# Round 35 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-35`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 35 Target Scope
  1. `supermodels-phototypelabs-com` — *SUPERMODELS — Image, Video, Voice & Music, Pay Per Use*
  2. `switchblade-awwwards-vercel-app` — *Blocked (`Hard per-target capture deadline exceeded (150s)`)*
  3. `tabletales-crz-studio` — *Table Tales by CRZ.STUDIO · Board Game Collection & Play Log*
  4. `tamasolajos-com` — *Tamás Olajos — AI Filmmaker & Director · London & Budapest*
  5. `tej-as_story` — *The testimony and autobiography of Tejas Kumar*
  6. `templates-preview-oxvo-app_t-oxvo-original-studio-max-commerce-3d-latest` — *SOLARA HALO S1 · Sound with presence.*
  7. `tengilemalamala-com` — *Luxury Safari Experiences in Greater Kruger & Sabi Sand · Tengile MalaMa...*
  8. `the-family-rice-tray-vercel-app` — *Mâm Cơm — the Vietnamese family rice tray*
  9. `thebranx-com` — *The branding agency for startups, AI & SaaS - The Branx*
  10. `thecassandravale-com` — *Cassandra Vale · Fashion, Stories & Branded Content*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `supermodels-phototypelabs-com` | `tier1_fast` | `1440×900px` (506,315 B) | `390×2400px` (253,875 B) | 123 | 16 | 294 | 112 | `0.09` / `0.51` | **25.0 / 25.0** |
| `tabletales-crz-studio` | `tier2_webgl` | `1440×900px` (774,061 B) | `390×844px` (137,541 B) | 45 | 16 | 288 | 109 | `0.09` / `0.50` | **25.0 / 25.0** |
| `tamasolajos-com` | `tier1_fast` | `1440×900px` (6,508 B) | `390×1082px` (2,887 B) | 1 | 13 | 267 | 97 | `0.09` / `0.51` | **25.0 / 25.0** |
| `tej-as_story` | `tier1_fast` | `1440×2400px` (942,794 B) | `390×2400px` (478,293 B) | 148 | 16 | 300 | 115 | `0.10` / `0.49` | **25.0 / 25.0** |
| `templates-preview-oxvo-app_t-oxvo-original-studio-max-commerce-3d-latest` | `tier1_fast` | `1440×2400px` (614,878 B) | `390×2400px` (130,142 B) | 92 | 16 | 282 | 106 | `0.11` / `0.50` | **25.0 / 25.0** |
| `tengilemalamala-com` | `tier1_fast` | `1440×2400px` (1,441,312 B) | `390×2400px` (831,063 B) | 5 | 16 | 282 | 106 | `0.10` / `0.51` | **25.0 / 25.0** |
| `the-family-rice-tray-vercel-app` | `tier1_fast` | `1440×2400px` (2,744,266 B) | `390×2400px` (868,959 B) | 38 | 16 | 300 | 115 | `0.10` / `0.51` | **25.0 / 25.0** |
| `thebranx-com` | `tier2_webgl` | `1440×900px` (41,709 B) | `390×844px` (18,621 B) | 195 | 16 | 296 | 113 | `0.11` / `0.50` | **25.0 / 25.0** |
| `thecassandravale-com` | `tier1_fast` | `1440×2400px` (2,689,135 B) | `390×2400px` (660,574 B) | 43 | 16 | 291 | 110 | `0.09` / `0.49` | **25.0 / 25.0** |
| `switchblade-awwwards-vercel-app` | `blocked` (`None`) | `none` | `none` | — | — | — | — | — | **Excluded (`Hard per-target capture deadline exceeded (150s)`)** |
