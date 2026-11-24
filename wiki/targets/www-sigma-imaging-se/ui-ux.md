---
title: "UI & UX Architecture: www-sigma-imaging-se"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-sigma-imaging-se

## Overview & Design Identity
- **Target**: `www-sigma-imaging-se` (**SIGMA Imaging Nordics & Baltics · Lenses, Cameras & Cine-lenses - Sigma**)
- **Production URL**: [https://www.sigma-imaging.se/](https://www.sigma-imaging.se/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fefefd` canvas, `#333333` ink, `#0077cb` accent)
- **Summary**: Official SIGMA subsidiary for the Nordics and Baltics. Lenses and cameras Made in Aizu, Japan, with 5-year warranty, local support and fi...
- **Total Clean CSS Variables Extracted**: `177` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Sigma Serif Headline`
- **Body Font Stack**: `Sigma Serif`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 88px`, `line-height: 83.6px`, `font-weight: 400`, `letter-spacing: -1.32px`); rule `h1` (`font-size: 2.25rem`, `line-height: 2.5rem`, `font-weight: 300`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: 0.08px`); rule `h2` (`font-size: 2.25rem`, `line-height: 2.5rem`, `font-weight: 300`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: 0.08px`); CSS variables `--ps-font-body: "Sigma Serif", serif`; rule `p` (`font-size: .8125rem`, `line-height: 125%`, `letter-spacing: .02em`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: 0.08px`); CSS variables `--amlabel-margin-between: 7px`, `--gap-amlabel-margin: var(--amlabel-margin-between)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fefefd` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#333333` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--amscroll-background-color)` in `:root` |
| **Interactive Accent / Highlight** | `#0077cb` | `.mollie-buttons .button:hover { background-color: #0077cb }` |
| **Secondary / Muted Copy** | `#9c9c9c` | `var(--adp-color-secondary)` in `:root` |
| **Structural Hairline Border** | `#cccfd6` | `var(--amscroll-border-color)` in `:root` |
| **Variable Token (`--amscroll--text--color`)** | `#252525` | `var(--amscroll--text--color)` in `:root` |
| **Variable Token (`--amcart-product-name`)** | `#000000` | `var(--amcart-product-name)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--amscroll-module--path` | `"../Amasty_Scroll"` | Design System Custom Token |
| `--amscroll--transition-duration` | `.2s` | Motion / Easing Token |
| `--amscroll--hover-filter` | `brightness(.8)` | Design System Custom Token |
| `--amscroll-loader--size` | `25px` | Layout / Spatial Grid Token |
| `--amscroll--text--color` | `#252525` | Typography Ink Token |
| `--amscroll-border-color` | `#cccfd6` | Brand / Palette Token |
| `--amscroll-background-color` | `#fff` | Canvas / Surface Token |
| `--amscroll--indent` | `10px` | Dimension / Scale Token |
| `--amscroll--indent--m` | `@amscroll--indent + @amscroll--indent/2` | Design System Custom Token |
| `--amscroll--indent--l` | `@amscroll--indent * 2` | Design System Custom Token |
| `--amscroll--indent--xl` | `@amscroll--indent--l + @amscroll--indent/2` | Design System Custom Token |
| `--amcart-background` | `#FFFFFF` | Canvas / Surface Token |
| `--amcart-product-name` | `#000000` | Color / Atmospheric Token |
| `--amcart-dialog-text` | `#000000` | Typography Ink Token |
| `--amcart-btn-text` | `#000000` | Typography Ink Token |
| `--amcart-continue-btn` | `#000000` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.ammenu-header-container> — `www-sigma-imaging-se`)**:
   - Landmark `<header class="ammenu-header-container page-header">` (`1425x0px`) hosting `SIGMA Imaging Nordics & Baltics · Le` navigation (`Products · Made in Aizu · Inspiration · Support · News`), DOM attributes (`data-src="//www.googletagmanage..."`, `data-cfasync="false"`, `data-dialog-ref-name="am-cookie-bar"`, `data-dispatch-action="cookiebar-action-allow"`), and stylesheet rule `air-datepicker-cell.-day-.-other-... { color:var(--adp-color-other-month) }`.
2. **Hero Stage & Focal Lead (<section.message> — `TREVOR KEY`)**:
   - Landmark `<section class="message global">` presenting display lead `TREVOR KEY` and copy excerpt *"BLACK WEEK & 65 YEARS CELEBRATION - INSTANTLY SAVE ON SELECTED PR"* over `#fefefd` canvas and `#333333` ink.
3. **Primary Showcase & Content Grid (<section.cms-index-index> — `SMALL, POWERFUL,`)**:
   - Landmark `<section class="cms-index-index">` rendering section `SMALL, POWERFUL,` with copy *"The Sigma FP2 is a camera fully designed around human creativity."*, asset references (`recaptcha__en.js`, `gtm.js`, `styles.css`, `eu-guarantee.css`), and grid rule `tepicker-cell.-day-.-other-month-... { color:var(--adp-color-other-month-hover) }`.
4. **Interactive Detail & Feature Matrix (<section.page-layout-1column> — `ADAPTABLE`)**:
   - Landmark `<section class="page-layout-1column">` framing `ADAPTABLE` and `NEW PRODUCTS` (*"Even in the digital age, taking a photograph is a deeply physical"*) with `#ffffff` surface cards, `#0077cb` accents, and `.air-datepicker-cell.-focus- { background:var(--adp-cell-background-color-hover) }`.
5. **Colophon & Global Directory Footer (<footer.page-footer> — `https://www.sigma-imaging.se/`)**:
   - Landmark `<footer class="page-footer">` anchoring `SIGMA Imaging Nordics & Baltics ` footer links (`Products · Made in Aizu · Inspiration · Support · News`), copy *"CONTEMPORARY 50 mm F1.4 CL DG"*, and `#cccfd6` structural dividers.
