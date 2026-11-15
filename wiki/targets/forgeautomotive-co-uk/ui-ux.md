# UI & UX Architecture: forgeautomotive-co-uk

## Overview & Design Identity
- **Target**: `forgeautomotive-co-uk` (**Bespoke Vehicle Builds & Styling · Forge Automotive**)
- **Production URL**: [https://forgeautomotive.co.uk/](https://forgeautomotive.co.uk/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#ffffff` accent)
- **Summary**: A luxury automotive atelier for bespoke styling, performance and craftsmanship — one-off Defender, G63, Range Rover, Urus and 911 builds.
- **Total Clean CSS Variables Extracted**: `20` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `GeistSans`
- **Body Font Stack**: `GeistSans Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `62.5%`, `68.75%`, `75%`, `1.4rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `62.5%`, `68.75%`, `75%`, `1.4rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `62.5%`, `68.75%`, `75%`, `1.4rem`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `62.5%`, `68.75%`, `75%`, `1.4rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | `#page:after { background: black }` (`#000000`) |
| **Primary Typography Ink** | `#ffffff` | `::selection { color: white }` (`#ffffff`) |
| **Elevated Surface / Card Substrate** | `#0c0c0c` | `<meta name="theme-color" content="#0c0c0c">` in `dom.html` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--page-beat-dur` | `1.2s` | Motion / Timing Token |
| `--page-leave-dur` | `var(--page-beat-dur)` | Design System Custom Token |
| `--page-enter-dur` | `var(--page-beat-dur)` | Design System Custom Token |
| `--page-enter-ease` | `cubic-bezier(.2, .7, .2, 1)` | Motion / Easing Token |
| `--black` | `var(--global-black)` | Canvas / Surface Token |
| `--white` | `var(--global-white)` | Canvas / Surface Token |
| `--bezzy` | `var(--easing-bezzy)` | Design System Custom Token |
| `--bezzy2` | `var(--easing-bezzy2)` | Design System Custom Token |
| `--bezzy3` | `var(--easing-bezzy3)` | Design System Custom Token |
| `--next-build-dur` | `1.2s` | Motion / Timing Token |
| `--next-build-ease` | `cubic-bezier(.7, .05, .13, 1)` | Motion / Easing Token |
| `--font-geist-sans` | `"GeistSans", "GeistSans Fallback"` | Typography / Scale Token |
| `--editorial` | `"editorial", "editorial Fallback"` | Design System Custom Token |
| `--lqip-mobile` | `url("data:image/jpeg` | Design System Custom Token |
| `--play-state` | `paused` | Design System Custom Token |
| `--fill-to` | `rgb(255, 255, 255)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sc-337305d3-0> — `forgeautomotive-co-uk`)**:
   - Landmark `<header class="sc-337305d3-0 sc-cf9722b1-0">` hosting `Bespoke Vehicle Builds & Styling · F` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-styled="active"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.sc-337305d3-0> — `We don’t modify vehicles We build `)**:
   - Landmark `<section class="sc-337305d3-0 sc-2b039258-0">` presenting display lead `We don’t modify vehicles We build them for you` and copy excerpt *"Bespoke vehicles built on distinction, desire, and identity. not "* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.sc-337305d3-0> — `For Those Who Refuse Ordinary`)**:
   - Landmark `<section class="sc-337305d3-0 sc-12ea9db1-0">` rendering section `For Those Who Refuse Ordinary` with copy *"A luxury automotive atelier for bespoke styling, performance and "*, asset references (`2fdd_lc5jd195.css`, `19rhlcx2srev9.css`, `2cf1_565uvy1t.css`, `431bw722fec3m.js`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.sc-337305d3-0> — `Our Approach To Every Build`)**:
   - Landmark `<section class="sc-337305d3-0 sc-e85696e3-0">` framing `Our Approach To Every Build` and `Identity` (*"Every decision is intentional, every detail has purpose based on "*) with `#0c0c0c` surface cards, `#ffffff` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.sc-337305d3-0> — `https://forgeautomotive.co.uk/`)**:
   - Landmark `<footer class="sc-337305d3-0 sc-a2c8839e-0">` anchoring `Bespoke Vehicle Builds & Styling` footer links (`Overview · Index · Archive · About · Contact`), copy *"S t a r t Y o u r P r o j e c t"*, and `#ffffff` structural dividers.
