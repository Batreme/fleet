# UI & UX Architecture: pda-archi_en

## Overview & Design Identity
- **Target**: `pda-archi_en` (**Architecture firm in Paris: renovation, refurbishment — PDA**)
- **Production URL**: [https://pda.archi/en](https://pda.archi/en)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#30363c` accent)
- **Summary**: PDA, Partners & Dalous Architecture, transforms office, hospitality and residential buildings in Paris: renovation, refurbishment, vertic...
- **Total Clean CSS Variables Extracted**: `133` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `SequelSans`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `100%`, `1.05em`, `.9em`, `.82em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--text-24)`, `line-height: var(--spacing-full)`, `font-weight: var(--font-we...`)
- **Body Copy**: CSS variables `--font-body: "SequelSans",sans-serif`; rule `p` (`font-size: var(--text-17)`, `line-height: 110%`, `font-weight: var(--font-we...`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1.33333`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--cc-bg)` in `:root` |
| **Primary Typography Ink** | `#2c2f31` | `var(--cc-primary-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#5e6266` | `var(--cc-secondary-color)` in `:root` |
| **Interactive Accent / Highlight** | `#30363c` | `var(--cc-btn-primary-bg)` in `:root` |
| **Secondary / Muted Copy** | `#000` | `var(--cc-btn-primary-hover-bg)` in `:root` |
| **Structural Hairline Border** | `#eaeff2` | `var(--cc-btn-secondary-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cc-modal-border-radius` | `.5rem` | Elevation / Border Token |
| `--cc-btn-border-radius` | `.4rem` | Elevation / Border Token |
| `--cc-modal-transition-duration` | `.25s` | Motion / Easing Token |
| `--cc-link-color` | `var(--cc-btn-primary-bg)` | Typography Ink Token |
| `--cc-modal-margin` | `1rem` | Layout / Spatial Grid Token |
| `--cc-z-index` | `2147483647` | Elevation / Border Token |
| `--cc-bg` | `#fff` | Canvas / Surface Token |
| `--cc-primary-color` | `#2c2f31` | Brand / Palette Token |
| `--cc-secondary-color` | `#5e6266` | Brand / Palette Token |
| `--cc-btn-primary-bg` | `#30363c` | Canvas / Surface Token |
| `--cc-btn-primary-color` | `#fff` | Brand / Palette Token |
| `--cc-btn-primary-border-color` | `var(--cc-btn-primary-bg)` | Brand / Palette Token |
| `--cc-btn-primary-hover-bg` | `#000` | Canvas / Surface Token |
| `--cc-btn-primary-hover-color` | `#fff` | Brand / Palette Token |
| `--cc-btn-primary-hover-border-color` | `var(--cc-btn-primary-hover-bg)` | Brand / Palette Token |
| `--cc-btn-secondary-bg` | `#eaeff2` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `pda-archi_en`)**:
   - Landmark `<header class="header fixed">` hosting `Architecture firm in Paris: renovati` navigation (`Projects · Expertise · Studio · Team · Digital Lab`), DOM attributes (`data-dark`, `data-block="aboutBlock"`, `data-src="https://pub-4eb76b4c2..."`, `data-block="featuredProjectsBlock"`), and stylesheet rule `cc-main span { all:unset;box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.relative> — `PDA, Partners & Dalous Architectur`)**:
   - Landmark `<section class="relative w-full">` presenting display lead `PDA, Partners & Dalous Architecture, an architect...` and copy excerpt *"Refurbish rather than"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `49 Champs-Élysées`)**:
   - Landmark `<section class="relative grid-w">` rendering section `49 Champs-Élysées` with copy *"Transform uses, keep the"*, asset references (`DmkCsKWL.js`, `DlrsJN3k.js`, `BEzBqhAX.js`, `C3NQ9IW_.js`), and grid rule `cc-main button { all:initial;box-sizing:border-box;color:unset;visibility:unset }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `68 Faubourg Saint-Honoré`)**:
   - Landmark `<section class="relative mt-68">` framing `68 Faubourg Saint-Honoré` and `118 Champs-Élysées` (*"Build where the city is"*) with `#5e6266` surface cards, `#30363c` accents, and `cc-main tr { all:revert;color:inherit;font-family:inherit;font-size:inherit;font-weig... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://pda.archi/en`)**:
   - Landmark `<footer class="footer bg-black">` anchoring `Architecture firm in Paris: reno` footer links (`Projects · Expertise · Studio · Team · Digital Lab`), copy *"5 avenue de l'Opéra 75001 Paris"*, and `#eaeff2` structural dividers.
