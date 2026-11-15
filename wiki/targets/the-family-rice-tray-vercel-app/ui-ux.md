# UI & UX Architecture: the-family-rice-tray-vercel-app

## Overview & Design Identity
- **Target**: `the-family-rice-tray-vercel-app` (**Mâm Cơm — the Vietnamese family rice tray**)
- **Production URL**: [https://the-family-rice-tray.vercel.app](https://the-family-rice-tray.vercel.app)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#3f040c` canvas, `#e3a94a` ink, `#8b0c1c` accent)
- **Summary**: A love letter to mâm cơm, the round tray of shared dishes at the centre of every Vietnamese home — laid out on the face of a Đông Sơn bro...
- **Total Clean CSS Variables Extracted**: `36` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Be Vietnam Pro`
- **Body Font Stack**: `Big Shoulders Display`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-display: "Big Shoulders Display", "Arial Narrow", system-ui, sans-serif`; rule `h1` (`font-size: var(--t-hero)`, `line-height: 0.82`, `letter-spacing: -0.015em`, `font-weight: 900`)
- **Section Heading (`H2`)**: CSS variables `--t-h2: clamp(2.4rem, 6vw, 4.6rem)`; rule `h2` (`font-size: var(--t-h2)`, `font-weight: 900`)
- **Body Copy**: CSS variables `--font-body: "Be Vietnam Pro", system-ui, -apple-system, "Segoe UI", sans-serif`, `--t-body: clamp(1rem, 0.55vw + 0.9rem, 1.16rem)`; rule `body` (`font-size: var(--t-body)`, `line-height: 1.72`, `font-weight: 300`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--t-body)`, `0.76rem`, `var(--t-lede)`, `0.62em`, `0.4em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#3f040c` | `var(--red-900)` in `:root` |
| **Primary Typography Ink** | `#5e0712` | `var(--red-800)` in `:root` |
| **Elevated Surface / Card Substrate** | `#7a0a18` | `var(--red-700)` in `:root` |
| **Interactive Accent / Highlight** | `#8b0c1c` | `var(--red-600)` in `:root` |
| **Secondary / Muted Copy** | `#a8121f` | `var(--red-500)` in `:root` |
| **Structural Hairline Border** | `#e3a94a` | `var(--gold-400)` in `:root` |
| **Variable Token (`--gold-300`)** | `#f0be6b` | `var(--gold-300)` in `:root` |
| **Variable Token (`--gold-200`)** | `#f7d9a0` | `var(--gold-200)` in `:root` |
| **Variable Token (`--jade`)** | `#2e6b58` | `var(--jade)` in `:root` |
| **Variable Token (`--jade-light`)** | `#7fb8a2` | `var(--jade-light)` in `:root` |
| **Variable Token (`--cream`)** | `#f7efe0` | `var(--cream)` in `:root` |
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
   - Landmark `<header class="masthead">` hosting `Mâm Cơm — the Vietnamese family rice` navigation (`The Tray · The Legend · The Recipe · Nếp Nhà`), DOM attributes (`data-audio-toggle`, `data-audio`, `data-jump="tab-com"`, `data-jump="tab-thitkho"`), and stylesheet rule `after { box-sizing: border-box; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Mâm Cơm The family rice tray`)**:
   - Landmark `<section class="hero">` presenting display lead `Mâm Cơm The family rice tray` and copy excerpt *"A love letter to a regional dish Việt Nam · Đông Nam Á"* over `#3f040c` canvas and `#e3a94a` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Three thousand years on a circle`)**:
   - Landmark `<section class="section tray-section">` rendering section `Three thousand years on a circle` with copy *"Việt Nam · Đông Nam Á"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `html { -webkit-text-size-adjust: 100%; }`.
4. **Interactive Detail & Feature Matrix (<section.feast> — `Cơm Trắng`)**:
   - Landmark `<section class="feast">` framing `Cơm Trắng` and `Thịt Kho Trứng` (*"mâm cơm · /məm kəːm/ · “the tray of rice”"*) with `#7a0a18` surface cards, `#8b0c1c` accents, and `img { max-width: 100%; height: auto; display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://the-family-rice-tray.vercel.app`)**:
   - Landmark `<footer class="footer">` anchoring `Mâm Cơm — the Vietnamese family ` footer links (`The Tray · The Legend · The Recipe · Nếp Nhà`), copy *"Vietnamese has no word for entrée . There is only cơm — rice"*, and `#e3a94a` structural dividers.
