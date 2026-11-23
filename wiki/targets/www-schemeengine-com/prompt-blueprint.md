---
title: "UI Prompt Blueprint: www-schemeengine-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-schemeengine-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#0082f3`)"
---

# UI Design System & Master Generation Blueprint: www-schemeengine-com

> **Home - Scheme Engine** (https://www.schemeengine.com/) — Scheme Engine is a BIPOC-owned production company and TV/Film studio founded to provoke and reimagine the status quo.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Home - Scheme Engine** (`https://www.schemeengine.com/`). Scheme Engine is a BIPOC-owned production company and TV/Film studio founded to provoke and reimagine the status quo.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#0082f3`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#0082f3` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Neuepower Ultra` for display copy (`We create from the culture we live.`) with `neue-haas-grotesk-display` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `80vw` container bounds (`gap: 32px`, padding `9px`) with `cubic-bezier(0.2,0.6,0.35,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `80vw` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `32px` grid gap.
- **Border Radius Scale**: `4px`, `3px`, `100%`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80vw`, `gap: 32px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#333333` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#ebebeb` | `var(--text-color)` in `:root` |
| **Structural Hairline Border** | `#3898ec` | `.w-select:focus { border-color: #3898ec }` |
| **Variable Token (`--purple`)** | `#1d0524` | `var(--purple)` in `:root` |
| **Variable Token (`--white`)** | `#fef9ef` | `var(--white)` in `:root` |
| **Variable Token (`--brown`)** | `#b47054` | `var(--brown)` in `:root` |
| **Variable Token (`--main-light`)** | `#d18221` | `var(--main-light)` in `:root` |
| **Variable Token (`--background-color`)** | `#140d16` | `var(--background-color)` in `:root` |
| **Variable Token (`--title-background-color`)** | `#111111` | `var(--title-background-color)` in `:root` |
| **Variable Token (`--widget-color`)** | `#424242` | `var(--widget-color)` in `:root` |
| **Variable Token (`--hover-color`)** | `#4f4f4f` | `var(--hover-color)` in `:root` |
| **Variable Token (`--focus-color`)** | `#595959` | `var(--focus-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--purple` | `#1d0524` | Color / Atmospheric Token |
| `--white` | `#fef9ef` | Canvas / Surface Token |
| `--black` | `#000` | Canvas / Surface Token |
| `--brown` | `#b47054` | Color / Atmospheric Token |
| `--main-dark` | `#000000` | Canvas / Surface Token |
| `--main-light` | `#D18221` | Canvas / Surface Token |
| `--visual-hidden` | `0` | Design System Custom Token |
| `--main-space` | `10vw` | Layout / Spatial Grid Token |
| `--background-color` | `#140D16` | Canvas / Surface Token |
| `--book-width` | `35vmin` | Layout / Spatial Grid Token |
| `--text-color` | `#ebebeb` | Typography Ink Token |
| `--title-background-color` | `#111111` | Canvas / Surface Token |
| `--title-text-color` | `#ebebeb` | Typography Ink Token |
| `--widget-color` | `#424242` | Brand / Palette Token |
| `--hover-color` | `#4f4f4f` | Brand / Palette Token |
| `--focus-color` | `#595959` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Neuepower Ultra`.
- **Primary Body Stack**: `neue-haas-grotesk-display`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 64px`, `line-height: 57.6px`, `font-weight: 400`); rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 24px`, `line-height: 30px`, `font-weight: 700`); rule `h2` (`font-size: 32px`, `line-height: 36px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 500`); rule `body` (`font-size: 14px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 500`); CSS variables `--font-family-mono: Menlo, Monaco, Consolas, "Droid Sans Mono", monospace`; rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.2,0.6,0.35,1)`, `cubic-bezier(0.65,0,0.35,1)`, `cubic-bezier(0.25,0.46,0.45,0.94)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-schemeengine-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-schemeengine-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-schemeengine-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.2,0.6,0.35,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.section:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Home - Scheme Engine                       │
│ ====================================================================== │
│ [ <header.header> (1440x104px)        | D i r e c t o r s · W o r k  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.section> (w=1440px)                           | │
│ | H1: We create from the culture we live.                            | │
│ | Substrate: #000000 | Ink: #ffffff | Accent: #0082f3                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section:nth(2)>) max-w: 80vw               | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Scheme Engine is a culture-f |  | Our award-winning directors  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.section:nth(3)>) — Impactful, resonant s   | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wf-active>  ) | https://www.schemeengine.com/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 32px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.header>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.section>) — 390px Vertical Lead               | │
│ | H1: We create from the culture we live.                            | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.section:nth(2) — 1-Col Stack              | │
│ | [ Item 1: Scheme Engine is a culture-first production comp       ] | │
│ | [ Item 2: Our award-winning directors and creatives work a       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.section:nth(3)>) — 1-Col (Impactful, resonan) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wf-active>  ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `www-schemeengine-com`)**:
   - Landmark `<header class="header">` (`1440x104px`) hosting `Home - Scheme Engine` navigation (`D i r e c t o r s · W o r k · F i l m & t v · C o n t a c t`), DOM attributes (`data-wf-domain="www.schemeengine.com"`, `data-wf-page="6856ec97d986105f5589bbe0"`, `data-wf-site="6856ec97d986105f5589bbd7"`, `data-word="Directors"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.section> — `We create from the culture we live`)**:
   - Landmark `<section class="section">` presenting display lead `We create from the culture we live.` and copy excerpt *"Scheme Engine is a culture-first production company championing t"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.section:nth(2)> — `Scheme Engine is a culture-first p`)**:
   - Landmark `<section class="section">` rendering section `Scheme Engine is a culture-first production comp` with copy *"Our award-winning directors and creatives work across formats, al"*, asset references (`cdn.prod.website-files.com`, `schemeengine.webflow.shared.3fbb9...`, `soy0bmb.js`, `68b845cb16daf25e488bd7a5_scheme-e...`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section:nth(3)> — `Our award-winning directors and cr`)**:
   - Landmark `<section class="section">` framing `Our award-winning directors and creatives work a` and `Impactful, resonant storytelling is rooted in li` (*"Impactful, resonant storytelling is rooted in lived experience. W"*) with `#333333` surface cards, `#0082f3` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.wf-active> — `https://www.schemeengine.com/`)**:
   - Landmark `<footer class="wf-active">` anchoring `Home - Scheme Engine` footer links (`D i r e c t o r s · W o r k · F i l m & t v · C o n t a c t`), copy *"The future does not look like the past. Neither do we."*, and `#3898ec` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-schemeengine-com (Home - Scheme Engine)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-schemeengine-com` (**Home - Scheme Engine** — `https://www.schemeengine.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#0082f3`).
