---
title: "UI Prompt Blueprint: citadelgroup-org"
date: 2026-11-23
captured_at: 2026-11-23
target: "citadelgroup-org"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ffa500`)"
---

# UI Design System & Master Generation Blueprint: citadelgroup-org

> **Citadel National Construction Group · Nationwide Construction** (https://citadelgroup.org/) — Citadel connects leading regional construction firms into one nationwide network, combining local expertise with national resources to de...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Citadel National Construction Group · Nationwide Construction** (`https://citadelgroup.org/`). Citadel connects leading regional construction firms into one nationwide network, combining local expertise with national resources to de...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ffa500`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#ffa500` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Montserrat` for display copy (`NATIONAL REACH. LOCAL EXPERTISE.`) with `Montserrat` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1124px` container bounds (`gap: 1rem`, padding `.58rem`) with `cubic-bezier(.22,1,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1124px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `.58rem` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `999px`, `.2rem`, `.5rem`, `.25rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1124px`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.58rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:767px)`, `@media (max-width:767px)`, `@media (min-width:768px)and (max-width:1139px)`, `@media (min-width:1140px)and (max-width:1279px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f7953e` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffa500` | `.citadel-footer-brand-grid a:hover { color: orange }` (`#ffa500`) |
| **Secondary / Muted Copy** | `#555555` | `var(--resource-hub-text-muted)` in `:root` |
| **Structural Hairline Border** | `#aaa69e` | `var(--resource-hub-border)` in `:root` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-editor-canvas-background`)** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Variable Token (`--citadel-dark-orange`)** | `#f87000` | `var(--citadel-dark-orange)` in `:root` |
| **Variable Token (`--citadel-medium-grey`)** | `#818486` | `var(--citadel-medium-grey)` in `:root` |
| **Variable Token (`--citadel-light-grey`)** | `#e3e3e4` | `var(--citadel-light-grey)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |
| `--wp-admin-theme-color--rgb` | `0,124,186` | Brand / Palette Token |
| `--wp-admin-theme-color-darker-10` | `#006ba1` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-10--rgb` | `0,107,160.5` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20` | `#005a87` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20--rgb` | `0,90,135` | Canvas / Surface Token |
| `--wp-admin-border-width-focus` | `2px` | Layout / Spatial Grid Token |
| `--wp-admin--admin-bar--position-offset` | `var(--wp-admin--admin-bar--height,0px)` | Dimension / Scale Token |
| `--citadel-orange` | `#f7953e` | Color / Atmospheric Token |
| `--citadel-dark-orange` | `#f87000` | Canvas / Surface Token |
| `--citadel-medium-grey` | `#818486` | Color / Atmospheric Token |
| `--citadel-light-grey` | `#e3e3e4` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Montserrat`.
- **Primary Body Stack**: `Montserrat`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 48px`, `font-weight: 700`, `letter-spacing: 3.84px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 30px`, `line-height: 36px`, `font-weight: 600`, `letter-spacing: 4.5px`); rule `h2` (`font-size: clamp(2.9rem,2.9vw,3.9rem)`, `line-height: 1.02`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-citadel-body: "Montserrat", system-ui, sans-serif`; rule `p` (`font-size: .88rem`, `line-height: 1.35`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.citadel-site-header`**: `transition: color .22s ease` extracted from `citadelgroup-org` stylesheet.
- **Selector `.logo-cover`**: `transition: background-color .36s ease,opacity .36s ease` extracted from `citadelgroup-org` stylesheet.
- **Selector `.citadel-site-nav-link`**: `transition: color .18s ease` extracted from `citadelgroup-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.citadel-site-header>` and `<section.citadel-about>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Citadel National Construction Group · Nati │
│ ====================================================================== │
│ [ <header.citadel-site-h (1440x91px)  | About · Case Studies · Map · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.citadel-hero> (w=1440px)                      | │
│ | H1: NATIONAL REACH. LOCAL EXPERTISE.                               | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #ffa500                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.citadel-about>) max-w: 1124px              | │
│ | +------------------------------+  +------------------------------+ | │
│ | | National Reach. Local Expert |  | Serving Clients With Nationa | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.citadel-partners>) — Seven firms. One conn | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer-) | https://citadelgroup.org/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.citadel-site-hea) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.citadel-hero>) — 390px Vertical Lead          | │
│ | H1: NATIONAL REACH. LOCAL EXPERTISE.                               | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.citadel-about) — 1-Col Stack              | │
│ | [ Item 1: National Reach. Local Expertise.                       ] | │
│ | [ Item 2: Serving Clients With National Needs                    ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.citadel-partner) — 1-Col (Seven firms. One c) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer-) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.citadel-site-header> — `citadelgroup-org`)**:
   - Landmark `<header class="citadel-site-header is-over-hero">` (`1440x91px`) hosting `Citadel National Construction Group ` navigation (`About · Case Studies · Map · Principals`), DOM attributes (`data-wp-strategy="async"`, `data-loaded="true"`, `data-module="scrollspy-nav"`, `data-logo-cover-surface="hidden"`), and stylesheet rule `html { scroll-behavior:smooth;overflow-x:clip }`.
2. **Hero Stage & Focal Lead (<section.citadel-hero> — `NATIONAL REACH. LOCAL EXPERTISE.`)**:
   - Landmark `<section class="citadel-hero">` presenting display lead `NATIONAL REACH. LOCAL EXPERTISE.` and copy excerpt *"Citadel National Construction Group leverages seven best-in-class"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.citadel-about> — `National Reach. Local Expertise.`)**:
   - Landmark `<section class="citadel-about">` rendering section `National Reach. Local Expertise.` with copy *"L o c a l s t r e n g t h . N a t i o n a l s c a l e ."*, asset references (`www.googletagmanager.com`, `embed`, `theme-core.min.css`, `framework-md.min.css`), and grid rule `body { margin:0;font-family:var(--font-citadel-body);color:var(--color-text-pri... }`.
4. **Interactive Detail & Feature Matrix (<section.citadel-partners> — `Serving Clients With National Need`)**:
   - Landmark `<section class="citadel-partners py-10">` framing `Serving Clients With National Needs` and `Seven firms. One connected construction network.` (*"L o c a l s t r e n g t h ."*) with `#f7953e` surface cards, `#ffa500` accents, and `.screen-reader-text { position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hi... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer-meta> — `https://citadelgroup.org/`)**:
   - Landmark `<footer class="site-footer-meta">` anchoring `Citadel National Construction Gr` footer links (`About · Case Studies · Map · Principals`), copy *"N a t i o n a l s c a l e ."*, and `#aaa69e` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: citadelgroup-org (Citadel National Construction Group · Nationwide Construction)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `citadelgroup-org` (**Citadel National Construction Group · Nationwide Construction** — `https://citadelgroup.org/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ffa500`).
- **Identity & Domain Context**: Citadel connects leading regional construction firms into one nationwide network, combining local expertise with national resources to de...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#ffa500`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#ffa500` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Montserrat` for display copy (`NATIONAL REACH. LOCAL EXPERTISE.`) with `Montserrat` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1124px` container bounds (`gap: 1rem`, padding `.58rem`) with `cubic-bezier(.22,1,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `citadelgroup-org` in your global stylesheet:

:root {
  /* Citadel National Construction Group · Nationwide Construction (citadelgroup-org) — Live-Grounded CSS Variables */
  --wp-block-synced-color: #7a00df; /* Brand / Palette Token (citadelgroup-org) */
  --wp-block-synced-color--rgb: 122,0,223; /* Brand / Palette Token (citadelgroup-org) */
  --wp-bound-block-color: var(--wp-block-synced-color); /* Brand / Palette Token (citadelgroup-org) */
  --wp-editor-canvas-background: #ddd; /* Canvas / Surface Token (citadelgroup-org) */
  --wp-admin-theme-color: #007cba; /* Brand / Palette Token (citadelgroup-org) */
  --wp-admin-theme-color--rgb: 0,124,186; /* Brand / Palette Token (citadelgroup-org) */
  --wp-admin-theme-color-darker-10: #006ba1; /* Canvas / Surface Token (citadelgroup-org) */
  --wp-admin-theme-color-darker-10--rgb: 0,107,160.5; /* Canvas / Surface Token (citadelgroup-org) */
  --wp-admin-theme-color-darker-20: #005a87; /* Canvas / Surface Token (citadelgroup-org) */
  --wp-admin-theme-color-darker-20--rgb: 0,90,135; /* Canvas / Surface Token (citadelgroup-org) */
  --wp-admin-border-width-focus: 2px; /* Layout / Spatial Grid Token (citadelgroup-org) */
  --wp-admin--admin-bar--position-offset: var(--wp-admin--admin-bar--height,0px); /* Dimension / Scale Token (citadelgroup-org) */
  --citadel-orange: #f7953e; /* Color / Atmospheric Token (citadelgroup-org) */
  --citadel-dark-orange: #f87000; /* Canvas / Surface Token (citadelgroup-org) */
  --citadel-medium-grey: #818486; /* Color / Atmospheric Token (citadelgroup-org) */
  --citadel-light-grey: #e3e3e4; /* Canvas / Surface Token (citadelgroup-org) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f7953e` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#ffa500` — grounded in `.citadel-footer-brand-grid a:hover { color: orange }` (`#ffa500`)
- **Secondary / Muted Copy**: `#555555` — grounded in `var(--resource-hub-text-muted)` in `:root`
- **Structural Hairline Border**: `#aaa69e` — grounded in `var(--resource-hub-border)` in `:root`
- **Variable Token (`--wp-block-synced-color`)**: `#7a00df` — grounded in `var(--wp-block-synced-color)` in `:root`
- **Variable Token (`--wp-editor-canvas-background`)**: `#dddddd` — grounded in `var(--wp-editor-canvas-background)` in `:root`
- **Variable Token (`--wp-admin-theme-color`)**: `#007cba` — grounded in `var(--wp-admin-theme-color)` in `:root`
- **Variable Token (`--wp-admin-theme-color-darker-10`)**: `#006ba1` — grounded in `var(--wp-admin-theme-color-darker-10)` in `:root`
- **Variable Token (`--wp-admin-theme-color-darker-20`)**: `#005a87` — grounded in `var(--wp-admin-theme-color-darker-20)` in `:root`
- **Variable Token (`--citadel-dark-orange`)**: `#f87000` — grounded in `var(--citadel-dark-orange)` in `:root`
- **Variable Token (`--citadel-medium-grey`)**: `#818486` — grounded in `var(--citadel-medium-grey)` in `:root`
- **Variable Token (`--citadel-light-grey`)**: `#e3e3e4` — grounded in `var(--citadel-light-grey)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1124px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `.58rem` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1124px`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.58rem` horizontal padding
- **Media Queries**: `@media (min-width:767px)`, `@media (max-width:767px)`, `@media (min-width:768px)and (max-width:1139px)`, `@media (min-width:1140px)and (max-width:1279px)`
- **Corner Radii**: `999px`, `.2rem`, `.5rem`, `.25rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Montserrat`
- **Body Font Stack**: `Montserrat`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 48px`, `line-height: 48px`, `font-weight: 700`, `letter-spacing: 3.84px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 30px`, `line-height: 36px`, `font-weight: 600`, `letter-spacing: 4.5px`); rule `h2` (`font-size: clamp(2.9rem,2.9vw,3.9rem)`, `line-height: 1.02`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-citadel-body: "Montserrat", system-ui, sans-serif`; rule `p` (`font-size: .88rem`, `line-height: 1.35`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `citadelgroup-org` (`Citadel National Construction Group · Nationwide Construction`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.citadel-site-header> — `citadelgroup-org`)**:
   - DOM & Selectors: Landmark `<header class="citadel-site-header is-over-hero">` (`1440x91px`) hosting `Citadel National Construction Group ` navigation (`About · Case Studies · Map · Principals`), DOM attributes (`data-wp-strategy="async"`, `data-loaded="true"`, `data-module="scrollspy-nav"`, `data-logo-cover-surface="hidden"`), and stylesheet rule `html { scroll-behavior:smooth;overflow-x:clip }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.citadel-site-header> — `citadelgroup-org`)` (`citadelgroup-org`) adapts across `@media (min-width:767px)`, `@media (max-width:767px)`, `@media (min-width:768px)and (max-width:1139px)`, `@media (min-width:1140px)and (max-width:1279px)` with `cubic-bezier(.22,1,.36,1)` transitions and links `About · Case Studies · Map · Principals`.
2. **Hero Stage & Focal Lead (<section.citadel-hero> — `NATIONAL REACH. LOCAL EXPERTISE.`)**:
   - DOM & Selectors: Landmark `<section class="citadel-hero">` presenting display lead `NATIONAL REACH. LOCAL EXPERTISE.` and copy excerpt *"Citadel National Construction Group leverages seven best-in-class"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#000000` headline `NATIONAL REACH. LOCAL EXPERTISE.`.
3. **Primary Showcase & Content Grid (<section.citadel-about> — `National Reach. Local Expertise.`)**:
   - DOM & Selectors: Landmark `<section class="citadel-about">` rendering section `National Reach. Local Expertise.` with copy *"L o c a l s t r e n g t h . N a t i o n a l s c a l e ."*, asset references (`www.googletagmanager.com`, `embed`, `theme-core.min.css`, `framework-md.min.css`), and grid rule `body { margin:0;font-family:var(--font-citadel-body);color:var(--color-text-pri... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.citadel-about> — `National Reach. Local Expertise.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1124px`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.58rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.citadel-partners> — `Serving Clients With National Need`)**:
   - DOM & Selectors: Landmark `<section class="citadel-partners py-10">` framing `Serving Clients With National Needs` and `Seven firms. One connected construction network.` (*"L o c a l s t r e n g t h ."*) with `#f7953e` surface cards, `#ffa500` accents, and `.screen-reader-text { position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hi... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.citadel-partners> — `Serving Clients With National Need`)` uses `999px`, `.2rem`, `.5rem`, `.25rem` radii, `#ffa500` highlights, and assets (www.googletagmanager.com, embed, theme-core.min.css).
5. **Colophon & Global Directory Footer (<footer.site-footer-meta> — `https://citadelgroup.org/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer-meta">` anchoring `Citadel National Construction Gr` footer links (`About · Case Studies · Map · Principals`), copy *"N a t i o n a l s c a l e ."*, and `#aaa69e` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer-meta> — `https://citadelgroup.org/`)` aligns to `1124px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `.58rem` lateral canvas padding with `1rem` grid gap and attributes (data-wp-strategy="async", data-loaded="true", data-module="scrollspy-nav").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Citadel National Construction Group leverages seven best-in-class contractors to d..."*
- Copy Excerpt 2: *"L o c a l s t r e n g t h . N a t i o n a l s c a l e ."*
- Copy Excerpt 3: *"L o c a l s t r e n g t h ."*
- Copy Excerpt 4: *"N a t i o n a l s c a l e ."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`citadelgroup-org`)**:
- `html { scroll-behavior:smooth;overflow-x:clip }`
- `body { margin:0;font-family:var(--font-citadel-body);color:var(--color-text-pri... }`
- `.screen-reader-text { position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hi... }`
- `.citadel-site-header.is-content-mode { background:transparent;box-shadow:none }`
- `.citadel-site-header.is-header-hi... { visibility:hidden;opacity:0;pointer-events:none;transform:translateY(-100%) }`
- **Per-Selector Transition Rules**:
- **Selector `.citadel-site-header`**: `transition: color .22s ease` extracted from `citadelgroup-org` stylesheet.
- **Selector `.logo-cover`**: `transition: background-color .36s ease,opacity .36s ease` extracted from `citadelgroup-org` stylesheet.
- **Selector `.citadel-site-nav-link`**: `transition: color .18s ease` extracted from `citadelgroup-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.citadel-site-header>` and `<section.citadel-about>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `citadelgroup-org`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
