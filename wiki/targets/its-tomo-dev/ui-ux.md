# UI & UX Architecture: its-tomo-dev

## Overview & Design Identity
- **Target**: `its-tomo-dev` (**its_tomo - creative engineer**)
- **Production URL**: [https://its-tomo.dev/](https://its-tomo.dev/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0b0b0c` / `#fffaee`)
- **Summary**: Tomo - creative señor engineer from Zagreb. Interfaces, real-time 3D and motion, built with an eye for design. Come in, the garage is open.
- **Total Clean CSS Variables Extracted**: `44` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `JetBrains Mono`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: CSS variables `--f-display: archivo, "Helvetica Neue", arial, sans-serif`
- **Section Heading (`H2`)**: CSS variables `--t-h2: clamp(1.9rem, 3.2vw, 3.4rem)`
- **Body Copy**: CSS variables `--t-body: clamp(0.95rem, 0.95vw, 1.05rem)`
- **Metadata & Labels**: CSS variables `--f-mono: "JetBrains Mono", ui-monospace, menlo, monospace`, `--t-mono: clamp(0.75rem, 0.75vw, 0.8125rem)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0b0b0c` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#ecebe6` | `var(--fg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f7b334` | `var(--neon)` in `:root` |
| **Interactive Accent / Highlight** | `#fffaee` | `.c-intro__heads { stroke: #fffaee }` |
| **Secondary / Muted Copy** | `#f4f6ff` | `.c-logo__underscore::after { background: #f4f6ff }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#0b0b0c` | Canvas / Surface Token |
| `--fg` | `#ecebe6` | Typography Ink Token |
| `--fg-2` | `rgb(236 235 230 / 70%)` | Typography Ink Token |
| `--fg-3` | `rgb(236 235 230 / 60%)` | Typography Ink Token |
| `--rule` | `rgb(236 235 230 / 16%)` | Color / Atmospheric Token |
| `--neon` | `#f7b334` | Color / Atmospheric Token |
| `--f-display` | `archivo, "Helvetica Neue", arial, sans-serif` | Dimension / Scale Token |
| `--f-mono` | `"JetBrains Mono", ui-monospace, menlo, monospace` | Typography / Scale Token |
| `--f-logo` | `var(--f-mono)` | Design System Custom Token |
| `--t-hero` | `clamp(2.6rem, 6.2vw, 7.2rem)` | Dimension / Scale Token |
| `--t-h2` | `clamp(1.9rem, 3.2vw, 3.4rem)` | Typography / Scale Token |
| `--t-lede` | `clamp(1.05rem, 1.2vw, 1.3rem)` | Dimension / Scale Token |
| `--t-body` | `clamp(0.95rem, 0.95vw, 1.05rem)` | Dimension / Scale Token |
| `--t-mono` | `clamp(0.75rem, 0.75vw, 0.8125rem)` | Typography / Scale Token |
| `--gutter` | `clamp(1rem, 3vw, 3rem)` | Layout / Spatial Grid Token |
| `--header-h` | `clamp(3.5rem, 6vw, 5.25rem)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.c-header> — `its-tomo-dev`)**:
   - Landmark `<header class="c-header">` hosting `its_tomo - creative engineer` navigation (`Work · Approach · Awards · Contact`), DOM attributes (`data-engine="three.js r186 webgpu"`, `data-side="left"`, `data-side="right"`, `data-station="door"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.c-station> — `Hello! It’s Tomo, creative señor e`)**:
   - Landmark `<section class="c-station c-station--door">` presenting display lead `Hello! It’s Tomo, creative señor engineer.` and copy excerpt *"its _ Tomo Creative Front Dev tomo, back to the door"* over `#0b0b0c` canvas and `#fffaee` ink.
3. **Primary Showcase & Content Grid (<section.c-station> — `C a r s , h a r d w a r e a n d t `)**:
   - Landmark `<section class="c-station c-station--car">` rendering section `C a r s , h a r d w a r e a n d t h i n g s t h a...` with copy *"Tomo Creative Front Dev"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `canvas { display:block;max-width:100% }`.
4. **Interactive Detail & Feature Matrix (<section.c-station> — `O n t h e b e n c h .`)**:
   - Landmark `<section class="c-station c-station--bench">` framing `O n t h e b e n c h .` and `01 DARC ROOM` (*"tomo, back to the door"*) with `#f7b334` surface cards, `#fffaee` accents, and `button { font:inherit;color:inherit;background:none;border:0;padding:0;cursor:poi... }`.
5. **Colophon & Global Directory Footer (<footer.c-footer> — `https://its-tomo.dev/`)**:
   - Landmark `<footer class="c-footer js-fade">` anchoring `its_tomo - creative engineer` footer links (`Work · Approach · Awards · Contact`), copy *"creative señor engineer."*, and `#fffaee` structural dividers.
