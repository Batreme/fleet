# UI & UX Architecture: ethanwong-photography

## Overview & Design Identity
- **Target**: `ethanwong-photography` (**Ethan W · Film-Inspired Wedding & Editorial Photographer · Washington DC...**)
- **Production URL**: [http://ethanwong.photography](http://ethanwong.photography)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#9b1120` canvas, `#8a8174` ink, `#c01f34` accent)
- **Summary**: Documentary wedding, editorial, portrait and commercial photography by Ethan Wong of Ethan W Photography. Film-inspired, vintage-leaning...
- **Total Clean CSS Variables Extracted**: `30` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cormorant`
- **Body Font Stack**: `Pinyon Script`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(var(--fit-min)`, `29px`, `var(--lab-nav)`, `clamp(28px,4.4vw,72px)`, `var(--lab-quiet)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(var(--fit-min)`, `29px`, `var(--lab-nav)`, `clamp(28px,4.4vw,72px)`, `var(--lab-quiet)`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(var(--fit-min)`, `29px`, `var(--lab-nav)`, `clamp(28px,4.4vw,72px)`, `var(--lab-quiet)`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(var(--fit-min)`, `29px`, `var(--lab-nav)`, `clamp(28px,4.4vw,72px)`, `var(--lab-quiet)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#9b1120` | `var(--red)` in `:root` |
| **Primary Typography Ink** | `#b3162a` | `var(--red-hover)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ab182c` | `var(--red-lift)` in `:root` |
| **Interactive Accent / Highlight** | `#c01f34` | `var(--red-lift-hover)` in `:root` |
| **Secondary / Muted Copy** | `#8a0f1e` | `var(--red-deep)` in `:root` |
| **Structural Hairline Border** | `#8a8174` | `var(--sf-ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--fit-lh` | `1` | Design System Custom Token |
| `--fit-reserve` | `0px` | Dimension / Scale Token |
| `--red` | `#9b1120` | Color / Atmospheric Token |
| `--red-hover` | `#b3162a` | Color / Atmospheric Token |
| `--red-lift` | `#ab182c` | Color / Atmospheric Token |
| `--red-lift-hover` | `#c01f34` | Color / Atmospheric Token |
| `--red-deep` | `#8a0f1e` | Color / Atmospheric Token |
| `--lab-nav` | `13px` | Layout / Spatial Grid Token |
| `--lab` | `12px` | Dimension / Scale Token |
| `--lab-sm` | `11px` | Dimension / Scale Token |
| `--lab-dock` | `9.5px` | Dimension / Scale Token |
| `--lab-quiet` | `10px` | Dimension / Scale Token |
| `--lab-w` | `400` | Design System Custom Token |
| `--lab-w-nav` | `400` | Layout / Spatial Grid Token |
| `--lab-w-dock` | `500` | Design System Custom Token |
| `--head-band` | `74px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site> — `ethanwong-photography`)**:
   - Landmark `<header class="site nav-on-dark">` hosting `Ethan W · Film-Inspired Wedding & Ed` navigation (`Editorial Exchange`), DOM attributes (`data-cursor="always"`, `data-nav`, `data-cta-ink`, `data-nav-theme="dark"`), and stylesheet rule `html { -ms-overflow-style:none;scrollbar-width:none;-webkit-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<main.idx-main> — `Ethan W (Ethan Wong), film-inspire`)**:
   - Landmark `<main class="idx-main">` presenting display lead `Ethan W (Ethan Wong), film-inspired documentary w...` and copy excerpt *"01 W e d d i n g s W e d d i n g s Stories & galleries"* over `#9b1120` canvas and `#8a8174` ink.
3. **Primary Showcase & Content Grid (<main.idx-main> — `01 W e d d i n g s W e d d i n g s`)**:
   - Landmark `<main class="idx-main">` rendering section `01 W e d d i n g s W e d d i n g s Stories & gal` with copy *"W e d d i n g s W e d d i n g s"*, asset references (`favicon-32.png`, `favicon-16.png`, `favicon-32-dark.png`, `favicon-16-dark.png`), and grid rule `html::-webkit-scrollbar { display:none }`.
4. **Interactive Detail & Feature Matrix (<main.idx-main> — `W e d d i n g s W e d d i n g s`)**:
   - Landmark `<main class="idx-main">` framing `W e d d i n g s W e d d i n g s` and `Stories & galleries` (*"Stories & galleries"*) with `#ab182c` surface cards, `#c01f34` accents, and `body { background:efede7 }`.
5. **Colophon & Global Directory Footer (<footer.sf> — `http://ethanwong.photography`)**:
   - Landmark `<footer class="sf sf--fixed">` anchoring `Ethan W · Film-Inspired Wedding ` footer links (`Editorial Exchange`), copy *"All visual stories More coming"*, and `#8a8174` structural dividers.
