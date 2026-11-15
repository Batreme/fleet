# UI & UX Architecture: tabletales-crz-studio

## Overview & Design Identity
- **Target**: `tabletales-crz-studio` (**Table Tales by CRZ.STUDIO · Board Game Collection & Play Log**)
- **Production URL**: [https://tabletales.crz.studio/](https://tabletales.crz.studio/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#08335d` / `#c98f2e`)
- **Summary**: Table Tales is a digital exhibition of board games as art: a curated collection and a living log of every night at the table. Designed an...
- **Total Clean CSS Variables Extracted**: `45` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `grotesk`
- **Body Font Stack**: `grotesk Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-display: "display", "display Fallback"`
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(56px,5.6vw,120px)`, `line-height: .92`, `letter-spacing: 0`, `font-weight: 400`)
- **Body Copy**: CSS variables `--text-body: clamp(16px, 1.25vw, 20px)`; rule `p` (`font-size: var(--text-body)`, `line-height: 1.35`)
- **Metadata & Labels**: CSS variables `--text-label: clamp(12px, .9vw, 14px)`, `--text-small: clamp(14px, 1.04vw, 16px)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#08335d` | `var(--color-blue)` in `:root` |
| **Primary Typography Ink** | `#f7b538` | `var(--color-golden)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fdffff` | `var(--color-azure)` in `:root` |
| **Interactive Accent / Highlight** | `#c98f2e` | `var(--color-ochre)` in `:root` |
| **Secondary / Muted Copy** | `#145a86` | `var(--color-teal)` in `:root` |
| **Structural Hairline Border** | `#010e1c` | `var(--color-night)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-blue` | `#08335d` | Brand / Palette Token |
| `--color-golden` | `#f7b538` | Brand / Palette Token |
| `--color-azure` | `#fdffff` | Brand / Palette Token |
| `--color-ochre` | `#c98f2e` | Brand / Palette Token |
| `--color-teal` | `#145a86` | Brand / Palette Token |
| `--color-night` | `#010e1c` | Brand / Palette Token |
| `--color-line-on-light` | `color-mix(in srgb, var(--color-blue) 22%, transparent)` | Canvas / Surface Token |
| `--color-line-on-dark` | `color-mix(in srgb, var(--color-azure) 22%, transparent)` | Canvas / Surface Token |
| `--color-muted-on-light` | `color-mix(in srgb, var(--color-blue) 62%, transparent)` | Canvas / Surface Token |
| `--color-muted-on-dark` | `color-mix(in srgb, var(--color-azure) 62%, transparent)` | Canvas / Surface Token |
| `--section-padding-inline` | `clamp(20px, 2.78vw, 64px)` | Layout / Spatial Grid Token |
| `--section-padding-block` | `clamp(72px, 8.33vw, 160px)` | Layout / Spatial Grid Token |
| `--measure-padding` | `clamp(0px, 18vw, 420px)` | Layout / Spatial Grid Token |
| `--space-2xs` | `4px` | Layout / Spatial Grid Token |
| `--space-xs` | `8px` | Layout / Spatial Grid Token |
| `--space-s` | `clamp(12px, 1.11vw, 16px)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.LYh_OG_variable> — `tabletales-crz-studio`)**:
   - Landmark `<header class="LYh_OG_variable">` hosting `Table Tales by CRZ.STUDIO · Board Ga` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `.YZMoQq_card:focus-visible { z-index:1;outline:2px solid var(--color-golden);outline-offset:-6px }`.
2. **Hero Stage & Focal Lead (<section.q_m67W_hero> — `T a b l e T a l e s`)**:
   - Landmark `<section class="q_m67W_hero">` presenting display lead `T a b l e T a l e s` and copy excerpt *"I n s t a g r a m I n s t a g r a m"* over `#08335d` canvas and `#fdffff` ink.
3. **Primary Showcase & Content Grid (<section.uxasZq_variable> — `Featured Games`)**:
   - Landmark `<section class="uxasZq_variable">` rendering section `Featured Games` with copy *"L i n k e d I n L i n k e d I n"*, asset references (`FoundersGrotesk_Bold-s.p.2z72oy2q...`, `FoundersGrotesk_BoldItalic-s.p.2h...`, `FoundersGrotesk_Light-s.p.03ydj7u...`, `FoundersGrotesk_LightItalic-s.p.2...`), and grid rule `.YZMoQq_paint { transform-origin:top;pointer-events:none;will-change:transform;position:... }`.
4. **Interactive Detail & Feature Matrix (<section.O43udq_featured> — `The play log`)**:
   - Landmark `<section class="O43udq_featured">` framing `The play log` and `C R Z . S T U D I O C R Z . S T U D I O` (*"C R Z . S T U D I O C R Z . S T U D I O"*) with `#fdffff` surface cards, `#c98f2e` accents, and `.YZMoQq_paint:first-child { background:var(--color-golden) }`.
5. **Colophon & Global Directory Footer (<footer.tUdqrq_footer> — `https://tabletales.crz.studio/`)**:
   - Landmark `<footer class="tUdqrq_footer">` anchoring `Table Tales by CRZ.STUDIO · Boar` footer links (`Overview · Index · Archive · About · Contact`), copy *"C R Z . S T U D I O"*, and `#010e1c` structural dividers.
