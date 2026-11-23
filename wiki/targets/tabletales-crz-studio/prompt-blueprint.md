---
title: "UI Prompt Blueprint: tabletales-crz-studio"
date: 2026-11-23
captured_at: 2026-11-23
target: "tabletales-crz-studio"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#08335d` / `#0000ff`)"
---

# UI Design System & Master Generation Blueprint: tabletales-crz-studio

> **Table Tales by CRZ.STUDIO · Board Game Collection & Play Log** (https://tabletales.crz.studio/) — Table Tales is a digital exhibition of board games as art: a curated collection and a living log of every night at the table. Designed an...

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Table Tales by CRZ.STUDIO · Board Game Collection & Play Log** (`https://tabletales.crz.studio/`). Table Tales is a digital exhibition of board games as art: a curated collection and a living log of every night at the table. Designed an...
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#08335d` / `#0000ff`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#08335d` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#fdffff` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `glowfor` for display copy (`TABLE TALES`) with `grotesk` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1360px` container bounds (`gap: 24px`, padding `40.032px`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1360px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `40.032px` lateral canvas padding with `24px` grid gap.
- **Border Radius Scale**: `2px`, `1px`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1360px`, `gap: 24px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `40.032px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1080px)`, `@media (max-width:700px)`, `@media (max-width:1200px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#08335d` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fdffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0000ff` | `body { background: blue }` (`#0000ff`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.AtWhqq_archiveLink { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#f7b538` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#0000ff` | `.J3CQ6a_ledger { border-top: #0000ff }` |
| **Variable Token (`--color-ochre`)** | `#c98f2e` | `var(--color-ochre)` in `:root` |
| **Variable Token (`--color-teal`)** | `#145a86` | `var(--color-teal)` in `:root` |
| **Variable Token (`--color-night`)** | `#010e1c` | `var(--color-night)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-blue` | `#08335d` | Brand / Palette Token |
| `--color-golden` | `#f7b538` | Brand / Palette Token |
| `--color-azure` | `#fdffff` | Brand / Palette Token |
| `--color-ochre` | `#c98f2e` | Brand / Palette Token |
| `--color-teal` | `#145a86` | Brand / Palette Token |
| `--color-night` | `#010e1c` | Brand / Palette Token |
| `--color-line-on-light` | `color-mix(in srgb, var(--color-blue) 22%, transparent)` | Canvas / Surface Token |
| `--color-line-on-dark` | `color-mix(in srgb, var(--color-azure) 22%, transparent)` | Canvas / Surface Token |
| `--color-muted-on-light` | `color-mix(in srgb, var(--color-blue) 62%, transparent)` | Canvas / Surface Token |
| `--color-muted-on-dark` | `color-mix(in srgb, var(--color-azure) 62%, transparent)` | Canvas / Surface Token |
| `--section-padding-inline` | `clamp(20px, 2.78vw, 64px)` | Layout / Spatial Grid Token |
| `--section-padding-block` | `clamp(72px, 8.33vw, 160px)` | Layout / Spatial Grid Token |
| `--measure-padding` | `clamp(0px, 18vw, 420px)` | Layout / Spatial Grid Token |
| `--space-2xs` | `4px` | Layout / Spatial Grid Token |
| `--space-xs` | `8px` | Layout / Spatial Grid Token |
| `--space-s` | `clamp(12px, 1.11vw, 16px)` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `glowfor`.
- **Primary Body Stack**: `grotesk`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 144px`, `line-height: 144px`, `font-weight: 400`); CSS variables `--font-display: "display", "display Fallback"`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 219.846px`, `line-height: 197.861px`, `font-weight: 400`); rule `h2` (`font-size: clamp(56px,5.6vw,120px)`, `line-height: .92`, `letter-spacing: 0`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-body: clamp(16px, 1.25vw, 20px)`; rule `p` (`font-size: var(--text-body)`, `line-height: 1.35`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-label: clamp(12px, .9vw, 14px)`, `--text-small: clamp(14px, 1.04vw, 16px)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.76,0,.24,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `media (prefers-reduced-motion:red...`**: `transition: .01ms!important` extracted from `tabletales-crz-studio` stylesheet.
- **Selector `._8wxUTq_closeButton`**: `transition: color var(--duration-fast) var(--ease-out)` extracted from `tabletales-crz-studio` stylesheet.
- **Selector `._8wxUTq_closeButton span:after`**: `transition: transform var(--duration-base) var(--ease-out)` extracted from `tabletales-crz-studio` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.LYh_OG_variable>` and `<section.uxasZq_variable>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Table Tales by CRZ.STUDIO · Board Game Col │
│ ====================================================================== │
│ [ <header.LYh_OG_variabl (1440x97px)  | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.q_m67W_hero> (w=1440px)                       | │
│ | H1: TABLE TALES                                                    | │
│ | Substrate: #08335d | Ink: #fdffff | Accent: #0000ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.uxasZq_variable>) max-w: 1360px            | │
│ | +------------------------------+  +------------------------------+ | │
│ | | T a b l e T a l e s          |  | Featured Games               | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.O43udq_featured>) — The play log           | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.tUdqrq_foote) | https://tabletales.crz.studio/       │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 24px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.LYh_OG_variable>) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.q_m67W_hero>) — 390px Vertical Lead           | │
│ | H1: TABLE TALES                                                    | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.uxasZq_variab) — 1-Col Stack              | │
│ | [ Item 1: T a b l e T a l e s                                    ] | │
│ | [ Item 2: Featured Games                                         ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.O43udq_featured) — 1-Col (The play log)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.tUdqrq_foote) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.LYh_OG_variable> — `tabletales-crz-studio`)**:
   - Landmark `<header class="LYh_OG_variable">` (`1440x97px`) hosting `Table Tales by CRZ.STUDIO · Board Ga` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `body { scrollbar-width:none;-ms-overflow-style:none;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.q_m67W_hero> — `TABLE TALES`)**:
   - Landmark `<section class="q_m67W_hero">` presenting display lead `TABLE TALES` and copy excerpt *"BOARD GAMES ARE ART MADE ALIVE BY THE HANDS THAT PLAY THEM"* over `#08335d` canvas and `#fdffff` ink.
3. **Primary Showcase & Content Grid (<section.uxasZq_variable> — `T a b l e T a l e s`)**:
   - Landmark `<section class="uxasZq_variable">` rendering section `T a b l e T a l e s` with copy *"Board games are art made alive by the hands that play them"*, asset references (`FoundersGrotesk_Bold-s.p.2z72oy2q...`, `FoundersGrotesk_BoldItalic-s.p.2h...`, `FoundersGrotesk_Light-s.p.03ydj7u...`, `FoundersGrotesk_LightItalic-s.p.2...`), and grid rule `html::-webkit-scrollbar { display:none }`.
4. **Interactive Detail & Feature Matrix (<section.O43udq_featured> — `Featured Games`)**:
   - Landmark `<section class="O43udq_featured">` framing `Featured Games` and `The play log` (*"Every game on this shelf began as a picture someone wanted to wal"*) with `#0000ff` surface cards, `#0000ff` accents, and `body::-webkit-scrollbar { display:none }`.
5. **Colophon & Global Directory Footer (<footer.tUdqrq_footer> — `https://tabletales.crz.studio/`)**:
   - Landmark `<footer class="tUdqrq_footer">` anchoring `Table Tales by CRZ.STUDIO · Boar` footer links (`Overview · Index · Archive · About · Contact`), copy *"Chosen for the worlds they build and the stories they leave "*, and `#0000ff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: tabletales-crz-studio (Table Tales by CRZ.STUDIO · Board Game Collection & Play Log)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `tabletales-crz-studio` (**Table Tales by CRZ.STUDIO · Board Game Collection & Play Log** — `https://tabletales.crz.studio/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#08335d` / `#0000ff`).
- **Identity & Domain Context**: Table Tales is a digital exhibition of board games as art: a curated collection and a living log of every night at the table. Designed an...
- **Primary Substrate**: `#08335d` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#fdffff`, **Accent / Highlight**: `#0000ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#08335d` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#fdffff` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `glowfor` for display copy (`TABLE TALES`) with `grotesk` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1360px` container bounds (`gap: 24px`, padding `40.032px`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `tabletales-crz-studio` in your global stylesheet:

:root {
  /* Table Tales by CRZ.STUDIO · Board Game Collection & Play Log (tabletales-crz-studio) — Live-Grounded CSS Variables */
  --color-blue: #08335d; /* Brand / Palette Token (tabletales-crz-studio) */
  --color-golden: #f7b538; /* Brand / Palette Token (tabletales-crz-studio) */
  --color-azure: #fdffff; /* Brand / Palette Token (tabletales-crz-studio) */
  --color-ochre: #c98f2e; /* Brand / Palette Token (tabletales-crz-studio) */
  --color-teal: #145a86; /* Brand / Palette Token (tabletales-crz-studio) */
  --color-night: #010e1c; /* Brand / Palette Token (tabletales-crz-studio) */
  --color-line-on-light: color-mix(in srgb, var(--color-blue) 22%, transparent); /* Canvas / Surface Token (tabletales-crz-studio) */
  --color-line-on-dark: color-mix(in srgb, var(--color-azure) 22%, transparent); /* Canvas / Surface Token (tabletales-crz-studio) */
  --color-muted-on-light: color-mix(in srgb, var(--color-blue) 62%, transparent); /* Canvas / Surface Token (tabletales-crz-studio) */
  --color-muted-on-dark: color-mix(in srgb, var(--color-azure) 62%, transparent); /* Canvas / Surface Token (tabletales-crz-studio) */
  --section-padding-inline: clamp(20px, 2.78vw, 64px); /* Layout / Spatial Grid Token (tabletales-crz-studio) */
  --section-padding-block: clamp(72px, 8.33vw, 160px); /* Layout / Spatial Grid Token (tabletales-crz-studio) */
  --measure-padding: clamp(0px, 18vw, 420px); /* Layout / Spatial Grid Token (tabletales-crz-studio) */
  --space-2xs: 4px; /* Layout / Spatial Grid Token (tabletales-crz-studio) */
  --space-xs: 8px; /* Layout / Spatial Grid Token (tabletales-crz-studio) */
  --space-s: clamp(12px, 1.11vw, 16px); /* Layout / Spatial Grid Token (tabletales-crz-studio) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#08335d` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#fdffff` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#0000ff` — grounded in `body { background: blue }` (`#0000ff`)
- **Interactive Accent / Highlight**: `#0000ff` — grounded in `.AtWhqq_archiveLink { color: blue }` (`#0000ff`)
- **Secondary / Muted Copy**: `#f7b538` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#0000ff` — grounded in `.J3CQ6a_ledger { border-top: #0000ff }`
- **Variable Token (`--color-ochre`)**: `#c98f2e` — grounded in `var(--color-ochre)` in `:root`
- **Variable Token (`--color-teal`)**: `#145a86` — grounded in `var(--color-teal)` in `:root`
- **Variable Token (`--color-night`)**: `#010e1c` — grounded in `var(--color-night)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1360px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `40.032px` lateral canvas padding with `24px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1360px`, `gap: 24px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `40.032px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1080px)`, `@media (max-width:700px)`, `@media (max-width:1200px)`
- **Corner Radii**: `2px`, `1px`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `glowfor`
- **Body Font Stack**: `grotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 144px`, `line-height: 144px`, `font-weight: 400`); CSS variables `--font-display: "display", "display Fallback"`
- **H2 Section Rule**: live computed `h2` (`font-size: 219.846px`, `line-height: 197.861px`, `font-weight: 400`); rule `h2` (`font-size: clamp(56px,5.6vw,120px)`, `line-height: .92`, `letter-spacing: 0`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-body: clamp(16px, 1.25vw, 20px)`; rule `p` (`font-size: var(--text-body)`, `line-height: 1.35`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-label: clamp(12px, .9vw, 14px)`, `--text-small: clamp(14px, 1.04vw, 16px)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `tabletales-crz-studio` (`Table Tales by CRZ.STUDIO · Board Game Collection & Play Log`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.LYh_OG_variable> — `tabletales-crz-studio`)**:
   - DOM & Selectors: Landmark `<header class="LYh_OG_variable">` (`1440x97px`) hosting `Table Tales by CRZ.STUDIO · Board Ga` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `body { scrollbar-width:none;-ms-overflow-style:none;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.LYh_OG_variable> — `tabletales-crz-studio`)` (`tabletales-crz-studio`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1080px)`, `@media (max-width:700px)`, `@media (max-width:1200px)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.76,0,.24,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.q_m67W_hero> — `TABLE TALES`)**:
   - DOM & Selectors: Landmark `<section class="q_m67W_hero">` presenting display lead `TABLE TALES` and copy excerpt *"BOARD GAMES ARE ART MADE ALIVE BY THE HANDS THAT PLAY THEM"* over `#08335d` canvas and `#fdffff` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#08335d` background with `#fdffff` headline `TABLE TALES`.
3. **Primary Showcase & Content Grid (<section.uxasZq_variable> — `T a b l e T a l e s`)**:
   - DOM & Selectors: Landmark `<section class="uxasZq_variable">` rendering section `T a b l e T a l e s` with copy *"Board games are art made alive by the hands that play them"*, asset references (`FoundersGrotesk_Bold-s.p.2z72oy2q...`, `FoundersGrotesk_BoldItalic-s.p.2h...`, `FoundersGrotesk_Light-s.p.03ydj7u...`, `FoundersGrotesk_LightItalic-s.p.2...`), and grid rule `html::-webkit-scrollbar { display:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.uxasZq_variable> — `T a b l e T a l e s`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1360px`, `gap: 24px`) on desktop and Single-column vertical stack at `390px` viewport width with `40.032px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.O43udq_featured> — `Featured Games`)**:
   - DOM & Selectors: Landmark `<section class="O43udq_featured">` framing `Featured Games` and `The play log` (*"Every game on this shelf began as a picture someone wanted to wal"*) with `#0000ff` surface cards, `#0000ff` accents, and `body::-webkit-scrollbar { display:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.O43udq_featured> — `Featured Games`)` uses `2px`, `1px`, `50%` radii, `#0000ff` highlights, and assets (FoundersGrotesk_Bold-s.p.2z72oy2q..., FoundersGrotesk_BoldItalic-s.p.2h..., FoundersGrotesk_Light-s.p.03ydj7u...).
5. **Colophon & Global Directory Footer (<footer.tUdqrq_footer> — `https://tabletales.crz.studio/`)**:
   - DOM & Selectors: Landmark `<footer class="tUdqrq_footer">` anchoring `Table Tales by CRZ.STUDIO · Boar` footer links (`Overview · Index · Archive · About · Contact`), copy *"Chosen for the worlds they build and the stories they leave "*, and `#0000ff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.tUdqrq_footer> — `https://tabletales.crz.studio/`)` aligns to `1360px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `40.032px` lateral canvas padding with `24px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"BOARD GAMES ARE ART MADE ALIVE BY THE HANDS THAT PLAY THEM"*
- Copy Excerpt 2: *"Board games are art made alive by the hands that play them"*
- Copy Excerpt 3: *"Every game on this shelf began as a picture someone wanted to walk into: a map, a..."*
- Copy Excerpt 4: *"Chosen for the worlds they build and the stories they leave behind."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.76,0,.24,1)`
- **Extracted Stylesheet Rules (`tabletales-crz-studio`)**:
- `body { scrollbar-width:none;-ms-overflow-style:none;margin:0;padding:0 }`
- `html::-webkit-scrollbar { display:none }`
- `body::-webkit-scrollbar { display:none }`
- `selection { background:var(--color-golden);color:var(--color-blue) }`
- `focus-visible { outline:2px solid var(--color-golden);outline-offset:3px }`
- **Per-Selector Transition Rules**:
- **Selector `media (prefers-reduced-motion:red...`**: `transition: .01ms!important` extracted from `tabletales-crz-studio` stylesheet.
- **Selector `._8wxUTq_closeButton`**: `transition: color var(--duration-fast) var(--ease-out)` extracted from `tabletales-crz-studio` stylesheet.
- **Selector `._8wxUTq_closeButton span:after`**: `transition: transform var(--duration-base) var(--ease-out)` extracted from `tabletales-crz-studio` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.LYh_OG_variable>` and `<section.uxasZq_variable>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `tabletales-crz-studio`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
