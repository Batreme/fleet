---
title: "UI & UX Architecture: withwise-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: withwise-com

## Overview & Design Identity
- **Target**: `withwise-com` (**Compliance-First Onboarding Software · Wise**)
- **Production URL**: [https://withwise.com/](https://withwise.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#4e1c4f` canvas, `#ffffff` ink, `#00c2ff` accent)
- **Summary**: Wise is built for self-employed workforces. We protect you from compliance risks, help you onboard users digitally, and pay them securely.
- **Total Clean CSS Variables Extracted**: `983` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Merriweather`
- **Body Font Stack**: `Figtree`
- **Monospace / Technical Font Stack**: `Consolas`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 60px`, `line-height: 84px`, `font-weight: 900`, `letter-spacing: -2px`); CSS variables `--gf-field-pwd-str-ind-display: inline-block`, `--gf-local-display: block`; rule `,.h1` (`font-size: 2.25rem`, `line-height: 1.4`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 42px`, `line-height: 58.8px`, `font-weight: 900`, `letter-spacing: -1px`); rule `,.h2` (`font-size: 1.8125rem`, `line-height: 1.4`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 300`); rule `p` (`font-size: var(--gf-ctrl-date-picker-hel...`, `line-height: var(--gf-ctrl-date-pi...`, `letter-spacing: var(--gf-ctrl-date-pi...`, `font-weight: var(--gf-ctrl...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 300`); CSS variables `--gf-label-space-primary: 8px`, `--gf-label-choice-field-space-primary: 12px`, `--gf-label-space-x-secondary: 12px`; rule `small` (`line-height: 0`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#4e1c4f` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#381334` | live computed `header` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#00c2ff` | `var(--gf-field-pg-prog-bar-bg-gradient-blues)` in `:root` |
| **Secondary / Muted Copy** | `#f2f3f5` | `var(--gf-color-secondary-darker)` in `:root` |
| **Structural Hairline Border** | `#dddddd` | `var(--border-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp--style--global--content-size` | `1170px` | Layout / Spatial Grid Token |
| `--wp--style--global--wide-size` | `1170px` | Layout / Spatial Grid Token |
| `--wp--style--block-gap` | `24px` | Layout / Spatial Grid Token |
| `--fa-family-brands` | `"Font Awesome 7 Brands"` | Brand / Palette Token |
| `--fa-font-brands` | `normal 400 1em/1 var(--fa-family-brands)` | Brand / Palette Token |
| `--fa-family-classic` | `"Font Awesome 7 Free"` | Typography / Scale Token |
| `--fa-font-regular` | `normal 400 1em/1 var(--fa-family-classic)` | Typography / Scale Token |
| `--fa-style-family-classic` | `var(--fa-family-classic)` | Typography / Scale Token |
| `--fa-font-solid` | `normal 900 1em/1 var(--fa-family-classic)` | Typography / Scale Token |
| `--input-fz` | `1rem` | Dimension / Scale Token |
| `--input-lh` | `1.5` | Design System Custom Token |
| `--input-pt` | `0.6875rem` | Dimension / Scale Token |
| `--input-pb` | `0.6875rem` | Dimension / Scale Token |
| `--input-pl` | `1rem` | Dimension / Scale Token |
| `--input-pr` | `1rem` | Dimension / Scale Token |
| `--input-bd` | `1px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `withwise-com`)**:
   - Landmark `<header class="header">` (`1440x92px`) hosting `Compliance-First Onboarding Software` navigation (`Request a callback · Platform · See article · Industries · Why Wise`), DOM attributes (`data-scroll-dir-x="0"`, `data-scroll-dir-y="0"`, `data-loader="hs-scriptloader"`, `data-hsjs-portal="145539501"`), and stylesheet rule `.tablepress>.row-hover>tr { content-visibility:auto }`.
2. **Hero Stage & Focal Lead (<section.flx-section> — `Stay compliant. Pay on time. Grow `)**:
   - Landmark `<section class="flx-section flx-masthead-1">` presenting display lead `Stay compliant. Pay on time. Grow without the risk.` and copy excerpt *"Now live: October 2026 Right to work rules"* over `#4e1c4f` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.bg-type-dark> — `Compliance-First Onboarding softwa`)**:
   - Landmark `<section class="flx-section bg-type-dark">` rendering section `Compliance-First Onboarding software` with copy *"Onboard your workforce in minutes, pay them accurately, and keep "*, asset references (`web-interactives-embed.js`, `banner.js`, `collectedforms.js`, `145539501.js`), and grid rule `.tablepress img { border:none;margin:0;max-width:none;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.flx-ft-grid> — `Stay compliant . Pay on time . Gro`)**:
   - Landmark `<section class="flx-section bg-type-dark">` framing `Stay compliant . Pay on time . Grow without the r...` and `Why It Matters` (*"We look after your workforce too."*) with `#381334` surface cards, `#00c2ff` accents, and `.tablepress-table-description { clear:both;display:block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://withwise.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Compliance-First Onboarding Soft` footer links (`Request a callback · Platform · See article · Industries · Why Wise`), copy *"Payments powered by"*, and `#dddddd` structural dividers.
