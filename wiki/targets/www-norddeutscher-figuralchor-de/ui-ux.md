# UI & UX Architecture: www-norddeutscher-figuralchor-de

## Overview & Design Identity
- **Target**: `www-norddeutscher-figuralchor-de` (**Norddeutscher Figuralchor Hannover — Kammerchor seit 1981**)
- **Production URL**: [https://www.norddeutscher-figuralchor.de](https://www.norddeutscher-figuralchor.de)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#000000` accent)
- **Summary**: Norddeutscher Figuralchor Hannover — semiprofessioneller Kammerchor seit 1981 unter Jörg Straube. Konzerte, CD-Einspielungen und Mitsinge...
- **Total Clean CSS Variables Extracted**: `24` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Playfair Display`
- **Body Font Stack**: `Syne`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--font-display: "Playfair Display", Georgia, serif`
- **Section Heading (`H2`)**: rule `h2` (`font-size: 8.6vw`, `letter-spacing: 0`, `font-weight: 400`)
- **Body Copy**: CSS variables `--font-body: "Syne", system-ui, sans-serif`; rule `body` (`font-size: 0`)
- **Metadata & Labels**: CSS variables `--font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#e6cac7` | `var(--color-rose)` in `:root` |
| **Elevated Surface / Card Substrate** | `#bd7716` | `var(--color-gold)` in `:root` |
| **Interactive Accent / Highlight** | `#000000` | `var(--color-ink)` in `:root` |
| **Secondary / Muted Copy** | `#404040` | `var(--color-charcoal)` in `:root` |
| **Structural Hairline Border** | `#d3d1de` | `var(--color-conductor)` in `:root` |
| **Variable Token (`--color-silver`)** | `#d6d6d6` | `var(--color-silver)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji",` | Typography / Scale Token |
| `--font-mono` | `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",` | Typography / Scale Token |
| `--color-white` | `#ffffff` | Canvas / Surface Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--ease-in-out` | `cubic-bezier(0.4, 0, 0.2, 1)` | Motion / Easing Token |
| `--default-transition-duration` | `150ms` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(0.4, 0, 0.2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-rose` | `#e6cac7` | Brand / Palette Token |
| `--color-gold` | `#bd7716` | Brand / Palette Token |
| `--color-ink` | `#000000` | Typography Ink Token |
| `--color-charcoal` | `#404040` | Brand / Palette Token |
| `--color-conductor` | `#d3d1de` | Brand / Palette Token |
| `--color-silver` | `#d6d6d6` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bg-rose> — `www-norddeutscher-figuralchor-de`)**:
   - Landmark `<header class="bg-rose relative">` hosting `Norddeutscher Figuralchor Hannover —` navigation (`Home · Der Chor · Der Dirigent · Konzerte · CDs`), DOM attributes (`data-infos="konzerte.html"`, `data-email="a29udGFrdEBub3JkZGV1d..."`, `data-email="a29udGFrdEBub3JkZGV1d..."`, `data-email="a29udGFrdEBub3JkZGV1d..."`), and stylesheet rule `file-selector-button { box-sizing: border-box; margin: 0; padding: 0; border: 0 solid; }`.
2. **Hero Stage & Focal Lead (<section.bg-white> — `Norddeutscher Figuralchor — Kammer`)**:
   - Landmark `<section class="bg-white overflow-hidden">` presenting display lead `Norddeutscher Figuralchor — Kammerchor aus Hannover` and copy excerpt *"Zum Hauptinhalt springen"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.bg-white> — `D e r M a ẞ s t a b`)**:
   - Landmark `<section class="bg-white">` rendering section `D e r M a ẞ s t a b` with copy *"Der Maßstab seit 1981"*, asset references (`favicon-home.svg`, `favicon.ico`, `apple-touch-icon.png`, `PlayfairDisplay-Regular.woff2`), and grid rule `hr { height: 0; color: inherit; border-top-width: 1px; }`.
4. **Interactive Detail & Feature Matrix (<section.bg-charcoal> — `S e i t 1 9 8 1 .`)**:
   - Landmark `<section class="bg-charcoal">` framing `S e i t 1 9 8 1 .` and `wird Teil von einem.` (*"wird Teil von einem."*) with `#bd7716` surface cards, `#000000` accents, and `h6 { font-size: inherit; font-weight: inherit; }`.
5. **Colophon & Global Directory Footer (<footer.bg-ink> — `https://www.norddeutscher-figuralchor.de`)**:
   - Landmark `<footer class="bg-ink">` anchoring `Norddeutscher Figuralchor Hannov` footer links (`Home · Der Chor · Der Dirigent · Konzerte · CDs`), copy *"Der Norddeutsche Figuralchor gestaltet seit 1981 Konzerte, d"*, and `#d3d1de` structural dividers.
