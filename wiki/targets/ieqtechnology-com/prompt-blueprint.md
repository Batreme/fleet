---
title: "UI Prompt Blueprint: ieqtechnology-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "ieqtechnology-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0a0a0a` ink, `#0d91d0` accent)"
---

# UI Design System & Master Generation Blueprint: ieqtechnology-com

> **IEQ Technology · Innovation. Experience. Quality.** (https://ieqtechnology.com/) — Managed IT, legacy system modernization, custom software and custom websites from a 100% U.S.-based team in Springfield, Oregon. Since 2011.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **IEQ Technology · Innovation. Experience. Quality.** (`https://ieqtechnology.com/`). Managed IT, legacy system modernization, custom software and custom websites from a 100% U.S.-based team in Springfield, Oregon. Since 2011.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0a0a0a` ink, `#0d91d0` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0a0a0a` primary typography and `#0d91d0` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Cabin` for display copy (`Innovation. Experience. Quality. THA`) with `Geist` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 2px`, padding `4px`) with `cubic-bezier(.2,.7,.1,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `4px` lateral canvas padding with `2px` grid gap.
- **Border Radius Scale**: `999px`, `4px`, `5px`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width<=860px)`, `@media (width<=640px)`, `@media (width<=1240px)`, `@media (width<=1040px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0a0a0a` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fafafa` | `var(--bg-2)` in `:root` |
| **Interactive Accent / Highlight** | `#0d91d0` | `var(--brand)` in `:root` |
| **Secondary / Muted Copy** | `#6b7280` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#0b80bd` | `var(--nav-line)` in `:root` |
| **Variable Token (`--ieq-teal`)** | `#074a6a` | `var(--ieq-teal)` in `:root` |
| **Variable Token (`--ieq-navy`)** | `#003e71` | `var(--ieq-navy)` in `:root` |
| **Variable Token (`--ieq-tint`)** | `#e1eff6` | `var(--ieq-tint)` in `:root` |
| **Variable Token (`--ieq-tint-2`)** | `#d5ebf6` | `var(--ieq-tint-2)` in `:root` |
| **Variable Token (`--bg-3`)** | `#f4f6f8` | `var(--bg-3)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif` | Typography / Scale Token |
| `--font-display` | `"Cabin","Geist",ui-sans-serif,system-ui,sans-serif` | Typography / Scale Token |
| `--font-mono` | `"Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace` | Typography / Scale Token |
| `--r-sm` | `6px` | Dimension / Scale Token |
| `--r-lg` | `16px` | Dimension / Scale Token |
| `--ease` | `cubic-bezier(.2,.7,.1,1)` | Motion / Easing Token |
| `--max` | `1440px` | Dimension / Scale Token |
| `--nav-h` | `76px` | Layout / Spatial Grid Token |
| `--ieq-blue` | `#0d91d0` | Color / Atmospheric Token |
| `--ieq-teal` | `#074a6a` | Color / Atmospheric Token |
| `--ieq-navy` | `#003e71` | Layout / Spatial Grid Token |
| `--ieq-tint` | `#e1eff6` | Canvas / Surface Token |
| `--ieq-tint-2` | `#d5ebf6` | Canvas / Surface Token |
| `--bg` | `#fff` | Canvas / Surface Token |
| `--bg-2` | `#fafafa` | Canvas / Surface Token |
| `--bg-3` | `#f4f6f8` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Cabin`.
- **Primary Body Stack**: `Geist`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 108px`, `line-height: 99.36px`, `font-weight: 600`, `letter-spacing: -3.24px`); CSS variables `--font-display: "Cabin","Geist",ui-sans-serif,system-ui,sans-serif`; rule `h1` (`font-size: 34px`, `letter-spacing: -.03em`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 61.2px`, `font-weight: 600`, `letter-spacing: -2.1px`); rule `.h2` (`font-size: clamp(40px,5vw,68px)`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); rule `p` (`font-size: 15px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--font-mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace`; rule `small` (`font-size: 12px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.7,.1,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(0.2,0.7,0.1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `body`**: `transition: background-color .3s var(--ease),color .3s var(--ease)` extracted from `ieqtechnology-com` stylesheet.
- **Selector `.btn`**: `transition: transform .2s var(--ease),background-color .2s,border-color .2...` extracted from `ieqtechnology-com` stylesheet.
- **Selector `.btn svg`**: `transition: transform .25s var(--ease)` extracted from `ieqtechnology-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.1,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.block>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.hero>` and `<section.block>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — IEQ Technology · Innovation. Experience. Q │
│ ====================================================================== │
│ [ <header.nav> (1440x77px)            | About · Services · All servi ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: Innovation. Experience. Quality. THAT'S IEQ TECHN...           | │
│ | Substrate: #ffffff | Ink: #0a0a0a | Accent: #0d91d0                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.block>) max-w: 1440px                      | │
│ | +------------------------------+  +------------------------------+ | │
│ | | I nnovation. E xperience. Q  |  | Four core services. One dedi | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.block:nth(2)>) — Managed IT Services       | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-foot>  ) | https://ieqtechnology.com/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 2px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.nav>            ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: Innovation. Experience. Quality. THAT'S IEQ TECHN...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.block>) — 1-Col Stack                     | │
│ | [ Item 1: I nnovation. E xperience. Q uality. That's IEQ Te...   ] | │
│ | [ Item 2: Four core services. One dedicated local team.          ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.block:nth(2)>) — 1-Col (Managed IT Service) | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-foot>  ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.nav> — `ieqtechnology-com`)**:
   - Landmark `<header class="nav scrolled">` (`1440x77px`) hosting `IEQ Technology · Innovation. Experie` navigation (`About · Services · All services · Our Work · Awards`), DOM attributes (`data-theme="light"`, `data-k="nw"`, `data-k="ne"`, `data-k="sw"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Innovation. Experience. Quality. T`)**:
   - Landmark `<section class="hero">` presenting display lead `Innovation. Experience. Quality. THAT'S IEQ TECHN...` and copy excerpt *"Managed IT, legacy system modernization, custom software, and web"* over `#ffffff` canvas and `#0a0a0a` ink.
3. **Primary Showcase & Content Grid (<section.block> — `I nnovation. E xperience. Q uality`)**:
   - Landmark `<section class="block">` rendering section `I nnovation. E xperience. Q uality. That's IEQ Te...` with copy *"Business of the Year"*, asset references (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `sitemap.xml`), and grid rule `html { scroll-behavior:smooth;-webkit-text-size-adjust:100% }`.
4. **Interactive Detail & Feature Matrix (<section.block:nth(2)> — `Four core services. One dedicated `)**:
   - Landmark `<section class="block">` framing `Four core services. One dedicated local team.` and `Managed IT Services` (*"Springfield Chamber"*) with `#fafafa` surface cards, `#0d91d0` accents, and `svg { display:block }`.
5. **Colophon & Global Directory Footer (<footer.site-foot> — `https://ieqtechnology.com/`)**:
   - Landmark `<footer class="site-foot block">` anchoring `IEQ Technology · Innovation. Exp` footer links (`About · Services · All services · Our Work · Awards`), copy *"Q uality. That's IEQ Technology."*, and `#0b80bd` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: ieqtechnology-com (IEQ Technology · Innovation. Experience. Quality.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `ieqtechnology-com` (**IEQ Technology · Innovation. Experience. Quality.** — `https://ieqtechnology.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0a0a0a` ink, `#0d91d0` accent).
- **Identity & Domain Context**: Managed IT, legacy system modernization, custom software and custom websites from a 100% U.S.-based team in Springfield, Oregon. Since 2011.
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#0a0a0a`, **Accent / Highlight**: `#0d91d0`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0a0a0a` primary typography and `#0d91d0` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Cabin` for display copy (`Innovation. Experience. Quality. THA`) with `Geist` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 2px`, padding `4px`) with `cubic-bezier(.2,.7,.1,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `ieqtechnology-com` in your global stylesheet:

:root {
  /* IEQ Technology · Innovation. Experience. Quality. (ieqtechnology-com) — Live-Grounded CSS Variables */
  --font-sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif; /* Typography / Scale Token (ieqtechnology-com) */
  --font-display: "Cabin","Geist",ui-sans-serif,system-ui,sans-serif; /* Typography / Scale Token (ieqtechnology-com) */
  --font-mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace; /* Typography / Scale Token (ieqtechnology-com) */
  --r-sm: 6px; /* Dimension / Scale Token (ieqtechnology-com) */
  --r-lg: 16px; /* Dimension / Scale Token (ieqtechnology-com) */
  --ease: cubic-bezier(.2,.7,.1,1); /* Motion / Easing Token (ieqtechnology-com) */
  --max: 1440px; /* Dimension / Scale Token (ieqtechnology-com) */
  --nav-h: 76px; /* Layout / Spatial Grid Token (ieqtechnology-com) */
  --ieq-blue: #0d91d0; /* Color / Atmospheric Token (ieqtechnology-com) */
  --ieq-teal: #074a6a; /* Color / Atmospheric Token (ieqtechnology-com) */
  --ieq-navy: #003e71; /* Layout / Spatial Grid Token (ieqtechnology-com) */
  --ieq-tint: #e1eff6; /* Canvas / Surface Token (ieqtechnology-com) */
  --ieq-tint-2: #d5ebf6; /* Canvas / Surface Token (ieqtechnology-com) */
  --bg: #fff; /* Canvas / Surface Token (ieqtechnology-com) */
  --bg-2: #fafafa; /* Canvas / Surface Token (ieqtechnology-com) */
  --bg-3: #f4f6f8; /* Canvas / Surface Token (ieqtechnology-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#0a0a0a` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#fafafa` — grounded in `var(--bg-2)` in `:root`
- **Interactive Accent / Highlight**: `#0d91d0` — grounded in `var(--brand)` in `:root`
- **Secondary / Muted Copy**: `#6b7280` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#0b80bd` — grounded in `var(--nav-line)` in `:root`
- **Variable Token (`--ieq-teal`)**: `#074a6a` — grounded in `var(--ieq-teal)` in `:root`
- **Variable Token (`--ieq-navy`)**: `#003e71` — grounded in `var(--ieq-navy)` in `:root`
- **Variable Token (`--ieq-tint`)**: `#e1eff6` — grounded in `var(--ieq-tint)` in `:root`
- **Variable Token (`--ieq-tint-2`)**: `#d5ebf6` — grounded in `var(--ieq-tint-2)` in `:root`
- **Variable Token (`--bg-3`)**: `#f4f6f8` — grounded in `var(--bg-3)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `4px` lateral canvas padding with `2px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding
- **Media Queries**: `@media (width<=860px)`, `@media (width<=640px)`, `@media (width<=1240px)`, `@media (width<=1040px)`
- **Corner Radii**: `999px`, `4px`, `5px`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Cabin`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 108px`, `line-height: 99.36px`, `font-weight: 600`, `letter-spacing: -3.24px`); CSS variables `--font-display: "Cabin","Geist",ui-sans-serif,system-ui,sans-serif`; rule `h1` (`font-size: 34px`, `letter-spacing: -.03em`)
- **H2 Section Rule**: live computed `h2` (`font-size: 60px`, `line-height: 61.2px`, `font-weight: 600`, `letter-spacing: -2.1px`); rule `.h2` (`font-size: clamp(40px,5vw,68px)`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); rule `p` (`font-size: 15px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--font-mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace`; rule `small` (`font-size: 12px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `ieqtechnology-com` (`IEQ Technology · Innovation. Experience. Quality.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.nav> — `ieqtechnology-com`)**:
   - DOM & Selectors: Landmark `<header class="nav scrolled">` (`1440x77px`) hosting `IEQ Technology · Innovation. Experie` navigation (`About · Services · All services · Our Work · Awards`), DOM attributes (`data-theme="light"`, `data-k="nw"`, `data-k="ne"`, `data-k="sw"`), and stylesheet rule `after { box-sizing:border-box }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.nav> — `ieqtechnology-com`)` (`ieqtechnology-com`) adapts across `@media (width<=860px)`, `@media (width<=640px)`, `@media (width<=1240px)`, `@media (width<=1040px)` with `cubic-bezier(.2,.7,.1,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(0.2,0.7,0.1,1)` transitions and links `About · Services · All services · Our Work · Awards`.
2. **Hero Stage & Focal Lead (<section.hero> — `Innovation. Experience. Quality. T`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Innovation. Experience. Quality. THAT'S IEQ TECHN...` and copy excerpt *"Managed IT, legacy system modernization, custom software, and web"* over `#ffffff` canvas and `#0a0a0a` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#0a0a0a` headline `Innovation. Experience. Quality. THAT'S IEQ TECHN...`.
3. **Primary Showcase & Content Grid (<section.block> — `I nnovation. E xperience. Q uality`)**:
   - DOM & Selectors: Landmark `<section class="block">` rendering section `I nnovation. E xperience. Q uality. That's IEQ Te...` with copy *"Business of the Year"*, asset references (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `sitemap.xml`), and grid rule `html { scroll-behavior:smooth;-webkit-text-size-adjust:100% }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.block> — `I nnovation. E xperience. Q uality`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2px`) on desktop and Single-column vertical stack at `390px` viewport width with `4px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.block:nth(2)> — `Four core services. One dedicated `)**:
   - DOM & Selectors: Landmark `<section class="block">` framing `Four core services. One dedicated local team.` and `Managed IT Services` (*"Springfield Chamber"*) with `#fafafa` surface cards, `#0d91d0` accents, and `svg { display:block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.block:nth(2)> — `Four core services. One dedicated `)` uses `999px`, `4px`, `5px`, `50%` radii, `#0d91d0` highlights, and assets (favicon.ico, favicon-32.png, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.site-foot> — `https://ieqtechnology.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-foot block">` anchoring `IEQ Technology · Innovation. Exp` footer links (`About · Services · All services · Our Work · Awards`), copy *"Q uality. That's IEQ Technology."*, and `#0b80bd` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-foot> — `https://ieqtechnology.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `4px` lateral canvas padding with `2px` grid gap and attributes (data-theme="light", data-k="nw", data-k="ne").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Managed IT, legacy system modernization, custom software, and web development. Eve..."*
- Copy Excerpt 2: *"Business of the Year"*
- Copy Excerpt 3: *"Springfield Chamber"*
- Copy Excerpt 4: *"Q uality. That's IEQ Technology."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.7,.1,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(0.2,0.7,0.1,1)`
- **Extracted Stylesheet Rules (`ieqtechnology-com`)**:
- `after { box-sizing:border-box }`
- `html { scroll-behavior:smooth;-webkit-text-size-adjust:100% }`
- `svg { display:block }`
- `textarea { font:inherit;color:inherit }`
- `selection { background:var(--brand);color:fff }`
- **Per-Selector Transition Rules**:
- **Selector `body`**: `transition: background-color .3s var(--ease),color .3s var(--ease)` extracted from `ieqtechnology-com` stylesheet.
- **Selector `.btn`**: `transition: transform .2s var(--ease),background-color .2s,border-color .2...` extracted from `ieqtechnology-com` stylesheet.
- **Selector `.btn svg`**: `transition: transform .25s var(--ease)` extracted from `ieqtechnology-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.1,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.block>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.hero>` and `<section.block>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `ieqtechnology-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
