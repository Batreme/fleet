# UI & UX Architecture: klad-design

## Overview & Design Identity
- **Target**: `klad-design` (**Multidisciplinary Design Syndicate – KLAD**)
- **Production URL**: [https://klad.design/](https://klad.design/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#010101` / `#0000`)
- **Summary**: Klad Syndicate is a multidisciplinary design studio offering comprehensive solutions for ambitious brands. Every design we deliver is ori...
- **Total Clean CSS Variables Extracted**: `68` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Helvetica Now Display`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-h1: 74px`, `--text-h1--line-height: 114%`, `--text-h1--letter-spacing: -.74px`
- **Section Heading (`H2`)**: CSS variables `--text-h2-md: 64px`, `--text-h2-md--line-height: 114%`, `--text-h2-md--letter-spacing: -.64px`; rule `h2` (`font-size: var(--text-p1)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-h1)`, `var(--text-h1-md)`)
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--text-h1--letter-spacing: -.74px`, `--text-h1-md--letter-spacing: -1.52px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#010101` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e6e6e6` | `var(--color-gray)` in `:root` |
| **Interactive Accent / Highlight** | `#0000` | `textarea { background-color: #0000 }` |
| **Secondary / Muted Copy** | `#000000` | `video { background-color: black }` (`#000000`) |
| **Structural Hairline Border** | `#808080` | `.case-close { color: gray }` (`#808080`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#010101` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--tracking-normal` | `0em` | Typography / Scale Token |
| `--blur-xs` | `4px` | Elevation / Border Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-gray` | `#e6e6e6` | Brand / Palette Token |
| `--font-helvetica` | `"Helvetica Now Display"` | Typography / Scale Token |
| `--text-normal` | `inherit` | Typography Ink Token |
| `--text-h1` | `74px` | Typography Ink Token |
| `--text-h1--line-height` | `114%` | Typography Ink Token |
| `--text-h1--letter-spacing` | `-.74px` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `klad-design`)**:
   - Landmark `<header class="site-header fixed">` hosting `Multidisciplinary Design Syndicate –` navigation (`About · Work · Process · Expectations · Pricing`), DOM attributes (`data-theme="light"`, `data-precedence="next"`, `data-page-noise="true"`, `data-active`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.transition-colors> — `Klad Syndicate Klad Syndicate Klad`)**:
   - Landmark `<section class="transition-colors">` presenting display lead `Klad Syndicate Klad Syndicate Klad Syndicate Klad...` and copy excerpt *"All Rights Reserved."* over `#010101` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.duration-200> — `Team 专责小组 Team 专责小组 Team 专责小组 Team`)**:
   - Landmark `<section class="duration-200">` rendering section `Team 专责小组 Team 专责小组 Team 专责小组 Team 专责小组 Team 专责小组...` with copy *"We are a multidisciplinary design syndicate offering comprehensiv"*, asset references (`logo-still.31i0fmdt_igcj.svg`, `world.39sfmav5iqip_.svg`, `1myj9p5-zqliw.css`, `0yigbjg0ha9p3.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.pt-20> — `Ksusha Ksusha Ksusha Ksusha Ksusha`)**:
   - Landmark `<section class="pt-20 z-1">` framing `Ksusha Ksusha Ksusha Ksusha Ksusha Ksusha` and `Lena S. Lena S. Lena S. Lena S. Lena S. Lena S.` (*"We actively avoid repeating ourselves. Our process may seem chaot"*) with `#e6e6e6` surface cards, `#0000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.absolute> — `https://klad.design/`)**:
   - Landmark `<footer class="absolute">` anchoring `Multidisciplinary Design Syndica` footer links (`About · Work · Process · Expectations · Pricing`), copy *"As a small team, we deliberately limit the number of project"*, and `#808080` structural dividers.
