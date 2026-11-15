# UI & UX Architecture: uimaven-art

## Overview & Design Identity
- **Target**: `uimaven-art` (**uimaven.art**)
- **Production URL**: [https://uimaven.art](https://uimaven.art)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#fb3748` / `#ffdb43`)
- **Summary**: UI/UX design portfolio of Leila Abbassova.
- **Total Clean CSS Variables Extracted**: `101` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Jost`
- **Body Font Stack**: `Jost Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-display: 64px`, `--text-display--line-height: .95`, `--text-display-phone: 40px`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-heading)`, `var(--text-heading-phone)`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--text-body: 16px`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fb3748` | `var(--color-red-100)` in `:root` |
| **Primary Typography Ink** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Elevated Surface / Card Substrate** | `#9f0712` | `var(--color-red-800)` in `:root` |
| **Interactive Accent / Highlight** | `#ffdb43` | `var(--color-yellow-100)` in `:root` |
| **Secondary / Muted Copy** | `#dfb400` | `var(--color-yellow-200)` in `:root` |
| **Structural Hairline Border** | `#edb200` | `var(--color-yellow-500)` in `:root` |
| **Variable Token (`--color-green-200`)** | `#1fc16b` | `var(--color-green-200)` in `:root` |
| **Variable Token (`--color-neutral-100`)** | `#fff` | `var(--color-neutral-100)` in `:root` |
| **Variable Token (`--color-neutral-200`)** | `#e8e8e8` | `var(--color-neutral-200)` in `:root` |
| **Variable Token (`--color-neutral-300`)** | `#d2d2d2` | `var(--color-neutral-300)` in `:root` |
| **Variable Token (`--color-black`)** | `#000` | `var(--color-black)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-jost` | `"Jost","Jost Fallback"` | Typography / Scale Token |
| `--type-weight` | `initial` | Typography / Scale Token |
| `--color-red-100` | `#fb3748` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-red-800` | `#9f0712` | Brand / Palette Token |
| `--color-yellow-100` | `#ffdb43` | Brand / Palette Token |
| `--color-yellow-200` | `#dfb400` | Brand / Palette Token |
| `--color-yellow-500` | `#edb200` | Brand / Palette Token |
| `--color-green-200` | `#1fc16b` | Brand / Palette Token |
| `--color-neutral-100` | `#fff` | Brand / Palette Token |
| `--color-neutral-200` | `#e8e8e8` | Brand / Palette Token |
| `--color-neutral-300` | `#d2d2d2` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.relative> — `uimaven-art`)**:
   - Landmark `<header class="relative shrink-0">` hosting `uimaven.art` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-home`), and stylesheet rule `jost_bd43172b-module__QzW_JW__cla... { font-family:Jost,Jost Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<main.mobile-stripes> — `uimaven.art`)**:
   - Landmark `<main class="mobile-stripes bg-primary-300">` presenting display lead `uimaven.art` and copy excerpt *"UI/UX design portfolio of Leila Abbassova."* over `#fb3748` canvas and `#ffdb43` ink.
3. **Primary Showcase & Content Grid (<main.mobile-stripes> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="mobile-stripes bg-primary-300">` rendering section `Featured Work & Interactive Showcase` with copy *"uimaven.art"*, asset references (`81cef6a21128489e-s.p.6cf41120.woff2`, `d7f27077a988d3d1.css`, `e48a17b7f69aeb46.js`, `2677990b2b1206f6.js`), and grid rule `.jost_bd43172b-module__QzW_JW__va... { --font-jost:"Jost","Jost Fallback" }`.
4. **Interactive Detail & Feature Matrix (<main.mobile-stripes> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="mobile-stripes bg-primary-300">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#9f0712` surface cards, `#ffdb43` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.bg-primary-300> — `https://uimaven.art`)**:
   - Landmark `<footer class="bg-primary-300">` anchoring `uimaven.art` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#edb200` structural dividers.
