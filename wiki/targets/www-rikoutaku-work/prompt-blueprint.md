---
title: "UI Prompt Blueprint: www-rikoutaku-work"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-rikoutaku-work"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f0f0f7` / `#0000ff`)"
---

# UI Design System & Master Generation Blueprint: www-rikoutaku-work

> **Rikoutaku（リコウタク）— RI.Studio · Interaction & UI/UX Design Portfolio** (https://www.rikoutaku.work/) — Rikoutaku（リコウタク）のポートフォリオサイト「RI.Studio」。東京を拠点とするインタラクション／UI・UXデザイナー。3Dスクロール体験、アプリUI、Web、AR、モーションの作品集。Interaction & UI/UX Designer based in...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Rikoutaku（リコウタク）— RI.Studio · Interaction & UI/UX Design Portfolio** (`https://www.rikoutaku.work/`). Rikoutaku（リコウタク）のポートフォリオサイト「RI.Studio」。東京を拠点とするインタラクション／UI・UXデザイナー。3Dスクロール体験、アプリUI、Web、AR、モーションの作品集。Interaction & UI/UX Designer based in...
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f0f0f7` / `#0000ff`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f0f0f7` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#111219` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Inter` for display copy (`Rikoutaku（リコウタク）— RI.Studio · Intera`) with `Inter` and `SF Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 24px`, padding `64.8px`) with `cubic-bezier(.16,1,.3,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `64.8px` lateral canvas padding with `24px` grid gap.
- **Border Radius Scale**: `50%`, `999px`, `8px`, `6px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 24px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `64.8px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 820px)`, `@media (max-width: 700px)`, `@media (min-width: 1800px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f0f0f7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#111219` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e2e2eb` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.c2n-menu nav a:hover { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#e9e4d8` | `var(--text)` in `:root` |
| **Structural Hairline Border** | `#f2f2f8` | `var(--c2n-line)` in `:root` (`rgb(255 255 255 / 16%)`) |
| **Variable Token (`--ri-curtain-bg`)** | `#2e3bff` | `var(--ri-curtain-bg)` in `:root` |
| **Variable Token (`--bg`)** | `#0b0b0c` | `var(--bg)` in `:root` |
| **Variable Token (`--faint`)** | `#2a2926` | `var(--faint)` in `:root` |
| **Variable Token (`--accent`)** | `#ff3b24` | `var(--accent)` in `:root` |
| **Variable Token (`--accent-2`)** | `#d92c18` | `var(--accent-2)` in `:root` |
| **Variable Token (`--circle-outline`)** | `#505050` | `var(--circle-outline)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ri-ease` | `cubic-bezier(.16, 1, .3, 1)` | Motion / Easing Token |
| `--ri-ease-io` | `cubic-bezier(.76, 0, .24, 1)` | Motion / Easing Token |
| `--ri-ease-in` | `cubic-bezier(.7, 0, .84, 0)` | Motion / Easing Token |
| `--ri-curtain-bg` | `#2e3bff` | Canvas / Surface Token |
| `--ri-curtain-ink` | `#f0f0f7` | Typography Ink Token |
| `--ri-curtain-z` | `2147483000` | Design System Custom Token |
| `--bg` | `#0b0b0c` | Canvas / Surface Token |
| `--text` | `#e9e4d8` | Typography Ink Token |
| `--dim` | `#e9e4d8` | Color / Atmospheric Token |
| `--faint` | `#2a2926` | Color / Atmospheric Token |
| `--accent` | `#ff3b24` | Brand / Palette Token |
| `--accent-2` | `#d92c18` | Brand / Palette Token |
| `--circle-outline` | `#505050` | Elevation / Border Token |
| `--ease` | `cubic-bezier(.16, 1, .3, 1)` | Motion / Easing Token |
| `--ease-soft` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--pad` | `clamp(1.4rem, 2.4vw, 2.8rem)` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: `SF Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: normal`, `font-weight: 700`); rule `h1` (`font-size: clamp(29px,2.5vw,40px)`, `line-height: 1.36`, `letter-spacing: -.055em`, `font-weight: 500`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 64px`, `line-height: 67.2px`, `font-weight: 550`, `letter-spacing: -4.16px`); rule `h2` (`font-size: clamp(94px,10.2vw,164px)`, `line-height: .94`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 12px`, `line-height: 1.65`, `letter-spacing: -.01em`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.76,0,.24,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `body`**: `transition: background .8s var(--ease-soft)` extracted from `www-rikoutaku-work` stylesheet.
- **Selector `.experience-canvas`**: `transition: opacity 1.6s var(--ease-soft)` extracted from `www-rikoutaku-work` stylesheet.
- **Selector `.gb-btn`**: `transition: color .4s var(--ease),border-color .4s var(--ease),background...` extracted from `www-rikoutaku-work` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.c2n-header>` and `<section.c2n-hero>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Rikoutaku（リコウタク）— RI.Studio · Interaction  │
│ ====================================================================== │
│ [ <header.c2n-header> (1440x99px)     | 01 Intro ↗ · 02 About me ↗ · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.composition-two> (w=1440px)                   | │
│ | H1: Rikoutaku（リコウタク）— RI.Studio · Interaction & UI/UX...           | │
│ | Substrate: #f0f0f7 | Ink: #111219 | Accent: #0000ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.c2n-hero>) max-w: 1440px                   | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Beyond the frame. B e y o n  |  | Selectedwork(06) S e l e c t | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.c2n-thinking>) — MofuLog M o f u L o g     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.c2n-contact>) | https://www.rikoutaku.work/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 24px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.c2n-header>     ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.composition-two) — 390px Vertical Lead        | │
│ | H1: Rikoutaku（リコウタク）— RI.Studio · Interaction & UI/UX...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.c2n-hero>) — 1-Col Stack                  | │
│ | [ Item 1: Beyond the frame. B e y o n d t h e f r a m e . I...   ] | │
│ | [ Item 2: Selectedwork(06) S e l e c t e d w o r k ( 0 6 )       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.c2n-thinking>) — 1-Col (MofuLog M o f u L ) | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.c2n-contact>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.c2n-header> — `www-rikoutaku-work`)**:
   - Landmark `<header class="c2n-header c2n-navigation-simple">` (`1440x99px`) hosting `Rikoutaku（リコウタク）— RI.Studio · Intera` navigation (`01 Intro ↗ · 02 About me ↗ · 03 Projects ↗ · 04 Contact ↗`), DOM attributes (`data-composition="two"`, `data-c2n-room="hero"`, `data-engine="three.js r165"`, `data-motion-system="studio"`), and stylesheet rule `after { margin:0;padding:0;box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.composition-two> — `Rikoutaku（リコウタク）— RI.Studio · Inte`)**:
   - Landmark `<section class="composition-two">` presenting display lead `Rikoutaku（リコウタク）— RI.Studio · Interaction & UI/UX...` and copy excerpt *"Let’s create Let’s create something different. something differen"* over `#f0f0f7` canvas and `#111219` ink.
3. **Primary Showcase & Content Grid (<section.c2n-hero> — `Beyond the frame. B e y o n d t h `)**:
   - Landmark `<section class="c2n-hero">` rendering section `Beyond the frame. B e y o n d t h e f r a m e . I...` with copy *"INTERACTION & UI/UX DESIGN"*, asset references (`favicon.svg`, `theme-boot.js`, `2026-8-10-white.glb`, `fonts.googleapis.com`), and grid rule `selection { background:var(--accent);color:fff }`.
4. **Interactive Detail & Feature Matrix (<section.c2n-thinking> — `Selectedwork(06) S e l e c t e d w`)**:
   - Landmark `<section class="c2n-thinking c2n-paper">` framing `Selectedwork(06) S e l e c t e d w o r k ( 0 6 )` and `MofuLog M o f u L o g` (*"Let’s create L e t ’ s c r e a t e something different. s o m e t"*) with `#e2e2eb` surface cards, `#0000ff` accents, and `.light { --bg: ece6d8;--text: 1a1a18;--dim: 807c72;--faint: cdc6b4 }`.
5. **Colophon & Global Directory Footer (<footer.c2n-contact> — `https://www.rikoutaku.work/`)**:
   - Landmark `<footer class="c2n-contact c2n-paper">` anchoring `Rikoutaku（リコウタク）— RI.Studio · In` footer links (`01 Intro ↗ · 02 About me ↗ · 03 Projects ↗ · 04 Contact ↗`), copy *"Let’s create L e t ’ s c r e a t e"*, and `#f2f2f8` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-rikoutaku-work (Rikoutaku（リコウタク）— RI.Studio · Interaction & UI/UX Design Portfolio)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-rikoutaku-work` (**Rikoutaku（リコウタク）— RI.Studio · Interaction & UI/UX Design Portfolio** — `https://www.rikoutaku.work/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f0f0f7` / `#0000ff`).
- **Identity & Domain Context**: Rikoutaku（リコウタク）のポートフォリオサイト「RI.Studio」。東京を拠点とするインタラクション／UI・UXデザイナー。3Dスクロール体験、アプリUI、Web、AR、モーションの作品集。Interaction & UI/UX Designer based in...
- **Primary Substrate**: `#f0f0f7` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#111219`, **Accent / Highlight**: `#0000ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f0f0f7` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#111219` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Inter` for display copy (`Rikoutaku（リコウタク）— RI.Studio · Intera`) with `Inter` and `SF Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 24px`, padding `64.8px`) with `cubic-bezier(.16,1,.3,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-rikoutaku-work` in your global stylesheet:

:root {
  /* Rikoutaku（リコウタク）— RI.Studio · Interaction & UI/UX Design Portfolio (www-rikoutaku-work) — Live-Grounded CSS Variables */
  --ri-ease: cubic-bezier(.16, 1, .3, 1); /* Motion / Easing Token (www-rikoutaku-work) */
  --ri-ease-io: cubic-bezier(.76, 0, .24, 1); /* Motion / Easing Token (www-rikoutaku-work) */
  --ri-ease-in: cubic-bezier(.7, 0, .84, 0); /* Motion / Easing Token (www-rikoutaku-work) */
  --ri-curtain-bg: #2e3bff; /* Canvas / Surface Token (www-rikoutaku-work) */
  --ri-curtain-ink: #f0f0f7; /* Typography Ink Token (www-rikoutaku-work) */
  --ri-curtain-z: 2147483000; /* Design System Custom Token (www-rikoutaku-work) */
  --bg: #0b0b0c; /* Canvas / Surface Token (www-rikoutaku-work) */
  --text: #e9e4d8; /* Typography Ink Token (www-rikoutaku-work) */
  --dim: #e9e4d8; /* Color / Atmospheric Token (www-rikoutaku-work) */
  --faint: #2a2926; /* Color / Atmospheric Token (www-rikoutaku-work) */
  --accent: #ff3b24; /* Brand / Palette Token (www-rikoutaku-work) */
  --accent-2: #d92c18; /* Brand / Palette Token (www-rikoutaku-work) */
  --circle-outline: #505050; /* Elevation / Border Token (www-rikoutaku-work) */
  --ease: cubic-bezier(.16, 1, .3, 1); /* Motion / Easing Token (www-rikoutaku-work) */
  --ease-soft: cubic-bezier(.4, 0, .2, 1); /* Motion / Easing Token (www-rikoutaku-work) */
  --pad: clamp(1.4rem, 2.4vw, 2.8rem); /* Layout / Spatial Grid Token (www-rikoutaku-work) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f0f0f7` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#111219` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#e2e2eb` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#0000ff` — grounded in `.c2n-menu nav a:hover { color: blue }` (`#0000ff`)
- **Secondary / Muted Copy**: `#e9e4d8` — grounded in `var(--text)` in `:root`
- **Structural Hairline Border**: `#f2f2f8` — grounded in `var(--c2n-line)` in `:root` (`rgb(255 255 255 / 16%)`)
- **Variable Token (`--ri-curtain-bg`)**: `#2e3bff` — grounded in `var(--ri-curtain-bg)` in `:root`
- **Variable Token (`--bg`)**: `#0b0b0c` — grounded in `var(--bg)` in `:root`
- **Variable Token (`--faint`)**: `#2a2926` — grounded in `var(--faint)` in `:root`
- **Variable Token (`--accent`)**: `#ff3b24` — grounded in `var(--accent)` in `:root`
- **Variable Token (`--accent-2`)**: `#d92c18` — grounded in `var(--accent-2)` in `:root`
- **Variable Token (`--circle-outline`)**: `#505050` — grounded in `var(--circle-outline)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `64.8px` lateral canvas padding with `24px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 24px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `64.8px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 820px)`, `@media (max-width: 700px)`, `@media (min-width: 1800px)`
- **Corner Radii**: `50%`, `999px`, `8px`, `6px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SF Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 32px`, `line-height: normal`, `font-weight: 700`); rule `h1` (`font-size: clamp(29px,2.5vw,40px)`, `line-height: 1.36`, `letter-spacing: -.055em`, `font-weight: 500`)
- **H2 Section Rule**: live computed `h2` (`font-size: 64px`, `line-height: 67.2px`, `font-weight: 550`, `letter-spacing: -4.16px`); rule `h2` (`font-size: clamp(94px,10.2vw,164px)`, `line-height: .94`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 12px`, `line-height: 1.65`, `letter-spacing: -.01em`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-rikoutaku-work` (`Rikoutaku（リコウタク）— RI.Studio · Interaction & UI/UX Design Portfolio`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.c2n-header> — `www-rikoutaku-work`)**:
   - DOM & Selectors: Landmark `<header class="c2n-header c2n-navigation-simple">` (`1440x99px`) hosting `Rikoutaku（リコウタク）— RI.Studio · Intera` navigation (`01 Intro ↗ · 02 About me ↗ · 03 Projects ↗ · 04 Contact ↗`), DOM attributes (`data-composition="two"`, `data-c2n-room="hero"`, `data-engine="three.js r165"`, `data-motion-system="studio"`), and stylesheet rule `after { margin:0;padding:0;box-sizing:border-box }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.c2n-header> — `www-rikoutaku-work`)` (`www-rikoutaku-work`) adapts across `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 820px)`, `@media (max-width: 700px)`, `@media (min-width: 1800px)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.76,0,.24,1)` transitions and links `01 Intro ↗ · 02 About me ↗ · 03 Projects ↗ · 04 Contact ↗`.
2. **Hero Stage & Focal Lead (<section.composition-two> — `Rikoutaku（リコウタク）— RI.Studio · Inte`)**:
   - DOM & Selectors: Landmark `<section class="composition-two">` presenting display lead `Rikoutaku（リコウタク）— RI.Studio · Interaction & UI/UX...` and copy excerpt *"Let’s create Let’s create something different. something differen"* over `#f0f0f7` canvas and `#111219` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×844px` mobile) sets `#f0f0f7` background with `#111219` headline `Rikoutaku（リコウタク）— RI.Studio · Interaction & UI/UX...`.
3. **Primary Showcase & Content Grid (<section.c2n-hero> — `Beyond the frame. B e y o n d t h `)**:
   - DOM & Selectors: Landmark `<section class="c2n-hero">` rendering section `Beyond the frame. B e y o n d t h e f r a m e . I...` with copy *"INTERACTION & UI/UX DESIGN"*, asset references (`favicon.svg`, `theme-boot.js`, `2026-8-10-white.glb`, `fonts.googleapis.com`), and grid rule `selection { background:var(--accent);color:fff }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.c2n-hero> — `Beyond the frame. B e y o n d t h `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 24px`) on desktop and Single-column vertical stack at `390px` viewport width with `64.8px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.c2n-thinking> — `Selectedwork(06) S e l e c t e d w`)**:
   - DOM & Selectors: Landmark `<section class="c2n-thinking c2n-paper">` framing `Selectedwork(06) S e l e c t e d w o r k ( 0 6 )` and `MofuLog M o f u L o g` (*"Let’s create L e t ’ s c r e a t e something different. s o m e t"*) with `#e2e2eb` surface cards, `#0000ff` accents, and `.light { --bg: ece6d8;--text: 1a1a18;--dim: 807c72;--faint: cdc6b4 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.c2n-thinking> — `Selectedwork(06) S e l e c t e d w`)` uses `50%`, `999px`, `8px`, `6px` radii, `#0000ff` highlights, and assets (favicon.svg, theme-boot.js, 2026-8-10-white.glb).
5. **Colophon & Global Directory Footer (<footer.c2n-contact> — `https://www.rikoutaku.work/`)**:
   - DOM & Selectors: Landmark `<footer class="c2n-contact c2n-paper">` anchoring `Rikoutaku（リコウタク）— RI.Studio · In` footer links (`01 Intro ↗ · 02 About me ↗ · 03 Projects ↗ · 04 Contact ↗`), copy *"Let’s create L e t ’ s c r e a t e"*, and `#f2f2f8` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.c2n-contact> — `https://www.rikoutaku.work/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `64.8px` lateral canvas padding with `24px` grid gap and attributes (data-composition="two", data-c2n-room="hero", data-engine="three.js r165").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Let’s create Let’s create something different. something different."*
- Copy Excerpt 2: *"INTERACTION & UI/UX DESIGN"*
- Copy Excerpt 3: *"Let’s create L e t ’ s c r e a t e something different. s o m e t h i n g d i f f..."*
- Copy Excerpt 4: *"Let’s create L e t ’ s c r e a t e"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.76,0,.24,1)`
- **Extracted Stylesheet Rules (`www-rikoutaku-work`)**:
- `after { margin:0;padding:0;box-sizing:border-box }`
- `selection { background:var(--accent);color:fff }`
- `.light { --bg: ece6d8;--text: 1a1a18;--dim: 807c72;--faint: cdc6b4 }`
- `html { scroll-behavior:auto }`
- `html::-webkit-scrollbar { width:0;height:0;display:none }`
- **Per-Selector Transition Rules**:
- **Selector `body`**: `transition: background .8s var(--ease-soft)` extracted from `www-rikoutaku-work` stylesheet.
- **Selector `.experience-canvas`**: `transition: opacity 1.6s var(--ease-soft)` extracted from `www-rikoutaku-work` stylesheet.
- **Selector `.gb-btn`**: `transition: color .4s var(--ease),border-color .4s var(--ease),background...` extracted from `www-rikoutaku-work` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.c2n-header>` and `<section.c2n-hero>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-rikoutaku-work`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
