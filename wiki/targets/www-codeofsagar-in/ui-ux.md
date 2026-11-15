# UI & UX Architecture: www-codeofsagar-in

## Overview & Design Identity
- **Target**: `www-codeofsagar-in` (**Sagar K. Ghosh — Full-stack Developer & Designer**)
- **Production URL**: [https://www.codeofsagar.in/](https://www.codeofsagar.in/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#171717` / `#0f0f0f`)
- **Summary**: Websites and stores that sell, 3D people remember and automation that gives your team its time back, designed and built by Sagar K. Ghosh.
- **Total Clean CSS Variables Extracted**: `126` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `spaceGrotesk`
- **Body Font Stack**: `spaceGrotesk Fallback`
- **Monospace / Technical Font Stack**: `spaceMono`
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-space-grotesk), ui-sans-serif, system-ui, sans-serif`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-lg)`, `var(--text-xs)`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-lg)`, `var(--text-xs)`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#171717` | `var(--color-neutral-900)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--color-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Interactive Accent / Highlight** | `#0f0f0f` | `var(--theme-black-olive)` in `:root` |
| **Secondary / Muted Copy** | `#eb5e28` | `var(--theme-burnt-orange)` in `:root` |
| **Structural Hairline Border** | `#262626` | `var(--ink-soft)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-neutral-900` | `#171717` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-lg` | `1.125rem` | Typography Ink Token |
| `--text-lg--line-height` | `calc(1.75 / 1.125)` | Typography Ink Token |
| `--text-7xl` | `4.5rem` | Typography Ink Token |
| `--text-7xl--line-height` | `1` | Typography Ink Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--tracking-tight` | `-.025em` | Typography / Scale Token |
| `--tracking-wide` | `.025em` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.NavBar-module__aMivtW__bar> — `www-codeofsagar-in`)**:
   - Landmark `<header class="NavBar-module__aMivtW__bar">` hosting `Sagar K. Ghosh — Full-stack Develope` navigation (`H H o o m m e e · W W o o r r k k · A A b b o o u u t t · F F A A Q Q`), DOM attributes (`data-nav-solid`, `data-lines-anim`, `data-sky="day"`, `data-dot="small"`), and stylesheet rule `host { --color-neutral-900:lab(7.78201% -.0000149012 0) }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Websites that sell. AI that never `)**:
   - Landmark `<section class="relative z-10">` presenting display lead `Websites that sell. AI that never sleeps.` and copy excerpt *"S S e e r r v v i i c c e e s s"* over `#171717` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.grain-surface> — `S A G A R K . G H O S H`)**:
   - Landmark `<section class="grain-surface home-titles">` rendering section `S A G A R K . G H O S H` with copy *"A A b b o o u u t t"*, asset references (`space_grotesk_latin_wght_normal-s...`, `space_mono_latin_400_normal-s.p.1...`, `space_mono_latin_700_normal-s.p.0...`, `36s0t0o8ux5as.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.font-grotesk> — `Get Found. Get Chosen. Get Bought.`)**:
   - Landmark `<section class="font-grotesk">` framing `Get Found. Get Chosen. Get Bought.` and `What clients say` (*"P P l l a a y y g g r r o o u u n n d d"*) with `#fff` surface cards, `#0f0f0f` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.codeofsagar.in/`)**:
   - Landmark `<footer class="relative flex">` anchoring `Sagar K. Ghosh — Full-stack Deve` footer links (`H H o o m m e e · W W o o r r k k · A A b b o o u u t t · F F A A Q Q`), copy *"C C o o n n t t a a c c t t"*, and `#262626` structural dividers.
