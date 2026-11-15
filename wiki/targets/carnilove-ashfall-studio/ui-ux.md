# UI & UX Architecture: carnilove-ashfall-studio

## Overview & Design Identity
- **Target**: `carnilove-ashfall-studio` (**Carnilove · Home**)
- **Production URL**: [https://carnilove.ashfall.studio/](https://carnilove.ashfall.studio/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#f6e1ce`)
- **Summary**: Rotate your device to portrait mode.
- **Total Clean CSS Variables Extracted**: `103` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `SparkCL`
- **Body Font Stack**: `TTBluescreens`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-h1: 16rem`, `--text-h1--line-height: 80%`, `--text-h1-mobile: 6.4rem`
- **Section Heading (`H2`)**: CSS variables `--text-h2: 10.8rem`, `--text-h2--line-height: 81%`, `--text-h2-mobile: 5rem`; rule `h2` (`font-size: var(--text-h4-mobile)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: calc(var(--tracking-t...`)
- **Body Copy**: CSS variables `--font-body: "Matter",sans-serif`, `--text-body-l: 1.7rem`, `--text-body-l--line-height: 190%`; rule `p` (`font-size: var(--text-body-s)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: calc(var(--tracking-t...`)
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--text-label: 1.4rem`, `--text-label--line-height: 100%`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#4a002a` | `var(--color-purple-dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#74003d` | `var(--color-purple-light)` in `:root` |
| **Interactive Accent / Highlight** | `#f6e1ce` | `var(--color-beige-dark)` in `:root` |
| **Secondary / Muted Copy** | `#fff3e4` | `var(--color-beige-light)` in `:root` |
| **Structural Hairline Border** | `#f00037` | `var(--color-red-light)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#000` | Canvas / Surface Token |
| `--spacing` | `.1rem` | Layout / Spatial Grid Token |
| `--breakpoint-xl` | `64.5rem` | Dimension / Scale Token |
| `--text-xl` | `26rem` | Typography Ink Token |
| `--text-xl--line-height` | `80%` | Typography Ink Token |
| `--tracking-tight` | `.01em` | Typography / Scale Token |
| `--ease-out` | `cubic-bezier(.23,1,.32,1)` | Motion / Easing Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--font-body` | `"Matter",sans-serif` | Typography / Scale Token |
| `--font-heading` | `"TTBluescreens",sans-serif` | Typography Ink Token |
| `--font-spark` | `"SparkCL",sans-serif` | Typography / Scale Token |
| `--font-multilingual` | `"NotoSans",sans-serif` | Typography / Scale Token |
| `--font-multilingual-bold` | `"NotoSansCondensed",sans-serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `carnilove-ashfall-studio`)**:
   - Landmark `<header class="header fixed">` hosting `Carnilove · Home` navigation (`Mission · Ambassadors · Blog · Contact · Dry Food`), DOM attributes (`data-astro-cid-sckkx6r4`, `data-src="https://images.ctfass..."`, `data-srcset="https://images.ctfass..."`, `data-sizes="100vw"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.dropdown-el> — `P U R E P R E S E N C E I N M O T `)**:
   - Landmark `<section class="dropdown-el flex">` presenting display lead `P U R E P R E S E N C E I N M O T I O N PURE PRES...` and copy excerpt *"Bosnia and Herzegovina de"* over `#000` canvas and `#fff3e4` ink.
3. **Primary Showcase & Content Grid (<section.dropdown-el> — `S H A R P E N E D B Y N A T U R A `)**:
   - Landmark `<section class="dropdown-el flex">` rendering section `S H A R P E N E D B Y N A T U R A L E N E R G Y S...` with copy *"T R U S T T H E I R"*, asset references (`apple-touch-icon-57x57.png`, `apple-touch-icon-60x60.png`, `apple-touch-icon-72x72.png`, `apple-touch-icon-76x76.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.dropdown-el> — `f r e e t o b e f i e r c e l y a `)**:
   - Landmark `<section class="dropdown-el flex">` framing `f r e e t o b e f i e r c e l y a l i v e free to...` and `TRUST THEIRINSTINCT` (*"TRUST THEIRINSTINCT"*) with `#74003d` surface cards, `#f6e1ce` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://carnilove.ashfall.studio/`)**:
   - Landmark `<footer class="footer flex">` anchoring `Carnilove · Home` footer links (`Mission · Ambassadors · Blog · Contact · Dry Food`), copy *"Real food that respects who they are — and who they’ve alway"*, and `#f00037` structural dividers.
