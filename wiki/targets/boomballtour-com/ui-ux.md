# UI & UX Architecture: boomballtour-com

## Overview & Design Identity
- **Target**: `boomballtour-com` (**Boom Ball Baseball · The Ultimate Family Sports Experience**)
- **Production URL**: [https://boomballtour.com/](https://boomballtour.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ccc` canvas, `#6610f2` ink, `#6610f2` accent)
- **Summary**: Discover Boom Ball — the interactive, family-friendly baseball show packed with energy, music, and nonstop fun for all ages.
- **Total Clean CSS Variables Extracted**: `585` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Brooklyn-700`
- **Body Font Stack**: `Hamburg-700`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--bbc-font-display: var(--bb-font-display, Georgia, serif)`, `--bb-font-display: "Groundout", Georgia, serif`; rule `,h1` (`font-size: calc(1.375rem + 1.5vw)`)
- **Section Heading (`H2`)**: rule `,h2` (`font-size: calc(1.325rem + .9vw)`)
- **Body Copy**: CSS variables `--bbc-font-body: var(--bb-font-body, Arial, Helvetica, sans-serif)`, `--bs-body-color-rgb: 33,37,41`, `--bs-body-bg-rgb: 255,255,255`; rule `p` (`font-size: 16px!important`)
- **Metadata & Labels**: CSS variables `--bbc-font-label: var(--bb-font-heading, Arial, Helvetica, sans-serif)`, `--bb-font-mono: "Roboto-600", "Courier New", monospace`, `--wpforms-label-color: rgba( 0, 0, 0, 0.85 )`; rule `,small` (`font-size: .875em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ccc` | `var(--iti-border-color)` in `:root` |
| **Primary Typography Ink** | `#555` | `var(--iti-icon-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0d6efd` | `var(--bs-blue)` in `:root` |
| **Interactive Accent / Highlight** | `#6610f2` | `var(--bs-indigo)` in `:root` |
| **Secondary / Muted Copy** | `#6f42c1` | `var(--bs-purple)` in `:root` |
| **Structural Hairline Border** | `#d63384` | `var(--bs-pink)` in `:root` |
| **Variable Token (`--bbc-blue`)** | `#1f335e` | `var(--bbc-blue)` in `:root` |
| **Variable Token (`--bbc-pink`)** | `#ff1e96` | `var(--bbc-pink)` in `:root` |
| **Variable Token (`--bbc-gold`)** | `#c2a155` | `var(--bbc-gold)` in `:root` |
| **Variable Token (`--bbc-paper`)** | `#f3ebdc` | `var(--bbc-paper)` in `:root` |
| **Variable Token (`--bbc-ink`)** | `#43433d` | `var(--bbc-ink)` in `:root` |
| **Variable Token (`--bbc-white`)** | `#fff` | `var(--bbc-white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--fa-family-brands` | `"Font Awesome 7 Brands"` | Brand / Palette Token |
| `--fa-font-brands` | `normal 400 1em/1 var(--fa-family-brands)` | Brand / Palette Token |
| `--fa-family` | `var(--fa-family-brands)` | Typography / Scale Token |
| `--fa-style` | `400` | Design System Custom Token |
| `--bbc-blue` | `var(--bb-color-blue, #1f335e)` | Color / Atmospheric Token |
| `--bbc-pink` | `var(--bb-color-pink, #ff1e96)` | Typography Ink Token |
| `--bbc-gold` | `var(--bb-color-gold, #c2a155)` | Color / Atmospheric Token |
| `--bbc-paper` | `var(--bb-color-paper, #f3ebdc)` | Canvas / Surface Token |
| `--bbc-ink` | `var(--bb-color-ink, #43433d)` | Typography Ink Token |
| `--bbc-white` | `var(--bb-color-white, #fff)` | Canvas / Surface Token |
| `--bbc-radius` | `var(--bb-radius-media, 10px)` | Elevation / Border Token |
| `--bbc-ease` | `var(--bb-motion-ease, cubic-bezier(0.22, 1, 0.36, 1))` | Motion / Easing Token |
| `--bbc-duration` | `var(--bb-motion-duration, 0.42s)` | Motion / Easing Token |
| `--bbc-font-body` | `var(--bb-font-body, Arial, Helvetica, sans-serif)` | Typography / Scale Token |
| `--bbc-font-strong` | `"Inter-600", var(--bbc-font-body)` | Typography / Scale Token |
| `--bbc-font-label` | `var(--bb-font-heading, Arial, Helvetica, sans-serif)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.footer-nav> — `boomballtour-com`)**:
   - Landmark `<nav class="footer-nav">` hosting `Boom Ball Baseball · The Ultimate Fa` navigation (`What’s Boom Ball · Teams · About · Tickets · Merch`), DOM attributes (`data-id="D8BJ15BC77UDFA3HME2G"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `root { --fa-family-brands:"Font Awesome 7 Brands";--fa-font-brands:normal 400 1... }`.
2. **Hero Stage & Focal Lead (<section.hero-banner> — `Bigger Than Baseball`)**:
   - Landmark `<section class="hero-banner">` presenting display lead `Bigger Than Baseball` and copy excerpt *"EVERY INNING BRINGS"* over `#ccc` canvas and `#6610f2` ink.
3. **Primary Showcase & Content Grid (<section.bb-feature> — `EVERY INNING BRINGS the WHOLE FAMI`)**:
   - Landmark `<section class="bb-feature is-enhanced">` rendering section `EVERY INNING BRINGS the WHOLE FAMILY SOMETHING NEW` with copy *"Boom Ball is baseball reimagined for families—a fast-paced, high-"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `.fab { --fa-family:var(--fa-family-brands);--fa-style:400 }`.
4. **Interactive Detail & Feature Matrix (<article.bb-feature__item> — `Babe Ruth Hologram`)**:
   - Landmark `<article class="bb-feature__item reveal-slide">` framing `Babe Ruth Hologram` and `Flips & Trick Plays` (*"Babe Ruth Hologram"*) with `#0d6efd` surface cards, `#6610f2` accents, and `.fa-firefox-browser { --fa:"\e007" }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://boomballtour.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Boom Ball Baseball · The Ultimat` footer links (`What’s Boom Ball · Teams · About · Tickets · Merch`), copy *"See The Great Bambino take the field and re-create his legen"*, and `#d63384` structural dividers.
