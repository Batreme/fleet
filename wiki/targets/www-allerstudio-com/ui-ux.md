# UI & UX Architecture: www-allerstudio-com

## Overview & Design Identity
- **Target**: `www-allerstudio-com` (**ALLER Studio — Product design and development studio**)
- **Production URL**: [https://www.allerstudio.com/](https://www.allerstudio.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#646aed`)
- **Summary**: Product design and development studio for Web3, AI, fintech, and gaming.
- **Total Clean CSS Variables Extracted**: `78` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-5xl: 3rem`, `--text-5xl--line-height: 1`, `--font-display: var(--font-rajdhani), "Arial Narrow", sans-serif`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--color-text-subtitle: #4e5964`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d5fe00` | `var(--color-lime)` in `:root` |
| **Interactive Accent / Highlight** | `#646aed` | `var(--color-violet)` in `:root` |
| **Secondary / Muted Copy** | `#fc4b08` | `var(--color-orange)` in `:root` |
| **Structural Hairline Border** | `#121212` | `var(--color-dark-950)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ease-out` | `cubic-bezier(.16, 1, .3, 1)` | Motion / Easing Token |
| `--ease-in-out` | `cubic-bezier(.37, 0, .63, 1)` | Motion / Easing Token |
| `--active` | `0` | Design System Custom Token |
| `--font-inter` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-rajdhani` | `"Rajdhani", "Rajdhani Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-inter), "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5 / 1)` | Typography Ink Token |
| `--text-lg` | `1.125rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header-in> — `www-allerstudio-com`)**:
   - Landmark `<header class="header-in fixed">` hosting `ALLER Studio — Product design and de` navigation (`Services · Case Studies · Studio · Insights · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `._3N0scq_board { width:954px;height:594px;transform:scale(var(--s,1));transform-origin:0... }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Product design and development stu`)**:
   - Landmark `<section class="relative pt-40">` presenting display lead `Product design and development studio for Web3, A...` and copy excerpt *"Lima · 10:44 AM UTC-5"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Technology can be complex. The exp`)**:
   - Landmark `<section class="relative px-4">` rendering section `Technology can be complex. The experience should...` with copy *"Fully booked · Next slot Q1 2027"*, asset references (`3206eb66b875a5b3-s.p.3gjg6tthudz5...`, `83afe278b6a6bb3c-s.p.45535valc9rz...`, `a079e02bba5bf7ab-s.p.2yv0x3fl1lx-...`, `a10c617c9026098c-s.p.1a-q6cj6za4e...`), and grid rule `._3N0scq_svg { pointer-events:none;position:absolute;inset:0;overflow:visible }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Complex flows`)**:
   - Landmark `<section class="relative px-4">` framing `Complex flows` and `Low user trust` (*"· Next slot Q1 2027"*) with `#d5fe00` surface cards, `#646aed` accents, and `._3N0scq_progress { stroke-dasharray:1 1;stroke-dashoffset:1px;opacity:1;transition:stroke-d... }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.allerstudio.com/`)**:
   - Landmark `<footer class="relative z-42">` anchoring `ALLER Studio — Product design an` footer links (`Services · Case Studies · Studio · Insights · Contact`), copy *"NYC · 10:44 AM UTC-5"*, and `#121212` structural dividers.
