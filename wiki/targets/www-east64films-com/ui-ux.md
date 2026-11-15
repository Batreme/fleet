# UI & UX Architecture: www-east64films-com

## Overview & Design Identity
- **Target**: `www-east64films-com` (**EAST 64 Films · Tokyo-Based International Production Company**)
- **Production URL**: [https://www.east64films.com/](https://www.east64films.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#4eaebf` canvas, `#151515` ink, `#e43936` accent)
- **Summary**: EAST 64 Films is a Tokyo-based production company working across Japan and abroad. From commercials, music videos, and branded content to...
- **Total Clean CSS Variables Extracted**: `111` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Noto Sans JP`
- **Body Font Stack**: `matrix-ii-ext-semi-narrow`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80%`, `75%`, `1rem`, `clamp(1.5rem,6vw,8rem)`, `13px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80%`, `75%`, `1rem`, `clamp(1.5rem,6vw,8rem)`, `13px`)
- **Body Copy**: CSS variables `--font-size-base: var(--font-size-md)`; rule `p` (`font-size: 13px`, `line-height: 1.4`, `font-weight: 400`)
- **Metadata & Labels**: CSS variables `--base-letter-spacing: 0em`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#4eaebf` | `var(--cl-blue)` in `:root` |
| **Primary Typography Ink** | `#f6b000` | `var(--cl-yellow)` in `:root` |
| **Elevated Surface / Card Substrate** | `#00a44d` | `var(--cl-green)` in `:root` |
| **Interactive Accent / Highlight** | `#e43936` | `var(--cl-red)` in `:root` |
| **Secondary / Muted Copy** | `#f46f2c` | `var(--cl-orange)` in `:root` |
| **Structural Hairline Border** | `#151515` | `var(--cl-dark)` in `:root` |
| **Variable Token (`--cl-white`)** | `#ffffff` | `var(--cl-white)` in `:root` |
| **Variable Token (`--cl-whitegray`)** | `#eeeeee` | `var(--cl-whitegray)` in `:root` |
| **Variable Token (`--cl-black`)** | `#1a1a1a` | `var(--cl-black)` in `:root` |
| **Variable Token (`--cl-blackgray`)** | `#222222` | `var(--cl-blackgray)` in `:root` |
| **Variable Token (`--cl-lightgray`)** | `#b9b9b9` | `var(--cl-lightgray)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cl-blue` | `#4eaebf` | Color / Atmospheric Token |
| `--cl-yellow` | `#f6b000` | Color / Atmospheric Token |
| `--cl-green` | `#00a44d` | Color / Atmospheric Token |
| `--cl-red` | `#e43936` | Color / Atmospheric Token |
| `--cl-orange` | `#f46f2c` | Color / Atmospheric Token |
| `--cl-dark` | `#151515` | Canvas / Surface Token |
| `--cl-white` | `#ffffff` | Canvas / Surface Token |
| `--cl-whitegray` | `#eeeeee` | Canvas / Surface Token |
| `--cl-black` | `#1a1a1a` | Canvas / Surface Token |
| `--cl-blackgray` | `#222222` | Canvas / Surface Token |
| `--cl-lightgray` | `#b9b9b9` | Canvas / Surface Token |
| `--cl-base` | `var(--cl-white)` | Design System Custom Token |
| `--cl-bg` | `var(--cl-blackgray)` | Canvas / Surface Token |
| `--fw-regular` | `400` | Design System Custom Token |
| `--fw-medium` | `500` | Design System Custom Token |
| `--fw-bold` | `700` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-east64films-com`)**:
   - Landmark `<header class="site-header">` hosting `EAST 64 Films · Tokyo-Based Internat` navigation (`T T O O P P · W W O O R R K K S S · A A B B O O U U T T`), DOM attributes (`data-lang-suffix="/"`, `data-lang-suffix="/"`, `data-lang-suffix="/"`, `data-lang-suffix="/works/"`), and stylesheet rule `.tk-matrix-ii { font-family: "matrix-ii",serif; }`.
2. **Hero Stage & Focal Lead (<section.p-works> — `F E N D I H o l i d a y C a m p a `)**:
   - Landmark `<section class="p-works">` presenting display lead `F E N D I H o l i d a y C a m p a i g n F E N D I` and copy excerpt *"W W O O R R K K S S"* over `#4eaebf` canvas and `#151515` ink.
3. **Primary Showcase & Content Grid (<section.p-works> — `W W O O R R K K S S`)**:
   - Landmark `<section class="p-works">` rendering section `W W O O R R K K S S` with copy *"A A R R T T I I S S T T S S"*, asset references (`knx0cof.css`, `fonts.googleapis.com`, `fonts.gstatic.com`, `favicon.ico`), and grid rule `.tk-matrix-ii-extra { font-family: "matrix-ii-extra",serif; }`.
4. **Interactive Detail & Feature Matrix (<section.p-works> — `A A R R T T I I S S T T S S`)**:
   - Landmark `<section class="p-works">` framing `A A R R T T I I S S T T S S` and `A A B B O O U U T T` (*"A A B B O O U U T T"*) with `#00a44d` surface cards, `#e43936` accents, and `.tk-matrix-ii-display-hilite-scr { font-family: "matrix-ii-display-hilite-scr",sans-serif; }`.
5. **Colophon & Global Directory Footer (<footer.l-footer> — `https://www.east64films.com/`)**:
   - Landmark `<footer class="l-footer">` anchoring `EAST 64 Films · Tokyo-Based Inte` footer links (`T T O O P P · W W O O R R K K S S · A A B B O O U U T T`), copy *"C o m m e r c i a l s , F i l m s , C r e a t i v e C a m p "*, and `#151515` structural dividers.
