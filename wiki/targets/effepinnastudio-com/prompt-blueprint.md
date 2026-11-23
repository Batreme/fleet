---
title: "UI Prompt Blueprint: effepinnastudio-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "effepinnastudio-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff0000`)"
---

# UI Design System & Master Generation Blueprint: effepinnastudio-com

> **Fabio Pinna — Art Director e Graphic Designer · Effepinna Studio** (https://effepinnastudio.com/) — Direzione artistica, progettazione grafica e produzione di immagini, video e animazioni per agenzie e brand. Fabio Pinna, freelance a Gra...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Fabio Pinna — Art Director e Graphic Designer · Effepinna Studio** (`https://effepinnastudio.com/`). Direzione artistica, progettazione grafica e produzione di immagini, video e animazioni per agenzie e brand. Fabio Pinna, freelance a Gra...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff0000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0000ee` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Instrument Sans` for display copy (`Fabio Pinna - Art Direction, Multime`) with `Instrument Sans` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 27px 40.32px`, padding `36.2264px`) with `cubic-bezier(.22,.78,.24,1)` easing and GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `36.2264px` lateral canvas padding with `27px 40.32px` grid gap.
- **Border Radius Scale**: `50%`, `999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 27px 40.32px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `36.2264px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 760px)`, `@media (max-width: 760px), (hover: none), (pointer: coarse), (pr...`, `@media (max-width: 1100px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f2ef` | `var(--paper)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0000` | `.controls button { background: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#ee2c3d` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ff0000` | `.hero-doodle { border: #ff0000 }` |
| **Variable Token (`--red`)** | `#ef233c` | `var(--red)` in `:root` |
| **Variable Token (`--ink`)** | `#0a0a0a` | `var(--ink)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--red` | `#ef233c` | Color / Atmospheric Token |
| `--paper` | `#f3f2ef` | Canvas / Surface Token |
| `--ink` | `#0a0a0a` | Typography Ink Token |
| `--font-text` | `"Instrument Sans", Arial, Helvetica, sans-serif` | Typography Ink Token |
| `--weight-text` | `400` | Typography Ink Token |
| `--weight-label` | `500` | Design System Custom Token |
| `--weight-heading` | `700` | Typography Ink Token |
| `--type-display` | `6rem` | Typography / Scale Token |
| `--leading-display` | `6.25rem` | Typography / Scale Token |
| `--type-page` | `4rem` | Typography / Scale Token |
| `--leading-page` | `4.25rem` | Typography / Scale Token |
| `--type-section` | `3rem` | Typography / Scale Token |
| `--leading-section` | `3.25rem` | Typography / Scale Token |
| `--type-block` | `1.75rem` | Typography / Scale Token |
| `--leading-block` | `2.125rem` | Typography / Scale Token |
| `--type-intro` | `1.5rem` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Instrument Sans`.
- **Primary Body Stack**: `Instrument Sans`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 36px`, `line-height: 28px`, `font-weight: 700`); CSS variables `--type-display: 6rem`, `--leading-display: 6.25rem`; rule `h1` (`font-size: 2rem`, `line-height: 2.25rem`, `font-weight: 500`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 50.4px`, `line-height: 52.92px`, `font-weight: 700`); rule `h2` (`font-size: var(--type-section)`, `line-height: var(--leading-section)`, `font-weight: var(--weight-...`).
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 28px`, `font-weight: 400`); CSS variables `--type-body: 1.125rem`, `--leading-body: 1.75rem`, `--space-paragraph: 1.5rem`; rule `p` (`font-size: var(--type-block)`, `line-height: var(--leading-block)`, `font-weight: var(--weight-...`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 28px`, `font-weight: 400`); CSS variables `--weight-label: 500`, `--type-meta: .875rem`, `--leading-meta: 1.25rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,.78,.24,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.menu-toggle span`**: `transition: transform .28s ease, background-color .2s ease` extracted from `effepinnastudio-com` stylesheet.
- **Selector `.ragdoll-cursor-hint`**: `transition: opacity 155ms ease, visibility 0s linear 155ms` extracted from `effepinnastudio-com` stylesheet.
- **Selector `.ragdoll-cursor-hint.is-visible`**: `transition: opacity 200ms ease, visibility 0s` extracted from `effepinnastudio-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,.78,.24,1)`)**: Governs interactive state transitions across `<header.hero>` and `<section.work>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Fabio Pinna — Art Director e Graphic Desig │
│ ====================================================================== │
│ [ <header.hero> (1440x900px)          | Home ↗ · Work ↗ · Agenzie e  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.manifesto> (w=1440px)                         | │
│ | H1: Fabio Pinna - Art Direction, Multimedia Graphic D...           | │
│ | Substrate: #ffffff | Ink: #0000ee | Accent: #ff0000                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.work>) max-w: 1440px                       | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Selezione Lavori             |  | Fastweb Tu sei Futuro        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.work-row>) — Dose e Dadda Summer M         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | https://effepinnastudio.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 27px 40.)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.hero>           ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.manifesto>) — 390px Vertical Lead             | │
│ | H1: Fabio Pinna - Art Direction, Multimedia Graphic D...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.work>) — 1-Col Stack                      | │
│ | [ Item 1: Selezione Lavori                                       ] | │
│ | [ Item 2: Fastweb Tu sei Futuro                                  ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.work-row>) — 1-Col (Dose e Dadda Summe)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.hero> — `effepinnastudio-com`)**:
   - Landmark `<header class="hero">` (`1440x900px`) hosting `Fabio Pinna — Art Director e Graphic` navigation (`Home ↗ · Work ↗ · Agenzie e brand ↗ · Chi sono ↗ · Contatti ↗`), DOM attributes (`data-work-preview-loading="true"`, `data-loading-theme="red"`, `data-loading-state="ready"`, `data-font-status="instrument-sans"`), and stylesheet rule `root { color-scheme: light;--red: ef233c;--paper: f3f2ef;--ink: 0a0a0a; }`.
2. **Hero Stage & Focal Lead (<section.manifesto> — `Fabio Pinna - Art Direction, Multi`)**:
   - Landmark `<section class="manifesto editorial-grid">` presenting display lead `Fabio Pinna - Art Direction, Multimedia Graphic D...` and copy excerpt *"Mi occupo di direzione artistica e graphic design multimediale. M"* over `#ffffff` canvas and `#0000ee` ink.
3. **Primary Showcase & Content Grid (<section.work> — `Selezione Lavori`)**:
   - Landmark `<section class="work">` rendering section `Selezione Lavori` with copy *"Mi occupo di direzione artistica e graphic design multimediale."*, asset references (`motion-policy-20261012.js`, `favicon-192.png`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `body { touch-action: manipulation;touch-action: pan-x pan-y; }`.
4. **Interactive Detail & Feature Matrix (<article.work-row> — `Fastweb Tu sei Futuro`)**:
   - Landmark `<article class="work-row">` framing `Fastweb Tu sei Futuro` and `Dose e Dadda Summer Merch` (*"Sviluppo il concept, progetto il linguaggio visivo e lavoro alla "*) with `#f3f2ef` surface cards, `#ff0000` accents, and `focus-visible { outline: 2px solid currentColor;outline-offset: 4px; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://effepinnastudio.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Fabio Pinna — Art Director e Gra` footer links (`Home ↗ · Work ↗ · Agenzie e brand ↗ · Chi sono ↗ · Contatti ↗`), copy *"Art director e graphic designer multimediale, tra Milano e G"*, and `#ff0000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: effepinnastudio-com (Fabio Pinna — Art Director e Graphic Designer · Effepinna Studio)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `effepinnastudio-com` (**Fabio Pinna — Art Director e Graphic Designer · Effepinna Studio** — `https://effepinnastudio.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff0000`).
- **Identity & Domain Context**: Direzione artistica, progettazione grafica e produzione di immagini, video e animazioni per agenzie e brand. Fabio Pinna, freelance a Gra...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#0000ee`, **Accent / Highlight**: `#ff0000`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0000ee` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Instrument Sans` for display copy (`Fabio Pinna - Art Direction, Multime`) with `Instrument Sans` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 27px 40.32px`, padding `36.2264px`) with `cubic-bezier(.22,.78,.24,1)` easing and GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `effepinnastudio-com` in your global stylesheet:

:root {
  /* Fabio Pinna — Art Director e Graphic Designer · Effepinna Studio (effepinnastudio-com) — Live-Grounded CSS Variables */
  --red: #ef233c; /* Color / Atmospheric Token (effepinnastudio-com) */
  --paper: #f3f2ef; /* Canvas / Surface Token (effepinnastudio-com) */
  --ink: #0a0a0a; /* Typography Ink Token (effepinnastudio-com) */
  --font-text: "Instrument Sans", Arial, Helvetica, sans-serif; /* Typography Ink Token (effepinnastudio-com) */
  --weight-text: 400; /* Typography Ink Token (effepinnastudio-com) */
  --weight-label: 500; /* Design System Custom Token (effepinnastudio-com) */
  --weight-heading: 700; /* Typography Ink Token (effepinnastudio-com) */
  --type-display: 6rem; /* Typography / Scale Token (effepinnastudio-com) */
  --leading-display: 6.25rem; /* Typography / Scale Token (effepinnastudio-com) */
  --type-page: 4rem; /* Typography / Scale Token (effepinnastudio-com) */
  --leading-page: 4.25rem; /* Typography / Scale Token (effepinnastudio-com) */
  --type-section: 3rem; /* Typography / Scale Token (effepinnastudio-com) */
  --leading-section: 3.25rem; /* Typography / Scale Token (effepinnastudio-com) */
  --type-block: 1.75rem; /* Typography / Scale Token (effepinnastudio-com) */
  --leading-block: 2.125rem; /* Typography / Scale Token (effepinnastudio-com) */
  --type-intro: 1.5rem; /* Typography / Scale Token (effepinnastudio-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#0000ee` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f3f2ef` — grounded in `var(--paper)` in `:root`
- **Interactive Accent / Highlight**: `#ff0000` — grounded in `.controls button { background: red }` (`#ff0000`)
- **Secondary / Muted Copy**: `#ee2c3d` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#ff0000` — grounded in `.hero-doodle { border: #ff0000 }`
- **Variable Token (`--red`)**: `#ef233c` — grounded in `var(--red)` in `:root`
- **Variable Token (`--ink`)**: `#0a0a0a` — grounded in `var(--ink)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `36.2264px` lateral canvas padding with `27px 40.32px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 27px 40.32px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `36.2264px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 760px)`, `@media (max-width: 760px), (hover: none), (pointer: coarse), (pr...`, `@media (max-width: 1100px)`
- **Corner Radii**: `50%`, `999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `Instrument Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 36px`, `line-height: 28px`, `font-weight: 700`); CSS variables `--type-display: 6rem`, `--leading-display: 6.25rem`; rule `h1` (`font-size: 2rem`, `line-height: 2.25rem`, `font-weight: 500`)
- **H2 Section Rule**: live computed `h2` (`font-size: 50.4px`, `line-height: 52.92px`, `font-weight: 700`); rule `h2` (`font-size: var(--type-section)`, `line-height: var(--leading-section)`, `font-weight: var(--weight-...`)
- **Body Copy Rule**: live computed `body` (`font-size: 18px`, `line-height: 28px`, `font-weight: 400`); CSS variables `--type-body: 1.125rem`, `--leading-body: 1.75rem`, `--space-paragraph: 1.5rem`; rule `p` (`font-size: var(--type-block)`, `line-height: var(--leading-block)`, `font-weight: var(--weight-...`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 18px`, `line-height: 28px`, `font-weight: 400`); CSS variables `--weight-label: 500`, `--type-meta: .875rem`, `--leading-meta: 1.25rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `effepinnastudio-com` (`Fabio Pinna — Art Director e Graphic Designer · Effepinna Studio`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.hero> — `effepinnastudio-com`)**:
   - DOM & Selectors: Landmark `<header class="hero">` (`1440x900px`) hosting `Fabio Pinna — Art Director e Graphic` navigation (`Home ↗ · Work ↗ · Agenzie e brand ↗ · Chi sono ↗ · Contatti ↗`), DOM attributes (`data-work-preview-loading="true"`, `data-loading-theme="red"`, `data-loading-state="ready"`, `data-font-status="instrument-sans"`), and stylesheet rule `root { color-scheme: light;--red: ef233c;--paper: f3f2ef;--ink: 0a0a0a; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.hero> — `effepinnastudio-com`)` (`effepinnastudio-com`) adapts across `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 760px)`, `@media (max-width: 760px), (hover: none), (pointer: coarse), (pr...`, `@media (max-width: 1100px)` with `cubic-bezier(.22,.78,.24,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.16,1,.3,1)` transitions and links `Home ↗ · Work ↗ · Agenzie e brand ↗ · Chi sono ↗ · Contatti ↗`.
2. **Hero Stage & Focal Lead (<section.manifesto> — `Fabio Pinna - Art Direction, Multi`)**:
   - DOM & Selectors: Landmark `<section class="manifesto editorial-grid">` presenting display lead `Fabio Pinna - Art Direction, Multimedia Graphic D...` and copy excerpt *"Mi occupo di direzione artistica e graphic design multimediale. M"* over `#ffffff` canvas and `#0000ee` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#0000ee` headline `Fabio Pinna - Art Direction, Multimedia Graphic D...`.
3. **Primary Showcase & Content Grid (<section.work> — `Selezione Lavori`)**:
   - DOM & Selectors: Landmark `<section class="work">` rendering section `Selezione Lavori` with copy *"Mi occupo di direzione artistica e graphic design multimediale."*, asset references (`motion-policy-20261012.js`, `favicon-192.png`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `body { touch-action: manipulation;touch-action: pan-x pan-y; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.work> — `Selezione Lavori`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 27px 40.32px`) on desktop and Single-column vertical stack at `390px` viewport width with `36.2264px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.work-row> — `Fastweb Tu sei Futuro`)**:
   - DOM & Selectors: Landmark `<article class="work-row">` framing `Fastweb Tu sei Futuro` and `Dose e Dadda Summer Merch` (*"Sviluppo il concept, progetto il linguaggio visivo e lavoro alla "*) with `#f3f2ef` surface cards, `#ff0000` accents, and `focus-visible { outline: 2px solid currentColor;outline-offset: 4px; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.work-row> — `Fastweb Tu sei Futuro`)` uses `50%`, `999px` radii, `#ff0000` highlights, and assets (motion-policy-20261012.js, favicon-192.png, favicon.ico).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://effepinnastudio.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `Fabio Pinna — Art Director e Gra` footer links (`Home ↗ · Work ↗ · Agenzie e brand ↗ · Chi sono ↗ · Contatti ↗`), copy *"Art director e graphic designer multimediale, tra Milano e G"*, and `#ff0000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://effepinnastudio.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `36.2264px` lateral canvas padding with `27px 40.32px` grid gap and attributes (data-work-preview-loading="true", data-loading-theme="red", data-loading-state="ready").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Mi occupo di direzione artistica e graphic design multimediale. Mi occupo di direz..."*
- Copy Excerpt 2: *"Mi occupo di direzione artistica e graphic design multimediale."*
- Copy Excerpt 3: *"Sviluppo il concept, progetto il linguaggio visivo e lavoro alla produzione: ident..."*
- Copy Excerpt 4: *"Art director e graphic designer multimediale, tra Milano e Gran Canaria."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,.78,.24,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`effepinnastudio-com`)**:
- `root { color-scheme: light;--red: ef233c;--paper: f3f2ef;--ink: 0a0a0a; }`
- `body { touch-action: manipulation;touch-action: pan-x pan-y; }`
- `focus-visible { outline: 2px solid currentColor;outline-offset: 4px; }`
- `body.is-loader-active { overflow: hidden; }`
- `body.is-menu-open { overflow: hidden; }`
- **Per-Selector Transition Rules**:
- **Selector `.menu-toggle span`**: `transition: transform .28s ease, background-color .2s ease` extracted from `effepinnastudio-com` stylesheet.
- **Selector `.ragdoll-cursor-hint`**: `transition: opacity 155ms ease, visibility 0s linear 155ms` extracted from `effepinnastudio-com` stylesheet.
- **Selector `.ragdoll-cursor-hint.is-visible`**: `transition: opacity 200ms ease, visibility 0s` extracted from `effepinnastudio-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,.78,.24,1)`)**: Governs interactive state transitions across `<header.hero>` and `<section.work>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `effepinnastudio-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
