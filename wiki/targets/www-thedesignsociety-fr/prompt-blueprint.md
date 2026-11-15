---
title: "UI Prompt Blueprint: www-thedesignsociety-fr"
date: 2026-11-15
target: "[[overview|www-thedesignsociety-fr]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#ebedf5` canvas, `#1e1e1e` ink, `#bcf015` accent)"
---

# UI Design System & Master Generation Blueprint: www-thedesignsociety-fr

> **The Design Society Lyon — la communauté des designers** (https://www.thedesignsociety.fr/) — L'association qui réunit les designers de Lyon autour de talks et d'apéros. Une société secrète si mal gardée qu'on a fait un site. Proch...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-thedesignsociety-fr/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **The Design Society Lyon — la communauté des designers** (`https://www.thedesignsociety.fr/`). L'association qui réunit les designers de Lyon autour de talks et d'apéros. Une société secrète si mal gardée qu'on a fait un site. Proch...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ebedf5` canvas, `#1e1e1e` ink, `#bcf015` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ebedf5` (`var(--background)` in `:root`) paired with `#1e1e1e` primary typography and `#bcf015` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Fkrasterromancompact Smooth` for display copy (`The Design Society — La société secr`) with `Geistpixel Line` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(0.625,0.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-thedesignsociety-fr/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `www-thedesignsociety-fr` stylesheet.
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `var(--radius--radius-s)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ebedf5` | `var(--background)` in `:root` |
| **Primary Typography Ink** | `#f0f0f0` | `var(--blue--content)` in `:root` |
| **Elevated Surface / Card Substrate** | `#350aff` | `var(--brand-color-2)` in `:root` |
| **Interactive Accent / Highlight** | `#bcf015` | `var(--brand-color-1)` in `:root` |
| **Secondary / Muted Copy** | `#1e1e1e` | `var(--content)` in `:root` |
| **Structural Hairline Border** | `#f7f7f7` | `var(--background-subtle)` in `:root` |
| **Variable Token (`--border`)** | `#1d1d1d26` | `var(--border)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `#ebedf5` | Canvas / Surface Token |
| `--_theme---content` | `var(--content)` | Brand / Palette Token |
| `--radius--radius-s` | `4px` | Elevation / Border Token |
| `--border` | `#1d1d1d26` | Elevation / Border Token |
| `--radius--radius-m` | `6px` | Elevation / Border Token |
| `--_theme---background-accent` | `var(--background-accent)` | Canvas / Surface Token |
| `--_theme---brand-color-2` | `var(--brand-color-2)` | Brand / Palette Token |
| `--_responsive---hero--padding-top` | `10em` | Layout / Spatial Grid Token |
| `--blue--content` | `#f0f0f0` | Color / Atmospheric Token |
| `--_responsive---hero--title-marquee` | `10em` | Dimension / Scale Token |
| `--brand-color-2` | `#350aff` | Brand / Palette Token |
| `--brand-color-1` | `#bcf015` | Brand / Palette Token |
| `--_responsive---hero--eye` | `150px` | Dimension / Scale Token |
| `--_responsive---hero--margin` | `var(--size--m)` | Layout / Spatial Grid Token |
| `--_theme---border` | `var(--border)` | Brand / Palette Token |
| `--_theme---content-subtle` | `var(--content-subtle)` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Fkrasterromancompact Smooth`.
- **Primary Body Stack**: `Geistpixel Line`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`).
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.625,0.05,0,1)`, `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(0.7,0,0.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `www-thedesignsociety-fr` stylesheet.
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-thedesignsociety-fr` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-thedesignsociety-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.625,0.05,0,1)`)**: Governs interactive state transitions across `<nav.twostep-nav>` and `<section.mwg005>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — The Design Society Lyon — la communauté de │
│ ====================================================================== │
│ [ <nav.twostep-nav>        | A c c u e i l · É v è n e m e n t s ·  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.mwg020>                                     |   │
│ | H1: The Design Society — La société secrète la moins...          |   │
│ | Substrate: #ebedf5    | Ink: #1e1e1e    | Accent: #bcf015        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.mwg005>          ) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | É v è n e m e n t s          |  | E v e n t b r i t e          | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<nav.twostep-nav>] -> [<section.mwg020>] -> [<section.mwg005>] |    │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://www.thedesignsociety.fr/   │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.twostep-nav> — `www-thedesignsociety-fr`)**:
   - Landmark `<nav class="twostep-nav">` hosting `The Design Society Lyon — la communa` navigation (`A c c u e i l · É v è n e m e n t s · A p r o p o s · C o n t a c t · I n s t a g r a m`), DOM attributes (`data-wf-domain="www.thedesignsociety.fr"`, `data-wf-page="698de82380130d2fe9cadaf6"`, `data-wf-site="698de82080130d2fe9cada54"`, `data-barba="wrapper"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.mwg020> — `The Design Society — La société se`)**:
   - Landmark `<section class="mwg020">` presenting display lead `The Design Society — La société secrète la moins...` and copy excerpt *"É v è n e m e n t s"* over `#ebedf5` canvas and `#1e1e1e` ink.
