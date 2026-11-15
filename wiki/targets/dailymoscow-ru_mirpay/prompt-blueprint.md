---
title: "UI Prompt Blueprint: dailymoscow-ru_mirpay"
date: 2026-11-15
target: "[[overview|dailymoscow-ru_mirpay]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#7b7b81` accent)"
---

# UI Design System & Master Generation Blueprint: dailymoscow-ru_mirpay

> **Спорт без лишних действий — Mir Pay × Daily Moscow** (https://dailymoscow.ru/mirpay) — Бокс, гольф, бассейн, падел, скалодром и йога — и ни одного лишнего движения, когда дело доходит до оплаты

![Desktop Viewport Capture (1440x13262)](file:///root/projects/fleet/wiki/targets/dailymoscow-ru_mirpay/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Спорт без лишних действий — Mir Pay × Daily Moscow** (`https://dailymoscow.ru/mirpay`). Бокс, гольф, бассейн, падел, скалодром и йога — и ни одного лишнего движения, когда дело доходит до оплаты
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#7b7b81` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--dmf-bg)` in `:root`) paired with `#fff` primary typography and `#7b7b81` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Manrope` for display copy (`Спорт без лишних действий`) with `Lora` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: 10px`, padding `5px`) with `cubic-bezier(.16,1,.3,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/dailymoscow-ru_mirpay/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×13262px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `640px` extracted from `dailymoscow-ru_mirpay` stylesheet.
- **Canvas Lateral Padding & Spacing**: `5px` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `6px`, `.5px`, `.5rem`, `3px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `5px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 769px)`, `@media only screen and (max-width:1200px)`, `@media only screen and (max-width:940px)`, `@media only screen and (max-width:450px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--dmf-bg)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--dmf-ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#9d9da4` | `var(--dmf-muted)` in `:root` |
| **Interactive Accent / Highlight** | `#7b7b81` | `var(--dmf-dim)` in `:root` |
| **Secondary / Muted Copy** | `#1f5bd7` | `var(--blue)` in `:root` |
| **Structural Hairline Border** | `#00aaff` | `var(--sky)` in `:root` |
| **Variable Token (`--green`)** | `#00a263` | `var(--green)` in `:root` |
| **Variable Token (`--green-t`)** | `#008452` | `var(--green-t)` in `:root` |
| **Variable Token (`--green-d`)** | `#0b4d31` | `var(--green-d)` in `:root` |
| **Variable Token (`--ink`)** | `#0f1530` | `var(--ink)` in `:root` |
| **Variable Token (`--text`)** | `#2a3150` | `var(--text)` in `:root` |
| **Variable Token (`--mute`)** | `#5d6683` | `var(--mute)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dmf-bg` | `#000` | Canvas / Surface Token |
| `--dmf-ink` | `#fff` | Typography Ink Token |
| `--dmf-muted` | `#9d9da4` | Color / Atmospheric Token |
| `--dmf-dim` | `#7b7b81` | Color / Atmospheric Token |
| `--dmf-rule` | `rgba(255, 255, 255, .14)` | Color / Atmospheric Token |
| `--dmf-surface` | `rgba(255, 255, 255, .05)` | Canvas / Surface Token |
| `--dmf-gap` | `32px` | Layout / Spatial Grid Token |
| `--dmf-rail` | `340px` | Dimension / Scale Token |
| `--blue` | `#1f5bd7` | Color / Atmospheric Token |
| `--sky` | `#00aaff` | Color / Atmospheric Token |
| `--green` | `#00a263` | Color / Atmospheric Token |
| `--green-t` | `#008452` | Color / Atmospheric Token |
| `--green-d` | `#0b4d31` | Color / Atmospheric Token |
| `--ink` | `#0f1530` | Typography Ink Token |
| `--text` | `#2a3150` | Typography Ink Token |
| `--mute` | `#5d6683` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Manrope`.
- **Primary Body Stack**: `Lora`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `6px`, `14px`, `10px`, `12px`).
- **Section Heading (`H2`)**: rule `.section-title` (`font-weight: 800`).
- **Body Copy**: rule `p` (`font-size: 14px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `6px`, `14px`, `10px`, `12px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(.2,.7,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.modal`**: `transition: .2s` extracted from `dailymoscow-ru_mirpay` stylesheet.
- **Selector `.main-tabs li a::after`**: `transition: .2s` extracted from `dailymoscow-ru_mirpay` stylesheet.
- **Selector `.main-slider .slick-arrow svg path`**: `transition: .2s` extracted from `dailymoscow-ru_mirpay` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.header>` and `<article.m3-body>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.main>` and `<article.m3-body>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Спорт без лишних действий — Mir Pay × Dail │
│ ====================================================================== │
│ [ <header.header>          | Бокс · Гольф · Бассейн · Падел · Скало ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.main>                                       |   │
│ | H1: Спорт без лишних действий                                    |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #7b7b81        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.m3-body>         ) max-w: 640px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Начинала я с бокса           |  | Потом был гольф              | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px  ) | │
│ | [<header.header>] -> [<section.main>] -> [<article.m3-body>] |       │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://dailymoscow.ru/mirpay      │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `dailymoscow-ru_mirpay`)**:
   - Landmark `<header class="header header-news">` hosting `Спорт без лишних действий — Mir Pay ` navigation (`Бокс · Гольф · Бассейн · Падел · Скалодром`), DOM attributes (`data-pd="26"`, `data-mx="-.4"`, `data-sp=".5"`, `data-pd="-40"`), and stylesheet rule `body.body-dark .category-main { border-color:1f1f1f }`.
2. **Hero Stage & Focal Lead (<section.main> — `Спорт без лишних действий`)**:
   - Landmark `<section class="main m3">` presenting display lead `Спорт без лишних действий` and copy excerpt *"Бокс, гольф, бассейн, падел, скалодром и йога — и ни одного лишне"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<article.m3-body> — `Начинала я с бокса`)**:
   - Landmark `<article class="m3-body">` rendering section `Начинала я с бокса` with copy *"ЕК Елена Карнеева редактор Daily Moscow"*, asset references (`tag.js`, `mirpay`, `footer-v2.css`, `components.css`), and grid rule `body.body-dark .category-main__name { color:fff }`.
4. **Interactive Detail & Feature Matrix (<section.m3-sec> — `Потом был гольф`)**:
   - Landmark `<section class="m3-sec">` framing `Потом был гольф` and `Дальше была вода, то есть аквакомплекс` (*"Елена Карнеева редактор Daily Moscow"*) with `#9d9da4` surface cards, `#7b7b81` accents, and `body.body-dark .category-quote__s... { color:7b7b81 }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://dailymoscow.ru/mirpay`)**:
   - Landmark `<footer class="footer dm-footer">` anchoring `Спорт без лишних действий — Mir ` footer links (`Бокс · Гольф · Бассейн · Падел · Скалодром`), copy *"редактор Daily Moscow"*, and `#00aaff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: dailymoscow-ru_mirpay (Спорт без лишних действий — Mir Pay × Daily Moscow)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `dailymoscow-ru_mirpay` (**Спорт без лишних действий — Mir Pay × Daily Moscow** — `https://dailymoscow.ru/mirpay`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#7b7b81` accent).
