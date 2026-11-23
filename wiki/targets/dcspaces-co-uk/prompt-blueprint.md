---
title: "UI Prompt Blueprint: dcspaces-co-uk"
date: 2026-11-23
captured_at: 2026-11-23
target: "dcspaces-co-uk"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#f4f1e9` canvas, `#343631` ink, `#6c8f6c` accent)"
---

# UI Design System & Master Generation Blueprint: dcspaces-co-uk

> **Chorley Builders · Extensions & Renovations · DC Carpentry** (https://dcspaces.co.uk/) — Family-run builders in Chorley. House extensions, wall and chimney breast removals, kitchens and bespoke staircases across Lancashire. Fr...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Chorley Builders · Extensions & Renovations · DC Carpentry** (`https://dcspaces.co.uk/`). Family-run builders in Chorley. House extensions, wall and chimney breast removals, kitchens and bespoke staircases across Lancashire. Fr...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f4f1e9` canvas, `#343631` ink, `#6c8f6c` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f4f1e9` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#343631` primary typography and `#6c8f6c` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Satoshi` for display copy (`Building & Renovation Specialists Ac`) with `Satoshi` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 2px`, padding `14px`) with `cubic-bezier(.22,.61,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `14px` lateral canvas padding with `2px` grid gap.
- **Border Radius Scale**: `999px`, `50%`, `8px`, `var(--r)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `14px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 760px)`, `@media (prefers-reduced-motion: no-preference)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 1140px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f1e9` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#343631` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f2f1ed` | `var(--cc-paper)` in `:root` |
| **Interactive Accent / Highlight** | `#6c8f6c` | `var(--brand-2)` in `:root` |
| **Secondary / Muted Copy** | `#767d86` | `var(--ink-3)` in `:root` |
| **Structural Hairline Border** | `#e0ddd6` | `var(--line)` in `:root` (`rgba(20,22,26,.09)`) |
| **Variable Token (`--cc-ink`)** | `#14161a` | `var(--cc-ink)` in `:root` |
| **Variable Token (`--cc-green`)** | `#344c3a` | `var(--cc-green)` in `:root` |
| **Variable Token (`--cc-forest`)** | `#2e432f` | `var(--cc-forest)` in `:root` |
| **Variable Token (`--cc-sage`)** | `#dfe5dc` | `var(--cc-sage)` in `:root` |
| **Variable Token (`--cc-sand`)** | `#e8e2d4` | `var(--cc-sand)` in `:root` |
| **Variable Token (`--cc-on-deep`)** | `#ffffff` | `var(--cc-on-deep)` in `:root` |
| **Variable Token (`--ink-2`)** | `#4a5058` | `var(--ink-2)` in `:root` |
| **Variable Token (`--paper-2`)** | `#e8e6e0` | `var(--paper-2)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cc-ink` | `#14161a` | Typography Ink Token |
| `--cc-green` | `#344c3a` | Color / Atmospheric Token |
| `--cc-forest` | `#2e432f` | Color / Atmospheric Token |
| `--cc-sage` | `#dfe5dc` | Color / Atmospheric Token |
| `--cc-sand` | `#e8e2d4` | Color / Atmospheric Token |
| `--cc-paper` | `#f2f1ed` | Canvas / Surface Token |
| `--cc-deep` | `#14161a` | Color / Atmospheric Token |
| `--cc-on-deep` | `#ffffff` | Color / Atmospheric Token |
| `--cc-font-display` | `'Satoshi', system-ui, sans-serif` | Typography / Scale Token |
| `--cc-font-body` | `'Satoshi', system-ui, sans-serif` | Typography / Scale Token |
| `--ink` | `#14161A` | Typography Ink Token |
| `--ink-2` | `#4A5058` | Typography Ink Token |
| `--ink-3` | `#767D86` | Typography Ink Token |
| `--paper` | `#F2F1ED` | Canvas / Surface Token |
| `--paper-2` | `#E8E6E0` | Canvas / Surface Token |
| `--white` | `#FFFFFF` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Satoshi`.
- **Primary Body Stack**: `Satoshi`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 73.6px`, `line-height: 73.6px`, `font-weight: 700`, `letter-spacing: -3.312px`); CSS variables `--cc-font-display: 'Satoshi', system-ui, sans-serif`; rule `h1` (`font-size: clamp(2.6rem, 5.6vw, 4.6rem)`, `line-height: 1`, `letter-spacing: -.045em`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 56px`, `line-height: 57.12px`, `font-weight: 700`, `letter-spacing: -2.24px`); rule `h2` (`font-size: clamp(1.5rem, 2.4vw, 2.1rem)`).
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 27.2px`, `font-weight: 400`); CSS variables `--cc-font-body: 'Satoshi', system-ui, sans-serif`; rule `p` (`font-size: .9rem`, `line-height: 1.55`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 27.2px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,.61,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.ck-bar`**: `transition: transform .28s ease` extracted from `dcspaces-co-uk` stylesheet.
- **Selector `.ck-btn`**: `transition: background-color .25s, color .25s` extracted from `dcspaces-co-uk` stylesheet.
- **Selector `.btn`**: `transition: background .25s var(--ease), color .25s var(--ease), border-co...` extracted from `dcspaces-co-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,.61,.36,1)`)**: Governs interactive state transitions across `<header.hdr>` and `<section.opening>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Chorley Builders · Extensions & Renovation │
│ ====================================================================== │
│ [ <header.hdr> (1440x86px)            | Home · About · All services  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: Building & Renovation Specialists Across Chorley...            | │
│ | Substrate: #f4f1e9 | Ink: #343631 | Accent: #6c8f6c                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.opening>) max-w: 1440px                    | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Everything your house needs, |  | Home Extensions              | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.section>) — Loft Conversions               | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.ftr>        ) | https://dcspaces.co.uk/              │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 2px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.hdr>            ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: Building & Renovation Specialists Across Chorley...            | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.opening>) — 1-Col Stack                   | │
│ | [ Item 1: Everything your house needs, from one team             ] | │
│ | [ Item 2: Home Extensions                                        ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.section>) — 1-Col (Loft Conversions)        | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.ftr>        ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.hdr> — `dcspaces-co-uk`)**:
   - Landmark `<header class="hdr">` (`1440x86px`) hosting `Chorley Builders · Extensions & Reno` navigation (`Home · About · All services · Extensions · Projects`), DOM attributes (`data-carousel`, `data-dir="prev"`, `data-dir="next"`, `data-dir="prev"`), and stylesheet rule `.dcc-hp { position: absolute !important; left: -9999px !important; width: 1px; hei... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Building & Renovation Specialists `)**:
   - Landmark `<section class="hero is-ready">` presenting display lead `Building & Renovation Specialists Across Chorley...` and copy excerpt *"CRAFTING UNIQUE SPACES"* over `#f4f1e9` canvas and `#343631` ink.
