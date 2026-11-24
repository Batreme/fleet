---
title: "UI Prompt Blueprint: relevovinco-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "relevovinco-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 1
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#d4b08f` canvas, `#36261a` ink, `#6b4c34` accent)"
---

# UI Design System & Master Generation Blueprint: relevovinco-com

> **Relevo & Vinco — inkless packaging, pressed into the board** (https://relevovinco.com/) — Relevo & Vinco is an inkless packaging workshop in Porto. We emboss, deboss, die-cut and fold raw board so a brand is something people fe...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Relevo & Vinco — inkless packaging, pressed into the board** (`https://relevovinco.com/`). Relevo & Vinco is an inkless packaging workshop in Porto. We emboss, deboss, die-cut and fold raw board so a brand is something people fe...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#d4b08f` canvas, `#36261a` ink, `#6b4c34` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#d4b08f` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#36261a` primary typography and `#6b4c34` accents.
  - **Grounded Typographic Hierarchy**: Uses `Instrument Sans` across display (`STAND OUT. PRESS IN.`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 8px`, padding `4px`) with `cubic-bezier(.3,.7,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=14400px` / doc `17763px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `4px` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `6px`, `var(--radius-1)`, `var(--radius-2)`, `var(--radius-3)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:900px)`, `@media (prefers-reduced-motion:no-preference)`, `@media (max-width:767px)`, `@media (prefers-reduced-motion:no-preference)and (max-width:767px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#d4b08f` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#36261a` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#47331f` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#6b4c34` | live computed `h2` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#6b4c34` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#6b4c34` | hairline divider derived from live computed `h2` `color` (`computed_styles.json`) |
| **Variable Token (`--color-3`)** | `#f7e8d2` | `var(--color-3)` in `:root` |
| **Variable Token (`--color-6`)** | `#1f140b` | `var(--color-6)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-1` | `#d4b08f` | Brand / Palette Token |
| `--color-2` | `#36261a` | Brand / Palette Token |
| `--color-3` | `#f7e8d2` | Brand / Palette Token |
| `--color-4` | `#6b4c34` | Brand / Palette Token |
| `--color-5` | `#47331f` | Brand / Palette Token |
| `--color-6` | `#1f140b` | Brand / Palette Token |
| `--font-1` | `"Gabarito", "Gabarito Fallback", "Arial", sans-serif` | Typography / Scale Token |
| `--font-2` | `"Instrument Sans", "Instrument Sans Fallback", "Arial", sans-serif` | Typography / Scale Token |
| `--radius-1` | `6px` | Elevation / Border Token |
| `--radius-2` | `50%` | Elevation / Border Token |
| `--radius-3` | `clamp(18px, 2.4vw, 34px)` | Elevation / Border Token |
| `--shadow-7` | `1px 1px 0 color-mix(in srgb, var(--color-3) 75%, transparent)` | Elevation / Border Token |
| `--shadow-14` | `10px 16px 18px color-mix(in srgb, var(--color-6) 32%, transparent)` | Elevation / Border Token |
| `--space-1` | `clamp(20px, 6.5vw, 96px)` | Layout / Spatial Grid Token |
| `--space-2` | `clamp(96px, 15vh, 180px)` | Layout / Spatial Grid Token |
| `--hero-cap` | `min(16vh, 11.2vw)` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Instrument Sans`.
- **Primary Body Stack**: `Instrument Sans`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 34px`, `line-height: 52.7px`, `font-weight: 700`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 86.4px`, `line-height: 79.488px`, `font-weight: 700`, `letter-spacing: 0.864px`).
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 26.35px`, `font-weight: 400`); rule `p` (`font-size: clamp(26px,2.8vw,42px)`, `line-height: 1.12`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 26.35px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.3,.7,.2,1)`, `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.2,.75,.15,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `relevovinco-com` stylesheet.
- **Selector `.m-btn`**: `transition: box-shadow .22s cubic-bezier(.3,.7,.2,1),transform .22s cubic-...` extracted from `relevovinco-com` stylesheet.
- **Selector `.m-btn::after`**: `transition: opacity .22s` extracted from `relevovinco-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.3,.7,.2,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.relief-defs__shade>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `17763px`, deepest scrollY reached `14400px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`.
- **Hover Physics (`primary_cta` · `Order a sample kit`)**: `transform`: `none` -> `matrix(1, 0, 0, 1, 0, 0)`; `boxShadow`: `color(srgb 0.968627 0.9...` -> `oklab(0.937149 0.007213...` (`transition-duration: 0.22s, 0.22s`, `timing: cubic-bezier(0.3, 0.7, 0.2, 1), cubic-bezier(0.3, 0.7, 0.2, 1)`).
- **Interactive Control Probe (`accordion`)**: Tested `CAN A BOX CARRY A BRAND WITH NO INK?` (diff `3.076`).
- **Route Transition Architecture**: First internal navigation (`/pt/`) measured as `direct` in `863ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Relevo & Vinco — inkless packaging, presse │
│ ====================================================================== │
│ [ <header.lenis> (1440x68px)          | Finishes · Process · Work ·  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relief-defs> (w=1440px)                       | │
│ | H1: STAND OUT. PRESS IN.                                           | │
│ | Substrate: #d4b08f | Ink: #36261a | Accent: #6b4c34                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.relief-defs__shad) max-w: 1440px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Stand out. Press in.         |  | Ink fades. Foil peels. Press | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.nav__bar>) — Six ways to say it wi         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.m-text-3>   ) | https://relevovinco.com/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.lenis>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.relief-defs>) — 390px Vertical Lead           | │
│ | H1: STAND OUT. PRESS IN.                                           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.relief-defs__) — 1-Col Stack              | │
│ | [ Item 1: Stand out. Press in.                                   ] | │
│ | [ Item 2: Ink fades. Foil peels. Pressure stays.                 ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.nav__bar>) — 1-Col (Six ways to say it)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.m-text-3>   ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `relevovinco-com`)**:
   - Landmark `<header class="lenis">` (`1440x68px`) hosting `Relevo & Vinco — inkless packaging, ` navigation (`Finishes · Process · Work · Boards · Contact`), DOM attributes (`data-fonts`, `data-part="layers"`, `data-part="tokens"`, `data-part="base"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.relief-defs> — `STAND OUT. PRESS IN.`)**:
   - Landmark `<section class="relief-defs">` presenting display lead `STAND OUT. PRESS IN.` and copy excerpt *"Relevo & Vinco is an inkless packaging workshop in Porto. We embo"* over `#d4b08f` canvas and `#36261a` ink.
3. **Primary Showcase & Content Grid (<section.relief-defs__shade> — `Stand out. Press in.`)**:
   - Landmark `<section class="relief-defs__shade">` rendering section `Stand out. Press in.` with copy *"Order a sample kit"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `gabarito-a94f9001.woff2`), and grid rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`.
4. **Interactive Detail & Feature Matrix (<section.nav__bar> — `Ink fades. Foil peels. Pressure st`)**:
   - Landmark `<section class="nav__bar">` framing `Ink fades. Foil peels. Pressure stays.` and `Six ways to say it without ink` (*"Every box we make carries its brand in the board itself: raised w"*) with `#47331f` surface cards, `#6b4c34` accents, and `img { display:block;max-width:100%;height:auto }`.
5. **Colophon & Global Directory Footer (<footer.m-text-3> — `https://relevovinco.com/`)**:
   - Landmark `<footer class="m-text-3">` anchoring `Relevo & Vinco — inkless packagi` footer links (`Finishes · Process · Work · Boards · Contact`), copy *"Nothing to scuff off in transit and nothing to separate at t"*, and `#6b4c34` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `STAND OUT. PRESS IN.` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `5%`): Active landmark `STAND OUT. PRESS IN.` · sticky/fixed elements: `2`
- **Step 03** (`y=3400px`, `20%`): Active landmark `SIX WAYS TO SAY IT WITHOUT INK` · sticky/fixed elements: `1`
- **Step 04** (`y=5950px`, `35%`): Active landmark `FLAT TO FINISHED IN FOUR MOVES` · sticky/fixed elements: `2`
- **Step 05** (`y=8500px`, `50%`): Active landmark `HALDE CANDLES` · sticky/fixed elements: `1`
- **Step 06** (`y=11050px`, `66%`): Active landmark `#navigation` · sticky/fixed elements: `1`
- **Step 07** (`y=13600px`, `81%`): Active landmark `A DISC OF EACH, PUNCHED FOR YOU` · sticky/fixed elements: `1`
- **Step 08** (`y=14400px`, `85%`): Active landmark `PILOT RUN` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Other Route (`/pt/`)**: `https://relevovinco.com/pt/` — H1: `SALTA À VISTA. MARCA FUNDO.`, scrollHeight `18008px`, transition `direct` (`863ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: relevovinco-com (Relevo & Vinco — inkless packaging, pressed into the board)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `relevovinco-com` (**Relevo & Vinco — inkless packaging, pressed into the board** — `https://relevovinco.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#d4b08f` canvas, `#36261a` ink, `#6b4c34` accent).
- **Identity & Domain Context**: Relevo & Vinco is an inkless packaging workshop in Porto. We emboss, deboss, die-cut and fold raw board so a brand is something people fe...
- **Primary Substrate**: `#d4b08f` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#36261a`, **Accent / Highlight**: `#6b4c34`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#d4b08f` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#36261a` primary typography and `#6b4c34` accents.
  - **Grounded Typographic Hierarchy**: Uses `Instrument Sans` across display (`STAND OUT. PRESS IN.`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 8px`, padding `4px`) with `cubic-bezier(.3,.7,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `relevovinco-com` in your global stylesheet:

:root {
  /* Relevo & Vinco — inkless packaging, pressed into the board (relevovinco-com) — Live-Grounded CSS Variables */
  --color-1: #d4b08f; /* Brand / Palette Token (relevovinco-com) */
  --color-2: #36261a; /* Brand / Palette Token (relevovinco-com) */
  --color-3: #f7e8d2; /* Brand / Palette Token (relevovinco-com) */
  --color-4: #6b4c34; /* Brand / Palette Token (relevovinco-com) */
  --color-5: #47331f; /* Brand / Palette Token (relevovinco-com) */
  --color-6: #1f140b; /* Brand / Palette Token (relevovinco-com) */
  --font-1: "Gabarito", "Gabarito Fallback", "Arial", sans-serif; /* Typography / Scale Token (relevovinco-com) */
  --font-2: "Instrument Sans", "Instrument Sans Fallback", "Arial", sans-serif; /* Typography / Scale Token (relevovinco-com) */
  --radius-1: 6px; /* Elevation / Border Token (relevovinco-com) */
  --radius-2: 50%; /* Elevation / Border Token (relevovinco-com) */
  --radius-3: clamp(18px, 2.4vw, 34px); /* Elevation / Border Token (relevovinco-com) */
  --shadow-7: 1px 1px 0 color-mix(in srgb, var(--color-3) 75%, transparent); /* Elevation / Border Token (relevovinco-com) */
  --shadow-14: 10px 16px 18px color-mix(in srgb, var(--color-6) 32%, transparent); /* Elevation / Border Token (relevovinco-com) */
  --space-1: clamp(20px, 6.5vw, 96px); /* Layout / Spatial Grid Token (relevovinco-com) */
  --space-2: clamp(96px, 15vh, 180px); /* Layout / Spatial Grid Token (relevovinco-com) */
  --hero-cap: min(16vh, 11.2vw); /* Dimension / Scale Token (relevovinco-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#d4b08f` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#36261a` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#47331f` — grounded in live computed `section` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#6b4c34` — grounded in live computed `h2` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#6b4c34` — grounded in live computed `h2` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#6b4c34` — grounded in hairline divider derived from live computed `h2` `color` (`computed_styles.json`)
- **Variable Token (`--color-3`)**: `#f7e8d2` — grounded in `var(--color-3)` in `:root`
- **Variable Token (`--color-6`)**: `#1f140b` — grounded in `var(--color-6)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `4px` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding
- **Media Queries**: `@media (max-width:900px)`, `@media (prefers-reduced-motion:no-preference)`, `@media (max-width:767px)`, `@media (prefers-reduced-motion:no-preference)and (max-width:767px)`
- **Corner Radii**: `6px`, `var(--radius-1)`, `var(--radius-2)`, `var(--radius-3)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `Instrument Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 34px`, `line-height: 52.7px`, `font-weight: 700`)
- **H2 Section Rule**: live computed `h2` (`font-size: 86.4px`, `line-height: 79.488px`, `font-weight: 700`, `letter-spacing: 0.864px`)
- **Body Copy Rule**: live computed `body` (`font-size: 17px`, `line-height: 26.35px`, `font-weight: 400`); rule `p` (`font-size: clamp(26px,2.8vw,42px)`, `line-height: 1.12`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 17px`, `line-height: 26.35px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `relevovinco-com` (`Relevo & Vinco — inkless packaging, pressed into the board`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `relevovinco-com`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` (`1440x68px`) hosting `Relevo & Vinco — inkless packaging, ` navigation (`Finishes · Process · Work · Boards · Contact`), DOM attributes (`data-fonts`, `data-part="layers"`, `data-part="tokens"`, `data-part="base"`), and stylesheet rule `after { box-sizing:border-box }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `relevovinco-com`)` (`relevovinco-com`) adapts across `@media (max-width:900px)`, `@media (prefers-reduced-motion:no-preference)`, `@media (max-width:767px)`, `@media (prefers-reduced-motion:no-preference)and (max-width:767px)` with `cubic-bezier(.3,.7,.2,1)`, `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.2,.75,.15,1)` transitions and links `Finishes · Process · Work · Boards · Contact`.
2. **Hero Stage & Focal Lead (<section.relief-defs> — `STAND OUT. PRESS IN.`)**:
   - DOM & Selectors: Landmark `<section class="relief-defs">` presenting display lead `STAND OUT. PRESS IN.` and copy excerpt *"Relevo & Vinco is an inkless packaging workshop in Porto. We embo"* over `#d4b08f` canvas and `#36261a` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#d4b08f` background with `#36261a` headline `STAND OUT. PRESS IN.`.
3. **Primary Showcase & Content Grid (<section.relief-defs__shade> — `Stand out. Press in.`)**:
   - DOM & Selectors: Landmark `<section class="relief-defs__shade">` rendering section `Stand out. Press in.` with copy *"Order a sample kit"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `gabarito-a94f9001.woff2`), and grid rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.relief-defs__shade> — `Stand out. Press in.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `4px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.nav__bar> — `Ink fades. Foil peels. Pressure st`)**:
   - DOM & Selectors: Landmark `<section class="nav__bar">` framing `Ink fades. Foil peels. Pressure stays.` and `Six ways to say it without ink` (*"Every box we make carries its brand in the board itself: raised w"*) with `#47331f` surface cards, `#6b4c34` accents, and `img { display:block;max-width:100%;height:auto }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.nav__bar> — `Ink fades. Foil peels. Pressure st`)` uses `6px`, `var(--radius-1)`, `var(--radius-2)`, `var(--radius-3)` radii, `#6b4c34` highlights, and assets (favicon.ico, favicon.svg, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.m-text-3> — `https://relevovinco.com/`)**:
   - DOM & Selectors: Landmark `<footer class="m-text-3">` anchoring `Relevo & Vinco — inkless packagi` footer links (`Finishes · Process · Work · Boards · Contact`), copy *"Nothing to scuff off in transit and nothing to separate at t"*, and `#6b4c34` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.m-text-3> — `https://relevovinco.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `4px` lateral canvas padding with `8px` grid gap and attributes (data-fonts, data-part="layers", data-part="tokens").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Relevo & Vinco is an inkless packaging workshop in Porto. We emboss, deboss, cut a..."*
- Copy Excerpt 2: *"Order a sample kit"*
- Copy Excerpt 3: *"Every box we make carries its brand in the board itself: raised where it should ca..."*
- Copy Excerpt 4: *"Nothing to scuff off in transit and nothing to separate at the recycling bin. The..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.3,.7,.2,1)`, `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.2,.75,.15,1)`
- **Extracted Stylesheet Rules (`relevovinco-com`)**:
- `after { box-sizing:border-box }`
- `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`
- `img { display:block;max-width:100%;height:auto }`
- `select { font:inherit;color:inherit }`
- `focus-visible { outline:3px solid var(--color-2);outline-offset:3px }`
- **Per-Selector Transition Rules**:
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `relevovinco-com` stylesheet.
- **Selector `.m-btn`**: `transition: box-shadow .22s cubic-bezier(.3,.7,.2,1),transform .22s cubic-...` extracted from `relevovinco-com` stylesheet.
- **Selector `.m-btn::after`**: `transition: opacity .22s` extracted from `relevovinco-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.3,.7,.2,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.relief-defs__shade>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `17763px` across 8 distinct viewport chapters using Lenis, GSAP/ScrollTrigger.
- **Vertical Chapter Sequence**: STAND OUT. PRESS IN. (0%) -> STAND OUT. PRESS IN. (5%) -> SIX WAYS TO SAY IT WITHOUT INK (20%) -> FLAT TO FINISHED IN FOUR MOVES (35%) -> HALDE CANDLES (50%) -> #navigation (66%) -> A DISC OF EACH, PUNCHED FOR... (81%) -> PILOT RUN (85%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `transform, boxShadow` with `0.22s, 0.22s cubic-bezier(0.3, 0.7, 0.2, 1), cubic-bezier(0.3, 0.7, 0.2, 1)`.
- **Multi-Page Routes**: Scaffold internal routes `/pt/` (other, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `relevovinco-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | STAND OUT. PRESS IN. | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `5%` | STAND OUT. PRESS IN. | `2` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `3400px` | `20%` | SIX WAYS TO SAY IT WITHOUT INK | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5950px` | `35%` | FLAT TO FINISHED IN FOUR MOVES | `2` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `8500px` | `50%` | HALDE CANDLES | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `11050px` | `66%` | #navigation | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `13600px` | `81%` | A DISC OF EACH, PUNCHED FOR YOU | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `14400px` | `85%` | PILOT RUN | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | STAND OUT. PRESS IN. | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `7200px` | `50%` | MORROW COFFEE | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `14400px` | `100%` | FEEL IT BEFORE YOU ORDER | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `other` | `https://relevovinco.com/pt/` | SALTA À VISTA. MARCA FUNDO. | `18008px` | `direct` (`863ms`) | [subpage-01-pt.webp](assets/subpage-01-pt.webp) |