- **Identity & Domain Context**: Scheme Engine is a BIPOC-owned production company and TV/Film studio founded to provoke and reimagine the status quo.
- **Primary Substrate**: `#000000` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#0082f3`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#0082f3` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Neuepower Ultra` for display copy (`We create from the culture we live.`) with `neue-haas-grotesk-display` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `80vw` container bounds (`gap: 32px`, padding `9px`) with `cubic-bezier(0.2,0.6,0.35,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-schemeengine-com` in your global stylesheet:

:root {
  /* Home - Scheme Engine (www-schemeengine-com) — Live-Grounded CSS Variables */
  --purple: #1d0524; /* Color / Atmospheric Token (www-schemeengine-com) */
  --white: #fef9ef; /* Canvas / Surface Token (www-schemeengine-com) */
  --black: #000; /* Canvas / Surface Token (www-schemeengine-com) */
  --brown: #b47054; /* Color / Atmospheric Token (www-schemeengine-com) */
  --main-dark: #000000; /* Canvas / Surface Token (www-schemeengine-com) */
  --main-light: #D18221; /* Canvas / Surface Token (www-schemeengine-com) */
  --visual-hidden: 0; /* Design System Custom Token (www-schemeengine-com) */
  --main-space: 10vw; /* Layout / Spatial Grid Token (www-schemeengine-com) */
  --background-color: #140D16; /* Canvas / Surface Token (www-schemeengine-com) */
  --book-width: 35vmin; /* Layout / Spatial Grid Token (www-schemeengine-com) */
  --text-color: #ebebeb; /* Typography Ink Token (www-schemeengine-com) */
  --title-background-color: #111111; /* Canvas / Surface Token (www-schemeengine-com) */
  --title-text-color: #ebebeb; /* Typography Ink Token (www-schemeengine-com) */
  --widget-color: #424242; /* Brand / Palette Token (www-schemeengine-com) */
  --hover-color: #4f4f4f; /* Brand / Palette Token (www-schemeengine-com) */
  --focus-color: #595959; /* Brand / Palette Token (www-schemeengine-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#333333` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#0082f3` — grounded in `.w-dropdown-link.w--current { color: #0082f3 }`
- **Secondary / Muted Copy**: `#ebebeb` — grounded in `var(--text-color)` in `:root`
- **Structural Hairline Border**: `#3898ec` — grounded in `.w-select:focus { border-color: #3898ec }`
- **Variable Token (`--purple`)**: `#1d0524` — grounded in `var(--purple)` in `:root`
- **Variable Token (`--white`)**: `#fef9ef` — grounded in `var(--white)` in `:root`
- **Variable Token (`--brown`)**: `#b47054` — grounded in `var(--brown)` in `:root`
- **Variable Token (`--main-light`)**: `#d18221` — grounded in `var(--main-light)` in `:root`
- **Variable Token (`--background-color`)**: `#140d16` — grounded in `var(--background-color)` in `:root`
- **Variable Token (`--title-background-color`)**: `#111111` — grounded in `var(--title-background-color)` in `:root`
- **Variable Token (`--widget-color`)**: `#424242` — grounded in `var(--widget-color)` in `:root`
- **Variable Token (`--hover-color`)**: `#4f4f4f` — grounded in `var(--hover-color)` in `:root`
- **Variable Token (`--focus-color`)**: `#595959` — grounded in `var(--focus-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `80vw` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `9px` lateral canvas padding with `32px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80vw`, `gap: 32px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`
- **Corner Radii**: `4px`, `3px`, `100%`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Neuepower Ultra`
- **Body Font Stack**: `neue-haas-grotesk-display`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 64px`, `line-height: 57.6px`, `font-weight: 400`); rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: live computed `h3 (primary section heading)` (`font-size: 24px`, `line-height: 30px`, `font-weight: 700`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 500`); rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 500`); CSS variables `--font-family-mono: Menlo, Monaco, Consolas, "Droid Sans Mono", monospace`; rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-schemeengine-com` (`Home - Scheme Engine`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `www-schemeengine-com`)**:
   - DOM & Selectors: Landmark `<header class="header">` (`1440x104px`) hosting `Home - Scheme Engine` navigation (`D i r e c t o r s · W o r k · F i l m & t v · C o n t a c t`), DOM attributes (`data-wf-domain="www.schemeengine.com"`, `data-wf-page="6856ec97d986105f5589bbe0"`, `data-wf-site="6856ec97d986105f5589bbd7"`, `data-word="Directors"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `www-schemeengine-com`)` (`www-schemeengine-com`) adapts across `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)` with `cubic-bezier(0.2,0.6,0.35,1)`, `cubic-bezier(0.65,0,0.35,1)`, `cubic-bezier(0.25,0.46,0.45,0.94)` transitions and links `D i r e c t o r s · W o r k · F i l m & t v · C o n t a c t`.
2. **Hero Stage & Focal Lead (<section.section> — `We create from the culture we live`)**:
   - DOM & Selectors: Landmark `<section class="section">` presenting display lead `We create from the culture we live.` and copy excerpt *"Scheme Engine is a culture-first production company championing t"* over `#000000` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000000` background with `#ffffff` headline `We create from the culture we live.`.
3. **Primary Showcase & Content Grid (<section.section:nth(2)> — `Scheme Engine is a culture-first p`)**:
   - DOM & Selectors: Landmark `<section class="section">` rendering section `Scheme Engine is a culture-first production comp` with copy *"Our award-winning directors and creatives work across formats, al"*, asset references (`cdn.prod.website-files.com`, `schemeengine.webflow.shared.3fbb9...`, `soy0bmb.js`, `68b845cb16daf25e488bd7a5_scheme-e...`), and grid rule `body { margin: 0; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section:nth(2)> — `Scheme Engine is a culture-first p`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80vw`, `gap: 32px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section:nth(3)> — `Our award-winning directors and cr`)**:
   - DOM & Selectors: Landmark `<section class="section">` framing `Our award-winning directors and creatives work a` and `Impactful, resonant storytelling is rooted in li` (*"Impactful, resonant storytelling is rooted in lived experience. W"*) with `#333333` surface cards, `#0082f3` accents, and `summary { display: block; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section:nth(3)> — `Our award-winning directors and cr`)` uses `4px`, `3px`, `100%`, `50%` radii, `#0082f3` highlights, and assets (cdn.prod.website-files.com, schemeengine.webflow.shared.3fbb9..., soy0bmb.js).
5. **Colophon & Global Directory Footer (<footer.wf-active> — `https://www.schemeengine.com/`)**:
   - DOM & Selectors: Landmark `<footer class="wf-active">` anchoring `Home - Scheme Engine` footer links (`D i r e c t o r s · W o r k · F i l m & t v · C o n t a c t`), copy *"The future does not look like the past. Neither do we."*, and `#3898ec` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wf-active> — `https://www.schemeengine.com/`)` aligns to `80vw` (non-`@media` desktop container stylesheet rule) with `9px` lateral canvas padding with `32px` grid gap and attributes (data-wf-domain="www.schemeengine.com", data-wf-page="6856ec97d986105f5589bbe0", data-wf-site="6856ec97d986105f5589bbd7").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Scheme Engine is a culture-first production company championing the most exciting,..."*
- Copy Excerpt 2: *"Our award-winning directors and creatives work across formats, always attuned to t..."*
- Copy Excerpt 3: *"Impactful, resonant storytelling is rooted in lived experience. We deliver it with..."*
- Copy Excerpt 4: *"The future does not look like the past. Neither do we."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.2,0.6,0.35,1)`, `cubic-bezier(0.65,0,0.35,1)`, `cubic-bezier(0.25,0.46,0.45,0.94)`
- **Extracted Stylesheet Rules (`www-schemeengine-com`)**:
- `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`
- `body { margin: 0; }`
- `summary { display: block; }`
- `video { vertical-align: baseline; display: inline-block; }`
- `template { display: none; }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-schemeengine-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-schemeengine-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-schemeengine-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.2,0.6,0.35,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.section:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-schemeengine-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
