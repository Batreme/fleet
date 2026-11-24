---
title: "UI Prompt Blueprint: jozue-fr"
date: 2026-11-24
captured_at: 2026-11-24
target: "jozue-fr"
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
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#111319` ink, `#f73326` accent)"
---

# UI Design System & Master Generation Blueprint: jozue-fr

> **Josué Pichot, freelance art director and photographer in Paris** (https://jozue.fr) — Paris-based freelance art director, photographer, director and product designer. 15+ years in advertising and digital. Available in-house...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Josué Pichot, freelance art director and photographer in Paris** (`https://jozue.fr`). Paris-based freelance art director, photographer, director and product designer. 15+ years in advertising and digital. Available in-house...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#111319` ink, `#f73326` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#111319` primary typography and `#f73326` accents.
  - **Grounded Typographic Hierarchy**: Uses `Neue Haas Grotesk Display` across display (`art director + photo grapher`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1399px` container bounds (`gap: 5rem`, padding `15px`) with `cubic-bezier(.4,0,1,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=9764px` / doc `11028px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1399px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `15px` lateral canvas padding with `5rem` grid gap.
- **Border Radius Scale**: `5px`, `3rem`, `1.9rem`, `2rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1399px`, `gap: 5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `15px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:767px)`, `@media (min-width:1024px)`, `@media (min-width:420px)`, `@media (min-width:1100px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#111319` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f2f0` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#f73326` | `.button-selected:hover { color: #f73326 }` |
| **Secondary / Muted Copy** | `#999999` | `.lightbox { color: #999999 }` |
| **Structural Hairline Border** | `#8c8c8c` | `.button-slide:hover path { stroke: #8c8c8c }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--motion-fast` | `200ms` | Motion / Easing Token |
| `--motion-base` | `300ms` | Motion / Easing Token |
| `--motion-slow` | `1000ms` | Motion / Easing Token |
| `--ease-default` | `ease` | Motion / Easing Token |
| `--ease-in` | `ease-in` | Motion / Easing Token |
| `--ease-in-out` | `ease-in-out` | Motion / Easing Token |
| `--transition-fade-in` | `300ms` | Motion / Easing Token |
| `--transition-hold` | `1000ms` | Motion / Easing Token |
| `--transition-fade-out` | `300ms` | Motion / Easing Token |
| `--dur-micro` | `160ms` | Motion / Timing Token |
| `--dur-base` | `380ms` | Motion / Timing Token |
| `--dur-move` | `720ms` | Motion / Timing Token |
| `--dur-cine` | `1400ms` | Motion / Timing Token |
| `--ease-enter` | `cubic-bezier(0.22,0.61,0.36,1)` | Motion / Easing Token |
| `--ease-exit` | `cubic-bezier(0.4,0,1,1)` | Motion / Easing Token |
| `--ease-move` | `cubic-bezier(0.4,0,0.2,1)` | Motion / Easing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Neue Haas Grotesk Display`.
- **Primary Body Stack**: `Neue Haas Grotesk Display`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 170px`, `line-height: 125.8px`, `font-weight: 700`, `letter-spacing: -5.1px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 170px`, `line-height: 125.8px`, `font-weight: 700`, `letter-spacing: -5.1px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); rule `p` (`font-size: 2.3rem`, `line-height: 1.22`, `letter-spacing: .03em`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(0.4,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `-vendor=youtube_nocookie] .lazyfr...`**: `transition: color .1s cubic-bezier(.4,0,1,1)` extracted from `jozue-fr` stylesheet.
- **Selector `.button-selected`**: `transition: all .3s` extracted from `jozue-fr` stylesheet.
- **Selector `.menu-toggle-bar`**: `transition: all .3s` extracted from `jozue-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<nav.menu>` and `<section.js-infos>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<article.homepage>` and `<section.js-infos>` interactive targets.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `11028px`, deepest scrollY reached `9764px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Nav / Drawer Probe (`Menu`)**: Triggered visual change (pixel diff `16.227`, captured in `assets/state-nav.webp`); revealed links: About., Works., Contact., 93310 Le Pré-Saint-Ge..., +33 6 61 77 32 20, hi@jozue.fr.
- **Hover Physics (`primary_cta` · `About.`)**: Computed transition `0.38s` / `cubic-bezier(0.22, 0.61, 0.36, 1)` (no static color/transform shift captured at rest).
- **Route Transition Architecture**: First internal navigation (`/works/billy/`) measured as `direct` in `890ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Josué Pichot, freelance art director and p │
│ ====================================================================== │
│ [ <nav.menu> (1440x900px)             | About. · Works. · Contact. · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.homepage> (w=1440px)                          | │
│ | H1: art director + photo grapher                                   | │
│ | Substrate: #ffffff | Ink: #111319 | Accent: #f73326                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.js-infos>) max-w: 1399px                   | │
│ | +------------------------------+  +------------------------------+ | │
│ | | a r t d i r e c t o r + p h  |  | selected works 18            | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.wrapper>) — Awards & Archives              | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.transi>     ) | https://jozue.fr                     │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 5rem)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.menu>              ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<article.homepage>) — 390px Vertical Lead              | │
│ | H1: art director + photo grapher                                   | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.js-infos>) — 1-Col Stack                  | │
│ | [ Item 1: a r t d i r e c t o r + p h o t o g r a p h e r c...   ] | │
│ | [ Item 2: selected works 18                                      ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.wrapper>) — 1-Col (Awards & Archives)       | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.transi>     ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.menu> — `jozue-fr`)**:
   - Landmark `<nav class="menu menu--site">` (`1440x900px`) hosting `Josué Pichot, freelance art director` navigation (`About. · Works. · Contact. · Français.`), DOM attributes (`data-intro="done"`, `data-color="111319"`, `data-color="F73326"`, `data-title="About"`), and stylesheet rule `.lazyframe__title { z-index:3;padding:15px 17px;position:absolute;top:0;left:0;right:0 }`.
2. **Hero Stage & Focal Lead (<article.homepage> — `art director + photo grapher`)**:
   - Landmark `<article class="homepage">` presenting display lead `art director + photo grapher` and copy excerpt *"93310 Le Pré-Saint-Gervais"* over `#ffffff` canvas and `#111319` ink.
3. **Primary Showcase & Content Grid (<section.js-infos> — `a r t d i r e c t o r + p h o t o `)**:
   - Landmark `<section class="js-infos homepage__infos">` rendering section `a r t d i r e c t o r + p h o t o g r a p h e r c...` with copy *"English. Français."*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `jozue-logo-full.DpMZCk-F.svg`), and grid rule `.lazyframe__title:after { z-index:-1 }`.
4. **Interactive Detail & Feature Matrix (<section.wrapper> — `selected works 18`)**:
   - Landmark `<section class="wrapper wrapper--infos">` framing `selected works 18` and `Awards & Archives` (*"a r t d i r e c t o r + p h o t o g r a p h e r"*) with `#f3f2f0` surface cards, `#f73326` accents, and `.lazyframe:hover { cursor:pointer }`.
5. **Colophon & Global Directory Footer (<footer.transi> — `https://jozue.fr`)**:
   - Landmark `<footer class="transi">` anchoring `Josué Pichot, freelance art dire` footer links (`About. · Works. · Contact. · Français.`), copy *"a r t d i r e c t o r"*, and `#8c8c8c` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `art director + photo grapher` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `8%`): Active landmark `selected works 18` · sticky/fixed elements: `1`
