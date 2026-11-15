# UI & UX Architecture: www-tokonoma-xyz

## Overview & Design Identity
- **Target**: `www-tokonoma-xyz` (**Tokonoma Studio — Image Making, Art, AI & Creative Direction**)
- **Production URL**: [https://www.tokonoma.xyz/](https://www.tokonoma.xyz/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#baff00` / `#000`)
- **Summary**: Tokonoma is an image-making studio working across analogue and AI photography, animation, creative coding, art and digital experiences. C...
- **Total Clean CSS Variables Extracted**: `3` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `EurostileMNExtendedBold`
- **Body Font Stack**: `AmstradPC`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`letter-spacing: .02em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 24px`, `line-height: 1.05`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `48px`, `16px`, `clamp(19px, calc(1.35vw + 4px)`, `22px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `48px`, `16px`, `clamp(19px, calc(1.35vw + 4px)`, `22px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#baff00` | `var(--cursor-color)` in `:root` |
| **Primary Typography Ink** | `#5f5f5f` | `var(--color-muted)` in `:root` |
| **Elevated Surface / Card Substrate** | `#141414` | `var(--color-panel)` in `:root` |
| **Interactive Accent / Highlight** | `#000` | `.viewer-menu-entry.cursor-hover { background: #000 }` |
| **Secondary / Muted Copy** | `#fff` | `.viewer-menu-entry.wheel-selected { color: #fff }` |
| **Structural Hairline Border** | `#f00` | `.pill-slot.wrong-target .slot-fill { fill: #f00 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cursor-color` | `#baff00` | Brand / Palette Token |
| `--color-muted` | `#5f5f5f` | Brand / Palette Token |
| `--color-panel` | `#141414` | Brand / Palette Token |
| `--www-tokonoma-xyz-bg` | `#baff00` | Canvas Substrate (from `var(--cursor-color)` in `:root`) |
| `--www-tokonoma-xyz-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |
| `--www-tokonoma-xyz-surface` | `#141414` | Surface Substrate (stylesheet-derived) |
| `--www-tokonoma-xyz-accent` | `#000` | Interactive Accent (stylesheet-derived) |
| `--www-tokonoma-xyz-muted` | `#fff` | Secondary Ink (stylesheet-derived) |
| `--www-tokonoma-xyz-border` | `#f00` | Structural Border (stylesheet-derived) |
| `--www-tokonoma-xyz-container` | `700px` | Container Bound (stylesheet-derived) |
| `--www-tokonoma-xyz-gap` | `32px` | Grid Gutter (stylesheet-derived) |
| `--www-tokonoma-xyz-pad` | `7px` | Lateral Padding (stylesheet-derived) |
| `--www-tokonoma-xyz-ease` | `cubic-bezier(.22,1,.36,1)` | Primary Easing Function |
| `--www-tokonoma-xyz-radius` | `999px` | Corner Radius (stylesheet-derived) |
| `--www-tokonoma-xyz-fs-base` | `12px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.interface> — `www-tokonoma-xyz`)**:
   - Landmark `<nav class="interface">` hosting `Tokonoma Studio — Image Making, Art,` navigation (`ABOUT · SHOWS`), DOM attributes (`data-target="www-tokonoma-xyz"`), and stylesheet rule `property --angle-1 { syntax: "<angle>"; inherits: false; initial-value: -75deg; }`.
2. **Hero Stage & Focal Lead (<main.entry-main> — `Tokonoma Studio — Image Making, Ar`)**:
   - Landmark `<main class="entry-main">` presenting display lead `Tokonoma Studio — Image Making, Art, AI & Creati` and copy excerpt *"Tokonoma is an image-making studio working across analogue and AI"* over `#baff00` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<main.entry-main> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="entry-main">` rendering section `Featured Work & Interactive Showcase` with copy *"Tokonoma Studio — Image Making, Art, AI & Creati"*, asset references (`EurostileMNExtendedBold.ttf`, `favicon-32x32-dm.png`, `styles.css`, `tokonoma_logo.png (Tokonoma)`), and grid rule `property --angle-2 { syntax: "<angle>"; inherits: false; initial-value: -45deg; }`.
4. **Interactive Detail & Feature Matrix (<main.entry-main> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="entry-main">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#141414` surface cards, `#000` accents, and `html.mobile-project-wheel .viewer... { inset: 160px 0 64px 0; }`.
5. **Colophon & Global Directory Footer (<footer.tokonoma-logo-frame> — `https://www.tokonoma.xyz/`)**:
   - Landmark `<footer class="tokonoma-logo-frame">` anchoring `Tokonoma Studio — Image Making, ` footer links (`ABOUT · SHOWS`), copy *"Technical Architecture & Narrative"*, and `#f00` structural dividers.
