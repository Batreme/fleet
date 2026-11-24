---
title: "UI Prompt Blueprint: www-3d-discovery-fr"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-3d-discovery-fr"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native+wheel
desktop_keyframes: 8
subpages_crawled: 3
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ebebeb` / `#f59e0b`)"
---

# UI Design System & Master Generation Blueprint: www-3d-discovery-fr

> **3D Discovery · Exploring New Dimensions** (https://www.3d-discovery.fr/) — Turn your spaces, projects and products into immersive web experiences: 3D exploration, content and interaction in one place to showcase,...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **3D Discovery · Exploring New Dimensions** (`https://www.3d-discovery.fr/`). Turn your spaces, projects and products into immersive web experiences: 3D exploration, content and interaction in one place to showcase,...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ebebeb` / `#f59e0b`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ebebeb` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1a1a1a` primary typography and `#f59e0b` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Sora` for display copy (`TURN YOUR SPACES INTO IMMERSIVE EXPE`) with `Inter` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1360px` container bounds (`gap: .5rem`, padding `1rem`) with `cubic-bezier(.8,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=6878px` / doc `11299px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1360px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `1rem` lateral canvas padding with `.5rem` grid gap.
- **Border Radius Scale**: `50%`, `999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1360px`, `gap: .5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ebebeb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1a1a1a` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e2e2e2` | `var(--bg-elevated)` in `:root` |
| **Interactive Accent / Highlight** | `#f59e0b` | `.badge--solid.badge--warning { background: #f59e0b }` |
| **Secondary / Muted Copy** | `#666666` | `var(--input-placeholder)` in `:root` |
| **Structural Hairline Border** | `#d4d4d4` | `var(--border-default)` in `:root` |
| **Variable Token (`--color-primary-light`)** | `#2e2e2e` | `var(--color-primary-light)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--sg-grade` | `url(#sg-grade)` | Design System Custom Token |
| `--color-primary` | `#1a1a1a` | Brand / Palette Token |
| `--color-primary-light` | `#2e2e2e` | Canvas / Surface Token |
| `--color-primary-dark` | `#1a1a1a` | Canvas / Surface Token |
| `--color-secondary` | `#1a1a1a` | Brand / Palette Token |
| `--header-height` | `64px` | Layout / Spatial Grid Token |
| `--header-height-mobile` | `56px` | Layout / Spatial Grid Token |
| `--container-padding` | `1.5rem` | Layout / Spatial Grid Token |
| `--transition-fast` | `.15s ease` | Motion / Easing Token |
| `--transition-base` | `.2s ease` | Motion / Easing Token |
| `--transition-slow` | `.3s ease` | Motion / Easing Token |
| `--transition-theme` | `.2s ease` | Brand / Palette Token |
| `--z-header` | `30` | Layout / Spatial Grid Token |
| `--z-modal` | `50` | Elevation / Border Token |
| `--z-tooltip` | `70` | Elevation / Border Token |
| `--bg-body` | `#ebebeb` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Sora`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: `JetBrains Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80px`, `line-height: 76px`, `font-weight: 500`, `letter-spacing: -1.6px`); rule `,.h1` (`font-size: 2.25rem`, `line-height: 1.1`, `letter-spacing: -.025em`, `font-weight: 700`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80px`, `line-height: 76px`, `font-weight: 500`, `letter-spacing: -1.6px`); rule `,.h2` (`font-size: 1.875rem`, `line-height: 1.1`, `letter-spacing: -.025em`, `font-weight: 700`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--tra-body-h: 16rem`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.8,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.65,0,.35,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `:after`**: `transition: .01ms!important` extracted from `www-3d-discovery-fr` stylesheet.
- **Selector `body`**: `transition: background-color var(--transition-theme),color var(--transitio...` extracted from `www-3d-discovery-fr` stylesheet.
- **Selector `::-webkit-scrollbar-track`**: `transition: background var(--transition-theme)` extracted from `www-3d-discovery-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.8,0,1,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.sg-section--seq>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native+wheel` (max document height `11299px`, deepest scrollY reached `6878px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `WebGL/Canvas`.
- **Hover Physics (`primary_cta` · `DEMO →`)**: Computed transition `0.25s, 0.25s` / `ease, ease` (no static color/transform shift captured at rest).
- **Theme Toggle Probe**: Detected `Switch to dark mode` (no body background diff).
- **Route Transition Architecture**: First internal navigation (`/en/solutions`) measured as `SPA` in `4007ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — 3D Discovery · Exploring New Dimensions    │
│ ====================================================================== │
│ [ <header.header> (1440x66px)         | Solutions · Experiences · Fe ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.sg-section> (w=1440px)                        | │
│ | H1: TURN YOUR SPACES INTO IMMERSIVE EXPERIENCES                    | │
│ | Substrate: #ebebeb | Ink: #1a1a1a | Accent: #f59e0b                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.sg-section--seq>) max-w: 1360px            | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Turn your spaces into immers |  | Choose your field            | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.sg-solutions>) — Seeing is understandi     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sg-footer>  ) | https://www.3d-discovery.fr/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .5rem)      │
│ ====================================================================== │
│ [ HEADER BAR (<header.header>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.sg-section>) — 390px Vertical Lead            | │
│ | H1: TURN YOUR SPACES INTO IMMERSIVE EXPERIENCES                    | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.sg-section--s) — 1-Col Stack              | │
│ | [ Item 1: Turn your spaces into immersive experiences            ] | │
│ | [ Item 2: Choose your field                                      ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.sg-solutions>) — 1-Col (Seeing is understa) | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sg-footer>  ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `www-3d-discovery-fr`)**:
   - Landmark `<header class="header">` (`1440x66px`) hosting `3D Discovery · Exploring New Dimensi` navigation (`Solutions · Experiences · Features · Blog`), DOM attributes (`data-theme="light"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.sg-section> — `TURN YOUR SPACES INTO IMMERSIVE EX`)**:
   - Landmark `<section class="sg-section">` presenting display lead `TURN YOUR SPACES INTO IMMERSIVE EXPERIENCES` and copy excerpt *"3D DISCOVERY · ©2026"* over `#ebebeb` canvas and `#1a1a1a` ink.
3. **Primary Showcase & Content Grid (<section.sg-section--seq> — `Turn your spaces into immersive ex`)**:
   - Landmark `<section class="sg-section sg-section--seq">` rendering section `Turn your spaces into immersive experiences` with copy *"3D Discovery · ©2026"*, asset references (`83afe278b6a6bb3c-s.p.0q-301v4kxxn...`, `c41ca59f1c34ba31-s.p.0xxb547n1hn7...`, `0ghcmdv7avfm..css`, `04vxxuqck~drg.css`), and grid rule `html:focus-within { scroll-behavior:smooth }`.
4. **Interactive Detail & Feature Matrix (<section.sg-solutions> — `Choose your field`)**:
   - Landmark `<section class="sg-section sg-solutions">` framing `Choose your field` and `Seeing is understanding` (*"Exploring new dimensions"*) with `#e2e2e2` surface cards, `#f59e0b` accents, and `body { min-height:100vh;line-height:1.5 }`.
5. **Colophon & Global Directory Footer (<footer.sg-footer> — `https://www.3d-discovery.fr/`)**:
   - Landmark `<footer class="sg-footer">` anchoring `3D Discovery · Exploring New Dim` footer links (`Solutions · Experiences · Features · Blog`), copy *"A single web experience for 3D exploration, content and inte"*, and `#d4d4d4` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `TURN YOUR SPACES INTO IMMERSIVE EXPERIENCES` · sticky/fixed elements: `2`
- **Step 02** (`y=850px`, `8%`): Active landmark `Section @ 8%` · sticky/fixed elements: `3`
- **Step 03** (`y=2563px`, `25%`): Active landmark `Section @ 25%` · sticky/fixed elements: `3`
- **Step 04** (`y=3426px`, `33%`): Active landmark `Section @ 33%` · sticky/fixed elements: `3`
- **Step 05** (`y=4289px`, `41%`): Active landmark `Section @ 41%` · sticky/fixed elements: `3`
- **Step 06** (`y=5152px`, `50%`): Active landmark `Section @ 50%` · sticky/fixed elements: `3`
- **Step 07** (`y=6015px`, `58%`): Active landmark `Section @ 58%` · sticky/fixed elements: `3`
- **Step 08** (`y=6878px`, `66%`): Active landmark `CHOOSE YOUR FIELD` · sticky/fixed elements: `3`

### Multi-Page Internal Route Map
- **Listing Route (`/en/solutions`)**: `https://www.3d-discovery.fr/en/solutions` — H1: `CHOOSE YOUR FIELD`, scrollHeight `2809px`, transition `SPA` (`4007ms`)
- **About Route (`/en/about`)**: `https://www.3d-discovery.fr/en/about` — H1: `About · 3D Discovery`, scrollHeight `2417px`, transition `direct` (`963ms`)
- **Listing Route (`/en/features`)**: `https://www.3d-discovery.fr/en/features` — H1: `EVERYTHING TO SHOW IT ALL`, scrollHeight `9728px`, transition `direct` (`585ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-3d-discovery-fr (3D Discovery · Exploring New Dimensions)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-3d-discovery-fr` (**3D Discovery · Exploring New Dimensions** — `https://www.3d-discovery.fr/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ebebeb` / `#f59e0b`).
- **Identity & Domain Context**: Turn your spaces, projects and products into immersive web experiences: 3D exploration, content and interaction in one place to showcase,...
- **Primary Substrate**: `#ebebeb` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#1a1a1a`, **Accent / Highlight**: `#f59e0b`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ebebeb` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1a1a1a` primary typography and `#f59e0b` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Sora` for display copy (`TURN YOUR SPACES INTO IMMERSIVE EXPE`) with `Inter` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1360px` container bounds (`gap: .5rem`, padding `1rem`) with `cubic-bezier(.8,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-3d-discovery-fr` in your global stylesheet:

:root {
  /* 3D Discovery · Exploring New Dimensions (www-3d-discovery-fr) — Live-Grounded CSS Variables */
  --sg-grade: url(#sg-grade); /* Design System Custom Token (www-3d-discovery-fr) */
  --color-primary: #1a1a1a; /* Brand / Palette Token (www-3d-discovery-fr) */
  --color-primary-light: #2e2e2e; /* Canvas / Surface Token (www-3d-discovery-fr) */
  --color-primary-dark: #1a1a1a; /* Canvas / Surface Token (www-3d-discovery-fr) */
  --color-secondary: #1a1a1a; /* Brand / Palette Token (www-3d-discovery-fr) */
  --header-height: 64px; /* Layout / Spatial Grid Token (www-3d-discovery-fr) */
  --header-height-mobile: 56px; /* Layout / Spatial Grid Token (www-3d-discovery-fr) */
  --container-padding: 1.5rem; /* Layout / Spatial Grid Token (www-3d-discovery-fr) */
  --transition-fast: .15s ease; /* Motion / Easing Token (www-3d-discovery-fr) */
  --transition-base: .2s ease; /* Motion / Easing Token (www-3d-discovery-fr) */
  --transition-slow: .3s ease; /* Motion / Easing Token (www-3d-discovery-fr) */
  --transition-theme: .2s ease; /* Brand / Palette Token (www-3d-discovery-fr) */
  --z-header: 30; /* Layout / Spatial Grid Token (www-3d-discovery-fr) */
  --z-modal: 50; /* Elevation / Border Token (www-3d-discovery-fr) */
  --z-tooltip: 70; /* Elevation / Border Token (www-3d-discovery-fr) */
  --bg-body: #ebebeb; /* Canvas / Surface Token (www-3d-discovery-fr) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ebebeb` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#1a1a1a` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#e2e2e2` — grounded in `var(--bg-elevated)` in `:root`
- **Interactive Accent / Highlight**: `#f59e0b` — grounded in `.badge--solid.badge--warning { background: #f59e0b }`
- **Secondary / Muted Copy**: `#666666` — grounded in `var(--input-placeholder)` in `:root`
- **Structural Hairline Border**: `#d4d4d4` — grounded in `var(--border-default)` in `:root`
- **Variable Token (`--color-primary-light`)**: `#2e2e2e` — grounded in `var(--color-primary-light)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1360px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `1rem` lateral canvas padding with `.5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1360px`, `gap: .5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`
- **Corner Radii**: `50%`, `999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Sora`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 80px`, `line-height: 76px`, `font-weight: 500`, `letter-spacing: -1.6px`); rule `,.h1` (`font-size: 2.25rem`, `line-height: 1.1`, `letter-spacing: -.025em`, `font-weight: 700`)
- **H2 Section Rule**: live computed `h2` (`font-size: 80px`, `line-height: 76px`, `font-weight: 500`, `letter-spacing: -1.6px`); rule `,.h2` (`font-size: 1.875rem`, `line-height: 1.1`, `letter-spacing: -.025em`, `font-weight: 700`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--tra-body-h: 16rem`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-3d-discovery-fr` (`3D Discovery · Exploring New Dimensions`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `www-3d-discovery-fr`)**:
   - DOM & Selectors: Landmark `<header class="header">` (`1440x66px`) hosting `3D Discovery · Exploring New Dimensi` navigation (`Solutions · Experiences · Features · Blog`), DOM attributes (`data-theme="light"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `after { box-sizing:border-box }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `www-3d-discovery-fr`)` (`www-3d-discovery-fr`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)` with `cubic-bezier(.8,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.65,0,.35,1)` transitions and links `Solutions · Experiences · Features · Blog`.
2. **Hero Stage & Focal Lead (<section.sg-section> — `TURN YOUR SPACES INTO IMMERSIVE EX`)**:
   - DOM & Selectors: Landmark `<section class="sg-section">` presenting display lead `TURN YOUR SPACES INTO IMMERSIVE EXPERIENCES` and copy excerpt *"3D DISCOVERY · ©2026"* over `#ebebeb` canvas and `#1a1a1a` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#ebebeb` background with `#1a1a1a` headline `TURN YOUR SPACES INTO IMMERSIVE EXPERIENCES`.
3. **Primary Showcase & Content Grid (<section.sg-section--seq> — `Turn your spaces into immersive ex`)**:
   - DOM & Selectors: Landmark `<section class="sg-section sg-section--seq">` rendering section `Turn your spaces into immersive experiences` with copy *"3D Discovery · ©2026"*, asset references (`83afe278b6a6bb3c-s.p.0q-301v4kxxn...`, `c41ca59f1c34ba31-s.p.0xxb547n1hn7...`, `0ghcmdv7avfm..css`, `04vxxuqck~drg.css`), and grid rule `html:focus-within { scroll-behavior:smooth }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.sg-section--seq> — `Turn your spaces into immersive ex`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1360px`, `gap: .5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.sg-solutions> — `Choose your field`)**:
   - DOM & Selectors: Landmark `<section class="sg-section sg-solutions">` framing `Choose your field` and `Seeing is understanding` (*"Exploring new dimensions"*) with `#e2e2e2` surface cards, `#f59e0b` accents, and `body { min-height:100vh;line-height:1.5 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.sg-solutions> — `Choose your field`)` uses `50%`, `999px` radii, `#f59e0b` highlights, and assets (83afe278b6a6bb3c-s.p.0q-301v4kxxn..., c41ca59f1c34ba31-s.p.0xxb547n1hn7..., 0ghcmdv7avfm..css).
5. **Colophon & Global Directory Footer (<footer.sg-footer> — `https://www.3d-discovery.fr/`)**:
   - DOM & Selectors: Landmark `<footer class="sg-footer">` anchoring `3D Discovery · Exploring New Dim` footer links (`Solutions · Experiences · Features · Blog`), copy *"A single web experience for 3D exploration, content and inte"*, and `#d4d4d4` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.sg-footer> — `https://www.3d-discovery.fr/`)` aligns to `1360px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `1rem` lateral canvas padding with `.5rem` grid gap and attributes (data-theme="light", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"3D DISCOVERY · ©2026"*
- Copy Excerpt 2: *"3D Discovery · ©2026"*
- Copy Excerpt 3: *"Exploring new dimensions"*
- Copy Excerpt 4: *"A single web experience for 3D exploration, content and interactions, designed to..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.8,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.65,0,.35,1)`
- **Extracted Stylesheet Rules (`www-3d-discovery-fr`)**:
- `after { box-sizing:border-box }`
- `html:focus-within { scroll-behavior:smooth }`
- `body { min-height:100vh;line-height:1.5 }`
- `svg { max-width:100%;display:block }`
- `select { font:inherit;color:inherit }`
- **Per-Selector Transition Rules**:
- **Selector `:after`**: `transition: .01ms!important` extracted from `www-3d-discovery-fr` stylesheet.
- **Selector `body`**: `transition: background-color var(--transition-theme),color var(--transitio...` extracted from `www-3d-discovery-fr` stylesheet.
- **Selector `::-webkit-scrollbar-track`**: `transition: background var(--transition-theme)` extracted from `www-3d-discovery-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.8,0,1,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.sg-section--seq>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native+wheel` vertical progression up to `11299px` across 8 distinct viewport chapters using Lenis, WebGL/Canvas.
- **Vertical Chapter Sequence**: TURN YOUR SPACES INTO IMMER... (0%) -> Section @ 8% (8%) -> Section @ 25% (25%) -> Section @ 33% (33%) -> Section @ 41% (41%) -> Section @ 50% (50%) -> Section @ 58% (58%) -> CHOOSE YOUR FIELD (66%).
- **Multi-Page Routes**: Scaffold internal routes `/en/solutions` (listing, SPA), `/en/about` (about, direct), `/en/features` (listing, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-3d-discovery-fr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | TURN YOUR SPACES INTO IMMERSIVE EXPERIENCES | `2` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `8%` | Section @ 8% | `3` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2563px` | `25%` | Section @ 25% | `3` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `3426px` | `33%` | Section @ 33% | `3` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `4289px` | `41%` | Section @ 41% | `3` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `5152px` | `50%` | Section @ 50% | `3` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `6015px` | `58%` | Section @ 58% | `3` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `6878px` | `66%` | CHOOSE YOUR FIELD | `3` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | TURN YOUR SPACES INTO IMMERSIVE EXPERIENCES | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `5968px` | `50%` | Section @ 57% | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `10423px` | `100%` | Footer | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://www.3d-discovery.fr/en/solutions` | CHOOSE YOUR FIELD | `2809px` | `SPA` (`4007ms`) | [subpage-01-en-solutions.webp](assets/subpage-01-en-solutions.webp) |
| `2` | `about` | `https://www.3d-discovery.fr/en/about` | About · 3D Discovery | `2417px` | `direct` (`963ms`) | [subpage-02-en-about.webp](assets/subpage-02-en-about.webp) |
| `3` | `listing` | `https://www.3d-discovery.fr/en/features` | EVERYTHING TO SHOW IT ALL | `9728px` | `direct` (`585ms`) | [subpage-03-en-features.webp](assets/subpage-03-en-features.webp) |

