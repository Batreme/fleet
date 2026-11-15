# UI & UX Architecture: navtec-com

## Overview & Design Identity
- **Target**: `navtec-com` (**Moab Adventure Tours · Navtec Expeditions Since 1896**)
- **Production URL**: [https://navtec.com/](https://navtec.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#062c3c` canvas, `#fcfbf8` ink, `#031820` accent)
- **Summary**: Explore Moab's canyons with expert guides. Rafting, 4x4 tours, canyoneering & hiking in Arches & Canyonlands. Family-owned since 1896. Bo...
- **Total Clean CSS Variables Extracted**: `95` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Eczar`
- **Body Font Stack**: `Geologica`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: CSS variables `--_headings---h1--font-family: var(--_fonts---font-headings)`, `--_headings---h1--font-size: 5.2rem`, `--_headings---h1--line-height: 1.25em`
- **Section Heading (`H2`)**: CSS variables `--_headings---h2--font-family: var(--_fonts---font-headings)`, `--_headings---h2--font-size: 4rem`, `--_headings---h2--line-height: 1.25em`
- **Body Copy**: CSS variables `--_base-styles---body--background: var(--sand)`, `--_base-styles---body--font-family: var(--_fonts---font-base)`, `--_base-styles---body--font-color: var(--deep-teal)`; rule `p` (`font-size: var(--_base-styles---typograp...`, `line-height: var(--_base-styles---...`)
- **Metadata & Labels**: CSS variables `--_base-styles---typography--letter-spacing: 0em`, `--_headings---h1--letter-spacing: 0em`, `--_headings---h2--letter-spacing: 0em`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#062c3c` | `var(--deep-teal)` in `:root` |
| **Primary Typography Ink** | `#ebe6d8` | `var(--sand)` in `:root` |
| **Elevated Surface / Card Substrate** | `#5b1f11` | `var(--rust-red)` in `:root` |
| **Interactive Accent / Highlight** | `#031820` | `var(--dark-teal)` in `:root` |
| **Secondary / Muted Copy** | `#fcfbf8` | `var(--off-white)` in `:root` |
| **Structural Hairline Border** | `#8c5129` | `var(--warm-brown)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_base-styles---body--background` | `var(--sand)` | Canvas / Surface Token |
| `--_base-styles---body--font-family` | `var(--_fonts---font-base)` | Typography / Scale Token |
| `--_base-styles---body--font-color` | `var(--deep-teal)` | Brand / Palette Token |
| `--_base-styles---typography--font-size-base` | `1.8rem` | Typography / Scale Token |
| `--_base-styles---typography--line-height` | `1.5em` | Typography / Scale Token |
| `--_base-styles---typography--font-weight` | `400` | Typography / Scale Token |
| `--_base-styles---typography--letter-spacing` | `0em` | Typography / Scale Token |
| `--_headings---h1--font-family` | `var(--_fonts---font-headings)` | Typography Ink Token |
| `--_headings---h1--font-size` | `5.2rem` | Typography Ink Token |
| `--_headings---h1--line-height` | `1.25em` | Typography Ink Token |
| `--_headings---h1--font-weight` | `400` | Typography Ink Token |
| `--_headings---h1--letter-spacing` | `0em` | Typography Ink Token |
| `--_headings---h2--font-family` | `var(--_fonts---font-headings)` | Typography Ink Token |
| `--_headings---h2--font-size` | `4rem` | Typography Ink Token |
| `--_headings---h2--line-height` | `1.25em` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav> — `navtec-com`)**:
   - Landmark `<nav class="nav">` hosting `Moab Adventure Tours · Navtec Expedi` navigation (`Half Day · Full Day · 2-3 Days · 4-6 Days · River & Rafting`), DOM attributes (`data-wf-domain="navtec.com"`, `data-wf-page="6a310f67244daebf3f62c77e"`, `data-wf-site="6a310f64244daebf3f62c717"`, `data-wf-intellimize-customer-id="117402178"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.header> — `Heading`)**:
   - Landmark `<section class="header">` presenting display lead `Heading` and copy excerpt *"Expeditions Browse Our Expeditions by Duration Half Day Full Day "* over `#062c3c` canvas and `#fcfbf8` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Wild Places, Thoughtfully Explored`)**:
   - Landmark `<section class="section">` rendering section `Wild Places, Thoughtfully Explored.` with copy *"Arches National Park"*, asset references (`cdn.prod.website-files.com`, `navtec.webflow.shared.6acfbfa82.m...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section-wave> — `71,000`)**:
   - Landmark `<section class="section-wave">` framing `71,000` and `61,000` (*"Canyonlands National Park"*) with `#5b1f11` surface cards, `#031820` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://navtec.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Moab Adventure Tours · Navtec Ex` footer links (`Half Day · Full Day · 2-3 Days · 4-6 Days · River & Rafting`), copy *"Moab Full Day Canyoneering Scramble through fins and pothole"*, and `#8c5129` structural dividers.
