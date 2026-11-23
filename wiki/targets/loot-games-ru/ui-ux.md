---
title: "UI & UX Architecture: loot-games-ru"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: loot-games-ru

## Overview & Design Identity
- **Target**: `loot-games-ru` (**LOOT – награды в играх за активность в реальной жизни**)
- **Production URL**: [https://loot-games.ru](https://loot-games.ru)
- **Final Redirected URL**: [https://loot.ru/](https://loot.ru/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ec5a00`)
- **Summary**: Получайте лутсы за обучение, тренировки, музыку, фильмы и книги. Обменивайте их на предметы и награды в 4500+ играх.
- **Total Clean CSS Variables Extracted**: `8` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `SF Pro`
- **Body Font Stack**: `SF Pro`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 13.7143px`, `line-height: normal`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 78.8571px`, `line-height: 70.9714px`, `font-weight: 500`); rule `h2` (`font-size: 11.5rem`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 6.85714px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 1.6rem`, `line-height: 1.2`, `font-weight: 500`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 6.85714px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#303030` | `.plans .plans-item.is--active { background: #303030 }` |
| **Interactive Accent / Highlight** | `#ec5a00` | `.start .start-card__footer-button { color: #ec5a00 }` |
| **Secondary / Muted Copy** | `#ec5a00` | `item li.card-second-footer__hid... { color: #ec5a00 }` |
| **Structural Hairline Border** | `#371500` | `.how .how-meta .how-center-wrap { border: #371500 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--energy-ease` | `cubic-bezier(.32, .72, 0, 1)` | Motion / Easing Token |
| `--smooth-ease` | `cubic-bezier(.625, .05, 0, 1)` | Motion / Easing Token |
| `--fade-ease` | `cubic-bezier(.25, .1, .25, 1)` | Motion / Easing Token |
| `--flicker-fg` | `#fff` | Typography Ink Token |
| `--flicker-bg` | `#000` | Canvas / Surface Token |
| `--flicker-duration` | `.3s` | Motion / Easing Token |
| `--img` | `url("/assets/images/icon-09.avif")` | Design System Custom Token |
| `--hue` | `0` | Design System Custom Token |
| `--loot-games-ru-bg` | `#000000` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--loot-games-ru-ink` | `#ffffff` | Primary Typography Ink (computed-derived) |
| `--loot-games-ru-surface` | `#303030` | Surface Substrate (computed-derived) |
| `--loot-games-ru-accent` | `#ec5a00` | Interactive Accent (computed-derived) |
| `--loot-games-ru-muted` | `#ec5a00` | Secondary Ink (computed-derived) |
| `--loot-games-ru-border` | `#371500` | Structural Border (computed-derived) |
| `--loot-games-ru-container` | `1440px` | Container Bound (computed-derived) |
| `--loot-games-ru-gap` | `2rem` | Grid Gutter (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.navbar> — `loot-games-ru`)**:
   - Landmark `<header class="navbar">` (`1440px`) hosting `LOOT – награды в играх за активность` navigation (`НАЧНИТЕ · ГЛАВНАЯ · ПАРТНЕРАМ · ПЛАНЫ · КАК ЭТО РАБОТАЕТ`), DOM attributes (`data-astro-cid-l7arcky5`, `data-menu-toggle`, `data-page-progress`, `data-scrollto="0"`), and stylesheet rule `.main-wrap { width:100%;height:auto }`.
2. **Hero Stage & Focal Lead (<section.main-wrap> — `ТВОЯ ЖИЗНЬ – ТВОЙ LOOT`)**:
   - Landmark `<section class="main-wrap">` presenting display lead `ТВОЯ ЖИЗНЬ – ТВОЙ LOOT` and copy excerpt *"Спорт, кино, книги, музыка: все, чем вы и так заняты, превращаетс"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.main-wrap__sticky> — `Что такое LOOT?`)**:
   - Landmark `<section class="main-wrap__sticky">` rendering section `Что такое LOOT?` with copy *"LOOT связывает реальную активность людей с наградами внутри игр –"*, asset references (`apple-touch-icon.png`, `favicon-32x32.png`, `favicon-16x16.png`, `favicon.ico`), and grid rule `.main-wrap__sticky { z-index:4;grid-template-areas:"section";width:100%;height:100svh;display... }`.
4. **Interactive Detail & Feature Matrix (<section.hero> — `Лутсы – внутренняя валюта LOOT`)**:
   - Landmark `<section class="hero is--section">` framing `Лутсы – внутренняя валюта LOOT` and `Выбирайте награду` (*"реальную активность людей"*) with `#303030` surface cards, `#ec5a00` accents, and `.is--section { opacity:0;pointer-events:none;grid-area:section;height:100svh }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://loot-games.ru`)**:
   - Landmark `<footer class="footer is--home">` anchoring `LOOT – награды в играх за активн` footer links (`НАЧНИТЕ · ГЛАВНАЯ · ПАРТНЕРАМ · ПЛАНЫ · КАК ЭТО РАБОТАЕТ`), copy *"ЗАГРУЖАЕМ НОВЫЙ МИР"*, and `#371500` structural dividers.
