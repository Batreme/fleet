---
title: "UI & UX Architecture: www-plugandplaydesign-co-uk"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-plugandplaydesign-co-uk

## Overview & Design Identity
- **Target**: `www-plugandplaydesign-co-uk` (**Web Design Agency London & Guildford · Plug & Play**)
- **Production URL**: [https://www.plugandplaydesign.co.uk/](https://www.plugandplaydesign.co.uk/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fafafa` canvas, `#080808` ink, `#808080` accent)
- **Summary**: Award-winning web design agency in London and Guildford. High-performance websites and digital retainers that drive measurable growth.
- **Total Clean CSS Variables Extracted**: `380` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 14px`, `line-height: 19.6px`, `font-weight: 400`, `letter-spacing: -0.28px`); rule `h1` (`font-size: var(--text-body-sm)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 32px`, `line-height: 38.4px`, `font-weight: 400`, `letter-spacing: -0.64px`); rule `h2` (`font-size: var(--text-body-sm)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-body-sm: .875rem`, `--text-body-sm--line-height: 1.4`, `--text-body-sm--letter-spacing: -.02em`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: "Geist Mono",ui-monospace,"SF Mono",Menlo,monospace`, `--default-mono-font-family: var(--font-mono)`, `--text-caption: .75rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fafafa` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#080808` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.bg-white { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#808080` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#808080` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#808080` | hairline divider derived from live computed `p` `color` (`computed_styles.json`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--page-margin` | `1rem` | Layout / Spatial Grid Token |
| `--content-width` | `calc(100vw - 2rem)` | Layout / Spatial Grid Token |
| `--spacing-scrolling-copy` | `calc((var(--scrolling-items-width) - 2.5rem) * 6 / 10)` | Typography Ink Token |
| `--spacing-scrolling-media` | `calc((var(--scrolling-items-width) - 2.5rem) * 4 / 10)` | Layout / Spatial Grid Token |
| `--spacing-scrolling-media-adjacent` | `calc((var(--scrolling-items-width) - 2.5rem) * 4.5 / 10)` | Layout / Spatial Grid Token |
| `--spacing-scrolling-expanded` | `calc((var(--scrolling-items-width) - 2.5rem) * 5.5 / 10)` | Layout / Spatial Grid Token |
| `--background` | `var(--color-grey-50)` | Canvas / Surface Token |
| `--background-secondary` | `var(--color-grey-100)` | Canvas / Surface Token |
| `--background-tertiary` | `var(--color-grey-200)` | Canvas / Surface Token |
| `--background-raised` | `var(--color-white)` | Canvas / Surface Token |
| `--background-glass` | `#fafafa01` | Canvas / Surface Token |
| `--foreground` | `var(--color-grey-950)` | Typography Ink Token |
| `--foreground-secondary` | `var(--color-grey-700)` | Typography Ink Token |
| `--foreground-tertiary` | `var(--color-grey-500)` | Typography Ink Token |
| `--foreground-inactive` | `var(--color-grey-400)` | Typography Ink Token |
| `--foreground-muted` | `var(--color-grey-600)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `www-plugandplaydesign-co-uk`)**:
   - Landmark `<header class="inset-x-0 z-40">` (`1440x60px`) hosting `Web Design Agency London & Guildford` navigation (`Web Design · Branding · Digital Marketing · UX / UI Design · eCommerce`), DOM attributes (`data-hero-enter`, `data-precedence="next"`, `data-precedence="next"`, `data-domain="plugandplaydesign.co.uk"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.px-page> — `Web Design Agency in London and Su`)**:
   - Landmark `<section class="px-page pt-section">` presenting display lead `Web Design Agency in London and Surrey` and copy excerpt *"Plug and Play is a creative web design agency based in Guildford,"* over `#fafafa` canvas and `#080808` ink.
3. **Primary Showcase & Content Grid (<section.bg-background> — `Web Design Agency`)**:
   - Landmark `<section class="bg-background px-page">` rendering section `Web Design Agency` with copy *"Websites that drive results,"*, asset references (`ca4cfa437ae45d18.css`, `dd5d352a082118c1.css`, `webpack-43624c9fe997cbf4.js`, `cf303062-0b72e54636065547.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.w-screen> — `Websites that drive results, digit`)**:
   - Landmark `<section class="w-screen">` framing `Websites that drive results, digital retainers th...` and `Critical thinking. Creativity. Innovation.` (*"digital retainers that deliver growth."*) with `#ffffff` surface cards, `#808080` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.bg-background> — `https://www.plugandplaydesign.co.uk/`)**:
   - Landmark `<footer class="bg-background px-page">` anchoring `Web Design Agency London & Guild` footer links (`Web Design · Branding · Digital Marketing · UX / UI Design · eCommerce`), copy *"Trusted by ambitious organisations across every major sector"*, and `#808080` structural dividers.
