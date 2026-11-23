---
title: "UI Prompt Blueprint: manifesto-blandina-org"
date: 2026-11-23
captured_at: 2026-11-23
target: "manifesto-blandina-org"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#edece8` / `#ffa500`)"
---

# UI Design System & Master Generation Blueprint: manifesto-blandina-org

> **Connect, Create, Change: Manifesto of Blandina** (https://manifesto.blandina.org/) — Manifesto of Blandina: connect with yourself, create the life you want, change the world. Yoga, mindfulness and meditation in Padua, the...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Connect, Create, Change: Manifesto of Blandina** (`https://manifesto.blandina.org/`). Manifesto of Blandina: connect with yourself, create the life you want, change the world. Yoga, mindfulness and meditation in Padua, the...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#edece8` / `#ffa500`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#edece8` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1d150c` primary typography and `#ffa500` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Host Grotesk` for display copy (`Blandina`) with `Host Grotesk` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1640px` container bounds (`gap: 8px`, padding `7px`) with `cubic-bezier(.55,.06,.68,.19)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1640px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `7px` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `50%`, `5px`, `2px`, `14px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1640px`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `7px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=64em)`, `@media (width<=63.99em)`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=1023px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#edece8` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1d150c` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffa500` | `.-bg-purple { background-color: orange }` (`#ffa500`) |
| **Interactive Accent / Highlight** | `#ffa500` | `.-bg-purple { background-color: orange }` (`#ffa500`) |
| **Secondary / Muted Copy** | `#fa712a` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#fa712a` | hairline divider derived from live computed `p` `color` (`computed_styles.json`) |
| **Variable Token (`--color-white`)** | `#ffffff` | `var(--color-white)` in `:root` |
| **Variable Token (`--color-bark-green`)** | `#4a4f32` | `var(--color-bark-green)` in `:root` |
| **Variable Token (`--color-field-green`)** | `#9c9873` | `var(--color-field-green)` in `:root` |
| **Variable Token (`--color-sand`)** | `#b59972` | `var(--color-sand)` in `:root` |
| **Variable Token (`--color-terracotta`)** | `#a54d25` | `var(--color-terracotta)` in `:root` |
| **Variable Token (`--color-black`)** | `#0f0f0f` | `var(--color-black)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-base` | `var(--font-sans)` | Typography / Scale Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-white-10` | `#ffffff1a` | Canvas / Surface Token |
| `--color-bark-green` | `#4a4f32` | Brand / Palette Token |
| `--color-field-green` | `#9c9873` | Brand / Palette Token |
| `--color-ivory` | `#edece8` | Brand / Palette Token |
| `--color-sand` | `#b59972` | Brand / Palette Token |
| `--color-terracotta` | `#a54d25` | Brand / Palette Token |
| `--color-black` | `#0f0f0f` | Canvas / Surface Token |
| `--color-soft-black` | `#1d150c` | Canvas / Surface Token |
| `--color-orange` | `#fa712a` | Brand / Palette Token |
| `--color-orange-30` | `#fa712a4d` | Brand / Palette Token |
| `--color-ivory-10` | `#edece81a` | Brand / Palette Token |
| `--color-ivory-30` | `#edece84d` | Brand / Palette Token |
| `--color-soft-black-10` | `#1d150c1a` | Canvas / Surface Token |
| `--color-soft-black-70` | `#1d150cb3` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Host Grotesk`.
- **Primary Body Stack**: `Host Grotesk`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: 38.4px`, `font-weight: 700`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 100px`, `line-height: 100px`, `font-weight: 400`, `letter-spacing: -6%`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: -4%`); CSS variables `--label-height: 20px`, `--meta-gap: 14px`, `--meta-gap-under: 19px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.55,.06,.68,.19)`, `cubic-bezier(.65,.05,.36,1)`, `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `a:not([class])`**: `transition: color var(--timing-fast) var(--easing-out)` extracted from `manifesto-blandina-org` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: .01ms!important` extracted from `manifesto-blandina-org` stylesheet.
- **Selector `.fade-in-leave-active`**: `transition: opacity var(--timing-default) var(--easing-in)` extracted from `manifesto-blandina-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.55,.06,.68,.19)`)**: Governs interactive state transitions across `<header.inspirational-gallery__head>` and `<section.the-intro>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Connect, Create, Change: Manifesto of Blan │
│ ====================================================================== │
│ [ <header.inspirational- (1400x34px)  | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: Blandina                                                       | │
│ | Substrate: #edece8 | Ink: #1d150c | Accent: #ffa500                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.the-intro>) max-w: 1640px                  | │
│ | +------------------------------+  +------------------------------+ | │
│ | | E v e r y t h i n g b e g i  |  | C o n n e c t w i t h y o u  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.immersive-video>) — Create the life you w  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.the-footer> ) | https://manifesto.blandina.org/      │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.inspirational-ga) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: Blandina                                                       | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.the-intro>) — 1-Col Stack                 | │
│ | [ Item 1: E v e r y t h i n g b e g i n s w i t h i n .          ] | │
│ | [ Item 2: C o n n e c t w i t h y o u r s e l f                  ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.immersive-video) — 1-Col (Create the life yo) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.the-footer> ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.inspirational-gallery__head> — `manifesto-blandina-org`)**:
   - Landmark `<header class="inspirational-gallery__head">` (`1400x34px`) hosting `Connect, Create, Change: Manifesto o` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-v-cb3bbcd5`, `data-v-59ccf550`, `data-cursor="hide"`, `data-v-ba6e3b8d`), and stylesheet rule `property --line-bottom { syntax:"<length>";inherits:true;initial-value:360px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Blandina`)**:
   - Landmark `<section class="hero hero--fx">` presenting display lead `Blandina` and copy excerpt *"CLICK ANYWHERE TO ENTER WITH SOUND"* over `#edece8` canvas and `#1d150c` ink.
