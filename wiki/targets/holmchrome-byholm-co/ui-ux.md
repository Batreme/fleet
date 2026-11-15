# UI & UX Architecture: holmchrome-byholm-co

## Overview & Design Identity
- **Target**: `holmchrome-byholm-co` (**HOLMCHROME · Portrait Photography**)
- **Production URL**: [https://holmchrome.byholm.co/](https://holmchrome.byholm.co/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#191919` / `#f2f2ef`)
- **Summary**: HOLMCHROME is a portrait photographer working between the studio and the street. Selected work, a full index of frames and studio informa...
- **Total Clean CSS Variables Extracted**: `2` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `SFMono-Regular`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `15px`, `13px`, `10px`, `12px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `15px`, `13px`, `10px`, `12px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `15px`, `13px`, `10px`, `12px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `15px`, `13px`, `10px`, `12px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#191919` | `var(--murekkep)` in `:root` |
| **Primary Typography Ink** | `#f6f6f6` | `body { background: #f6f6f6 }` |
| **Elevated Surface / Card Substrate** | `#fff` | `body.filmde #vizor { color: #fff }` |
| **Interactive Accent / Highlight** | `#f2f2ef` | `.v-menu-btn .cizgi { background: #f2f2ef }` |
| **Secondary / Muted Copy** | `#0d0d0d` | `#menu-panel { background: #0d0d0d }` |
| **Structural Hairline Border** | `#eceae4` | `#menu-panel a { color: #eceae4 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--murekkep` | `#191919` | Color / Atmospheric Token |
| `--lupCap` | `140px` | Dimension / Scale Token |
| `--holmchrome-byhol-bg` | `#191919` | Canvas Substrate (from `var(--murekkep)` in `:root`) |
| `--holmchrome-byhol-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |
| `--holmchrome-byhol-surface` | `#fff` | Surface Substrate (stylesheet-derived) |
| `--holmchrome-byhol-accent` | `#f2f2ef` | Interactive Accent (stylesheet-derived) |
| `--holmchrome-byhol-muted` | `#0d0d0d` | Secondary Ink (stylesheet-derived) |
| `--holmchrome-byhol-border` | `#eceae4` | Structural Border (stylesheet-derived) |
| `--holmchrome-byhol-container` | `none` | Container Bound (stylesheet-derived) |
| `--holmchrome-byhol-gap` | `6px` | Grid Gutter (stylesheet-derived) |
| `--holmchrome-byhol-pad` | `34px` | Lateral Padding (stylesheet-derived) |
| `--holmchrome-byhol-ease` | `cubic-bezier(.3,.7,.2,1.2)` | Primary Easing Function |
| `--holmchrome-byhol-radius` | `50%` | Corner Radius (stylesheet-derived) |
| `--holmchrome-byhol-fs-base` | `11px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.if-hero> — `holmchrome-byholm-co`)**:
   - Landmark `<header class="if-hero">` hosting `HOLMCHROME · Portrait Photography` navigation (`HOLMCHROME`), DOM attributes (`data-engine="three.js r186"`, `data-engine="three.js r186"`, `data-engine="three.js r186"`, `data-engine="three.js r186"`), and stylesheet rule `body { color:191919;background:f6f6f6;overflow:hidden }`.
2. **Hero Stage & Focal Lead (<section.atla> — `HOLMCHROME`)**:
   - Landmark `<section class="atla">` presenting display lead `HOLMCHROME` and copy excerpt *"Portrait photographer working between the studio and the street."* over `#191919` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.imlecsiz> — `H O L M C H R O M E`)**:
   - Landmark `<section class="imlecsiz">` rendering section `H O L M C H R O M E` with copy *"Work · Index · Journal · Info"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `manifest.webmanifest`), and grid rule `app { touch-action:none;-webkit-tap-highlight-color:transparent;position:fixed... }`.
4. **Interactive Detail & Feature Matrix (<section.if-ozet> — `Work · Index · Journal · Info`)**:
   - Landmark `<section class="if-ozet">` framing `Work · Index · Journal · Info` and `This site is built with WebGL and needs JavaScri` (*"This site is built with WebGL and needs JavaScript to run."*) with `#fff` surface cards, `#f2f2ef` accents, and `root { --murekkep:191919 }`.
5. **Colophon & Global Directory Footer (<footer.if-son> — `https://holmchrome.byholm.co/`)**:
   - Landmark `<footer class="if-son if-izgara">` anchoring `HOLMCHROME · Portrait Photograph` footer links (`HOLMCHROME`), copy *"· G O L D E N H O U R"*, and `#eceae4` structural dividers.
