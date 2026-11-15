# UI & UX Architecture: www-paaspop-nl

## Overview & Design Identity
- **Target**: `www-paaspop-nl` (**Paaspop 2027 · 26, 27 & 28 maart**)
- **Production URL**: [https://www.paaspop.nl/](https://www.paaspop.nl/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#100026` / `#000c`)
- **Summary**: Op 26, 27 en 28 maart vieren we 50 jaar Paaspop. Verschillende generaties, verschillende smaken, dezelfde mentaliteit. Dat vieren we groo...
- **Total Clean CSS Variables Extracted**: `294` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Onest`
- **Body Font Stack**: `Recoleta`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--_typography---rich-text--h1: 6rem`; rule `h1` (`font-size: var(--_typography---rich-text...`, `line-height: var(--_typography---l...`)
- **Section Heading (`H2`)**: CSS variables `--_typography---rich-text--h2: 4rem`; rule `h2` (`font-size: var(--_typography---rich-text...`, `line-height: var(--_typography---l...`)
- **Body Copy**: CSS variables `--_typography---body-size--regular: 1rem`, `--_typography---line-height--body: 1.3`, `--_typography---body-size--large: 1.5rem`; rule `p` (`font-size: var(--_typography---body-size...`)
- **Metadata & Labels**: CSS variables `--_typography---heading-size--small: 1.5rem`, `--_typography---heading-size--xsmall: 1.25rem`, `--gap-spacing--small: 1rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#100026` | `var(--_colors---midnight--100)` in `:root` |
| **Primary Typography Ink** | `#ffb82e` | `var(--_colors---amber--100)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0003` | `var(--_colors---black--20)` in `:root` |
| **Interactive Accent / Highlight** | `#000c` | `var(--_colors---black--80)` in `:root` |
| **Secondary / Muted Copy** | `#fff3` | `var(--_colors---white--20)` in `:root` |
| **Structural Hairline Border** | `#7e10ff` | `var(--_colors---purple--100)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
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

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.navbar_component> — `www-paaspop-nl`)**:
   - Landmark `<header class="navbar_component">` hosting `Paaspop 2027 · 26, 27 & 28 maart` navigation (`Home · Line-up · Tickets · Veelgestelde vragen · Paradise City`), DOM attributes (`data-wf-domain="www.paaspop.nl"`, `data-wf-page="6ac63e14514945d47eafbb94"`, `data-wf-site="6ac63e14514945d47eafbb98"`, `data-page-load-state="done"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section_hero> — `Deze website maakt gebruik van coo`)**:
   - Landmark `<section class="section_hero">` presenting display lead `Deze website maakt gebruik van cookies` and copy excerpt *"Noodzakelijk Noodzakelijke cookies helpen een website bruikbaarde"* over `#100026` canvas and `#ffb82e` ink.
3. **Primary Showcase & Content Grid (<section.section_fifty-years> — `The unexpected, the unbelievable, `)**:
   - Landmark `<section class="section_fifty-years">` rendering section `The unexpected, the unbelievable, & unforgettable` with copy *"Noodzakelijke cookies helpen een website bruikbaarder te maken, d"*, asset references (`cdn.prod.website-files.com`, `paaspop.webflow.shared.7aa3d0213....`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section_line-up> — `50 years of the greatest show on e`)**:
   - Landmark `<section class="section_line-up">` framing `50 years of the greatest show on earth` and `the first 50 names` (*"Voorkeuren Voorkeurscookies zorgen ervoor dat een website informa"*) with `#0003` surface cards, `#000c` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer_component> — `https://www.paaspop.nl/`)**:
   - Landmark `<footer class="footer_component">` anchoring `Paaspop 2027 · 26, 27 & 28 maart` footer links (`Home · Line-up · Tickets · Veelgestelde vragen · Paradise City`), copy *"Voorkeurscookies zorgen ervoor dat een website informatie ka"*, and `#7e10ff` structural dividers.
