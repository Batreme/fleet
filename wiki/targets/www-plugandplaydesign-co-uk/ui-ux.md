# UI & UX Architecture: www-plugandplaydesign-co-uk

## Overview & Design Identity
- **Target**: `www-plugandplaydesign-co-uk` (**Web Design Agency London & Guildford · Plug & Play**)
- **Production URL**: [https://www.plugandplaydesign.co.uk/](https://www.plugandplaydesign.co.uk/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#c40806` canvas, `#fff` ink, `#000` accent)
- **Summary**: Award-winning web design agency in London and Guildford. High-performance websites and digital retainers that drive measurable growth.
- **Total Clean CSS Variables Extracted**: `380` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Mono`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: var(--text-body-sm)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--text-body-sm)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`)
- **Body Copy**: CSS variables `--text-body-sm: .875rem`, `--text-body-sm--line-height: 1.4`, `--text-body-sm--letter-spacing: -.02em`
- **Metadata & Labels**: CSS variables `--font-mono: "Geist Mono",ui-monospace,"SF Mono",Menlo,monospace`, `--default-mono-font-family: var(--font-mono)`, `--color-media-caption: #0006`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#c40806` | `var(--color-red-600)` in `:root` |
| **Primary Typography Ink** | `#5f58ff` | `var(--color-purple-600)` in `:root` |
| **Elevated Surface / Card Substrate** | `#4b23cd` | `var(--color-purple-700)` in `:root` |
| **Interactive Accent / Highlight** | `#000` | `var(--color-black)` in `:root` |
| **Secondary / Muted Copy** | `#fff` | `var(--color-white)` in `:root` |
| **Structural Hairline Border** | `#fafafa` | `var(--color-grey-50)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Geist","Helvetica Neue",Arial,sans-serif` | Typography / Scale Token |
| `--font-mono` | `"Geist Mono",ui-monospace,"SF Mono",Menlo,monospace` | Typography / Scale Token |
| `--color-red-600` | `#c40806` | Brand / Palette Token |
| `--color-purple-600` | `#5f58ff` | Brand / Palette Token |
| `--color-purple-700` | `#4b23cd` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--radius-xs` | `.125rem` | Elevation / Border Token |
| `--radius-sm` | `.25rem` | Elevation / Border Token |
| `--radius-md` | `.5rem` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `www-plugandplaydesign-co-uk`)**:
   - Landmark `<header class="fixed inset-x-0">` hosting `Web Design Agency London & Guildford` navigation (`Our Work · Web Design · Branding · Digital Marketing · UX / UI Design`), DOM attributes (`data-hero-enter`, `data-precedence="next"`, `data-precedence="next"`, `data-domain="plugandplaydesign.co.uk"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.px-page> — `Web Design Agency in London and Su`)**:
   - Landmark `<section class="px-page pt-section">` presenting display lead `Web Design Agency in London and Surrey` and copy excerpt *"Plug and Play is a creative web design agency based in Guildford,"* over `#c40806` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.bg-background> — `Our process`)**:
   - Landmark `<section class="bg-background px-page">` rendering section `Our process` with copy *"digital transformation"*, asset references (`ca4cfa437ae45d18.css`, `dd5d352a082118c1.css`, `webpack-43624c9fe997cbf4.js`, `cf303062-0b72e54636065547.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.w-screen> — `What types of websites do we build`)**:
   - Landmark `<section class="w-screen">` framing `What types of websites do we build?` and `What industries do you work with?` (*"(via its enterprise site,"*) with `#4b23cd` surface cards, `#000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.bg-background> — `https://www.plugandplaydesign.co.uk/`)**:
   - Landmark `<footer class="bg-background px-page">` anchoring `Web Design Agency London & Guild` footer links (`Our Work · Web Design · Branding · Digital Marketing · UX / UI Design`), copy *"digital marketing strategy"*, and `#fafafa` structural dividers.
