---
title: "UI & UX Architecture: plastic-ocean-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: plastic-ocean-com

## Overview & Design Identity
- **Target**: `plastic-ocean-com` (**Plastic Ocean**)
- **Production URL**: [http://plastic-ocean.com/](http://plastic-ocean.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0d70ff` accent)
- **Summary**: Plastic Ocean
- **Total Clean CSS Variables Extracted**: `14` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Host Grotesk Regular`
- **Body Font Stack**: `Inter Tight`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: observed font-size ladder: `16px`, `14px`, `22px`, `20px`, `10px`
- **Section Heading (`H2`)**: observed font-size ladder: `16px`, `14px`, `22px`, `20px`, `10px`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#eeeeee` | `.form .tt-form__captcha .form__... { background-color: #eeeeee }` |
| **Interactive Accent / Highlight** | `#0d70ff` | `.tt-rich-link { color: #0d70ff }` |
| **Secondary / Muted Copy** | `#4f4f4f` | `var(--pswp-icon-color-secondary)` in `:root` |
| **Structural Hairline Border** | `#4f4f4f` | `var(--pswp-icon-stroke-color)` in `:root` |
| **Variable Token (`--pswp-placeholder-bg`)** | `#222222` | `var(--pswp-placeholder-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--default-cell-min-width` | `35px` | Layout / Spatial Grid Token |
| `--pswp-bg` | `#000` | Canvas / Surface Token |
| `--pswp-placeholder-bg` | `#222` | Canvas / Surface Token |
| `--pswp-root-z-index` | `100000` | Elevation / Border Token |
| `--pswp-preloader-color` | `rgba(79, 79, 79, 0.4)` | Brand / Palette Token |
| `--pswp-preloader-color-secondary` | `rgba(255, 255, 255, 0.9)` | Brand / Palette Token |
| `--pswp-icon-color` | `#fff` | Brand / Palette Token |
| `--pswp-icon-color-secondary` | `#4f4f4f` | Brand / Palette Token |
| `--pswp-icon-stroke-color` | `#4f4f4f` | Brand / Palette Token |
| `--pswp-icon-stroke-width` | `2px` | Layout / Spatial Grid Token |
| `--pswp-error-text-color` | `var(--pswp-icon-color)` | Typography Ink Token |
| `--custom-fade` | `1` | Design System Custom Token |
| `--webp-bottle-opacity` | `0` | Design System Custom Token |
| `--white-bg-opacity` | `1` | Canvas / Surface Token |
| `--plastic-ocean-co-bg` | `#ffffff` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--plastic-ocean-co-ink` | `#000000` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.wf-displayswap-n4-inactive> — `plastic-ocean-com`)**:
   - Landmark `<header class="wf-displayswap-n4-inactive">` (`1440px`) hosting `Plastic Ocean` navigation (`get in touch · Case · Nikolai Kudriavtsev · Natalia Pugacheva · Evgeny Kuzmin`), DOM attributes (`data-size="1920x1080"`, `data-origin-src="/thumb/2/evC8fvcePJXD..."`, `data-lenis-prevent="true"`, `data-url="https://t.me/nick_kudrya"`), and stylesheet rule `body { overflow-anchor:none;overflow-wrap:break-word;background:fff;margin:0;fo... }`.
2. **Hero Stage & Focal Lead (<section.section> — `Plastic Ocean`)**:
   - Landmark `<section class="section section--u-iqub3glf6">` presenting display lead `Plastic Ocean` and copy excerpt *"This website is a non-commercial demonstration project. We do not"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.section--u-i8upocq6y> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="section section--u-i8upocq6y">` rendering section `Featured Work & Interactive Showcase` with copy *"If you’re interested in this format of storytelling — get in touc"*, asset references (`tt_default_styles.css`, `design-i8z5xo3zc-1649318570_style...`, `shared-design-styles.css`, `animation-design-styles.css`), and grid rule `a:hover { text-decoration:none }`.
4. **Interactive Detail & Feature Matrix (<section.section--u-ir9wd7wkv> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="section section--u-ir9wd7wkv">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Plastic pollution is often communicated through overwhelming stat"*) with `#eeeeee` surface cards, `#0d70ff` accents, and `.text-block-wrap-div { flex-grow:1;max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.lenis-smooth> — `http://plastic-ocean.com/`)**:
   - Landmark `<footer class="lenis-smooth">` anchoring `Plastic Ocean` footer links (`get in touch · Case · Nikolai Kudriavtsev · Natalia Pugacheva · Evgeny Kuzmin`), copy *"The vertical scroll acts as a timeline. As the user scrolls "*, and `#4f4f4f` structural dividers.
