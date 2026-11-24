---
title: "UI & UX Architecture: nickho-motorsports-nl"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: nickho-motorsports-nl

## Overview & Design Identity
- **Target**: `nickho-motorsports-nl` (**Nick Ho - Dutch Racing Driver · Porsche Carrera Cup**)
- **Production URL**: [https://nickho-motorsports.nl/](https://nickho-motorsports.nl/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#fed60a`)
- **Summary**: 21-year-old racing driver from Rotterdam competing in Porsche Carrera Cup Deutschland. 17 career podiums, 14 circuits raced. Follow my mo...
- **Total Clean CSS Variables Extracted**: `94` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Anton`
- **Body Font Stack**: `.875rem`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 50px`, `line-height: 55px`, `font-weight: 600`); CSS variables `--_typography---rich-text--h1: 6rem`; rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 50px`, `line-height: 55px`, `font-weight: 600`); CSS variables `--_typography---rich-text--h2: 4rem`; rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 22.4px`, `font-weight: 400`); CSS variables `--_typography---line-height--body: 1.4`, `--_typography---body-size--regular: 1rem`, `--_typography---body-size--small: .875rem`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 22.4px`, `font-weight: 400`); CSS variables `--_typography---heading-size--small: 2rem`, `--_typography---heading-size--xsmall: 1.625rem`, `--_typography---body-size--small: .875rem`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#fed60a` | `var(--_colors---primary--100)` in `:root` |
| **Secondary / Muted Copy** | `#333333` | live computed `nav` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_typography---fonts--primary-font` | `Helvetica, Arial, sans-serif` | Brand / Palette Token |
| `--_colors---black--80` | `#333` | Canvas / Surface Token |
| `--_typography---line-height--body` | `1.4` | Typography / Scale Token |
| `--_typography---heading-size--xlarge` | `10rem` | Typography Ink Token |
| `--_typography---line-height--heading` | `1` | Typography Ink Token |
| `--_typography---heading-size--large` | `3.125rem` | Typography Ink Token |
| `--_typography---heading-size--medium` | `2rem` | Typography Ink Token |
| `--_typography---heading-size--small` | `2rem` | Typography Ink Token |
| `--_typography---heading-size--xsmall` | `1.625rem` | Typography Ink Token |
| `--_typography---body-size--regular` | `1rem` | Layout / Spatial Grid Token |
| `--_typography---body-size--small` | `.875rem` | Layout / Spatial Grid Token |
| `--_typography---body-size--large` | `1.25rem` | Layout / Spatial Grid Token |
| `--_typography---fonts--heading-font` | `Anton, Arial, sans-serif` | Typography Ink Token |
| `--_colors---black--100` | `black` | Canvas / Surface Token |
| `--_colors---white--100` | `white` | Canvas / Surface Token |
| `--_typography---rich-text--h1` | `6rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.bold-nav-full> — `nickho-motorsports-nl`)**:
   - Landmark `<nav class="bold-nav-full">` (`1440x0px`) hosting `Nick Ho - Dutch Racing Driver · Pors` navigation (`About · History · Gallery · Calendar · Contact`), DOM attributes (`data-wf-domain="nickho-motorsports.nl"`, `data-wf-page="6a422333c15d8477da5a843f"`, `data-wf-site="6a422333c15d8477da5a8443"`, `data-grab-cursor`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.section_hero> — `NICK HO`)**:
   - Landmark `<section class="section_hero">` presenting display lead `NICK HO` and copy excerpt *"S e e m o r e S e e m o r e"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.section_about> — `Nick Ho`)**:
   - Landmark `<section class="section_about">` rendering section `Nick Ho` with copy *"S o u n d o n S o u n d o n"*, asset references (`cdn.prod.website-files.com`, `nick-ho.webflow.shared.f23fd3a71.css`, `6a423f0c4a28dcd7702058a2_nick-ho-...`, `6a423f14a90180269b9bab31_nick-ho-...`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section_agenda> — `S o u n d o n S o u n d o n`)**:
   - Landmark `<section class="section_agenda">` framing `S o u n d o n S o u n d o n` and `I n s t a g r a m I n s t a g r a m` (*"I n s t a g r a m I n s t a g r a m"*) with `#ffff00` surface cards, `#fed60a` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.w-embed> — `https://nickho-motorsports.nl/`)**:
   - Landmark `<footer class="w-embed">` anchoring `Nick Ho - Dutch Racing Driver · ` footer links (`About · History · Gallery · Calendar · Contact`), copy *"L i n k e d I n L i n k e d I n"*, and `#e2e2e2` structural dividers.
