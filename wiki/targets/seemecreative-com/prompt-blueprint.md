---
title: "UI Prompt Blueprint: seemecreative-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "seemecreative-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 3
subpages_crawled: 3
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#f8f7f7` canvas, `#333333` ink, `#ffa500` accent)"
---

# UI Design System & Master Generation Blueprint: seemecreative-com

> **SEE ME Creative** (https://seemecreative.com/) — SEE ME emerged from the desire to forge a creative environment that reimagines the ways in which we tell, create, and share stories.

![Desktop Journey Filmstrip (1280x2484)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **SEE ME Creative** (`https://seemecreative.com/`). SEE ME emerged from the desire to forge a creative environment that reimagines the ways in which we tell, create, and share stories.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f8f7f7` canvas, `#333333` ink, `#ffa500` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f8f7f7` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#333333` primary typography and `#ffa500` accents.
  - **Grounded Typographic Hierarchy**: Uses `ABC Favorit` across display (`SEE ME Creative`) and body copy, paired with `ABC Favorit Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 20px`, padding `25px`) with `cubic-bezier(0.4,0,0.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×2484px` (`assets/desktop-journey.webp`, `3` keyframes up to `y=1522px` / doc `2422px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `25px` lateral canvas padding with `20px` grid gap.
- **Border Radius Scale**: `2px`, `15px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 20px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `25px` horizontal padding.
- **Extracted CSS Media Queries**: `@media only screen and (max-width:850px)`, `@media only screen and (max-width:1024px)`, `@media only screen and (min-width:1800px)`, `@media only screen and (max-width:1799px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f8f7f7` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#333333` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `:after { background-color: #ffffff }` |
| **Interactive Accent / Highlight** | `#ffa500` | `.menu a.router-link-active .index { color: orange }` (`#ffa500`) |
| **Secondary / Muted Copy** | `#ffa500` | `.glyph { color: orange }` (`#ffa500`) |
| **Structural Hairline Border** | `#ffa500` | `path { stroke: #ffa500 }` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-gray`)** | `#b2b2b2` | `var(--color-gray)` in `:root` |
| **Variable Token (`--color-orange`)** | `#ff5600` | `var(--color-orange)` in `:root` |
| **Variable Token (`--color-orange-inverse`)** | `#00a9ff` | `var(--color-orange-inverse)` in `:root` |
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
- **Primary Body Stack**: `ABC Favorit`.
- **Technical / Metadata Stack**: `ABC Favorit Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: normal`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 50px`, `line-height: 45px`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 18px`, `line-height: 130%`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--unit-margin-small: 10px`, `--unit-max-width-small: 680px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.4,0,0.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `st-featured .index .number[data-v...`**: `transition: opacity .4s var(--easing-motion)` extracted from `seemecreative-com` stylesheet.
- **Selector `ock-artist-featured .title[data-v...`**: `transition: color .4s var(--easing-motion)` extracted from `seemecreative-com` stylesheet.
- **Selector `ist-featured .image[data-v-6c3b37...`**: `transition: filter .4s var(--easing-motion)` extracted from `seemecreative-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.2,1)`)**: Governs interactive state transitions across `<header.global-header>` and `<section.page-home>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.page>` and `<section.page-home>` interactive targets.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `2422px`, deepest scrollY reached `1522px` across `3` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Hover Physics (`primary_cta` · `001 WORK`)**: `color`: `rgb(248, 247, 247)` -> `rgb(0, 169, 255)`; `borderColor`: `rgb(248, 247, 247)` -> `rgb(0, 169, 255)` (`transition-duration: 0.4s`, `timing: cubic-bezier(0.4, 0, 0.2, 1)`).
- **Route Transition Architecture**: First internal navigation (`/work/`) measured as `MPA` in `1196ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — SEE ME Creative                            │
│ ====================================================================== │
│ [ <header.global-header> (1440x66px)  | 001 Work · 002 Artists · 003 ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.page> (w=1440px)                              | │
│ | H1: SEE ME Creative                                                | │
│ | Substrate: #f8f7f7 | Ink: #333333 | Accent: #ffa500                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.page-home>) max-w: 1440px                  | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Where your vision goes to gr |  | WE ARE A FULL-SERVICE CREATI | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.page:nth(2)>) — 「 WE ARE A FULL-SERVI      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wp-seo>     ) | https://seemecreative.com/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 20px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.global-header>  ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.page>) — 390px Vertical Lead                  | │
│ | H1: SEE ME Creative                                                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.page-home>) — 1-Col Stack                 | │
│ | [ Item 1: Where your vision goes to grow                         ] | │
│ | [ Item 2: WE ARE A FULL-SERVICE CREATIVE AGENCY BUILDING WO...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.page:nth(2)>) — 1-Col (「 WE ARE A FULL-SE)  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wp-seo>     ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.global-header> — `seemecreative-com`)**:
   - Landmark `<header class="global-header header">` (`1440x66px`) hosting `SEE ME Creative` navigation (`001 Work · 002 Artists · 003 About · 004 News`), DOM attributes (`data-capo`, `data-v-344bacdf`, `data-v-bd05448e`, `data-v-61c5c60e`), and stylesheet rule `.tag { color:var(--color-charcoal);font-size:10px;font-weight:400;line-height:201% }`.
2. **Hero Stage & Focal Lead (<section.page> — `SEE ME Creative`)**:
   - Landmark `<section class="page page-home">` presenting display lead `SEE ME Creative` and copy excerpt *"sayhello@seemecreative.com"* over `#f8f7f7` canvas and `#333333` ink.
3. **Primary Showcase & Content Grid (<section.page-home> — `Where your vision goes to grow`)**:
   - Landmark `<section class="page page-home">` rendering section `Where your vision goes to grow` with copy *"SEE ME Creative"*, asset references (`entry.BKkY1yHX.css`, `wp-image.abO9u4pg.css`, `grid-work.Dsp1qX9O.css`, `grid-masonry.BnNvLTuH.css`), and grid rule `.tag:after { color:var(--color-charcoal) }`.
4. **Interactive Detail & Feature Matrix (<section.page:nth(2)> — `WE ARE A FULL-SERVICE CREATIVE AGE`)**:
   - Landmark `<section class="page page-home">` framing `WE ARE A FULL-SERVICE CREATIVE AGENCY BUILDING WO...` and `「 WE ARE A FULL-SERVICE CREATIVE AGENCY BUILDING...` (*"Where your vision goes to grow"*) with `#ffffff` surface cards, `#ffa500` accents, and `.media { transition:filter .4s var(--easing-motion) }`.
5. **Colophon & Global Directory Footer (<footer.wp-seo> — `https://seemecreative.com/`)**:
   - Landmark `<footer class="wp-seo">` anchoring `SEE ME Creative` footer links (`001 Work · 002 Artists · 003 About · 004 News`), copy *"WE ARE A FULL-SERVICE CREATIVE AGENCY BUILDING WO..."*, and `#ffa500` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Where your vision goes to grow` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `56%`): Active landmark `Merrell` · sticky/fixed elements: `1`
- **Step 03** (`y=1522px`, `100%`): Active landmark `Where artists can be and become` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Listing Route (`/work/`)**: `https://seemecreative.com/work/` — H1: `work`, scrollHeight `900px`, transition `MPA` (`1196ms`)
- **Detail Route (`/featured/merrell-holiday-2/`)**: `https://seemecreative.com/featured/merrell-holiday-2/` — H1: `Merrell – Gift The What If`, scrollHeight `5707px`, transition `direct` (`1698ms`)
- **About Route (`/about/`)**: `https://seemecreative.com/about/` — H1: `About`, scrollHeight `3119px`, transition `direct` (`726ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: seemecreative-com (SEE ME Creative)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `seemecreative-com` (**SEE ME Creative** — `https://seemecreative.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f8f7f7` canvas, `#333333` ink, `#ffa500` accent).
- **Identity & Domain Context**: SEE ME emerged from the desire to forge a creative environment that reimagines the ways in which we tell, create, and share stories.
- **Primary Substrate**: `#f8f7f7` (live computed `html` `background-color` (`computed_styles.json`)), **Primary Ink**: `#333333`, **Accent / Highlight**: `#ffa500`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f8f7f7` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#333333` primary typography and `#ffa500` accents.
  - **Grounded Typographic Hierarchy**: Uses `ABC Favorit` across display (`SEE ME Creative`) and body copy, paired with `ABC Favorit Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 20px`, padding `25px`) with `cubic-bezier(0.4,0,0.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `seemecreative-com` in your global stylesheet:

:root {
  /* SEE ME Creative (seemecreative-com) — Live-Grounded CSS Variables */
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
- **Primary Canvas Substrate**: `#f8f7f7` — grounded in live computed `html` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#333333` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `:after { background-color: #ffffff }`
- **Interactive Accent / Highlight**: `#ffa500` — grounded in `.menu a.router-link-active .index { color: orange }` (`#ffa500`)
- **Secondary / Muted Copy**: `#ffa500` — grounded in `.glyph { color: orange }` (`#ffa500`)
- **Structural Hairline Border**: `#ffa500` — grounded in `path { stroke: #ffa500 }`
- **Variable Token (`--color-black`)**: `#000000` — grounded in `var(--color-black)` in `:root`
- **Variable Token (`--color-gray`)**: `#b2b2b2` — grounded in `var(--color-gray)` in `:root`
- **Variable Token (`--color-orange`)**: `#ff5600` — grounded in `var(--color-orange)` in `:root`
- **Variable Token (`--color-orange-inverse`)**: `#00a9ff` — grounded in `var(--color-orange-inverse)` in `:root`
- **Variable Token (`--color-off-white`)**: `#f9f3f2` — grounded in `var(--color-off-white)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×2484px` (multi-frame vertical journey filmstrip (2484px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `25px` lateral canvas padding with `20px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 20px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `25px` horizontal padding
- **Media Queries**: `@media only screen and (max-width:850px)`, `@media only screen and (max-width:1024px)`, `@media only screen and (min-width:1800px)`, `@media only screen and (max-width:1799px)`
- **Corner Radii**: `2px`, `15px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `ABC Favorit`
- **Body Font Stack**: `ABC Favorit`
- **Monospace / Technical Font Stack**: `ABC Favorit Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 32px`, `line-height: normal`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 50px`, `line-height: 45px`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 18px`, `line-height: 130%`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--unit-margin-small: 10px`, `--unit-max-width-small: 680px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `seemecreative-com` (`SEE ME Creative`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.global-header> — `seemecreative-com`)**:
   - DOM & Selectors: Landmark `<header class="global-header header">` (`1440x66px`) hosting `SEE ME Creative` navigation (`001 Work · 002 Artists · 003 About · 004 News`), DOM attributes (`data-capo`, `data-v-344bacdf`, `data-v-bd05448e`, `data-v-61c5c60e`), and stylesheet rule `.tag { color:var(--color-charcoal);font-size:10px;font-weight:400;line-height:201% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.global-header> — `seemecreative-com`)` (`seemecreative-com`) adapts across `@media only screen and (max-width:850px)`, `@media only screen and (max-width:1024px)`, `@media only screen and (min-width:1800px)`, `@media only screen and (max-width:1799px)` with `cubic-bezier(0.4,0,0.2,1)` transitions and links `001 Work · 002 Artists · 003 About · 004 News`.
2. **Hero Stage & Focal Lead (<section.page> — `SEE ME Creative`)**:
   - DOM & Selectors: Landmark `<section class="page page-home">` presenting display lead `SEE ME Creative` and copy excerpt *"sayhello@seemecreative.com"* over `#f8f7f7` canvas and `#333333` ink.
   - Responsive Contract: Hero stage (`1280×2484px` desktop / `390×2616px` mobile) sets `#f8f7f7` background with `#333333` headline `SEE ME Creative`.
3. **Primary Showcase & Content Grid (<section.page-home> — `Where your vision goes to grow`)**:
   - DOM & Selectors: Landmark `<section class="page page-home">` rendering section `Where your vision goes to grow` with copy *"SEE ME Creative"*, asset references (`entry.BKkY1yHX.css`, `wp-image.abO9u4pg.css`, `grid-work.Dsp1qX9O.css`, `grid-masonry.BnNvLTuH.css`), and grid rule `.tag:after { color:var(--color-charcoal) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.page-home> — `Where your vision goes to grow`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 20px`) on desktop and Single-column vertical stack at `390px` viewport width with `25px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.page:nth(2)> — `WE ARE A FULL-SERVICE CREATIVE AGE`)**:
   - DOM & Selectors: Landmark `<section class="page page-home">` framing `WE ARE A FULL-SERVICE CREATIVE AGENCY BUILDING WO...` and `「 WE ARE A FULL-SERVICE CREATIVE AGENCY BUILDING...` (*"Where your vision goes to grow"*) with `#ffffff` surface cards, `#ffa500` accents, and `.media { transition:filter .4s var(--easing-motion) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.page:nth(2)> — `WE ARE A FULL-SERVICE CREATIVE AGE`)` uses `2px`, `15px` radii, `#ffa500` highlights, and assets (entry.BKkY1yHX.css, wp-image.abO9u4pg.css, grid-work.Dsp1qX9O.css).
5. **Colophon & Global Directory Footer (<footer.wp-seo> — `https://seemecreative.com/`)**:
   - DOM & Selectors: Landmark `<footer class="wp-seo">` anchoring `SEE ME Creative` footer links (`001 Work · 002 Artists · 003 About · 004 News`), copy *"WE ARE A FULL-SERVICE CREATIVE AGENCY BUILDING WO..."*, and `#ffa500` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wp-seo> — `https://seemecreative.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `25px` lateral canvas padding with `20px` grid gap and attributes (data-capo, data-v-344bacdf, data-v-bd05448e).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"sayhello@seemecreative.com"*

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
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.2,1)`)**: Governs interactive state transitions across `<header.global-header>` and `<section.page-home>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.page>` and `<section.page-home>` interactive targets.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `2422px` across 3 distinct viewport chapters.
- **Vertical Chapter Sequence**: Where your vision goes to grow (0%) -> Merrell (56%) -> Where artists can be and be... (100%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `color, borderColor` with `0.4s cubic-bezier(0.4, 0, 0.2, 1)`.
- **Multi-Page Routes**: Scaffold internal routes `/work/` (listing, MPA), `/featured/merrell-holiday-2/` (detail, direct), `/about/` (about, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `seemecreative-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Where your vision goes to grow | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `56%` | Merrell | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `1522px` | `100%` | Where artists can be and become | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Where your vision goes to grow | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `2176px` | `50%` | Bumble | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `4353px` | `100%` | Imani Dennison | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://seemecreative.com/work/` | work | `900px` | `MPA` (`1196ms`) | [subpage-01-work.webp](assets/subpage-01-work.webp) |
| `2` | `detail` | `https://seemecreative.com/featured/merrell-holiday-2/` | Merrell – Gift The What If | `5707px` | `direct` (`1698ms`) | [subpage-02-featured-merrell-holiday-2.webp](assets/subpage-02-featured-merrell-holiday-2.webp) |
| `3` | `about` | `https://seemecreative.com/about/` | About | `3119px` | `direct` (`726ms`) | [subpage-03-about.webp](assets/subpage-03-about.webp) |

