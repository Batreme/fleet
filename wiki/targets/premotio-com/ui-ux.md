# UI & UX Architecture: premotio-com

## Overview & Design Identity
- **Target**: `premotio-com` (**premotio — finished design into polished motion**)
- **Production URL**: [https://premotio.com/](https://premotio.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5f5f7` / `#000000`)
- **Summary**: premotio turns finished design into polished motion without sending you into a video editor. Pick a preset, drop in your work and export...
- **Total Clean CSS Variables Extracted**: `439` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter Tight Fallback\: BlinkMacSystemFont`
- **Body Font Stack**: `Inter Tight Fallback\: Segoe UI`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-size-h1: 6.25rem`, `--font-size-tablet-h1: 5rem`, `--font-size-mobile-h1: 3.5rem`
- **Section Heading (`H2`)**: CSS variables `--font-size-h2: 3.25rem`, `--font-size-tablet-h2: 2.75rem`, `--font-size-mobile-h2: 2rem`
- **Body Copy**: CSS variables `--body-top: 59`, `--font-size-paragraph: 1rem`, `--font-size-body: 1.0625rem`
- **Metadata & Labels**: CSS variables `--shadow-caption: 0 .5rem 1.5rem #1d1d1f1f`, `--font-size-label: .9375rem`, `--font-size-meta: .75rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f5f7` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#1d1d1f` | `var(--fg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--on-fg)` in `:root` |
| **Interactive Accent / Highlight** | `#000000` | `var(--logo)` in `:root` |
| **Secondary / Muted Copy** | `#6e6e73` | `var(--fg-muted)` in `:root` |
| **Structural Hairline Border** | `#e5e5ea` | `var(--border)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--step` | `13.875rem` | Dimension / Scale Token |
| `--scale` | `.66` | Design System Custom Token |
| `--corner` | `1.25rem` | Dimension / Scale Token |
| `--drum` | `0` | Design System Custom Token |
| `--top` | `1.125rem` | Dimension / Scale Token |
| `--room` | `max(7.5rem, 100svh - 25.3125rem)` | Dimension / Scale Token |
| `--panel` | `47.1875rem` | Dimension / Scale Token |
| `--rounded` | `calc(var(--panel)*20/755)` | Elevation / Border Token |
| `--bottom` | `2rem` | Dimension / Scale Token |
| `--swatch` | `min(2.25rem, (100cqi - 3 * var(--swatch-gap) - var(--space-8)) / 4)` | Brand / Palette Token |
| `--swatch-gap` | `.625rem` | Brand / Palette Token |
| `--full` | `0` | Design System Custom Token |
| `--open` | `0` | Design System Custom Token |
| `--late` | `0` | Design System Custom Token |
| `--height` | `clamp(39.25rem, 100svh, 48rem)` | Layout / Spatial Grid Token |
| `--chat-top` | `calc(var(--height) - 9.875rem)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.app-nav> — `premotio-com`)**:
   - Landmark `<header class="app-nav app-nav--active">` hosting `premotio — finished design into poli` navigation (`Library · How it works · MCP · Pricing · Contact`), DOM attributes (`data-v-a799f99b`, `data-v-a3457c20`, `data-v-39640a56`, `data-v-f9a31650`), and stylesheet rule `before { content:attr(data-word) }`.
2. **Hero Stage & Focal Lead (<section.hero> — `D e s i g n e d a l r e a d y N o `)**:
   - Landmark `<section class="hero is-on">` presenting display lead `D e s i g n e d a l r e a d y N o w m a k e i t (...` and copy excerpt *"D e s i g n e d a l r e a d y"* over `#f5f5f7` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.library> — `S t a r t w i t h t h e g o o d p `)**:
   - Landmark `<section class="library">` rendering section `S t a r t w i t h t h e g o o d p a r t` with copy *"N o w m a k e i t ( move )"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `_payload.json`), and grid rule `.reveal-line-mask { clip-path:inset(0 -100vw -.2em -.15em) }`.
4. **Interactive Detail & Feature Matrix (<section.categories> — `Preset categories`)**:
   - Landmark `<section class="categories">` framing `Preset categories` and `T a k e t h e s h o r t c u t . K i l l t h e ( t...` (*"Designed already Now make it move"*) with `#ffffff` surface cards, `#000000` accents, and `focus-visible { outline:2px solid var(--fg);outline-offset:.125rem }`.
5. **Colophon & Global Directory Footer (<footer.app-footer> — `https://premotio.com/`)**:
   - Landmark `<footer class="app-footer">` anchoring `premotio — finished design into ` footer links (`Library · How it works · MCP · Pricing · Contact`), copy *"Premotio turns finished design into polished motion — withou"*, and `#e5e5ea` structural dividers.
