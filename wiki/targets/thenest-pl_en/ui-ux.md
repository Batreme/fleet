# UI & UX Architecture: thenest-pl_en

## Overview & Design Identity
- **Target**: `thenest-pl_en` (**The Nest — a registered business address in central Warsaw**)
- **Production URL**: [https://thenest.pl/en](https://thenest.pl/en)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#eef0ea` canvas, `#04191c` ink, `#ffe2e2` accent)
- **Summary**: Register your Polish company at Piękna 49 in central Warsaw. Virtual office from 109 PLN/mo net, private offices quoted individually, mai...
- **Total Clean CSS Variables Extracted**: `138` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Bodoni Moda`
- **Body Font Stack**: `Bodoni Moda Fallback`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: CSS variables `--font-display: "Bodoni Moda", "Bodoni Moda Fallback"`, `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#eef0ea` | `var(--rd-ivory)` in `:root` |
| **Primary Typography Ink** | `#04191c` | `var(--rd-deep)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fef2f2` | `var(--color-red-50)` in `:root` |
| **Interactive Accent / Highlight** | `#ffe2e2` | `var(--color-red-100)` in `:root` |
| **Secondary / Muted Copy** | `#ffa3a3` | `var(--color-red-300)` in `:root` |
| **Structural Hairline Border** | `#ff6568` | `var(--color-red-400)` in `:root` |
| **Variable Token (`--rd-rule`)** | `#003a4024` | `var(--rd-rule)` in `:root` |
| **Variable Token (`--rd-rule-strong`)** | `#003a4047` | `var(--rd-rule-strong)` in `:root` |
| **Variable Token (`--rd-rule-invert`)** | `#e9ebe62e` | `var(--rd-rule-invert)` in `:root` |
| **Variable Token (`--rd-rule-invert-strong`)** | `#e9ebe657` | `var(--rd-rule-invert-strong)` in `:root` |
| **Variable Token (`--rd-ivory-dim`)** | `#eef0ead1` | `var(--rd-ivory-dim)` in `:root` |
| **Variable Token (`--rd-ivory-faint`)** | `#eef0ea99` | `var(--rd-ivory-faint)` in `:root` |
| **Variable Token (`--color-red-500`)** | `#fb2c36` | `var(--color-red-500)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--rd-rule` | `#003a4024` | Color / Atmospheric Token |
| `--rd-rule-strong` | `#003a4047` | Color / Atmospheric Token |
| `--rd-rule-invert` | `#e9ebe62e` | Color / Atmospheric Token |
| `--rd-rule-invert-strong` | `#e9ebe657` | Color / Atmospheric Token |
| `--rd-ivory` | `#eef0ea` | Color / Atmospheric Token |
| `--rd-ivory-dim` | `#eef0ead1` | Color / Atmospheric Token |
| `--rd-ivory-faint` | `#eef0ea99` | Color / Atmospheric Token |
| `--rd-deep` | `#04191c` | Color / Atmospheric Token |
| `--rd-container` | `1200px` | Layout / Spatial Grid Token |
| `--font-display` | `"Bodoni Moda", "Bodoni Moda Fallback"` | Typography / Scale Token |
| `--font-serif` | `ui-serif,Georgia,Cambria,"Times New Roman",Times,serif` | Typography / Scale Token |
| `--color-red-50` | `#fef2f2` | Brand / Palette Token |
| `--color-red-100` | `#ffe2e2` | Brand / Palette Token |
| `--color-red-300` | `#ffa3a3` | Brand / Palette Token |
| `--color-red-400` | `#ff6568` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `thenest-pl_en`)**:
   - Landmark `<header class="fixed top-0">` hosting `The Nest — a registered business add` navigation (`About Us · Offers · News & Insights · FAQ · Contact`), DOM attributes (`data-scroll-behavior="smooth"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.rd-serif { font-family:var(--font-display), "Iowan Old Style", Palatino, Georgia, s... }`.
2. **Hero Stage & Focal Lead (<section.relative> — `A Warsaw business address for your`)**:
   - Landmark `<section class="relative overflow-hidden">` presenting display lead `A Warsaw business address for your company. Piękn...` and copy excerpt *"Skip to main content"* over `#eef0ea` canvas and `#04191c` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Register your company at a real ad`)**:
   - Landmark `<section class="relative overflow-hidden">` rendering section `Register your company at a real address.` with copy *"Register your company"*, asset references (`7665c2bcc9077b83-s.p.3nqaju0iyo2m...`, `cd9c266256ef2177-s.p.0ia0bwd-fjee...`, `thenest-logo-white.svg`, `2qf24jap9hfz0.css`), and grid rule `.rd-rule { border-color:var(--rd-rule) }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Everything under one address. Offi`)**:
   - Landmark `<section class="relative overflow-hidden">` framing `Everything under one address. Office , mail , roo...` and `Office to rent — once you outgrow the virtual office` (*"at a real address."*) with `#fef2f2` surface cards, `#ffe2e2` accents, and `.rd-rule-strong { border-color:var(--rd-rule-strong) }`.
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://thenest.pl/en`)**:
   - Landmark `<footer class="border-t border-border">` anchoring `The Nest — a registered business` footer links (`About Us · Offers · News & Insights · FAQ · Contact`), copy *"An address at Piękna 49 for your KRS or CEIDG registration —"*, and `#ff6568` structural dividers.
