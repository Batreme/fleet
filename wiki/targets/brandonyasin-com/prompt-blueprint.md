---
title: "UI Prompt Blueprint: brandonyasin-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "brandonyasin-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#363229` canvas, `#c3beb1` ink, `#ffeb48` accent)"
---

# UI Design System & Master Generation Blueprint: brandonyasin-com

> **Brandon Yasin — Creative Director & Designer** (https://brandonyasin.com) — Brand, digital and spatial design within lifestyle and luxury. AI scales the production, not the craft. Based in Denmark, working globally.

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Brandon Yasin — Creative Director & Designer** (`https://brandonyasin.com`). Brand, digital and spatial design within lifestyle and luxury. AI scales the production, not the craft. Based in Denmark, working globally.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#363229` canvas, `#c3beb1` ink, `#ffeb48` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#363229` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#c3beb1` primary typography and `#ffeb48` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Neue Haas Unica Pro` for display copy (`archive`) with `Neue Haas Unica Pro` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `114.05vw` container bounds (`gap: 3rem`, padding `16px`) with `cubic-bezier(.645,.045,.355,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `114.05vw` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `16px` lateral canvas padding with `3rem` grid gap.
- **Border Radius Scale**: `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 114.05vw`, `gap: 3rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding.
- **Extracted CSS Media Queries**: `@media only screen and (width>=768px)`, `@media only screen and (width>=1025px)`, `@media only screen and (width>=1438px)`, `@media (width>=768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#363229` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#c3beb1` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.img-wrap:after { background-color: #000000 }` |
| **Interactive Accent / Highlight** | `#ffeb48` | `::-moz-placeholder { color: #ffeb48 }` |
| **Secondary / Muted Copy** | `#111111` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ffffff` | `:before { border: #ffffff }` |
| **Variable Token (`--color-bg`)** | `#f8f6f2` | `var(--color-bg)` in `:root` |
| **Variable Token (`--selection-bg`)** | `#443000` | `var(--selection-bg)` in `:root` |
| **Variable Token (`--color-green`)** | `#263b1c` | `var(--color-green)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-main` | `#111` | Brand / Palette Token |
| `--color-bg` | `#f8f6f2` | Canvas / Surface Token |
| `--selection-color` | `#111` | Brand / Palette Token |
| `--selection-bg` | `#44300033` | Canvas / Surface Token |
| `--focus-bg` | `var(--color-main)` | Canvas / Surface Token |
| `--focus-color` | `var(--color-bg)` | Brand / Palette Token |
| `--lvh` | `1vh` | Layout / Spatial Grid Token |
| `--svh` | `1vh` | Layout / Spatial Grid Token |
| `--img-over-opacity` | `0` | Design System Custom Token |
| `--bg-brightness` | `1` | Canvas / Surface Token |
| `--size` | `1168` | Layout / Spatial Grid Token |
| `--cut` | `100%` | Dimension / Scale Token |
| `--color-green` | `#263b1c` | Brand / Palette Token |
| `--line-x` | `0px` | Dimension / Scale Token |
| `--line-w` | `0` | Design System Custom Token |
| `--rows-tile-h` | `19.9rem` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Neue Haas Unica Pro`.
- **Primary Body Stack**: `Neue Haas Unica Pro`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 90.144px`, `line-height: 111.779px`, `font-weight: 400`, `letter-spacing: -3.60576px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40.032px`, `line-height: 48.0384px`, `font-weight: 400`, `letter-spacing: -1.60128px`).
- **Body Copy**: live computed `body` (`font-size: 15.984px`, `line-height: 20.7792px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 12px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.87,0,.13,1)`, `cubic-bezier(.33333,1,.66667,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `label`**: `transition: color .2s ease-out` extracted from `brandonyasin-com` stylesheet.
- **Selector `textarea[data-v-564d7e72]:-webkit...`**: `transition: background-color 10000000s step-end` extracted from `brandonyasin-com` stylesheet.
- **Selector `al-wrap textarea[data-v-564d7e72]...`**: `transition: background-color 10000000s step-end` extracted from `brandonyasin-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.645,.045,.355,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.header>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Brandon Yasin — Creative Director & Design │
│ ====================================================================== │
│ [ <header.header> (1440x84px)         | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.archive-container> (w=1440px)                 | │
│ | H1: archive                                                        | │
│ | Substrate: #363229 | Ink: #c3beb1 | Accent: #ffeb48                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.header>) max-w: 114.05vw                   | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Every project begins with ob |  | Brandon Awwwards Site of the | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.holder>) — Brandon Awwwards Site           | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.menu-tile>  ) | https://brandonyasin.com             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 3rem)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.header>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.archive-contain) — 390px Vertical Lead        | │
│ | H1: archive                                                        | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.header>) — 1-Col Stack                    | │
│ | [ Item 1: Every project begins with observation. Understan       ] | │
│ | [ Item 2: Brandon Awwwards Site of the day SOTD Yasin Site       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.holder>) — 1-Col (Brandon Awwwards S)       | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.menu-tile>  ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `brandonyasin-com`)**:
   - Landmark `<header class="header font-body-12">` (`1440x84px`) hosting `Brandon Yasin — Creative Director & ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-hid="initial-time-theme"`, `data-v-b4d4802c`, `data-slug="/archive"`, `data-menu-title-lag`), and stylesheet rule `.font-headline-1 { letter-spacing:-.04em;font:400 5.4rem/1.24 Neue Haas Unica Pro,Helvetica... }`.
2. **Hero Stage & Focal Lead (<section.archive-container> — `archive`)**:
   - Landmark `<section class="archive-container container">` presenting display lead `archive` and copy excerpt *"Every project begins with observation. Understanding the context,"* over `#363229` canvas and `#c3beb1` ink.
3. **Primary Showcase & Content Grid (<section.header> — `Every project begins with observat`)**:
   - Landmark `<section class="header about-header">` rendering section `Every project begins with observation. Understan` with copy *"Brandon Awwwards Site of the day SOTD Yasin Site of the day SOTD "*, asset references (`entry.CxmSBJR3.css`, `BUkWhEWa.js`, `DK3Fl9T5.js`, `IQKDJ7dv.js`), and grid rule `.font-headline-2 { letter-spacing:0;font:251 2.8rem/1.2 Neue Haas Unica Pro,Helvetica Neue,... }`.
4. **Interactive Detail & Feature Matrix (<section.holder> — `Brandon Awwwards Site of the day S`)**:
   - Landmark `<section class="holder">` framing `Brandon Awwwards Site of the day SOTD Yasin Site` and `Brandon Awwwards Site of the day SOTD` (*"Brandon Awwwards Site of the day SOTD"*) with `#000000` surface cards, `#ffeb48` accents, and `.font-headline-2-large { letter-spacing:0;font:251 5.5rem/1.24 Neue Haas Unica Pro,Helvetica Neue... }`.
5. **Colophon & Global Directory Footer (<footer.menu-tile> — `https://brandonyasin.com`)**:
   - Landmark `<footer class="menu-tile">` anchoring `Brandon Yasin — Creative Directo` footer links (`Overview · Index · Archive · About · Contact`), copy *"Site of the day SOTD"*, and `#ffffff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: brandonyasin-com (Brandon Yasin — Creative Director & Designer)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `brandonyasin-com` (**Brandon Yasin — Creative Director & Designer** — `https://brandonyasin.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#363229` canvas, `#c3beb1` ink, `#ffeb48` accent).
- **Identity & Domain Context**: Brand, digital and spatial design within lifestyle and luxury. AI scales the production, not the craft. Based in Denmark, working globally.
- **Primary Substrate**: `#363229` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#c3beb1`, **Accent / Highlight**: `#ffeb48`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#363229` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#c3beb1` primary typography and `#ffeb48` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Neue Haas Unica Pro` for display copy (`archive`) with `Neue Haas Unica Pro` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `114.05vw` container bounds (`gap: 3rem`, padding `16px`) with `cubic-bezier(.645,.045,.355,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `brandonyasin-com` in your global stylesheet:

:root {
  /* Brandon Yasin — Creative Director & Designer (brandonyasin-com) — Live-Grounded CSS Variables */
  --color-main: #111; /* Brand / Palette Token (brandonyasin-com) */
  --color-bg: #f8f6f2; /* Canvas / Surface Token (brandonyasin-com) */
  --selection-color: #111; /* Brand / Palette Token (brandonyasin-com) */
  --selection-bg: #44300033; /* Canvas / Surface Token (brandonyasin-com) */
  --focus-bg: var(--color-main); /* Canvas / Surface Token (brandonyasin-com) */
  --focus-color: var(--color-bg); /* Brand / Palette Token (brandonyasin-com) */
  --lvh: 1vh; /* Layout / Spatial Grid Token (brandonyasin-com) */
  --svh: 1vh; /* Layout / Spatial Grid Token (brandonyasin-com) */
  --img-over-opacity: 0; /* Design System Custom Token (brandonyasin-com) */
  --bg-brightness: 1; /* Canvas / Surface Token (brandonyasin-com) */
  --size: 1168; /* Layout / Spatial Grid Token (brandonyasin-com) */
  --cut: 100%; /* Dimension / Scale Token (brandonyasin-com) */
  --color-green: #263b1c; /* Brand / Palette Token (brandonyasin-com) */
  --line-x: 0px; /* Dimension / Scale Token (brandonyasin-com) */
  --line-w: 0; /* Design System Custom Token (brandonyasin-com) */
  --rows-tile-h: 19.9rem; /* Dimension / Scale Token (brandonyasin-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#363229` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#c3beb1` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#000000` — grounded in `.img-wrap:after { background-color: #000000 }`
- **Interactive Accent / Highlight**: `#ffeb48` — grounded in `::-moz-placeholder { color: #ffeb48 }`
- **Secondary / Muted Copy**: `#111111` — grounded in live computed `h2` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#ffffff` — grounded in `:before { border: #ffffff }`
- **Variable Token (`--color-bg`)**: `#f8f6f2` — grounded in `var(--color-bg)` in `:root`
- **Variable Token (`--selection-bg`)**: `#443000` — grounded in `var(--selection-bg)` in `:root`
- **Variable Token (`--color-green`)**: `#263b1c` — grounded in `var(--color-green)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `114.05vw` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `16px` lateral canvas padding with `3rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 114.05vw`, `gap: 3rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding
- **Media Queries**: `@media only screen and (width>=768px)`, `@media only screen and (width>=1025px)`, `@media only screen and (width>=1438px)`, `@media (width>=768px)`
- **Corner Radii**: `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Neue Haas Unica Pro`
- **Body Font Stack**: `Neue Haas Unica Pro`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 90.144px`, `line-height: 111.779px`, `font-weight: 400`, `letter-spacing: -3.60576px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 40.032px`, `line-height: 48.0384px`, `font-weight: 400`, `letter-spacing: -1.60128px`)
- **Body Copy Rule**: live computed `body` (`font-size: 15.984px`, `line-height: 20.7792px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12px`, `line-height: 12px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `brandonyasin-com` (`Brandon Yasin — Creative Director & Designer`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `brandonyasin-com`)**:
   - DOM & Selectors: Landmark `<header class="header font-body-12">` (`1440x84px`) hosting `Brandon Yasin — Creative Director & ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-hid="initial-time-theme"`, `data-v-b4d4802c`, `data-slug="/archive"`, `data-menu-title-lag`), and stylesheet rule `.font-headline-1 { letter-spacing:-.04em;font:400 5.4rem/1.24 Neue Haas Unica Pro,Helvetica... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `brandonyasin-com`)` (`brandonyasin-com`) adapts across `@media only screen and (width>=768px)`, `@media only screen and (width>=1025px)`, `@media only screen and (width>=1438px)`, `@media (width>=768px)` with `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.87,0,.13,1)`, `cubic-bezier(.33333,1,.66667,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.archive-container> — `archive`)**:
   - DOM & Selectors: Landmark `<section class="archive-container container">` presenting display lead `archive` and copy excerpt *"Every project begins with observation. Understanding the context,"* over `#363229` canvas and `#c3beb1` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#363229` background with `#c3beb1` headline `archive`.
3. **Primary Showcase & Content Grid (<section.header> — `Every project begins with observat`)**:
   - DOM & Selectors: Landmark `<section class="header about-header">` rendering section `Every project begins with observation. Understan` with copy *"Brandon Awwwards Site of the day SOTD Yasin Site of the day SOTD "*, asset references (`entry.CxmSBJR3.css`, `BUkWhEWa.js`, `DK3Fl9T5.js`, `IQKDJ7dv.js`), and grid rule `.font-headline-2 { letter-spacing:0;font:251 2.8rem/1.2 Neue Haas Unica Pro,Helvetica Neue,... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.header> — `Every project begins with observat`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 114.05vw`, `gap: 3rem`) on desktop and Single-column vertical stack at `390px` viewport width with `16px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.holder> — `Brandon Awwwards Site of the day S`)**:
   - DOM & Selectors: Landmark `<section class="holder">` framing `Brandon Awwwards Site of the day SOTD Yasin Site` and `Brandon Awwwards Site of the day SOTD` (*"Brandon Awwwards Site of the day SOTD"*) with `#000000` surface cards, `#ffeb48` accents, and `.font-headline-2-large { letter-spacing:0;font:251 5.5rem/1.24 Neue Haas Unica Pro,Helvetica Neue... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.holder> — `Brandon Awwwards Site of the day S`)` uses `50%` radii, `#ffeb48` highlights, and assets (entry.CxmSBJR3.css, BUkWhEWa.js, DK3Fl9T5.js).
5. **Colophon & Global Directory Footer (<footer.menu-tile> — `https://brandonyasin.com`)**:
   - DOM & Selectors: Landmark `<footer class="menu-tile">` anchoring `Brandon Yasin — Creative Directo` footer links (`Overview · Index · Archive · About · Contact`), copy *"Site of the day SOTD"*, and `#ffffff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.menu-tile> — `https://brandonyasin.com`)` aligns to `114.05vw` (non-`@media` desktop container stylesheet rule) with `16px` lateral canvas padding with `3rem` grid gap and attributes (data-hid="initial-time-theme", data-v-b4d4802c, data-slug="/archive").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Every project begins with observation. Understanding the context, people and brand..."*
- Copy Excerpt 2: *"Brandon Awwwards Site of the day SOTD Yasin Site of the day SOTD 24 OCT '26"*
- Copy Excerpt 3: *"Brandon Awwwards Site of the day SOTD"*
- Copy Excerpt 4: *"Site of the day SOTD"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.87,0,.13,1)`, `cubic-bezier(.33333,1,.66667,1)`
- **Extracted Stylesheet Rules (`brandonyasin-com`)**:
- `.font-headline-1 { letter-spacing:-.04em;font:400 5.4rem/1.24 Neue Haas Unica Pro,Helvetica... }`
- `.font-headline-2 { letter-spacing:0;font:251 2.8rem/1.2 Neue Haas Unica Pro,Helvetica Neue,... }`
- `.font-headline-2-large { letter-spacing:0;font:251 5.5rem/1.24 Neue Haas Unica Pro,Helvetica Neue... }`
- `.font-headline-3 { letter-spacing:0;font:251 2.8rem/1.1 Neue Haas Unica Pro,Helvetica Neue,... }`
- `.font-headline-4 { letter-spacing:0;font:251 2.8rem/1.1 Neue Haas Unica Pro,Helvetica Neue,... }`
- **Per-Selector Transition Rules**:
- **Selector `label`**: `transition: color .2s ease-out` extracted from `brandonyasin-com` stylesheet.
- **Selector `textarea[data-v-564d7e72]:-webkit...`**: `transition: background-color 10000000s step-end` extracted from `brandonyasin-com` stylesheet.
- **Selector `al-wrap textarea[data-v-564d7e72]...`**: `transition: background-color 10000000s step-end` extracted from `brandonyasin-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.645,.045,.355,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.header>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `brandonyasin-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
