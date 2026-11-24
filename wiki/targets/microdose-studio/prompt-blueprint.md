---
title: "UI Prompt Blueprint: microdose-studio"
date: 2026-11-24
captured_at: 2026-11-24
target: "microdose-studio"
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
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0000ff`)"
---

# UI Design System & Master Generation Blueprint: microdose-studio

> **Microdose Studio - Design & Development Agency for Startups** (https://microdose.studio/) — Microdose Studio helps tech startups turn ideas into products through strategy, brand and product design, React/Next.js development, and...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Microdose Studio - Design & Development Agency for Startups** (`https://microdose.studio/`). Microdose Studio helps tech startups turn ideas into products through strategy, brand and product design, React/Next.js development, and...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0000ff`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#0c152a` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Uses `Geist` across display (`We build AI-first products for start`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1530px` container bounds (`gap: 4px`, padding `195px`) with `cubic-bezier(0.87,0.45,0.33,0.88)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=14131px` / doc `15031px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1530px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `195px` lateral canvas padding with `4px` grid gap.
- **Border Radius Scale**: `100px`, `var(--radius-pill)`, `6.25rem`, `1px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1530px`, `gap: 4px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `195px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (min-width: 768px) and (max-width: 819px)`, `@media (max-width: 1640px)`, `@media (max-width: 1520px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0c152a` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e8e8ec` | `var(--color-card-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ff` | `.legal-block a:hover { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#6b6c71` | `var(--color-muted)` in `:root` |
| **Structural Hairline Border** | `#eae5e5` | `var(--color-footer-border)` in `:root` (`rgba(116, 84, 84, 0.15)`) |
| **Variable Token (`--color-black`)** | `#19171b` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-bg-dark`)** | `#121113` | `var(--color-bg-dark)` in `:root` |
| **Variable Token (`--color-blue-start`)** | `#1935d9` | `var(--color-blue-start)` in `:root` |
| **Variable Token (`--color-blue-end`)** | `#2f2be2` | `var(--color-blue-end)` in `:root` |
| **Variable Token (`--color-blue-border`)** | `#1f34c9` | `var(--color-blue-border)` in `:root` |
| **Variable Token (`--color-grey-cool`)** | `#818a94` | `var(--color-grey-cool)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#19171b` | Canvas / Surface Token |
| `--color-dark` | `#0c152a` | Canvas / Surface Token |
| `--color-muted` | `#6b6c71` | Brand / Palette Token |
| `--color-white` | `#ffffff` | Canvas / Surface Token |
| `--color-bg-dark` | `#121113` | Canvas / Surface Token |
| `--color-card-bg` | `#e8e8ec` | Canvas / Surface Token |
| `--color-blue-start` | `#1935d9` | Brand / Palette Token |
| `--color-blue-end` | `#2f2be2` | Brand / Palette Token |
| `--color-blue-border` | `#1f34c9` | Brand / Palette Token |
| `--color-footer-border` | `rgba(116, 84, 84, 0.15)` | Brand / Palette Token |
| `--color-white-50` | `rgba(255, 255, 255, 0.5)` | Canvas / Surface Token |
| `--color-grey-cool` | `#818a94` | Brand / Palette Token |
| `--font-primary` | `'Geist', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif` | Brand / Palette Token |
| `--font-accent` | `'Metal', serif` | Brand / Palette Token |
| `--radius-lg` | `16px` | Elevation / Border Token |
| `--radius-xl` | `24px` | Elevation / Border Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Geist`.
- **Primary Body Stack**: `Geist`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 80px`, `font-weight: 400`, `letter-spacing: -4.32px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 80px`, `font-weight: 400`, `letter-spacing: -4.32px`); rule `h2` (`font-size: 26px`, `line-height: 42px`, `letter-spacing: -1.56px`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `body` (`font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.87,0.45,0.33,0.88)`, `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(0.43,0.98,0.87,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.page-bg--fade`**: `transition: opacity 1.2s ease` extracted from `microdose-studio` stylesheet.
- **Selector `media (prefers-reduced-motion: re...`**: `transition: none` extracted from `microdose-studio` stylesheet.
- **Selector `.nav`**: `transition: background 0.3s` extracted from `microdose-studio` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.87,0.45,0.33,0.88)`)**: Governs interactive state transitions across `<nav.nav>` and `<section.portfolio-carousel>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `15031px`, deepest scrollY reached `14131px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`, `WebGL/Canvas`.
- **Route Transition Architecture**: First internal navigation (`/case-studies`) measured as `MPA` in `1099ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Microdose Studio - Design & Development Ag │
│ ====================================================================== │
│ [ <nav.nav> (1440x80px)               | microdose .studio · About us ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: We build AI-first products for startups and enter...           | │
│ | Substrate: #ffffff | Ink: #0c152a | Accent: #0000ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.portfolio-carouse) max-w: 1530px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | W e b u i l d A I - f i r s  |  | O u r s e l e c t e d p r o  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.about>) — M o b i l e A p p f o            | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | https://microdose.studio/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 4px)        │
│ ====================================================================== │
│ [ HEADER BAR (<nav.nav>               ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: We build AI-first products for startups and enter...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.portfolio-car) — 1-Col Stack              | │
│ | [ Item 1: W e b u i l d A I - f i r s t p r o d u c t s f o...   ] | │
│ | [ Item 2: O u r s e l e c t e d p r o j e c t s .                ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.about>) — 1-Col (M o b i l e A p p )        | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.nav> — `microdose-studio`)**:
   - Landmark `<nav class="nav blur-fade-in">` (`1440x80px`) hosting `Microdose Studio - Design & Developm` navigation (`microdose .studio · About us 01 · Case Studies 02 · Services 03 · Labs 04`), DOM attributes (`data-scroll-indicator="home"`, `data-consent="deny"`, `data-consent="accept"`, `data-chrome="nav"`), and stylesheet rule `after { margin: 0; padding: 0; box-sizing: border-box; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `We build AI-first products for sta`)**:
   - Landmark `<section class="hero blur-fade-in">` presenting display lead `We build AI-first products for startups and enter...` and copy excerpt *"We use cookies to improve experience and performance of our websi"* over `#ffffff` canvas and `#0c152a` ink.
3. **Primary Showcase & Content Grid (<section.portfolio-carousel> — `W e b u i l d A I - f i r s t p r `)**:
   - Landmark `<section class="portfolio-carousel">` rendering section `W e b u i l d A I - f i r s t p r o d u c t s f o...` with copy *"Accepting new projects"*, asset references (`favicon-96x96.png`, `favicon.ico`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `selection { background-color: var(--color-blue-start); color: var(--color-white); te... }`.
4. **Interactive Detail & Feature Matrix (<section.about> — `O u r s e l e c t e d p r o j e c `)**:
   - Landmark `<section class="about">` framing `O u r s e l e c t e d p r o j e c t s .` and `M o b i l e A p p f o r H y p e r P e r s o n a l...` (*"Your Design & Dev Partner."*) with `#e8e8ec` surface cards, `#0000ff` accents, and `html { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://microdose.studio/`)**:
   - Landmark `<footer class="footer">` anchoring `Microdose Studio - Design & Deve` footer links (`microdose .studio · About us 01 · Case Studies 02 · Services 03 · Labs 04`), copy *"e n t e r p r i s e s ."*, and `#eae5e5` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `We build AI-first products for startups and enter...` · sticky/fixed elements: `4`
- **Step 02** (`y=850px`, `6%`): Active landmark `#about` · sticky/fixed elements: `5`
- **Step 03** (`y=4250px`, `30%`): Active landmark `Unifying a Global GTM Analytics Platform from Ide...` · sticky/fixed elements: `3`
- **Step 04** (`y=5950px`, `42%`): Active landmark `Designing modern experience for a global diagnost...` · sticky/fixed elements: `3`
- **Step 05** (`y=8500px`, `60%`): Active landmark `Ready for another dose?` · sticky/fixed elements: `4`
- **Step 06** (`y=10200px`, `72%`): Active landmark `Capabilities that scale with your vision.` · sticky/fixed elements: `4`
- **Step 07** (`y=13600px`, `96%`): Active landmark `Got a project in mind?` · sticky/fixed elements: `3`
- **Step 08** (`y=14131px`, `100%`): Active landmark `Got a project in mind?` · sticky/fixed elements: `4`

### Multi-Page Internal Route Map
- **Listing Route (`/case-studies`)**: `https://microdose.studio/case-studies` — H1: `Each dose blends aesthetics and function to craft...`, scrollHeight `6729px`, transition `MPA` (`1099ms`)
- **About Route (`/about`)**: `https://microdose.studio/about` — H1: `A perfectly calibrated dose. Right amount of craf...`, scrollHeight `10827px`, transition `direct` (`576ms`)
- **Listing Route (`/services`)**: `https://microdose.studio/services` — H1: `One team for strategy, design & build.`, scrollHeight `23139px`, transition `direct` (`384ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: microdose-studio (Microdose Studio - Design & Development Agency for Startups)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `microdose-studio` (**Microdose Studio - Design & Development Agency for Startups** — `https://microdose.studio/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0000ff`).
- **Identity & Domain Context**: Microdose Studio helps tech startups turn ideas into products through strategy, brand and product design, React/Next.js development, and...
- **Primary Substrate**: `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)), **Primary Ink**: `#0c152a`, **Accent / Highlight**: `#0000ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#0c152a` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Uses `Geist` across display (`We build AI-first products for start`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1530px` container bounds (`gap: 4px`, padding `195px`) with `cubic-bezier(0.87,0.45,0.33,0.88)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `microdose-studio` in your global stylesheet:

:root {
  /* Microdose Studio - Design & Development Agency for Startups (microdose-studio) — Live-Grounded CSS Variables */
  --color-black: #19171b; /* Canvas / Surface Token (microdose-studio) */
  --color-dark: #0c152a; /* Canvas / Surface Token (microdose-studio) */
  --color-muted: #6b6c71; /* Brand / Palette Token (microdose-studio) */
  --color-white: #ffffff; /* Canvas / Surface Token (microdose-studio) */
  --color-bg-dark: #121113; /* Canvas / Surface Token (microdose-studio) */
  --color-card-bg: #e8e8ec; /* Canvas / Surface Token (microdose-studio) */
  --color-blue-start: #1935d9; /* Brand / Palette Token (microdose-studio) */
  --color-blue-end: #2f2be2; /* Brand / Palette Token (microdose-studio) */
  --color-blue-border: #1f34c9; /* Brand / Palette Token (microdose-studio) */
  --color-footer-border: rgba(116, 84, 84, 0.15); /* Brand / Palette Token (microdose-studio) */
  --color-white-50: rgba(255, 255, 255, 0.5); /* Canvas / Surface Token (microdose-studio) */
  --color-grey-cool: #818a94; /* Brand / Palette Token (microdose-studio) */
  --font-primary: 'Geist', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; /* Brand / Palette Token (microdose-studio) */
  --font-accent: 'Metal', serif; /* Brand / Palette Token (microdose-studio) */
  --radius-lg: 16px; /* Elevation / Border Token (microdose-studio) */
  --radius-xl: 24px; /* Elevation / Border Token (microdose-studio) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `browser-default` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#0c152a` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#e8e8ec` — grounded in `var(--color-card-bg)` in `:root`
- **Interactive Accent / Highlight**: `#0000ff` — grounded in `.legal-block a:hover { color: blue }` (`#0000ff`)
- **Secondary / Muted Copy**: `#6b6c71` — grounded in `var(--color-muted)` in `:root`
- **Structural Hairline Border**: `#eae5e5` — grounded in `var(--color-footer-border)` in `:root` (`rgba(116, 84, 84, 0.15)`)
- **Variable Token (`--color-black`)**: `#19171b` — grounded in `var(--color-black)` in `:root`
- **Variable Token (`--color-bg-dark`)**: `#121113` — grounded in `var(--color-bg-dark)` in `:root`
- **Variable Token (`--color-blue-start`)**: `#1935d9` — grounded in `var(--color-blue-start)` in `:root`
- **Variable Token (`--color-blue-end`)**: `#2f2be2` — grounded in `var(--color-blue-end)` in `:root`
- **Variable Token (`--color-blue-border`)**: `#1f34c9` — grounded in `var(--color-blue-border)` in `:root`
- **Variable Token (`--color-grey-cool`)**: `#818a94` — grounded in `var(--color-grey-cool)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1530px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `195px` lateral canvas padding with `4px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1530px`, `gap: 4px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `195px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (min-width: 768px) and (max-width: 819px)`, `@media (max-width: 1640px)`, `@media (max-width: 1520px)`
- **Corner Radii**: `100px`, `var(--radius-pill)`, `6.25rem`, `1px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 72px`, `line-height: 80px`, `font-weight: 400`, `letter-spacing: -4.32px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 72px`, `line-height: 80px`, `font-weight: 400`, `letter-spacing: -4.32px`); rule `h2` (`font-size: 26px`, `line-height: 42px`, `letter-spacing: -1.56px`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `body` (`font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `microdose-studio` (`Microdose Studio - Design & Development Agency for Startups`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.nav> — `microdose-studio`)**:
   - DOM & Selectors: Landmark `<nav class="nav blur-fade-in">` (`1440x80px`) hosting `Microdose Studio - Design & Developm` navigation (`microdose .studio · About us 01 · Case Studies 02 · Services 03 · Labs 04`), DOM attributes (`data-scroll-indicator="home"`, `data-consent="deny"`, `data-consent="accept"`, `data-chrome="nav"`), and stylesheet rule `after { margin: 0; padding: 0; box-sizing: border-box; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.nav> — `microdose-studio`)` (`microdose-studio`) adapts across `@media (prefers-reduced-motion: reduce)`, `@media (min-width: 768px) and (max-width: 819px)`, `@media (max-width: 1640px)`, `@media (max-width: 1520px)` with `cubic-bezier(0.87,0.45,0.33,0.88)`, `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(0.43,0.98,0.87,1)` transitions and links `microdose .studio · About us 01 · Case Studies 02 · Services 03 · Labs 04`.
2. **Hero Stage & Focal Lead (<section.hero> — `We build AI-first products for sta`)**:
   - DOM & Selectors: Landmark `<section class="hero blur-fade-in">` presenting display lead `We build AI-first products for startups and enter...` and copy excerpt *"We use cookies to improve experience and performance of our websi"* over `#ffffff` canvas and `#0c152a` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#ffffff` background with `#0c152a` headline `We build AI-first products for startups and enter...`.
3. **Primary Showcase & Content Grid (<section.portfolio-carousel> — `W e b u i l d A I - f i r s t p r `)**:
   - DOM & Selectors: Landmark `<section class="portfolio-carousel">` rendering section `W e b u i l d A I - f i r s t p r o d u c t s f o...` with copy *"Accepting new projects"*, asset references (`favicon-96x96.png`, `favicon.ico`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `selection { background-color: var(--color-blue-start); color: var(--color-white); te... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.portfolio-carousel> — `W e b u i l d A I - f i r s t p r `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1530px`, `gap: 4px`) on desktop and Single-column vertical stack at `390px` viewport width with `195px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.about> — `O u r s e l e c t e d p r o j e c `)**:
   - DOM & Selectors: Landmark `<section class="about">` framing `O u r s e l e c t e d p r o j e c t s .` and `M o b i l e A p p f o r H y p e r P e r s o n a l...` (*"Your Design & Dev Partner."*) with `#e8e8ec` surface cards, `#0000ff` accents, and `html { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.about> — `O u r s e l e c t e d p r o j e c `)` uses `100px`, `var(--radius-pill)`, `6.25rem`, `1px` radii, `#0000ff` highlights, and assets (favicon-96x96.png, favicon.ico, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://microdose.studio/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Microdose Studio - Design & Deve` footer links (`microdose .studio · About us 01 · Case Studies 02 · Services 03 · Labs 04`), copy *"e n t e r p r i s e s ."*, and `#eae5e5` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://microdose.studio/`)` aligns to `1530px` (non-`@media` desktop container stylesheet rule) with `195px` lateral canvas padding with `4px` grid gap and attributes (data-scroll-indicator="home", data-consent="deny", data-consent="accept").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We use cookies to improve experience and performance of our website"*
- Copy Excerpt 2: *"Accepting new projects"*
- Copy Excerpt 3: *"Your Design & Dev Partner."*
- Copy Excerpt 4: *"e n t e r p r i s e s ."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.87,0.45,0.33,0.88)`, `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(0.43,0.98,0.87,1)`
- **Extracted Stylesheet Rules (`microdose-studio`)**:
- `after { margin: 0; padding: 0; box-sizing: border-box; }`
- `selection { background-color: var(--color-blue-start); color: var(--color-white); te... }`
- `html { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;... }`
- `html::-webkit-scrollbar { display: none; }`
- `.blur-fade-in { opacity: 0; }`
- **Per-Selector Transition Rules**:
- **Selector `.page-bg--fade`**: `transition: opacity 1.2s ease` extracted from `microdose-studio` stylesheet.
- **Selector `media (prefers-reduced-motion: re...`**: `transition: none` extracted from `microdose-studio` stylesheet.
- **Selector `.nav`**: `transition: background 0.3s` extracted from `microdose-studio` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.87,0.45,0.33,0.88)`)**: Governs interactive state transitions across `<nav.nav>` and `<section.portfolio-carousel>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `15031px` across 8 distinct viewport chapters using Lenis, GSAP/ScrollTrigger, WebGL/Canvas.
- **Vertical Chapter Sequence**: We build AI-first products... (0%) -> #about (6%) -> Unifying a Global GTM Analy... (30%) -> Designing modern experience... (42%) -> Ready for another dose? (60%) -> Capabilities that scale wit... (72%) -> Got a project in mind? (96%) -> Got a project in mind? (100%).
- **Multi-Page Routes**: Scaffold internal routes `/case-studies` (listing, MPA), `/about` (about, direct), `/services` (listing, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `microdose-studio`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | We build AI-first products for startups and e... | `4` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `6%` | #about | `5` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `4250px` | `30%` | Unifying a Global GTM Analytics Platform from... | `3` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5950px` | `42%` | Designing modern experience for a global diag... | `3` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `8500px` | `60%` | Ready for another dose? | `4` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `10200px` | `72%` | Capabilities that scale with your vision. | `4` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `13600px` | `96%` | Got a project in mind? | `3` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `14131px` | `100%` | Got a project in mind? | `4` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | We build AI-first products for startups a... | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `6344px` | `50%` | Ready for another dose? | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `12689px` | `100%` | Got a project in mind? | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://microdose.studio/case-studies` | Each dose blends aesthetics and funct... | `6729px` | `MPA` (`1099ms`) | [subpage-01-case-studies.webp](assets/subpage-01-case-studies.webp) |
| `2` | `about` | `https://microdose.studio/about` | A perfectly calibrated dose. Right am... | `10827px` | `direct` (`576ms`) | [subpage-02-about.webp](assets/subpage-02-about.webp) |
| `3` | `listing` | `https://microdose.studio/services` | One team for strategy, design & build. | `23139px` | `direct` (`384ms`) | [subpage-03-services.webp](assets/subpage-03-services.webp) |