3. **Primary Showcase & Content Grid (<section.opening> — `Everything your house needs, from `)**:
   - Landmark `<section class="opening">` rendering section `Everything your house needs, from one team` with copy *"Crafting unique spaces"*, asset references (`favicon.png`, `apple-touch-icon.png`, `satoshi-900.woff2`, `satoshi-400.woff2`), and grid rule `.dcc-msg--ok { background: e6ebe3; color: 2e432f; border: 1px solid rgba(52,76,58,.25); }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Home Extensions`)**:
   - Landmark `<section class="section">` framing `Home Extensions` and `Loft Conversions` (*"Whether you’re planning a home extension, full renovation, loft c"*) with `#f2f1ed` surface cards, `#6c8f6c` accents, and `.dcc-msg--err { background: f6e8e4; color: 7a2e1f; border: 1px solid rgba(122,46,31,.22); }`.
5. **Colophon & Global Directory Footer (<footer.ftr> — `https://dcspaces.co.uk/`)**:
   - Landmark `<footer class="ftr">` anchoring `Chorley Builders · Extensions & ` footer links (`Home · About · All services · Extensions · Projects`), copy *"As a family-run business, we combine skilled craftsmanship w"*, and `#e0ddd6` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: dcspaces-co-uk (Chorley Builders · Extensions & Renovations · DC Carpentry)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `dcspaces-co-uk` (**Chorley Builders · Extensions & Renovations · DC Carpentry** — `https://dcspaces.co.uk/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f4f1e9` canvas, `#343631` ink, `#6c8f6c` accent).
- **Identity & Domain Context**: Family-run builders in Chorley. House extensions, wall and chimney breast removals, kitchens and bespoke staircases across Lancashire. Fr...
- **Primary Substrate**: `#f4f1e9` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#343631`, **Accent / Highlight**: `#6c8f6c`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f4f1e9` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#343631` primary typography and `#6c8f6c` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Satoshi` for display copy (`Building & Renovation Specialists Ac`) with `Satoshi` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 2px`, padding `14px`) with `cubic-bezier(.22,.61,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `dcspaces-co-uk` in your global stylesheet:

