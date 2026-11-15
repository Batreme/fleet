# UI & UX Architecture: loot-games-ru

## Overview & Design Identity
- **Target**: `loot-games-ru` (**LOOT – награды в играх за активность в реальной жизни**)
- **Production URL**: [https://loot-games.ru](https://loot-games.ru)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#fffc`)
- **Summary**: Получайте лутсы за обучение, тренировки, музыку, фильмы и книги. Обменивайте их на предметы и награды в 4500+ играх.
- **Total Clean CSS Variables Extracted**: `8` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Atkinson`
- **Body Font Stack**: `SF Pro`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.47619vw`, `clamp(3px,.520833vw + .0109375rem...`, `2.48756vw`, `1.81818vw`, `1.6rem`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 11.5rem`, `font-weight: 500`)
- **Body Copy**: rule `p` (`font-size: 1.6rem`, `line-height: 1.2`, `font-weight: 500`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.47619vw`, `clamp(3px,.520833vw + .0109375rem...`, `2.48756vw`, `1.81818vw`, `1.6rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--flicker-fg)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--flicker-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffa500` | `.loading-layer svg circle { stroke: orange }` (`#ffa500`) |
| **Interactive Accent / Highlight** | `#fffc` | `.tagline { color: #fffc }` |
| **Secondary / Muted Copy** | `#ec5a00` | `.is--orange:before { background: #ec5a00 }` |
| **Structural Hairline Border** | `#fff9` | `.calc .calc-meta__desc { color: #fff9 }` |

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
| `--loot-games-ru-bg` | `#fff` | Canvas Substrate (from `var(--flicker-fg)` in `:root`) |
| `--loot-games-ru-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |
| `--loot-games-ru-surface` | `#ffa500` | Surface Substrate (stylesheet-derived) |
| `--loot-games-ru-accent` | `#fffc` | Interactive Accent (stylesheet-derived) |
| `--loot-games-ru-muted` | `#ec5a00` | Secondary Ink (stylesheet-derived) |
| `--loot-games-ru-border` | `#fff9` | Structural Border (stylesheet-derived) |
| `--loot-games-ru-container` | `3840px` | Container Bound (stylesheet-derived) |
| `--loot-games-ru-gap` | `1rem` | Grid Gutter (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.navbar> — `loot-games-ru`)**:
   - Landmark `<header class="navbar">` hosting `LOOT – награды в играх за активность` navigation (`НАЧНИТЕ · ГЛАВНАЯ · ПАРТНЕРАМ · ПЛАНЫ · КАК ЭТО РАБОТАЕТ`), DOM attributes (`data-astro-cid-l7arcky5`, `data-menu-toggle`, `data-page-progress`, `data-scrollto="0"`), and stylesheet rule `html { width:100%;height:100svh;position:fixed;top:0;left:0;overflow:hidden }`.
2. **Hero Stage & Focal Lead (<section.main-wrap> — `ТВОЯ ЖИЗНЬ – ТВОЙ LOOT`)**:
   - Landmark `<section class="main-wrap">` presenting display lead `ТВОЯ ЖИЗНЬ – ТВОЙ LOOT` and copy excerpt *"ОГРН 1197746200123 · ИНН 7707428570"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.main-wrap__sticky> — `Что такое LOOT?`)**:
   - Landmark `<section class="main-wrap__sticky">` rendering section `Что такое LOOT?` with copy *"141590, Московская обл., г. о. Химки, г. Химки, Транспортный пр-д"*, asset references (`apple-touch-icon.png`, `favicon-32x32.png`, `favicon-16x16.png`, `favicon.ico`), and grid rule `.scroller-wrapper.is--seq-lock { touch-action:none }`.
4. **Interactive Detail & Feature Matrix (<section.hero> — `Лутсы – внутренняя валюта LOOT`)**:
   - Landmark `<section class="hero is--section">` framing `Лутсы – внутренняя валюта LOOT` and `5 км` (*"partners@loot-games.ru"*) with `#ffa500` surface cards, `#fffc` accents, and `.scroller-content { min-height:100% }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://loot-games.ru`)**:
   - Landmark `<footer class="footer is--home">` anchoring `LOOT – награды в играх за активн` footer links (`НАЧНИТЕ · ГЛАВНАЯ · ПАРТНЕРАМ · ПЛАНЫ · КАК ЭТО РАБОТАЕТ`), copy *"Свяжитесь с командой"*, and `#fff9` structural dividers.
