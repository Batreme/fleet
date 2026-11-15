# UI & UX Architecture: anemone-mina-massoud-com

## Overview & Design Identity
- **Target**: `anemone-mina-massoud-com` (**Anemone: an interactive paper-theatre film by Mina Massoud**)
- **Production URL**: [https://anemone.mina-massoud.com/](https://anemone.mina-massoud.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#efe6d2` / `#8d8170`)
- **Summary**: A scroll-driven, interactive WebGL short film. A lonely boy buries his flower in a tin, grows into a knight who never puts down his sword...
- **Total Clean CSS Variables Extracted**: `11` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Source Serif 4`
- **Body Font Stack**: `Anemone Hand`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `40px`, `168px`, `30px`, `14px`, `78px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 64px`, `font-weight: 400`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `40px`, `168px`, `30px`, `14px`, `78px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `40px`, `168px`, `30px`, `14px`, `78px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#efe6d2` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#c9bda6` | `var(--paper-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#2a211b` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#8d8170` | `var(--dim)` in `:root` |
| **Secondary / Muted Copy** | `#000` | `html { background: #000 }` |
| **Structural Hairline Border** | `#0000` | `.vignette { background: #0000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#efe6d2` | Canvas / Surface Token |
| `--paper-2` | `#c9bda6` | Canvas / Surface Token |
| `--ink` | `#2a211b` | Typography Ink Token |
| `--dim` | `#8d8170` | Color / Atmospheric Token |
| `--serif` | `"Source Serif 4", Georgia, serif` | Typography / Scale Token |
| `--hand` | `"Anemone Hand", "Segoe Print", cursive` | Dimension / Scale Token |
| `--wild` | `"Anemone Wild", "Anemone Brush", sans-serif` | Dimension / Scale Token |
| `--brush` | `"Anemone Brush", sans-serif` | Dimension / Scale Token |
| `--lx` | `0px` | Dimension / Scale Token |
| `--ly` | `0px` | Dimension / Scale Token |
| `--lightningcss-dark` | `initial` | Canvas / Surface Token |
| `--anemone-mina-mas-bg` | `#efe6d2` | Canvas Substrate (from `var(--paper)` in `:root`) |
| `--anemone-mina-mas-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |
| `--anemone-mina-mas-surface` | `#2a211b` | Surface Substrate (stylesheet-derived) |
| `--anemone-mina-mas-accent` | `#8d8170` | Interactive Accent (stylesheet-derived) |
| `--anemone-mina-mas-muted` | `#000` | Secondary Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.has-flower> — `anemone-mina-massoud-com`)**:
   - Landmark `<header class="has-flower">` hosting `Anemone: an interactive paper-theatr` navigation (`Mina Massoud · mina-massoud.com`), DOM attributes (`data-engine="three.js r170"`, `data-section="1"`, `data-section="2"`, `data-section="3"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.section> — `Anemone`)**:
   - Landmark `<section class="section section-1">` presenting display lead `Anemone` and copy excerpt *"An interactive paper-theatre film by Mina Massoud . It needs Java"* over `#efe6d2` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Anemone. The windflower.`)**:
   - Landmark `<section class="section section-2">` rendering section `Anemone. The windflower.` with copy *"A battlefield burns at night. In the middle of it a knight in a r"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `html { scrollbar-gutter:stable;background:000;overflow-x:clip }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `The knight in the fire`)**:
   - Landmark `<section class="section section-3">` framing `The knight in the fire` and `The windflower` (*"Years before. A schoolyard at dusk. He was eight. He made a paper"*) with `#2a211b` surface cards, `#8d8170` accents, and `img { -webkit-user-drag:none }`.
5. **Colophon & Global Directory Footer (<footer.css3d> — `https://anemone.mina-massoud.com/`)**:
   - Landmark `<footer class="css3d">` anchoring `Anemone: an interactive paper-th` footer links (`Mina Massoud · mina-massoud.com`), copy *"That night, it rained. He dug a small hole at the roots of t"*, and `#0000` structural dividers.
