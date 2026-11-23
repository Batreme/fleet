---
title: "UI & UX Architecture: www-paaspop-nl"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-paaspop-nl

## Overview & Design Identity
- **Target**: `www-paaspop-nl` (**Paaspop 2027 · 26, 27 & 28 maart**)
- **Production URL**: [https://www.paaspop.nl/](https://www.paaspop.nl/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#100026` / `#0082f3`)
- **Summary**: Op 26, 27 en 28 maart vieren we 50 jaar Paaspop. Verschillende generaties, verschillende smaken, dezelfde mentaliteit. Dat vieren we groo...
- **Total Clean CSS Variables Extracted**: `298` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Recoleta`
- **Body Font Stack**: `Onest`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80px`, `line-height: 80px`, `font-weight: 700`); CSS variables `--_typography---rich-text--h1: 6rem`; rule `h1` (`font-size: var(--_typography---rich-text...`, `line-height: var(--_typography---l...`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 72px`, `font-weight: 700`); CSS variables `--_typography---rich-text--h2: 4rem`; rule `h2` (`font-size: var(--_typography---rich-text...`, `line-height: var(--_typography---l...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 500`); CSS variables `--_typography---body-size--regular: 1rem`, `--_typography---line-height--body: 1.3`, `--_typography---body-size--large: 1.5rem`; rule `p` (`font-size: var(--_typography---body-size...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 500`); CSS variables `--_typography---heading-size--small: 1.5rem`, `--_typography---heading-size--xsmall: 1.25rem`, `--gap-spacing--small: 1rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#100026` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#222222` | `.w-slider-nav-invert>div.w-active { background-color: #222222 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#ff87e1` | `var(--_colors---pink--100)` in `:root` |
| **Structural Hairline Border** | `#3898ec` | `.w-select:focus { border-color: #3898ec }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_colors---midnight--100` | `#100026` | Brand / Palette Token |
| `--_typography---fonts--primary-font` | `Onest,sans-serif` | Brand / Palette Token |
| `--_colors---black--100` | `black` | Canvas / Surface Token |
| `--_typography---body-size--regular` | `1rem` | Layout / Spatial Grid Token |
| `--_typography---line-height--body` | `1.3` | Typography / Scale Token |
| `--_typography---fonts--heading-font` | `Recoleta,Arial,sans-serif` | Typography Ink Token |
| `--_typography---heading-size--xlarge` | `5rem` | Typography Ink Token |
| `--_typography---line-height--heading` | `1` | Typography Ink Token |
| `--_typography---heading-size--large` | `4.5rem` | Typography Ink Token |
| `--_typography---heading-size--medium` | `2.5rem` | Typography Ink Token |
| `--_typography---heading-size--small` | `1.5rem` | Typography Ink Token |
| `--_typography---heading-size--xsmall` | `1.25rem` | Typography Ink Token |
| `--_typography---button-size--regular` | `.875rem` | Layout / Spatial Grid Token |
| `--_typography---line-height--button` | `1.2` | Typography / Scale Token |
| `--_typography---body-size--large` | `1.5rem` | Layout / Spatial Grid Token |
| `--gap-spacing--small` | `1rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.navbar_component> — `www-paaspop-nl`)**:
   - Landmark `<header class="navbar_component">` (`1440x92px`) hosting `Paaspop 2027 · 26, 27 & 28 maart` navigation (`Home · Line-up · Tickets · Veelgestelde vragen · Paradise City`), DOM attributes (`data-wf-domain="www.paaspop.nl"`, `data-wf-page="6ac63e14514945d47eafbb94"`, `data-wf-site="6ac63e14514945d47eafbb98"`, `data-page-load-state="done"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section_hero> — `THE UNEXPECTED, THE UNBELIEVABLE, `)**:
   - Landmark `<section class="section_hero">` presenting display lead `THE UNEXPECTED, THE UNBELIEVABLE, & UNFORGETTABLE` and copy excerpt *"In 2027 vieren we vijftig jaar Paaspop. Een halve eeuw vol muziek"* over `#100026` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.section_fifty-years> — `The unexpected, the unbelievable, `)**:
   - Landmark `<section class="section_fifty-years">` rendering section `The unexpected, the unbelievable, & unforgettable` with copy *"Met deze eerste 50 namen duiken we head first de 50e editie in! C"*, asset references (`cdn.prod.website-files.com`, `paaspop.webflow.shared.7aa3d0213....`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section_line-up> — `50 years of the greatest show on e`)**:
   - Landmark `<section class="section_line-up">` framing `50 years of the greatest show on earth` and `the first 50 names` (*"The full Paaspop experience begint wanneer je de weg oversteekt n"*) with `#222222` surface cards, `#0082f3` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer_component> — `https://www.paaspop.nl/`)**:
   - Landmark `<footer class="footer_component">` anchoring `Paaspop 2027 · 26, 27 & 28 maart` footer links (`Home · Line-up · Tickets · Veelgestelde vragen · Paradise City`), copy *"Ontdek ze allemaal! Van hard-hitting gitaarwerk tot disco en"*, and `#3898ec` structural dividers.
