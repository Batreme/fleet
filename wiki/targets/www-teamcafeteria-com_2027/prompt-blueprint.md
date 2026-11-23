---
title: "UI Prompt Blueprint: www-teamcafeteria-com_2027"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-teamcafeteria-com_2027"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#35ff92`)"
---

# UI Design System & Master Generation Blueprint: www-teamcafeteria-com_2027

> **2027 — a [cafeteria] report** (https://www.teamcafeteria.com/2027) — 1,423 people told us what 2027 looks like. A scroll-driven [cafeteria] report.

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **2027 — a [cafeteria] report** (`https://www.teamcafeteria.com/2027`). 1,423 people told us what 2027 looks like. A scroll-driven [cafeteria] report.
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#35ff92`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#fcfcfc` primary typography and `#35ff92` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Satoshi 2027` for display copy (`2027 — a [cafeteria] report`) with `Satoshi 2027` and `Rubik Mono One`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 24px`, padding `4px`) with `cubic-bezier(.65,0,.35,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `4px` lateral canvas padding with `24px` grid gap.
- **Border Radius Scale**: `22%`, `40px`, `50%`, `99px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 24px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:761px)`, `@media (max-width:760px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1100px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fcfcfc` | live computed `footer` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1d1b1b` | live computed `nav` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#35ff92` | `var(--accent)` in `:root` |
| **Secondary / Muted Copy** | `#686b6b` | `var(--c-text-mute)` in `:root` |
| **Structural Hairline Border** | `#232020` | `var(--c-border-strong)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-gray-100-rgb` | `252 252 252` | Brand / Palette Token |
| `--color-gray-200-rgb` | `248 248 249` | Brand / Palette Token |
| `--color-gray-300-rgb` | `241 241 247` | Brand / Palette Token |
| `--color-gray-400-rgb` | `224 226 231` | Brand / Palette Token |
| `--color-gray-500-rgb` | `215 216 222` | Brand / Palette Token |
| `--color-gray-600-rgb` | `178 188 189` | Brand / Palette Token |
| `--color-gray-700-rgb` | `100 113 121` | Brand / Palette Token |
| `--color-gray-800-rgb` | `48 48 50` | Brand / Palette Token |
| `--color-gray-900-rgb` | `35 32 32` | Brand / Palette Token |
| `--color-gray-1000-rgb` | `23 21 21` | Brand / Palette Token |
| `--color-green-200-rgb` | `203, 255, 218` | Brand / Palette Token |
| `--color-green-400-rgb` | `53 255 146` | Brand / Palette Token |
| `--color-green-500-rgb` | `37 100 66` | Brand / Palette Token |
| `--color-blue-100-rgb` | `160 216 255` | Brand / Palette Token |
| `--color-blue-500-rgb` | `37 99 235` | Brand / Palette Token |
| `--color-pink-100-rgb` | `255 223 254` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Satoshi 2027`.
- **Primary Body Stack**: `Satoshi 2027`.
- **Technical / Metadata Stack**: `Rubik Mono One`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 81px`, `line-height: 89.1px`, `font-weight: 500`); rule `h1` (`font-size: clamp(2rem,5vw,3rem)`, `line-height: 1.1`, `font-weight: 700`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 57.6px`, `line-height: 63.36px`, `font-weight: 500`); rule `h2` (`font-size: clamp(1.5rem,3.5vw,2rem)`, `line-height: 1.2`, `font-weight: 700`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 500`); CSS variables `--font-size-vw-body: 1.5vw`, `--font-size-body: clamp(1.125rem, var(--font-size-vw-body), 1.5rem)`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 500`); CSS variables `--font-family-mono: "Roboto Mono", monospace`, `--mono: "Roboto Mono 2027",ui-monospace,Menlo,monospace`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `body.report2027-page .rw>i`**: `transition: transform .5s cubic-bezier(.65,0,.35,1) calc(var(--i,0)*70ms)` extracted from `www-teamcafeteria-com_2027` stylesheet.
- **Selector `body.report2027-page #nav button`**: `transition: opacity .3s` extracted from `www-teamcafeteria-com_2027` stylesheet.
- **Selector `body.report2027-page #nav .navt .tx`**: `transition: transform .55s cubic-bezier(.65,0,.35,1),opacity .4s` extracted from `www-teamcafeteria-com_2027` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.65,0,.35,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.fact>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — 2027 — a [cafeteria] report                │
│ ====================================================================== │
│ [ <header.site-header> (1440x58px)    | ask AI → · studies →         ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.report-doc> (w=1440px)                        | │
│ | H1: 2027 — a [cafeteria] report                                    | │
│ | Substrate: #000000 | Ink: #fcfcfc | Accent: #35ff92                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.fact>) max-w: 1440px                       | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Shoes                        |  | Spend                        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.fact:nth(2)>) — Collabs                    | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | https://www.teamcafeteria.com/2027   │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 24px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.site-header>    ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<article.report-doc>) — 390px Vertical Lead            | │
│ | H1: 2027 — a [cafeteria] report                                    | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.fact>) — 1-Col Stack                      | │
│ | [ Item 1: Shoes                                                  ] | │
│ | [ Item 2: Spend                                                  ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.fact:nth(2)>) — 1-Col (Collabs)             | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `www-teamcafeteria-com_2027`)**:
   - Landmark `<header class="site-header">` (`1440x58px`) hosting `2027 — a [cafeteria] report` navigation (`ask AI → · studies →`), DOM attributes (`data-nav-flow-ready="true"`, `data-nav-pill-ready="true"`, `data-cta-location="use_cases_menu"`, `data-track-cta`), and stylesheet rule `font-face { font-family:Anton;font-weight:100 900;font-display:swap;src:url(/_astro/... }`.
