# UI & UX Architecture: nickho-motorsports-nl

## Overview & Design Identity
- **Target**: `nickho-motorsports-nl` (**Nick Ho - Dutch Racing Driver · Porsche Carrera Cup**)
- **Production URL**: [https://nickho-motorsports.nl/](https://nickho-motorsports.nl/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#333` / `#fffc`)
- **Summary**: 21-year-old racing driver from Rotterdam competing in Porsche Carrera Cup Deutschland. 17 career podiums, 14 circuits raced. Follow my mo...
- **Total Clean CSS Variables Extracted**: `94` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Anton`
- **Body Font Stack**: `Helvetica`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--_typography---rich-text--h1: 6rem`; rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: CSS variables `--_typography---rich-text--h2: 4rem`; rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: CSS variables `--_typography---line-height--body: 1.4`, `--_typography---body-size--regular: 1rem`, `--_typography---body-size--small: .875rem`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: CSS variables `--_typography---heading-size--small: 2rem`, `--_typography---heading-size--xsmall: 1.625rem`, `--_typography---body-size--small: .875rem`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#333` | `var(--_colors---black--80)` in `:root` |
| **Primary Typography Ink** | `#fff3` | `var(--_colors---white--20)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fed60a` | `var(--_colors---primary--100)` in `:root` |
| **Interactive Accent / Highlight** | `#fffc` | `var(--_colors---white--80)` in `:root` |
| **Secondary / Muted Copy** | `#0003` | `var(--_colors---black--20)` in `:root` |
| **Structural Hairline Border** | `#0000` | `a { background-color: #0000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
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

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.bold-nav-full> — `nickho-motorsports-nl`)**:
   - Landmark `<nav class="bold-nav-full">` hosting `Nick Ho - Dutch Racing Driver · Pors` navigation (`About · History · Gallery · Calendar · Contact`), DOM attributes (`data-wf-domain="nickho-motorsports.nl"`, `data-wf-page="6a422333c15d8477da5a843f"`, `data-wf-site="6a422333c15d8477da5a8443"`, `data-grab-cursor`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.section_hero> — `Nick Ho`)**:
   - Landmark `<section class="section_hero">` presenting display lead `Nick Ho` and copy excerpt *"S e e m o r e S e e m o r e"* over `#333` canvas and `#fed60a` ink.
3. **Primary Showcase & Content Grid (<section.section_about> — `The Foundation`)**:
   - Landmark `<section class="section_about">` rendering section `The Foundation` with copy *"S o u n d o n S o u n d o n"*, asset references (`cdn.prod.website-files.com`, `nick-ho.webflow.shared.f23fd3a71.css`, `6a423f0c4a28dcd7702058a2_nick-ho-...`, `6a423f14a90180269b9bab31_nick-ho-...`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section_agenda> — `First Victories`)**:
   - Landmark `<section class="section_agenda">` framing `First Victories` and `Proving Speed` (*"I n s t a g r a m I n s t a g r a m"*) with `#fed60a` surface cards, `#fffc` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.w-embed> — `https://nickho-motorsports.nl/`)**:
   - Landmark `<footer class="w-embed">` anchoring `Nick Ho - Dutch Racing Driver · ` footer links (`About · History · Gallery · Calendar · Contact`), copy *"L i n k e d I n L i n k e d I n"*, and `#0000` structural dividers.
