---
title: "UI Prompt Blueprint: www-terakawaoffice-com_en"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-terakawaoffice-com_en"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fbfaf7` / `#7e6538`)"
---

# UI Design System & Master Generation Blueprint: www-terakawaoffice-com_en

> **Architectural Photographer in Tokyo, Japan · TERAKAWA Photo Office** (https://www.terakawaoffice.com/en/) — Tokyo architectural photographer Naoki Terakawa. Completion photography, drone aerials, models, time-lapse — for architects and developer...

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Architectural Photographer in Tokyo, Japan · TERAKAWA Photo Office** (`https://www.terakawaoffice.com/en/`). Tokyo architectural photographer Naoki Terakawa. Completion photography, drone aerials, models, time-lapse — for architects and developer...
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fbfaf7` / `#7e6538`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#fbfaf7` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#141414` primary typography and `#7e6538` accents.
  - **Grounded Typographic Hierarchy**: Pairs `EB Garamond` for display copy (`Architecture, as it truly is.`) with `Inter` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1320px` container bounds (`gap: 20px`, padding `40px`) with `cubic-bezier(0.7,0,0.3,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1320px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `40px` lateral canvas padding with `20px` grid gap.
- **Border Radius Scale**: `2px`, `50%`, `1px`, `999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1320px`, `gap: 20px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `40px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:700px)`, `@media (min-width:1280px) and (orientation:landscape)`, `@media (min-width:901px) and (max-width:1279px),(min-width:1280p...`, `@media (max-width:900px) and (min-width:700px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fbfaf7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#141414` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f5f2ea` | `var(--paper-warm)` in `:root` |
| **Interactive Accent / Highlight** | `#7e6538` | `var(--accent)` in `:root` |
| **Secondary / Muted Copy** | `#8f8f8f` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e4e2dc` | `var(--line)` in `:root` |
| **Variable Token (`--ink-2`)** | `#3a3a3a` | `var(--ink-2)` in `:root` |
| **Variable Token (`--ink-soft`)** | `#6b6b6b` | `var(--ink-soft)` in `:root` |
| **Variable Token (`--ink-mute`)** | `#6d6d6d` | `var(--ink-mute)` in `:root` |
| **Variable Token (`--line-soft`)** | `#efede7` | `var(--line-soft)` in `:root` |
| **Variable Token (`--accent-dark`)** | `#6d5a33` | `var(--accent-dark)` in `:root` |
| **Variable Token (`--accent-soft`)** | `#c4b18a` | `var(--accent-soft)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#141414` | Typography Ink Token |
| `--ink-2` | `#3a3a3a` | Typography Ink Token |
| `--ink-soft` | `#6b6b6b` | Typography Ink Token |
| `--ink-mute` | `#6d6d6d` | Typography Ink Token |
| `--line` | `#e4e2dc` | Color / Atmospheric Token |
| `--line-soft` | `#efede7` | Color / Atmospheric Token |
| `--paper` | `#fbfaf7` | Canvas / Surface Token |
| `--paper-warm` | `#f5f2ea` | Canvas / Surface Token |
| `--accent` | `#7e6538` | Brand / Palette Token |
| `--accent-dark` | `#6d5a33` | Canvas / Surface Token |
| `--accent-soft` | `#c4b18a` | Brand / Palette Token |
| `--serif-jp` | `'Noto Serif JP',serif` | Typography / Scale Token |
| `--serif-en` | `'EB Garamond',serif` | Typography / Scale Token |
| `--sans` | `'Inter','Noto Serif JP',sans-serif` | Typography / Scale Token |
| `--tpo-ease` | `cubic-bezier(.16,1,.3,1)` | Motion / Easing Token |
| `--fin` | `20px` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `EB Garamond`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 51.84px`, `line-height: 60.1344px`, `font-weight: 400`, `letter-spacing: 0.2592px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 33.12px`, `line-height: 42.3936px`, `font-weight: 400`, `letter-spacing: -0.13248px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 28.8px`, `font-weight: 300`); rule `p` (`font-size: 17px`, `line-height: 1.65`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 28.8px`, `font-weight: 300`); CSS variables `--bh-caption-gap: 36px`, `--tx-label: 'Inter',-apple-system,'Helvetica Neue',sans-serif`; rule `small` (`font-size: 0.32em`, `letter-spacing: 0.15em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.7,0,0.3,1)`, `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(.22,.61,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.folio-dl`**: `transition: all 0.4s!important` extracted from `www-terakawaoffice-com_en` stylesheet.
- **Selector `.folio-dl .dl-icon`**: `transition: transform 0.4s` extracted from `www-terakawaoffice-com_en` stylesheet.
- **Selector `header`**: `transition: top 0.4s cubic-bezier(0.7,0,0.3,1)` extracted from `www-terakawaoffice-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.7,0,0.3,1)`)**: Governs interactive state transitions across `<header.tpo-js>` and `<section.trust-bar>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Architectural Photographer in Tokyo, Japan │
│ ====================================================================== │
│ [ <header.tpo-js> (1440x87px)         | Works · Services · Pricing · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: Architecture, as it truly is.                                  | │
│ | Substrate: #fbfaf7 | Ink: #141414 | Accent: #7e6538                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.trust-bar>) max-w: 1320px                  | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Space and intent, in a singl |  | Three reasons to work with T | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.works-index>) — Fine detail, faithful      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | https://www.terakawaoffice.com/en/   │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 20px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.tpo-js>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: Architecture, as it truly is.                                  | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.trust-bar>) — 1-Col Stack                 | │
│ | [ Item 1: Space and intent, in a single frame.                   ] | │
│ | [ Item 2: Three reasons to work with TERAKAWA.                   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.works-index>) — 1-Col (Fine detail, faith)  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.tpo-js> — `www-terakawaoffice-com_en`)**:
   - Landmark `<header class="tpo-js">` (`1440x87px`) hosting `Architectural Photographer in Tokyo,` navigation (`Works · Services · Pricing · About · Contact`), DOM attributes (`data-tpo-field-worker`, `data-blue-hour`, `data-bh-mode="holding"`, `data-work-title="Nogeyama Zoological P..."`), and stylesheet rule `html { scroll-behavior:smooth }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Architecture, as it truly is.`)**:
   - Landmark `<section class="hero">` presenting display lead `Architecture, as it truly is.` and copy excerpt *"Photography for Architecture — Tokyo, Japan."* over `#fbfaf7` canvas and `#141414` ink.
3. **Primary Showcase & Content Grid (<section.trust-bar> — `Space and intent, in a single fram`)**:
   - Landmark `<section class="trust-bar">` rendering section `Space and intent, in a single frame.` with copy *"Light, recomposed."*, asset references (`favicon.ico`, `favicon-96.png`, `favicon.svg`, `apple-touch-icon.png`), and grid rule `img { display:block;max-width:100% }`.
4. **Interactive Detail & Feature Matrix (<section.works-index> — `Three reasons to work with TERAKAW`)**:
   - Landmark `<section class="works-index">` framing `Three reasons to work with TERAKAWA.` and `Fine detail, faithfully recorded.` (*"Click or tap to enlarge. Hold to move the light; release to revea"*) with `#f5f2ea` surface cards, `#7e6538` accents, and `.topbar-center { justify-self:center;display:flex;align-items:center;gap:16px }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.terakawaoffice.com/en/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Architectural Photographer in To` footer links (`Works · Services · Pricing · About · Contact`), copy *"Move the pointer or your finger to guide the light. Release "*, and `#e4e2dc` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-terakawaoffice-com_en (Architectural Photographer in Tokyo, Japan · TERAKAWA Photo Office)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-terakawaoffice-com_en` (**Architectural Photographer in Tokyo, Japan · TERAKAWA Photo Office** — `https://www.terakawaoffice.com/en/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fbfaf7` / `#7e6538`).
- **Identity & Domain Context**: Tokyo architectural photographer Naoki Terakawa. Completion photography, drone aerials, models, time-lapse — for architects and developer...
- **Primary Substrate**: `#fbfaf7` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#141414`, **Accent / Highlight**: `#7e6538`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#fbfaf7` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#141414` primary typography and `#7e6538` accents.
  - **Grounded Typographic Hierarchy**: Pairs `EB Garamond` for display copy (`Architecture, as it truly is.`) with `Inter` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1320px` container bounds (`gap: 20px`, padding `40px`) with `cubic-bezier(0.7,0,0.3,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-terakawaoffice-com_en` in your global stylesheet:

:root {
  /* Architectural Photographer in Tokyo, Japan · TERAKAWA Photo Office (www-terakawaoffice-com_en) — Live-Grounded CSS Variables */
  --ink: #141414; /* Typography Ink Token (www-terakawaoffice-com_en) */
  --ink-2: #3a3a3a; /* Typography Ink Token (www-terakawaoffice-com_en) */
  --ink-soft: #6b6b6b; /* Typography Ink Token (www-terakawaoffice-com_en) */
  --ink-mute: #6d6d6d; /* Typography Ink Token (www-terakawaoffice-com_en) */
  --line: #e4e2dc; /* Color / Atmospheric Token (www-terakawaoffice-com_en) */
  --line-soft: #efede7; /* Color / Atmospheric Token (www-terakawaoffice-com_en) */
  --paper: #fbfaf7; /* Canvas / Surface Token (www-terakawaoffice-com_en) */
  --paper-warm: #f5f2ea; /* Canvas / Surface Token (www-terakawaoffice-com_en) */
  --accent: #7e6538; /* Brand / Palette Token (www-terakawaoffice-com_en) */
  --accent-dark: #6d5a33; /* Canvas / Surface Token (www-terakawaoffice-com_en) */
  --accent-soft: #c4b18a; /* Brand / Palette Token (www-terakawaoffice-com_en) */
  --serif-jp: 'Noto Serif JP',serif; /* Typography / Scale Token (www-terakawaoffice-com_en) */
  --serif-en: 'EB Garamond',serif; /* Typography / Scale Token (www-terakawaoffice-com_en) */
  --sans: 'Inter','Noto Serif JP',sans-serif; /* Typography / Scale Token (www-terakawaoffice-com_en) */
  --tpo-ease: cubic-bezier(.16,1,.3,1); /* Motion / Easing Token (www-terakawaoffice-com_en) */
  --fin: 20px; /* Dimension / Scale Token (www-terakawaoffice-com_en) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fbfaf7` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#141414` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f5f2ea` — grounded in `var(--paper-warm)` in `:root`
- **Interactive Accent / Highlight**: `#7e6538` — grounded in `var(--accent)` in `:root`
- **Secondary / Muted Copy**: `#8f8f8f` — grounded in live computed `footer` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#e4e2dc` — grounded in `var(--line)` in `:root`
- **Variable Token (`--ink-2`)**: `#3a3a3a` — grounded in `var(--ink-2)` in `:root`
- **Variable Token (`--ink-soft`)**: `#6b6b6b` — grounded in `var(--ink-soft)` in `:root`
- **Variable Token (`--ink-mute`)**: `#6d6d6d` — grounded in `var(--ink-mute)` in `:root`
- **Variable Token (`--line-soft`)**: `#efede7` — grounded in `var(--line-soft)` in `:root`
- **Variable Token (`--accent-dark`)**: `#6d5a33` — grounded in `var(--accent-dark)` in `:root`
- **Variable Token (`--accent-soft`)**: `#c4b18a` — grounded in `var(--accent-soft)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1320px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `40px` lateral canvas padding with `20px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1320px`, `gap: 20px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `40px` horizontal padding
- **Media Queries**: `@media (min-width:700px)`, `@media (min-width:1280px) and (orientation:landscape)`, `@media (min-width:901px) and (max-width:1279px),(min-width:1280p...`, `@media (max-width:900px) and (min-width:700px)`
- **Corner Radii**: `2px`, `50%`, `1px`, `999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `EB Garamond`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 51.84px`, `line-height: 60.1344px`, `font-weight: 400`, `letter-spacing: 0.2592px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 33.12px`, `line-height: 42.3936px`, `font-weight: 400`, `letter-spacing: -0.13248px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 28.8px`, `font-weight: 300`); rule `p` (`font-size: 17px`, `line-height: 1.65`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 28.8px`, `font-weight: 300`); CSS variables `--bh-caption-gap: 36px`, `--tx-label: 'Inter',-apple-system,'Helvetica Neue',sans-serif`; rule `small` (`font-size: 0.32em`, `letter-spacing: 0.15em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-terakawaoffice-com_en` (`Architectural Photographer in Tokyo, Japan · TERAKAWA Photo Office`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.tpo-js> — `www-terakawaoffice-com_en`)**:
   - DOM & Selectors: Landmark `<header class="tpo-js">` (`1440x87px`) hosting `Architectural Photographer in Tokyo,` navigation (`Works · Services · Pricing · About · Contact`), DOM attributes (`data-tpo-field-worker`, `data-blue-hour`, `data-bh-mode="holding"`, `data-work-title="Nogeyama Zoological P..."`), and stylesheet rule `html { scroll-behavior:smooth }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.tpo-js> — `www-terakawaoffice-com_en`)` (`www-terakawaoffice-com_en`) adapts across `@media (min-width:700px)`, `@media (min-width:1280px) and (orientation:landscape)`, `@media (min-width:901px) and (max-width:1279px),(min-width:1280p...`, `@media (max-width:900px) and (min-width:700px)` with `cubic-bezier(0.7,0,0.3,1)`, `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(.22,.61,.36,1)` transitions and links `Works · Services · Pricing · About · Contact`.
2. **Hero Stage & Focal Lead (<section.hero> — `Architecture, as it truly is.`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Architecture, as it truly is.` and copy excerpt *"Photography for Architecture — Tokyo, Japan."* over `#fbfaf7` canvas and `#141414` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#fbfaf7` background with `#141414` headline `Architecture, as it truly is.`.
3. **Primary Showcase & Content Grid (<section.trust-bar> — `Space and intent, in a single fram`)**:
   - DOM & Selectors: Landmark `<section class="trust-bar">` rendering section `Space and intent, in a single frame.` with copy *"Light, recomposed."*, asset references (`favicon.ico`, `favicon-96.png`, `favicon.svg`, `apple-touch-icon.png`), and grid rule `img { display:block;max-width:100% }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.trust-bar> — `Space and intent, in a single fram`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1320px`, `gap: 20px`) on desktop and Single-column vertical stack at `390px` viewport width with `40px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.works-index> — `Three reasons to work with TERAKAW`)**:
   - DOM & Selectors: Landmark `<section class="works-index">` framing `Three reasons to work with TERAKAWA.` and `Fine detail, faithfully recorded.` (*"Click or tap to enlarge. Hold to move the light; release to revea"*) with `#f5f2ea` surface cards, `#7e6538` accents, and `.topbar-center { justify-self:center;display:flex;align-items:center;gap:16px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.works-index> — `Three reasons to work with TERAKAW`)` uses `2px`, `50%`, `1px`, `999px` radii, `#7e6538` highlights, and assets (favicon.ico, favicon-96.png, favicon.svg).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.terakawaoffice.com/en/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `Architectural Photographer in To` footer links (`Works · Services · Pricing · About · Contact`), copy *"Move the pointer or your finger to guide the light. Release "*, and `#e4e2dc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://www.terakawaoffice.com/en/`)` aligns to `1320px` (non-`@media` desktop container stylesheet rule) with `40px` lateral canvas padding with `20px` grid gap and attributes (data-tpo-field-worker, data-blue-hour, data-bh-mode="holding").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Photography for Architecture — Tokyo, Japan."*
- Copy Excerpt 2: *"Light, recomposed."*
- Copy Excerpt 3: *"Click or tap to enlarge. Hold to move the light; release to reveal the next photog..."*
- Copy Excerpt 4: *"Move the pointer or your finger to guide the light. Release to change the photograph."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.7,0,0.3,1)`, `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(.22,.61,.36,1)`
- **Extracted Stylesheet Rules (`www-terakawaoffice-com_en`)**:
- `html { scroll-behavior:smooth }`
- `img { display:block;max-width:100% }`
- `.topbar-center { justify-self:center;display:flex;align-items:center;gap:16px }`
- `.topbar-center::after { content:'';width:28px;height:1px;background:rgba(255,255,255,0.2) }`
- `.topbar-right { justify-self:end }`
- **Per-Selector Transition Rules**:
- **Selector `.folio-dl`**: `transition: all 0.4s!important` extracted from `www-terakawaoffice-com_en` stylesheet.
- **Selector `.folio-dl .dl-icon`**: `transition: transform 0.4s` extracted from `www-terakawaoffice-com_en` stylesheet.
- **Selector `header`**: `transition: top 0.4s cubic-bezier(0.7,0,0.3,1)` extracted from `www-terakawaoffice-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.7,0,0.3,1)`)**: Governs interactive state transitions across `<header.tpo-js>` and `<section.trust-bar>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-terakawaoffice-com_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
