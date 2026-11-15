# UI & UX Architecture: www-era-residence-com

## Overview & Design Identity
- **Target**: `www-era-residence-com` (**ERA Residence — Contemporary Mediterranean Residences in Estepona**)
- **Production URL**: [https://www.era-residence.com/](https://www.era-residence.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#1ba64b` canvas, `#f3f3ec` ink, `#340c24` accent)
- **Summary**: Boutique residences on the New Golden Mile combining contemporary architecture, natural materials and resort-style living near Marbella a...
- **Total Clean CSS Variables Extracted**: `202` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Maison Neue Extended`
- **Body Font Stack**: `ambroise-francois-std`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--_fonts---font-display: ambroise-francois-std,sans-serif`, `--_fonts---h1--size: calc(192rem/var(--_special-units---scale-ratio))`, `--_fonts---h1--line-height: 87.5%`
- **Section Heading (`H2`)**: CSS variables `--_fonts---h2--size: calc(136rem/var(--_special-units---scale-ratio))`, `--_fonts---h2--line-height: 88.235%`, `--_fonts---h2--letter-spacing: -.024em`
- **Body Copy**: CSS variables `--_fonts---font-body: "Maison Neue Extended",Arial,sans-serif`
- **Metadata & Labels**: CSS variables `--_fonts---h1--letter-spacing: -.024em`, `--_fonts---h2--letter-spacing: -.024em`, `--_fonts---h3--letter-spacing: -.024em`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#1ba64b` | `var(--_colors---additional--success)` in `:root` |
| **Primary Typography Ink** | `#ffa800` | `var(--_colors---additional--alert)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e23d3d` | `var(--_colors---additional--error)` in `:root` |
| **Interactive Accent / Highlight** | `#340c24` | `var(--_global-colors---brand-500--velvet-plum)` in `:root` |
| **Secondary / Muted Copy** | `#f3f3ec` | `var(--_global-colors---base-0--100)` in `:root` |
| **Structural Hairline Border** | `#b5cedb` | `var(--_global-colors---brand-500--powder-sky)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_fonts---font-body` | `"Maison Neue Extended",Arial,sans-serif` | Typography / Scale Token |
| `--_colors---base-1000--primary` | `var(--_global-colors---base-1000--100)` | Brand / Palette Token |
| `--_fonts---font-display` | `ambroise-francois-std,sans-serif` | Typography / Scale Token |
| `--_fonts---h1--size` | `calc(192rem/var(--_special-units---scale-ratio))` | Typography / Scale Token |
| `--_fonts---h1--line-height` | `87.5%` | Typography / Scale Token |
| `--_fonts---h1--letter-spacing` | `-.024em` | Typography / Scale Token |
| `--_fonts---h2--size` | `calc(136rem/var(--_special-units---scale-ratio))` | Typography / Scale Token |
| `--_fonts---h2--line-height` | `88.235%` | Typography / Scale Token |
| `--_fonts---h2--letter-spacing` | `-.024em` | Typography / Scale Token |
| `--_fonts---h3--size` | `calc(96rem/var(--_special-units---scale-ratio))` | Typography / Scale Token |
| `--_fonts---h3--line-height` | `91.667%` | Typography / Scale Token |
| `--_fonts---h3--letter-spacing` | `-.024em` | Typography / Scale Token |
| `--_fonts---h4--size` | `calc(63rem/var(--_special-units---scale-ratio))` | Typography / Scale Token |
| `--_fonts---h4--line-height` | `88.889%` | Typography / Scale Token |
| `--_fonts---h4--letter-spacing` | `-.016em` | Typography / Scale Token |
| `--_fonts---h5--size` | `calc(40rem/var(--_special-units---scale-ratio))` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-era-residence-com`)**:
   - Landmark `<header class="w-mod-js">` hosting `ERA Residence — Contemporary Mediter` navigation (`Accept Accept · Decline Decline · Menu Menu · Close Close · Contact Contact`), DOM attributes (`data-wf-domain="www.era-residence.com"`, `data-wf-page="6a068da7ad91b057365bf968"`, `data-wf-site="6a068da7ad91b057365bf967"`, `data-barba="wrapper"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section> — `Era Residence`)**:
   - Landmark `<section class="section clip">` presenting display lead `Era Residence` and copy excerpt *"Era Residence A place to return to."* over `#1ba64b` canvas and `#f3f3ec` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Estepona`)**:
   - Landmark `<section class="section arch">` rendering section `Estepona` with copy *"A place to return to."*, asset references (`cdn.prod.website-files.com`, `era-residence.webflow.shared.c955...`, `845813938192979`, `fbevents.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `A place by day by day by night by `)**:
   - Landmark `<section class="section z-2">` framing `A place by day by day by night by night to return to` and `Real-Life Location` (*"Select an Apartment Select an Apartment"*) with `#e23d3d` surface cards, `#340c24` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.lenis> — `https://www.era-residence.com/`)**:
   - Landmark `<footer class="lenis">` anchoring `ERA Residence — Contemporary Med` footer links (`Accept Accept · Decline Decline · Menu Menu · Close Close · Contact Contact`), copy *"Book a call Book a call"*, and `#b5cedb` structural dividers.