:root {
  /* Chorley Builders · Extensions & Renovations · DC Carpentry (dcspaces-co-uk) — Live-Grounded CSS Variables */
  --cc-ink: #14161a; /* Typography Ink Token (dcspaces-co-uk) */
  --cc-green: #344c3a; /* Color / Atmospheric Token (dcspaces-co-uk) */
  --cc-forest: #2e432f; /* Color / Atmospheric Token (dcspaces-co-uk) */
  --cc-sage: #dfe5dc; /* Color / Atmospheric Token (dcspaces-co-uk) */
  --cc-sand: #e8e2d4; /* Color / Atmospheric Token (dcspaces-co-uk) */
  --cc-paper: #f2f1ed; /* Canvas / Surface Token (dcspaces-co-uk) */
  --cc-deep: #14161a; /* Color / Atmospheric Token (dcspaces-co-uk) */
  --cc-on-deep: #ffffff; /* Color / Atmospheric Token (dcspaces-co-uk) */
  --cc-font-display: 'Satoshi', system-ui, sans-serif; /* Typography / Scale Token (dcspaces-co-uk) */
  --cc-font-body: 'Satoshi', system-ui, sans-serif; /* Typography / Scale Token (dcspaces-co-uk) */
  --ink: #14161A; /* Typography Ink Token (dcspaces-co-uk) */
  --ink-2: #4A5058; /* Typography Ink Token (dcspaces-co-uk) */
  --ink-3: #767D86; /* Typography Ink Token (dcspaces-co-uk) */
  --paper: #F2F1ED; /* Canvas / Surface Token (dcspaces-co-uk) */
  --paper-2: #E8E6E0; /* Canvas / Surface Token (dcspaces-co-uk) */
  --white: #FFFFFF; /* Canvas / Surface Token (dcspaces-co-uk) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f4f1e9` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#343631` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f2f1ed` — grounded in `var(--cc-paper)` in `:root`
- **Interactive Accent / Highlight**: `#6c8f6c` — grounded in `var(--brand-2)` in `:root`
- **Secondary / Muted Copy**: `#767d86` — grounded in `var(--ink-3)` in `:root`
- **Structural Hairline Border**: `#e0ddd6` — grounded in `var(--line)` in `:root` (`rgba(20,22,26,.09)`)
- **Variable Token (`--cc-ink`)**: `#14161a` — grounded in `var(--cc-ink)` in `:root`
- **Variable Token (`--cc-green`)**: `#344c3a` — grounded in `var(--cc-green)` in `:root`
- **Variable Token (`--cc-forest`)**: `#2e432f` — grounded in `var(--cc-forest)` in `:root`
- **Variable Token (`--cc-sage`)**: `#dfe5dc` — grounded in `var(--cc-sage)` in `:root`
- **Variable Token (`--cc-sand`)**: `#e8e2d4` — grounded in `var(--cc-sand)` in `:root`
- **Variable Token (`--cc-on-deep`)**: `#ffffff` — grounded in `var(--cc-on-deep)` in `:root`
- **Variable Token (`--ink-2`)**: `#4a5058` — grounded in `var(--ink-2)` in `:root`
- **Variable Token (`--paper-2`)**: `#e8e6e0` — grounded in `var(--paper-2)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `14px` lateral canvas padding with `2px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `14px` horizontal padding
- **Media Queries**: `@media (max-width: 760px)`, `@media (prefers-reduced-motion: no-preference)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 1140px)`
- **Corner Radii**: `999px`, `50%`, `8px`, `var(--r)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Satoshi`
- **Body Font Stack**: `Satoshi`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 73.6px`, `line-height: 73.6px`, `font-weight: 700`, `letter-spacing: -3.312px`); CSS variables `--cc-font-display: 'Satoshi', system-ui, sans-serif`; rule `h1` (`font-size: clamp(2.6rem, 5.6vw, 4.6rem)`, `line-height: 1`, `letter-spacing: -.045em`)
- **H2 Section Rule**: live computed `h2` (`font-size: 56px`, `line-height: 57.12px`, `font-weight: 700`, `letter-spacing: -2.24px`); rule `h2` (`font-size: clamp(1.5rem, 2.4vw, 2.1rem)`)
- **Body Copy Rule**: live computed `body` (`font-size: 17px`, `line-height: 27.2px`, `font-weight: 400`); CSS variables `--cc-font-body: 'Satoshi', system-ui, sans-serif`; rule `p` (`font-size: .9rem`, `line-height: 1.55`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 17px`, `line-height: 27.2px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `dcspaces-co-uk` (`Chorley Builders · Extensions & Renovations · DC Carpentry`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.hdr> — `dcspaces-co-uk`)**:
   - DOM & Selectors: Landmark `<header class="hdr">` (`1440x86px`) hosting `Chorley Builders · Extensions & Reno` navigation (`Home · About · All services · Extensions · Projects`), DOM attributes (`data-carousel`, `data-dir="prev"`, `data-dir="next"`, `data-dir="prev"`), and stylesheet rule `.dcc-hp { position: absolute !important; left: -9999px !important; width: 1px; hei... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.hdr> — `dcspaces-co-uk`)` (`dcspaces-co-uk`) adapts across `@media (max-width: 760px)`, `@media (prefers-reduced-motion: no-preference)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 1140px)` with `cubic-bezier(.22,.61,.36,1)` transitions and links `Home · About · All services · Extensions · Projects`.
2. **Hero Stage & Focal Lead (<section.hero> — `Building & Renovation Specialists `)**:
   - DOM & Selectors: Landmark `<section class="hero is-ready">` presenting display lead `Building & Renovation Specialists Across Chorley...` and copy excerpt *"CRAFTING UNIQUE SPACES"* over `#f4f1e9` canvas and `#343631` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f4f1e9` background with `#343631` headline `Building & Renovation Specialists Across Chorley...`.