2. **Hero Stage & Focal Lead (<article.report-doc> — `2027 — a [cafeteria] report`)**:
   - Landmark `<article class="report-doc">` presenting display lead `2027 — a [cafeteria] report` and copy excerpt *"we asked 1,423 young consumers about the year ahead"* over `#000000` canvas and `#fcfcfc` ink.
3. **Primary Showcase & Content Grid (<section.fact> — `Shoes`)**:
   - Landmark `<section class="fact">` rendering section `Shoes` with copy *"Back to the experience"*, asset references (`favicon.svg`, `Satoshi-Medium.dlbj618m.woff2`, `Satoshi-Bold.BRirVCsc.woff2`, `Satoshi-Black.BWj4aoZT.woff2`), and grid rule `body.report2027-page .report2027 { line-height:normal }`.
4. **Interactive Detail & Feature Matrix (<section.fact:nth(2)> — `Spend`)**:
   - Landmark `<section class="fact">` framing `Spend` and `Collabs` (*"277 hours of conversation"*) with `#1d1b1b` surface cards, `#35ff92` accents, and `track { position:relative;width:1px;pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.teamcafeteria.com/2027`)**:
   - Landmark `<footer class="footer theme-dark">` anchoring `2027 — a [cafeteria] report` footer links (`ask AI → · studies →`), copy *"50% female · 48% male · median age 20"*, and `#232020` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-teamcafeteria-com_2027 (2027 — a [cafeteria] report)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-teamcafeteria-com_2027` (**2027 — a [cafeteria] report** — `https://www.teamcafeteria.com/2027`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#35ff92`).
- **Identity & Domain Context**: 1,423 people told us what 2027 looks like. A scroll-driven [cafeteria] report.
- **Primary Substrate**: `#000000` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#fcfcfc`, **Accent / Highlight**: `#35ff92`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#fcfcfc` primary typography and `#35ff92` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Satoshi 2027` for display copy (`2027 — a [cafeteria] report`) with `Satoshi 2027` and `Rubik Mono One`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 24px`, padding `4px`) with `cubic-bezier(.65,0,.35,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-teamcafeteria-com_2027` in your global stylesheet:

:root {
  /* 2027 — a [cafeteria] report (www-teamcafeteria-com_2027) — Live-Grounded CSS Variables */
  --color-gray-100-rgb: 252 252 252; /* Brand / Palette Token (www-teamcafeteria-com_2027) */
  --color-gray-200-rgb: 248 248 249; /* Brand / Palette Token (www-teamcafeteria-com_2027) */
  --color-gray-300-rgb: 241 241 247; /* Brand / Palette Token (www-teamcafeteria-com_2027) */
  --color-gray-400-rgb: 224 226 231; /* Brand / Palette Token (www-teamcafeteria-com_2027) */
  --color-gray-500-rgb: 215 216 222; /* Brand / Palette Token (www-teamcafeteria-com_2027) */
  --color-gray-600-rgb: 178 188 189; /* Brand / Palette Token (www-teamcafeteria-com_2027) */
  --color-gray-700-rgb: 100 113 121; /* Brand / Palette Token (www-teamcafeteria-com_2027) */
  --color-gray-800-rgb: 48 48 50; /* Brand / Palette Token (www-teamcafeteria-com_2027) */
  --color-gray-900-rgb: 35 32 32; /* Brand / Palette Token (www-teamcafeteria-com_2027) */
  --color-gray-1000-rgb: 23 21 21; /* Brand / Palette Token (www-teamcafeteria-com_2027) */
  --color-green-200-rgb: 203, 255, 218; /* Brand / Palette Token (www-teamcafeteria-com_2027) */
  --color-green-400-rgb: 53 255 146; /* Brand / Palette Token (www-teamcafeteria-com_2027) */
  --color-green-500-rgb: 37 100 66; /* Brand / Palette Token (www-teamcafeteria-com_2027) */
  --color-blue-100-rgb: 160 216 255; /* Brand / Palette Token (www-teamcafeteria-com_2027) */
  --color-blue-500-rgb: 37 99 235; /* Brand / Palette Token (www-teamcafeteria-com_2027) */
  --color-pink-100-rgb: 255 223 254; /* Typography Ink Token (www-teamcafeteria-com_2027) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#fcfcfc` — grounded in live computed `footer` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#1d1b1b` — grounded in live computed `nav` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#35ff92` — grounded in `var(--accent)` in `:root`
- **Secondary / Muted Copy**: `#686b6b` — grounded in `var(--c-text-mute)` in `:root`
- **Structural Hairline Border**: `#232020` — grounded in `var(--c-border-strong)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `4px` lateral canvas padding with `24px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 24px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding
- **Media Queries**: `@media (min-width:761px)`, `@media (max-width:760px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1100px)`
- **Corner Radii**: `22%`, `40px`, `50%`, `99px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Satoshi 2027`
- **Body Font Stack**: `Satoshi 2027`
- **Monospace / Technical Font Stack**: `Rubik Mono One`
- **H1 Display Rule**: live computed `h1` (`font-size: 81px`, `line-height: 89.1px`, `font-weight: 500`); rule `h1` (`font-size: clamp(2rem,5vw,3rem)`, `line-height: 1.1`, `font-weight: 700`)
- **H2 Section Rule**: live computed `h2` (`font-size: 57.6px`, `line-height: 63.36px`, `font-weight: 500`); rule `h2` (`font-size: clamp(1.5rem,3.5vw,2rem)`, `line-height: 1.2`, `font-weight: 700`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 500`); CSS variables `--font-size-vw-body: 1.5vw`, `--font-size-body: clamp(1.125rem, var(--font-size-vw-body), 1.5rem)`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 500`); CSS variables `--font-family-mono: "Roboto Mono", monospace`, `--mono: "Roboto Mono 2027",ui-monospace,Menlo,monospace`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-teamcafeteria-com_2027` (`2027 — a [cafeteria] report`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `www-teamcafeteria-com_2027`)**:
   - DOM & Selectors: Landmark `<header class="site-header">` (`1440x58px`) hosting `2027 — a [cafeteria] report` navigation (`ask AI → · studies →`), DOM attributes (`data-nav-flow-ready="true"`, `data-nav-pill-ready="true"`, `data-cta-location="use_cases_menu"`, `data-track-cta`), and stylesheet rule `font-face { font-family:Anton;font-weight:100 900;font-display:swap;src:url(/_astro/... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `www-teamcafeteria-com_2027`)` (`www-teamcafeteria-com_2027`) adapts across `@media (min-width:761px)`, `@media (max-width:760px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1100px)` with `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `ask AI → · studies →`.
2. **Hero Stage & Focal Lead (<article.report-doc> — `2027 — a [cafeteria] report`)**:
   - DOM & Selectors: Landmark `<article class="report-doc">` presenting display lead `2027 — a [cafeteria] report` and copy excerpt *"we asked 1,423 young consumers about the year ahead"* over `#000000` canvas and `#fcfcfc` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#000000` background with `#fcfcfc` headline `2027 — a [cafeteria] report`.
3. **Primary Showcase & Content Grid (<section.fact> — `Shoes`)**:
   - DOM & Selectors: Landmark `<section class="fact">` rendering section `Shoes` with copy *"Back to the experience"*, asset references (`favicon.svg`, `Satoshi-Medium.dlbj618m.woff2`, `Satoshi-Bold.BRirVCsc.woff2`, `Satoshi-Black.BWj4aoZT.woff2`), and grid rule `body.report2027-page .report2027 { line-height:normal }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.fact> — `Shoes`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 24px`) on desktop and Single-column vertical stack at `390px` viewport width with `4px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.fact:nth(2)> — `Spend`)**:
   - DOM & Selectors: Landmark `<section class="fact">` framing `Spend` and `Collabs` (*"277 hours of conversation"*) with `#1d1b1b` surface cards, `#35ff92` accents, and `track { position:relative;width:1px;pointer-events:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.fact:nth(2)> — `Spend`)` uses `22%`, `40px`, `50%`, `99px` radii, `#35ff92` highlights, and assets (favicon.svg, Satoshi-Medium.dlbj618m.woff2, Satoshi-Bold.BRirVCsc.woff2).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.teamcafeteria.com/2027`)**:
   - DOM & Selectors: Landmark `<footer class="footer theme-dark">` anchoring `2027 — a [cafeteria] report` footer links (`ask AI → · studies →`), copy *"50% female · 48% male · median age 20"*, and `#232020` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://www.teamcafeteria.com/2027`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `4px` lateral canvas padding with `24px` grid gap and attributes (data-nav-flow-ready="true", data-nav-pill-ready="true", data-cta-location="use_cases_menu").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"we asked 1,423 young consumers about the year ahead"*
- Copy Excerpt 2: *"Back to the experience"*
- Copy Excerpt 3: *"277 hours of conversation"*
- Copy Excerpt 4: *"50% female · 48% male · median age 20"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`www-teamcafeteria-com_2027`)**:
- `font-face { font-family:Anton;font-weight:100 900;font-display:swap;src:url(/_astro/... }`
- `body.report2027-page .report2027 { line-height:normal }`
- `track { position:relative;width:1px;pointer-events:none }`
- `stage { position:fixed;left:0;top:0;width:100vw;height:100vh;height:100lvh;overf... }`
- `pc { position:absolute;left:0;top:0;width:100%;height:100%;display:block }`
- **Per-Selector Transition Rules**:
- **Selector `body.report2027-page .rw>i`**: `transition: transform .5s cubic-bezier(.65,0,.35,1) calc(var(--i,0)*70ms)` extracted from `www-teamcafeteria-com_2027` stylesheet.
- **Selector `body.report2027-page #nav button`**: `transition: opacity .3s` extracted from `www-teamcafeteria-com_2027` stylesheet.
- **Selector `body.report2027-page #nav .navt .tx`**: `transition: transform .55s cubic-bezier(.65,0,.35,1),opacity .4s` extracted from `www-teamcafeteria-com_2027` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.65,0,.35,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.fact>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-teamcafeteria-com_2027`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
