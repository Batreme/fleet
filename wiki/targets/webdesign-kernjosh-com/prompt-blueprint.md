---
title: "UI Prompt Blueprint: webdesign-kernjosh-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "webdesign-kernjosh-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 1
subpages_crawled: 0
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f5f1e6` / `#007aff`)"
---

# UI Design System & Master Generation Blueprint: webdesign-kernjosh-com

> **Josh Kern** (https://webdesign.kernjosh.com) — Josh Kern - webdesign and dev. Some work, info, and how to get in touch.

![Desktop Journey Filmstrip (1280x828)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x872)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Josh Kern** (`https://webdesign.kernjosh.com`). Josh Kern - webdesign and dev. Some work, info, and how to get in touch.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f5f1e6` / `#007aff`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f5f1e6` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0c0908` primary typography and `#007aff` accents.
  - **Grounded Typographic Hierarchy**: Uses `DM Sans` across display (`Hey my name is Josh and I cool websi`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1400px` container bounds (`gap: 12px`, padding `.45rem`) with `cubic-bezier(.22,1,.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×828px` (`assets/desktop-journey.webp`, `1` keyframes up to `y=0px` / doc `900px`), Mobile `390×872px` (`assets/mobile-journey.webp`, `1` keyframes).
- **Master Container Bounds**: `1400px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `.45rem` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `999px`, `6px`, `4px`, `1px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.45rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (width<=600px)`, `@media (width<=1000px)`, `@media (width<=560px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f1e6` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0c0908` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ece3cb` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#007aff` | `.mail-nav__btn { color: #007aff }` |
| **Secondary / Muted Copy** | `#3f3f3f` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#8b8983` | `.nico-batt { border: #8b8983 }` |
| **Variable Token (`--base-200`)** | `#e0dfd7` | `var(--base-200)` in `:root` |
| **Variable Token (`--base-300`)** | `#5f5f5f` | `var(--base-300)` in `:root` |
| **Variable Token (`--kuli-ground`)** | `#e6dfd0` | `var(--kuli-ground)` in `:root` |
| **Variable Token (`--buy-bg`)** | `#2a1d15` | `var(--buy-bg)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--base-100` | `#f5f1e6` | Color / Atmospheric Token |
| `--base-200` | `#e0dfd7` | Color / Atmospheric Token |
| `--base-300` | `#5f5f5f` | Color / Atmospheric Token |
| `--base-350` | `#3f3f3f` | Color / Atmospheric Token |
| `--base-400` | `#0c0908` | Color / Atmospheric Token |
| `--kuli-pad-top` | `clamp(8.5rem, 18vh, 11.5rem)` | Layout / Spatial Grid Token |
| `--kuli-thumb-h` | `clamp(3rem, 7vh, 4.5rem)` | Dimension / Scale Token |
| `--kuli-ground` | `#e6dfd0` | Color / Atmospheric Token |
| `--kuli-line-h` | `9px` | Dimension / Scale Token |
| `--buy-bg` | `#2a1d15` | Canvas / Surface Token |
| `--kuli-box-ink` | `6px` | Typography Ink Token |
| `--kuli-phone-ratio` | `720 / 1278` | Design System Custom Token |
| `--ease` | `cubic-bezier(.22, 1, .36, 1)` | Motion / Easing Token |
| `--ease-spring` | `cubic-bezier(.34, 1.56, .64, 1)` | Motion / Easing Token |
| `--frame-w` | `min(calc(62vh * 16 / 10), 88vw)` | Dimension / Scale Token |
| `--enter-op` | `1` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `DM Sans`.
- **Primary Body Stack**: `DM Sans`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 15.3px`, `line-height: 26.775px`, `font-weight: 400`); CSS variables `--about-font-display: "UglyDave", cursive`; rule `h1` (`font-size: clamp(.9rem,1.7vmin,1.1rem)`, `line-height: 1.75`, `font-weight: inherit`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: 26.4px`, `font-weight: 400`, `letter-spacing: -0.24px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--about-font-body: "DM Sans", sans-serif`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--about-font-label: "DM Sans", sans-serif`, `--about-label-size: .98rem`, `--about-label-tracking: -.005em`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(.33,1,.68,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.loader`**: `transition: opacity .12s` extracted from `webdesign-kernjosh-com` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none` extracted from `webdesign-kernjosh-com` stylesheet.
- **Selector `.loader .loading-hint`**: `transition: none` extracted from `webdesign-kernjosh-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<nav.nav>` and `<section.work-stage>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `900px`, deepest scrollY reached `0px` across `1` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Josh Kern                                  │
│ ====================================================================== │
│ [ <nav.nav> (1440x42px)               | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.desk> (w=1440px)                              | │
│ | H1: Hey my name is Josh and I cool websites :)                     | │
│ | Substrate: #f5f1e6 | Ink: #0c0908 | Accent: #007aff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.work-stage>) max-w: 1400px                 | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Getting to know you          |  | Building the site            | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.process-shell>) — Handover & going live    | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.legal-footer) | https://webdesign.kernjosh.com       │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.nav>               ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.desk>) — 390px Vertical Lead                  | │
│ | H1: Hey my name is Josh and I cool websites :)                     | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.work-stage>) — 1-Col Stack                | │
│ | [ Item 1: Getting to know you                                    ] | │
│ | [ Item 2: Building the site                                      ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.process-shell>) — 1-Col (Handover & going l)  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.legal-footer) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.nav> — `webdesign-kernjosh-com`)**:
   - Landmark `<nav class="nav">` (`1440x42px`) hosting `Josh Kern` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-landscape="primary"`, `data-back-pill`, `data-back-arrow-path`, `data-work-open`), and stylesheet rule `selection { color:0a0a0a;background:fff19a }`.
2. **Hero Stage & Focal Lead (<section.desk> — `Hey my name is Josh and I cool web`)**:
   - Landmark `<section class="desk">` presenting display lead `Hey my name is Josh and I cool websites :)` and copy excerpt *"I ask a lot of questions because I want the website to feel like "* over `#f5f1e6` canvas and `#0c0908` ink.