3. **Primary Showcase & Content Grid (<section.the-intro> — `E v e r y t h i n g b e g i n s w `)**:
   - Landmark `<section class="the-intro home-h__panel">` rendering section `E v e r y t h i n g b e g i n s w i t h i n .` with copy *"Connect with yourself,Create the life you want,Change the world. "*, asset references (`embeds.iubenda.com`, `cdn.iubenda.com`, `entry.D6Uwv4sb.css`, `useSmokeLayer.C7tBsLdG.css`), and grid rule `.-is-hidden { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.immersive-video> — `C o n n e c t w i t h y o u r s e `)**:
   - Landmark `<section class="immersive-video home-h__panel">` framing `C o n n e c t w i t h y o u r s e l f` and `Create the life you want` (*"Connect with yourself,Create the life you want,Change the world."*) with `#ffa500` surface cards, `#ffa500` accents, and `.-is-mobile { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.the-footer> — `https://manifesto.blandina.org/`)**:
   - Landmark `<footer class="the-footer">` anchoring `Connect, Create, Change: Manifes` footer links (`Overview · Index · Archive · About · Contact`), copy *"Connect with yourself,"*, and `#fa712a` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: manifesto-blandina-org (Connect, Create, Change: Manifesto of Blandina)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `manifesto-blandina-org` (**Connect, Create, Change: Manifesto of Blandina** — `https://manifesto.blandina.org/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#edece8` / `#ffa500`).
- **Identity & Domain Context**: Manifesto of Blandina: connect with yourself, create the life you want, change the world. Yoga, mindfulness and meditation in Padua, the...
- **Primary Substrate**: `#edece8` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#1d150c`, **Accent / Highlight**: `#ffa500`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#edece8` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1d150c` primary typography and `#ffa500` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Host Grotesk` for display copy (`Blandina`) with `Host Grotesk` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1640px` container bounds (`gap: 8px`, padding `7px`) with `cubic-bezier(.55,.06,.68,.19)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `manifesto-blandina-org` in your global stylesheet:

:root {
  /* Connect, Create, Change: Manifesto of Blandina (manifesto-blandina-org) — Live-Grounded CSS Variables */
  --font-base: var(--font-sans); /* Typography / Scale Token (manifesto-blandina-org) */
  --color-white: #fff; /* Canvas / Surface Token (manifesto-blandina-org) */
  --color-white-10: #ffffff1a; /* Canvas / Surface Token (manifesto-blandina-org) */
  --color-bark-green: #4a4f32; /* Brand / Palette Token (manifesto-blandina-org) */
  --color-field-green: #9c9873; /* Brand / Palette Token (manifesto-blandina-org) */
  --color-ivory: #edece8; /* Brand / Palette Token (manifesto-blandina-org) */
  --color-sand: #b59972; /* Brand / Palette Token (manifesto-blandina-org) */
  --color-terracotta: #a54d25; /* Brand / Palette Token (manifesto-blandina-org) */
  --color-black: #0f0f0f; /* Canvas / Surface Token (manifesto-blandina-org) */
  --color-soft-black: #1d150c; /* Canvas / Surface Token (manifesto-blandina-org) */
  --color-orange: #fa712a; /* Brand / Palette Token (manifesto-blandina-org) */
  --color-orange-30: #fa712a4d; /* Brand / Palette Token (manifesto-blandina-org) */
  --color-ivory-10: #edece81a; /* Brand / Palette Token (manifesto-blandina-org) */
  --color-ivory-30: #edece84d; /* Brand / Palette Token (manifesto-blandina-org) */
  --color-soft-black-10: #1d150c1a; /* Canvas / Surface Token (manifesto-blandina-org) */
  --color-soft-black-70: #1d150cb3; /* Canvas / Surface Token (manifesto-blandina-org) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#edece8` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#1d150c` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffa500` — grounded in `.-bg-purple { background-color: orange }` (`#ffa500`)
- **Interactive Accent / Highlight**: `#ffa500` — grounded in `.-bg-purple { background-color: orange }` (`#ffa500`)
- **Secondary / Muted Copy**: `#fa712a` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#fa712a` — grounded in hairline divider derived from live computed `p` `color` (`computed_styles.json`)
- **Variable Token (`--color-white`)**: `#ffffff` — grounded in `var(--color-white)` in `:root`
- **Variable Token (`--color-bark-green`)**: `#4a4f32` — grounded in `var(--color-bark-green)` in `:root`
- **Variable Token (`--color-field-green`)**: `#9c9873` — grounded in `var(--color-field-green)` in `:root`
- **Variable Token (`--color-sand`)**: `#b59972` — grounded in `var(--color-sand)` in `:root`
- **Variable Token (`--color-terracotta`)**: `#a54d25` — grounded in `var(--color-terracotta)` in `:root`
- **Variable Token (`--color-black`)**: `#0f0f0f` — grounded in `var(--color-black)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1640px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `7px` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1640px`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `7px` horizontal padding
- **Media Queries**: `@media (width>=64em)`, `@media (width<=63.99em)`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=1023px)`
- **Corner Radii**: `50%`, `5px`, `2px`, `14px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Host Grotesk`
- **Body Font Stack**: `Host Grotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 32px`, `line-height: 38.4px`, `font-weight: 700`)
- **H2 Section Rule**: live computed `h2` (`font-size: 100px`, `line-height: 100px`, `font-weight: 400`, `letter-spacing: -6%`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 18px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: -4%`); CSS variables `--label-height: 20px`, `--meta-gap: 14px`, `--meta-gap-under: 19px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `manifesto-blandina-org` (`Connect, Create, Change: Manifesto of Blandina`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.inspirational-gallery__head> — `manifesto-blandina-org`)**:
   - DOM & Selectors: Landmark `<header class="inspirational-gallery__head">` (`1400x34px`) hosting `Connect, Create, Change: Manifesto o` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-v-cb3bbcd5`, `data-v-59ccf550`, `data-cursor="hide"`, `data-v-ba6e3b8d`), and stylesheet rule `property --line-bottom { syntax:"<length>";inherits:true;initial-value:360px }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.inspirational-gallery__head> — `manifesto-blandina-org`)` (`manifesto-blandina-org`) adapts across `@media (width>=64em)`, `@media (width<=63.99em)`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=1023px)` with `cubic-bezier(.55,.06,.68,.19)`, `cubic-bezier(.65,.05,.36,1)`, `cubic-bezier(.16,1,.3,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.hero> — `Blandina`)**:
   - DOM & Selectors: Landmark `<section class="hero hero--fx">` presenting display lead `Blandina` and copy excerpt *"CLICK ANYWHERE TO ENTER WITH SOUND"* over `#edece8` canvas and `#1d150c` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#edece8` background with `#1d150c` headline `Blandina`.