- **Step 03** (`y=2380px`, `24%`): Active landmark `Section @ 24%` · sticky/fixed elements: `2`
- **Step 04** (`y=4091px`, `41%`): Active landmark `Section @ 41%` · sticky/fixed elements: `2`
- **Step 05** (`y=5950px`, `61%`): Active landmark `Section @ 61%` · sticky/fixed elements: `1`
- **Step 06** (`y=7650px`, `78%`): Active landmark `FEW WORDS` · sticky/fixed elements: `1`
- **Step 07** (`y=9350px`, `96%`): Active landmark `PARTNERS IN CRIME` · sticky/fixed elements: `1`
- **Step 08** (`y=9764px`, `100%`): Active landmark `#contact` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Detail Route (`/works/billy/`)**: `https://jozue.fr/works/billy/` — H1: `billy`, scrollHeight `7856px`, transition `direct` (`890ms`)
- **Detail Route (`/works/hoppy-road/`)**: `https://jozue.fr/works/hoppy-road/` — H1: `hoppy road`, scrollHeight `8115px`, transition `direct` (`814ms`)
- **Detail Route (`/works/vianney/`)**: `https://jozue.fr/works/vianney/` — H1: `vianney`, scrollHeight `8598px`, transition `direct` (`943ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: jozue-fr (Josué Pichot, freelance art director and photographer in Paris)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `jozue-fr` (**Josué Pichot, freelance art director and photographer in Paris** — `https://jozue.fr`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#111319` ink, `#f73326` accent).
- **Identity & Domain Context**: Paris-based freelance art director, photographer, director and product designer. 15+ years in advertising and digital. Available in-house...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#111319`, **Accent / Highlight**: `#f73326`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#111319` primary typography and `#f73326` accents.
  - **Grounded Typographic Hierarchy**: Uses `Neue Haas Grotesk Display` across display (`art director + photo grapher`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1399px` container bounds (`gap: 5rem`, padding `15px`) with `cubic-bezier(.4,0,1,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `jozue-fr` in your global stylesheet:

:root {
  /* Josué Pichot, freelance art director and photographer in Paris (jozue-fr) — Live-Grounded CSS Variables */
  --motion-fast: 200ms; /* Motion / Easing Token (jozue-fr) */
  --motion-base: 300ms; /* Motion / Easing Token (jozue-fr) */
  --motion-slow: 1000ms; /* Motion / Easing Token (jozue-fr) */
  --ease-default: ease; /* Motion / Easing Token (jozue-fr) */
  --ease-in: ease-in; /* Motion / Easing Token (jozue-fr) */
  --ease-in-out: ease-in-out; /* Motion / Easing Token (jozue-fr) */
  --transition-fade-in: 300ms; /* Motion / Easing Token (jozue-fr) */
  --transition-hold: 1000ms; /* Motion / Easing Token (jozue-fr) */
  --transition-fade-out: 300ms; /* Motion / Easing Token (jozue-fr) */
  --dur-micro: 160ms; /* Motion / Timing Token (jozue-fr) */
  --dur-base: 380ms; /* Motion / Timing Token (jozue-fr) */
  --dur-move: 720ms; /* Motion / Timing Token (jozue-fr) */
  --dur-cine: 1400ms; /* Motion / Timing Token (jozue-fr) */
  --ease-enter: cubic-bezier(0.22,0.61,0.36,1); /* Motion / Easing Token (jozue-fr) */
  --ease-exit: cubic-bezier(0.4,0,1,1); /* Motion / Easing Token (jozue-fr) */
  --ease-move: cubic-bezier(0.4,0,0.2,1); /* Motion / Easing Token (jozue-fr) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#111319` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f3f2f0` — grounded in live computed `section` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#f73326` — grounded in `.button-selected:hover { color: #f73326 }`
- **Secondary / Muted Copy**: `#999999` — grounded in `.lightbox { color: #999999 }`
- **Structural Hairline Border**: `#8c8c8c` — grounded in `.button-slide:hover path { stroke: #8c8c8c }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1399px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `15px` lateral canvas padding with `5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1399px`, `gap: 5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `15px` horizontal padding
- **Media Queries**: `@media (min-width:767px)`, `@media (min-width:1024px)`, `@media (min-width:420px)`, `@media (min-width:1100px)`
- **Corner Radii**: `5px`, `3rem`, `1.9rem`, `2rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Neue Haas Grotesk Display`
- **Body Font Stack**: `Neue Haas Grotesk Display`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 170px`, `line-height: 125.8px`, `font-weight: 700`, `letter-spacing: -5.1px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 170px`, `line-height: 125.8px`, `font-weight: 700`, `letter-spacing: -5.1px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); rule `p` (`font-size: 2.3rem`, `line-height: 1.22`, `letter-spacing: .03em`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `jozue-fr` (`Josué Pichot, freelance art director and photographer in Paris`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.menu> — `jozue-fr`)**:
   - DOM & Selectors: Landmark `<nav class="menu menu--site">` (`1440x900px`) hosting `Josué Pichot, freelance art director` navigation (`About. · Works. · Contact. · Français.`), DOM attributes (`data-intro="done"`, `data-color="111319"`, `data-color="F73326"`, `data-title="About"`), and stylesheet rule `.lazyframe__title { z-index:3;padding:15px 17px;position:absolute;top:0;left:0;right:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.menu> — `jozue-fr`)` (`jozue-fr`) adapts across `@media (min-width:767px)`, `@media (min-width:1024px)`, `@media (min-width:420px)`, `@media (min-width:1100px)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(0.4,0,1,1)` transitions and links `About. · Works. · Contact. · Français.`.
2. **Hero Stage & Focal Lead (<article.homepage> — `art director + photo grapher`)**:
   - DOM & Selectors: Landmark `<article class="homepage">` presenting display lead `art director + photo grapher` and copy excerpt *"93310 Le Pré-Saint-Gervais"* over `#ffffff` canvas and `#111319` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#ffffff` background with `#111319` headline `art director + photo grapher`.
3. **Primary Showcase & Content Grid (<section.js-infos> — `a r t d i r e c t o r + p h o t o `)**:
   - DOM & Selectors: Landmark `<section class="js-infos homepage__infos">` rendering section `a r t d i r e c t o r + p h o t o g r a p h e r c...` with copy *"English. Français."*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `jozue-logo-full.DpMZCk-F.svg`), and grid rule `.lazyframe__title:after { z-index:-1 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.js-infos> — `a r t d i r e c t o r + p h o t o `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1399px`, `gap: 5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `15px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.wrapper> — `selected works 18`)**:
   - DOM & Selectors: Landmark `<section class="wrapper wrapper--infos">` framing `selected works 18` and `Awards & Archives` (*"a r t d i r e c t o r + p h o t o g r a p h e r"*) with `#f3f2f0` surface cards, `#f73326` accents, and `.lazyframe:hover { cursor:pointer }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.wrapper> — `selected works 18`)` uses `5px`, `3rem`, `1.9rem`, `2rem` radii, `#f73326` highlights, and assets (favicon.ico, favicon.svg, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.transi> — `https://jozue.fr`)**:
   - DOM & Selectors: Landmark `<footer class="transi">` anchoring `Josué Pichot, freelance art dire` footer links (`About. · Works. · Contact. · Français.`), copy *"a r t d i r e c t o r"*, and `#8c8c8c` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.transi> — `https://jozue.fr`)` aligns to `1399px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `15px` lateral canvas padding with `5rem` grid gap and attributes (data-intro="done", data-color="111319", data-color="F73326").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"93310 Le Pré-Saint-Gervais"*
- Copy Excerpt 2: *"English. Français."*
- Copy Excerpt 3: *"a r t d i r e c t o r + p h o t o g r a p h e r"*
- Copy Excerpt 4: *"a r t d i r e c t o r"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(0.4,0,1,1)`
- **Extracted Stylesheet Rules (`jozue-fr`)**:
- `.lazyframe__title { z-index:3;padding:15px 17px;position:absolute;top:0;left:0;right:0 }`
- `.lazyframe__title:after { z-index:-1 }`
- `.lazyframe:hover { cursor:pointer }`
- `.lazyframe:before { content:"";width:100%;padding-top:100%;display:block }`
- `before { padding-top:56.25% }`
- **Per-Selector Transition Rules**:
- **Selector `-vendor=youtube_nocookie] .lazyfr...`**: `transition: color .1s cubic-bezier(.4,0,1,1)` extracted from `jozue-fr` stylesheet.
- **Selector `.button-selected`**: `transition: all .3s` extracted from `jozue-fr` stylesheet.
- **Selector `.menu-toggle-bar`**: `transition: all .3s` extracted from `jozue-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<nav.menu>` and `<section.js-infos>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<article.homepage>` and `<section.js-infos>` interactive targets.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `11028px` across 8 distinct viewport chapters.
- **Vertical Chapter Sequence**: art director + photo grapher (0%) -> selected works 18 (8%) -> Section @ 24% (24%) -> Section @ 41% (41%) -> Section @ 61% (61%) -> FEW WORDS (78%) -> PARTNERS IN CRIME (96%) -> #contact (100%).
- **Navigation Drawer / Menu State**: Replicate interactive menu toggle (`Menu`) with Escape-to-close keyboard handling.
- **Multi-Page Routes**: Scaffold internal routes `/works/billy/` (detail, direct), `/works/hoppy-road/` (detail, direct), `/works/vianney/` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `jozue-fr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | art director + photo grapher | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `8%` | selected works 18 | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2380px` | `24%` | Section @ 24% | `2` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `4091px` | `41%` | Section @ 41% | `2` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `5950px` | `61%` | Section @ 61% | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `7650px` | `78%` | FEW WORDS | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `9350px` | `96%` | PARTNERS IN CRIME | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `9764px` | `100%` | #contact | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | art director + photo grapher | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `3395px` | `50%` | let's talk | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `6738px` | `100%` | #contact | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `nav_menu` | Nav/Menu opened (`Menu`, diff `16.227`) | [state-nav.webp](assets/state-nav.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `detail` | `https://jozue.fr/works/billy/` | billy | `7856px` | `direct` (`890ms`) | [subpage-01-works-billy.webp](assets/subpage-01-works-billy.webp) |
| `2` | `detail` | `https://jozue.fr/works/hoppy-road/` | hoppy road | `8115px` | `direct` (`814ms`) | [subpage-02-works-hoppy-road.webp](assets/subpage-02-works-hoppy-road.webp) |
| `3` | `detail` | `https://jozue.fr/works/vianney/` | vianney | `8598px` | `direct` (`943ms`) | [subpage-03-works-vianney.webp](assets/subpage-03-works-vianney.webp) |