- **Identity & Domain Context**: Бокс, гольф, бассейн, падел, скалодром и йога — и ни одного лишнего движения, когда дело доходит до оплаты
- **Primary Substrate**: `#000` (`var(--dmf-bg)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#7b7b81`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--dmf-bg)` in `:root`) paired with `#fff` primary typography and `#7b7b81` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Manrope` for display copy (`Спорт без лишних действий`) with `Lora` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: 10px`, padding `5px`) with `cubic-bezier(.16,1,.3,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `dailymoscow-ru_mirpay` in your global stylesheet:

:root {
  /* Спорт без лишних действий — Mir Pay × Daily Moscow (dailymoscow-ru_mirpay) — Ground-Truth Extracted CSS Variables */
  --dmf-bg: #000; /* Canvas / Surface Token (dailymoscow-ru_mirpay) */
  --dmf-ink: #fff; /* Typography Ink Token (dailymoscow-ru_mirpay) */
  --dmf-muted: #9d9da4; /* Color / Atmospheric Token (dailymoscow-ru_mirpay) */
  --dmf-dim: #7b7b81; /* Color / Atmospheric Token (dailymoscow-ru_mirpay) */
  --dmf-rule: rgba(255, 255, 255, .14); /* Color / Atmospheric Token (dailymoscow-ru_mirpay) */
  --dmf-surface: rgba(255, 255, 255, .05); /* Canvas / Surface Token (dailymoscow-ru_mirpay) */
  --dmf-gap: 32px; /* Layout / Spatial Grid Token (dailymoscow-ru_mirpay) */
  --dmf-rail: 340px; /* Dimension / Scale Token (dailymoscow-ru_mirpay) */
  --blue: #1f5bd7; /* Color / Atmospheric Token (dailymoscow-ru_mirpay) */
  --sky: #00aaff; /* Color / Atmospheric Token (dailymoscow-ru_mirpay) */
  --green: #00a263; /* Color / Atmospheric Token (dailymoscow-ru_mirpay) */
  --green-t: #008452; /* Color / Atmospheric Token (dailymoscow-ru_mirpay) */
  --green-d: #0b4d31; /* Color / Atmospheric Token (dailymoscow-ru_mirpay) */
  --ink: #0f1530; /* Typography Ink Token (dailymoscow-ru_mirpay) */
  --text: #2a3150; /* Typography Ink Token (dailymoscow-ru_mirpay) */
  --mute: #5d6683; /* Color / Atmospheric Token (dailymoscow-ru_mirpay) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--dmf-bg)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--dmf-ink)` in `:root`
- **Elevated Surface / Card Substrate**: `#9d9da4` — grounded in `var(--dmf-muted)` in `:root`
- **Interactive Accent / Highlight**: `#7b7b81` — grounded in `var(--dmf-dim)` in `:root`
- **Secondary / Muted Copy**: `#1f5bd7` — grounded in `var(--blue)` in `:root`
- **Structural Hairline Border**: `#00aaff` — grounded in `var(--sky)` in `:root`
- **Variable Token (`--green`)**: `#00a263` — grounded in `var(--green)` in `:root`
- **Variable Token (`--green-t`)**: `#008452` — grounded in `var(--green-t)` in `:root`
- **Variable Token (`--green-d`)**: `#0b4d31` — grounded in `var(--green-d)` in `:root`
- **Variable Token (`--ink`)**: `#0f1530` — grounded in `var(--ink)` in `:root`
- **Variable Token (`--text`)**: `#2a3150` — grounded in `var(--text)` in `:root`
- **Variable Token (`--mute`)**: `#5d6683` — grounded in `var(--mute)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×13262px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `640px` extracted from `dailymoscow-ru_mirpay` stylesheet
- **Padding & Gutters**: `5px` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `5px` horizontal padding
- **Media Queries**: `@media (min-width: 769px)`, `@media only screen and (max-width:1200px)`, `@media only screen and (max-width:940px)`, `@media only screen and (max-width:450px)`
- **Corner Radii**: `6px`, `.5px`, `.5rem`, `3px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Manrope`
- **Body Font Stack**: `Lora`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `6px`, `14px`, `10px`, `12px`)
- **H2 Section Rule**: rule `.section-title` (`font-weight: 800`)
- **Body Copy Rule**: rule `p` (`font-size: 14px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `6px`, `14px`, `10px`, `12px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `dailymoscow-ru_mirpay` (`Спорт без лишних действий — Mir Pay × Daily Moscow`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `dailymoscow-ru_mirpay`)**:
   - DOM & Selectors: Landmark `<header class="header header-news">` hosting `Спорт без лишних действий — Mir Pay ` navigation (`Бокс · Гольф · Бассейн · Падел · Скалодром`), DOM attributes (`data-pd="26"`, `data-mx="-.4"`, `data-sp=".5"`, `data-pd="-40"`), and stylesheet rule `body.body-dark .category-main { border-color:1f1f1f }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `dailymoscow-ru_mirpay`)` (`dailymoscow-ru_mirpay`) adapts across `@media (min-width: 769px)`, `@media only screen and (max-width:1200px)`, `@media only screen and (max-width:940px)`, `@media only screen and (max-width:450px)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(.2,.7,.2,1)` transitions and links `Бокс · Гольф · Бассейн · Падел · Скалодром`.
2. **Hero Stage & Focal Lead (<section.main> — `Спорт без лишних действий`)**:
   - DOM & Selectors: Landmark `<section class="main m3">` presenting display lead `Спорт без лишних действий` and copy excerpt *"Бокс, гольф, бассейн, падел, скалодром и йога — и ни одного лишне"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×13262px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Спорт без лишних действий`.
