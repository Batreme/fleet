# UI & UX Architecture: verasfawaz-com

## Overview & Design Identity
- **Target**: `verasfawaz-com` (**Véras Fawaz**)
- **Production URL**: [https://verasfawaz.com](https://verasfawaz.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#202426` / `#24292b`)
- **Summary**: Véras Fawaz © 1993 - 2026
- **Total Clean CSS Variables Extracted**: `111` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Studio Mono`
- **Body Font Stack**: `Studio Sans`
- **Monospace / Technical Font Stack**: `Studio Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: var(--ui-title)`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 22px!important`, `line-height: 1.2!important`)
- **Body Copy**: rule `p` (`font-size: 16px`, `line-height: 1.5`)
- **Metadata & Labels**: CSS variables `--type-mono: "Studio Mono",monospace`, `--ui-meta: 12px`, `--meta: 13px`; rule `small` (`letter-spacing: 0`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#202426` | `var(--ui-ink)` in `:root` |
| **Primary Typography Ink** | `#575e61` | `var(--ui-muted)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f7f7f2` | `var(--paper)` in `:root` |
| **Interactive Accent / Highlight** | `#24292b` | `var(--panel-ink)` in `:root` |
| **Secondary / Muted Copy** | `#fff` | `var(--detail-paper)` in `:root` |
| **Structural Hairline Border** | `#202020` | `var(--detail-ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--project-scroll-progress` | `inherit` | Design System Custom Token |
| `--window-milk` | `rgba(255,255,255,.68)` | Color / Atmospheric Token |
| `--media-vignette` | `1` | Design System Custom Token |
| `--media-text-opacity` | `1` | Typography Ink Token |
| `--media-arrow-opacity` | `1` | Design System Custom Token |
| `--project-header-fill` | `0!important` | Layout / Spatial Grid Token |
| `--type-sans` | `"Helvetica Neue",Helvetica,Arial,sans-serif` | Typography / Scale Token |
| `--type-mono` | `"Studio Mono",monospace` | Typography / Scale Token |
| `--ui-font` | `var(--type-sans)` | Typography / Scale Token |
| `--ui-action` | `15px` | Dimension / Scale Token |
| `--ui-meta` | `12px` | Dimension / Scale Token |
| `--ui-title` | `32px` | Dimension / Scale Token |
| `--site-edge` | `32px` | Dimension / Scale Token |
| `--panel-pad` | `24px` | Layout / Spatial Grid Token |
| `--content-width` | `1000px` | Layout / Spatial Grid Token |
| `--ui-blur` | `24px` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.studio-power-pending> — `verasfawaz-com`)**:
   - Landmark `<header class="studio-power-pending">` hosting `Véras Fawaz` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-studio-ready="true"`, `data-arrival="waiting"`, `data-arrival-navigation="visible"`, `data-arrival-from="night"`), and stylesheet rule `before { display:none!important }`.
2. **Hero Stage & Focal Lead (<section.temporary-panel> — `Véras Fawaz`)**:
   - Landmark `<section class="temporary-panel">` presenting display lead `Véras Fawaz` and copy excerpt *"Skip to the archive"* over `#202426` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.studio-ui> — `Skip to the archive`)**:
   - Landmark `<section class="studio-ui">` rendering section `Skip to the archive` with copy *"Studio opnieuw laden"*, asset references (`packs.js`, `wide-blackout.webp`, `startup-input-game-exit-20261018.js`, `apple-touch-icon.png`), and grid rule `header::after { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.compact-music-ui> — `Studio opnieuw laden`)**:
   - Landmark `<section class="compact-music-ui">` framing `Studio opnieuw laden` and `PLEASE TOUCH EVERYTHING` (*"PLEASE TOUCH EVERYTHING"*) with `#f7f7f2` surface cards, `#24292b` accents, and `header { background:none!important }`.
5. **Colophon & Global Directory Footer (<footer.context-footer-ui> — `https://verasfawaz.com`)**:
   - Landmark `<footer class="context-footer-ui">` anchoring `Véras Fawaz` footer links (`Overview · Index · Archive · About · Contact`), copy *"View record & tracks"*, and `#202020` structural dividers.
