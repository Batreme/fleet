---
title: "UI & UX Architecture: thecontenders-co"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: thecontenders-co

## Overview & Design Identity
- **Target**: `thecontenders-co` (**The Contenders · Strategic Brand & Design Consultancy**)
- **Production URL**: [https://thecontenders.co/](https://thecontenders.co/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ed0000`)
- **Summary**: Where business meets brand. The Contenders is an independent Australian consultancy creating distinctive brands that deliver measurable i...
- **Total Clean CSS Variables Extracted**: `130` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Mesapholic`
- **Body Font Stack**: `DieGrotesk`
- **Monospace / Technical Font Stack**: `iki-mono-variable`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 180px`, `line-height: 144px`, `font-weight: 400`); CSS variables `--heading-h1-font-family: var(--font-serif)`, `--heading-h1-font-size: 4rem`, `--heading-h1-font-weight: 400`
- **Section Heading (`H2`)**: CSS variables `--heading-h2-font-family: var(--font-serif)`, `--heading-h2-font-size: 3.5rem`, `--heading-h2-font-weight: 400`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 200`); CSS variables `--body-l-font-family: var(--font-sans)`, `--body-l-font-size: 1.125rem`, `--body-l-font-weight: 400`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 200`); CSS variables `--font-mono: "iki-mono-variable", sans-serif`, `--heading-h1-letter-spacing: -.02em`, `--heading-h2-letter-spacing: -.02em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e5e5e5` | `.bg-black-10 { background-color: #e5e5e5 }` |
| **Interactive Accent / Highlight** | `#ed0000` | `.homepage-intro-link__artwork { color: #ed0000 }` |
| **Secondary / Muted Copy** | `#808080` | `.text-gray-900 { color: gray }` (`#808080`) |
| **Structural Hairline Border** | `#b2b2b2` | `.border-black-30 { border-color: #b2b2b2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-background` | `var(--color-white)` | Canvas / Surface Token |
| `--color-foreground` | `var(--color-black)` | Typography Ink Token |
| `--color-border` | `var(--color-black-30)` | Brand / Palette Token |
| `--color-active-link` | `var(--color-red)` | Typography Ink Token |
| `--color-blockquote` | `var(--color-black-60)` | Brand / Palette Token |
| `--font-serif` | `var(--font-mesapholic), serif` | Typography / Scale Token |
| `--font-sans` | `var(--font-die-grotesk), sans-serif` | Typography / Scale Token |
| `--font-mono` | `"iki-mono-variable", sans-serif` | Typography / Scale Token |
| `--heading-xxl-font-family` | `var(--font-serif)` | Typography Ink Token |
| `--heading-xxl-font-size` | `10rem` | Typography Ink Token |
| `--heading-xxl-font-weight` | `400` | Typography Ink Token |
| `--heading-xxl-line-height` | `80%` | Typography Ink Token |
| `--heading-xl-font-family` | `var(--font-serif)` | Typography Ink Token |
| `--heading-xl-font-size` | `12.4rem` | Typography Ink Token |
| `--heading-xl-font-weight` | `400` | Typography Ink Token |
| `--heading-xl-line-height` | `80%` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.py-4> — `thecontenders-co`)**:
   - Landmark `<nav class="py-4 navbar-transition-excluded">` (`1385x134px`) hosting `The Contenders · Strategic Brand & D` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-theme="white"`, `data-homepage="true"`, `data-lenis-prevent="true"`), and stylesheet rule `.WkV8yq_className { font-family:DieGrotesk,DieGrotesk Fallback }`.
2. **Hero Stage & Focal Lead (<section.homepage-intro-copy> — `THE CONTENDERS IS A CONSULTANCY WH`)**:
   - Landmark `<section class="homepage-intro-copy">` presenting display lead `THE CONTENDERS IS A CONSULTANCY WHERE BUSINESS ME...` and copy excerpt *"In the spirit of reconciliation, The Contenders acknowledges the "* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.homepage-intro-copy:nth(2)> — `THE CONTENDERS`)**:
   - Landmark `<section class="homepage-intro-copy">` rendering section `THE CONTENDERS` with copy *"THE CONTENDERS IS A CONSULTANCY WHERE BUSINESS MEETS BRAND."*, asset references (`Horizontal-3fa5268f-53f1-4223-a6c...`, `Compact-7923dd47-d322-4f23-802c-c...`, `00k7ot6zx_lfg.css`, `123l3rregymnq.js`), and grid rule `.WkV8yq_variable { --font-die-grotesk:"DieGrotesk", "DieGrotesk Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.homepage-intro-copy:nth(3)> — `THE CONTENDERS IS A CONSULTANCY WH`)**:
   - Landmark `<section class="homepage-intro-copy">` framing `THE CONTENDERS IS A CONSULTANCY WHERE BUSINESS M` and `WE UNDERSTAND THAT YOUR ORGANISATION IS FIGHTING` (*"WE UNDERSTAND THAT YOUR ORGANISATION IS FIGHTING FOR SOMETHING."*) with `#e5e5e5` surface cards, `#ed0000` accents, and `.HMGLSG_className { font-family:Mesapholic,Mesapholic Fallback }`.
5. **Colophon & Global Directory Footer (<footer.fixed> — `https://thecontenders.co/`)**:
   - Landmark `<footer class="fixed">` anchoring `The Contenders · Strategic Brand` footer links (`Overview · Index · Archive · About · Contact`), copy *"GREATER GROWTH. GREATER INFLUENCE. GREATER IMPACT."*, and `#b2b2b2` structural dividers.
