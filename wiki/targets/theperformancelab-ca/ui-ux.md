# UI & UX Architecture: theperformancelab-ca

## Overview & Design Identity
- **Target**: `theperformancelab-ca` (**The Performance Lab — Sports Science & Athletic Testing in Toronto**)
- **Production URL**: [https://theperformancelab.ca/](https://theperformancelab.ca/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#292929` accent)
- **Summary**: The Performance Lab is a Toronto sports science centre offering 3D motion-capture testing, performance training, and sports therapy — tru...
- **Total Clean CSS Variables Extracted**: `37` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `display`
- **Body Font Stack**: `display Fallback`
- **Monospace / Technical Font Stack**: `mono`
- **Hero Display (`H1`)**: CSS variables `--font-display-family: "display","display Fallback"`, `--font-display: var(--font-display)`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.75rem`, `.875rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.75rem`, `.875rem`)
- **Metadata & Labels**: CSS variables `--font-mono-family: "mono","mono Fallback"`, `--font-mono: var(--font-mono)`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#727272` | `var(--color-neutral-grey-01)` in `:root` |
| **Interactive Accent / Highlight** | `#292929` | `var(--color-neutral-grey-03)` in `:root` |
| **Secondary / Muted Copy** | `#0000` | `textarea { background-color: #0000 }` |
| **Structural Hairline Border** | `#ffffff` | `15 { background-color: white }` (`#ffffff`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-display-family` | `"display","display Fallback"` | Typography / Scale Token |
| `--font-mono-family` | `"mono","mono Fallback"` | Typography / Scale Token |
| `--font-diatype-family` | `"diatype","diatype Fallback"` | Typography / Scale Token |
| `--font-mono` | `var(--font-mono)` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--ease-in` | `cubic-bezier(.4,0,1,1)` | Motion / Easing Token |
| `--ease-out` | `cubic-bezier(0,0,.2,1)` | Motion / Easing Token |
| `--ease-in-out` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--blur-sm` | `8px` | Elevation / Border Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `theperformancelab-ca`)**:
   - Landmark `<header class="fixed inset-x-0">` hosting `The Performance Lab — Sports Science` navigation (`H O M E · W H O W E A R E · B L O G · C O N T A C T`), DOM attributes (`data-precedence="next"`, `data-theme="dark"`, `data-services-open="false"`, `data-scroll-state="false"`), and stylesheet rule `.__className_9dcdb7 { font-family:display,display Fallback }`.
2. **Hero Stage & Focal Lead (<section.mx-auto> — `UNLOCK NEXT LEVEL PERFORMANCE`)**:
   - Landmark `<section class="mx-auto relative">` presenting display lead `UNLOCK NEXT LEVEL PERFORMANCE` and copy excerpt *"B O O K A C O N S U L T A T I O N"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.hidden> — `Helping you move better, recover s`)**:
   - Landmark `<section class="hidden relative">` rendering section `Helping you move better, recover smarter, and per...` with copy *"Everything your body needs to perform, recover, and last."*, asset references (`desktop.jpg`, `i1.webp`, `i2.webp`, `i3.webp`), and grid rule `.__variable_9dcdb7 { --font-display-family:"display","display Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.mx-auto> — `Reach your goals. Whether you’re p`)**:
   - Landmark `<section class="mx-auto relative">` framing `Reach your goals. Whether you’re pursuing profess...` and `#1 Sports science centre IN Canada` (*"BOOK A CONSULTATION"*) with `#727272` surface cards, `#292929` accents, and `.__className_ac1fe6 { font-family:mono,mono Fallback;font-weight:400;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.mx-auto> — `https://theperformancelab.ca/`)**:
   - Landmark `<footer class="mx-auto flex">` anchoring `The Performance Lab — Sports Sci` footer links (`H O M E · W H O W E A R E · B L O G · C O N T A C T`), copy *"info@myperformancelab.com"*, and `#ffffff` structural dividers.
