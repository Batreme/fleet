# UI & UX Architecture: bybang-co

## Overview & Design Identity
- **Target**: `bybang-co` (**Estudio Bang · Architecture, Interiors, Objects & Digital Media**)
- **Production URL**: [https://bybang.co/](https://bybang.co/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f5f5f2` canvas, `#141414` ink, `#141414` accent)
- **Summary**: Estudio Bang is a Barcelona-based architecture studio working across architecture, interiors, objects and digital media. We create spaces...
- **Total Clean CSS Variables Extracted**: `39` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Mono`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 32px`, `line-height: .95`, `letter-spacing: -.02em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`)
- **Body Copy**: rule `p` (`font-size: 16px`, `line-height: 1.4`, `letter-spacing: -.02em`)
- **Metadata & Labels**: CSS variables `--mono: "Geist Mono", ui-monospace, monospace`; rule `small` (`font-size: 11px`, `line-height: 1`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f5f2` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#e1e1e1` | `var(--panel)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d7d7d0` | `var(--panel-dark)` in `:root` |
| **Interactive Accent / Highlight** | `#141414` | `var(--text)` in `:root` |
| **Secondary / Muted Copy** | `#946ec4` | `var(--accent)` in `:root` |
| **Structural Hairline Border** | `#ffffff` | `var(--site-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#f5f5f2` | Canvas / Surface Token |
| `--panel` | `#e1e1e1` | Color / Atmospheric Token |
| `--panel-dark` | `#d7d7d0` | Canvas / Surface Token |
| `--text` | `#141414` | Typography Ink Token |
| `--muted` | `rgba(20, 20, 20, .3)` | Color / Atmospheric Token |
| `--border` | `rgba(20, 20, 20, .08)` | Elevation / Border Token |
| `--accent` | `#946ec4` | Brand / Palette Token |
| `--shadow` | `0 24px 80px rgba(11, 12, 11, .12)` | Elevation / Border Token |
| `--mono` | `"Geist Mono", ui-monospace, monospace` | Typography / Scale Token |
| `--sans` | `"Geist", "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--stable-viewport-height` | `100vh` | Layout / Spatial Grid Token |
| `--not-found-row-height` | `clamp(50px, 5.28vw, 76px)` | Layout / Spatial Grid Token |
| `--not-found-type-size` | `clamp(48px, 5.14vw, 74px)` | Typography / Scale Token |
| `--site-bg` | `#ffffff` | Canvas / Surface Token |
| `--site-ink` | `#141414` | Typography Ink Token |
| `--site-muted` | `rgba(20, 20, 20, .3)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-chrome> — `bybang-co`)**:
   - Landmark `<header class="site-chrome">` hosting `Estudio Bang · Architecture, Interio` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-cursor-target="logo"`, `data-cursor-target="logo"`, `data-entry-signal="0"`, `data-filter="all"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<main.site-home> — `Estudio Bang · Architecture, Inter`)**:
   - Landmark `<main class="site-home">` presenting display lead `Estudio Bang · Architecture, Interiors, Objects ` and copy excerpt *"BCN 16 : 01 BUE 12 : 01"* over `#f5f5f2` canvas and `#141414` ink.
3. **Primary Showcase & Content Grid (<main.site-home> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="site-home">` rendering section `Featured Work & Interactive Showcase` with copy *"Copyright Estudio Bang® 2026 · Legal & Privacy · Made by Tremendo"*, asset references (`intro-01.webp`, `intro-02.webp`, `intro-03.webp`, `intro-04.webp`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<main.site-home> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="site-home">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Copyright Estudio Bang® 2026"*) with `#d7d7d0` surface cards, `#141414` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.custom-cursor__shape> — `https://bybang.co/`)**:
   - Landmark `<footer class="custom-cursor__shape">` anchoring `Estudio Bang · Architecture, Int` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#ffffff` structural dividers.
