---
title: "UI & UX Architecture: bcgbuildingdesign-com-au"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: bcgbuildingdesign-com-au

## Overview & Design Identity
- **Target**: `bcgbuildingdesign-com-au` (**Building Designer Gold Coast · BCG Building Design**)
- **Production URL**: [https://bcgbuildingdesign.com.au/](https://bcgbuildingdesign.com.au/)
- **Final Redirected URL**: [https://www.bcgbuildingdesign.com.au/](https://www.bcgbuildingdesign.com.au/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f3efe8` canvas, `#3a3028` ink, `#0082f3` accent)
- **Summary**: Boutique building design studio in Gold Coast crafting high-end custom homes and major renovations, personally led from concept to constr...
- **Total Clean CSS Variables Extracted**: `159` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `NeueHaasDisplay Pro`
- **Body Font Stack**: `NeueHaasDisplay Pro`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 14.4px`, `font-weight: 500`); CSS variables `--_typography---h1--h1-font-size: 3.5rem`, `--_typography---h1--h1-line-height: var(--_typography---font-height--tiny)`, `--_typography---h1--h1-font-weight: var(--font-weight--semi-bold)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 40px`, `font-weight: 600`); CSS variables `--_typography---h2--h2-font-size: 3em`, `--_typography---h2--h2-line-height: var(--_typography---font-height--medium)`, `--_typography---h2--h2-font-weight: var(--font-weight--bold)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 600`); CSS variables `--font-family--body: "NeueHaasDisplay Pro",Arial,sans-serif`, `--_typography---body--body-line-height: var(--_typography---font-height--medium)`, `--_typography---body--body-letter-spacing: var(--_typography---letter-spacing--default)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 600`); CSS variables `--_typography---body--body-letter-spacing: var(--_typography---letter-spacing--default)`, `--_typography---h1--h1-letter-spacing: var(--_typography---letter-spacing--default)`, `--_typography---h2--h2-letter-spacing: var(--_typography---letter-spacing--default)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f3efe8` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#3a3028` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#fffdf8` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--brand--beige` | `#f3efe8` | Brand / Palette Token |
| `--font-family--body` | `"NeueHaasDisplay Pro",Arial,sans-serif` | Typography / Scale Token |
| `--_theme---text-color--primary` | `var(--neutral--black)` | Typography Ink Token |
| `--_typography---body--body-line-height` | `var(--_typography---font-height--medium)` | Typography / Scale Token |
| `--font-weight--semi-bold` | `600` | Typography / Scale Token |
| `--_typography---body--body-letter-spacing` | `var(--_typography---letter-spacing--default)` | Typography / Scale Token |
| `--font-family--heading` | `"NeueHaasDisplay Pro",Arial,sans-serif` | Typography Ink Token |
| `--_typography---h1--h1-font-size` | `3.5rem` | Typography / Scale Token |
| `--_typography---h1--h1-line-height` | `var(--_typography---font-height--tiny)` | Typography / Scale Token |
| `--_typography---h1--h1-font-weight` | `var(--font-weight--semi-bold)` | Typography / Scale Token |
| `--_typography---h1--h1-letter-spacing` | `var(--_typography---letter-spacing--default)` | Typography / Scale Token |
| `--_typography---h2--h2-font-size` | `3em` | Typography / Scale Token |
| `--_typography---h2--h2-line-height` | `var(--_typography---font-height--medium)` | Typography / Scale Token |
| `--_typography---h2--h2-font-weight` | `var(--font-weight--bold)` | Typography / Scale Token |
| `--_typography---h2--h2-letter-spacing` | `var(--_typography---letter-spacing--default)` | Typography / Scale Token |
| `--_typography---h3--h3-font-size` | `2.5rem` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.navbar> — `bcgbuildingdesign-com-au`)**:
   - Landmark `<nav class="navbar">` (`1440x40px`) hosting `Building Designer Gold Coast · BCG B` navigation (`Home · Studio · Process · Projects · Project Enquiry`), DOM attributes (`data-wf-domain="www.bcgbuildingdesign..."`, `data-wf-page="6a794e5aeebba97e3ac774a5"`, `data-wf-site="6a794e5aeebba97e3ac774ae"`, `data-barba="wrapper"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section> — `Building Designer Gold Coast`)**:
   - Landmark `<section class="section is-relative">` presenting display lead `Building Designer Gold Coast` and copy excerpt *"BCG is a boutique building design studio based on the Gold Coast,"* over `#f3efe8` canvas and `#3a3028` ink.
3. **Primary Showcase & Content Grid (<section.is-sticky> — `Every considered home begins with `)**:
   - Landmark `<section class="section is-sticky">` rendering section `Every considered home begins with a considered ap...` with copy *"We’ve had a great experience with BCG designs. We approached Bian"*, asset references (`cdn.prod.website-files.com`, `bcg-staging.webflow.shared.4c5b11...`, `gtm.js`, `recaptcha__en.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section-brown> — `Featured Works`)**:
   - Landmark `<section class="section-brown">` framing `Featured Works` and `Thoughtful home design requires everyone working...` (*"We have had the opportunity of working collaboratively on a few p"*) with `#ffff00` surface cards, `#0082f3` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.section_footer> — `https://bcgbuildingdesign.com.au/`)**:
   - Landmark `<footer class="section_footer">` anchoring `Building Designer Gold Coast · B` footer links (`Home · Studio · Process · Projects · Project Enquiry`), copy *"Davey Constructions"*, and `#e2e2e2` structural dividers.
