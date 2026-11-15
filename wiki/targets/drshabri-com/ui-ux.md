# UI & UX Architecture: drshabri-com

## Overview & Design Identity
- **Target**: `drshabri-com` (**Cosmetic Dentist & Facial Aesthetics, Marylebone**)
- **Production URL**: [https://drshabri.com/](https://drshabri.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ccc` canvas, `#555` ink, `#d9534f` accent)
- **Summary**: Cosmetic dentist and facial aesthetics in Marylebone and Beaconsfield. Dr Shabri treats the smile, skin and facial proportions as one con...
- **Total Clean CSS Variables Extracted**: `169` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Trustindex Poppins`
- **Body Font Stack**: `gravesend-sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `2.5em`, `100px`, `15px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `2.5em`, `100px`, `15px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `2.5em`, `100px`, `15px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ccc` | `var(--iti-border-gray)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--iti-input-bg-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#69727d` | `var(--iti-input-border-color)` in `:root` |
| **Interactive Accent / Highlight** | `#d9534f` | `var(--iti-input-invalid-color)` in `:root` |
| **Secondary / Muted Copy** | `#555` | `var(--iti-icon-color)` in `:root` |
| **Structural Hairline Border** | `#ffffff` | `var(--e-form-steps-indicator-active-secondary-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--flex-right` | `flex-start` | Design System Custom Token |
| `--justify-content` | `var(--flex-right,flex-end)` | Design System Custom Token |
| `--direction-multiplier` | `1` | Design System Custom Token |
| `--flex-direction` | `initial` | Design System Custom Token |
| `--flex-wrap` | `initial` | Layout / Spatial Grid Token |
| `--align-items` | `initial` | Design System Custom Token |
| `--align-content` | `initial` | Design System Custom Token |
| `--gap` | `initial` | Layout / Spatial Grid Token |
| `--flex-basis` | `initial` | Design System Custom Token |
| `--flex-grow` | `initial` | Design System Custom Token |
| `--flex-shrink` | `initial` | Typography Ink Token |
| `--order` | `initial` | Design System Custom Token |
| `--align-self` | `initial` | Design System Custom Token |
| `--page-title-display` | `block` | Design System Custom Token |
| `--border-radius` | `0` | Elevation / Border Token |
| `--border-top-width` | `0px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.elementor> — `drshabri-com`)**:
   - Landmark `<header class="elementor elementor-15">` hosting `Cosmetic Dentist & Facial Aesthetics` navigation (`DENTISTRY · Dental Consultation · Gum Contouring · Internal Bleaching · Teeth Whitening`), DOM attributes (`data-wpmeteor-nooptimize="true"`, `data-phast-no-defer`, `data-wpmeteor-nooptimize="true"`, `data-phast-ie-fallback-url="https://use.typekit.n..."`), and stylesheet rule `.elementor .e-div-block-base { min-width:30px;padding:10px;display:block; }`.
2. **Hero Stage & Focal Lead (<main.site-main> — `Cosmetic Dentistry`)**:
   - Landmark `<main class="site-main post-13">` presenting display lead `Cosmetic Dentistry` and copy excerpt *"DENTISTRY Cosmetic Dentistry Dental Consultation Dr Shabri Signat"* over `#ccc` canvas and `#555` ink.
3. **Primary Showcase & Content Grid (<main.site-main> — `General Dentistry`)**:
   - Landmark `<main class="site-main post-13">` rendering section `General Dentistry` with copy *"Dental Consultation"*, asset references (`www.googletagmanager.com`, `embed`, `header-footer.css`, `custom-frontend.min.css`), and grid rule `.elementor .e-flexbox-base { padding:10px;display:flex;flex-direction:row; }`.
4. **Interactive Detail & Feature Matrix (<main.site-main> — `Orthodontics`)**:
   - Landmark `<main class="site-main post-13">` framing `Orthodontics` and `Preventive Dentistry` (*"Dr Shabri Signature Harmonisation"*) with `#69727d` surface cards, `#d9534f` accents, and `.elementor .e-tabs-base { padding-block-start:0px;display:flex;flex-direction:column;gap:30px; }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://drshabri.com/`)**:
   - Landmark `<footer class="elementor elementor-314">` anchoring `Cosmetic Dentist & Facial Aesthe` footer links (`DENTISTRY · Dental Consultation · Gum Contouring · Internal Bleaching · Teeth Whitening`), copy *"Composite Bonding & Composite Veneers"*, and `#ffffff` structural dividers.
