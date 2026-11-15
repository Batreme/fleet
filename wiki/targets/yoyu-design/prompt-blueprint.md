---
title: "UI Prompt Blueprint: yoyu-design"
date: 2026-11-15
target: "[[overview|yoyu-design]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#EDEFF4`)"
---

# UI Design System & Master Generation Blueprint: yoyu-design

> **ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サービス** (https://yoyu.design/) — 園の業務としくみを整え、まず余裕をつくる。その余裕を、園が大切にする保育の実現へつなげる技術支援サービスです。

![Desktop Viewport Capture (1440x27863)](file:///root/projects/fleet/wiki/targets/yoyu-design/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サービス** (`https://yoyu.design/`). 園の業務としくみを整え、まず余裕をつくる。その余裕を、園が大切にする保育の実現へつなげる技術支援サービスです。
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#EDEFF4`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000000` (`var(--tag-background)` in `:root`) paired with `#FFFFFF` primary typography and `#EDEFF4` accents.
  - **Extracted Typographic Hierarchy**: Pairs `DotGothic16` for display copy (`私たちのご提案`) with `IBM Plex Sans JP` and `IBM Plex Sans JP`.
  - **Calibrated Spatial Grid & Motion**: Combines `920px` container bounds (`gap: 6px`, padding `6px`) with `cubic-bezier(.22,1,.36,1)` easing and Swiper Touch Carousel Engine, HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/yoyu-design/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×27863px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `920px` extracted from `yoyu-design` stylesheet.
- **Canvas Lateral Padding & Spacing**: `6px` lateral canvas padding with `6px` grid gap.
- **Border Radius Scale**: `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 920px`, `gap: 6px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (min-width:781px)and (max-width:920px)`, `@media screen and (min-width:781px)and (max-width:1439px)`, `@media screen and (max-width:780px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | `var(--tag-background)` in `:root` |
| **Primary Typography Ink** | `#858890` | `var(--color-gray-dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#E2E4EA` | `var(--color-gray-heavy)` in `:root` |
| **Interactive Accent / Highlight** | `#EDEFF4` | `var(--color-gray-middle)` in `:root` |
| **Secondary / Muted Copy** | `#F6F8FB` | `var(--color-gray-light)` in `:root` |
| **Structural Hairline Border** | `#FFFFFF` | `var(--color-white)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--menu-bar-delay` | `0ms` | Motion / Easing Token |
| `--idle-big-kid-base-size` | `540px` | Layout / Spatial Grid Token |
| `--idle-big-kid-rest-half` | `270px` | Dimension / Scale Token |
| `--idle-big-kid-center-offset` | `-68px` | Dimension / Scale Token |
| `--idle-big-kid-floor-offset` | `128px` | Dimension / Scale Token |
| `--idle-big-kid-actions-margin` | `64px` | Layout / Spatial Grid Token |
| `--idle-big-kid-actions-height` | `84px` | Layout / Spatial Grid Token |
| `--idle-big-kid-actions-bottom-limit` | `63px` | Dimension / Scale Token |
| `--idle-big-kid-glyph-origin-x` | `50%` | Dimension / Scale Token |
| `--idle-big-kid-glyph-origin-y` | `55.5556%` | Dimension / Scale Token |
| `--idle-big-kid-reveal-delay` | `.48s` | Motion / Easing Token |
| `--idle-big-kid-reveal-stagger` | `.16s` | Motion / Timing Token |
| `--idle-big-kid-reveal-duration` | `.32s` | Motion / Easing Token |
| `--idle-big-kid-fade-duration` | `.48s` | Motion / Easing Token |
| `--idle-big-kid-heart-x` | `0px` | Dimension / Scale Token |
| `--idle-big-kid-heart-y` | `0px` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `DotGothic16`.
- **Primary Body Stack**: `IBM Plex Sans JP`.
- **Technical / Metadata Stack**: `IBM Plex Sans JP`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `8px`, `11px`, `14px`, `4.6153846154vw`, `20px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `8px`, `11px`, `14px`, `4.6153846154vw`, `20px`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `8px`, `11px`, `14px`, `4.6153846154vw`, `20px`).
- **Metadata & Navigation Labels**: CSS variables `--pixel-small: 4px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(0.4,0,0.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.site-header__menu-icon i[data-v-...`**: `transition: top .2s cubic-bezier(.22,1,.36,1),right .2s cubic-bezier(.22,1...` extracted from `yoyu-design` stylesheet.
- **Selector `header__menu-icon i[data-v-8ab53e...`**: `transition: transform 104ms cubic-bezier(.22,1,.36,1)` extracted from `yoyu-design` stylesheet.
- **Selector `e-header-menu-enter-active[data-v...`**: `transition: opacity .16s ease-out` extracted from `yoyu-design` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.quick-test>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サービス         │
│ ====================================================================== │
│ [ <header.site-header>     | QUICK TEST · 私たちからの提案 · サポート領域 · 事例紹介  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.first-view>                                 |   │
│ | H1: 私たちのご提案                                                      |   │
│ | Substrate: #000000    | Ink: #FFFFFF    | Accent: #EDEFF4        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.quick-test>      ) max-w: 920px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | サービスの大まかな流れ                  |  | 定例ミーティング                     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 6px   ) | │
│ | [<header.site-heade] -> [<section.first-vie] -> [<section.quick-tes] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | https://yoyu.design/               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `yoyu-design`)**:
   - Landmark `<header class="site-header is-visible">` hosting `ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サービス` navigation (`QUICK TEST · 私たちからの提案 · サポート領域 · 事例紹介 · FAQ`), DOM attributes (`data-question-invasion-reveal-active="false"`, `data-question-invasion-reveal-start-scroll-y="2885"`, `data-question-invasion-covered="false"`, `data-question-content-visible="false"`), and stylesheet rule `.main-content { min-height:100svh }`.
2. **Hero Stage & Focal Lead (<section.first-view> — `私たちのご提案`)**:
   - Landmark `<section class="first-view">` presenting display lead `私たちのご提案` and copy excerpt *"園の余裕創出から理念実現まで、園づくりを支える技術支援サービス"* over `#000000` canvas and `#FFFFFF` ink.
3. **Primary Showcase & Content Grid (<section.quick-test> — `サービスの大まかな流れ`)**:
   - Landmark `<section class="quick-test is-idle">` rendering section `サービスの大まかな流れ` with copy *"システムを導入したのになぜか時間に追われていませんか？"*, asset references (`gtm.js`, `favicon-32.png`, `favicon.svg`, `apple-touch-icon.png`), and grid rule `.idle-big-kid-overlay { translate:var(--idle-big-kid-shake-x, 0) var(--idle-big-kid-shake-y, 0) }`.
4. **Interactive Detail & Feature Matrix (<article.quick-test__panel> — `定例ミーティング`)**:
   - Landmark `<article class="quick-test__panel is-current">` framing `定例ミーティング` and `課題の整理` (*"保育に集中できない 保育に集中できない 保育に集中できない"*) with `#E2E4EA` surface cards, `#EDEFF4` accents, and `hover { box-shadow:inset 0 -2px 000 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://yoyu.design/`)**:
   - Landmark `<footer class="site-footer">` anchoring `ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サー` footer links (`QUICK TEST · 私たちからの提案 · サポート領域 · 事例紹介 · FAQ`), copy *"園児情報を書き写すまいにち 園児情報を書き写すまいにち 園児情報を書き写すまいにち"*, and `#FFFFFF` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: yoyu-design (ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サービス)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `yoyu-design` (**ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サービス** — `https://yoyu.design/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#EDEFF4`).
- **Identity & Domain Context**: 園の業務としくみを整え、まず余裕をつくる。その余裕を、園が大切にする保育の実現へつなげる技術支援サービスです。
- **Primary Substrate**: `#000000` (`var(--tag-background)` in `:root`), **Primary Ink**: `#FFFFFF`, **Accent / Highlight**: `#EDEFF4`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000000` (`var(--tag-background)` in `:root`) paired with `#FFFFFF` primary typography and `#EDEFF4` accents.
  - **Extracted Typographic Hierarchy**: Pairs `DotGothic16` for display copy (`私たちのご提案`) with `IBM Plex Sans JP` and `IBM Plex Sans JP`.
  - **Calibrated Spatial Grid & Motion**: Combines `920px` container bounds (`gap: 6px`, padding `6px`) with `cubic-bezier(.22,1,.36,1)` easing and Swiper Touch Carousel Engine, HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `yoyu-design` in your global stylesheet:

:root {
  /* ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サービス (yoyu-design) — Ground-Truth Extracted CSS Variables */
  --menu-bar-delay: 0ms; /* Motion / Easing Token (yoyu-design) */
  --idle-big-kid-base-size: 540px; /* Layout / Spatial Grid Token (yoyu-design) */
  --idle-big-kid-rest-half: 270px; /* Dimension / Scale Token (yoyu-design) */
  --idle-big-kid-center-offset: -68px; /* Dimension / Scale Token (yoyu-design) */
  --idle-big-kid-floor-offset: 128px; /* Dimension / Scale Token (yoyu-design) */
  --idle-big-kid-actions-margin: 64px; /* Layout / Spatial Grid Token (yoyu-design) */
  --idle-big-kid-actions-height: 84px; /* Layout / Spatial Grid Token (yoyu-design) */
  --idle-big-kid-actions-bottom-limit: 63px; /* Dimension / Scale Token (yoyu-design) */
  --idle-big-kid-glyph-origin-x: 50%; /* Dimension / Scale Token (yoyu-design) */
  --idle-big-kid-glyph-origin-y: 55.5556%; /* Dimension / Scale Token (yoyu-design) */
  --idle-big-kid-reveal-delay: .48s; /* Motion / Easing Token (yoyu-design) */
  --idle-big-kid-reveal-stagger: .16s; /* Motion / Timing Token (yoyu-design) */
  --idle-big-kid-reveal-duration: .32s; /* Motion / Easing Token (yoyu-design) */
  --idle-big-kid-fade-duration: .48s; /* Motion / Easing Token (yoyu-design) */
  --idle-big-kid-heart-x: 0px; /* Dimension / Scale Token (yoyu-design) */
  --idle-big-kid-heart-y: 0px; /* Dimension / Scale Token (yoyu-design) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in `var(--tag-background)` in `:root`
- **Primary Typography Ink**: `#858890` — grounded in `var(--color-gray-dark)` in `:root`
- **Elevated Surface / Card Substrate**: `#E2E4EA` — grounded in `var(--color-gray-heavy)` in `:root`
- **Interactive Accent / Highlight**: `#EDEFF4` — grounded in `var(--color-gray-middle)` in `:root`
- **Secondary / Muted Copy**: `#F6F8FB` — grounded in `var(--color-gray-light)` in `:root`
- **Structural Hairline Border**: `#FFFFFF` — grounded in `var(--color-white)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×27863px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `920px` extracted from `yoyu-design` stylesheet
- **Padding & Gutters**: `6px` lateral canvas padding with `6px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 920px`, `gap: 6px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding
- **Media Queries**: `@media screen and (min-width:781px)and (max-width:920px)`, `@media screen and (min-width:781px)and (max-width:1439px)`, `@media screen and (max-width:780px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `DotGothic16`
- **Body Font Stack**: `IBM Plex Sans JP`
- **Monospace / Technical Font Stack**: `IBM Plex Sans JP`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `8px`, `11px`, `14px`, `4.6153846154vw`, `20px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `8px`, `11px`, `14px`, `4.6153846154vw`, `20px`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `8px`, `11px`, `14px`, `4.6153846154vw`, `20px`)
- **Metadata & Index Rule**: CSS variables `--pixel-small: 4px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `yoyu-design` (`ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サービス`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `yoyu-design`)**:
   - DOM & Selectors: Landmark `<header class="site-header is-visible">` hosting `ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サービス` navigation (`QUICK TEST · 私たちからの提案 · サポート領域 · 事例紹介 · FAQ`), DOM attributes (`data-question-invasion-reveal-active="false"`, `data-question-invasion-reveal-start-scroll-y="2885"`, `data-question-invasion-covered="false"`, `data-question-content-visible="false"`), and stylesheet rule `.main-content { min-height:100svh }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `yoyu-design`)` (`yoyu-design`) adapts across `@media screen and (min-width:781px)and (max-width:920px)`, `@media screen and (min-width:781px)and (max-width:1439px)`, `@media screen and (max-width:780px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(0.4,0,0.2,1)` transitions and links `QUICK TEST · 私たちからの提案 · サポート領域 · 事例紹介 · FAQ`.
2. **Hero Stage & Focal Lead (<section.first-view> — `私たちのご提案`)**:
   - DOM & Selectors: Landmark `<section class="first-view">` presenting display lead `私たちのご提案` and copy excerpt *"園の余裕創出から理念実現まで、園づくりを支える技術支援サービス"* over `#000000` canvas and `#FFFFFF` ink.
   - Responsive Contract: Hero stage (`1440×27863px` desktop / `390×2400px` mobile) sets `#000000` background with `#FFFFFF` headline `私たちのご提案`.
3. **Primary Showcase & Content Grid (<section.quick-test> — `サービスの大まかな流れ`)**:
   - DOM & Selectors: Landmark `<section class="quick-test is-idle">` rendering section `サービスの大まかな流れ` with copy *"システムを導入したのになぜか時間に追われていませんか？"*, asset references (`gtm.js`, `favicon-32.png`, `favicon.svg`, `apple-touch-icon.png`), and grid rule `.idle-big-kid-overlay { translate:var(--idle-big-kid-shake-x, 0) var(--idle-big-kid-shake-y, 0) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.quick-test> — `サービスの大まかな流れ`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 920px`, `gap: 6px`) on desktop and Single-column vertical stack at `390px` viewport width with `6px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.quick-test__panel> — `定例ミーティング`)**:
   - DOM & Selectors: Landmark `<article class="quick-test__panel is-current">` framing `定例ミーティング` and `課題の整理` (*"保育に集中できない 保育に集中できない 保育に集中できない"*) with `#E2E4EA` surface cards, `#EDEFF4` accents, and `hover { box-shadow:inset 0 -2px 000 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.quick-test__panel> — `定例ミーティング`)` uses `50%` radii, `#EDEFF4` highlights, and assets (gtm.js, favicon-32.png, favicon.svg).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://yoyu.design/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サー` footer links (`QUICK TEST · 私たちからの提案 · サポート領域 · 事例紹介 · FAQ`), copy *"園児情報を書き写すまいにち 園児情報を書き写すまいにち 園児情報を書き写すまいにち"*, and `#FFFFFF` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://yoyu.design/`)` aligns to `920px` extracted from `yoyu-design` stylesheet with `6px` lateral canvas padding with `6px` grid gap and attributes (data-question-invasion-reveal-active="false", data-question-invasion-reveal-start-scroll-y="2885", data-question-invasion-covered="false").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"園の余裕創出から理念実現まで、園づくりを支える技術支援サービス"*
- Copy Excerpt 2: *"システムを導入したのになぜか時間に追われていませんか？"*
- Copy Excerpt 3: *"保育に集中できない 保育に集中できない 保育に集中できない"*
- Copy Excerpt 4: *"園児情報を書き写すまいにち 園児情報を書き写すまいにち 園児情報を書き写すまいにち"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(0.4,0,0.2,1)`
- **Extracted Stylesheet Rules (`yoyu-design`)**:
- `.main-content { min-height:100svh }`
- `.idle-big-kid-overlay { translate:var(--idle-big-kid-shake-x, 0) var(--idle-big-kid-shake-y, 0) }`
- `hover { box-shadow:inset 0 -2px 000 }`
- `before { transform:scaleX(1) }`
- `html.is-yoyu-menu-open body { overflow:hidden }`
- **Per-Selector Transition Rules**:
- **Selector `.site-header__menu-icon i[data-v-...`**: `transition: top .2s cubic-bezier(.22,1,.36,1),right .2s cubic-bezier(.22,1...` extracted from `yoyu-design` stylesheet.
- **Selector `header__menu-icon i[data-v-8ab53e...`**: `transition: transform 104ms cubic-bezier(.22,1,.36,1)` extracted from `yoyu-design` stylesheet.
- **Selector `e-header-menu-enter-active[data-v...`**: `transition: opacity .16s ease-out` extracted from `yoyu-design` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.quick-test>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `yoyu-design`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
