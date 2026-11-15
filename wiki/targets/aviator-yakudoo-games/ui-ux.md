# UI & UX Architecture: aviator-yakudoo-games

## Overview & Design Identity
- **Target**: `aviator-yakudoo-games` (**Aviator**)
- **Production URL**: [https://aviator.yakudoo.games](https://aviator.yakudoo.games)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#b6c6a6` / `#f7d9aa`)
- **Summary**: How far can you fly?
- **Total Clean CSS Variables Extracted**: `87` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Hammersmith One`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.62em`, `.7em`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.62em`, `.7em`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.62em`, `.7em`)
- **Metadata & Labels**: CSS variables `--stats-label: #b6c6a6`, `--stats-label-gap: 16`, `--ui-min-label: 10px`; rule `small` (`line-height: 1`, `font-weight: 400`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#b6c6a6` | `var(--stats-label)` in `:root` |
| **Primary Typography Ink** | `#3a6da8` | `var(--tut-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#444` | `body { color: #444 }` |
| **Interactive Accent / Highlight** | `#f7d9aa` | `body { background: #f7d9aa }` |
| **Secondary / Muted Copy** | `#000` | `.app { background: #000 }` |
| **Structural Hairline Border** | `#fff` | `.debug { color: #fff }` |
| **Variable Token (`--ui-shadow`)** | `#14468278` | `var(--ui-shadow)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--start-top` | `59.5%` | Dimension / Scale Token |
| `--hud-icon` | `42` | Design System Custom Token |
| `--lu` | `clamp(.6px, calc(var(--app-w,100vw) / 2000), 1px)` | Dimension / Scale Token |
| `--menu-gap-scale` | `.7` | Layout / Spatial Grid Token |
| `--board-delay` | `0s` | Motion / Easing Token |
| `--brand-w` | `max(15px, calc(30 * var(--u)))` | Brand / Palette Token |
| `--links-icon-h` | `max(20px, calc(30 * var(--u)))` | Typography Ink Token |
| `--edge` | `calc(60 * var(--u) + (var(--links-icon-h) - var(--brand-w) * 30 / 25) / 2)` | Design System Custom Token |
| `--rh` | `min(1vw, 6px)` | Dimension / Scale Token |
| `--app-w` | `1440px` | Dimension / Scale Token |
| `--app-h` | `900px` | Dimension / Scale Token |
| `--ui-shadow` | `#14468278` | Elevation / Border Token |
| `--ui-shadow-y` | `0.06em` | Elevation / Border Token |
| `--ui-veil` | `0.3` | Design System Custom Token |
| `--ui-gauge` | `80` | Design System Custom Token |
| `--ui-cx` | `96` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.links> — `aviator-yakudoo-games`)**:
   - Landmark `<nav class="links">` hosting `Aviator` navigation (`YAKUDOO GAMES · EPIC AGENCY`), DOM attributes (`data-phase="menu"`, `data-engine="three.js r186"`, `data-screen="loading"`, `data-field="progress"`), and stylesheet rule `font-face { font-family:Hammersmith One;src:url(./HammersmithOne-Regular-DS-TeCEr.wo... }`.
2. **Hero Stage & Focal Lead (<section.board> — `GAME PAUSED`)**:
   - Landmark `<section class="board">` presenting display lead `GAME PAUSED` and copy excerpt *"S H O O T ’ E M U P"* over `#b6c6a6` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.board> — `KEEP FLYING?`)**:
   - Landmark `<section class="board">` rendering section `KEEP FLYING?` with copy *"SHARE THE GAME LINK COPIED Send the link on Or your favorite mess"*, asset references (`favicon.png`, `apple-touch-icon.png`, `main-B6RCEMmP.js`, `modulepreload-polyfill-P2Xu9kJm.js`), and grid rule `after { box-sizing:border-box }`.
4. **Interactive Detail & Feature Matrix (<section.board> — `GAMEOVER`)**:
   - Landmark `<section class="board">` framing `GAMEOVER` and `LINK COPIED Send the link on Or your favorite me` (*"LINK COPIED Send the link on Or your favorite messaging app."*) with `#444` surface cards, `#f7d9aa` accents, and `body { overscroll-behavior:none;height:100%;margin:0;overflow:hidden }`.
5. **Colophon & Global Directory Footer (<footer.energy-gauge__stop> — `https://aviator.yakudoo.games`)**:
   - Landmark `<footer class="energy-gauge__stop">` anchoring `Aviator` footer links (`YAKUDOO GAMES · EPIC AGENCY`), copy *"Send the link on Or your favorite messaging app."*, and `#fff` structural dividers.