3. **Primary Showcase & Content Grid (<section.work-stage> — `Getting to know you`)**:
   - Landmark `<section class="work-stage">` rendering section `Getting to know you` with copy *"1 Getting to know you I ask a lot of questions because I want the"*, asset references (`favicon.png`, `apple-touch-icon.png`, `challenges.cloudflare.com`, `main-CwptEoZ4.js`), and grid rule `font-face { font-family:Outfit;src:url(/assets/Outfit-Variable-D6ftewdU.woff2)format... }`.
4. **Interactive Detail & Feature Matrix (<section.process-shell> — `Building the site`)**:
   - Landmark `<section class="process-shell">` framing `Building the site` and `Handover & going live` (*"I start exploring ideas for the landing page by throwing a lot of"*) with `#ece3cb` surface cards, `#007aff` accents, and `root { --base-100:f5f1e6;--base-200:e0dfd7;--base-300:5f5f5f;--base-350:3f3f3f;... }`.
5. **Colophon & Global Directory Footer (<footer.legal-footer> — `https://webdesign.kernjosh.com`)**:
   - Landmark `<footer class="legal-footer">` anchoring `Josh Kern` footer links (`Overview · Index · Archive · About · Contact`), copy *"3 Building the site I build everything with custom code, add"*, and `#8b8983` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Getting to know you` · sticky/fixed elements: `5`

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: webdesign-kernjosh-com (Josh Kern)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `webdesign-kernjosh-com` (**Josh Kern** — `https://webdesign.kernjosh.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5f1e6` / `#007aff`).
- **Identity & Domain Context**: Josh Kern - webdesign and dev. Some work, info, and how to get in touch.
- **Primary Substrate**: `#f5f1e6` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#0c0908`, **Accent / Highlight**: `#007aff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f5f1e6` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0c0908` primary typography and `#007aff` accents.
  - **Grounded Typographic Hierarchy**: Uses `DM Sans` across display (`Hey my name is Josh and I cool websi`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1400px` container bounds (`gap: 12px`, padding `.45rem`) with `cubic-bezier(.22,1,.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `webdesign-kernjosh-com` in your global stylesheet:

:root {
  /* Josh Kern (webdesign-kernjosh-com) — Live-Grounded CSS Variables */
  --base-100: #f5f1e6; /* Color / Atmospheric Token (webdesign-kernjosh-com) */
  --base-200: #e0dfd7; /* Color / Atmospheric Token (webdesign-kernjosh-com) */
  --base-300: #5f5f5f; /* Color / Atmospheric Token (webdesign-kernjosh-com) */
  --base-350: #3f3f3f; /* Color / Atmospheric Token (webdesign-kernjosh-com) */
  --base-400: #0c0908; /* Color / Atmospheric Token (webdesign-kernjosh-com) */
  --kuli-pad-top: clamp(8.5rem, 18vh, 11.5rem); /* Layout / Spatial Grid Token (webdesign-kernjosh-com) */
  --kuli-thumb-h: clamp(3rem, 7vh, 4.5rem); /* Dimension / Scale Token (webdesign-kernjosh-com) */
  --kuli-ground: #e6dfd0; /* Color / Atmospheric Token (webdesign-kernjosh-com) */
  --kuli-line-h: 9px; /* Dimension / Scale Token (webdesign-kernjosh-com) */
  --buy-bg: #2a1d15; /* Canvas / Surface Token (webdesign-kernjosh-com) */
  --kuli-box-ink: 6px; /* Typography Ink Token (webdesign-kernjosh-com) */
  --kuli-phone-ratio: 720 / 1278; /* Design System Custom Token (webdesign-kernjosh-com) */
  --ease: cubic-bezier(.22, 1, .36, 1); /* Motion / Easing Token (webdesign-kernjosh-com) */
  --ease-spring: cubic-bezier(.34, 1.56, .64, 1); /* Motion / Easing Token (webdesign-kernjosh-com) */
  --frame-w: min(calc(62vh * 16 / 10), 88vw); /* Dimension / Scale Token (webdesign-kernjosh-com) */
  --enter-op: 1; /* Design System Custom Token (webdesign-kernjosh-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f5f1e6` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#0c0908` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ece3cb` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#007aff` — grounded in `.mail-nav__btn { color: #007aff }`
- **Secondary / Muted Copy**: `#3f3f3f` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#8b8983` — grounded in `.nico-batt { border: #8b8983 }`
- **Variable Token (`--base-200`)**: `#e0dfd7` — grounded in `var(--base-200)` in `:root`
- **Variable Token (`--base-300`)**: `#5f5f5f` — grounded in `var(--base-300)` in `:root`
- **Variable Token (`--kuli-ground`)**: `#e6dfd0` — grounded in `var(--kuli-ground)` in `:root`
- **Variable Token (`--buy-bg`)**: `#2a1d15` — grounded in `var(--buy-bg)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×828px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×872px` (full-page live capture (872px), `390px` standard mobile width).
- **Container Max-Width**: `1400px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `.45rem` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.45rem` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (width<=600px)`, `@media (width<=1000px)`, `@media (width<=560px)`
- **Corner Radii**: `999px`, `6px`, `4px`, `1px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `DM Sans`
- **Body Font Stack**: `DM Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 15.3px`, `line-height: 26.775px`, `font-weight: 400`); CSS variables `--about-font-display: "UglyDave", cursive`; rule `h1` (`font-size: clamp(.9rem,1.7vmin,1.1rem)`, `line-height: 1.75`, `font-weight: inherit`)
- **H2 Section Rule**: live computed `h2` (`font-size: 24px`, `line-height: 26.4px`, `font-weight: 400`, `letter-spacing: -0.24px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--about-font-body: "DM Sans", sans-serif`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--about-font-label: "DM Sans", sans-serif`, `--about-label-size: .98rem`, `--about-label-tracking: -.005em`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `webdesign-kernjosh-com` (`Josh Kern`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.nav> — `webdesign-kernjosh-com`)**:
   - DOM & Selectors: Landmark `<nav class="nav">` (`1440x42px`) hosting `Josh Kern` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-landscape="primary"`, `data-back-pill`, `data-back-arrow-path`, `data-work-open`), and stylesheet rule `selection { color:0a0a0a;background:fff19a }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.nav> — `webdesign-kernjosh-com`)` (`webdesign-kernjosh-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (width<=600px)`, `@media (width<=1000px)`, `@media (width<=560px)` with `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(.33,1,.68,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.desk> — `Hey my name is Josh and I cool web`)**:
   - DOM & Selectors: Landmark `<section class="desk">` presenting display lead `Hey my name is Josh and I cool websites :)` and copy excerpt *"I ask a lot of questions because I want the website to feel like "* over `#f5f1e6` canvas and `#0c0908` ink.
   - Responsive Contract: Hero stage (`1280×828px` desktop / `390×872px` mobile) sets `#f5f1e6` background with `#0c0908` headline `Hey my name is Josh and I cool websites :)`.
3. **Primary Showcase & Content Grid (<section.work-stage> — `Getting to know you`)**:
   - DOM & Selectors: Landmark `<section class="work-stage">` rendering section `Getting to know you` with copy *"1 Getting to know you I ask a lot of questions because I want the"*, asset references (`favicon.png`, `apple-touch-icon.png`, `challenges.cloudflare.com`, `main-CwptEoZ4.js`), and grid rule `font-face { font-family:Outfit;src:url(/assets/Outfit-Variable-D6ftewdU.woff2)format... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.work-stage> — `Getting to know you`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `.45rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.process-shell> — `Building the site`)**:
   - DOM & Selectors: Landmark `<section class="process-shell">` framing `Building the site` and `Handover & going live` (*"I start exploring ideas for the landing page by throwing a lot of"*) with `#ece3cb` surface cards, `#007aff` accents, and `root { --base-100:f5f1e6;--base-200:e0dfd7;--base-300:5f5f5f;--base-350:3f3f3f;... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.process-shell> — `Building the site`)` uses `999px`, `6px`, `4px`, `1px` radii, `#007aff` highlights, and assets (favicon.png, apple-touch-icon.png, challenges.cloudflare.com).
5. **Colophon & Global Directory Footer (<footer.legal-footer> — `https://webdesign.kernjosh.com`)**:
   - DOM & Selectors: Landmark `<footer class="legal-footer">` anchoring `Josh Kern` footer links (`Overview · Index · Archive · About · Contact`), copy *"3 Building the site I build everything with custom code, add"*, and `#8b8983` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.legal-footer> — `https://webdesign.kernjosh.com`)` aligns to `1400px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `.45rem` lateral canvas padding with `12px` grid gap and attributes (data-landscape="primary", data-back-pill, data-back-arrow-path).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"I ask a lot of questions because I want the website to feel like something that is..."*
- Copy Excerpt 2: *"1 Getting to know you I ask a lot of questions because I want the website to feel..."*
- Copy Excerpt 3: *"I start exploring ideas for the landing page by throwing a lot of stuff at the wal..."*
- Copy Excerpt 4: *"3 Building the site I build everything with custom code, adding animations and int..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(.33,1,.68,1)`
- **Extracted Stylesheet Rules (`webdesign-kernjosh-com`)**:
- `selection { color:0a0a0a;background:fff19a }`
- `font-face { font-family:Outfit;src:url(/assets/Outfit-Variable-D6ftewdU.woff2)format... }`
- `root { --base-100:f5f1e6;--base-200:e0dfd7;--base-300:5f5f5f;--base-350:3f3f3f;... }`
- `html { -webkit-text-size-adjust:100%;-moz-text-size-adjust:100%;text-size-adjus... }`
- `body { background:var(--base-100);color:var(--base-400);overscroll-behavior:non... }`
- **Per-Selector Transition Rules**:
- **Selector `.loader`**: `transition: opacity .12s` extracted from `webdesign-kernjosh-com` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none` extracted from `webdesign-kernjosh-com` stylesheet.
- **Selector `.loader .loading-hint`**: `transition: none` extracted from `webdesign-kernjosh-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<nav.nav>` and `<section.work-stage>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `900px` across 1 distinct viewport chapters.
- **Vertical Chapter Sequence**: Getting to know you (0%).

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `webdesign-kernjosh-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Getting to know you | `5` | [desktop-step-01.webp](assets/desktop-step-01.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Getting to know you | [mobile-step-01.webp](assets/mobile-step-01.webp) |

