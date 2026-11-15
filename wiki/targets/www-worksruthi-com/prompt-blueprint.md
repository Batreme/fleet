---
title: "UI Prompt Blueprint: www-worksruthi-com"
date: 2026-11-15
target: "[[overview|www-worksruthi-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#82181a` / `#e33529`)"
---

# UI Design System & Master Generation Blueprint: www-worksruthi-com

> **meet Sruthi. a copywriter, marketer and artist with chutzpah.** (https://www.worksruthi.com/) — you've built something good and nobody's talking about it yet? i write and design the art that helps capitalists sell their stuff. loudly.

![Desktop Viewport Capture (1440x9736)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **meet Sruthi. a copywriter, marketer and artist with chutzpah.** (`https://www.worksruthi.com/`). you've built something good and nobody's talking about it yet? i write and design the art that helps capitalists sell their stuff. loudly.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#82181a` / `#e33529`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#82181a` (`var(--color-red-900)` in `:root`) paired with `#f3f3e9` primary typography and `#e33529` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Impact` for display copy (`sruthi`) with `Bayon` and `Courier Prime`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--gap-block)`, padding `var(--page-pad-x)`) with `cubic-bezier(.4,0,1,1)` easing and GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×9736px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `www-worksruthi-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--page-pad-x)` lateral canvas padding with `var(--gap-block)` grid gap.
- **Border Radius Scale**: `.25rem`, `50%`, `16px`, `999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--gap-block)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--page-pad-x)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#82181a` | `var(--color-red-900)` in `:root` |
| **Primary Typography Ink** | `#f3f3e9` | `var(--spring)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1c1b1a` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#e33529` | `var(--cinnabar)` in `:root` |
| **Secondary / Muted Copy** | `#f4ced3` | `var(--cherub)` in `:root` |
| **Structural Hairline Border** | `#afd8fb` | `var(--sail)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--vp-100` | `0px` | Dimension / Scale Token |
| `--color-red-900` | `#82181a` | Brand / Palette Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--ease-in` | `cubic-bezier(.4, 0, 1, 1)` | Motion / Easing Token |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` | Motion / Easing Token |
| `--ease-in-out` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--font-display` | `"Impact", "Arial Narrow", sans-serif` | Typography / Scale Token |
| `--font-bayon` | `"Bayon", "Arial Narrow", sans-serif` | Typography / Scale Token |
| `--font-sans` | `"Geist", "Helvetica Neue", Helvetica, Arial, sans-serif` | Typography / Scale Token |
| `--font-mono` | `"Geist Mono", "SF Mono", Menlo, monospace` | Typography / Scale Token |
| `--font-helvetica` | `"Helvetica Neue", Helvetica, Arial, sans-serif` | Typography / Scale Token |
| `--spring` | `#f3f3e9` | Elevation / Border Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Impact`.
- **Primary Body Stack**: `Bayon`.
- **Technical / Metadata Stack**: `Courier Prime`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: "Impact", "Arial Narrow", sans-serif`, `--h1: calc(clamp(72px, calc(28.17px + 11.24vw), 190px) * var(--vp-scale))`.
- **Section Heading (`H2`)**: CSS variables `--h2: calc(clamp(62px, calc(28.57px + 8.57vw), 152px) * var(--vp-scale))`.
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `12px`, `42px`).
- **Metadata & Navigation Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--font-mono: "Geist Mono", "SF Mono", Menlo, monospace`, `--lh-small: 1.14`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-worksruthi-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-worksruthi-com` stylesheet.
- **Selector `.ease-in`**: `transition: var(--ease-in)` extracted from `www-worksruthi-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.pl-lock>` and `<section.bq>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — meet Sruthi. a copywriter, marketer and ar │
│ ====================================================================== │
│ [ <header.pl-lock>         | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: sruthi                                                       |   │
│ | Substrate: #82181a    | Ink: #f3f3e9    | Accent: #e33529        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.bq>              ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | I'M YOUR PERSON TO GET SH*T  |  | work i'm super proud of .    | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.pl-lock>] -> [<section.hero>] -> [<section.bq>] |           │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | https://www.worksruthi.com/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.pl-lock> — `www-worksruthi-com`)**:
   - Landmark `<header class="pl-lock">` hosting `meet Sruthi. a copywriter, marketer ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`), and stylesheet rule `host { --vp-100:0px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `sruthi`)**:
   - Landmark `<section class="hero in">` presenting display lead `sruthi` and copy excerpt *"P L A Y G R O U N D"* over `#82181a` canvas and `#f3f3e9` ink.
3. **Primary Showcase & Content Grid (<section.bq> — `I'M YOUR PERSON TO GET SH*T DONE`)**:
   - Landmark `<section class="bq">` rendering section `I'M YOUR PERSON TO GET SH*T DONE` with copy *"handmade with 🫀 and 🧠 and"*, asset references (`Impact.woff2`, `0_vr5kr4-0c-u.css`, `3y62y2uuds32t.css`, `1mlftcslf095m.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.sfold> — `work i'm super proud of .`)**:
   - Landmark `<section class="sfold">` framing `work i'm super proud of .` and `before you ask . . .` (*"MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE <3<3<3 MY WEBSITE"*) with `#1c1b1a` surface cards, `#e33529` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.worksruthi.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `meet Sruthi. a copywriter, marke` footer links (`Overview · Index · Archive · About · Contact`), copy *"MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE <3<3<3"*, and `#afd8fb` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-worksruthi-com (meet Sruthi. a copywriter, marketer and artist with chutzpah.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-worksruthi-com` (**meet Sruthi. a copywriter, marketer and artist with chutzpah.** — `https://www.worksruthi.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#82181a` / `#e33529`).
- **Identity & Domain Context**: you've built something good and nobody's talking about it yet? i write and design the art that helps capitalists sell their stuff. loudly.
- **Primary Substrate**: `#82181a` (`var(--color-red-900)` in `:root`), **Primary Ink**: `#f3f3e9`, **Accent / Highlight**: `#e33529`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#82181a` (`var(--color-red-900)` in `:root`) paired with `#f3f3e9` primary typography and `#e33529` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Impact` for display copy (`sruthi`) with `Bayon` and `Courier Prime`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--gap-block)`, padding `var(--page-pad-x)`) with `cubic-bezier(.4,0,1,1)` easing and GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-worksruthi-com` in your global stylesheet:

:root {
  /* meet Sruthi. a copywriter, marketer and artist with chutzpah. (www-worksruthi-com) — Ground-Truth Extracted CSS Variables */
  --vp-100: 0px; /* Dimension / Scale Token (www-worksruthi-com) */
  --color-red-900: #82181a; /* Brand / Palette Token (www-worksruthi-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (www-worksruthi-com) */
  --ease-in: cubic-bezier(.4, 0, 1, 1); /* Motion / Easing Token (www-worksruthi-com) */
  --ease-out: cubic-bezier(0, 0, .2, 1); /* Motion / Easing Token (www-worksruthi-com) */
  --ease-in-out: cubic-bezier(.4, 0, .2, 1); /* Motion / Easing Token (www-worksruthi-com) */
  --default-transition-duration: .15s; /* Motion / Easing Token (www-worksruthi-com) */
  --default-transition-timing-function: cubic-bezier(.4, 0, .2, 1); /* Motion / Easing Token (www-worksruthi-com) */
  --default-font-family: var(--font-sans); /* Typography / Scale Token (www-worksruthi-com) */
  --default-mono-font-family: var(--font-mono); /* Typography / Scale Token (www-worksruthi-com) */
  --font-display: "Impact", "Arial Narrow", sans-serif; /* Typography / Scale Token (www-worksruthi-com) */
  --font-bayon: "Bayon", "Arial Narrow", sans-serif; /* Typography / Scale Token (www-worksruthi-com) */
  --font-sans: "Geist", "Helvetica Neue", Helvetica, Arial, sans-serif; /* Typography / Scale Token (www-worksruthi-com) */
  --font-mono: "Geist Mono", "SF Mono", Menlo, monospace; /* Typography / Scale Token (www-worksruthi-com) */
  --font-helvetica: "Helvetica Neue", Helvetica, Arial, sans-serif; /* Typography / Scale Token (www-worksruthi-com) */
  --spring: #f3f3e9; /* Elevation / Border Token (www-worksruthi-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#82181a` — grounded in `var(--color-red-900)` in `:root`
- **Primary Typography Ink**: `#f3f3e9` — grounded in `var(--spring)` in `:root`
- **Elevated Surface / Card Substrate**: `#1c1b1a` — grounded in `var(--ink)` in `:root`
- **Interactive Accent / Highlight**: `#e33529` — grounded in `var(--cinnabar)` in `:root`
- **Secondary / Muted Copy**: `#f4ced3` — grounded in `var(--cherub)` in `:root`
- **Structural Hairline Border**: `#afd8fb` — grounded in `var(--sail)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×9736px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `www-worksruthi-com` stylesheet
- **Padding & Gutters**: `var(--page-pad-x)` lateral canvas padding with `var(--gap-block)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--gap-block)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--page-pad-x)` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.25rem`, `50%`, `16px`, `999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Impact`
- **Body Font Stack**: `Bayon`
- **Monospace / Technical Font Stack**: `Courier Prime`
- **H1 Display Rule**: CSS variables `--font-display: "Impact", "Arial Narrow", sans-serif`, `--h1: calc(clamp(72px, calc(28.17px + 11.24vw), 190px) * var(--vp-scale))`
- **H2 Section Rule**: CSS variables `--h2: calc(clamp(62px, calc(28.57px + 8.57vw), 152px) * var(--vp-scale))`
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `12px`, `42px`)
- **Metadata & Index Rule**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--font-mono: "Geist Mono", "SF Mono", Menlo, monospace`, `--lh-small: 1.14`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-worksruthi-com` (`meet Sruthi. a copywriter, marketer and artist with chutzpah.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.pl-lock> — `www-worksruthi-com`)**:
   - DOM & Selectors: Landmark `<header class="pl-lock">` hosting `meet Sruthi. a copywriter, marketer ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`), and stylesheet rule `host { --vp-100:0px }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.pl-lock> — `www-worksruthi-com`)` (`www-worksruthi-com`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.hero> — `sruthi`)**:
   - DOM & Selectors: Landmark `<section class="hero in">` presenting display lead `sruthi` and copy excerpt *"P L A Y G R O U N D"* over `#82181a` canvas and `#f3f3e9` ink.
   - Responsive Contract: Hero stage (`1440×9736px` desktop / `390×2400px` mobile) sets `#82181a` background with `#f3f3e9` headline `sruthi`.
3. **Primary Showcase & Content Grid (<section.bq> — `I'M YOUR PERSON TO GET SH*T DONE`)**:
   - DOM & Selectors: Landmark `<section class="bq">` rendering section `I'M YOUR PERSON TO GET SH*T DONE` with copy *"handmade with 🫀 and 🧠 and"*, asset references (`Impact.woff2`, `0_vr5kr4-0c-u.css`, `3y62y2uuds32t.css`, `1mlftcslf095m.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.bq> — `I'M YOUR PERSON TO GET SH*T DONE`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--gap-block)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--page-pad-x)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.sfold> — `work i'm super proud of .`)**:
   - DOM & Selectors: Landmark `<section class="sfold">` framing `work i'm super proud of .` and `before you ask . . .` (*"MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE <3<3<3 MY WEBSITE"*) with `#1c1b1a` surface cards, `#e33529` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.sfold> — `work i'm super proud of .`)` uses `.25rem`, `50%`, `16px`, `999px` radii, `#e33529` highlights, and assets (Impact.woff2, 0_vr5kr4-0c-u.css, 3y62y2uuds32t.css).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.worksruthi.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `meet Sruthi. a copywriter, marke` footer links (`Overview · Index · Archive · About · Contact`), copy *"MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE <3<3<3"*, and `#afd8fb` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://www.worksruthi.com/`)` aligns to `40rem` extracted from `www-worksruthi-com` stylesheet with `var(--page-pad-x)` lateral canvas padding with `var(--gap-block)` grid gap and attributes (data-precedence="next", data-precedence="next", data-sdkn="@vercel/analytics/next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"P L A Y G R O U N D"*
- Copy Excerpt 2: *"handmade with 🫀 and 🧠 and"*
- Copy Excerpt 3: *"MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE <3<3<3 MY WEBSITE IS NOW ON AWWWAR..."*
- Copy Excerpt 4: *"MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE <3<3<3"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-worksruthi-com`)**:
- `host { --vp-100:0px }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-worksruthi-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-worksruthi-com` stylesheet.
- **Selector `.ease-in`**: `transition: var(--ease-in)` extracted from `www-worksruthi-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.pl-lock>` and `<section.bq>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-worksruthi-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