3. **Primary Showcase & Content Grid (<section.opening> — `Everything your house needs, from `)**:
   - DOM & Selectors: Landmark `<section class="opening">` rendering section `Everything your house needs, from one team` with copy *"Crafting unique spaces"*, asset references (`favicon.png`, `apple-touch-icon.png`, `satoshi-900.woff2`, `satoshi-400.woff2`), and grid rule `.dcc-msg--ok { background: e6ebe3; color: 2e432f; border: 1px solid rgba(52,76,58,.25); }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.opening> — `Everything your house needs, from `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2px`) on desktop and Single-column vertical stack at `390px` viewport width with `14px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section> — `Home Extensions`)**:
   - DOM & Selectors: Landmark `<section class="section">` framing `Home Extensions` and `Loft Conversions` (*"Whether you’re planning a home extension, full renovation, loft c"*) with `#f2f1ed` surface cards, `#6c8f6c` accents, and `.dcc-msg--err { background: f6e8e4; color: 7a2e1f; border: 1px solid rgba(122,46,31,.22); }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section> — `Home Extensions`)` uses `999px`, `50%`, `8px`, `var(--r)` radii, `#6c8f6c` highlights, and assets (favicon.png, apple-touch-icon.png, satoshi-900.woff2).
5. **Colophon & Global Directory Footer (<footer.ftr> — `https://dcspaces.co.uk/`)**:
   - DOM & Selectors: Landmark `<footer class="ftr">` anchoring `Chorley Builders · Extensions & ` footer links (`Home · About · All services · Extensions · Projects`), copy *"As a family-run business, we combine skilled craftsmanship w"*, and `#e0ddd6` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.ftr> — `https://dcspaces.co.uk/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `14px` lateral canvas padding with `2px` grid gap and attributes (data-carousel, data-dir="prev", data-dir="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"CRAFTING UNIQUE SPACES"*
- Copy Excerpt 2: *"Crafting unique spaces"*
- Copy Excerpt 3: *"Whether you’re planning a home extension, full renovation, loft conversion or stru..."*
- Copy Excerpt 4: *"As a family-run business, we combine skilled craftsmanship with professional proje..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,.61,.36,1)`
- **Extracted Stylesheet Rules (`dcspaces-co-uk`)**:
- `.dcc-hp { position: absolute !important; left: -9999px !important; width: 1px; hei... }`
- `.dcc-msg--ok { background: e6ebe3; color: 2e432f; border: 1px solid rgba(52,76,58,.25); }`
- `.dcc-msg--err { background: f6e8e4; color: 7a2e1f; border: 1px solid rgba(122,46,31,.22); }`
- `.dcc-404 { min-height: clamp(420px, 60vh, 560px); background: 344c3a; }`
- `.dcc-404 .phero__cta { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 22px; }`
- **Per-Selector Transition Rules**:
- **Selector `.ck-bar`**: `transition: transform .28s ease` extracted from `dcspaces-co-uk` stylesheet.
- **Selector `.ck-btn`**: `transition: background-color .25s, color .25s` extracted from `dcspaces-co-uk` stylesheet.
- **Selector `.btn`**: `transition: background .25s var(--ease), color .25s var(--ease), border-co...` extracted from `dcspaces-co-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,.61,.36,1)`)**: Governs interactive state transitions across `<header.hdr>` and `<section.opening>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `dcspaces-co-uk`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