3. **Primary Showcase & Content Grid (<section.mwg005> — `É v è n e m e n t s`)**:
   - Landmark `<section class="mwg005">` rendering section `É v è n e m e n t s` with copy *"E v e n t b r i t e"*, asset references (`cdn.prod.website-files.com`, `the-design-society-22535e.webflow...`, `6a96a56caf2dbc50ad13753b_webclip.png`, `6a96a56c5cc7207fcb2e955c_webclip.png`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.section-6> — `E v e n t b r i t e`)**:
   - Landmark `<section class="section-6">` framing `E v e n t b r i t e` and `A c c è s p r e s q u e r e s t r e i n t` (*"A c c è s p r e s q u e r e s t r e i n t"*) with `#350aff` surface cards, `#bcf015` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.thedesignsociety.fr/`)**:
   - Landmark `<footer class="footer">` anchoring `The Design Society Lyon — la com` footer links (`A c c u e i l · É v è n e m e n t s · A p r o p o s · C o n t a c t · I n s t a g r a m`), copy *"A n o n y m a t r e l a t i f"*, and `#f7f7f7` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-thedesignsociety-fr (The Design Society Lyon — la communauté des designers)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-thedesignsociety-fr` (**The Design Society Lyon — la communauté des designers** — `https://www.thedesignsociety.fr/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ebedf5` canvas, `#1e1e1e` ink, `#bcf015` accent).
- **Identity & Domain Context**: L'association qui réunit les designers de Lyon autour de talks et d'apéros. Une société secrète si mal gardée qu'on a fait un site. Proch...
- **Primary Substrate**: `#ebedf5` (`var(--background)` in `:root`), **Primary Ink**: `#1e1e1e`, **Accent / Highlight**: `#bcf015`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ebedf5` (`var(--background)` in `:root`) paired with `#1e1e1e` primary typography and `#bcf015` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Fkrasterromancompact Smooth` for display copy (`The Design Society — La société secr`) with `Geistpixel Line` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(0.625,0.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-thedesignsociety-fr` in your global stylesheet:

:root {
  /* The Design Society Lyon — la communauté des designers (www-thedesignsociety-fr) — Ground-Truth Extracted CSS Variables */
  --background: #ebedf5; /* Canvas / Surface Token (www-thedesignsociety-fr) */
  --_theme---content: var(--content); /* Brand / Palette Token (www-thedesignsociety-fr) */
  --radius--radius-s: 4px; /* Elevation / Border Token (www-thedesignsociety-fr) */
  --border: #1d1d1d26; /* Elevation / Border Token (www-thedesignsociety-fr) */
  --radius--radius-m: 6px; /* Elevation / Border Token (www-thedesignsociety-fr) */
  --_theme---background-accent: var(--background-accent); /* Canvas / Surface Token (www-thedesignsociety-fr) */
  --_theme---brand-color-2: var(--brand-color-2); /* Brand / Palette Token (www-thedesignsociety-fr) */
  --_responsive---hero--padding-top: 10em; /* Layout / Spatial Grid Token (www-thedesignsociety-fr) */
  --blue--content: #f0f0f0; /* Color / Atmospheric Token (www-thedesignsociety-fr) */
  --_responsive---hero--title-marquee: 10em; /* Dimension / Scale Token (www-thedesignsociety-fr) */
  --brand-color-2: #350aff; /* Brand / Palette Token (www-thedesignsociety-fr) */
  --brand-color-1: #bcf015; /* Brand / Palette Token (www-thedesignsociety-fr) */
  --_responsive---hero--eye: 150px; /* Dimension / Scale Token (www-thedesignsociety-fr) */
  --_responsive---hero--margin: var(--size--m); /* Layout / Spatial Grid Token (www-thedesignsociety-fr) */
  --_theme---border: var(--border); /* Brand / Palette Token (www-thedesignsociety-fr) */
  --_theme---content-subtle: var(--content-subtle); /* Brand / Palette Token (www-thedesignsociety-fr) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ebedf5` — grounded in `var(--background)` in `:root`
- **Primary Typography Ink**: `#f0f0f0` — grounded in `var(--blue--content)` in `:root`
- **Elevated Surface / Card Substrate**: `#350aff` — grounded in `var(--brand-color-2)` in `:root`
- **Interactive Accent / Highlight**: `#bcf015` — grounded in `var(--brand-color-1)` in `:root`
- **Secondary / Muted Copy**: `#1e1e1e` — grounded in `var(--content)` in `:root`
- **Structural Hairline Border**: `#f7f7f7` — grounded in `var(--background-subtle)` in `:root`
- **Variable Token (`--border`)**: `#1d1d1d26` — grounded in `var(--border)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `www-thedesignsociety-fr` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `var(--radius--radius-s)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Fkrasterromancompact Smooth`
- **Body Font Stack**: `Geistpixel Line`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy Rule**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Index Rule**: rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-thedesignsociety-fr` (`The Design Society Lyon — la communauté des designers`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.twostep-nav> — `www-thedesignsociety-fr`)**:
   - DOM & Selectors: Landmark `<nav class="twostep-nav">` hosting `The Design Society Lyon — la communa` navigation (`A c c u e i l · É v è n e m e n t s · A p r o p o s · C o n t a c t · I n s t a g r a m`), DOM attributes (`data-wf-domain="www.thedesignsociety.fr"`, `data-wf-page="698de82380130d2fe9cadaf6"`, `data-wf-site="698de82080130d2fe9cada54"`, `data-barba="wrapper"`), and stylesheet rule `html.lenis body { height:auto }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.twostep-nav> — `www-thedesignsociety-fr`)` (`www-thedesignsociety-fr`) adapts across `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)` with `cubic-bezier(0.625,0.05,0,1)`, `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(0.7,0,0.3,1)` transitions and links `A c c u e i l · É v è n e m e n t s · A p r o p o s · C o n t a c t · I n s t a g r a m`.
2. **Hero Stage & Focal Lead (<section.mwg020> — `The Design Society — La société se`)**:
   - DOM & Selectors: Landmark `<section class="mwg020">` presenting display lead `The Design Society — La société secrète la moins...` and copy excerpt *"É v è n e m e n t s"* over `#ebedf5` canvas and `#1e1e1e` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ebedf5` background with `#1e1e1e` headline `The Design Society — La société secrète la moins...`.
3. **Primary Showcase & Content Grid (<section.mwg005> — `É v è n e m e n t s`)**:
   - DOM & Selectors: Landmark `<section class="mwg005">` rendering section `É v è n e m e n t s` with copy *"E v e n t b r i t e"*, asset references (`cdn.prod.website-files.com`, `the-design-society-22535e.webflow...`, `6a96a56caf2dbc50ad13753b_webclip.png`, `6a96a56c5cc7207fcb2e955c_webclip.png`), and grid rule `.lenis-stopped { overflow:clip }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.mwg005> — `É v è n e m e n t s`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section-6> — `E v e n t b r i t e`)**:
   - DOM & Selectors: Landmark `<section class="section-6">` framing `E v e n t b r i t e` and `A c c è s p r e s q u e r e s t r e i n t` (*"A c c è s p r e s q u e r e s t r e i n t"*) with `#350aff` surface cards, `#bcf015` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section-6> — `E v e n t b r i t e`)` uses `3px`, `100%`, `50%`, `var(--radius--radius-s)` radii, `#bcf015` highlights, and assets (cdn.prod.website-files.com, the-design-society-22535e.webflow..., 6a96a56caf2dbc50ad13753b_webclip.png).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.thedesignsociety.fr/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `The Design Society Lyon — la com` footer links (`A c c u e i l · É v è n e m e n t s · A p r o p o s · C o n t a c t · I n s t a g r a m`), copy *"A n o n y m a t r e l a t i f"*, and `#f7f7f7` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://www.thedesignsociety.fr/`)` aligns to `940px` extracted from `www-thedesignsociety-fr` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.thedesignsociety.fr", data-wf-page="698de82380130d2fe9cadaf6", data-wf-site="698de82080130d2fe9cada54").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"É v è n e m e n t s"*
- Copy Excerpt 2: *"E v e n t b r i t e"*
- Copy Excerpt 3: *"A c c è s p r e s q u e r e s t r e i n t"*
- Copy Excerpt 4: *"A n o n y m a t r e l a t i f"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.625,0.05,0,1)`, `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(0.7,0,0.3,1)`
- **Extracted Stylesheet Rules (`www-thedesignsociety-fr`)**:
- `html.lenis body { height:auto }`
- `.lenis-stopped { overflow:clip }`
- `.lenis.lenis-smooth iframe { pointer-events:none }`
- `.lenis.lenis-autoToggle { transition-property:overflow;transition-duration:1ms;transition-behavior... }`
- `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`
- **Per-Selector Transition Rules**:
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `www-thedesignsociety-fr` stylesheet.
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-thedesignsociety-fr` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-thedesignsociety-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.625,0.05,0,1)`)**: Governs interactive state transitions across `<nav.twostep-nav>` and `<section.mwg005>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-thedesignsociety-fr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
