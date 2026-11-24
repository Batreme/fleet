---
title: "UI Prompt Blueprint: effepinnastudio-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "effepinnastudio-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 3
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff0000`)"
---

# UI Design System & Master Generation Blueprint: effepinnastudio-com

> **Fabio Pinna — Art Director e Graphic Designer · Effepinna Studio** (https://effepinnastudio.com/) — Direzione artistica, progettazione grafica e produzione di immagini, video e animazioni per agenzie e brand. Fabio Pinna, freelance a Gra...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Fabio Pinna — Art Director e Graphic Designer · Effepinna Studio** (`https://effepinnastudio.com/`). Direzione artistica, progettazione grafica e produzione di immagini, video e animazioni per agenzie e brand. Fabio Pinna, freelance a Gra...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff0000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0000ee` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Uses `Instrument Sans` across display (`Fabio Pinna - Art Direction, Multime`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 27px 40.32px`, padding `36.2264px`) with `cubic-bezier(.22,.78,.24,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=6491px` / doc `7391px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
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
| **Structural Hairline Border** | `#f8a6ae` | `var(--calmilene-line)` in `:root` (`rgba(239, 43, 63, 0.42)`) |
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
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `7391px`, deepest scrollY reached `6491px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `GSAP/ScrollTrigger`, `WebGL/Canvas`.
- **Nav / Drawer Probe (`Apri menu`)**: Triggered visual change (pixel diff `130.548`, captured in `assets/state-nav.webp`); revealed links: Home ↗, Work ↗, Agenzie e brand ↗, Chi sono ↗, Contatti ↗, Articoli ↗.
- **Route Transition Architecture**: First internal navigation (`/blog/vallelata.html`) measured as `direct` in `3069ms`.

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
   - Landmark `<footer class="site-footer">` anchoring `Fabio Pinna — Art Director e Gra` footer links (`Home ↗ · Work ↗ · Agenzie e brand ↗ · Chi sono ↗ · Contatti ↗`), copy *"Art director e graphic designer multimediale, tra Milano e G"*, and `#f8a6ae` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `#manifesto-title` · sticky/fixed elements: `4`
- **Step 02** (`y=850px`, `13%`): Active landmark `#manifesto-title` · sticky/fixed elements: `4`
- **Step 03** (`y=1700px`, `26%`): Active landmark `Fastweb Tu sei Futuro` · sticky/fixed elements: `4`
- **Step 04** (`y=2550px`, `39%`): Active landmark `Dose e Dadda Summer Merch` · sticky/fixed elements: `4`
- **Step 05** (`y=4250px`, `65%`): Active landmark `Per le agenzie` · sticky/fixed elements: `4`
- **Step 06** (`y=5100px`, `79%`): Active landmark `Altri articoli Altri articoli` · sticky/fixed elements: `4`
- **Step 07** (`y=5950px`, `92%`): Active landmark `Footer` · sticky/fixed elements: `4`
- **Step 08** (`y=6491px`, `100%`): Active landmark `Footer` · sticky/fixed elements: `4`

