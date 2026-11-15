# UI & UX Architecture: oliviaarents-com

## Overview & Design Identity
- **Target**: `oliviaarents-com` (**OliviaOS 96 — Personal Edition**)
- **Production URL**: [https://oliviaarents.com/](https://oliviaarents.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#8ccf88` canvas, `#000` ink, `#08130b` accent)
- **Summary**: OliviaOS 96 — Personal Edition. Olivia's personal portfolio, imagined as a late-1990s desktop operating system.
- **Total Clean CSS Variables Extracted**: `7` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `VT323`
- **Body Font Stack**: `Courier New`
- **Monospace / Technical Font Stack**: `Courier New`
- **Hero Display (`H1`)**: rule `h1` (`letter-spacing: 1px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 17px`)
- **Body Copy**: rule `p` (`font-size: 11px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.5rem`, `clamp(2rem,7vw,3rem)`, `1.125rem`, `clamp(1.125rem,5vw,1.5rem)`, `21px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#8ccf88` | `:root { color: #8ccf88 }` |
| **Primary Typography Ink** | `#000` | `:root { background: #000 }` |
| **Elevated Surface / Card Substrate** | `#a1afa0` | `.boot-screen__edition { color: #a1afa0 }` |
| **Interactive Accent / Highlight** | `#08130b` | `.boot-screen__progress { background: #08130b }` |
| **Secondary / Muted Copy** | `#548b59` | `.boot-screen__progress { border: #548b59 }` |
| **Structural Hairline Border** | `#95ab7a` | `.calculator { color: #95ab7a }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--lightningcss-dark` | `initial` | Canvas / Surface Token |
| `--lightningcss-light` | `initial` | Canvas / Surface Token |
| `--touch-dock-height` | `calc(70px + env(safe-area-inset-bottom,0px))` | Layout / Spatial Grid Token |
| `--taskbar-height` | `48px` | Layout / Spatial Grid Token |
| `--desktop-icon-width` | `94px` | Layout / Spatial Grid Token |
| `--desktop-icon-height` | `88px` | Layout / Spatial Grid Token |
| `--boot-fade-duration` | `450ms` | Motion / Easing Token |
| `--oliviaarents-com-bg` | `#8ccf88` | Canvas Substrate (from `:root { color: #8ccf88 }`) |
| `--oliviaarents-com-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |
| `--oliviaarents-com-surface` | `#a1afa0` | Surface Substrate (stylesheet-derived) |
| `--oliviaarents-com-accent` | `#08130b` | Interactive Accent (stylesheet-derived) |
| `--oliviaarents-com-muted` | `#548b59` | Secondary Ink (stylesheet-derived) |
| `--oliviaarents-com-border` | `#95ab7a` | Structural Border (stylesheet-derived) |
| `--oliviaarents-com-container` | `48rem` | Container Bound (stylesheet-derived) |
| `--oliviaarents-com-gap` | `.75rem` | Grid Gutter (stylesheet-derived) |
| `--oliviaarents-com-pad` | `2rem` | Lateral Padding (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.desktop> — `oliviaarents-com`)**:
   - Landmark `<header class="desktop">` hosting `OliviaOS 96 — Personal Edition` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sdkn="@vercel/analytics/react"`, `data-sdkv="2.0.1"`, `data-dragging="false"`, `data-dragging="false"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<main.desktop> — `OliviaOS 96`)**:
   - Landmark `<main class="desktop">` presenting display lead `OliviaOS 96` and copy excerpt *"Drag an icon or use arrow keys to move it. Hold Shift for smaller"* over `#8ccf88` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<main.desktop> — `Drag an icon or use arrow keys to `)**:
   - Landmark `<main class="desktop">` rendering section `Drag an icon or use arrow keys to move it. Hold ` with copy *"Click anywhere to boot _"*, asset references (`favicon.svg`, `index-DfR-XKA5.js`, `index-BnFyCq9P.css`, `script.js`), and grid rule `body { overscroll-behavior:none;width:100%;height:100%;overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<main.desktop> — `Click anywhere to boot _`)**:
   - Landmark `<main class="desktop">` framing `Click anywhere to boot _` and `oliviaarents-com Archive & Directory` (*"Drag an icon or use arrow keys to move it. Hold "*) with `#a1afa0` surface cards, `#08130b` accents, and `root { height:100dvh;overflow:hidden }`.
5. **Colophon & Global Directory Footer (<footer.taskbar> — `https://oliviaarents.com/`)**:
   - Landmark `<footer class="taskbar">` anchoring `OliviaOS 96 — Personal Edition` footer links (`Overview · Index · Archive · About · Contact`), copy *"Click anywhere to boot _"*, and `#95ab7a` structural dividers.
