# UI & UX Architecture: thecontenders-co

## Overview & Design Identity
- **Target**: `thecontenders-co` (**The Contenders · Strategic Brand & Design Consultancy**)
- **Production URL**: [https://thecontenders.co/](https://thecontenders.co/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#e40014` / `#f3f4f6`)
- **Summary**: Where business meets brand. The Contenders is an independent Australian consultancy creating distinctive brands that deliver measurable i...
- **Total Clean CSS Variables Extracted**: `130` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `DieGrotesk`
- **Body Font Stack**: `DieGrotesk Fallback`
- **Monospace / Technical Font Stack**: `iki-mono-variable`
- **Hero Display (`H1`)**: CSS variables `--heading-h1-font-family: var(--font-serif)`, `--heading-h1-font-size: 4rem`, `--heading-h1-font-weight: 400`
- **Section Heading (`H2`)**: CSS variables `--heading-h2-font-family: var(--font-serif)`, `--heading-h2-font-size: 3.5rem`, `--heading-h2-font-weight: 400`
- **Body Copy**: CSS variables `--body-l-font-family: var(--font-sans)`, `--body-l-font-size: 1.125rem`, `--body-l-font-weight: 400`
- **Metadata & Labels**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e40014` | `var(--color-red-600)` in `:root` |
| **Primary Typography Ink** | `#bf000f` | `var(--color-red-700)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f9fafb` | `var(--color-gray-50)` in `:root` |
| **Interactive Accent / Highlight** | `#f3f4f6` | `var(--color-gray-100)` in `:root` |
| **Secondary / Muted Copy** | `#e5e7eb` | `var(--color-gray-200)` in `:root` |
| **Structural Hairline Border** | `#d1d5dc` | `var(--color-gray-300)` in `:root` |
| **Variable Token (`--color-gray-400`)** | `#99a1af` | `var(--color-gray-400)` in `:root` |
| **Variable Token (`--color-gray-800`)** | `#1e2939` | `var(--color-gray-800)` in `:root` |
| **Variable Token (`--color-gray-900`)** | `#101828` | `var(--color-gray-900)` in `:root` |
| **Variable Token (`--color-gray-950`)** | `#030712` | `var(--color-gray-950)` in `:root` |
| **Variable Token (`--color-black`)** | `#000` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-white`)** | `#fff` | `var(--color-white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-die-grotesk` | `"DieGrotesk", "DieGrotesk Fallback"` | Typography / Scale Token |
| `--font-mesapholic` | `"Mesapholic", "Mesapholic Fallback"` | Typography / Scale Token |
| `--font-serif` | `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--color-red-600` | `#e40014` | Brand / Palette Token |
| `--color-red-700` | `#bf000f` | Brand / Palette Token |
| `--color-gray-50` | `#f9fafb` | Brand / Palette Token |
| `--color-gray-100` | `#f3f4f6` | Brand / Palette Token |
| `--color-gray-200` | `#e5e7eb` | Brand / Palette Token |
| `--color-gray-300` | `#d1d5dc` | Brand / Palette Token |
| `--color-gray-400` | `#99a1af` | Brand / Palette Token |
| `--color-gray-800` | `#1e2939` | Brand / Palette Token |
| `--color-gray-900` | `#101828` | Brand / Palette Token |
| `--color-gray-950` | `#030712` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.fixed> — `thecontenders-co`)**:
   - Landmark `<nav class="fixed z-50">` hosting `The Contenders · Strategic Brand & D` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-theme="white"`, `data-homepage="true"`, `data-lenis-prevent="true"`), and stylesheet rule `.WkV8yq_className { font-family:DieGrotesk,DieGrotesk Fallback }`.
2. **Hero Stage & Focal Lead (<section.homepage-intro-copy> — `THE CONTENDERS IS A CONSULTANCY WH`)**:
   - Landmark `<section class="homepage-intro-copy">` presenting display lead `THE CONTENDERS IS A CONSULTANCY WHERE BUSINESS ME...` and copy excerpt *"arrow_forward Newsletter sign up arrow_forward"* over `#e40014` canvas and `#f9fafb` ink.
3. **Primary Showcase & Content Grid (<section.homepage-intro-copy> — `THE CONTENDERS`)**:
   - Landmark `<section class="homepage-intro-copy">` rendering section `THE CONTENDERS` with copy *"Newsletter sign up"*, asset references (`Horizontal-3fa5268f-53f1-4223-a6c...`, `Compact-7923dd47-d322-4f23-802c-c...`, `00k7ot6zx_lfg.css`, `123l3rregymnq.js`), and grid rule `.WkV8yq_variable { --font-die-grotesk:"DieGrotesk", "DieGrotesk Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.homepage-intro-copy> — `Newsletter sign up`)**:
   - Landmark `<section class="homepage-intro-copy">` framing `Newsletter sign up` and `THE CONTENDERS IS A CONSULTANCY WHERE BUSINESS M` (*"THE CONTENDERS IS A CONSULTANCY WHERE BUSINESS MEETS BRAND."*) with `#f9fafb` surface cards, `#f3f4f6` accents, and `.HMGLSG_className { font-family:Mesapholic,Mesapholic Fallback }`.
5. **Colophon & Global Directory Footer (<footer.fixed> — `https://thecontenders.co/`)**:
   - Landmark `<footer class="fixed">` anchoring `The Contenders · Strategic Brand` footer links (`Overview · Index · Archive · About · Contact`), copy *"WE UNDERSTAND THAT YOUR ORGANISATION IS FIGHTING FOR SOMETHI"*, and `#d1d5dc` structural dividers.
