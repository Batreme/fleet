---
title: "UI Prompt Blueprint: m3-pg-de"
date: 2026-11-24
captured_at: 2026-11-24
target: "m3-pg-de"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 6
subpages_crawled: 3
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0d6efd` accent)"
---

# UI Design System & Master Generation Blueprint: m3-pg-de

> **M3 Planungsgruppe** (https://m3-pg.de) — Nachhaltigkeit. Ästhetik. Wirtschaftlichkeit.

![Desktop Journey Filmstrip (1280x4968)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **M3 Planungsgruppe** (`https://m3-pg.de`). Nachhaltigkeit. Ästhetik. Wirtschaftlichkeit.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0d6efd` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0d6efd` accents.
  - **Grounded Typographic Hierarchy**: Uses `Inter` across display (`M3 Planungsgruppe`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1420px` container bounds (`gap: 1rem`, padding `2rem`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×4968px` (`assets/desktop-journey.webp`, `6` keyframes up to `y=3831px` / doc `4731px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1420px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `2rem` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `100%`, `0.375rem`, `.25rem`, `var(--bs-border-radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1420px`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (prefers-reduced-motion:no-preference)`, `@media (min-width:1200px)`, `@media (min-width:576px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f8f9fa` | `var(--bs-tertiary-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#0d6efd` | `var(--bs-primary)` in `:root` |
| **Secondary / Muted Copy** | `#6c757d` | `var(--bs-secondary)` in `:root` |
| **Structural Hairline Border** | `#9ec5fe` | `var(--bs-primary-border-subtle)` in `:root` |
| **Variable Token (`--bs-indigo`)** | `#6610f2` | `var(--bs-indigo)` in `:root` |
| **Variable Token (`--bs-purple`)** | `#6f42c1` | `var(--bs-purple)` in `:root` |
| **Variable Token (`--bs-pink`)** | `#d63384` | `var(--bs-pink)` in `:root` |
| **Variable Token (`--bs-red`)** | `#dc3545` | `var(--bs-red)` in `:root` |
| **Variable Token (`--bs-orange`)** | `#fd7e14` | `var(--bs-orange)` in `:root` |
| **Variable Token (`--bs-yellow`)** | `#ffc107` | `var(--bs-yellow)` in `:root` |
| **Variable Token (`--bs-green`)** | `#198754` | `var(--bs-green)` in `:root` |
| **Variable Token (`--bs-teal`)** | `#20c997` | `var(--bs-teal)` in `:root` |
| **Variable Token (`--bs-cyan`)** | `#0dcaf0` | `var(--bs-cyan)` in `:root` |
| **Variable Token (`--bs-gray-dark`)** | `#343a40` | `var(--bs-gray-dark)` in `:root` |
| **Variable Token (`--bs-gray-200`)** | `#e9ecef` | `var(--bs-gray-200)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bs-blue` | `#0d6efd` | Color / Atmospheric Token |
| `--bs-indigo` | `#6610f2` | Color / Atmospheric Token |
| `--bs-purple` | `#6f42c1` | Color / Atmospheric Token |
| `--bs-pink` | `#d63384` | Typography Ink Token |
| `--bs-red` | `#dc3545` | Color / Atmospheric Token |
| `--bs-orange` | `#fd7e14` | Color / Atmospheric Token |
| `--bs-yellow` | `#ffc107` | Color / Atmospheric Token |
| `--bs-green` | `#198754` | Color / Atmospheric Token |
| `--bs-teal` | `#20c997` | Color / Atmospheric Token |
| `--bs-cyan` | `#0dcaf0` | Color / Atmospheric Token |
| `--bs-black` | `#000` | Canvas / Surface Token |
| `--bs-white` | `#fff` | Canvas / Surface Token |
| `--bs-gray` | `#6c757d` | Color / Atmospheric Token |
| `--bs-gray-dark` | `#343a40` | Canvas / Surface Token |
| `--bs-gray-100` | `#f8f9fa` | Color / Atmospheric Token |
| `--bs-gray-200` | `#e9ecef` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 155.4px`, `line-height: 155.4px`, `font-weight: 700`, `letter-spacing: -4.662px`); rule `,h1` (`font-size: calc(1.375rem + 1.5vw)`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 64px`, `line-height: 74px`, `font-weight: 600`, `letter-spacing: -1.92px`); rule `,h2` (`font-size: calc(1.325rem + .9vw)`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: -0.16px`); CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `body` (`font-size: 18px`, `line-height: 26px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 20px`, `line-height: 24px`, `font-weight: 600`, `letter-spacing: -0.4px`); rule `,small` (`font-size: .875em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.form-control`**: `transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out` extracted from `m3-pg-de` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none` extracted from `m3-pg-de` stylesheet.
- **Selector `.form-control::-webkit-file-uploa...`**: `transition: color .15s ease-in-out,background-color .15s ease-in-out,borde...` extracted from `m3-pg-de` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.header-desk>` and `<section.page-template>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `4731px`, deepest scrollY reached `3831px` across `6` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Hover Physics (`primary_cta` · `M3 Planungsgruppe`)**: Computed transition `0s` / `ease` (no static color/transform shift captured at rest).
- **Route Transition Architecture**: First internal navigation (`/blog/`) measured as `MPA` in `1882ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — M3 Planungsgruppe                          │
│ ====================================================================== │
│ [ <header.header-desk> (1440x60px)    | M3 Planungsgruppe · Leistung ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.wp-singular> (w=1440px)                       | │
│ | H1: M3 Planungsgruppe                                              | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #0d6efd                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.page-template>) max-w: 1420px              | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Nachhaltigkeit. Ästhetik. Wi |  | Planung, die Bestand hat.    | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.page-template-tem) — B18 – Fachwerk trifft | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.page-templat) | https://m3-pg.de                     │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.header-desk>    ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.wp-singular>) — 390px Vertical Lead           | │
│ | H1: M3 Planungsgruppe                                              | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.page-template) — 1-Col Stack              | │
│ | [ Item 1: Nachhaltigkeit. Ästhetik. Wirtschaftlichkeit.          ] | │
│ | [ Item 2: Planung, die Bestand hat.                              ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.page-template-t) — 1-Col (B18 – Fachwerk tri) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.page-templat) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header-desk> — `m3-pg-de`)**:
   - Landmark `<header class="header-desk">` (`1440x60px`) hosting `M3 Planungsgruppe` navigation (`M3 Planungsgruppe · Leistungen · Projekte · Über uns · Blog`), DOM attributes (`data-wp-strategy="defer"`, `data-more="Mehr erfahren"`, `data-less="Weniger"`, `data-more="Mehr erfahren"`), and stylesheet rule `.bi-123::before { content:"\f67f" }`.
2. **Hero Stage & Focal Lead (<section.wp-singular> — `M3 Planungsgruppe`)**:
   - Landmark `<section class="wp-singular">` presenting display lead `M3 Planungsgruppe` and copy excerpt *"Gute Planung verbindet für uns Nachhaltigkeit, Ästhetik und Wirts"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.page-template> — `Nachhaltigkeit. Ästhetik. Wirtscha`)**:
   - Landmark `<section class="page-template">` rendering section `Nachhaltigkeit. Ästhetik. Wirtschaftlichkeit.` with copy *"Unser Fokus liegt auf präziser Planung, bewusst eingesetzten Mate"*, asset references (`bootstrap.min.css`, `slick.min.css`, `main.css`, `responsive.css`), and grid rule `.bi-alarm-fill::before { content:"\f101" }`.
4. **Interactive Detail & Feature Matrix (<section.page-template-templates> — `Planung, die Bestand hat.`)**:
   - Landmark `<section class="page-template-templates">` framing `Planung, die Bestand hat.` and `B18 – Fachwerk trifft Glas` (*"Jedes Projekt beginnt mit einem offenen und zielgerichteten Dialo"*) with `#f8f9fa` surface cards, `#0d6efd` accents, and `.bi-alarm::before { content:"\f102" }`.
5. **Colophon & Global Directory Footer (<footer.page-template-home> — `https://m3-pg.de`)**:
   - Landmark `<footer class="page-template-home">` anchoring `M3 Planungsgruppe` footer links (`M3 Planungsgruppe · Leistungen · Projekte · Über uns · Blog`), copy *"Auf dieser Grundlage entwickeln wir eine klare Projektstrate"*, and `#9ec5fe` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `#intro` · sticky/fixed elements: `2`
- **Step 02** (`y=850px`, `22%`): Active landmark `Planung, die Bestand hat.` · sticky/fixed elements: `3`
- **Step 03** (`y=1700px`, `44%`): Active landmark `#logo-middle` · sticky/fixed elements: `3`
- **Step 04** (`y=2550px`, `67%`): Active landmark `Labwerk` · sticky/fixed elements: `3`
- **Step 05** (`y=3400px`, `89%`): Active landmark `WIR DENKEN BAUPROJEKTE ALS SYSTEM – GESTALTET, GE...` · sticky/fixed elements: `3`
- **Step 06** (`y=3831px`, `100%`): Active landmark `M3 Planungsgruppe` · sticky/fixed elements: `3`

### Multi-Page Internal Route Map
- **Listing Route (`/blog/`)**: `https://m3-pg.de/blog/` — H1: `Blog`, scrollHeight `2924px`, transition `MPA` (`1882ms`)
- **Detail Route (`/project/labwerk/`)**: `https://m3-pg.de/project/labwerk/` — H1: `NEUBAU EINES BÜRO- UND LABORGEBÄUDES MIT LAGERHALLE`, scrollHeight `6154px`, transition `direct` (`1165ms`)
- **Detail Route (`/project/hanghaus/`)**: `https://m3-pg.de/project/hanghaus/` — H1: `HANGHAUS`, scrollHeight `4774px`, transition `direct` (`1273ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: m3-pg-de (M3 Planungsgruppe)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `m3-pg-de` (**M3 Planungsgruppe** — `https://m3-pg.de`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0d6efd` accent).
- **Identity & Domain Context**: Nachhaltigkeit. Ästhetik. Wirtschaftlichkeit.
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#0d6efd`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0d6efd` accents.
  - **Grounded Typographic Hierarchy**: Uses `Inter` across display (`M3 Planungsgruppe`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1420px` container bounds (`gap: 1rem`, padding `2rem`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `m3-pg-de` in your global stylesheet:

:root {
  /* M3 Planungsgruppe (m3-pg-de) — Live-Grounded CSS Variables */
  --bs-blue: #0d6efd; /* Color / Atmospheric Token (m3-pg-de) */
  --bs-indigo: #6610f2; /* Color / Atmospheric Token (m3-pg-de) */
  --bs-purple: #6f42c1; /* Color / Atmospheric Token (m3-pg-de) */
  --bs-pink: #d63384; /* Typography Ink Token (m3-pg-de) */
  --bs-red: #dc3545; /* Color / Atmospheric Token (m3-pg-de) */
  --bs-orange: #fd7e14; /* Color / Atmospheric Token (m3-pg-de) */
  --bs-yellow: #ffc107; /* Color / Atmospheric Token (m3-pg-de) */
  --bs-green: #198754; /* Color / Atmospheric Token (m3-pg-de) */
  --bs-teal: #20c997; /* Color / Atmospheric Token (m3-pg-de) */
  --bs-cyan: #0dcaf0; /* Color / Atmospheric Token (m3-pg-de) */
  --bs-black: #000; /* Canvas / Surface Token (m3-pg-de) */
  --bs-white: #fff; /* Canvas / Surface Token (m3-pg-de) */
  --bs-gray: #6c757d; /* Color / Atmospheric Token (m3-pg-de) */
  --bs-gray-dark: #343a40; /* Canvas / Surface Token (m3-pg-de) */
  --bs-gray-100: #f8f9fa; /* Color / Atmospheric Token (m3-pg-de) */
  --bs-gray-200: #e9ecef; /* Color / Atmospheric Token (m3-pg-de) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f8f9fa` — grounded in `var(--bs-tertiary-bg)` in `:root`
- **Interactive Accent / Highlight**: `#0d6efd` — grounded in `var(--bs-primary)` in `:root`
- **Secondary / Muted Copy**: `#6c757d` — grounded in `var(--bs-secondary)` in `:root`
- **Structural Hairline Border**: `#9ec5fe` — grounded in `var(--bs-primary-border-subtle)` in `:root`
- **Variable Token (`--bs-indigo`)**: `#6610f2` — grounded in `var(--bs-indigo)` in `:root`
- **Variable Token (`--bs-purple`)**: `#6f42c1` — grounded in `var(--bs-purple)` in `:root`
- **Variable Token (`--bs-pink`)**: `#d63384` — grounded in `var(--bs-pink)` in `:root`
- **Variable Token (`--bs-red`)**: `#dc3545` — grounded in `var(--bs-red)` in `:root`
- **Variable Token (`--bs-orange`)**: `#fd7e14` — grounded in `var(--bs-orange)` in `:root`
- **Variable Token (`--bs-yellow`)**: `#ffc107` — grounded in `var(--bs-yellow)` in `:root`
- **Variable Token (`--bs-green`)**: `#198754` — grounded in `var(--bs-green)` in `:root`
- **Variable Token (`--bs-teal`)**: `#20c997` — grounded in `var(--bs-teal)` in `:root`
- **Variable Token (`--bs-cyan`)**: `#0dcaf0` — grounded in `var(--bs-cyan)` in `:root`
- **Variable Token (`--bs-gray-dark`)**: `#343a40` — grounded in `var(--bs-gray-dark)` in `:root`
- **Variable Token (`--bs-gray-200`)**: `#e9ecef` — grounded in `var(--bs-gray-200)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×4968px` (multi-frame vertical journey filmstrip (4968px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1420px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `2rem` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1420px`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (prefers-reduced-motion:no-preference)`, `@media (min-width:1200px)`, `@media (min-width:576px)`
- **Corner Radii**: `100%`, `0.375rem`, `.25rem`, `var(--bs-border-radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 155.4px`, `line-height: 155.4px`, `font-weight: 700`, `letter-spacing: -4.662px`); rule `,h1` (`font-size: calc(1.375rem + 1.5vw)`)
- **H2 Section Rule**: live computed `h2` (`font-size: 64px`, `line-height: 74px`, `font-weight: 600`, `letter-spacing: -1.92px`); rule `,h2` (`font-size: calc(1.325rem + .9vw)`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: -0.16px`); CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `body` (`font-size: 18px`, `line-height: 26px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 20px`, `line-height: 24px`, `font-weight: 600`, `letter-spacing: -0.4px`); rule `,small` (`font-size: .875em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `m3-pg-de` (`M3 Planungsgruppe`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header-desk> — `m3-pg-de`)**:
   - DOM & Selectors: Landmark `<header class="header-desk">` (`1440x60px`) hosting `M3 Planungsgruppe` navigation (`M3 Planungsgruppe · Leistungen · Projekte · Über uns · Blog`), DOM attributes (`data-wp-strategy="defer"`, `data-more="Mehr erfahren"`, `data-less="Weniger"`, `data-more="Mehr erfahren"`), and stylesheet rule `.bi-123::before { content:"\f67f" }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header-desk> — `m3-pg-de`)` (`m3-pg-de`) adapts across `@media (prefers-reduced-motion: reduce)`, `@media (prefers-reduced-motion:no-preference)`, `@media (min-width:1200px)`, `@media (min-width:576px)` with `cubic-bezier(.4,0,.2,1)` transitions and links `M3 Planungsgruppe · Leistungen · Projekte · Über uns · Blog`.
2. **Hero Stage & Focal Lead (<section.wp-singular> — `M3 Planungsgruppe`)**:
   - DOM & Selectors: Landmark `<section class="wp-singular">` presenting display lead `M3 Planungsgruppe` and copy excerpt *"Gute Planung verbindet für uns Nachhaltigkeit, Ästhetik und Wirts"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1280×4968px` desktop / `390×2616px` mobile) sets `#ffffff` background with `#000000` headline `M3 Planungsgruppe`.
3. **Primary Showcase & Content Grid (<section.page-template> — `Nachhaltigkeit. Ästhetik. Wirtscha`)**:
   - DOM & Selectors: Landmark `<section class="page-template">` rendering section `Nachhaltigkeit. Ästhetik. Wirtschaftlichkeit.` with copy *"Unser Fokus liegt auf präziser Planung, bewusst eingesetzten Mate"*, asset references (`bootstrap.min.css`, `slick.min.css`, `main.css`, `responsive.css`), and grid rule `.bi-alarm-fill::before { content:"\f101" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.page-template> — `Nachhaltigkeit. Ästhetik. Wirtscha`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1420px`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.page-template-templates> — `Planung, die Bestand hat.`)**:
   - DOM & Selectors: Landmark `<section class="page-template-templates">` framing `Planung, die Bestand hat.` and `B18 – Fachwerk trifft Glas` (*"Jedes Projekt beginnt mit einem offenen und zielgerichteten Dialo"*) with `#f8f9fa` surface cards, `#0d6efd` accents, and `.bi-alarm::before { content:"\f102" }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.page-template-templates> — `Planung, die Bestand hat.`)` uses `100%`, `0.375rem`, `.25rem`, `var(--bs-border-radius)` radii, `#0d6efd` highlights, and assets (bootstrap.min.css, slick.min.css, main.css).
5. **Colophon & Global Directory Footer (<footer.page-template-home> — `https://m3-pg.de`)**:
   - DOM & Selectors: Landmark `<footer class="page-template-home">` anchoring `M3 Planungsgruppe` footer links (`M3 Planungsgruppe · Leistungen · Projekte · Über uns · Blog`), copy *"Auf dieser Grundlage entwickeln wir eine klare Projektstrate"*, and `#9ec5fe` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.page-template-home> — `https://m3-pg.de`)` aligns to `1420px` (non-`@media` desktop container stylesheet rule) with `2rem` lateral canvas padding with `1rem` grid gap and attributes (data-wp-strategy="defer", data-more="Mehr erfahren", data-less="Weniger").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Gute Planung verbindet für uns Nachhaltigkeit, Ästhetik und Wirtschaftlichkeit. Wi..."*
- Copy Excerpt 2: *"Unser Fokus liegt auf präziser Planung, bewusst eingesetzten Materialien und einer..."*
- Copy Excerpt 3: *"Jedes Projekt beginnt mit einem offenen und zielgerichteten Dialog mit dem Auftrag..."*
- Copy Excerpt 4: *"Auf dieser Grundlage entwickeln wir eine klare Projektstrategie, die als verbindli..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`m3-pg-de`)**:
- `.bi-123::before { content:"\f67f" }`
- `.bi-alarm-fill::before { content:"\f101" }`
- `.bi-alarm::before { content:"\f102" }`
- `.bi-align-bottom::before { content:"\f103" }`
- `.bi-align-center::before { content:"\f104" }`
- **Per-Selector Transition Rules**:
- **Selector `.form-control`**: `transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out` extracted from `m3-pg-de` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none` extracted from `m3-pg-de` stylesheet.
- **Selector `.form-control::-webkit-file-uploa...`**: `transition: color .15s ease-in-out,background-color .15s ease-in-out,borde...` extracted from `m3-pg-de` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.header-desk>` and `<section.page-template>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `4731px` across 6 distinct viewport chapters.
- **Vertical Chapter Sequence**: #intro (0%) -> Planung, die Bestand hat. (22%) -> #logo-middle (44%) -> Labwerk (67%) -> WIR DENKEN BAUPROJEKTE ALS... (89%) -> M3 Planungsgruppe (100%).
- **Multi-Page Routes**: Scaffold internal routes `/blog/` (listing, MPA), `/project/labwerk/` (detail, direct), `/project/hanghaus/` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `m3-pg-de`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | #intro | `2` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `22%` | Planung, die Bestand hat. | `3` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `1700px` | `44%` | #logo-middle | `3` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `2550px` | `67%` | Labwerk | `3` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `3400px` | `89%` | WIR DENKEN BAUPROJEKTE ALS SYSTEM – GESTALTET... | `3` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `3831px` | `100%` | M3 Planungsgruppe | `3` | [desktop-step-06.webp](assets/desktop-step-06.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | NACHHALTIGKEIT. ÄSTHETIK. WIRTSCHAFTLICHK... | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `1915px` | `50%` | Labwerk | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `3830px` | `100%` | M3 Planungsgruppe | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://m3-pg.de/blog/` | Blog | `2924px` | `MPA` (`1882ms`) | [subpage-01-blog.webp](assets/subpage-01-blog.webp) |
| `2` | `detail` | `https://m3-pg.de/project/labwerk/` | NEUBAU EINES BÜRO- UND LABORGEBÄUDES... | `6154px` | `direct` (`1165ms`) | [subpage-02-project-labwerk.webp](assets/subpage-02-project-labwerk.webp) |
| `3` | `detail` | `https://m3-pg.de/project/hanghaus/` | HANGHAUS | `4774px` | `direct` (`1273ms`) | [subpage-03-project-hanghaus.webp](assets/subpage-03-project-hanghaus.webp) |

