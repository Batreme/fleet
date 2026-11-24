---
title: "UI & UX Architecture: boomballtour-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: boomballtour-com

## Overview & Design Identity
- **Target**: `boomballtour-com` (**Boom Ball Baseball · The Ultimate Family Sports Experience**)
- **Production URL**: [https://boomballtour.com/](https://boomballtour.com/)
- **Final Redirected URL**: [https://boomball.com/](https://boomball.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f4eddf` canvas, `#1f335e` ink, `#0000ff` accent)
- **Summary**: Discover Boom Ball — the interactive, family-friendly baseball show packed with energy, music, and nonstop fun for all ages.
- **Total Clean CSS Variables Extracted**: `586` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Groundout`
- **Body Font Stack**: `Inter-400`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 96px`, `line-height: 76.8px`, `font-weight: 500`); CSS variables `--bb-font-display: "Groundout", Georgia, serif`, `--bbc-font-display: var(--bb-font-display, Georgia, serif)`; rule `,h1` (`font-size: calc(1.375rem + 1.5vw)`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 239.04px`, `line-height: 191.232px`, `font-weight: 400`, `letter-spacing: -3px`); rule `,h2` (`font-size: calc(1.325rem + .9vw)`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 23.4px`, `font-weight: 400`); CSS variables `--bb-font-body: "Inter-400", Arial, Helvetica, sans-serif`, `--bb-font-body-medium: "Inter-500", Arial, Helvetica, sans-serif`, `--bs-body-bg-rgb: 255,255,255`; rule `p` (`font-size: 16px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 23.4px`, `font-weight: 400`); CSS variables `--bb-font-mono: "Roboto-600", "Courier New", monospace`, `--bbc-font-label: var(--bb-font-heading, Arial, Helvetica, sans-serif)`, `--wpforms-field-size-sublabel-spacing: 5px`; rule `,small` (`font-size: .875em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4eddf` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1f335e` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3ebdc` | `var(--bb-color-paper)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ff` | `.bb-consent-btn--primary:hover { background-color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#5ba238` | `var(--fkcart-saving-text-price-color)` in `:root` |
| **Structural Hairline Border** | `#b8b3a8` | `var(--bb-color-divider)` in `:root` |
| **Variable Token (`--bb-color-pink`)** | `#ff1e96` | `var(--bb-color-pink)` in `:root` |
| **Variable Token (`--bb-color-gold`)** | `#c2a155` | `var(--bb-color-gold)` in `:root` |
| **Variable Token (`--bb-color-ink`)** | `#43433d` | `var(--bb-color-ink)` in `:root` |
| **Variable Token (`--bb-color-white`)** | `#ffffff` | `var(--bb-color-white)` in `:root` |
| **Variable Token (`--bb-color-slate`)** | `#79859f` | `var(--bb-color-slate)` in `:root` |
| **Variable Token (`--bb-color-inactive`)** | `#f894c5` | `var(--bb-color-inactive)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bb-color-pink` | `#ff1e96` | Typography Ink Token |
| `--bb-color-blue` | `#1f335e` | Brand / Palette Token |
| `--bb-color-gold` | `#c2a155` | Brand / Palette Token |
| `--bb-color-ink` | `#43433d` | Typography Ink Token |
| `--bb-color-paper` | `#f3ebdc` | Canvas / Surface Token |
| `--bb-color-white` | `#ffffff` | Canvas / Surface Token |
| `--bb-color-slate` | `#79859f` | Brand / Palette Token |
| `--bb-color-frame` | `rgb(255 255 255 / 35%)` | Brand / Palette Token |
| `--bb-color-divider` | `#B8B3A8` | Brand / Palette Token |
| `--bb-color-inactive` | `#f894c5` | Brand / Palette Token |
| `--bb-font-body` | `"Inter-400", Arial, Helvetica, sans-serif` | Typography / Scale Token |
| `--bb-font-body-medium` | `"Inter-500", Arial, Helvetica, sans-serif` | Typography / Scale Token |
| `--bb-font-heading` | `"Hamburg-700", Arial, Helvetica, sans-serif` | Typography Ink Token |
| `--bb-font-display` | `"Groundout", Georgia, serif` | Typography / Scale Token |
| `--bb-font-script` | `"Brooklyn-700", Georgia, serif` | Typography / Scale Token |
| `--bb-font-mono` | `"Roboto-600", "Courier New", monospace` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.footer-nav> — `boomballtour-com`)**:
   - Landmark `<nav class="footer-nav">` (`273x144px`) hosting `Boom Ball Baseball · The Ultimate Fa` navigation (`What’s Boom Ball · Teams · About · Tickets · Merch`), DOM attributes (`data-id="D8BJ15BC77UDFA3HME2G"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `merce-page .woocommerce-message .... { float:right }`.
2. **Hero Stage & Focal Lead (<section.hero-banner> — `Bigger Than Baseball`)**:
   - Landmark `<section class="hero-banner">` presenting display lead `Bigger Than Baseball` and copy excerpt *"See The Great Bambino take the field and re-create his legendary "* over `#f4eddf` canvas and `#1f335e` ink.
3. **Primary Showcase & Content Grid (<section.bb-feature> — `See The Great Bambino take the fie`)**:
   - Landmark `<section class="bb-feature is-enhanced">` rendering section `See The Great Bambino take the field and re-crea` with copy *"EVERY INNING BRINGS"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `.woocommerce-page .col2-set { width:100% }`.
4. **Interactive Detail & Feature Matrix (<article.bb-feature__item> — `EVERY INNING BRINGS`)**:
   - Landmark `<article class="bb-feature__item reveal-slide">` framing `EVERY INNING BRINGS` and `Boom Ball is baseball reimagined for families—a ` (*"Boom Ball is baseball reimagined for families—a fast-paced, high-"*) with `#f3ebdc` surface cards, `#0000ff` accents, and `.woocommerce-page .col2-set::before { content:" ";display:table }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://boomballtour.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Boom Ball Baseball · The Ultimat` footer links (`What’s Boom Ball · Teams · About · Tickets · Merch`), copy *"Babe Ruth Hologram"*, and `#b8b3a8` structural dividers.
