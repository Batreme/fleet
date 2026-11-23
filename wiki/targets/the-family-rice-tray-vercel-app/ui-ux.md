---
title: "UI & UX Architecture: the-family-rice-tray-vercel-app"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: the-family-rice-tray-vercel-app

## Overview & Design Identity
- **Target**: `the-family-rice-tray-vercel-app` (**Mâm Cơm — the Vietnamese family rice tray**)
- **Production URL**: [https://the-family-rice-tray.vercel.app](https://the-family-rice-tray.vercel.app)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#5e0712` canvas, `#f7efe0` ink, `#ff0000` accent)
- **Summary**: A love letter to mâm cơm, the round tray of shared dishes at the centre of every Vietnamese home — laid out on the face of a Đông Sơn bro...
- **Total Clean CSS Variables Extracted**: `38` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Big Shoulders Display`
- **Body Font Stack**: `Be Vietnam Pro`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 134.4px`, `line-height: 110.208px`, `font-weight: 900`, `letter-spacing: -2.016px`); CSS variables `--font-display: "Big Shoulders Display", "Arial Narrow", system-ui, sans-serif`; rule `h1` (`font-size: var(--t-hero)`, `line-height: 0.82`, `letter-spacing: -0.015em`, `font-weight: 900`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 73.6px`, `line-height: 75.072px`, `font-weight: 900`, `letter-spacing: -0.736px`); CSS variables `--t-h2: clamp(2.4rem, 6vw, 4.6rem)`; rule `h2` (`font-size: var(--t-h2)`, `font-weight: 900`)
- **Body Copy**: live computed `body` (`font-size: 18.56px`, `line-height: 31.9232px`, `font-weight: 300`); CSS variables `--font-body: "Be Vietnam Pro", system-ui, -apple-system, "Segoe UI", sans-serif`, `--t-body: clamp(1rem, 0.55vw + 0.9rem, 1.16rem)`; rule `body` (`font-size: var(--t-body)`, `line-height: 1.72`, `font-weight: 300`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18.56px`, `line-height: 31.9232px`, `font-weight: 300`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#5e0712` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f7efe0` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#3f040c` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff0000` | `.stepper button { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#f0be6b` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#a0582e` | `.btn--ghost { border: #a0582e }` |
| **Variable Token (`--red-700`)** | `#7a0a18` | `var(--red-700)` in `:root` |
| **Variable Token (`--red-600`)** | `#8b0c1c` | `var(--red-600)` in `:root` |
| **Variable Token (`--red-500`)** | `#a8121f` | `var(--red-500)` in `:root` |
| **Variable Token (`--gold-400`)** | `#e3a94a` | `var(--gold-400)` in `:root` |
| **Variable Token (`--gold-200`)** | `#f7d9a0` | `var(--gold-200)` in `:root` |
| **Variable Token (`--jade`)** | `#2e6b58` | `var(--jade)` in `:root` |
| **Variable Token (`--jade-light`)** | `#7fb8a2` | `var(--jade-light)` in `:root` |
| **Variable Token (`--cream-dim`)** | `#dccdb4` | `var(--cream-dim)` in `:root` |
| **Variable Token (`--ink`)** | `#1a0509` | `var(--ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--red-900` | `#3f040c` | Color / Atmospheric Token |
| `--red-800` | `#5e0712` | Color / Atmospheric Token |
| `--red-700` | `#7a0a18` | Color / Atmospheric Token |
| `--red-600` | `#8b0c1c` | Color / Atmospheric Token |
| `--red-500` | `#a8121f` | Color / Atmospheric Token |
| `--gold-400` | `#e3a94a` | Color / Atmospheric Token |
| `--gold-300` | `#f0be6b` | Color / Atmospheric Token |
| `--gold-200` | `#f7d9a0` | Color / Atmospheric Token |
| `--jade` | `#2e6b58` | Color / Atmospheric Token |
| `--jade-light` | `#7fb8a2` | Canvas / Surface Token |
| `--cream` | `#f7efe0` | Color / Atmospheric Token |
| `--cream-dim` | `#dccdb4` | Color / Atmospheric Token |
| `--cream-faint` | `rgba(247, 239, 224, 0.62)` | Color / Atmospheric Token |
| `--ink` | `#1a0509` | Typography Ink Token |
| `--font-display` | `"Big Shoulders Display", "Arial Narrow", system-ui, sans-serif` | Typography / Scale Token |
| `--font-body` | `"Be Vietnam Pro", system-ui, -apple-system, "Segoe UI", sans-serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.masthead> — `the-family-rice-tray-vercel-app`)**:
   - Landmark `<header class="masthead">` (`1440x67px`) hosting `Mâm Cơm — the Vietnamese family rice` navigation (`The Tray · The Legend · The Recipe · Nếp Nhà`), DOM attributes (`data-audio-toggle`, `data-audio`, `data-jump="tab-com"`, `data-jump="tab-thitkho"`), and stylesheet rule `after { box-sizing: border-box; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `MÂM CƠM THE FAMILY RICE TRAY`)**:
   - Landmark `<section class="hero">` presenting display lead `MÂM CƠM THE FAMILY RICE TRAY` and copy excerpt *"A LOVE LETTER TO A REGIONAL DISH VIỆT NAM · ĐÔNG NAM Á"* over `#5e0712` canvas and `#f7efe0` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Mâm Cơm The family rice tray`)**:
   - Landmark `<section class="section tray-section">` rendering section `Mâm Cơm The family rice tray` with copy *"A love letter to a regional dish Việt Nam · Đông Nam Á"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `html { -webkit-text-size-adjust: 100%; }`.
4. **Interactive Detail & Feature Matrix (<section.feast> — `Three thousand years on a circle`)**:
   - Landmark `<section class="feast">` framing `Three thousand years on a circle` and `Thịt Kho Trứng` (*"Việt Nam · Đông Nam Á"*) with `#3f040c` surface cards, `#ff0000` accents, and `img { max-width: 100%; height: auto; display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://the-family-rice-tray.vercel.app`)**:
   - Landmark `<footer class="footer">` anchoring `Mâm Cơm — the Vietnamese family ` footer links (`The Tray · The Legend · The Recipe · Nếp Nhà`), copy *"mâm cơm · /məm kəːm/ · “the tray of rice”"*, and `#a0582e` structural dividers.
