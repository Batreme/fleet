---
title: "UI Prompt Blueprint: white-desert-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "white-desert-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1f2a44` ink, `#0000ff` accent)"
---

# UI Design System & Master Generation Blueprint: white-desert-com

> **Luxury Adventures in Antarctica · White Desert** (https://white-desert.com/) — White Desert is the world’s leading luxury Antarctic expedition company, offering once-in-a-lifetime journeys to the South Pole and Emper...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Luxury Adventures in Antarctica · White Desert** (`https://white-desert.com/`). White Desert is the world’s leading luxury Antarctic expedition company, offering once-in-a-lifetime journeys to the South Pole and Emper...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1f2a44` ink, `#0000ff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1f2a44` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Oswald` for display copy (`ANTARCTICA`) with `Inter Tight` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: var(--spacing-md)`, padding `var(--size-3)`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (live computed `body` `max-width`).
- **Canvas Lateral Padding & Spacing**: `var(--size-3)` lateral canvas padding with `var(--spacing-md)` grid gap.
- **Border Radius Scale**: `2px`, `var(--radius-sm)`, `var(--radius-0125)`, `8px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: var(--spacing-md)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--size-3)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:768px)`, `@media (max-width:767px)`, `@media (max-width:540px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1f2a44` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f5f5f5` | `.global-flyout_content-item { background-color: #f5f5f5 }` |
| **Interactive Accent / Highlight** | `#0000ff` | `.nav-link { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#a8acb3` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#1f2330` | `var(--border)` in `:root` |
| **Variable Token (`--surface`)** | `#12141a` | `var(--surface)` in `:root` |
| **Variable Token (`--primary`)** | `#6aa5ff` | `var(--primary)` in `:root` |
| **Variable Token (`--primary-contrast`)** | `#0b0c0f` | `var(--primary-contrast)` in `:root` |
| **Variable Token (`--black`)** | `#000000` | `var(--black)` in `:root` |
| **Variable Token (`--dark-bg`)** | `#090b10` | `var(--dark-bg)` in `:root` |
| **Variable Token (`--wd_deep-blue`)** | `#0e1118` | `var(--wd_deep-blue)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#fff` | Canvas / Surface Token |
| `--surface` | `#12141a` | Canvas / Surface Token |
| `--text` | `var(--wd_dark-blue)` | Typography Ink Token |
| `--quote-accent` | `var(--WD_Dark-Blue,#1f2a44)` | Brand / Palette Token |
| `--muted` | `#a8acb3` | Color / Atmospheric Token |
| `--primary` | `#6aa5ff` | Brand / Palette Token |
| `--primary-contrast` | `#0b0c0f` | Brand / Palette Token |
| `--border` | `#1f2330` | Elevation / Border Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--black` | `#000` | Canvas / Surface Token |
| `--black-faded` | `rgba(0,0,0,.5)` | Canvas / Surface Token |
| `--dark-bg` | `#090b10` | Canvas / Surface Token |
| `--background` | `var(--bg)` | Canvas / Surface Token |
| `--foreground` | `var(--text)` | Typography Ink Token |
| `--wd_dark-blue` | `#1f2a44` | Canvas / Surface Token |
| `--wd_deep-blue` | `#0e1118` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Oswald`.
- **Primary Body Stack**: `Inter Tight`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 256px`, `line-height: 256px`, `font-weight: 400`); rule `h1` (`font-size: var(--size-375)`, `line-height: 100%`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 90px`, `line-height: normal`, `font-weight: 500`); rule `h2` (`font-size: var(--size-2)`, `line-height: var(--lh-120)`, `font-weight: 500`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 14px`, `line-height: 1.4`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.5,1,.89,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.card-flick_image:after`**: `transition: opacity .4s` extracted from `white-desert-com` stylesheet.
- **Selector `.card-flick_image img`**: `transition: transform .6s cubic-bezier(.4,0,.2,1)` extracted from `white-desert-com` stylesheet.
- **Selector `.cookie-banner`**: `transition: transform 1s cubic-bezier(.4,0,.2,1)` extracted from `white-desert-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.lenis>` and `<section.tall-parallax-banner>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Luxury Adventures in Antarctica · White De │
│ ====================================================================== │
│ [ <nav.lenis> (1440x80px)             | Rates · Enquire · Home · Enq ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.padding-top-large-bottom-me (w=1440px)        | │
│ | H1: ANTARCTICA                                                     | │
│ | Substrate: #ffffff | Ink: #1f2a44 | Accent: #0000ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.tall-parallax-ban) max-w: 1440px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Antarctica                   |  | Vast, majestic and unimagina | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.bg-white>) — Baby Penguins & Blue          | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.custom-curso) | https://white-desert.com/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--sp)   │
│ ====================================================================== │
│ [ HEADER BAR (<nav.lenis>             ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.padding-top-lar) — 390px Vertical Lead        | │
│ | H1: ANTARCTICA                                                     | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.tall-parallax) — 1-Col Stack              | │
│ | [ Item 1: Antarctica                                             ] | │
│ | [ Item 2: Vast, majestic and unimaginably beautiful — setti...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.bg-white>) — 1-Col (Baby Penguins & Bl)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.custom-curso) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.lenis> — `white-desert-com`)**:
   - Landmark `<nav class="lenis">` (`1440x80px`) hosting `Luxury Adventures in Antarctica · Wh` navigation (`Rates · Enquire · Home · Enquire now · Dates & Prices`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.basic-banner_bg { z-index:0;position:absolute;top:0;bottom:0;left:0;right:0 }`.
2. **Hero Stage & Focal Lead (<section.padding-top-large-bottom-medium> — `ANTARCTICA`)**:
   - Landmark `<section class="padding-top-large-bottom-medium m-pb-625">` presenting display lead `ANTARCTICA` and copy excerpt *"Luxury and adventure in the most remote place on Earth"* over `#ffffff` canvas and `#1f2a44` ink.
3. **Primary Showcase & Content Grid (<section.tall-parallax-banner> — `Antarctica`)**:
   - Landmark `<section class="tall-parallax-banner">` rendering section `Antarctica` with copy *"The Last Continent"*, asset references (`cabcbbbe485680be.css`, `7e7f4251c3582625.css`, `5dd7b716df5564d7.css`, `112bdbe21ebfd0e0.css`), and grid rule `.basic-banner_overlay { z-index:1;background-color:rgba(0,0,0,.2);position:absolute;top:0;bottom... }`.
4. **Interactive Detail & Feature Matrix (<section.bg-white> — `Vast, majestic and unimaginably be`)**:
   - Landmark `<section class="padding-top-large-bottom-medium bg-white">` framing `Vast, majestic and unimaginably beautiful — setti...` and `Baby Penguins & Blue Tunnels` (*"Between November and February, during the short polar summer, we "*) with `#f5f5f5` surface cards, `#0000ff` accents, and `.basic-banner_content { z-index:2;width:100%;color:var(--white);text-align:center;position:relative }`.
5. **Colophon & Global Directory Footer (<footer.custom-cursor_dot> — `https://white-desert.com/`)**:
   - Landmark `<footer class="custom-cursor_dot">` anchoring `Luxury Adventures in Antarctica ` footer links (`Rates · Enquire · Home · Enquire now · Dates & Prices`), copy *"Witness the Emperor chicks as they take their first steps an"*, and `#1f2330` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: white-desert-com (Luxury Adventures in Antarctica · White Desert)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `white-desert-com` (**Luxury Adventures in Antarctica · White Desert** — `https://white-desert.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1f2a44` ink, `#0000ff` accent).
- **Identity & Domain Context**: White Desert is the world’s leading luxury Antarctic expedition company, offering once-in-a-lifetime journeys to the South Pole and Emper...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#1f2a44`, **Accent / Highlight**: `#0000ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1f2a44` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Oswald` for display copy (`ANTARCTICA`) with `Inter Tight` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: var(--spacing-md)`, padding `var(--size-3)`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `white-desert-com` in your global stylesheet:

:root {
  /* Luxury Adventures in Antarctica · White Desert (white-desert-com) — Live-Grounded CSS Variables */
  --bg: #fff; /* Canvas / Surface Token (white-desert-com) */
  --surface: #12141a; /* Canvas / Surface Token (white-desert-com) */
  --text: var(--wd_dark-blue); /* Typography Ink Token (white-desert-com) */
  --quote-accent: var(--WD_Dark-Blue,#1f2a44); /* Brand / Palette Token (white-desert-com) */
  --muted: #a8acb3; /* Color / Atmospheric Token (white-desert-com) */
  --primary: #6aa5ff; /* Brand / Palette Token (white-desert-com) */
  --primary-contrast: #0b0c0f; /* Brand / Palette Token (white-desert-com) */
  --border: #1f2330; /* Elevation / Border Token (white-desert-com) */
  --white: #fff; /* Canvas / Surface Token (white-desert-com) */
  --black: #000; /* Canvas / Surface Token (white-desert-com) */
  --black-faded: rgba(0,0,0,.5); /* Canvas / Surface Token (white-desert-com) */
  --dark-bg: #090b10; /* Canvas / Surface Token (white-desert-com) */
  --background: var(--bg); /* Canvas / Surface Token (white-desert-com) */
  --foreground: var(--text); /* Typography Ink Token (white-desert-com) */
  --wd_dark-blue: #1f2a44; /* Canvas / Surface Token (white-desert-com) */
  --wd_deep-blue: #0e1118; /* Color / Atmospheric Token (white-desert-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#1f2a44` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f5f5f5` — grounded in `.global-flyout_content-item { background-color: #f5f5f5 }`
- **Interactive Accent / Highlight**: `#0000ff` — grounded in `.nav-link { color: blue }` (`#0000ff`)
- **Secondary / Muted Copy**: `#a8acb3` — grounded in `var(--muted)` in `:root`
- **Structural Hairline Border**: `#1f2330` — grounded in `var(--border)` in `:root`
- **Variable Token (`--surface`)**: `#12141a` — grounded in `var(--surface)` in `:root`
- **Variable Token (`--primary`)**: `#6aa5ff` — grounded in `var(--primary)` in `:root`
- **Variable Token (`--primary-contrast`)**: `#0b0c0f` — grounded in `var(--primary-contrast)` in `:root`
- **Variable Token (`--black`)**: `#000000` — grounded in `var(--black)` in `:root`
- **Variable Token (`--dark-bg`)**: `#090b10` — grounded in `var(--dark-bg)` in `:root`
- **Variable Token (`--wd_deep-blue`)**: `#0e1118` — grounded in `var(--wd_deep-blue)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (live computed `body` `max-width`)
- **Padding & Gutters**: `var(--size-3)` lateral canvas padding with `var(--spacing-md)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: var(--spacing-md)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--size-3)` horizontal padding
- **Media Queries**: `@media (max-width:768px)`, `@media (max-width:767px)`, `@media (max-width:540px)`, `@media (min-width:768px)`
- **Corner Radii**: `2px`, `var(--radius-sm)`, `var(--radius-0125)`, `8px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Oswald`
- **Body Font Stack**: `Inter Tight`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 256px`, `line-height: 256px`, `font-weight: 400`); rule `h1` (`font-size: var(--size-375)`, `line-height: 100%`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 90px`, `line-height: normal`, `font-weight: 500`); rule `h2` (`font-size: var(--size-2)`, `line-height: var(--lh-120)`, `font-weight: 500`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 14px`, `line-height: 1.4`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `white-desert-com` (`Luxury Adventures in Antarctica · White Desert`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.lenis> — `white-desert-com`)**:
   - DOM & Selectors: Landmark `<nav class="lenis">` (`1440x80px`) hosting `Luxury Adventures in Antarctica · Wh` navigation (`Rates · Enquire · Home · Enquire now · Dates & Prices`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.basic-banner_bg { z-index:0;position:absolute;top:0;bottom:0;left:0;right:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.lenis> — `white-desert-com`)` (`white-desert-com`) adapts across `@media (max-width:768px)`, `@media (max-width:767px)`, `@media (max-width:540px)`, `@media (min-width:768px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.5,1,.89,1)` transitions and links `Rates · Enquire · Home · Enquire now · Dates & Prices`.
2. **Hero Stage & Focal Lead (<section.padding-top-large-bottom-medium> — `ANTARCTICA`)**:
   - DOM & Selectors: Landmark `<section class="padding-top-large-bottom-medium m-pb-625">` presenting display lead `ANTARCTICA` and copy excerpt *"Luxury and adventure in the most remote place on Earth"* over `#ffffff` canvas and `#1f2a44` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#1f2a44` headline `ANTARCTICA`.
3. **Primary Showcase & Content Grid (<section.tall-parallax-banner> — `Antarctica`)**:
   - DOM & Selectors: Landmark `<section class="tall-parallax-banner">` rendering section `Antarctica` with copy *"The Last Continent"*, asset references (`cabcbbbe485680be.css`, `7e7f4251c3582625.css`, `5dd7b716df5564d7.css`, `112bdbe21ebfd0e0.css`), and grid rule `.basic-banner_overlay { z-index:1;background-color:rgba(0,0,0,.2);position:absolute;top:0;bottom... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.tall-parallax-banner> — `Antarctica`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: var(--spacing-md)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--size-3)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.bg-white> — `Vast, majestic and unimaginably be`)**:
   - DOM & Selectors: Landmark `<section class="padding-top-large-bottom-medium bg-white">` framing `Vast, majestic and unimaginably beautiful — setti...` and `Baby Penguins & Blue Tunnels` (*"Between November and February, during the short polar summer, we "*) with `#f5f5f5` surface cards, `#0000ff` accents, and `.basic-banner_content { z-index:2;width:100%;color:var(--white);text-align:center;position:relative }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.bg-white> — `Vast, majestic and unimaginably be`)` uses `2px`, `var(--radius-sm)`, `var(--radius-0125)`, `8px` radii, `#0000ff` highlights, and assets (cabcbbbe485680be.css, 7e7f4251c3582625.css, 5dd7b716df5564d7.css).
5. **Colophon & Global Directory Footer (<footer.custom-cursor_dot> — `https://white-desert.com/`)**:
   - DOM & Selectors: Landmark `<footer class="custom-cursor_dot">` anchoring `Luxury Adventures in Antarctica ` footer links (`Rates · Enquire · Home · Enquire now · Dates & Prices`), copy *"Witness the Emperor chicks as they take their first steps an"*, and `#1f2330` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.custom-cursor_dot> — `https://white-desert.com/`)` aligns to `1440px` (live computed `body` `max-width`) with `var(--size-3)` lateral canvas padding with `var(--spacing-md)` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Luxury and adventure in the most remote place on Earth"*
- Copy Excerpt 2: *"The Last Continent"*
- Copy Excerpt 3: *"Between November and February, during the short polar summer, we fly guests and sc..."*
- Copy Excerpt 4: *"Witness the Emperor chicks as they take their first steps and explore the ethereal..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.5,1,.89,1)`
- **Extracted Stylesheet Rules (`white-desert-com`)**:
- `.basic-banner_bg { z-index:0;position:absolute;top:0;bottom:0;left:0;right:0 }`
- `.basic-banner_overlay { z-index:1;background-color:rgba(0,0,0,.2);position:absolute;top:0;bottom... }`
- `.basic-banner_content { z-index:2;width:100%;color:var(--white);text-align:center;position:relative }`
- `.basic-banner_layout { width:100% }`
- `.basic-banner_inner { align-items:center;gap:var(--spacing-md);flex-direction:column;display:flex }`
- **Per-Selector Transition Rules**:
- **Selector `.card-flick_image:after`**: `transition: opacity .4s` extracted from `white-desert-com` stylesheet.
- **Selector `.card-flick_image img`**: `transition: transform .6s cubic-bezier(.4,0,.2,1)` extracted from `white-desert-com` stylesheet.
- **Selector `.cookie-banner`**: `transition: transform 1s cubic-bezier(.4,0,.2,1)` extracted from `white-desert-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.lenis>` and `<section.tall-parallax-banner>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `white-desert-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