3. **Primary Showcase & Content Grid (<section.the-intro> — `E v e r y t h i n g b e g i n s w `)**:
   - DOM & Selectors: Landmark `<section class="the-intro home-h__panel">` rendering section `E v e r y t h i n g b e g i n s w i t h i n .` with copy *"Connect with yourself,Create the life you want,Change the world. "*, asset references (`embeds.iubenda.com`, `cdn.iubenda.com`, `entry.D6Uwv4sb.css`, `useSmokeLayer.C7tBsLdG.css`), and grid rule `.-is-hidden { display:none!important }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.the-intro> — `E v e r y t h i n g b e g i n s w `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1640px`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `7px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.immersive-video> — `C o n n e c t w i t h y o u r s e `)**:
   - DOM & Selectors: Landmark `<section class="immersive-video home-h__panel">` framing `C o n n e c t w i t h y o u r s e l f` and `Create the life you want` (*"Connect with yourself,Create the life you want,Change the world."*) with `#ffa500` surface cards, `#ffa500` accents, and `.-is-mobile { display:none!important }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.immersive-video> — `C o n n e c t w i t h y o u r s e `)` uses `50%`, `5px`, `2px`, `14px` radii, `#ffa500` highlights, and assets (embeds.iubenda.com, cdn.iubenda.com, entry.D6Uwv4sb.css).
5. **Colophon & Global Directory Footer (<footer.the-footer> — `https://manifesto.blandina.org/`)**:
   - DOM & Selectors: Landmark `<footer class="the-footer">` anchoring `Connect, Create, Change: Manifes` footer links (`Overview · Index · Archive · About · Contact`), copy *"Connect with yourself,"*, and `#fa712a` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.the-footer> — `https://manifesto.blandina.org/`)` aligns to `1640px` (non-`@media` desktop container stylesheet rule) with `7px` lateral canvas padding with `8px` grid gap and attributes (data-v-cb3bbcd5, data-v-59ccf550, data-cursor="hide").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"CLICK ANYWHERE TO ENTER WITH SOUND"*
- Copy Excerpt 2: *"Connect with yourself,Create the life you want,Change the world. Connect with your..."*
- Copy Excerpt 3: *"Connect with yourself,Create the life you want,Change the world."*
- Copy Excerpt 4: *"Connect with yourself,"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.55,.06,.68,.19)`, `cubic-bezier(.65,.05,.36,1)`, `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`manifesto-blandina-org`)**:
- `property --line-bottom { syntax:"<length>";inherits:true;initial-value:360px }`
- `.-is-hidden { display:none!important }`
- `.-is-mobile { display:none!important }`
- `.-is-desktop { display:none!important }`
- `.-bg-white { background-color:var(--color-ivory);color:var(--color-soft-black) }`
- **Per-Selector Transition Rules**:
- **Selector `a:not([class])`**: `transition: color var(--timing-fast) var(--easing-out)` extracted from `manifesto-blandina-org` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: .01ms!important` extracted from `manifesto-blandina-org` stylesheet.
- **Selector `.fade-in-leave-active`**: `transition: opacity var(--timing-default) var(--easing-in)` extracted from `manifesto-blandina-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.55,.06,.68,.19)`)**: Governs interactive state transitions across `<header.inspirational-gallery__head>` and `<section.the-intro>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `manifesto-blandina-org`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
