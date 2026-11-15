# UI & UX Architecture: plastic-ocean-com

## Overview & Design Identity
- **Target**: `plastic-ocean-com` (**Plastic Ocean**)
- **Production URL**: [http://plastic-ocean.com/](http://plastic-ocean.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#4f4f4f` accent)
- **Summary**: Plastic Ocean
- **Total Clean CSS Variables Extracted**: `14` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter Tight`
- **Body Font Stack**: `Host Grotesk Regular`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `20px`, `1.04vw`, `3.33vw`, `1.67vw`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `20px`, `1.04vw`, `3.33vw`, `1.67vw`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `20px`, `1.04vw`, `3.33vw`, `1.67vw`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `20px`, `1.04vw`, `3.33vw`, `1.67vw`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--pswp-bg)` in `:root` |
| **Primary Typography Ink** | `#222` | `var(--pswp-placeholder-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--pswp-icon-color)` in `:root` |
| **Interactive Accent / Highlight** | `#4f4f4f` | `var(--pswp-icon-color-secondary)` in `:root` |
| **Secondary / Muted Copy** | `#ffffff` | `body { background: white }` (`#ffffff`) |
| **Structural Hairline Border** | `#000000` | `.mosaic-wrap { color: #000000 }` |

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
| `--plastic-ocean-co-bg` | `#000` | Canvas Substrate (from `var(--pswp-bg)` in `:root`) |
| `--plastic-ocean-co-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.wf-displayswap-n4-inactive> — `plastic-ocean-com`)**:
   - Landmark `<header class="wf-displayswap-n4-inactive">` hosting `Plastic Ocean` navigation (`get in touch · Case · Nikolai Kudriavtsev · Natalia Pugacheva · Evgeny Kuzmin`), DOM attributes (`data-size="1920x1080"`, `data-origin-src="/thumb/2/evC8fvcePJXD..."`, `data-lenis-prevent="true"`, `data-url="https://t.me/nick_kudrya"`), and stylesheet rule `.div--u-iww1jyf2k { width: 78.13vw; height: 100%; transform: translate3D(0px, 0vh, 0px); }`.
2. **Hero Stage & Focal Lead (<section.section> — `Plastic Ocean`)**:
   - Landmark `<section class="section section--u-iqub3glf6">` presenting display lead `Plastic Ocean` and copy excerpt *"This website is a non-commercial demonstration project. We do not"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="section section--u-i8upocq6y">` rendering section `Featured Work & Interactive Showcase` with copy *"If you’re interested in this format of storytelling — get in touc"*, asset references (`tt_default_styles.css`, `design-i8z5xo3zc-1649318570_style...`, `shared-design-styles.css`, `animation-design-styles.css`), and grid rule `.text--u-ise53ezbe { opacity: 0; transform: translate3D(0px, 0px, 0px); }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="section section--u-ir9wd7wkv">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Plastic pollution is often communicated through overwhelming stat"*) with `#fff` surface cards, `#4f4f4f` accents, and `.image--u-it5s3ovyb { transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg) translate3D(0px, 0p... }`.
5. **Colophon & Global Directory Footer (<footer.lenis-smooth> — `http://plastic-ocean.com/`)**:
   - Landmark `<footer class="lenis-smooth">` anchoring `Plastic Ocean` footer links (`get in touch · Case · Nikolai Kudriavtsev · Natalia Pugacheva · Evgeny Kuzmin`), copy *"The vertical scroll acts as a timeline. As the user scrolls "*, and `#000000` structural dividers.
