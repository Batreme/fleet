# UI & UX Architecture: namaha-healthcare

## Overview & Design Identity
- **Target**: `namaha-healthcare` (**Namaha Healthcare**)
- **Production URL**: [https://namaha.healthcare](https://namaha.healthcare)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000000` ink, `#0000` accent)
- **Summary**: With over seventy years in healthcare, the Kapadia family has nurtured a legacy built on trust, compassion, and clinical integrity.
- **Total Clean CSS Variables Extracted**: `0` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Victorserif 50`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `.slick-loading .slick-list { background: #fff }` |
| **Primary Typography Ink** | `#ffffff` | `.slick-next:before { color: white }` (`#ffffff`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.slick-dots li.slick-active but... { color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#0000` | `a { background-color: #0000 }` |
| **Secondary / Muted Copy** | `#000` | `mark { color: #000 }` |
| **Structural Hairline Border** | `#ff0` | `mark { background: #ff0 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--namaha-healthcar-bg` | `#fff` | Canvas Substrate (from `.slick-loading .slick-list { background: #fff }`) |
| `--namaha-healthcar-ink` | `#000000` | Primary Typography Ink (stylesheet-derived) |
| `--namaha-healthcar-surface` | `#000000` | Surface Substrate (stylesheet-derived) |
| `--namaha-healthcar-accent` | `#0000` | Interactive Accent (stylesheet-derived) |
| `--namaha-healthcar-muted` | `#000` | Secondary Ink (stylesheet-derived) |
| `--namaha-healthcar-border` | `#ff0` | Structural Border (stylesheet-derived) |
| `--namaha-healthcar-container` | `940px` | Container Bound (stylesheet-derived) |
| `--namaha-healthcar-gap` | `7px` | Grid Gutter (stylesheet-derived) |
| `--namaha-healthcar-pad` | `5px` | Lateral Padding (stylesheet-derived) |
| `--namaha-healthcar-ease` | `cubic-bezier(.645,.045,.355,1)` | Primary Easing Function |
| `--namaha-healthcar-radius` | `3px` | Corner Radius (stylesheet-derived) |
| `--namaha-healthcar-fs-base` | `20px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `namaha-healthcare`)**:
   - Landmark `<header class="w-mod-js">` hosting `Namaha Healthcare` navigation (`1 Our Philosophy · 2 Our Team · 3 Departments · 5 Our Facilities · 6 Guides`), DOM attributes (`data-wf-domain="www.namaha.healthcare"`, `data-wf-page="68949db83756970449601627"`, `data-wf-site="68949db8375697044960161c"`, `data-w-id="2086974e-b9c8-7268-e0..."`), and stylesheet rule `.slick-loading .slick-list { background: fff url('./ajax-loader.gif') center center no-repeat; }`.
2. **Hero Stage & Focal Lead (<section.headersection> — `S e v e n d e c a d e s o f s e r `)**:
   - Landmark `<section class="headersection scrolled-over">` presenting display lead `S e v e n d e c a d e s o f s e r v i c e i n h e...` and copy excerpt *"4 Specialised healthcare for women"* over `#fff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.header> — `B e c a u s e t h e i r h e a l t `)**:
   - Landmark `<section class="header">` rendering section `B e c a u s e t h e i r h e a l t h s h a p e s g...` with copy *"Your well-being matters to us. We are here to assist you with car"*, asset references (`cdn.prod.website-files.com`, `namaha-v2.webflow.shared.a69184c8...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `.slick-next:focus { color: transparent; outline: none; background: transparent; }`.
4. **Interactive Detail & Feature Matrix (<section.hero_section> — `Specialty Departments`)**:
   - Landmark `<section class="hero_section gsapherosection">` framing `Specialty Departments` and `P i o n e e r s i n R o b o t i c K n e e R e p l...` (*"CALL TO BOOK (+91 22) 6123 6123"*) with `#000000` surface cards, `#0000` accents, and `.slick-next:focus:before { opacity: 1; }`.
5. **Colophon & Global Directory Footer (<footer.wf-geist-n6-active> — `https://namaha.healthcare`)**:
   - Landmark `<footer class="wf-geist-n6-active">` anchoring `Namaha Healthcare` footer links (`1 Our Philosophy · 2 Our Team · 3 Departments · 5 Our Facilities · 6 Guides`), copy *"Call us Our lines are available 24/7. Reach out to us to get"*, and `#ff0` structural dividers.
