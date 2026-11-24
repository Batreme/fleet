---
title: "UI & UX Architecture: 1stdecember-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: 1stdecember-com

## Overview & Design Identity
- **Target**: `1stdecember-com` (**First December Films · Ad Film Production House in India**)
- **Production URL**: [https://1stdecember.com](https://1stdecember.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#efece7` canvas, `#20201e` ink, `#ffff00` accent)
- **Summary**: Mumbai advertising film production house with 150+ international awards. TVCs, brand films and digital campaigns for brands across India...
- **Total Clean CSS Variables Extracted**: `600` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Tartuffo Trial Regular`
- **Body Font Stack**: `Pp neue montreal Medium`
- **Monospace / Technical Font Stack**: `DM Mono Medium`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 120px`, `line-height: 120px`, `font-weight: 400`, `letter-spacing: -2.4px`); CSS variables `--_typography---h1--h1-font-size: 7.5rem`, `--_typography---h1--h1-line-height: var(--font-height--tiny)`, `--_typography---h1--h1-font-weight: var(--font-weight--normal)`; rule `h1` (`font-size: var(--text-base)`, `line-height: var(--tw-leading,var(...`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 299.52px`, `line-height: 254.592px`, `font-weight: 400`, `letter-spacing: -5.9904px`); CSS variables `--_typography---h2--h2-font-size: 5rem`, `--_typography---h2--h2-line-height: var(--font-height--tiny)`, `--_typography---h2--h2-font-weight: var(--font-weight--normal)`; rule `h2` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-family--body: "Pp neue montreal Medium",Arial,sans-serif`, `--_typography---body--body-font-size: 1rem`, `--_typography---body--body-line-height: var(--font-height--xlarge)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_typography---body--body-letter-spacing: var(--letter-spacing--default)`, `--_typography---h1--h1-letter-spacing: var(--letter-spacing--tighter)`, `--_typography---h2--h2-letter-spacing: var(--letter-spacing--tighter)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#efece7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#20201e` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e5e7eb` | `var(--cal-bg-emphasis)` in `:root` |
| **Interactive Accent / Highlight** | `#ffff00` | `.cta_blog_post { background-color: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#6b7280` | `var(--cal-text-subtle)` in `:root` |
| **Structural Hairline Border** | `#9ca3b0` | `var(--cal-border-emphasis)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--brand--white-light` | `#efece7` | Canvas / Surface Token |
| `--font-family--body` | `"Pp neue montreal Medium",Arial,sans-serif` | Typography / Scale Token |
| `--_theme---text--primary` | `var(--brand--black-dark)` | Typography Ink Token |
| `--_typography---body--body-font-size` | `1rem` | Typography / Scale Token |
| `--_typography---body--body-line-height` | `var(--font-height--xlarge)` | Typography / Scale Token |
| `--_typography---body--body-font-weight` | `var(--font-weight--normal)` | Typography / Scale Token |
| `--_typography---body--body-letter-spacing` | `var(--letter-spacing--default)` | Typography / Scale Token |
| `--_layout---spacing--none` | `0rem` | Layout / Spatial Grid Token |
| `--font-family--heading` | `"Tartuffo Trial Regular",Arial,sans-serif` | Typography Ink Token |
| `--_typography---h1--h1-font-size` | `7.5rem` | Typography / Scale Token |
| `--_typography---h1--h1-line-height` | `var(--font-height--tiny)` | Typography / Scale Token |
| `--_typography---h1--h1-font-weight` | `var(--font-weight--normal)` | Typography / Scale Token |
| `--_typography---h1--h1-letter-spacing` | `var(--letter-spacing--tighter)` | Typography / Scale Token |
| `--_typography---h2--h2-font-size` | `5rem` | Typography / Scale Token |
| `--_typography---h2--h2-line-height` | `var(--font-height--tiny)` | Typography / Scale Token |
| `--_typography---h2--h2-font-weight` | `var(--font-weight--normal)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.underlay-nav__header> — `1stdecember-com`)**:
   - Landmark `<header class="underlay-nav__header">` (`1440x98px`) hosting `First December Films · Ad Film Produ` navigation (`Home · Work · Directors · About · AI Ad Films`), DOM attributes (`data-wf-domain="1stdecember.com"`, `data-wf-page="6a530ef9dd045382387c1080"`, `data-wf-site="6a530ef3dd045382387c1010"`, `data-key="CANq2ndVhhRcE6Gj1ydbwg"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section_about> — `1st December Films`)**:
   - Landmark `<section class="section_about">` presenting display lead `1st December Films` and copy excerpt *"First December Films is a Mumbai based advertising film house, an"* over `#efece7` canvas and `#20201e` ink.
3. **Primary Showcase & Content Grid (<section.section_work> — `India's most awarded ad film house`)**:
   - Landmark `<section class="section_work">` rendering section `India's most awarded ad film house` with copy *"E x p l o r e A l l W o r k"*, asset references (`cdn.prod.website-files.com`, `first-december-films.webflow.shar...`, `6acdf9b670164716e898eb2d_fav%20we...`, `6acdf9b6d5ee9f500bdfb333_fav%20we...`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section_team-home> — `The one film a brand builds its ye`)**:
   - Landmark `<section class="section_team-home">` framing `The one film a brand builds its year around` and `what we are proud of` (*"Cannes Gold and Glass Lion winning producer, counted among the wo"*) with `#e5e7eb` surface cards, `#ffff00` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.demo-footer> — `https://1stdecember.com`)**:
   - Landmark `<footer class="demo-footer">` anchoring `First December Films · Ad Film P` footer links (`Home · Work · Directors · About · AI Ad Films`), copy *"Cannes Lions winning director (2014, 2016, 2017) and the onl"*, and `#9ca3b0` structural dividers.
