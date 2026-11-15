# UI & UX Architecture: www-bluesqx-com

## Overview & Design Identity
- **Target**: `www-bluesqx-com` (**Blue Square X – Premium LED Displays & Immersive Digital Experiences**)
- **Production URL**: [https://www.bluesqx.com/](https://www.bluesqx.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#fff0`)
- **Summary**: We design and deliver high-end LED display systems and immersive digital experiences for luxury brands, retail spaces, and iconic environ...
- **Total Clean CSS Variables Extracted**: `66` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Beausite Classic`
- **Body Font Stack**: `Arial`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Section Heading (`H2`)**: rule `h2` (`letter-spacing: -.125rem`)
- **Body Copy**: CSS variables `--_typography---font-styles--body: "Beausite Classic",Arial,sans-serif`
- **Metadata & Labels**: CSS variables `--_ui-styles---radius--xxsmall: .125rem`, `--_ui-styles---radius--small: .25rem`; rule `.label` (`font-size: 0.75rem`, `font-weight: 400`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--_primitives---colors--white)` in `:root` |
| **Primary Typography Ink** | `#1b1e24` | `var(--_primitives---colors--neutral-darkest)` in `:root` |
| **Elevated Surface / Card Substrate** | `#7d8086` | `var(--_primitives---colors--neutral)` in `:root` |
| **Interactive Accent / Highlight** | `#fff0` | `var(--_primitives---opacity--transparent)` in `:root` |
| **Secondary / Muted Copy** | `#fff3` | `var(--_primitives---opacity--white-20)` in `:root` |
| **Structural Hairline Border** | `#0229d5` | `var(--_primitives---colors--blue-accent)` in `:root` |
| **Variable Token (`--_primitives---opacity--neutral-darkest-15`)** | `#1b1e2426` | `var(--_primitives---opacity--neutral-darkest-15)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_primitives---colors--white` | `#fff` | Canvas / Surface Token |
| `--_typography---font-styles--body` | `"Beausite Classic",Arial,sans-serif` | Typography / Scale Token |
| `--_primitives---colors--neutral-darkest` | `#1b1e24` | Canvas / Surface Token |
| `--_typography---font-styles--heading` | `"Beausite Classic",Arial,sans-serif` | Typography Ink Token |
| `--outline-button--text` | `var(--_primitives---colors--neutral-darkest)` | Typography Ink Token |
| `--header--link-color-hover` | `var(--_primitives---colors--blue-accent)` | Typography Ink Token |
| `--_primitives---colors--neutral` | `#7d8086` | Brand / Palette Token |
| `--_primitives---colors--neutral-darker` | `#1b1e24` | Canvas / Surface Token |
| `--_ui-styles---radius--xxsmall` | `.125rem` | Elevation / Border Token |
| `--button--border` | `var(--_primitives---colors--neutral-darkest)` | Elevation / Border Token |
| `--button--background` | `var(--_primitives---colors--neutral-darkest)` | Canvas / Surface Token |
| `--button--text` | `var(--_primitives---colors--white)` | Typography Ink Token |
| `--_primitives---opacity--transparent` | `#fff0` | Color / Atmospheric Token |
| `--_primitives---opacity--neutral-darkest-15` | `#1b1e2426` | Canvas / Surface Token |
| `--outline-button--border` | `var(--_primitives---opacity--neutral-darkest-15)` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.navbar_menu> — `www-bluesqx-com`)**:
   - Landmark `<nav class="navbar_menu w-nav-menu">` hosting `Blue Square X – Premium LED Displays` navigation (`Art & Museums · Corporate · Hospitality · Luxury Living · Luxury Real Estate`), DOM attributes (`data-wf-domain="www.bluesqx.com"`, `data-wf-page="69272aa8c1734eeb3d97ece3"`, `data-wf-site="69272aa5c1734eeb3d97e49c"`, `data-lenis-prevent="true"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.banner_component> — `Let’s Be in Touch`)**:
   - Landmark `<section class="banner_component dark">` presenting display lead `Let’s Be in Touch` and copy excerpt *"By submitting this form, you agree to receive promotional emails "* over `#fff` canvas and `#1b1e24` ink.
3. **Primary Showcase & Content Grid (<section.section_header> — `Stay Inspired`)**:
   - Landmark `<section class="section_header dark">` rendering section `Stay Inspired` with copy *"Get the latest insights, projects, and innovations from Blue Squa"*, asset references (`cdn.prod.website-files.com`, `bluesquarex.webflow.shared.e27118...`, `pixel.gif`, `data.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section_services-cards> — `Build Your Immersive Experiences`)**:
   - Landmark `<section class="section_services-cards base">` framing `Build Your Immersive Experiences` and `Discover LED Indoor and Outdoor Products` (*"Stay Inspired! Subscribe for the latest Blue Square X updates."*) with `#7d8086` surface cards, `#fff0` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.bluesqx.com/`)**:
   - Landmark `<footer class="footer dark">` anchoring `Blue Square X – Premium LED Disp` footer links (`Art & Museums · Corporate · Hospitality · Luxury Living · Luxury Real Estate`), copy *"Luxury Real Estate"*, and `#0229d5` structural dividers.
