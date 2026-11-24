---
title: "UI Prompt Blueprint: www-remyshoots-co-za"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-remyshoots-co-za"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: wheel
desktop_keyframes: 1
subpages_crawled: 1
http_status: 200
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#111111` canvas, `#ffffff` ink, `#808080` accent)"
---

# UI Design System & Master Generation Blueprint: www-remyshoots-co-za

> **Remy Shoots** (https://www.remyshoots.co.za/) — Documenting emotion, movement and meaning. Since ©2016 — the photography portfolio of Remy.

![Desktop Journey Filmstrip (1280x828)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x872)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Remy Shoots** (`https://www.remyshoots.co.za/`). Documenting emotion, movement and meaning. Since ©2016 — the photography portfolio of Remy.
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#111111` canvas, `#ffffff` ink, `#808080` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#111111` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#808080` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Helvetica Neue` for display copy (`REMYSHOOTS®`) with `Roboto Mono` and `Roboto Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 20px`, padding `var(--nav-caret-lane)`) with `cubic-bezier(.4,0,.15,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×828px` (`assets/desktop-journey.webp`, `1` keyframes up to `y=0px` / doc `900px`), Mobile `390×872px` (`assets/mobile-journey.webp`, `1` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` viewport stage).
- **Canvas Lateral Padding & Spacing**: `var(--nav-caret-lane)` lateral canvas padding with `20px` grid gap.
- **Border Radius Scale**: `50%`, `1000px`, `999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 20px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--nav-caret-lane)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:760px)`, `@media (min-width:761px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1101px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#111111` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#2e2e2e` | `var(--panel)` in `:root` |
| **Interactive Accent / Highlight** | `#808080` | `.studio-chrome .nav-works-link { color: gray }` (`#808080`) |
| **Secondary / Muted Copy** | `#ff3131` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#2e2e2e` | `.gesture-tutorial { border: #2e2e2e }` |
| **Variable Token (`--cream`)** | `#fcf8ef` | `var(--cream)` in `:root` |
| **Variable Token (`--gray-150`)** | `#cbc7c2` | `var(--gray-150)` in `:root` |
| **Variable Token (`--gray-200`)** | `#b2aeab` | `var(--gray-200)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cream` | `#fcf8ef` | Color / Atmospheric Token |
| `--gray-150` | `#cbc7c2` | Color / Atmospheric Token |
| `--gray-200` | `#b2aeab` | Color / Atmospheric Token |
| `--red` | `#ff3131` | Color / Atmospheric Token |
| `--panel` | `#2e2e2e` | Color / Atmospheric Token |
| `--bg` | `#111` | Canvas / Surface Token |
| `--stage-lift` | `24px` | Dimension / Scale Token |
| `--vcaret-x` | `calc(8.33vw + 219px)` | Dimension / Scale Token |
| `--vig-size` | `45%` | Layout / Spatial Grid Token |
| `--vig-radius` | `min(114vh, 114vw)` | Elevation / Border Token |
| `--vig-open` | `1.2` | Design System Custom Token |
| `--nav-caret-lane` | `28px` | Layout / Spatial Grid Token |
| `--nav-caret-gap` | `8px` | Layout / Spatial Grid Token |
| `--nav-caret-size` | `.9em` | Layout / Spatial Grid Token |
| `--vt-stage-dur` | `1.6s` | Motion / Timing Token |
| `--vt-stage-ease` | `cubic-bezier(.887, 0, .113, 1)` | Motion / Easing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Helvetica Neue`.
- **Primary Body Stack**: `Roboto Mono`.
- **Technical / Metadata Stack**: `Roboto Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 93.6px`, `line-height: 93.6px`, `font-weight: 800`, `letter-spacing: -2.808px`).
- **Section Heading (`H2`)**: observed font-size ladder: `93.6px`, `16px`, `24.336px`, `15.12px`, `clamp(13px,1.05vw,18px)`.
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 600`); rule `p` (`font-size: clamp(13px,1.05vw,18px)`, `line-height: 1.2`, `letter-spacing: -.04em`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 15.12px`, `line-height: 18.144px`, `font-weight: 600`, `letter-spacing: -0.3024px`); CSS variables `--vt-meta-dur: .45s`, `--vt-meta-out-delay: 0s`, `--vt-meta-in-delay: .45s`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.15,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.887,0,.113,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.hand-control`**: `transition: opacity .25s` extracted from `www-remyshoots-co-za` stylesheet.
- **Selector `.vticker`**: `transition: transform .45s cubic-bezier(.4,0,.15,1)` extracted from `www-remyshoots-co-za` stylesheet.
- **Selector `.vticker-caret`**: `transition: transform .45s cubic-bezier(.4,0,.15,1)` extracted from `www-remyshoots-co-za` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.15,1)`)**: Governs interactive state transitions across `<header.chrome>` and `<div.chrome-slider>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<div.view-slider>` and `<div.chrome-slider>` interactive targets.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `wheel` (max document height `900px`, deepest scrollY reached `0px` across `1` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Route Transition Architecture**: First internal navigation (`/about`) measured as `direct` in `1155ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Remy Shoots                                │
│ ====================================================================== │
│ [ <header.chrome> (1360x0px)          | works(21) works(21) · motion ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.view-slider> (w=1440px)                           | │
│ | H1: REMYSHOOTS®                                                    | │
│ | Substrate: #111111 | Ink: #ffffff | Accent: #808080                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.chrome-slider>) max-w: 1440px                  | │
│ | +------------------------------+  +------------------------------+ | │
│ | | documenting emotion, documen |  | documenting emotion, documen | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<div.chrome>) — documenting emotion,                | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.logo>       ) | https://www.remyshoots.co.za/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 20px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.chrome>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<div.view-slider>) — 390px Vertical Lead               | │
│ | H1: REMYSHOOTS®                                                    | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<div.chrome-slider>) — 1-Col Stack                 | │
│ | [ Item 1: documenting emotion, documenting emotion, moveme       ] | │
│ | [ Item 2: documenting emotion, documenting emotion,              ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<div.chrome>) — 1-Col (documenting emotio)           | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.logo>       ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.chrome> — `www-remyshoots-co-za`)**:
   - Landmark `<header class="chrome">` (`1360x0px`) hosting `Remy Shoots` navigation (`works(21) works(21) · motion(8) motion(8) · About About · contact contact`), DOM attributes (`data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`, `data-disable-auto-track="1"`), and stylesheet rule `nter_d7e32889-module__94mdca__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<div.view-slider> — `REMYSHOOTS®`)**:
   - Landmark `<div class="view-slider">` presenting display lead `REMYSHOOTS®` and copy excerpt *"documenting emotion, documenting emotion, movement and meaning. m"* over `#111111` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<div.chrome-slider> — `documenting emotion, documenting e`)**:
   - Landmark `<div class="chrome-slider">` rendering section `documenting emotion, documenting emotion, moveme` with copy *"documenting emotion, documenting emotion,"*, asset references (`2f13ad8e538108e0-s.p.22iyan98j1_2...`, `83afe278b6a6bb3c-s.p.2bn3s6zvc0dy...`, `under-armour.svg`, `playhead.svg`), and grid rule `inter_d7e32889-module__94mdca__va... { --font-sans:"Inter", "Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<div.chrome> — `documenting emotion, documenting e`)**:
   - Landmark `<div class="chrome">` framing `documenting emotion, documenting emotion,` and `documenting emotion,` (*"documenting emotion,"*) with `#2e2e2e` surface cards, `#808080` accents, and `mono_955658b9-module__SfQagW__cla... { font-family:Roboto Mono,Roboto Mono Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.logo> — `https://www.remyshoots.co.za/`)**:
   - Landmark `<footer class="logo">` anchoring `Remy Shoots` footer links (`works(21) works(21) · motion(8) motion(8) · About About · contact contact`), copy *"movement and meaning. movement and meaning."*, and `#2e2e2e` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `REMYSHOOTS®` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **About Route (`/about`)**: `https://www.remyshoots.co.za/about` — H1: `MULTI-AWARD WINNING PRODUCTION STUDIO. SINCE ©2016`, scrollHeight `900px`, transition `direct` (`1155ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-remyshoots-co-za (Remy Shoots)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-remyshoots-co-za` (**Remy Shoots** — `https://www.remyshoots.co.za/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#111111` canvas, `#ffffff` ink, `#808080` accent).
- **Identity & Domain Context**: Documenting emotion, movement and meaning. Since ©2016 — the photography portfolio of Remy.
- **Primary Substrate**: `#111111` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#808080`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#111111` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#808080` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Helvetica Neue` for display copy (`REMYSHOOTS®`) with `Roboto Mono` and `Roboto Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 20px`, padding `var(--nav-caret-lane)`) with `cubic-bezier(.4,0,.15,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-remyshoots-co-za` in your global stylesheet:

:root {
  /* Remy Shoots (www-remyshoots-co-za) — Live-Grounded CSS Variables */
  --cream: #fcf8ef; /* Color / Atmospheric Token (www-remyshoots-co-za) */
  --gray-150: #cbc7c2; /* Color / Atmospheric Token (www-remyshoots-co-za) */
  --gray-200: #b2aeab; /* Color / Atmospheric Token (www-remyshoots-co-za) */
  --red: #ff3131; /* Color / Atmospheric Token (www-remyshoots-co-za) */
  --panel: #2e2e2e; /* Color / Atmospheric Token (www-remyshoots-co-za) */
  --bg: #111; /* Canvas / Surface Token (www-remyshoots-co-za) */
  --stage-lift: 24px; /* Dimension / Scale Token (www-remyshoots-co-za) */
  --vcaret-x: calc(8.33vw + 219px); /* Dimension / Scale Token (www-remyshoots-co-za) */
  --vig-size: 45%; /* Layout / Spatial Grid Token (www-remyshoots-co-za) */
  --vig-radius: min(114vh, 114vw); /* Elevation / Border Token (www-remyshoots-co-za) */
  --vig-open: 1.2; /* Design System Custom Token (www-remyshoots-co-za) */
  --nav-caret-lane: 28px; /* Layout / Spatial Grid Token (www-remyshoots-co-za) */
  --nav-caret-gap: 8px; /* Layout / Spatial Grid Token (www-remyshoots-co-za) */
  --nav-caret-size: .9em; /* Layout / Spatial Grid Token (www-remyshoots-co-za) */
  --vt-stage-dur: 1.6s; /* Motion / Timing Token (www-remyshoots-co-za) */
  --vt-stage-ease: cubic-bezier(.887, 0, .113, 1); /* Motion / Easing Token (www-remyshoots-co-za) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#111111` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#2e2e2e` — grounded in `var(--panel)` in `:root`
- **Interactive Accent / Highlight**: `#808080` — grounded in `.studio-chrome .nav-works-link { color: gray }` (`#808080`)
- **Secondary / Muted Copy**: `#ff3131` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#2e2e2e` — grounded in `.gesture-tutorial { border: #2e2e2e }`
- **Variable Token (`--cream`)**: `#fcf8ef` — grounded in `var(--cream)` in `:root`
- **Variable Token (`--gray-150`)**: `#cbc7c2` — grounded in `var(--gray-150)` in `:root`
- **Variable Token (`--gray-200`)**: `#b2aeab` — grounded in `var(--gray-200)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×828px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×872px` (full-page live capture (872px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` viewport stage)
- **Padding & Gutters**: `var(--nav-caret-lane)` lateral canvas padding with `20px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 20px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--nav-caret-lane)` horizontal padding
- **Media Queries**: `@media (max-width:760px)`, `@media (min-width:761px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1101px)`
- **Corner Radii**: `50%`, `1000px`, `999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Helvetica Neue`
- **Body Font Stack**: `Roboto Mono`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 93.6px`, `line-height: 93.6px`, `font-weight: 800`, `letter-spacing: -2.808px`)
- **H2 Section Rule**: observed font-size ladder: `93.6px`, `16px`, `24.336px`, `15.12px`, `clamp(13px,1.05vw,18px)`
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 600`); rule `p` (`font-size: clamp(13px,1.05vw,18px)`, `line-height: 1.2`, `letter-spacing: -.04em`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 15.12px`, `line-height: 18.144px`, `font-weight: 600`, `letter-spacing: -0.3024px`); CSS variables `--vt-meta-dur: .45s`, `--vt-meta-out-delay: 0s`, `--vt-meta-in-delay: .45s`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-remyshoots-co-za` (`Remy Shoots`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.chrome> — `www-remyshoots-co-za`)**:
   - DOM & Selectors: Landmark `<header class="chrome">` (`1360x0px`) hosting `Remy Shoots` navigation (`works(21) works(21) · motion(8) motion(8) · About About · contact contact`), DOM attributes (`data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`, `data-disable-auto-track="1"`), and stylesheet rule `nter_d7e32889-module__94mdca__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.chrome> — `www-remyshoots-co-za`)` (`www-remyshoots-co-za`) adapts across `@media (max-width:760px)`, `@media (min-width:761px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1101px)` with `cubic-bezier(.4,0,.15,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.887,0,.113,1)` transitions and links `works(21) works(21) · motion(8) motion(8) · About About · contact contact`.
2. **Hero Stage & Focal Lead (<div.view-slider> — `REMYSHOOTS®`)**:
   - DOM & Selectors: Landmark `<div class="view-slider">` presenting display lead `REMYSHOOTS®` and copy excerpt *"documenting emotion, documenting emotion, movement and meaning. m"* over `#111111` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1280×828px` desktop / `390×872px` mobile) sets `#111111` background with `#ffffff` headline `REMYSHOOTS®`.
3. **Primary Showcase & Content Grid (<div.chrome-slider> — `documenting emotion, documenting e`)**:
   - DOM & Selectors: Landmark `<div class="chrome-slider">` rendering section `documenting emotion, documenting emotion, moveme` with copy *"documenting emotion, documenting emotion,"*, asset references (`2f13ad8e538108e0-s.p.22iyan98j1_2...`, `83afe278b6a6bb3c-s.p.2bn3s6zvc0dy...`, `under-armour.svg`, `playhead.svg`), and grid rule `inter_d7e32889-module__94mdca__va... { --font-sans:"Inter", "Inter Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.chrome-slider> — `documenting emotion, documenting e`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 20px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--nav-caret-lane)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.chrome> — `documenting emotion, documenting e`)**:
   - DOM & Selectors: Landmark `<div class="chrome">` framing `documenting emotion, documenting emotion,` and `documenting emotion,` (*"documenting emotion,"*) with `#2e2e2e` surface cards, `#808080` accents, and `mono_955658b9-module__SfQagW__cla... { font-family:Roboto Mono,Roboto Mono Fallback;font-style:normal }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.chrome> — `documenting emotion, documenting e`)` uses `50%`, `1000px`, `999px` radii, `#808080` highlights, and assets (2f13ad8e538108e0-s.p.22iyan98j1_2..., 83afe278b6a6bb3c-s.p.2bn3s6zvc0dy..., under-armour.svg).
5. **Colophon & Global Directory Footer (<footer.logo> — `https://www.remyshoots.co.za/`)**:
   - DOM & Selectors: Landmark `<footer class="logo">` anchoring `Remy Shoots` footer links (`works(21) works(21) · motion(8) motion(8) · About About · contact contact`), copy *"movement and meaning. movement and meaning."*, and `#2e2e2e` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.logo> — `https://www.remyshoots.co.za/`)` aligns to `1440px` (full-bleed `100%` viewport stage) with `var(--nav-caret-lane)` lateral canvas padding with `20px` grid gap and attributes (data-precedence="next", data-sdkn="@vercel/analytics/next", data-sdkv="2.0.1").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"documenting emotion, documenting emotion, movement and meaning. movement and meaning."*
- Copy Excerpt 2: *"documenting emotion, documenting emotion,"*
- Copy Excerpt 3: *"documenting emotion,"*
- Copy Excerpt 4: *"movement and meaning. movement and meaning."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.15,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.887,0,.113,1)`
- **Extracted Stylesheet Rules (`www-remyshoots-co-za`)**:
- `nter_d7e32889-module__94mdca__cla... { font-family:Inter,Inter Fallback;font-style:normal }`
- `inter_d7e32889-module__94mdca__va... { --font-sans:"Inter", "Inter Fallback" }`
- `mono_955658b9-module__SfQagW__cla... { font-family:Roboto Mono,Roboto Mono Fallback;font-style:normal }`
- `mono_955658b9-module__SfQagW__var... { --font-mono:"Roboto Mono", "Roboto Mono Fallback" }`
- `root { --cream:fcf8ef;--gray-150:cbc7c2;--gray-200:b2aeab;--red:ff3131;--panel:... }`
- **Per-Selector Transition Rules**:
- **Selector `.hand-control`**: `transition: opacity .25s` extracted from `www-remyshoots-co-za` stylesheet.
- **Selector `.vticker`**: `transition: transform .45s cubic-bezier(.4,0,.15,1)` extracted from `www-remyshoots-co-za` stylesheet.
- **Selector `.vticker-caret`**: `transition: transform .45s cubic-bezier(.4,0,.15,1)` extracted from `www-remyshoots-co-za` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.15,1)`)**: Governs interactive state transitions across `<header.chrome>` and `<div.chrome-slider>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<div.view-slider>` and `<div.chrome-slider>` interactive targets.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `wheel` vertical progression up to `900px` across 1 distinct viewport chapters.
- **Vertical Chapter Sequence**: REMYSHOOTS® (0%).
- **Multi-Page Routes**: Scaffold internal routes `/about` (about, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-remyshoots-co-za`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | REMYSHOOTS® | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | REMYSHOOTS® | [mobile-step-01.webp](assets/mobile-step-01.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `about` | `https://www.remyshoots.co.za/about` | MULTI-AWARD WINNING PRODUCTION STUDIO... | `900px` | `direct` (`1155ms`) | [subpage-01-about.webp](assets/subpage-01-about.webp) |

