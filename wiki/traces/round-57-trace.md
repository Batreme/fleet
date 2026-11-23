# Round 57 Execution Trace: Live Recrawl & UI Prompt Blueprint Verification

> [!NOTE]
> **Audit Trace ID**: `TRACE-2026-11-23-ROUND-57`  
> **Active Branch**: `fix/live-recrawl-575-targets`  
> **Analyzed Targets**: `9` live (`1` marked `status: blocked` and excluded from tally per `C1`)  
> **Deterministic Evaluation (`C1`–`C15`)**: **`25.0 / 25.0`**

---

## 1. Round 57 Target Scope
  1. `www-zrk-technology` — *Shahed interceptor with auto-guidance · Zirka*
  2. `www-zzdp-nl` — *Al meer dan 70 jaar betekenisvolle architectuur · ZZDP*
  3. `xavierjoliot-com` — *Xavier Joliot · Développeur Créatif*
  4. `xiloteca-it_en` — *Blocked (`Live mobile screenshot capture failed (0 valid PNG bytes)`)*
  5. `yaas-energy-com` — *YAAS Energy — Zero-Sugar Energy Drink in 5 Bold Flavors*
  6. `yigua-art` — *一卦*
  7. `yoloexe-com` — *YOLO — DxL*
  8. `yoyu-design` — *ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サービス*
  9. `yumlog-dev` — *YumLog — the calorie tracker you can talk to, for Apple Watch and iPhone*
  10. `yuyafilmstudio-dev` — *YUYA FILM STUDIO*

---

## 2. Live Capture & Ground-Truth Extraction Metrics (Verified PNG IHDR, Computed Styles & DOM/CSS)

| Target Slug | Capture Tier | Desktop PNG (`assets/desktop.png`) | Mobile PNG (`assets/mobile.png`) | Raw CSS Vars | Curated Root Vars | Blueprint Lines | Unsplit Fence Lines | Max Jaccard (Line / Word) | Truth Eval Score |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `www-zrk-technology` | `tier1_fast` | `1440×2400px` (1,492,191 B) | `390×2400px` (473,732 B) | 8 | 16 | 284 | 107 | `0.09` / `0.50` | **25.0 / 25.0** |
| `www-zzdp-nl` | `tier1_fast` | `1440×2400px` (685,849 B) | `390×2400px` (354,509 B) | 209 | 16 | 290 | 110 | `0.09` / `0.52` | **25.0 / 25.0** |
| `xavierjoliot-com` | `tier1_fast` | `1440×900px` (880,802 B) | `390×844px` (28,204 B) | 37 | 16 | 304 | 117 | `0.08` / `0.51` | **25.0 / 25.0** |
| `yaas-energy-com` | `tier1_fast` | `1440×2400px` (505,313 B) | `390×2400px` (155,067 B) | 54 | 16 | 282 | 106 | `0.09` / `0.51` | **25.0 / 25.0** |
| `yigua-art` | `tier1_fast` | `1440×977px` (178,634 B) | `390×1033px` (86,403 B) | 60 | 16 | 286 | 108 | `0.08` / `0.51` | **25.0 / 25.0** |
| `yoloexe-com` | `tier1_fast` | `1440×2400px` (572,665 B) | `390×2400px` (185,472 B) | 29 | 16 | 290 | 110 | `0.09` / `0.53` | **25.0 / 25.0** |
| `yoyu-design` | `tier2_webgl` | `1440×900px` (62,748 B) | `390×844px` (27,744 B) | 95 | 16 | 298 | 114 | `0.08` / `0.52` | **25.0 / 25.0** |
| `yumlog-dev` | `tier1_fast` | `1440×2400px` (1,068,054 B) | `390×2400px` (388,945 B) | 26 | 16 | 302 | 116 | `0.09` / `0.50` | **25.0 / 25.0** |
| `yuyafilmstudio-dev` | `tier2_webgl` | `1440×900px` (470,335 B) | `390×844px` (138,650 B) | 9 | 16 | 288 | 109 | `0.08` / `0.53` | **25.0 / 25.0** |
| `xiloteca-it_en` | `blocked` (`200`) | `none` | `none` | — | — | — | — | — | **Excluded (`Live mobile screenshot capture failed (0 valid PNG bytes)`)** |
