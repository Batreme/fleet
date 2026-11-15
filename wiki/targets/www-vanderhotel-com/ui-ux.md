# UI & UX Architecture: www-vanderhotel-com

## Overview & Design Identity
- **Target**: `www-vanderhotel-com` (**Hotel & Restaurant Ljubljana · Vander Urbani Resort**)
- **Production URL**: [https://www.vanderhotel.com](https://www.vanderhotel.com)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f4f2f1` canvas, `#353230` ink, `#F3F5FB` accent)
- **Summary**: This Design Hotel offers 20 beautiful rooms. For the foodies we have our HAUS & À la carte restaurant or for a glass of champagne we sugg...
- **Total Clean CSS Variables Extracted**: `25` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Sohne Buch`
- **Body Font Stack**: `Arial`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `18px`, `1rem`, `7rem`, `5rem`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2.5rem`)
- **Body Copy**: CSS variables `--_typography---font-styles--body: "Sohne Buch",Arial,sans-serif`
- **Metadata & Labels**: CSS variables `--_ui-styles---radius--small: 0px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f2f1` | `var(--_primitives---colors--white)` in `:root` |
| **Primary Typography Ink** | `#353230` | `var(--_primitives---colors--dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#967850` | `var(--_primitives---colors--brown)` in `:root` |
| **Interactive Accent / Highlight** | `#F3F5FB` | `var(--main-light-color)` in `:root` |
| **Secondary / Muted Copy** | `#ccc` | `.datepicker-dropdown { border: #ccc }` |
| **Structural Hairline Border** | `#39f` | `.datepicker-top-right { color: #39f }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-scheme-1--background-primary` | `var(--_primitives---colors--white)` | Canvas / Surface Token |
| `--_typography---font-styles--body` | `"Sohne Buch",Arial,sans-serif` | Typography / Scale Token |
| `--color-scheme-1--text-primary` | `var(--_primitives---colors--dark)` | Typography Ink Token |
| `--_typography---font-styles--heading` | `"Sohne Buch",Arial,sans-serif` | Typography Ink Token |
| `--_primitives---colors--neutral-darkest` | `black` | Canvas / Surface Token |
| `--_primitives---colors--white` | `#f4f2f1` | Canvas / Surface Token |
| `--color-scheme-1--text-secondary` | `var(--_primitives---colors--brown)` | Typography Ink Token |
| `--color-scheme-1--background-secondary` | `var(--_primitives---colors--dark)` | Canvas / Surface Token |
| `--color-scheme-1--text-white` | `var(--_primitives---colors--white)` | Canvas / Surface Token |
| `--color-scheme-1--background-brown` | `var(--_primitives---colors--brown)` | Canvas / Surface Token |
| `--_ui-styles---stroke--border-width` | `1px` | Layout / Spatial Grid Token |
| `--color-scheme-1--border` | `var(--_primitives---colors--brown)` | Brand / Palette Token |
| `--_ui-styles---radius--medium` | `0px` | Elevation / Border Token |
| `--color-scheme-1--foreground` | `var(--_primitives---colors--white)` | Typography Ink Token |
| `--_ui-styles---radius--small` | `0px` | Elevation / Border Token |
| `--_ui-styles---radius--large` | `0px` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.navbar> — `www-vanderhotel-com`)**:
   - Landmark `<header class="navbar">` hosting `Hotel & Restaurant Ljubljana · Vande` navigation (`Hotel · Food & Drink · meetings & Events · book now · journal`), DOM attributes (`data-wf-domain="www.vanderhotel.com"`, `data-wf-page="67f3b8c25d374ee9920d88c8"`, `data-wf-site="67f3b8c25d374ee9920d885b"`, `data-w-id="792db6bb-fe71-b745-03..."`), and stylesheet rule `.datepicker-container::after { border: 5px solid transparent; content: " "; display: block; height: 0;... }`.
2. **Hero Stage & Focal Lead (<section.section-2> — `where comfort meets culture`)**:
   - Landmark `<section class="section-2">` presenting display lead `where comfort meets culture` and copy excerpt *"Best price is guaranteed when booking directly! Choosing this opt"* over `#f4f2f1` canvas and `#353230` ink.
3. **Primary Showcase & Content Grid (<section.section-hero> — `wake up in`)**:
   - Landmark `<section class="section-hero">` rendering section `wake up in` with copy *"Our team is ready to help you plan your perfect stay. Feel free t"*, asset references (`cdn.prod.website-files.com`, `vander-hotel.webflow.shared.087c8...`, `vander-hotel.webflow.67f3b8c25d37...`, `1910953583635711`), and grid rule `.datepicker-inline { position: static; }`.
4. **Interactive Detail & Feature Matrix (<section.section-wake-up> — `vanderland`)**:
   - Landmark `<section class="section-wake-up">` framing `vanderland` and `experience` (*"Book online instead"*) with `#967850` surface cards, `#F3F5FB` accents, and `.datepicker-top-right { border-top-color: 39f; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.vanderhotel.com`)**:
   - Landmark `<footer class="footer">` anchoring `Hotel & Restaurant Ljubljana · V` footer links (`Hotel · Food & Drink · meetings & Events · book now · journal`), copy *"Experience a stylish, relaxed city break filled with comfort"*, and `#39f` structural dividers.
