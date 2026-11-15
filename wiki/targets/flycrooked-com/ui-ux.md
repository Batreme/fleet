# UI & UX Architecture: flycrooked-com

## Overview & Design Identity
- **Target**: `flycrooked-com` (**Crow · Trip planner and flight finder for iPhone**)
- **Production URL**: [https://flycrooked.com/](https://flycrooked.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#17181c`)
- **Summary**: Your iPhone travel companion. Plan a trip, compare flight routes, track delays and gate changes, and carry a blunt local guide when you l...
- **Total Clean CSS Variables Extracted**: `86` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `display`
- **Body Font Stack**: `display Fallback`
- **Monospace / Technical Font Stack**: `mono`
- **Hero Display (`H1`)**: CSS variables `--font-display: "display","display Fallback"`, `--display: var(--font-display),"Arial Narrow",Arial,sans-serif`; rule `h1` (`font-size: 88px`, `line-height: .94`, `letter-spacing: 0`, `font-weight: 700`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 46px`, `line-height: 1.05`, `letter-spacing: 0`, `font-weight: 600`)
- **Body Copy**: CSS variables `--font-body: "body","body Fallback"`, `--body: var(--font-body),-apple-system,"Segoe UI",sans-serif`; rule `p` (`font-size: 16px`, `line-height: 1.75`)
- **Metadata & Labels**: CSS variables `--font-mono: "mono"`, `--default-mono-font-family: var(--font-mono)`, `--mono: var(--font-mono),ui-monospace,"SF Mono",Menlo,monospace`; rule `small` (`font-size: 11.5px`, `letter-spacing: .08em`, `font-weight: 500`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#eceff3` | `var(--concourse)` in `:root` |
| **Interactive Accent / Highlight** | `#17181c` | `var(--sign-black)` in `:root` |
| **Secondary / Muted Copy** | `#1c1e24` | `var(--panel-black)` in `:root` |
| **Structural Hairline Border** | `#ff3d81` | `var(--accent)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-display` | `"display","display Fallback"` | Typography / Scale Token |
| `--font-mono` | `"mono"` | Typography / Scale Token |
| `--font-body` | `"body","body Fallback"` | Typography / Scale Token |
| `--font-wordmark` | `"wordmark"` | Typography / Scale Token |
| `--color-neutral-100` | `oklch(97% 0 0)` | Brand / Palette Token |
| `--color-neutral-200` | `oklch(92.2% 0 0)` | Brand / Palette Token |
| `--color-neutral-300` | `oklch(87% 0 0)` | Brand / Palette Token |
| `--color-neutral-400` | `oklch(70.8% 0 0)` | Brand / Palette Token |
| `--color-neutral-800` | `oklch(26.9% 0 0)` | Brand / Palette Token |
| `--color-neutral-900` | `oklch(20.5% 0 0)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--tracking-wide` | `.025em` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `flycrooked-com`)**:
   - Landmark `<header class="nav">` hosting `Crow · Trip planner and flight finde` navigation (`Guides · How it works · Support · Privacy · Terms`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="story-fonts"`, `data-precedence="story-fonts"`), and stylesheet rule `.__className_2063d3 { font-family:display,display Fallback }`.
2. **Hero Stage & Focal Lead (<section.stage> — `Marrakech`)**:
   - Landmark `<section class="stage">` presenting display lead `Marrakech` and copy excerpt *"First slot of the day. The blue walls, before the coaches."* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.stage> — `Trip wires`)**:
   - Landmark `<section class="stage">` rendering section `Trip wires` with copy *"Timed entry · 08:00"*, asset references (`06ac09dcb8ec7d56.p.woff2`, `4224042929936d69-s.p.woff2`, `422bb7078d9b61dc.p.woff2`, `532b6dda9c49d302-s.p.woff2`), and grid rule `.__variable_2063d3 { --font-display:"display","display Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.stage> — `What Changed`)**:
   - Landmark `<section class="stage">` framing `What Changed` and `WATCHES` (*"In before the tour groups walk over from the square."*) with `#eceff3` surface cards, `#17181c` accents, and `.__className_c3828f { font-family:mono }`.
5. **Colophon & Global Directory Footer (<footer.sfoot> — `https://flycrooked.com/`)**:
   - Landmark `<footer class="sfoot">` anchoring `Crow · Trip planner and flight f` footer links (`Guides · How it works · Support · Privacy · Terms`), copy *"Lose the map. Crow saved the way back offline."*, and `#ff3d81` structural dividers.
