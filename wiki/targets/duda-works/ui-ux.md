# UI & UX Architecture: duda-works

## Overview & Design Identity
- **Target**: `duda-works` (**Duda Lima**)
- **Production URL**: [http://duda.works](http://duda.works)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#060403` canvas, `#fff` ink, `#fff` accent)
- **Summary**: Production web application and digital experience at http://duda.works.
- **Total Clean CSS Variables Extracted**: `5` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Aeonik Pro`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `12px`, `11px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `12px`, `11px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `12px`, `11px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `12px`, `11px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#060403` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--text)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#060403` | Canvas / Surface Token |
| `--text` | `#fff` | Typography Ink Token |
| `--text-dim` | `rgba(255, 255, 255, 0.62)` | Typography Ink Token |
| `--border` | `rgba(255, 255, 255, 0.1)` | Elevation / Border Token |
| `--border-strong` | `rgba(255, 255, 255, 0.28)` | Elevation / Border Token |
| `--duda-works-bg` | `#060403` | Canvas Substrate (from `var(--bg)` in `:root`) |
| `--duda-works-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |
| `--duda-works-surface` | `#060403` | Surface Substrate (stylesheet-derived) |
| `--duda-works-accent` | `#fff` | Interactive Accent (stylesheet-derived) |
| `--duda-works-muted` | `#fff` | Secondary Ink (stylesheet-derived) |
| `--duda-works-border` | `#fff` | Structural Border (stylesheet-derived) |
| `--duda-works-container` | `1400px` | Container Bound (stylesheet-derived) |
| `--duda-works-gap` | `16px` | Grid Gutter (stylesheet-derived) |
| `--duda-works-pad` | `24px` | Lateral Padding (stylesheet-derived) |
| `--duda-works-ease` | `cubic-bezier(0.22,1,0.36,1)` | Primary Easing Function |
| `--duda-works-radius` | `8px` | Corner Radius (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `duda-works`)**:
   - Landmark `<header class="site-header">` hosting `Duda Lima` navigation (`P r o j e c t s · A b o u t`), DOM attributes (`data-char="P"`, `data-char="r"`, `data-char="o"`, `data-char="j"`), and stylesheet rule `view-transition { navigation: auto; }`.
2. **Hero Stage & Focal Lead (<section.mwg_effect107> — `Duda Lima`)**:
   - Landmark `<section class="mwg_effect107">` presenting display lead `Duda Lima` and copy excerpt *"Production web application and digital experience at http://duda."* over `#060403` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.mwg_effect107> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="mwg_effect107">` rendering section `Featured Work & Interactive Showcase` with copy *"Duda Lima"*, asset references (`hotjar-6782564.js`, `modules.47ae0ae40a423a71e31f.js`, `02.png`, `24.png`), and grid rule `html { background: var(--bg); }`.
4. **Interactive Detail & Feature Matrix (<section.mwg_effect107> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="mwg_effect107">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#060403` surface cards, `#fff` accents, and `.wordmark svg { display: block; filter: drop-shadow(0 1px 4px rgba(0, 0, 0, 0.75)) drop-... }`.
5. **Colophon & Global Directory Footer (<footer.icon-menu> — `http://duda.works`)**:
   - Landmark `<footer class="icon-menu">` anchoring `Duda Lima` footer links (`P r o j e c t s · A b o u t`), copy *"Technical Architecture & Narrative"*, and `#fff` structural dividers.
