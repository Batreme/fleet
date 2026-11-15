---
title: "UI Prompt Blueprint: gpg-dops-agency"
date: 2026-11-15
target: "[[overview|gpg-dops-agency]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#1051b4` accent)"
---

# UI Design System & Master Generation Blueprint: gpg-dops-agency

> **Garvinpromo** (https://gpg.dops.agency/) — Welcome to Garvin Promotion Group, a leading provider of rebate management, spiffs, and loyalty incentive programs

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Garvinpromo** (`https://gpg.dops.agency/`). Welcome to Garvin Promotion Group, a leading provider of rebate management, spiffs, and loyalty incentive programs
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#1051b4` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--vc-clr-primary)` in `:root`) paired with `#fff` primary typography and `#1051b4` accents.
  - **Extracted Typographic Hierarchy**: Pairs `PPMori` for display copy (`Welcome to Garvin Promotion Group, a`) with `PPMori Semi Bold` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `960px` container bounds (`gap: 16px`, padding `24px`) with `cubic-bezier(.37,0,.63,1)` easing and Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `960px` extracted from `gpg-dops-agency` stylesheet.
- **Canvas Lateral Padding & Spacing**: `24px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `50%`, `4px`, `35px`, `var(--vc-nav-border-radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 960px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `24px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (min-width:1025px)`, `@media screen and (max-width:960px)`, `@media screen and (max-width:767px),screen and (max-width:825px)...`, `@media (max-width:1024px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--vc-clr-primary)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--vc-clr-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#003c97` | `:before { background-color: #003c97 }` |
| **Interactive Accent / Highlight** | `#1051b4` | `:before { background-color: #1051b4 }` |
| **Secondary / Muted Copy** | `#f15928` | `:before { background-color: #f15928 }` |
| **Structural Hairline Border** | `#d3d3d3` | `:before { background-color: #d3d3d3 }` |
| **Variable Token (`--vc-clr-secondary`)** | `#090f207f` | `var(--vc-clr-secondary)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--line` | `16px` | Dimension / Scale Token |
| `--height-mask` | `22px` | Layout / Spatial Grid Token |
| `--vc-clr-primary` | `#000` | Brand / Palette Token |
| `--vc-clr-secondary` | `#090f207f` | Brand / Palette Token |
| `--vc-clr-white` | `#fff` | Canvas / Surface Token |
| `--vc-icn-width` | `1.2em` | Layout / Spatial Grid Token |
| `--vc-nav-width` | `30px` | Layout / Spatial Grid Token |
| `--vc-nav-height` | `30px` | Layout / Spatial Grid Token |
| `--vc-nav-border-radius` | `0` | Layout / Spatial Grid Token |
| `--vc-nav-color` | `var(--vc-clr-primary)` | Brand / Palette Token |
| `--vc-nav-color-hover` | `var(--vc-clr-secondary)` | Brand / Palette Token |
| `--vc-nav-background` | `transparent` | Canvas / Surface Token |
| `--vc-pgn-width` | `12px` | Layout / Spatial Grid Token |
| `--vc-pgn-height` | `4px` | Layout / Spatial Grid Token |
| `--vc-pgn-margin` | `4px` | Layout / Spatial Grid Token |
| `--vc-pgn-border-radius` | `0` | Elevation / Border Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `PPMori`.
- **Primary Body Stack**: `PPMori Semi Bold`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `14px`, `12px`, `22px`, `16px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `14px`, `12px`, `22px`, `16px`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `14px`, `12px`, `22px`, `16px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `14px`, `12px`, `22px`, `16px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.37,0,.63,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.circle[data-v-2f21aabe]`**: `transition: left 1.25s ease-in-out` extracted from `gpg-dops-agency` stylesheet.
- **Selector `media screen and (min-width:1025px)`**: `transition: transform .65s ease-in-out` extracted from `gpg-dops-agency` stylesheet.
- **Selector `.accordion-leave-active[data-v-99...`**: `transition: height .3s ease-in-out,opacity .2s ease` extracted from `gpg-dops-agency` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.37,0,.63,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.carousel>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Garvinpromo                                │
│ ====================================================================== │
│ [ <header.header>          | Services Services · About us About us  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.carousel>                                   |   │
│ | H1: Welcome to Garvin Promotion Group, a leading prov...         |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #1051b4        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.carousel>        ) max-w: 960px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Promotion strategy and devel |  | Rebate fulfillment           | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.header>] -> [<section.carousel>] -> [<section.carousel>] |  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://gpg.dops.agency/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `gpg-dops-agency`)**:
   - Landmark `<header class="header header--light">` hosting `Garvinpromo` navigation (`Services Services · About us About us · Let's Talk`), DOM attributes (`data-v-537c3597`, `data-v-5f87b270`, `data-v-05812e15`, `data-v-f8de3fbd`), and stylesheet rule `before { border-radius:50%;content:"";display:block;height:100%;left:0;position:a... }`.
2. **Hero Stage & Focal Lead (<section.carousel> — `Welcome to Garvin Promotion Group,`)**:
   - Landmark `<section class="carousel home-strategic__carousel">` presenting display lead `Welcome to Garvin Promotion Group, a leading prov...` and copy excerpt *"Garvin Promotion Group"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.carousel> — `Promotion strategy and development`)**:
   - Landmark `<section class="carousel">` rendering section `Promotion strategy and development` with copy *"Clients success Clients success"*, asset references (`garvinpromo.com`, `favicon.ico`, `favicon-16x16.png`, `favicon-32x32.png`), and grid rule `hover .faq__item-question { color:898995 }`.
4. **Interactive Detail & Feature Matrix (<section.preloader--initial> — `Rebate fulfillment`)**:
   - Landmark `<section class="preloader--initial">` framing `Rebate fulfillment` and `Loyalty programs` (*"Garvin Promotion Group 10220 South 51st Street Phoenix, AZ 85044"*) with `#003c97` surface cards, `#1051b4` accents, and `hover .faq__item-cross { border-color:898995 }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://gpg.dops.agency/`)**:
   - Landmark `<footer class="footer bg-dark">` anchoring `Garvinpromo` footer links (`Services Services · About us About us · Let's Talk`), copy *"Welcome to Garvin Promotion Group, a leading provider of reb"*, and `#d3d3d3` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: gpg-dops-agency (Garvinpromo)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `gpg-dops-agency` (**Garvinpromo** — `https://gpg.dops.agency/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#1051b4` accent).
- **Identity & Domain Context**: Welcome to Garvin Promotion Group, a leading provider of rebate management, spiffs, and loyalty incentive programs
- **Primary Substrate**: `#000` (`var(--vc-clr-primary)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#1051b4`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--vc-clr-primary)` in `:root`) paired with `#fff` primary typography and `#1051b4` accents.
  - **Extracted Typographic Hierarchy**: Pairs `PPMori` for display copy (`Welcome to Garvin Promotion Group, a`) with `PPMori Semi Bold` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `960px` container bounds (`gap: 16px`, padding `24px`) with `cubic-bezier(.37,0,.63,1)` easing and Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `gpg-dops-agency` in your global stylesheet:

:root {
  /* Garvinpromo (gpg-dops-agency) — Ground-Truth Extracted CSS Variables */
  --line: 16px; /* Dimension / Scale Token (gpg-dops-agency) */
  --height-mask: 22px; /* Layout / Spatial Grid Token (gpg-dops-agency) */
  --vc-clr-primary: #000; /* Brand / Palette Token (gpg-dops-agency) */
  --vc-clr-secondary: #090f207f; /* Brand / Palette Token (gpg-dops-agency) */
  --vc-clr-white: #fff; /* Canvas / Surface Token (gpg-dops-agency) */
  --vc-icn-width: 1.2em; /* Layout / Spatial Grid Token (gpg-dops-agency) */
  --vc-nav-width: 30px; /* Layout / Spatial Grid Token (gpg-dops-agency) */
  --vc-nav-height: 30px; /* Layout / Spatial Grid Token (gpg-dops-agency) */
  --vc-nav-border-radius: 0; /* Layout / Spatial Grid Token (gpg-dops-agency) */
  --vc-nav-color: var(--vc-clr-primary); /* Brand / Palette Token (gpg-dops-agency) */
  --vc-nav-color-hover: var(--vc-clr-secondary); /* Brand / Palette Token (gpg-dops-agency) */
  --vc-nav-background: transparent; /* Canvas / Surface Token (gpg-dops-agency) */
  --vc-pgn-width: 12px; /* Layout / Spatial Grid Token (gpg-dops-agency) */
  --vc-pgn-height: 4px; /* Layout / Spatial Grid Token (gpg-dops-agency) */
  --vc-pgn-margin: 4px; /* Layout / Spatial Grid Token (gpg-dops-agency) */
  --vc-pgn-border-radius: 0; /* Elevation / Border Token (gpg-dops-agency) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--vc-clr-primary)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--vc-clr-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#003c97` — grounded in `:before { background-color: #003c97 }`
- **Interactive Accent / Highlight**: `#1051b4` — grounded in `:before { background-color: #1051b4 }`
- **Secondary / Muted Copy**: `#f15928` — grounded in `:before { background-color: #f15928 }`
- **Structural Hairline Border**: `#d3d3d3` — grounded in `:before { background-color: #d3d3d3 }`
- **Variable Token (`--vc-clr-secondary`)**: `#090f207f` — grounded in `var(--vc-clr-secondary)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `960px` extracted from `gpg-dops-agency` stylesheet
- **Padding & Gutters**: `24px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 960px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `24px` horizontal padding
- **Media Queries**: `@media screen and (min-width:1025px)`, `@media screen and (max-width:960px)`, `@media screen and (max-width:767px),screen and (max-width:825px)...`, `@media (max-width:1024px)`
- **Corner Radii**: `50%`, `4px`, `35px`, `var(--vc-nav-border-radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `PPMori`
- **Body Font Stack**: `PPMori Semi Bold`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `14px`, `12px`, `22px`, `16px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `14px`, `12px`, `22px`, `16px`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `14px`, `12px`, `22px`, `16px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `14px`, `12px`, `22px`, `16px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `gpg-dops-agency` (`Garvinpromo`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `gpg-dops-agency`)**:
   - DOM & Selectors: Landmark `<header class="header header--light">` hosting `Garvinpromo` navigation (`Services Services · About us About us · Let's Talk`), DOM attributes (`data-v-537c3597`, `data-v-5f87b270`, `data-v-05812e15`, `data-v-f8de3fbd`), and stylesheet rule `before { border-radius:50%;content:"";display:block;height:100%;left:0;position:a... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `gpg-dops-agency`)` (`gpg-dops-agency`) adapts across `@media screen and (min-width:1025px)`, `@media screen and (max-width:960px)`, `@media screen and (max-width:767px),screen and (max-width:825px)...`, `@media (max-width:1024px)` with `cubic-bezier(.37,0,.63,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.16,1,.3,1)` transitions and links `Services Services · About us About us · Let's Talk`.
2. **Hero Stage & Focal Lead (<section.carousel> — `Welcome to Garvin Promotion Group,`)**:
   - DOM & Selectors: Landmark `<section class="carousel home-strategic__carousel">` presenting display lead `Welcome to Garvin Promotion Group, a leading prov...` and copy excerpt *"Garvin Promotion Group"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Welcome to Garvin Promotion Group, a leading prov...`.
3. **Primary Showcase & Content Grid (<section.carousel> — `Promotion strategy and development`)**:
   - DOM & Selectors: Landmark `<section class="carousel">` rendering section `Promotion strategy and development` with copy *"Clients success Clients success"*, asset references (`garvinpromo.com`, `favicon.ico`, `favicon-16x16.png`, `favicon-32x32.png`), and grid rule `hover .faq__item-question { color:898995 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.carousel> — `Promotion strategy and development`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 960px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `24px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.preloader--initial> — `Rebate fulfillment`)**:
   - DOM & Selectors: Landmark `<section class="preloader--initial">` framing `Rebate fulfillment` and `Loyalty programs` (*"Garvin Promotion Group 10220 South 51st Street Phoenix, AZ 85044"*) with `#003c97` surface cards, `#1051b4` accents, and `hover .faq__item-cross { border-color:898995 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.preloader--initial> — `Rebate fulfillment`)` uses `50%`, `4px`, `35px`, `var(--vc-nav-border-radius)` radii, `#1051b4` highlights, and assets (garvinpromo.com, favicon.ico, favicon-16x16.png).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://gpg.dops.agency/`)**:
   - DOM & Selectors: Landmark `<footer class="footer bg-dark">` anchoring `Garvinpromo` footer links (`Services Services · About us About us · Let's Talk`), copy *"Welcome to Garvin Promotion Group, a leading provider of reb"*, and `#d3d3d3` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://gpg.dops.agency/`)` aligns to `960px` extracted from `gpg-dops-agency` stylesheet with `24px` lateral canvas padding with `16px` grid gap and attributes (data-v-537c3597, data-v-5f87b270, data-v-05812e15).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Garvin Promotion Group"*
- Copy Excerpt 2: *"Clients success Clients success"*
- Copy Excerpt 3: *"Garvin Promotion Group 10220 South 51st Street Phoenix, AZ 85044"*
- Copy Excerpt 4: *"Welcome to Garvin Promotion Group, a leading provider of rebate management, spiffs..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.37,0,.63,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`gpg-dops-agency`)**:
- `before { border-radius:50%;content:"";display:block;height:100%;left:0;position:a... }`
- `hover .faq__item-question { color:898995 }`
- `hover .faq__item-cross { border-color:898995 }`
- `hover .faq__item-cross:before { background-color:898995 }`
- `after { height:var(--line);width:2px }`
- **Per-Selector Transition Rules**:
- **Selector `.circle[data-v-2f21aabe]`**: `transition: left 1.25s ease-in-out` extracted from `gpg-dops-agency` stylesheet.
- **Selector `media screen and (min-width:1025px)`**: `transition: transform .65s ease-in-out` extracted from `gpg-dops-agency` stylesheet.
- **Selector `.accordion-leave-active[data-v-99...`**: `transition: height .3s ease-in-out,opacity .2s ease` extracted from `gpg-dops-agency` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.37,0,.63,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.carousel>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `gpg-dops-agency`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
