# UI & UX Architecture: davidcata-com_en-musica

## Overview & Design Identity
- **Target**: `davidcata-com_en-musica` (**Music — “Queridos todos:” and “Origen”, by David Catá**)
- **Production URL**: [https://davidcata.com/en/musica/](https://davidcata.com/en/musica/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#1f3a78` / `#EDE7DE`)
- **Summary**: The music of David Catá: his new album “Queridos todos:” (20 November 2026), pre-order signed and dedicated, and the instrumental album “...
- **Total Clean CSS Variables Extracted**: `12` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Caveat`
- **Body Font Stack**: `Caveat Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.55rem`, `line-height: 1.15`, `letter-spacing: -.02em`)
- **Body Copy**: rule `p` (`font-size: 15px`, `line-height: 1.75`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#1f3a78` | `var(--tinta-pluma)` in `:root` |
| **Primary Typography Ink** | `#e5e7eb` | `:before { border: #e5e7eb }` |
| **Elevated Surface / Card Substrate** | `#9ca3af` | `textarea::-moz-placeholder { color: #9ca3af }` |
| **Interactive Accent / Highlight** | `#EDE7DE` | `.fill-hueso { fill: #EDE7DE }` |
| **Secondary / Muted Copy** | `#fff` | `.fill-white { fill: #fff }` |
| **Structural Hairline Border** | `#F2EEE7` | `html { background: #F2EEE7 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--f-titular` | `"Fraunces",Georgia,serif` | Dimension / Scale Token |
| `--f-texto` | `"Karla",system-ui,sans-serif` | Typography Ink Token |
| `--papel` | `242 238 231` | Design System Custom Token |
| `--sala` | `10 9 8` | Design System Custom Token |
| `--hilo` | `158 43 37` | Design System Custom Token |
| `--renglon` | `2.25rem` | Dimension / Scale Token |
| `--tinta-pluma` | `#1f3a78` | Canvas / Surface Token |
| `--f-mano` | `"Caveat","Caveat Fallback"` | Design System Custom Token |
| `--marca` | `29, 185, 84` | Design System Custom Token |
| `--movil` | `0% 50%` | Dimension / Scale Token |
| `--pos` | `50% 50%` | Dimension / Scale Token |
| `--acento` | `204, 139, 61` | Design System Custom Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--davidcata-com-en-bg` | `#1f3a78` | Canvas Substrate (from `var(--tinta-pluma)` in `:root`) |
| `--davidcata-com-en-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.mundo-calido> — `davidcata-com_en-musica`)**:
   - Landmark `<header class="mundo-calido mundo-musica">` hosting `Music — “Queridos todos:” and “Orige` navigation (`In cinemas · Albums ▾ · Origen Album · 2023 · Listen · Concerts`), DOM attributes (`data-mundo="sala"`, `data-hero="oscuro"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Queridos todos:`)**:
   - Landmark `<section class="relative flex">` presenting display lead `Queridos todos:` and copy excerpt *"Queridos todos: New album · 20.11.2026"* over `#1f3a78` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `His theme in “Arriba Tutto”`)**:
   - Landmark `<section class="relative overflow-clip">` rendering section `His theme in “Arriba Tutto”` with copy *"New album · 20.11.2026"*, asset references (`cd-queridos-limpio-240.webp`, `portada-240.webp`, `amazonmusic.png`, `07c1226183551f0e.css`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.border-t> — `Three ways to experience it`)**:
   - Landmark `<section class="border-t py-20">` framing `Three ways to experience it` and `Two albums. One memory.` (*"Origen Album · 2023"*) with `#9ca3af` surface cards, `#EDE7DE` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://davidcata.com/en/musica/`)**:
   - Landmark `<footer class="border-t bg-papel">` anchoring `Music — “Queridos todos:” and “O` footer links (`In cinemas · Albums ▾ · Origen Album · 2023 · Listen · Concerts`), copy *"Pre-order signed · € 20"*, and `#F2EEE7` structural dividers.
