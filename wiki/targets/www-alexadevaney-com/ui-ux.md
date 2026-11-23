---
title: "UI & UX Architecture: www-alexadevaney-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-alexadevaney-com

## Overview & Design Identity
- **Target**: `www-alexadevaney-com` (**North County San Diego Luxury Homes – Alexa Devaney**)
- **Production URL**: [https://www.alexadevaney.com/](https://www.alexadevaney.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f7f6f4` canvas, `#333333` ink, `#000080` accent)
- **Summary**: Alexa Devaney, Senior Realtor Associate with The Oppenheim Group, helps families buy and sell luxury homes from Encinitas and Carlsbad to...
- **Total Clean CSS Variables Extracted**: `17` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Montserrat`
- **Body Font Stack**: `Montserrat`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 84px`, `line-height: 89.04px`, `font-weight: 400`, `letter-spacing: 0.5px`); CSS variables `--display-font: "Montserrat",sans-serif`; rule `h1` (`font-size: clamp(38px,5.4vw,72px)`, `line-height: 1.02`, `letter-spacing: -1.4px`, `font-weight: 300`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 37.44px`, `line-height: 54.288px`, `font-weight: 400`); rule `h2` (`font-size: 30px`, `letter-spacing: 1px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--body-font: "Montserrat",sans-serif`; rule `p` (`font-size: 16px`, `line-height: 1.7`, `letter-spacing: 1px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f6f4` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#333333` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.navbar.scrolled { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#000080` | `.lp-btn--outline { color: navy }` (`#000080`) |
| **Secondary / Muted Copy** | `#b6b0a6` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#f8f7f5` | `.sidemenu__nav li { border-bottom: #f8f7f5 }` |
| **Variable Token (`--navy`)** | `#004f71` | `var(--navy)` in `:root` |
| **Variable Token (`--taupe`)** | `#88786a` | `var(--taupe)` in `:root` |
| **Variable Token (`--cream`)** | `#fbf9f7` | `var(--cream)` in `:root` |
| **Variable Token (`--cat`)** | `#7fb0c4` | `var(--cat)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--navy` | `#004F71` | Layout / Spatial Grid Token |
| `--navy-90` | `rgba(0,79,113,0.9)` | Layout / Spatial Grid Token |
| `--taupe` | `#88786A` | Color / Atmospheric Token |
| `--taupe-overlay` | `rgba(136,120,106,0.4)` | Color / Atmospheric Token |
| `--cream` | `#FBF9F7` | Color / Atmospheric Token |
| `--white` | `#FFFFFF` | Canvas / Surface Token |
| `--heading-font` | `"Montserrat",sans-serif` | Typography Ink Token |
| `--display-font` | `"Montserrat",sans-serif` | Typography / Scale Token |
| `--body-font` | `"Montserrat",sans-serif` | Typography / Scale Token |
| `--rail-gutter` | `max(25px,calc((100% - 1370px) / 2 + 25px))` | Layout / Spatial Grid Token |
| `--cat` | `#7fb0c4` | Color / Atmospheric Token |
| `--ag-top` | `96px` | Dimension / Scale Token |
| `--ag-h` | `min(calc(100vh - var(--ag-top) - 24px),780px)` | Dimension / Scale Token |
| `--decal` | `url(/brand/og-ring-decal.webp)` | Design System Custom Token |
| `--mix` | `0` | Design System Custom Token |
| `--hs-menu-max` | `340px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.navbar> — `www-alexadevaney-com`)**:
   - Landmark `<nav class="navbar">` (`1440x79px`) hosting `North County San Diego Luxury Homes ` navigation (`Buy · Sell · Old Encinitas · Leucadia · Cardiff-by-the-Sea`), DOM attributes (`data-intro="done"`, `data-precedence="next"`, `data-precedence="next"`, `data-nimg="fill"`), and stylesheet rule `.intro { display:none }`.
2. **Hero Stage & Focal Lead (<section.video-section> — `A Family-First Realtor for North C`)**:
   - Landmark `<section class="video-section hn-hero">` presenting display lead `A Family-First Realtor for North County` and copy excerpt *"Surf breaks, bluff-top streets, and a laid-back coastal village f"* over `#f7f6f4` canvas and `#333333` ink.
3. **Primary Showcase & Content Grid (<section.hn-statement> — `Surf breaks, bluff-top streets, an`)**:
   - Landmark `<section class="hn-statement">` rendering section `Surf breaks, bluff-top streets, and a laid-back ` with copy *"Communities North County San Diego View all communities → Encinit"*, asset references (`og-emblem.webp`, `og-wordmark-light.webp`, `og-wordmark-dark.webp`, `og-ring-decal.webp`), and grid rule `.intro__orb { scale:1.12;transition:scale .6s ease-in }`.
4. **Interactive Detail & Feature Matrix (<section.hn-stats> — `Communities North County San Diego`)**:
   - Landmark `<section class="hn-stats">` framing `Communities North County San Diego View all comm` and `North County San Diego` (*"North County San Diego"*) with `#ffffff` surface cards, `#000080` accents, and `.intro__content { position:relative;display:flex;flex-direction:column;align-items:center;... }`.
5. **Colophon & Global Directory Footer (<footer.intro__emblem> — `https://www.alexadevaney.com/`)**:
   - Landmark `<footer class="intro__emblem">` anchoring `North County San Diego Luxury Ho` footer links (`Buy · Sell · Old Encinitas · Leucadia · Cardiff-by-the-Sea`), copy *"Encinitas → Surf breaks, bluff-top streets, and a laid-back "*, and `#f8f7f5` structural dividers.
