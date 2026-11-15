# UI & UX Architecture: kingriver-com-au

## Overview & Design Identity
- **Target**: `kingriver-com-au` (**Australian Wagyu Beef · King River Legendary Wagyu**)
- **Production URL**: [https://kingriver.com.au/](https://kingriver.com.au/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f6ede8` / `#e5240a`)
- **Summary**: Explore the exquisite taste of King River Australian Wagyu beef and its unique quality that sets it apart in the culinary world.
- **Total Clean CSS Variables Extracted**: `51` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `feijoa`
- **Body Font Stack**: `sweet-sans-pro`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `14px`)
- **Section Heading (`H2`)**: rule `,h2` (`font-size: 1.375rem`, `font-weight: 700`)
- **Body Copy**: rule `p` (`font-size: .75rem`, `line-height: 2`, `letter-spacing: .05em`, `font-weight: 700`)
- **Metadata & Labels**: CSS variables `--chain-meta: 1rem`, `--chain-meta-gap: 1.25rem`, `--chain-caption-gap: 0px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f6ede8` | `var(--button-base)` in `:root` |
| **Primary Typography Ink** | `#3b1013` | `var(--button-ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#7d1a1c` | `var(--marker-color)` in `:root` |
| **Interactive Accent / Highlight** | `#e5240a` | `var(--marker-active-color)` in `:root` |
| **Secondary / Muted Copy** | `#551115` | `var(--beef-background)` in `:root` |
| **Structural Hairline Border** | `#f2e5de` | `var(--field-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--button-base` | `#f6ede8` | Color / Atmospheric Token |
| `--button-ink` | `#3b1013` | Typography Ink Token |
| `--button-fill` | `#f6ede8` | Color / Atmospheric Token |
| `--marker-size` | `12px` | Layout / Spatial Grid Token |
| `--marker-active-size` | `18px` | Layout / Spatial Grid Token |
| `--marker-color` | `#7d1a1c` | Brand / Palette Token |
| `--marker-active-color` | `#e5240a` | Brand / Palette Token |
| `--button-ease` | `cubic-bezier(0.33,1,0.68,1)` | Motion / Easing Token |
| `--button-sweep` | `0.34s` | Motion / Timing Token |
| `--pill-ease` | `cubic-bezier(0.33,1,0.68,1)` | Motion / Easing Token |
| `--jewel-slide-gap` | `1rem` | Layout / Spatial Grid Token |
| `--jewel-slide-size` | `82%` | Layout / Spatial Grid Token |
| `--beef-background` | `#551115` | Canvas / Surface Token |
| `--card-ease` | `cubic-bezier(0.33,1,0.68,1)` | Motion / Easing Token |
| `--row-ease` | `cubic-bezier(0.33,1,0.68,1)` | Motion / Easing Token |
| `--card-bg` | `#f6ede8` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `kingriver-com-au`)**:
   - Landmark `<header class="fixed top-0">` hosting `Australian Wagyu Beef · King River L` navigation (`Our Properties · Our Story · Our Beef · Jewel · Partners`), DOM attributes (`data-template="base.twig"`, `data-transition`, `data-transition-shade`, `data-transition-panel`), and stylesheet rule `before { border:0 solid e5e7eb;box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.remove-section-padding> — `King River`)**:
   - Landmark `<section class="remove-section-padding relative">` presenting display lead `King River` and copy excerpt *"King River Australian Wagyu"* over `#f6ede8` canvas and `#3b1013` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `From our family to yours.`)**:
   - Landmark `<section class="relative bg-maroon-dark">` rendering section `From our family to yours.` with copy *"Queensland, Australia"*, asset references (`clarity.js`, `yxd9a243r4`, `gtm.js`, `humans.txt`), and grid rule `body { line-height:inherit;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<section.home> — `RED LABEL`)**:
   - Landmark `<section class="home">` framing `RED LABEL` and `KING RIVER` (*"Fifth-generation Australian Wagyu"*) with `#7d1a1c` surface cards, `#e5240a` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.overflow-hidden> — `https://kingriver.com.au/`)**:
   - Landmark `<footer class="overflow-hidden bg-maroon-dark">` anchoring `Australian Wagyu Beef · King Riv` footer links (`Our Properties · Our Story · Our Beef · Jewel · Partners`), copy *"King River is a fifth-generation family business producing A"*, and `#f2e5de` structural dividers.