3. **Primary Showcase & Content Grid (<article.m3-body> — `Начинала я с бокса`)**:
   - DOM & Selectors: Landmark `<article class="m3-body">` rendering section `Начинала я с бокса` with copy *"ЕК Елена Карнеева редактор Daily Moscow"*, asset references (`tag.js`, `mirpay`, `footer-v2.css`, `components.css`), and grid rule `body.body-dark .category-main__name { color:fff }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.m3-body> — `Начинала я с бокса`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `5px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.m3-sec> — `Потом был гольф`)**:
   - DOM & Selectors: Landmark `<section class="m3-sec">` framing `Потом был гольф` and `Дальше была вода, то есть аквакомплекс` (*"Елена Карнеева редактор Daily Moscow"*) with `#9d9da4` surface cards, `#7b7b81` accents, and `body.body-dark .category-quote__s... { color:7b7b81 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.m3-sec> — `Потом был гольф`)` uses `6px`, `.5px`, `.5rem`, `3px` radii, `#7b7b81` highlights, and assets (tag.js, mirpay, footer-v2.css).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://dailymoscow.ru/mirpay`)**:
   - DOM & Selectors: Landmark `<footer class="footer dm-footer">` anchoring `Спорт без лишних действий — Mir ` footer links (`Бокс · Гольф · Бассейн · Падел · Скалодром`), copy *"редактор Daily Moscow"*, and `#00aaff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://dailymoscow.ru/mirpay`)` aligns to `640px` extracted from `dailymoscow-ru_mirpay` stylesheet with `5px` lateral canvas padding with `10px` grid gap and attributes (data-pd="26", data-mx="-.4", data-sp=".5").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Бокс, гольф, бассейн, падел, скалодром и йога — и ни одного лишнего движения, когд..."*
- Copy Excerpt 2: *"ЕК Елена Карнеева редактор Daily Moscow"*
- Copy Excerpt 3: *"Елена Карнеева редактор Daily Moscow"*
- Copy Excerpt 4: *"редактор Daily Moscow"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(.2,.7,.2,1)`
- **Extracted Stylesheet Rules (`dailymoscow-ru_mirpay`)**:
- `body.body-dark .category-main { border-color:1f1f1f }`
- `body.body-dark .category-main__name { color:fff }`
- `body.body-dark .category-quote__s... { color:7b7b81 }`
- `ody.body-dark .category-quote__st... { color:7b7b81 }`
- `strong { font-weight:bolder }`
- **Per-Selector Transition Rules**:
- **Selector `.modal`**: `transition: .2s` extracted from `dailymoscow-ru_mirpay` stylesheet.
- **Selector `.main-tabs li a::after`**: `transition: .2s` extracted from `dailymoscow-ru_mirpay` stylesheet.
- **Selector `.main-slider .slick-arrow svg path`**: `transition: .2s` extracted from `dailymoscow-ru_mirpay` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.header>` and `<article.m3-body>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.main>` and `<article.m3-body>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `dailymoscow-ru_mirpay`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
