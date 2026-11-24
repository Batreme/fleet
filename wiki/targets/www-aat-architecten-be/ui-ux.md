---
title: "UI & UX Architecture: www-aat-architecten-be"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-aat-architecten-be

## Overview & Design Identity
- **Target**: `www-aat-architecten-be` (**AAT Architecten**)
- **Production URL**: [https://www.aat-architecten.be/](https://www.aat-architecten.be/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1d1d1b` ink, `#185abc` accent)
- **Summary**: Architectenbureau uit Turnhout (Antwerpen), actief in een ruimer gebied. Architectuurprojecten voor openbare besturen, scholen en bedrijv...
- **Total Clean CSS Variables Extracted**: `148` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Suisse Intl`
- **Body Font Stack**: `Suisse Intl`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40px`, `line-height: 50px`, `font-weight: 400`); CSS variables `--h1-size: clamp(32px, 3vw + 1.5rem, 72px)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 31.52px`, `line-height: 39.4px`, `font-weight: 400`); CSS variables `--h2-size: clamp(28px, 2.2vw + 1.2rem, 48px)`; rule `h2` (`font-size: var(--h4-size)`, `font-weight: var(--font-we...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: var(--text-13)`, `line-height: 1`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--form-field-small-width: calc(25% - calc(var(--spacing) * 4))`, `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1d1d1b` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f9fafb` | `.aspect-ratio-box .no-image:before { background-color: #f9fafb }` |
| **Interactive Accent / Highlight** | `#185abc` | `.rc-2fa-submit-button-holder bu... { background-color: #185abc }` |
| **Secondary / Muted Copy** | `#ababab` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e9f3e3` | `20 { border-color: #e9f3e3 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--reverse-aspect-ratio` | `1` | Design System Custom Token |
| `--form-spacing-x` | `calc(var(--spacing) * 8)` | Layout / Spatial Grid Token |
| `--form-spacing-y` | `calc(var(--spacing) * 10)` | Layout / Spatial Grid Token |
| `--form-submit-spacing` | `calc(var(--spacing) * 10)` | Layout / Spatial Grid Token |
| `--form-field-small-width` | `calc(25% - calc(var(--spacing) * 4))` | Layout / Spatial Grid Token |
| `--rte-margin` | `calc(var(--spacing) * 6)` | Layout / Spatial Grid Token |
| `--rte-link-color` | `var(--color-black-500)` | Typography Ink Token |
| `--g-spacing` | `calc(var(--spacing) * 24)` | Layout / Spatial Grid Token |
| `--none` | `linear(0, 1)` | Design System Custom Token |
| `--h1-size` | `clamp(32px, 3vw + 1.5rem, 72px)` | Typography / Scale Token |
| `--h2-size` | `clamp(28px, 2.2vw + 1.2rem, 48px)` | Typography / Scale Token |
| `--h3-size` | `clamp(24px, 1.8vw + 1rem, 40px)` | Typography / Scale Token |
| `--h4-size` | `clamp(20px, 1.3vw + .8rem, 32px)` | Layout / Spatial Grid Token |
| `--h5-size` | `clamp(18px, .5vw + 1rem, 20px)` | Layout / Spatial Grid Token |
| `--h6-size` | `clamp(16px, .4vw + .9rem, 18px)` | Layout / Spatial Grid Token |
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-wrapper__row> — `www-aat-architecten-be`)**:
   - Landmark `<header class="site-wrapper__row site-wrapper__row--header">` (`1440x110px`) hosting `AAT Architecten` navigation (`Projecten · Over · Contact`), DOM attributes (`data-lenis-prevent`, `data-split="heading"`, `data-duration="1.6"`, `data-stagger="0.18"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.home-intro-block> — `Wij ontwerpen gebouwen die werken `)**:
   - Landmark `<section class="home-intro-block mb-g">` presenting display lead `Wij ontwerpen gebouwen die werken voor publieke r...` and copy excerpt *"Wij ontwerpen gebouwen die werken voor"* over `#ffffff` canvas and `#1d1d1b` ink.
3. **Primary Showcase & Content Grid (<section.block-featured-projects> — `Projecten`)**:
   - Landmark `<section class="block-featured-projects block-featured-projects--first">` rendering section `Projecten` with copy *"publieke ruimtes, scholen en bedrijven, en"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `.lenis.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.block-text-and-portrait> — `publieke ruimtes, scholen en bedri`)**:
   - Landmark `<section class="block-text-and-portrait row">` framing `publieke ruimtes, scholen en bedrijven, en` and `vertrekken daarbij steeds van de ruimte` (*"vertrekken daarbij steeds van de ruimte"*) with `#f9fafb` surface cards, `#185abc` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.mobile-nav__footer> — `https://www.aat-architecten.be/`)**:
   - Landmark `<footer class="mobile-nav__footer">` anchoring `AAT Architecten` footer links (`Projecten · Over · Contact`), copy *"Schooltje van de Hei"*, and `#e9f3e3` structural dividers.
