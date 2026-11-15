# UI & UX Architecture: altamedfoundation-org

## Overview & Design Identity
- **Target**: `altamedfoundation-org` (**AltaMed Foundation · AltaMed Foundation**)
- **Production URL**: [https://altamedfoundation.org/](https://altamedfoundation.org/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#fb2c36` canvas, `#f9fafb` ink, `#155dfc` accent)
- **Summary**: AltaMed ensures everyone in our community has access to quality health care, enabling them to live healthy, happy lives.
- **Total Clean CSS Variables Extracted**: `175` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `proxima-nova`
- **Body Font Stack**: `gotham-xnarrow`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`
- **Section Heading (`H2`)**: CSS variables `--text-3xl: 1.875rem`, `--text-3xl--line-height: calc(2.25 / 1.875)`, `--text-title-lg: 34px`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--font-size-body: 18px`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Primary Typography Ink** | `#bf000f` | `var(--color-red-700)` in `:root` |
| **Elevated Surface / Card Substrate** | `#3080ff` | `var(--color-blue-500)` in `:root` |
| **Interactive Accent / Highlight** | `#155dfc` | `var(--color-blue-600)` in `:root` |
| **Secondary / Muted Copy** | `#f9fafb` | `var(--color-gray-50)` in `:root` |
| **Structural Hairline Border** | `#f3f4f6` | `var(--color-gray-100)` in `:root` |
| **Variable Token (`--color-gray-200`)** | `#e5e7eb` | `var(--color-gray-200)` in `:root` |
| **Variable Token (`--color-gray-300`)** | `#d1d5db` | `var(--color-gray-300)` in `:root` |
| **Variable Token (`--color-gray-400`)** | `#9ca3af` | `var(--color-gray-400)` in `:root` |
| **Variable Token (`--color-gray-500`)** | `#6b7280` | `var(--color-gray-500)` in `:root` |
| **Variable Token (`--color-gray-600`)** | `#5e5668` | `var(--color-gray-600)` in `:root` |
| **Variable Token (`--color-gray-700`)** | `#374151` | `var(--color-gray-700)` in `:root` |
| **Variable Token (`--color-gray-800`)** | `#1f2937` | `var(--color-gray-800)` in `:root` |
| **Variable Token (`--color-gray-900`)** | `#242029` | `var(--color-gray-900)` in `:root` |
| **Variable Token (`--color-black`)** | `#000` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-white`)** | `#fff` | `var(--color-white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-red-700` | `#bf000f` | Brand / Palette Token |
| `--color-blue-500` | `#3080ff` | Brand / Palette Token |
| `--color-blue-600` | `#155dfc` | Brand / Palette Token |
| `--color-gray-50` | `#f9fafb` | Brand / Palette Token |
| `--color-gray-100` | `#f3f4f6` | Brand / Palette Token |
| `--color-gray-200` | `#e5e7eb` | Brand / Palette Token |
| `--color-gray-300` | `#d1d5db` | Brand / Palette Token |
| `--color-gray-400` | `#9ca3af` | Brand / Palette Token |
| `--color-gray-500` | `#6b7280` | Brand / Palette Token |
| `--color-gray-600` | `#5e5668` | Brand / Palette Token |
| `--color-gray-700` | `#374151` | Brand / Palette Token |
| `--color-gray-800` | `#1f2937` | Brand / Palette Token |
| `--color-gray-900` | `#242029` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.relative> — `altamedfoundation-org`)**:
   - Landmark `<header class="relative z-50">` hosting `AltaMed Foundation · AltaMed Foundat` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-scroll-behavior="smooth"`, `data-precedence="next"`, `data-href="/_next/static/immutab..."`, `data-nimg="1"`), and stylesheet rule `.tk-proxima-nova { font-family: "proxima-nova",sans-serif; }`.
2. **Hero Stage & Focal Lead (<section.bg-white> — `H.E.L.P. Campaign`)**:
   - Landmark `<section class="bg-white py-12">` presenting display lead `H.E.L.P. Campaign` and copy excerpt *"AltaMed ensures everyone in our community has access to quality h"* over `#fb2c36` canvas and `#f9fafb` ink.
3. **Primary Showcase & Content Grid (<section.scroll-mt-24> — `Impact Stories`)**:
   - Landmark `<section class="scroll-mt-24 bg-purple">` rendering section `Impact Stories` with copy *"Health. Equity. Life. Programs."*, asset references (`vdqo9h3n.api.sanity.io`, `altamed-foundation-logo.svg`, `3kc4s5-t1h7ps.js`, `1h6ujiewnnn1_.js`), and grid rule `.tk-gotham-xnarrow { font-family: "gotham-xnarrow",sans-serif; }`.
4. **Interactive Detail & Feature Matrix (<section.scroll-mt-24> — `Homeward Bound: Preemie Twins’ Inc`)**:
   - Landmark `<section class="scroll-mt-24 bg-white">` framing `Homeward Bound: Preemie Twins’ Incredible Journey...` and `Make a Difference` (*"Learn More about the H.E.L.P. Campaign"*) with `#3080ff` surface cards, `#155dfc` accents, and `.tk-gotham-narrow { font-family: "gotham-narrow",sans-serif; }`.
5. **Colophon & Global Directory Footer (<footer.bg-white> — `https://altamedfoundation.org/`)**:
   - Landmark `<footer class="bg-white pt-8">` anchoring `AltaMed Foundation · AltaMed Fou` footer links (`Overview · Index · Archive · About · Contact`), copy *"about the H.E.L.P. Campaign"*, and `#f3f4f6` structural dividers.
