---
title: "UI Prompt Blueprint: seemecreative-com"
date: 2026-11-15
target: "seemecreative-com"
status: analyzed
capture: dom
archetype: "Light-Substrate Editorial & Modular Grid System (`#f8f7f7` canvas, `#000` ink, `#333` accent)"
---

# UI Design System & Master Generation Blueprint: seemecreative-com

> **SEE ME Creative** (https://seemecreative.com/) — SEE ME emerged from the desire to forge a creative environment that reimagines the ways in which we tell, create, and share stories.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **SEE ME Creative** (`https://seemecreative.com/`). SEE ME emerged from the desire to forge a creative environment that reimagines the ways in which we tell, create, and share stories.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f8f7f7` canvas, `#000` ink, `#333` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f8f7f7` (`var(--color-white)` in `:root`) paired with `#000` primary typography and `#333` accents.
  - **Extracted Typographic Hierarchy**: Pairs `ABC Favorit` for display copy (`SEE ME Creative`) with `ABC Favorit Mono` and `ABC Favorit Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `560px` container bounds (`gap: 20px`, padding `var(--unit-header-height)`) with `cubic-bezier(0.4,0,0.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2422px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `560px` extracted from `seemecreative-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--unit-header-height)` lateral canvas padding with `20px` grid gap.
- **Border Radius Scale**: `2px`, `15px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 560px`, `gap: 20px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--unit-header-height)` horizontal padding.
- **Extracted CSS Media Queries**: `@media only screen and (min-width:1800px)`, `@media only screen and (max-width:1024px)`, `@media only screen and (max-width:850px)`, `@media only screen and (max-width:1799px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f8f7f7` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--color-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#b2b2b2` | `var(--color-gray)` in `:root` |
| **Interactive Accent / Highlight** | `#333` | `var(--color-charcoal)` in `:root` |
| **Secondary / Muted Copy** | `#ff5600` | `var(--color-orange)` in `:root` |
| **Structural Hairline Border** | `#00a9ff` | `var(--color-orange-inverse)` in `:root` |
| **Variable Token (`--color-off-white`)** | `#f9f3f2` | `var(--color-off-white)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-white` | `#f8f7f7` | Canvas / Surface Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-gray` | `#b2b2b2` | Brand / Palette Token |
| `--color-charcoal` | `#333` | Brand / Palette Token |
| `--color-orange` | `#ff5600` | Brand / Palette Token |
| `--color-orange-inverse` | `#00a9ff` | Brand / Palette Token |
| `--color-off-white` | `#f9f3f2` | Canvas / Surface Token |
| `--color-white-inverse` | `#f8f7f7` | Canvas / Surface Token |
| `--unit-100vh` | `100vh` | Layout / Spatial Grid Token |
| `--unit-gap` | `25px` | Layout / Spatial Grid Token |
| `--unit-max-width` | `1800px` | Layout / Spatial Grid Token |
| `--unit-header-height` | `66px` | Layout / Spatial Grid Token |
| `--font-primary` | `"ABC Favorit",sans-serif` | Brand / Palette Token |
| `--font-secondary` | `"Cardinal Fruit Web",serif` | Brand / Palette Token |
| `--font-tertiary` | `"ABC Favorit Mono",monospace` | Typography / Scale Token |
| `--easing-motion` | `cubic-bezier(0.4,0,0.2,1)` | Motion / Easing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `ABC Favorit`.
- **Primary Body Stack**: `ABC Favorit Mono`.
- **Technical / Metadata Stack**: `ABC Favorit Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `25px`, `10px`, `20px`, `32px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `25px`, `10px`, `20px`, `32px`).
- **Body Copy**: rule `p` (`font-size: 18px`, `line-height: 130%`, `font-weight: 400`).
- **Metadata & Navigation Labels**: CSS variables `--unit-margin-small: 10px`, `--unit-max-width-small: 680px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.4,0,0.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `st-featured .index .number[data-v...`**: `transition: opacity .4s var(--easing-motion)` extracted from `seemecreative-com` stylesheet.
- **Selector `ock-artist-featured .title[data-v...`**: `transition: color .4s var(--easing-motion)` extracted from `seemecreative-com` stylesheet.
- **Selector `ist-featured .image[data-v-6c3b37...`**: `transition: filter .4s var(--easing-motion)` extracted from `seemecreative-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.2,1)`)**: Governs interactive state transitions across `<header.global-header>` and `<section.page>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.page>` and `<section.page>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — SEE ME Creative                            │
│ ====================================================================== │
│ [ <header.global-header>   | 001 Work · 002 Artists · 003 About · 0 ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.page>                                       |   │
│ | H1: SEE ME Creative                                              |   │
│ | Substrate: #f8f7f7    | Ink: #000       | Accent: #333           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.page>            ) max-w: 560px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Where your vision goes to gr |  | WE ARE A FULL-SERVICE CREATI | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 20px  ) | │
│ | [<header.global-hea] -> [<section.page>] -> [<section.page>] |       │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wp-seo>       ) | https://seemecreative.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.global-header> — `seemecreative-com`)**:
   - Landmark `<header class="global-header header">` hosting `SEE ME Creative` navigation (`001 Work · 002 Artists · 003 About · 004 News`), DOM attributes (`data-capo`, `data-v-344bacdf`, `data-v-bd05448e`, `data-v-61c5c60e`), and stylesheet rule `.tag { color:var(--color-charcoal);font-size:10px;font-weight:400;line-height:201% }`.
2. **Hero Stage & Focal Lead (<section.page> — `SEE ME Creative`)**:
   - Landmark `<section class="page page-home">` presenting display lead `SEE ME Creative` and copy excerpt *"MIKE & Wiki Patta x Tommy Hilfiger ✛"* over `#f8f7f7` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.page> — `Where your vision goes to grow`)**:
   - Landmark `<section class="page page-home">` rendering section `Where your vision goes to grow` with copy *"Integrated Campaign Prose ✛"*, asset references (`entry.BKkY1yHX.css`, `wp-image.abO9u4pg.css`, `grid-work.Dsp1qX9O.css`, `grid-masonry.BnNvLTuH.css`), and grid rule `.tag:after { color:var(--color-charcoal) }`.
4. **Interactive Detail & Feature Matrix (<section.page> — `WE ARE A FULL-SERVICE CREATIVE AGE`)**:
   - Landmark `<section class="page page-home">` framing `WE ARE A FULL-SERVICE CREATIVE AGENCY BUILDING WO...` and `「 WE ARE A FULL-SERVICE CREATIVE AGENCY BUILDING...` (*"Kids These Days i-D ✛"*) with `#b2b2b2` surface cards, `#333` accents, and `.media { transition:filter .4s var(--easing-motion) }`.
5. **Colophon & Global Directory Footer (<footer.wp-seo> — `https://seemecreative.com/`)**:
   - Landmark `<footer class="wp-seo">` anchoring `SEE ME Creative` footer links (`001 Work · 002 Artists · 003 About · 004 News`), copy *"Localized Campaign Bumble ✛"*, and `#00a9ff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: seemecreative-com (SEE ME Creative)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `seemecreative-com` (**SEE ME Creative** — `https://seemecreative.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f8f7f7` canvas, `#000` ink, `#333` accent).
- **Identity & Domain Context**: SEE ME emerged from the desire to forge a creative environment that reimagines the ways in which we tell, create, and share stories.
- **Primary Substrate**: `#f8f7f7` (`var(--color-white)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#333`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f8f7f7` (`var(--color-white)` in `:root`) paired with `#000` primary typography and `#333` accents.
  - **Extracted Typographic Hierarchy**: Pairs `ABC Favorit` for display copy (`SEE ME Creative`) with `ABC Favorit Mono` and `ABC Favorit Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `560px` container bounds (`gap: 20px`, padding `var(--unit-header-height)`) with `cubic-bezier(0.4,0,0.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `seemecreative-com` in your global stylesheet:

:root {
  /* SEE ME Creative (seemecreative-com) — Ground-Truth Extracted CSS Variables */
  --color-white: #f8f7f7; /* Canvas / Surface Token (seemecreative-com) */
  --color-black: #000; /* Canvas / Surface Token (seemecreative-com) */
  --color-gray: #b2b2b2; /* Brand / Palette Token (seemecreative-com) */
  --color-charcoal: #333; /* Brand / Palette Token (seemecreative-com) */
  --color-orange: #ff5600; /* Brand / Palette Token (seemecreative-com) */
  --color-orange-inverse: #00a9ff; /* Brand / Palette Token (seemecreative-com) */
  --color-off-white: #f9f3f2; /* Canvas / Surface Token (seemecreative-com) */
  --color-white-inverse: #f8f7f7; /* Canvas / Surface Token (seemecreative-com) */
  --unit-100vh: 100vh; /* Layout / Spatial Grid Token (seemecreative-com) */
  --unit-gap: 25px; /* Layout / Spatial Grid Token (seemecreative-com) */
  --unit-max-width: 1800px; /* Layout / Spatial Grid Token (seemecreative-com) */
  --unit-header-height: 66px; /* Layout / Spatial Grid Token (seemecreative-com) */
  --font-primary: "ABC Favorit",sans-serif; /* Brand / Palette Token (seemecreative-com) */
  --font-secondary: "Cardinal Fruit Web",serif; /* Brand / Palette Token (seemecreative-com) */
  --font-tertiary: "ABC Favorit Mono",monospace; /* Typography / Scale Token (seemecreative-com) */
  --easing-motion: cubic-bezier(0.4,0,0.2,1); /* Motion / Easing Token (seemecreative-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f8f7f7` — grounded in `var(--color-white)` in `:root`
- **Primary Typography Ink**: `#000` — grounded in `var(--color-black)` in `:root`
- **Elevated Surface / Card Substrate**: `#b2b2b2` — grounded in `var(--color-gray)` in `:root`
- **Interactive Accent / Highlight**: `#333` — grounded in `var(--color-charcoal)` in `:root`
- **Secondary / Muted Copy**: `#ff5600` — grounded in `var(--color-orange)` in `:root`
- **Structural Hairline Border**: `#00a9ff` — grounded in `var(--color-orange-inverse)` in `:root`
- **Variable Token (`--color-off-white`)**: `#f9f3f2` — grounded in `var(--color-off-white)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2422px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `560px` extracted from `seemecreative-com` stylesheet
- **Padding & Gutters**: `var(--unit-header-height)` lateral canvas padding with `20px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 560px`, `gap: 20px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--unit-header-height)` horizontal padding
- **Media Queries**: `@media only screen and (min-width:1800px)`, `@media only screen and (max-width:1024px)`, `@media only screen and (max-width:850px)`, `@media only screen and (max-width:1799px)`
- **Corner Radii**: `2px`, `15px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `ABC Favorit`
- **Body Font Stack**: `ABC Favorit Mono`
- **Monospace / Technical Font Stack**: `ABC Favorit Mono`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `25px`, `10px`, `20px`, `32px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `25px`, `10px`, `20px`, `32px`)
- **Body Copy Rule**: rule `p` (`font-size: 18px`, `line-height: 130%`, `font-weight: 400`)
- **Metadata & Index Rule**: CSS variables `--unit-margin-small: 10px`, `--unit-max-width-small: 680px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `seemecreative-com` (`SEE ME Creative`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.global-header> — `seemecreative-com`)**:
   - DOM & Selectors: Landmark `<header class="global-header header">` hosting `SEE ME Creative` navigation (`001 Work · 002 Artists · 003 About · 004 News`), DOM attributes (`data-capo`, `data-v-344bacdf`, `data-v-bd05448e`, `data-v-61c5c60e`), and stylesheet rule `.tag { color:var(--color-charcoal);font-size:10px;font-weight:400;line-height:201% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.global-header> — `seemecreative-com`)` (`seemecreative-com`) adapts across `@media only screen and (min-width:1800px)`, `@media only screen and (max-width:1024px)`, `@media only screen and (max-width:850px)`, `@media only screen and (max-width:1799px)` with `cubic-bezier(0.4,0,0.2,1)` transitions and links `001 Work · 002 Artists · 003 About · 004 News`.
2. **Hero Stage & Focal Lead (<section.page> — `SEE ME Creative`)**:
   - DOM & Selectors: Landmark `<section class="page page-home">` presenting display lead `SEE ME Creative` and copy excerpt *"MIKE & Wiki Patta x Tommy Hilfiger ✛"* over `#f8f7f7` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2422px` desktop / `390×2400px` mobile) sets `#f8f7f7` background with `#000` headline `SEE ME Creative`.
3. **Primary Showcase & Content Grid (<section.page> — `Where your vision goes to grow`)**:
   - DOM & Selectors: Landmark `<section class="page page-home">` rendering section `Where your vision goes to grow` with copy *"Integrated Campaign Prose ✛"*, asset references (`entry.BKkY1yHX.css`, `wp-image.abO9u4pg.css`, `grid-work.Dsp1qX9O.css`, `grid-masonry.BnNvLTuH.css`), and grid rule `.tag:after { color:var(--color-charcoal) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.page> — `Where your vision goes to grow`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 560px`, `gap: 20px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--unit-header-height)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.page> — `WE ARE A FULL-SERVICE CREATIVE AGE`)**:
   - DOM & Selectors: Landmark `<section class="page page-home">` framing `WE ARE A FULL-SERVICE CREATIVE AGENCY BUILDING WO...` and `「 WE ARE A FULL-SERVICE CREATIVE AGENCY BUILDING...` (*"Kids These Days i-D ✛"*) with `#b2b2b2` surface cards, `#333` accents, and `.media { transition:filter .4s var(--easing-motion) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.page> — `WE ARE A FULL-SERVICE CREATIVE AGE`)` uses `2px`, `15px` radii, `#333` highlights, and assets (entry.BKkY1yHX.css, wp-image.abO9u4pg.css, grid-work.Dsp1qX9O.css).
5. **Colophon & Global Directory Footer (<footer.wp-seo> — `https://seemecreative.com/`)**:
   - DOM & Selectors: Landmark `<footer class="wp-seo">` anchoring `SEE ME Creative` footer links (`001 Work · 002 Artists · 003 About · 004 News`), copy *"Localized Campaign Bumble ✛"*, and `#00a9ff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wp-seo> — `https://seemecreative.com/`)` aligns to `560px` extracted from `seemecreative-com` stylesheet with `var(--unit-header-height)` lateral canvas padding with `20px` grid gap and attributes (data-capo, data-v-344bacdf, data-v-bd05448e).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"MIKE & Wiki Patta x Tommy Hilfiger ✛"*
- Copy Excerpt 2: *"Integrated Campaign Prose ✛"*
- Copy Excerpt 3: *"Kids These Days i-D ✛"*
- Copy Excerpt 4: *"Localized Campaign Bumble ✛"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.4,0,0.2,1)`
- **Extracted Stylesheet Rules (`seemecreative-com`)**:
- `.tag { color:var(--color-charcoal);font-size:10px;font-weight:400;line-height:201% }`
- `.tag:after { color:var(--color-charcoal) }`
- `.media { transition:filter .4s var(--easing-motion) }`
- `after { color:var(--color-white);content:var(--separator) }`
- `last-of-type { margin-right:0 }`
- **Per-Selector Transition Rules**:
- **Selector `st-featured .index .number[data-v...`**: `transition: opacity .4s var(--easing-motion)` extracted from `seemecreative-com` stylesheet.
- **Selector `ock-artist-featured .title[data-v...`**: `transition: color .4s var(--easing-motion)` extracted from `seemecreative-com` stylesheet.
- **Selector `ist-featured .image[data-v-6c3b37...`**: `transition: filter .4s var(--easing-motion)` extracted from `seemecreative-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.2,1)`)**: Governs interactive state transitions across `<header.global-header>` and `<section.page>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.page>` and `<section.page>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `seemecreative-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
