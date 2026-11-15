# UI & UX Architecture: www-1centre-com

## Overview & Design Identity
- **Target**: `www-1centre-com` (**1Centre — Trade Credit Software for NZ & Australia**)
- **Production URL**: [https://www.1centre.com/](https://www.1centre.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f99c00` / `#fff`)
- **Summary**: Trade credit software for suppliers in New Zealand and Australia: digital account applications, ID checks, credit decisions, 24/7 monitor...
- **Total Clean CSS Variables Extracted**: `87` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `15.5px`, `13.5px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `15.5px`, `13.5px`)
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f99c00` | `var(--color-amber-500)` in `:root` |
| **Primary Typography Ink** | `#b75000` | `var(--color-amber-700)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `var(--color-white)` in `:root` |
| **Secondary / Muted Copy** | `#fafbfa` | `var(--color-canvas)` in `:root` |
| **Structural Hairline Border** | `#101112` | `var(--color-ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dot-r` | `0px` | Dimension / Scale Token |
| `--qc-r` | `60%` | Dimension / Scale Token |
| `--qc-r2` | `70%` | Dimension / Scale Token |
| `--font-sans` | `var(--font-inter), ui-sans-serif, system-ui, -apple-system, sans-serif` | Typography / Scale Token |
| `--font-serif` | `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--color-amber-500` | `#f99c00` | Brand / Palette Token |
| `--color-amber-700` | `#b75000` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-4xl` | `2.25rem` | Typography Ink Token |
| `--text-4xl--line-height` | `calc(2.5 / 2.25)` | Typography Ink Token |
| `--text-5xl` | `3rem` | Typography Ink Token |
| `--text-5xl--line-height` | `1` | Typography Ink Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sticky> — `www-1centre-com`)**:
   - Landmark `<header class="sticky top-0">` hosting `1Centre — Trade Credit Software for ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-nimg="1"`, `data-dark="true"`), and stylesheet rule `host { --color-amber-500:lab(72.7183% 31.8672 97.9407);--color-amber-700:lab(47... }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Trade credit at scale, so you can `)**:
   - Landmark `<section class="relative overflow-hidden">` presenting display lead `Trade credit at scale, so you can focus on sales.` and copy excerpt *"Trade credit at scale,"* over `#f99c00` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.group> — `Build trade credit workflows on ev`)**:
   - Landmark `<section class="group border-y">` rendering section `Build trade credit workflows on everything your b...` with copy *"so you can focus on sales."*, asset references (`5e4d537aaa9e154b-s.p.0g9-.3zp53cu...`, `83afe278b6a6bb3c-s.p.0q-301v4kxxn...`, `logo-mark.svg`, `mitre10.svg`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.mx-auto> — `Open trade accounts from the count`)**:
   - Landmark `<section class="mx-auto scroll-mt-20">` framing `Open trade accounts from the counter, the web, yo...` and `Write your own credit rules — and let them decide...` (*"1Centre helps businesses across all industries trade with trust. "*) with `#000` surface cards, `#fff` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.1centre.com/`)**:
   - Landmark `<footer class="relative overflow-hidden">` anchoring `1Centre — Trade Credit Software ` footer links (`Overview · Index · Archive · About · Contact`), copy *"1Centre helps businesses across all industries"*, and `#101112` structural dividers.
