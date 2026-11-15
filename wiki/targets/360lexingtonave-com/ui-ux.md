# UI & UX Architecture: 360lexingtonave-com

## Overview & Design Identity
- **Target**: `360lexingtonave-com` (**360 Lexington Avenue**)
- **Production URL**: [https://360lexingtonave.com](https://360lexingtonave.com)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#111213` canvas, `#fff` ink, `#000` accent)
- **Summary**: Located at 40th Street and Lexington Avenue, just a two-minute walk from Grand Central Terminal.
- **Total Clean CSS Variables Extracted**: `36` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 110px`, `line-height: 100%`, `letter-spacing: -.03em`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 74px`, `line-height: 100%`, `letter-spacing: -.03em`, `font-weight: 400`)
- **Body Copy**: rule `p` (`font-size: 12px`, `line-height: 116%`, `letter-spacing: -.03em`, `font-weight: 400`)
- **Metadata & Labels**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#111213` | `var(--token-c796e2cf-d257-4b33-b047-54ba873a0aa1)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--token-12fc5a7c-f912-48c9-8238-1c64b516e639)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff6` | `var(--token-fcb71b86-915a-48dc-848f-900a8d21781e)` in `:root` |
| **Interactive Accent / Highlight** | `#000` | `:hover { color: #000 }` |
| **Secondary / Muted Copy** | `#f5f5f5` | `.framer-jJ6Uj .framer-oq6atu { background-color: #f5f5f5 }` |
| **Variable Token (`--token-1e846e4d-2af5-4cab-b763-361cb3703674`)** | `#ffffff29` | `var(--token-1e846e4d-2af5-4cab-b763-361cb3703674)` in `:root` |
| **Variable Token (`--token-fedfb1b7-b3b3-4fcd-a5c5-e2a1955b044e`)** | `#11121366` | `var(--token-fedfb1b7-b3b3-4fcd-a5c5-e2a1955b044e)` in `:root` |
| **Variable Token (`--token-6ac23283-84f0-4aba-8ffe-b86657dd600d`)** | `#1112130a` | `var(--token-6ac23283-84f0-4aba-8ffe-b86657dd600d)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-c796e2cf-d257-4b33-b047-54ba873a0aa1` | `#111213` | Color / Atmospheric Token |
| `--token-12fc5a7c-f912-48c9-8238-1c64b516e639` | `#fff` | Color / Atmospheric Token |
| `--token-fcb71b86-915a-48dc-848f-900a8d21781e` | `#fff6` | Color / Atmospheric Token |
| `--token-1e846e4d-2af5-4cab-b763-361cb3703674` | `#ffffff29` | Color / Atmospheric Token |
| `--token-fedfb1b7-b3b3-4fcd-a5c5-e2a1955b044e` | `#11121366` | Color / Atmospheric Token |
| `--token-6ac23283-84f0-4aba-8ffe-b86657dd600d` | `#1112130a` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |
| `--font-size` | `var(--framer-font-size)` | Typography / Scale Token |
| `--text-transform` | `var(--framer-text-transform)` | Typography Ink Token |
| `--line-height` | `var(--framer-line-height)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `360lexingtonave-com`)**:
   - Landmark `<header class="lenis">` hosting `360 Lexington Avenue` navigation (`Available Offices · Prime Corner Retail · Contact Us · Explore Retail · Explore Offices`), DOM attributes (`data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`, `data-fid="e25c75bee6148e62c6ea7..."`), and stylesheet rule `main { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<div.lenis-smooth> — `Built For Difference Makers`)**:
   - Landmark `<div class="lenis-smooth">` presenting display lead `Built For Difference Makers` and copy excerpt *"Prime Corner Retail"* over `#111213` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<div.framer-jJ6Uj> — `360 Lex has been thoroughly reimag`)**:
   - Landmark `<div class="framer-jJ6Uj">` rendering section `360 Lex has been thoroughly reimagined with a new...` with copy *"Located at 40th Street and Lexington Avenue:"*, asset references (`Grxz4pBrnDA6VjRjN6h8ucts0.png`, `oehMxFzuMfSIeZHPUFXOF3LFOiM.png`, `factors.js`, `fonts.gstatic.com`), and grid rule `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`.
4. **Interactive Detail & Feature Matrix (<div.framer-DOsz9> — `2-Minute Walk to Grand Central`)**:
   - Landmark `<div class="framer-DOsz9">` framing `2-Minute Walk to Grand Central` and `Surrounded By Dining & Entertainment` (*"just a two-minute walk from Grand Central Terminal."*) with `#fff6` surface cards, `#000` accents, and `button { font-family:sans-serif;font-size:12px }`.
5. **Colophon & Global Directory Footer (<footer.framer-Kw8IE> — `https://360lexingtonave.com`)**:
   - Landmark `<footer class="framer-Kw8IE">` anchoring `360 Lexington Avenue` footer links (`Available Offices · Prime Corner Retail · Contact Us · Explore Retail · Explore Offices`), copy *"Located at 40th and Lexington Avenue, just a two-minute walk"*, and `#fff` structural dividers.
