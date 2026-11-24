---
title: "UI & UX Architecture: www-norddeutscher-figuralchor-de"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-norddeutscher-figuralchor-de

## Overview & Design Identity
- **Target**: `www-norddeutscher-figuralchor-de` (**Norddeutscher Figuralchor Hannover — Kammerchor seit 1981**)
- **Production URL**: [https://www.norddeutscher-figuralchor.de](https://www.norddeutscher-figuralchor.de)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×5796px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#c9a85e` accent)
- **Summary**: Norddeutscher Figuralchor Hannover — semiprofessioneller Kammerchor seit 1981 unter Jörg Straube. Konzerte, CD-Einspielungen und Mitsinge...
- **Total Clean CSS Variables Extracted**: `24` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Syne`
- **Body Font Stack**: `Syne`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 0px`, `line-height: 0px`, `font-weight: 400`); CSS variables `--font-display: "Playfair Display", Georgia, serif`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 123.84px`, `line-height: 185.76px`, `font-weight: 400`); rule `h2` (`font-size: 8.6vw`, `letter-spacing: 0`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 0px`, `line-height: 0px`, `font-weight: 400`); CSS variables `--font-body: "Syne", system-ui, sans-serif`; rule `body` (`font-size: 0`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 43.2px`, `line-height: 64.8px`, `font-weight: 400`); CSS variables `--font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e6cac7` | live computed `header` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#c9a85e` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#c9a85e` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e3e3e3` | `#navi-top { border: #e3e3e3 }` |
| **Variable Token (`--color-gold`)** | `#bd7716` | `var(--color-gold)` in `:root` |
| **Variable Token (`--color-charcoal`)** | `#404040` | `var(--color-charcoal)` in `:root` |
| **Variable Token (`--color-conductor`)** | `#d3d1de` | `var(--color-conductor)` in `:root` |
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
   - Landmark `<header class="bg-rose relative">` (`1425x679px`) hosting `Norddeutscher Figuralchor Hannover —` navigation (`Home · Der Chor · Der Dirigent · Konzerte · CDs`), DOM attributes (`data-infos="konzerte.html"`, `data-email="a29udGFrdEBub3JkZGV1d..."`, `data-email="a29udGFrdEBub3JkZGV1d..."`, `data-email="a29udGFrdEBub3JkZGV1d..."`), and stylesheet rule `file-selector-button { box-sizing: border-box; margin: 0; padding: 0; border: 0 solid; }`.
2. **Hero Stage & Focal Lead (<section.bg-white> — `Norddeutscher Figuralchor — Kammer`)**:
   - Landmark `<section class="bg-white overflow-hidden">` presenting display lead `Norddeutscher Figuralchor — Kammerchor aus Hannover` and copy excerpt *"Der Maßstab seit 1981"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.bg-white:nth(2)> — `Der Maßstab seit 1981`)**:
   - Landmark `<section class="bg-white">` rendering section `Der Maßstab seit 1981` with copy *"wird Teil von einem."*, asset references (`favicon-home.svg`, `favicon.ico`, `apple-touch-icon.png`, `PlayfairDisplay-Regular.woff2`), and grid rule `hr { height: 0; color: inherit; border-top-width: 1px; }`.
4. **Interactive Detail & Feature Matrix (<section.bg-charcoal> — `wird Teil von einem.`)**:
   - Landmark `<section class="bg-charcoal">` framing `wird Teil von einem.` and `Der Norddeutsche Figuralchor gestaltet seit 1981` (*"Der Norddeutsche Figuralchor gestaltet seit 1981 Konzerte, die Me"*) with `#e6cac7` surface cards, `#c9a85e` accents, and `h6 { font-size: inherit; font-weight: inherit; }`.
5. **Colophon & Global Directory Footer (<footer.bg-ink> — `https://www.norddeutscher-figuralchor.de`)**:
   - Landmark `<footer class="bg-ink">` anchoring `Norddeutscher Figuralchor Hannov` footer links (`Home · Der Chor · Der Dirigent · Konzerte · CDs`), copy *"// 5 x Echo Klassik // Deutscher Chorwettbewerb // Brahms-We"*, and `#e3e3e3` structural dividers.
