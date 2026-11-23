---
title: "UI Prompt Blueprint: loot-games-ru"
date: 2026-11-23
captured_at: 2026-11-23
target: "loot-games-ru"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ec5a00`)"
---

# UI Design System & Master Generation Blueprint: loot-games-ru

> **LOOT – награды в играх за активность в реальной жизни** (https://loot-games.ru) — Получайте лутсы за обучение, тренировки, музыку, фильмы и книги. Обменивайте их на предметы и награды в 4500+ играх.

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **LOOT – награды в играх за активность в реальной жизни** (`https://loot-games.ru`). Получайте лутсы за обучение, тренировки, музыку, фильмы и книги. Обменивайте их на предметы и награды в 4500+ играх.
- **Final Redirected URL**: [https://loot.ru/](https://loot.ru/)
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ec5a00`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ec5a00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `SF Pro` for display copy (`ТВОЯ ЖИЗНЬ – ТВОЙ LOOT`) with `SF Pro` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 2rem`, padding `30.8571px`) with `cubic-bezier(.625,.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `30.8571px` lateral canvas padding with `2rem` grid gap.
- **Border Radius Scale**: `2rem`, `50%`, `4rem`, `2.5rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `30.8571px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (orientation:landscape) and (width<=1000px)`, `@media screen and (width<=1000px) and (orientation:landscape)`, `@media screen and (width<=481px) and (orientation:portrait)`, `@media screen and (width>=482px) and (orientation:portrait)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#303030` | `.plans .plans-item.is--active { background: #303030 }` |
| **Interactive Accent / Highlight** | `#ec5a00` | `.start .start-card__footer-button { color: #ec5a00 }` |
| **Secondary / Muted Copy** | `#ec5a00` | `item li.card-second-footer__hid... { color: #ec5a00 }` |
| **Structural Hairline Border** | `#371500` | `.how .how-meta .how-center-wrap { border: #371500 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
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

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `SF Pro`.
- **Primary Body Stack**: `SF Pro`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 13.7143px`, `line-height: normal`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 78.8571px`, `line-height: 70.9714px`, `font-weight: 500`); rule `h2` (`font-size: 11.5rem`, `font-weight: 500`).
- **Body Copy**: live computed `body` (`font-size: 6.85714px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 1.6rem`, `line-height: 1.2`, `font-weight: 500`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 6.85714px`, `line-height: normal`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.625,0,.875,0)`, `cubic-bezier(.32,.72,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.button-v2-text[data-astro-cid-en...`**: `transition: opacity .4s ease-out` extracted from `loot-games-ru` stylesheet.
- **Selector `ton-v2-icon__arrow[data-astro-cid...`**: `transition: transform .4s cubic-bezier(.625,.05,0,1)` extracted from `loot-games-ru` stylesheet.
- **Selector `.how .how-meta .how-right__item`**: `transition: background .6s ease-out, scale .4s 50ms var(--smooth-ease)` extracted from `loot-games-ru` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.625,.05,0,1)`)**: Governs interactive state transitions across `<header.navbar>` and `<section.main-wrap__sticky>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — LOOT – награды в играх за активность в реа │
│ ====================================================================== │
│ [ <header.navbar> (1440px)            | НАЧНИТЕ · ГЛАВНАЯ · ПАРТНЕРА ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.main-wrap> (w=1440px)                         | │
│ | H1: ТВОЯ ЖИЗНЬ – ТВОЙ LOOT                                         | │
│ | Substrate: #000000 | Ink: #ffffff | Accent: #ec5a00                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.main-wrap__sticky) max-w: 1440px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Что такое LOOT?              |  | Лутсы – внутренняя валюта LO | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.hero>) — Выбирайте награду                 | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | https://loot-games.ru                │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 2rem)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.navbar>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.main-wrap>) — 390px Vertical Lead             | │
│ | H1: ТВОЯ ЖИЗНЬ – ТВОЙ LOOT                                         | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.main-wrap__st) — 1-Col Stack              | │
│ | [ Item 1: Что такое LOOT?                                        ] | │
│ | [ Item 2: Лутсы – внутренняя валюта LOOT                         ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.hero>) — 1-Col (Выбирайте награду)          | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
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

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: loot-games-ru (LOOT – награды в играх за активность в реальной жизни)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `loot-games-ru` (**LOOT – награды в играх за активность в реальной жизни** — `https://loot-games.ru`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ec5a00`).
- **Identity & Domain Context**: Получайте лутсы за обучение, тренировки, музыку, фильмы и книги. Обменивайте их на предметы и награды в 4500+ играх.
- **Primary Substrate**: `#000000` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#ec5a00`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ec5a00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `SF Pro` for display copy (`ТВОЯ ЖИЗНЬ – ТВОЙ LOOT`) with `SF Pro` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 2rem`, padding `30.8571px`) with `cubic-bezier(.625,.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `loot-games-ru` in your global stylesheet:

:root {
  /* LOOT – награды в играх за активность в реальной жизни (loot-games-ru) — Live-Grounded CSS Variables */
  --energy-ease: cubic-bezier(.32, .72, 0, 1); /* Motion / Easing Token (loot-games-ru) */
  --smooth-ease: cubic-bezier(.625, .05, 0, 1); /* Motion / Easing Token (loot-games-ru) */
  --fade-ease: cubic-bezier(.25, .1, .25, 1); /* Motion / Easing Token (loot-games-ru) */
  --flicker-fg: #fff; /* Typography Ink Token (loot-games-ru) */
  --flicker-bg: #000; /* Canvas / Surface Token (loot-games-ru) */
  --flicker-duration: .3s; /* Motion / Easing Token (loot-games-ru) */
  --img: url("/assets/images/icon-09.avif"); /* Design System Custom Token (loot-games-ru) */
  --hue: 0; /* Design System Custom Token (loot-games-ru) */
  --loot-games-ru-bg: #000000; /* Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) (loot-games-ru) */
  --loot-games-ru-ink: #ffffff; /* Primary Typography Ink (computed-derived) (loot-games-ru) */
  --loot-games-ru-surface: #303030; /* Surface Substrate (computed-derived) (loot-games-ru) */
  --loot-games-ru-accent: #ec5a00; /* Interactive Accent (computed-derived) (loot-games-ru) */
  --loot-games-ru-muted: #ec5a00; /* Secondary Ink (computed-derived) (loot-games-ru) */
  --loot-games-ru-border: #371500; /* Structural Border (computed-derived) (loot-games-ru) */
  --loot-games-ru-container: 1440px; /* Container Bound (computed-derived) (loot-games-ru) */
  --loot-games-ru-gap: 2rem; /* Grid Gutter (computed-derived) (loot-games-ru) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#303030` — grounded in `.plans .plans-item.is--active { background: #303030 }`
- **Interactive Accent / Highlight**: `#ec5a00` — grounded in `.start .start-card__footer-button { color: #ec5a00 }`
- **Secondary / Muted Copy**: `#ec5a00` — grounded in `item li.card-second-footer__hid... { color: #ec5a00 }`
- **Structural Hairline Border**: `#371500` — grounded in `.how .how-meta .how-center-wrap { border: #371500 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `30.8571px` lateral canvas padding with `2rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `30.8571px` horizontal padding
- **Media Queries**: `@media (orientation:landscape) and (width<=1000px)`, `@media screen and (width<=1000px) and (orientation:landscape)`, `@media screen and (width<=481px) and (orientation:portrait)`, `@media screen and (width>=482px) and (orientation:portrait)`
- **Corner Radii**: `2rem`, `50%`, `4rem`, `2.5rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `SF Pro`
- **Body Font Stack**: `SF Pro`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 13.7143px`, `line-height: normal`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 78.8571px`, `line-height: 70.9714px`, `font-weight: 500`); rule `h2` (`font-size: 11.5rem`, `font-weight: 500`)
- **Body Copy Rule**: live computed `body` (`font-size: 6.85714px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 1.6rem`, `line-height: 1.2`, `font-weight: 500`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 6.85714px`, `line-height: normal`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `loot-games-ru` (`LOOT – награды в играх за активность в реальной жизни`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.navbar> — `loot-games-ru`)**:
   - DOM & Selectors: Landmark `<header class="navbar">` (`1440px`) hosting `LOOT – награды в играх за активность` navigation (`НАЧНИТЕ · ГЛАВНАЯ · ПАРТНЕРАМ · ПЛАНЫ · КАК ЭТО РАБОТАЕТ`), DOM attributes (`data-astro-cid-l7arcky5`, `data-menu-toggle`, `data-page-progress`, `data-scrollto="0"`), and stylesheet rule `.main-wrap { width:100%;height:auto }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.navbar> — `loot-games-ru`)` (`loot-games-ru`) adapts across `@media (orientation:landscape) and (width<=1000px)`, `@media screen and (width<=1000px) and (orientation:landscape)`, `@media screen and (width<=481px) and (orientation:portrait)`, `@media screen and (width>=482px) and (orientation:portrait)` with `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.625,0,.875,0)`, `cubic-bezier(.32,.72,0,1)` transitions and links `НАЧНИТЕ · ГЛАВНАЯ · ПАРТНЕРАМ · ПЛАНЫ · КАК ЭТО РАБОТАЕТ`.
2. **Hero Stage & Focal Lead (<section.main-wrap> — `ТВОЯ ЖИЗНЬ – ТВОЙ LOOT`)**:
   - DOM & Selectors: Landmark `<section class="main-wrap">` presenting display lead `ТВОЯ ЖИЗНЬ – ТВОЙ LOOT` and copy excerpt *"Спорт, кино, книги, музыка: все, чем вы и так заняты, превращаетс"* over `#000000` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#000000` background with `#ffffff` headline `ТВОЯ ЖИЗНЬ – ТВОЙ LOOT`.
3. **Primary Showcase & Content Grid (<section.main-wrap__sticky> — `Что такое LOOT?`)**:
   - DOM & Selectors: Landmark `<section class="main-wrap__sticky">` rendering section `Что такое LOOT?` with copy *"LOOT связывает реальную активность людей с наградами внутри игр –"*, asset references (`apple-touch-icon.png`, `favicon-32x32.png`, `favicon-16x16.png`, `favicon.ico`), and grid rule `.main-wrap__sticky { z-index:4;grid-template-areas:"section";width:100%;height:100svh;display... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.main-wrap__sticky> — `Что такое LOOT?`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2rem`) on desktop and Single-column vertical stack at `390px` viewport width with `30.8571px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.hero> — `Лутсы – внутренняя валюта LOOT`)**:
   - DOM & Selectors: Landmark `<section class="hero is--section">` framing `Лутсы – внутренняя валюта LOOT` and `Выбирайте награду` (*"реальную активность людей"*) with `#303030` surface cards, `#ec5a00` accents, and `.is--section { opacity:0;pointer-events:none;grid-area:section;height:100svh }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.hero> — `Лутсы – внутренняя валюта LOOT`)` uses `2rem`, `50%`, `4rem`, `2.5rem` radii, `#ec5a00` highlights, and assets (apple-touch-icon.png, favicon-32x32.png, favicon-16x16.png).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://loot-games.ru`)**:
   - DOM & Selectors: Landmark `<footer class="footer is--home">` anchoring `LOOT – награды в играх за активн` footer links (`НАЧНИТЕ · ГЛАВНАЯ · ПАРТНЕРАМ · ПЛАНЫ · КАК ЭТО РАБОТАЕТ`), copy *"ЗАГРУЖАЕМ НОВЫЙ МИР"*, and `#371500` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://loot-games.ru`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `30.8571px` lateral canvas padding with `2rem` grid gap and attributes (data-astro-cid-l7arcky5, data-menu-toggle, data-page-progress).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Спорт, кино, книги, музыка: все, чем вы и так заняты, превращается в настоящие игр..."*
- Copy Excerpt 2: *"LOOT связывает реальную активность людей с наградами внутри игр – и дает бизнесу н..."*
- Copy Excerpt 3: *"реальную активность людей"*
- Copy Excerpt 4: *"ЗАГРУЖАЕМ НОВЫЙ МИР"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.625,0,.875,0)`, `cubic-bezier(.32,.72,0,1)`
- **Extracted Stylesheet Rules (`loot-games-ru`)**:
- `.main-wrap { width:100%;height:auto }`
- `.main-wrap__sticky { z-index:4;grid-template-areas:"section";width:100%;height:100svh;display... }`
- `.is--section { opacity:0;pointer-events:none;grid-area:section;height:100svh }`
- `.is--section.is--active { pointer-events:auto }`
- `titles-trigger { height:300vh }`
- **Per-Selector Transition Rules**:
- **Selector `.button-v2-text[data-astro-cid-en...`**: `transition: opacity .4s ease-out` extracted from `loot-games-ru` stylesheet.
- **Selector `ton-v2-icon__arrow[data-astro-cid...`**: `transition: transform .4s cubic-bezier(.625,.05,0,1)` extracted from `loot-games-ru` stylesheet.
- **Selector `.how .how-meta .how-right__item`**: `transition: background .6s ease-out, scale .4s 50ms var(--smooth-ease)` extracted from `loot-games-ru` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.625,.05,0,1)`)**: Governs interactive state transitions across `<header.navbar>` and `<section.main-wrap__sticky>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `loot-games-ru`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
