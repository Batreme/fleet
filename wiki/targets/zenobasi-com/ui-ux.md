# UI & UX Architecture: zenobasi-com

## Overview & Design Identity
- **Target**: `zenobasi-com` (**Zen Obasi — Art Director**)
- **Production URL**: [https://zenobasi.com](https://zenobasi.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#000`)
- **Summary**: Art director and visual strategist working across identity, campaign and editorial for brands worldwide.
- **Total Clean CSS Variables Extracted**: `13` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Google Sans Flex`
- **Body Font Stack**: `Google Sans Flex`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--text-large)`, `var(--text-small)`, `clamp(1.5rem,7vw,2rem)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--text-large)`, `var(--text-small)`, `clamp(1.5rem,7vw,2rem)`)
- **Body Copy**: rule `,p` (`font-size: var(--text-small)`, `line-height: 1.35`, `font-weight: 400`)
- **Metadata & Labels**: CSS variables `--text-small: 0.7rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--base-100)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--base-300)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0c0c0c` | `.background { background-color: #0c0c0c }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--base-100` | `#fff` | Color / Atmospheric Token |
| `--base-200` | `rgb(255 255 255/0.5)` | Color / Atmospheric Token |
| `--base-300` | `#000` | Color / Atmospheric Token |
| `--edge` | `clamp(2rem,3.5vw,3rem)` | Dimension / Scale Token |
| `--section-gap` | `18rem` | Layout / Spatial Grid Token |
| `--text-small` | `0.7rem` | Typography Ink Token |
| `--text-large` | `clamp(16px,3.5vw,24px)` | Typography Ink Token |
| `--side-reach` | `3.5em` | Dimension / Scale Token |
| `--font-sans` | `"Google Sans Flex"` | Typography / Scale Token |
| `--backdrop` | `0 0 0` | Design System Custom Token |
| `--digit-h` | `1.1em` | Dimension / Scale Token |
| `--fill-mobile` | `0.75` | Design System Custom Token |
| `--fill-desktop` | `0.45` | Design System Custom Token |
| `--zenobasi-com-bg` | `#fff` | Canvas Substrate (from `var(--base-100)` in `:root`) |
| `--zenobasi-com-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |
| `--zenobasi-com-surface` | `#0c0c0c` | Surface Substrate (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.lenis> — `zenobasi-com`)**:
   - Landmark `<nav class="lenis">` hosting `Zen Obasi — Art Director` navigation (`Index Index · Work Work · About About · Inquire Inquire · Zen Obasi Zen Obasi`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/css/5f4..."`, `data-engine="three.js r186"`, `data-copy="lines"`), and stylesheet rule `html { overflow-x:clip }`.
2. **Hero Stage & Focal Lead (<main.background> — `Zen Obasi, Art Director`)**:
   - Landmark `<main class="background">` presenting display lead `Zen Obasi, Art Director` and copy excerpt *"Zen Obasi Zen Obasi"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<main.container> — `Zen Obasi Zen Obasi`)**:
   - Landmark `<main class="container">` rendering section `Zen Obasi Zen Obasi` with copy *"Art Direction / Visual Identity"*, asset references (`2adbc45882a5a7c5.p.woff2`, `webpack-b827b2449ca92f38.js`, `4bd1b696-228d6cc6681fc189.js`, `826-cff36fe3db5d20f7.js`), and grid rule `body { font-family:var(--font-sans),sans-serif;background-color:var(--base-300)... }`.
4. **Interactive Detail & Feature Matrix (<main.menu-toggle> — `Art Direction / Visual Identity`)**:
   - Landmark `<main class="menu-toggle">` framing `Art Direction / Visual Identity` and `Accepting Briefs for S/S 2027` (*"Accepting Briefs for S/S 2027"*) with `#0c0c0c` surface cards, `#000` accents, and `selection { background-color:var(--base-100);color:var(--base-300) }`.
5. **Colophon & Global Directory Footer (<footer.footer-pinned> — `https://zenobasi.com`)**:
   - Landmark `<footer class="footer-pinned footer-simple">` anchoring `Zen Obasi — Art Director` footer links (`Index Index · Work Work · About About · Inquire Inquire · Zen Obasi Zen Obasi`), copy *"Art Direction / Visual Identity"*, and `#000` structural dividers.