### Multi-Page Internal Route Map
- **Detail Route (`/blog/vallelata.html`)**: `https://effepinnastudio.com/blog/vallelata.html` — H1: `Vallelata: campagne display, visual e video AI.`, scrollHeight `10853px`, transition `direct` (`3069ms`)
- **Detail Route (`/blog/pennicanza.html`)**: `https://effepinnastudio.com/blog/pennicanza.html` — H1: `La Pennicanza: Natale in miniatura.`, scrollHeight `6608px`, transition `direct` (`1254ms`)
- **Detail Route (`/blog/mega-effe-x.html`)**: `https://effepinnastudio.com/blog/mega-effe-x.html` — H1: `Mega Effe X`, scrollHeight `7594px`, transition `direct` (`2621ms`)

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
  - **Grounded Typographic Hierarchy**: Uses `Instrument Sans` across display (`Fabio Pinna - Art Direction, Multime`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 27px 40.32px`, padding `36.2264px`) with `cubic-bezier(.22,.78,.24,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

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
- **Structural Hairline Border**: `#f8a6ae` — grounded in `var(--calmilene-line)` in `:root` (`rgba(239, 43, 63, 0.42)`)
- **Variable Token (`--red`)**: `#ef233c` — grounded in `var(--red)` in `:root`
- **Variable Token (`--ink`)**: `#0a0a0a` — grounded in `var(--ink)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
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
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#ffffff` background with `#0000ee` headline `Fabio Pinna - Art Direction, Multimedia Graphic D...`.
3. **Primary Showcase & Content Grid (<section.work> — `Selezione Lavori`)**:
   - DOM & Selectors: Landmark `<section class="work">` rendering section `Selezione Lavori` with copy *"Mi occupo di direzione artistica e graphic design multimediale."*, asset references (`motion-policy-20261012.js`, `favicon-192.png`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `body { touch-action: manipulation;touch-action: pan-x pan-y; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.work> — `Selezione Lavori`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 27px 40.32px`) on desktop and Single-column vertical stack at `390px` viewport width with `36.2264px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.work-row> — `Fastweb Tu sei Futuro`)**:
   - DOM & Selectors: Landmark `<article class="work-row">` framing `Fastweb Tu sei Futuro` and `Dose e Dadda Summer Merch` (*"Sviluppo il concept, progetto il linguaggio visivo e lavoro alla "*) with `#f3f2ef` surface cards, `#ff0000` accents, and `focus-visible { outline: 2px solid currentColor;outline-offset: 4px; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.work-row> — `Fastweb Tu sei Futuro`)` uses `50%`, `999px` radii, `#ff0000` highlights, and assets (motion-policy-20261012.js, favicon-192.png, favicon.ico).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://effepinnastudio.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `Fabio Pinna — Art Director e Gra` footer links (`Home ↗ · Work ↗ · Agenzie e brand ↗ · Chi sono ↗ · Contatti ↗`), copy *"Art director e graphic designer multimediale, tra Milano e G"*, and `#f8a6ae` structural dividers.
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
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `7391px` across 8 distinct viewport chapters using GSAP/ScrollTrigger, WebGL/Canvas.
- **Vertical Chapter Sequence**: #manifesto-title (0%) -> #manifesto-title (13%) -> Fastweb Tu sei Futuro (26%) -> Dose e Dadda Summer Merch (39%) -> Per le agenzie (65%) -> Altri articoli Altri articoli (79%) -> Footer (92%) -> Footer (100%).
- **Navigation Drawer / Menu State**: Replicate interactive menu toggle (`Apri menu`) with Escape-to-close keyboard handling.
- **Multi-Page Routes**: Scaffold internal routes `/blog/vallelata.html` (detail, direct), `/blog/pennicanza.html` (detail, direct), `/blog/mega-effe-x.html` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `effepinnastudio-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | #manifesto-title | `4` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `13%` | #manifesto-title | `4` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `1700px` | `26%` | Fastweb Tu sei Futuro | `4` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `2550px` | `39%` | Dose e Dadda Summer Merch | `4` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `4250px` | `65%` | Per le agenzie | `4` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `5100px` | `79%` | Altri articoli Altri articoli | `4` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `5950px` | `92%` | Footer | `4` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `6491px` | `100%` | Footer | `4` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | #manifesto-title | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `3396px` | `50%` | Servizi Servizi | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `6792px` | `100%` | Footer | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `nav_menu` | Nav/Menu opened (`Apri menu`, diff `130.548`) | [state-nav.webp](assets/state-nav.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `detail` | `https://effepinnastudio.com/blog/vallelata.html` | Vallelata: campagne display, visual e... | `10853px` | `direct` (`3069ms`) | [subpage-01-blog-vallelata-html.webp](assets/subpage-01-blog-vallelata-html.webp) |
| `2` | `detail` | `https://effepinnastudio.com/blog/pennicanza.html` | La Pennicanza: Natale in miniatura. | `6608px` | `direct` (`1254ms`) | [subpage-02-blog-pennicanza-html.webp](assets/subpage-02-blog-pennicanza-html.webp) |
| `3` | `detail` | `https://effepinnastudio.com/blog/mega-effe-x.html` | Mega Effe X | `7594px` | `direct` (`2621ms`) | [subpage-03-blog-mega-effe-x-html.webp](assets/subpage-03-blog-mega-effe-x-html.webp) |

