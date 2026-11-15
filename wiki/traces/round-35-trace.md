# Round 35 Execution Trace: UI Prompt Blueprint Expansion

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-15-ROUND-35`  
> **Active Branch**: `feat/ui-prompt-expansion`  
> **Analyzed Targets**: `10` (`0` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C14`)**: **`25.0 / 25.0`**

---

## 1. Round 35 Target Scope
  1. `supermodels-phototypelabs-com` — *SUPERMODELS — Image, Video, Voice & Music, Pay Per Use* (`https://supermodels.phototypelabs.com`)
  2. `switchblade-awwwards-vercel-app` — *SWITCHBLADE™* (`https://switchblade-awwwards.vercel.app/`)
  3. `tabletales-crz-studio` — *Table Tales by CRZ.STUDIO · Board Game Collection & Play Log* (`https://tabletales.crz.studio/`)
  4. `tamasolajos-com` — *Tamás Olajos — AI Filmmaker & Director · London & Budapest* (`https://tamasolajos.com/`)
  5. `tej-as_story` — *The testimony and autobiography of Tejas Kumar* (`https://tej.as/story`)
  6. `templates-preview-oxvo-app_t-oxvo-original-studio-max-commerce-3d-latest` — *SOLARA HALO S1 · Sound with presence.* (`https://templates-preview.oxvo.app/t/oxvo-original-studio-max-commerce-3d/latest/#/`)
  7. `tengilemalamala-com` — *Luxury Safari Experiences in Greater Kruger & Sabi Sand · Tengile MalaMa...* (`https://tengilemalamala.com/`)
  8. `the-family-rice-tray-vercel-app` — *Mâm Cơm — the Vietnamese family rice tray* (`https://the-family-rice-tray.vercel.app`)
  9. `thebranx-com` — *The branding agency for startups, AI & SaaS - The Branx* (`https://thebranx.com`)
  10. `thecassandravale-com` — *Cassandra Vale · Fashion, Stories & Branded Content* (`https://thecassandravale.com/`)

---

## 2. Ground-Truth Asset & Extraction Metrics (Verified PNG IHDR & DOM/CSS)

| Target Slug | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `supermodels-phototypelabs-com` | `1440×2400px` (192,781 B) | `390×2400px` (143,446 B) | 123 | 16 | 260 | 108 | `0.11` / `0.51` | **25.0 / 25.0** |
| `switchblade-awwwards-vercel-app` | `1440×2400px` (83,838 B) | `390×2400px` (47,513 B) | 58 | 16 | 256 | 106 | `0.09` / `0.53` | **25.0 / 25.0** |
| `tabletales-crz-studio` | `1440×2400px` (47,639 B) | `390×2400px` (410,312 B) | 45 | 16 | 256 | 106 | `0.10` / `0.52` | **25.0 / 25.0** |
| `tamasolajos-com` | `1440×2400px` (285,597 B) | `390×2400px` (93,029 B) | 1 | 13 | 233 | 93 | `0.11` / `0.52` | **25.0 / 25.0** |
| `tej-as_story` | `1440×2400px` (803,419 B) | `390×2400px` (687,670 B) | 148 | 16 | 262 | 109 | `0.11` / `0.51` | **25.0 / 25.0** |
| `templates-preview-oxvo-app_t-oxvo-original-studio-max-commerce-3d-latest` | `1440×2400px` (933,214 B) | `390×2400px` (172,421 B) | 92 | 16 | 256 | 106 | `0.11` / `0.52` | **25.0 / 25.0** |
| `tengilemalamala-com` | `1440×11566px` (4,902,911 B) | `390×2400px` (128,582 B) | 5 | 16 | 258 | 107 | `0.09` / `0.51` | **25.0 / 25.0** |
| `the-family-rice-tray-vercel-app` | `1440×10547px` (4,240,140 B) | `390×2400px` (584,021 B) | 36 | 16 | 270 | 113 | `0.10` / `0.51` | **25.0 / 25.0** |
| `thebranx-com` | `1440×9398px` (2,139,066 B) | `390×2400px` (141,198 B) | 191 | 16 | 256 | 106 | `0.11` / `0.53` | **25.0 / 25.0** |
| `thecassandravale-com` | `1440×2400px` (72,962 B) | `390×2400px` (59,738 B) | 42 | 16 | 264 | 110 | `0.10` / `0.50` | **25.0 / 25.0** |
