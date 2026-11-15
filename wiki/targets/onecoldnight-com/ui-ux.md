# UI & UX Architecture: onecoldnight-com

## Overview & Design Identity
- **Target**: `onecoldnight-com` (**The Little Match Girl**)
- **Production URL**: [https://onecoldnight.com/](https://onecoldnight.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f2efe6` / `#fff`)
- **Summary**: Andersen's Little Match Girl as a scroll-through noir picture book: open the pages, step into the snow, and strike the matches one by one.
- **Total Clean CSS Variables Extracted**: `14` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `italic 500 16px/1 "Cormorant Garamond`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`letter-spacing: -.02em`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `21px`, `17px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `21px`, `17px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `21px`, `17px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f2efe6` | `var(--dxl-mark-fg)` in `:root` |
| **Primary Typography Ink** | `#050505` | `var(--dxlBg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ff7a1a` | `var(--dxlAccent)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `.cap.speech { background: #fff }` |
| **Secondary / Muted Copy** | `#6b5a4c` | `.burn .flecks i { background: #6b5a4c }` |
| **Structural Hairline Border** | `#1a0d06` | `.burn .stick { background: #1a0d06 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dxl-mark-font` | `italic 500 16px/1 "Cormorant Garamond", Georgia, serif` | Typography / Scale Token |
| `--dxl-mark-tracking` | `.02em` | Typography / Scale Token |
| `--dxl-mark-fg` | `#f2efe6` | Typography Ink Token |
| `--dxl-mark-bg` | `transparent` | Canvas / Surface Token |
| `--dxl-mark-opacity` | `.7` | Design System Custom Token |
| `--dx` | `-9px` | Dimension / Scale Token |
| `--fs` | `1.1` | Design System Custom Token |
| `--dxl-bg` | `var(--dxlBg)` | Canvas / Surface Token |
| `--dxl-fg` | `var(--dxlFg)` | Typography Ink Token |
| `--dxl-accent` | `var(--dxlAccent)` | Brand / Palette Token |
| `--dxlBg` | `#050505` | Canvas / Surface Token |
| `--dxlFg` | `#f2efe6` | Typography Ink Token |
| `--dxlAccent` | `#ff7a1a` | Brand / Palette Token |
| `--head` | `1.000` | Design System Custom Token |
| `--onecoldnight-com-bg` | `#f2efe6` | Canvas Substrate (from `var(--dxl-mark-fg)` in `:root`) |
| `--onecoldnight-com-ink` | `#050505` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.locked> — `onecoldnight-com`)**:
   - Landmark `<header class="locked">` hosting `The Little Match Girl` navigation (`Created by DxL`), DOM attributes (`data-engine="three.js r180"`, `data-dxl-mark`, `data-astro-cid-n6wkilw4`), and stylesheet rule `focus-visible { text-shadow:0 0 6px 050505,0 0 18px rgba(255,122,26,.6) }`.
2. **Hero Stage & Focal Lead (<section.gate> — `The Little Match Girl`)**:
   - Landmark `<section class="gate">` presenting display lead `The Little Match Girl` and copy excerpt *"H. C. Andersen · 1845"* over `#f2efe6` canvas and `#050505` ink.
3. **Primary Showcase & Content Grid (<article.story> — `The story`)**:
   - Landmark `<article class="story">` rendering section `The story` with copy *"A picture book in ink and snow. On the last night of the year, a "*, asset references (`favicon.svg`, `apple-touch-icon.png`, `sitemap-index.xml`, `script.js`), and grid rule `.dot { display:none }`.
4. **Interactive Detail & Feature Matrix (<article.story> — `A picture book in ink and snow. On`)**:
   - Landmark `<article class="story">` framing `A picture book in ink and snow. On the last nigh` and `Scroll to turn the pages. The story is read alou` (*"Scroll to turn the pages. The story is read aloud, so turn your s"*) with `#ff7a1a` surface cards, `#fff` accents, and `html { background:050505 }`.
5. **Colophon & Global Directory Footer (<footer.gate> — `https://onecoldnight.com/`)**:
   - Landmark `<footer class="gate">` anchoring `The Little Match Girl` footer links (`Created by DxL`), copy *"Continue without sound"*, and `#1a0d06` structural dividers.
