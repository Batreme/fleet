---
title: "UI & UX Architecture: zenobasi-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: zenobasi-com

## Overview & Design Identity
- **Target**: `zenobasi-com` (**Zen Obasi — Art Director**)
- **Production URL**: [https://zenobasi.com](https://zenobasi.com)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1280×1656px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#0c0c0c`)
- **Summary**: Art director and visual strategist working across identity, campaign and editorial for brands worldwide.
- **Total Clean CSS Variables Extracted**: `13` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Google Sans Flex`
- **Body Font Stack**: `Google Sans Flex`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 24px`, `line-height: 30px`, `font-weight: 350`)
- **Section Heading (`H2`)**: observed font-size ladder: `24px`, `16px`, `11.2px`, `var(--text-large)`, `var(--text-small)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `,p` (`font-size: var(--text-small)`, `line-height: 1.35`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-small: 0.7rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0c0c0c` | `.background { background-color: #0c0c0c }` |
| **Interactive Accent / Highlight** | `#0c0c0c` | `<meta name="theme-color" content="#0c0c0c">` in `dom.html` |
| **Secondary / Muted Copy** | `#ffffff` | secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ffffff` | hairline divider derived from secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--base-100` | `#fff` | Color / Atmospheric Token |
| `--base-200` | `rgb(255 255 255/0.5)` | Color / Atmospheric Token |
| `--base-300` | `#000` | Color / Atmospheric Token |
| `--edge` | `clamp(2rem,3.5vw,3rem)` | Dimension / Scale Token |
| `--section-gap` | `18rem` | Layout / Spatial Grid Token |
| `--text-small` | `0.7rem` | Typography Ink Token |
| `--text-large` | `clamp(16px,3.5vw,24px)` | Typography Ink Token |
| `--side-reach` | `3.5em` | Dimension / Scale Token |
| `--font-sans` | `"Google Sans Flex"` | Typography / Scale Token |
| `--backdrop` | `0 0 0` | Design System Custom Token |
| `--digit-h` | `1.1em` | Dimension / Scale Token |
| `--fill-mobile` | `0.75` | Design System Custom Token |
| `--fill-desktop` | `0.45` | Design System Custom Token |
| `--zenobasi-com-bg` | `#000000` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--zenobasi-com-ink` | `#ffffff` | Primary Typography Ink (computed-derived) |
| `--zenobasi-com-surface` | `#0c0c0c` | Surface Substrate (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.lenis> — `zenobasi-com`)**:
   - Landmark `<nav class="lenis">` (`1440x111px`) hosting `Zen Obasi — Art Director` navigation (`Index Index · Work Work · About About · Inquire Inquire · Zen Obasi Zen Obasi`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/css/5f4..."`, `data-copy="lines"`, `data-copy="lines"`), and stylesheet rule `html { overflow-x:clip }`.
2. **Hero Stage & Focal Lead (<main.background> — `Zen Obasi, Art Director`)**:
   - Landmark `<main class="background">` presenting display lead `Zen Obasi, Art Director` and copy excerpt *"ART DIRECTION / VISUAL IDENTITY"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.container> — `ART DIRECTION / VISUAL IDENTITY`)**:
   - Landmark `<main class="container">` rendering section `ART DIRECTION / VISUAL IDENTITY` with copy *"Art Direction / Visual Identity"*, asset references (`2adbc45882a5a7c5.p.woff2`, `webpack-b827b2449ca92f38.js`, `4bd1b696-228d6cc6681fc189.js`, `826-cff36fe3db5d20f7.js`), and grid rule `body { font-family:var(--font-sans),sans-serif;background-color:var(--base-300)... }`.
4. **Interactive Detail & Feature Matrix (<main.menu-toggle> — `Art Direction / Visual Identity`)**:
   - Landmark `<main class="menu-toggle">` framing `Art Direction / Visual Identity` and `Accepting Briefs for S/S 2027` (*"Accepting Briefs for S/S 2027"*) with `#0c0c0c` surface cards, `#0c0c0c` accents, and `selection { background-color:var(--base-100);color:var(--base-300) }`.
5. **Colophon & Global Directory Footer (<footer.footer-pinned> — `https://zenobasi.com`)**:
   - Landmark `<footer class="footer-pinned footer-simple">` anchoring `Zen Obasi — Art Director` footer links (`Index Index · Work Work · About About · Inquire Inquire · Zen Obasi Zen Obasi`), copy *"Zen Obasi Zen Obasi"*, and `#ffffff` structural dividers.
