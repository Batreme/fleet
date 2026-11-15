# UI & UX Architecture: thebranx-com

## Overview & Design Identity
- **Target**: `thebranx-com` (**The branding agency for startups, AI & SaaS - The Branx**)
- **Production URL**: [https://thebranx.com](https://thebranx.com)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff085` canvas, `#4a5565` ink, `#f9fafb` accent)
- **Summary**: The Branx builds category-defining brands and websites for AI, SaaS and B2B tech startups: strategy, identity, web design and motion, fro...
- **Total Clean CSS Variables Extracted**: `191` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Marcellus`
- **Body Font Stack**: `Marcellus Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: var(--bx-fs-display)`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-6xl: 3.75rem`; rule `h1` (`font-size: var(--bx-fs-statement)`, `line-height: var(--bx-lh-statement)`)
- **Section Heading (`H2`)**: CSS variables `--text-3xl: var(--bx-fs-h2)`, `--text-3xl--line-height: calc(2.25 / 1.875)`, `--bx-fs-h2: clamp(32px, 3.6vw, 72px)`; rule `h2` (`font-size: var(--text-xl)`)
- **Body Copy**: CSS variables `--leading-body: var(--bx-lh-body)`, `--bx-fs-body: 16px`, `--bx-lh-body: 1.6`; rule `p` (`font-size: var(--bx-fs-lead)`, `line-height: var(--bx-lh-body)`)
- **Metadata & Labels**: CSS variables `--font-mono: var(--bx-mono)`, `--text-xs: 14px`, `--text-sm: var(--bx-fs-small)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff085` | `var(--color-yellow-200)` in `:root` |
| **Primary Typography Ink** | `#3080ff` | `var(--color-blue-500)` in `:root` |
| **Elevated Surface / Card Substrate** | `#155dfc` | `var(--color-blue-600)` in `:root` |
| **Interactive Accent / Highlight** | `#f9fafb` | `var(--color-gray-50)` in `:root` |
| **Secondary / Muted Copy** | `#4a5565` | `var(--color-gray-600)` in `:root` |
| **Structural Hairline Border** | `#fff` | `var(--color-white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-marcellus` | `"Marcellus", "Marcellus Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--bx-sans)` | Typography / Scale Token |
| `--font-mono` | `var(--bx-mono)` | Typography / Scale Token |
| `--color-yellow-200` | `#fff085` | Brand / Palette Token |
| `--color-blue-500` | `#3080ff` | Brand / Palette Token |
| `--color-blue-600` | `#155dfc` | Brand / Palette Token |
| `--color-gray-50` | `#f9fafb` | Brand / Palette Token |
| `--color-gray-600` | `#4a5565` | Brand / Palette Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `14px` | Typography Ink Token |
| `--text-sm` | `var(--bx-fs-small)` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-lg` | `var(--bx-fs-lead)` | Typography Ink Token |
| `--text-xl` | `var(--bx-fs-card)` | Typography Ink Token |
| `--text-3xl` | `var(--bx-fs-h2)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bx-navbar> — `thebranx-com`)**:
   - Landmark `<header class="bx-navbar">` hosting `The branding agency for startups, AI` navigation (`Brand identity · Web design & dev. · Strategy & messaging · Motion design · Product naming`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-ch2css="true"`, `data-bx-nav`), and stylesheet rule `llus_b0edf5b9-module__eeLBqG__cla... { font-family:Marcellus,Marcellus Fallback;font-style:normal;font-weight:400 }`.
2. **Hero Stage & Focal Lead (<section.bx-hero> — `The tech branding agency for AI & `)**:
   - Landmark `<section class="bx-hero">` presenting display lead `The tech branding agency for AI & SaaS startups` and copy excerpt *"Strategy & messaging"* over `#fff085` canvas and `#4a5565` ink.
3. **Primary Showcase & Content Grid (<section.bx-section> — `The Branx turns complex tech into `)**:
   - Landmark `<section class="bx-section">` rendering section `The Branx turns complex tech into category-defini...` with copy *"The tech branding agency"*, asset references (`ec2f4458eb06f74e-s.p.217u6tza6bra...`, `0u5m-o-ck0mfs.css`, `3rz2zp8k1t-b-.css`, `194ug3jq7qzm9.js`), and grid rule `ellus_b0edf5b9-module__eeLBqG__va... { --font-marcellus:"Marcellus", "Marcellus Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.bx-philosophy> — `AI made it easy to launch a brand.`)**:
   - Landmark `<section class="bx-philosophy">` framing `AI made it easy to launch a brand. It made it har...` and `Start with the identity. Add the rest when you're...` (*"for AI & SaaS startups"*) with `#155dfc` surface cards, `#f9fafb` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.bx-footer> — `https://thebranx.com`)**:
   - Landmark `<footer class="bx-footer">` anchoring `The branding agency for startups` footer links (`Brand identity · Web design & dev. · Strategy & messaging · Motion design · Product naming`), copy *"Video intelligence for the real world"*, and `#fff` structural dividers.
