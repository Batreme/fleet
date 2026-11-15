# UI & UX Architecture: residences-loamhouse-com-au

## Overview & Design Identity
- **Target**: `residences-loamhouse-com-au` (**Loam House — Sandringham**)
- **Production URL**: [https://residences.loamhouse.com.au](https://residences.loamhouse.com.au)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#1e211d` canvas, `#fbfaf6` ink, `#8d4f36` accent)
- **Summary**: Loam House — house-sized residences in Sandringham. Final release now selling.
- **Total Clean CSS Variables Extracted**: `17` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `DM Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(76px,8.5vw,138px)`, `line-height: .74`, `letter-spacing: -.045em`, `font-weight: 300`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(52px,8vw,120px)`, `line-height: .9`, `letter-spacing: -.02em`, `font-weight: 400`)
- **Body Copy**: rule `p` (`font-size: clamp(15px,1.3vw,19px)`, `line-height: 1.6`, `font-weight: 300`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `9.5px`, `11px`, `6.5px`, `5.5px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#1e211d` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#f1eee7` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fbfaf6` | `var(--chalk)` in `:root` |
| **Interactive Accent / Highlight** | `#8d4f36` | `var(--clay)` in `:root` |
| **Secondary / Muted Copy** | `#626852` | `var(--olive)` in `:root` |
| **Structural Hairline Border** | `#2c3128` | `.blabel { fill: #2c3128 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#1e211d` | Typography Ink Token |
| `--paper` | `#f1eee7` | Canvas / Surface Token |
| `--chalk` | `#fbfaf6` | Color / Atmospheric Token |
| `--clay` | `#8d4f36` | Color / Atmospheric Token |
| `--olive` | `#626852` | Color / Atmospheric Token |
| `--line` | `rgba(30,33,29,.18)` | Color / Atmospheric Token |
| `--serif` | `"Cormorant Garamond",Georgia,serif` | Typography / Scale Token |
| `--hero-serif` | `"Cormorant Garamond",Georgia,serif` | Typography / Scale Token |
| `--sans` | `"DM Sans",Arial,sans-serif` | Typography / Scale Token |
| `--hgut` | `6vw` | Dimension / Scale Token |
| `--scan` | `.2` | Design System Custom Token |
| `--mob-pos` | `36% center` | Dimension / Scale Token |
| `--pulse-period` | `4.1s` | Motion / Timing Token |
| `--ping-scale` | `4.2` | Design System Custom Token |
| `--ping-op` | `0.36` | Design System Custom Token |
| `--num-op` | `1` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `residences-loamhouse-com-au`)**:
   - Landmark `<header class="site-header">` hosting `Loam House — Sandringham` navigation (`Proposition · Size · Storage · Finishes · Precinct`), DOM attributes (`data-preloader`, `data-pl-pct`, `data-header`, `data-open-calendly`), and stylesheet rule `stage { position:absolute;inset:0;overflow:hidden }`.
2. **Hero Stage & Focal Lead (<section.hero> — `House-sized. Bayside living.`)**:
   - Landmark `<section class="hero chapter">` presenting display lead `House-sized. Bayside living.` and copy excerpt *"Download the brochure Brochure"* over `#1e211d` canvas and `#fbfaf6` ink.
3. **Primary Showcase & Content Grid (<section.form-chapter> — `Leave the upkeep. Keep the life.`)**:
   - Landmark `<section class="form-chapter chapter">` rendering section `Leave the upkeep. Keep the life.` with copy *"Download the brochure"*, asset references (`clientParamBuilder.bundle.js`, `clarity.js`, `yed6eroa3m`, `1440095636442948`), and grid rule `map { position:absolute;inset:0;width:100%;height:100%;display:block;touch-act... }`.
4. **Interactive Detail & Feature Matrix (<section.cine> — `A backyard oasis, without the mowi`)**:
   - Landmark `<section class="cine chapter">` framing `A backyard oasis, without the mowing.` and `Everything you need. Nothing you don’t.` (*"Book an appointment Appointment"*) with `#fbfaf6` surface cards, `#8d4f36` accents, and `.station circle { fill:fff;stroke:40453b;stroke-width:1;pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.pl-panels> — `https://residences.loamhouse.com.au`)**:
   - Landmark `<footer class="pl-panels">` anchoring `Loam House — Sandringham` footer links (`Proposition · Size · Storage · Finishes · Precinct`), copy *"Book an appointment"*, and `#2c3128` structural dividers.
