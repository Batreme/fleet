---
title: "UI Prompt Blueprint: pixlpin-com_designs"
date: 2026-11-23
captured_at: 2026-11-23
target: "pixlpin-com_designs"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#171717` ink, `#ff0844` accent)"
---

# UI Design System & Master Generation Blueprint: pixlpin-com_designs

> **Pixlpin: 64K+ Free UI Designs, App Screens, Motion & Graphics** (https://pixlpin.com/designs) — Join free. Browse 64K+ real app screens, user flows, websites, motion, logos & 3D, curated from the internet and updated daily.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Pixlpin: 64K+ Free UI Designs, App Screens, Motion & Graphics** (`https://pixlpin.com/designs`). Join free. Browse 64K+ real app screens, user flows, websites, motion, logos & 3D, curated from the internet and updated daily.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#171717` ink, `#ff0844` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#171717` primary typography and `#ff0844` accents.
  - **Grounded Typographic Hierarchy**: Pairs `GeistSans` for display copy (`Featured Designs`) with `GeistSans` and `monoFont`.
  - **Calibrated Spatial Grid & Motion**: Combines `1176px` container bounds (`gap: 6px`, padding `16px`) with `cubic-bezier(.45,0,.55,1)` easing and Framer Motion Layout Physics.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1176px` (measured `<main>` bounding box width within `1440px` desktop viewport).
- **Canvas Lateral Padding & Spacing**: `16px` lateral canvas padding with `6px` grid gap.
- **Border Radius Scale**: `999px`, `var(--radius-pill)`, `var(--radius-m)`, `var(--radius-s)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1176px`, `gap: 6px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding.
- **Extracted CSS Media Queries**: `@media not (min-width:1280px)`, `@media not (min-width:768px)`, `@media not (min-width:600px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#171717` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f2f2f2` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff0844` | `var(--gradient-member-1)` in `:root` |
| **Secondary / Muted Copy** | `#666666` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#f2f2f2` | `var(--color-card-border)` in `:root` |
| **Variable Token (`--ds-background-200`)** | `#fafafa` | `var(--ds-background-200)` in `:root` |
| **Variable Token (`--ds-gray-200`)** | `#ebebeb` | `var(--ds-gray-200)` in `:root` |
| **Variable Token (`--ds-gray-300`)** | `#e6e6e6` | `var(--ds-gray-300)` in `:root` |
| **Variable Token (`--ds-gray-500`)** | `#c9c9c9` | `var(--ds-gray-500)` in `:root` |
| **Variable Token (`--ds-gray-600`)** | `#a8a8a8` | `var(--ds-gray-600)` in `:root` |
| **Variable Token (`--ds-gray-700`)** | `#8f8f8f` | `var(--ds-gray-700)` in `:root` |
| **Variable Token (`--ds-gray-alpha-400`)** | `#000000` | `var(--ds-gray-alpha-400)` in `:root` |
| **Variable Token (`--ds-blue-700`)** | `#006bff` | `var(--ds-blue-700)` in `:root` |
| **Variable Token (`--ds-blue-800`)** | `#005ae0` | `var(--ds-blue-800)` in `:root` |
| **Variable Token (`--ds-blue-900`)** | `#005ff2` | `var(--ds-blue-900)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--lightningcss-light` | `initial` | Canvas / Surface Token |
| `--ds-background-100` | `#fff` | Canvas / Surface Token |
| `--ds-background-200` | `#fafafa` | Canvas / Surface Token |
| `--ds-gray-100` | `#f2f2f2` | Color / Atmospheric Token |
| `--ds-gray-200` | `#ebebeb` | Color / Atmospheric Token |
| `--ds-gray-300` | `#e6e6e6` | Color / Atmospheric Token |
| `--ds-gray-400` | `#ebebeb` | Color / Atmospheric Token |
| `--ds-gray-500` | `#c9c9c9` | Color / Atmospheric Token |
| `--ds-gray-600` | `#a8a8a8` | Color / Atmospheric Token |
| `--ds-gray-700` | `#8f8f8f` | Color / Atmospheric Token |
| `--ds-gray-900` | `#666` | Color / Atmospheric Token |
| `--ds-gray-1000` | `#171717` | Color / Atmospheric Token |
| `--ds-gray-alpha-400` | `#00000014` | Color / Atmospheric Token |
| `--ds-blue-700` | `#006bff` | Color / Atmospheric Token |
| `--ds-blue-800` | `#005ae0` | Color / Atmospheric Token |
| `--ds-blue-900` | `#005ff2` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `GeistSans`.
- **Primary Body Stack**: `GeistSans`.
- **Technical / Metadata Stack**: `monoFont`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 12px`, `line-height: 16px`, `font-weight: 500`); CSS variables `--text-size-display: 48px`, `--text-line-display: 56px`, `--text-track-display: -.06em`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 18px`, `line-height: 16px`, `font-weight: 500`).
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: 16px`, `font-weight: 500`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 16px`, `font-weight: 500`); CSS variables `--font-mono: var(--font-geist-mono), ui-monospace, monospace`, `--read-small-size: 15px`, `--read-small-line: 24px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.45,0,.55,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.32,.72,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `media (prefers-reduced-motion:red...`**: `transition: .01ms` extracted from `pixlpin-com_designs` stylesheet.
- **Selector `.sidebar-sponsor__tile`**: `transition: transform var(--duration-spring) var(--ease-spring)` extracted from `pixlpin-com_designs` stylesheet.
- **Selector `debar-sponsor:active .sidebar-spo...`**: `transition: var(--duration-fast)` extracted from `pixlpin-com_designs` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.45,0,.55,1)`)**: Governs interactive state transitions across `<header.top-bar>` and `<article.tile--video>`.
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Pixlpin: 64K+ Free UI Designs, App Screens │
│ ====================================================================== │
│ [ <header.top-bar> (264x900px)        | All · Apps · AI · Productivi ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.tile> (w=1176px)                              | │
│ | H1: Featured Designs                                               | │
│ | Substrate: #ffffff | Ink: #171717 | Accent: #ff0844                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.tile--video>) max-w: 1176px                | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Explore 64,000+ designs Join |  | Gemini AI GIF Generation Fea | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.tile:nth(2)>) — Gemini AI GIF Generat      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.shell-footer) | https://pixlpin.com/designs          │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 6px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.top-bar>        ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<article.tile>) — 390px Vertical Lead                  | │
│ | H1: Featured Designs                                               | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<article.tile--video>) — 1-Col Stack               | │
│ | [ Item 1: Explore 64,000+ designs Join 1,000+ Members, Exp       ] | │
│ | [ Item 2: Gemini AI GIF Generation Feature Announcement by       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.tile:nth(2)>) — 1-Col (Gemini AI GIF Gene)  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.shell-footer) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.top-bar> — `pixlpin-com_designs`)**:
   - Landmark `<header class="top-bar">` (`264x900px`) hosting `Pixlpin: 64K+ Free UI Designs, App S` navigation (`All · Apps · AI · Productivity · Business and SaaS`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.rAj-_a_className { font-family:GeistSans,GeistSans Fallback }`.
2. **Hero Stage & Focal Lead (<article.tile> — `Featured Designs`)**:
   - Landmark `<article class="tile tile--video">` presenting display lead `Featured Designs` and copy excerpt *"Explore 64,000+ designs Join 1,000+ Members, Explore 64,000+ desi"* over `#ffffff` canvas and `#171717` ink.
3. **Primary Showcase & Content Grid (<article.tile--video> — `Explore 64,000+ designs Join 1,000`)**:
   - Landmark `<article class="tile tile--video">` rendering section `Explore 64,000+ designs Join 1,000+ Members, Exp` with copy *"Gemini AI GIF Generation Feature Announcement by Google Gemini Sh"*, asset references (`lovable.webp`, `44hnhs08my_73.css`, `349k6yv56b9jt.css`, `3l0ai14c31l8b.css`), and grid rule `.rAj-_a_variable { --font-geist-sans:"GeistSans", "GeistSans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<article.tile:nth(2)> — `Gemini AI GIF Generation Feature A`)**:
   - Landmark `<article class="tile tile--video">` framing `Gemini AI GIF Generation Feature Announcement by` and `Gemini AI GIF Generation Feature Announcement by` (*"Gemini AI GIF Generation Feature Announcement by Google Gemini"*) with `#f2f2f2` surface cards, `#ff0844` accents, and `after { box-sizing:border-box }`.
5. **Colophon & Global Directory Footer (<footer.shell-footer> — `https://pixlpin.com/designs`)**:
   - Landmark `<footer class="shell-footer">` anchoring `Pixlpin: 64K+ Free UI Designs, A` footer links (`All · Apps · AI · Productivity · Business and SaaS`), copy *"Claude Mobile App Redesign Walkthrough by Daniel Destefanis "*, and `#f2f2f2` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: pixlpin-com_designs (Pixlpin: 64K+ Free UI Designs, App Screens, Motion & Graphics)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `pixlpin-com_designs` (**Pixlpin: 64K+ Free UI Designs, App Screens, Motion & Graphics** — `https://pixlpin.com/designs`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#171717` ink, `#ff0844` accent).
- **Identity & Domain Context**: Join free. Browse 64K+ real app screens, user flows, websites, motion, logos & 3D, curated from the internet and updated daily.
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#171717`, **Accent / Highlight**: `#ff0844`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#171717` primary typography and `#ff0844` accents.
  - **Grounded Typographic Hierarchy**: Pairs `GeistSans` for display copy (`Featured Designs`) with `GeistSans` and `monoFont`.
  - **Calibrated Spatial Grid & Motion**: Combines `1176px` container bounds (`gap: 6px`, padding `16px`) with `cubic-bezier(.45,0,.55,1)` easing and Framer Motion Layout Physics.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `pixlpin-com_designs` in your global stylesheet:

:root {
  /* Pixlpin: 64K+ Free UI Designs, App Screens, Motion & Graphics (pixlpin-com_designs) — Live-Grounded CSS Variables */
  --lightningcss-light: initial; /* Canvas / Surface Token (pixlpin-com_designs) */
  --ds-background-100: #fff; /* Canvas / Surface Token (pixlpin-com_designs) */
  --ds-background-200: #fafafa; /* Canvas / Surface Token (pixlpin-com_designs) */
  --ds-gray-100: #f2f2f2; /* Color / Atmospheric Token (pixlpin-com_designs) */
  --ds-gray-200: #ebebeb; /* Color / Atmospheric Token (pixlpin-com_designs) */
  --ds-gray-300: #e6e6e6; /* Color / Atmospheric Token (pixlpin-com_designs) */
  --ds-gray-400: #ebebeb; /* Color / Atmospheric Token (pixlpin-com_designs) */
  --ds-gray-500: #c9c9c9; /* Color / Atmospheric Token (pixlpin-com_designs) */
  --ds-gray-600: #a8a8a8; /* Color / Atmospheric Token (pixlpin-com_designs) */
  --ds-gray-700: #8f8f8f; /* Color / Atmospheric Token (pixlpin-com_designs) */
  --ds-gray-900: #666; /* Color / Atmospheric Token (pixlpin-com_designs) */
  --ds-gray-1000: #171717; /* Color / Atmospheric Token (pixlpin-com_designs) */
  --ds-gray-alpha-400: #00000014; /* Color / Atmospheric Token (pixlpin-com_designs) */
  --ds-blue-700: #006bff; /* Color / Atmospheric Token (pixlpin-com_designs) */
  --ds-blue-800: #005ae0; /* Color / Atmospheric Token (pixlpin-com_designs) */
  --ds-blue-900: #005ff2; /* Color / Atmospheric Token (pixlpin-com_designs) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#171717` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f2f2f2` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#ff0844` — grounded in `var(--gradient-member-1)` in `:root`
- **Secondary / Muted Copy**: `#666666` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#f2f2f2` — grounded in `var(--color-card-border)` in `:root`
- **Variable Token (`--ds-background-200`)**: `#fafafa` — grounded in `var(--ds-background-200)` in `:root`
- **Variable Token (`--ds-gray-200`)**: `#ebebeb` — grounded in `var(--ds-gray-200)` in `:root`
- **Variable Token (`--ds-gray-300`)**: `#e6e6e6` — grounded in `var(--ds-gray-300)` in `:root`
- **Variable Token (`--ds-gray-500`)**: `#c9c9c9` — grounded in `var(--ds-gray-500)` in `:root`
- **Variable Token (`--ds-gray-600`)**: `#a8a8a8` — grounded in `var(--ds-gray-600)` in `:root`
- **Variable Token (`--ds-gray-700`)**: `#8f8f8f` — grounded in `var(--ds-gray-700)` in `:root`
- **Variable Token (`--ds-gray-alpha-400`)**: `#000000` — grounded in `var(--ds-gray-alpha-400)` in `:root`
- **Variable Token (`--ds-blue-700`)**: `#006bff` — grounded in `var(--ds-blue-700)` in `:root`
- **Variable Token (`--ds-blue-800`)**: `#005ae0` — grounded in `var(--ds-blue-800)` in `:root`
- **Variable Token (`--ds-blue-900`)**: `#005ff2` — grounded in `var(--ds-blue-900)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1176px` (measured `<main>` bounding box width within `1440px` desktop viewport)
- **Padding & Gutters**: `16px` lateral canvas padding with `6px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1176px`, `gap: 6px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding
- **Media Queries**: `@media not (min-width:1280px)`, `@media not (min-width:768px)`, `@media not (min-width:600px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `999px`, `var(--radius-pill)`, `var(--radius-m)`, `var(--radius-s)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `GeistSans`
- **Body Font Stack**: `GeistSans`
- **Monospace / Technical Font Stack**: `monoFont`
- **H1 Display Rule**: live computed `h1` (`font-size: 12px`, `line-height: 16px`, `font-weight: 500`); CSS variables `--text-size-display: 48px`, `--text-line-display: 56px`, `--text-track-display: -.06em`
- **H2 Section Rule**: live computed `h2` (`font-size: 18px`, `line-height: 16px`, `font-weight: 500`)
- **Body Copy Rule**: live computed `body` (`font-size: 12px`, `line-height: 16px`, `font-weight: 500`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12px`, `line-height: 16px`, `font-weight: 500`); CSS variables `--font-mono: var(--font-geist-mono), ui-monospace, monospace`, `--read-small-size: 15px`, `--read-small-line: 24px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `pixlpin-com_designs` (`Pixlpin: 64K+ Free UI Designs, App Screens, Motion & Graphics`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.top-bar> — `pixlpin-com_designs`)**:
   - DOM & Selectors: Landmark `<header class="top-bar">` (`264x900px`) hosting `Pixlpin: 64K+ Free UI Designs, App S` navigation (`All · Apps · AI · Productivity · Business and SaaS`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.rAj-_a_className { font-family:GeistSans,GeistSans Fallback }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.top-bar> — `pixlpin-com_designs`)` (`pixlpin-com_designs`) adapts across `@media not (min-width:1280px)`, `@media not (min-width:768px)`, `@media not (min-width:600px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.45,0,.55,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.32,.72,0,1)` transitions and links `All · Apps · AI · Productivity · Business and SaaS`.
2. **Hero Stage & Focal Lead (<article.tile> — `Featured Designs`)**:
   - DOM & Selectors: Landmark `<article class="tile tile--video">` presenting display lead `Featured Designs` and copy excerpt *"Explore 64,000+ designs Join 1,000+ Members, Explore 64,000+ desi"* over `#ffffff` canvas and `#171717` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#171717` headline `Featured Designs`.
3. **Primary Showcase & Content Grid (<article.tile--video> — `Explore 64,000+ designs Join 1,000`)**:
   - DOM & Selectors: Landmark `<article class="tile tile--video">` rendering section `Explore 64,000+ designs Join 1,000+ Members, Exp` with copy *"Gemini AI GIF Generation Feature Announcement by Google Gemini Sh"*, asset references (`lovable.webp`, `44hnhs08my_73.css`, `349k6yv56b9jt.css`, `3l0ai14c31l8b.css`), and grid rule `.rAj-_a_variable { --font-geist-sans:"GeistSans", "GeistSans Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.tile--video> — `Explore 64,000+ designs Join 1,000`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1176px`, `gap: 6px`) on desktop and Single-column vertical stack at `390px` viewport width with `16px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.tile:nth(2)> — `Gemini AI GIF Generation Feature A`)**:
   - DOM & Selectors: Landmark `<article class="tile tile--video">` framing `Gemini AI GIF Generation Feature Announcement by` and `Gemini AI GIF Generation Feature Announcement by` (*"Gemini AI GIF Generation Feature Announcement by Google Gemini"*) with `#f2f2f2` surface cards, `#ff0844` accents, and `after { box-sizing:border-box }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.tile:nth(2)> — `Gemini AI GIF Generation Feature A`)` uses `999px`, `var(--radius-pill)`, `var(--radius-m)`, `var(--radius-s)` radii, `#ff0844` highlights, and assets (lovable.webp, 44hnhs08my_73.css, 349k6yv56b9jt.css).
5. **Colophon & Global Directory Footer (<footer.shell-footer> — `https://pixlpin.com/designs`)**:
   - DOM & Selectors: Landmark `<footer class="shell-footer">` anchoring `Pixlpin: 64K+ Free UI Designs, A` footer links (`All · Apps · AI · Productivity · Business and SaaS`), copy *"Claude Mobile App Redesign Walkthrough by Daniel Destefanis "*, and `#f2f2f2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.shell-footer> — `https://pixlpin.com/designs`)` aligns to `1176px` (measured `<main>` bounding box width within `1440px` desktop viewport) with `16px` lateral canvas padding with `6px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Explore 64,000+ designs Join 1,000+ Members, Explore 64,000+ designs"*
- Copy Excerpt 2: *"Gemini AI GIF Generation Feature Announcement by Google Gemini Share Save Google G..."*
- Copy Excerpt 3: *"Gemini AI GIF Generation Feature Announcement by Google Gemini"*
- Copy Excerpt 4: *"Claude Mobile App Redesign Walkthrough by Daniel Destefanis Share Save Daniel Dest..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.45,0,.55,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.32,.72,0,1)`
- **Extracted Stylesheet Rules (`pixlpin-com_designs`)**:
- `.rAj-_a_className { font-family:GeistSans,GeistSans Fallback }`
- `.rAj-_a_variable { --font-geist-sans:"GeistSans", "GeistSans Fallback" }`
- `after { box-sizing:border-box }`
- `svg { max-width:100%;display:block }`
- `select { font:inherit;color:inherit }`
- **Per-Selector Transition Rules**:
- **Selector `media (prefers-reduced-motion:red...`**: `transition: .01ms` extracted from `pixlpin-com_designs` stylesheet.
- **Selector `.sidebar-sponsor__tile`**: `transition: transform var(--duration-spring) var(--ease-spring)` extracted from `pixlpin-com_designs` stylesheet.
- **Selector `debar-sponsor:active .sidebar-spo...`**: `transition: var(--duration-fast)` extracted from `pixlpin-com_designs` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.45,0,.55,1)`)**: Governs interactive state transitions across `<header.top-bar>` and `<article.tile--video>`.
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `pixlpin-com_designs`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
