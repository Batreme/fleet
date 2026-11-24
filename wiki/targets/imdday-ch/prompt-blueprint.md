---
title: "UI Prompt Blueprint: imdday-ch"
date: 2026-11-24
captured_at: 2026-11-24
target: "imdday-ch"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: wheel
desktop_keyframes: 1
subpages_crawled: 0
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#b2b2b2` / `#bbbcc4`)"
---

# UI Design System & Master Generation Blueprint: imdday-ch

> **IMDDay 2026** (https://imdday.ch/) — Dirk Koy, born in 1977, is a Basel-based artist active in various fields of moving image creation. He is a digital world-builder who samp...

![Desktop Journey Filmstrip (1280x828)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **IMDDay 2026** (`https://imdday.ch/`). Dirk Koy, born in 1977, is a Basel-based artist active in various fields of moving image creation. He is a digital world-builder who samp...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#b2b2b2` / `#bbbcc4`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#b2b2b2` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#bbbcc4` accents.
  - **Grounded Typographic Hierarchy**: Uses `Neue Montreal` across display (`Getting there`) and body copy, paired with `Roboto Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1157px` container bounds (`gap: 0px 19.6922px`, padding `33.5386px`) with `cubic-bezier(0.37,0,0.63,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×828px` (`assets/desktop-journey.webp`, `1` keyframes up to `y=0px` / doc `8873px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1157px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `33.5386px` lateral canvas padding with `0px 19.6922px` grid gap.
- **Border Radius Scale**: `6px 6px 0px 0px`, `39.3843px`, `var(--bld-br)`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1157px`, `gap: 0px 19.6922px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `33.5386px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 768px)`, `@media (min-width: 769px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#b2b2b2` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#bbbcc4` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#bbbcc4` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#8e8e8e` | `.Speakers_Item { border-bottom: #8e8e8e }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--main-font` | `"Neue Montreal"` | Typography / Scale Token |
| `--text-xs` | `calc(0.4231rem + 0.8974vw)` | Typography Ink Token |
| `--text-s` | `calc(-0.0962rem + 3.2051vw)` | Typography Ink Token |
| `--text-m` | `calc(1.2019rem + 1.6026vw)` | Typography Ink Token |
| `--text-l` | `calc(1.1731rem + 4.2308vw)` | Typography Ink Token |
| `--text-xl` | `calc(0.4519rem + 7.4359vw)` | Typography Ink Token |
| `--padding` | `calc(-33.8462px + 12.1795vw)` | Layout / Spatial Grid Token |
| `--left-column` | `calc(1.2019rem + 14.1026vw)` | Layout / Spatial Grid Token |
| `--space-xs` | `calc(7.6923px + 0.641vw)` | Layout / Spatial Grid Token |
| `--space-s` | `calc(2.1538px + 2.1795vw)` | Layout / Spatial Grid Token |
| `--space-m` | `calc(29.2308px + 1.6026vw)` | Layout / Spatial Grid Token |
| `--space-l` | `calc(50.7692px + 2.5641vw)` | Layout / Spatial Grid Token |
| `--ease-inout-sine` | `cubic-bezier(0.37, 0, 0.63, 1)` | Motion / Easing Token |
| `--ease-in-cubic` | `cubic-bezier(0.32, 0, 0.67, 0)` | Motion / Easing Token |
| `--ease-out-cubic` | `cubic-bezier(0.33, 1, 0.68, 1)` | Motion / Easing Token |
| `--ease-inout-cubic` | `cubic-bezier(0.65, 0, 0.35, 1)` | Motion / Easing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Neue Montreal`.
- **Primary Body Stack**: `Neue Montreal`.
- **Technical / Metadata Stack**: `Roboto Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 114.307px`, `line-height: 114.307px`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 114.307px`, `line-height: 114.307px`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 19.6922px`, `line-height: 23.6306px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 19.6922px`, `line-height: 19.6922px`, `font-weight: 400`); CSS variables `--text-xs: calc(0.4231rem + 0.8974vw)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.37,0,0.63,1)`, `cubic-bezier(0.32,0,0.67,0)`, `cubic-bezier(0.33,1,0.68,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.tp-fldv_b`**: `transition: border-radius .2s ease-in-out .2s` extracted from `imdday-ch` stylesheet.
- **Selector `.tp-fldv_m`**: `transition: transform .2s ease-in-out` extracted from `imdday-ch` stylesheet.
- **Selector `.tp-fldv_c`**: `transition: height .2s ease-in-out,opacity .2s linear,padding .2s ease-in-out` extracted from `imdday-ch` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.37,0,0.63,1)`)**: Governs interactive state transitions across `<header.Navigation_Main>` and `<article.Stage_Node>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `wheel` (max document height `8873px`, deepest scrollY reached `0px` across `1` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `WebGL/Canvas`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — IMDDay 2026                                │
│ ====================================================================== │
│ [ <header.Navigation_Mai (116x400px)  | T ickets · L ineup · T imeta ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.Speakers_Item> (w=1440px)                     | │
│ | H1: Getting there                                                  | │
│ | Substrate: #b2b2b2 | Ink: #ffffff | Accent: #bbbcc4                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.Stage_Node>) max-w: 1157px                 | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Elodie Anglade               |  | Immo Schneider               | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.Speakers_Item:nth) — Joëlle Bitton         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.Footer_Main>) | https://imdday.ch/                   │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px 19.6)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.Navigation_Main>) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<article.Speakers_Item>) — 390px Vertical Lead         | │
│ | H1: Getting there                                                  | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<article.Stage_Node>) — 1-Col Stack                | │
│ | [ Item 1: Elodie Anglade                                         ] | │
│ | [ Item 2: Immo Schneider                                         ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.Speakers_Item:n) — 1-Col (Joëlle Bitton)    | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.Footer_Main>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.Navigation_Main> — `imdday-ch`)**:
   - Landmark `<header class="Navigation_Main">` (`116x400px`) hosting `IMDDay 2026` navigation (`T ickets · L ineup · T imetable · G etting there · A bout`), DOM attributes (`data-tp-style="plugin-default"`, `data-engine="three.js r181"`, `data-config="%7B%22speed%22:0.2,%2..."`, `data-id="lineup"`), and stylesheet rule `selection { background: a1a1a1; color: white; }`.
2. **Hero Stage & Focal Lead (<article.Speakers_Item> — `Getting there`)**:
   - Landmark `<article class="Speakers_Item Stage_Node">` presenting display lead `Getting there` and copy excerpt *"Dirk Koy, born in 1977, is a Basel-based artist active in various"* over `#b2b2b2` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<article.Stage_Node> — `Elodie Anglade`)**:
   - Landmark `<article class="Speakers_Item Stage_Node">` rendering section `Elodie Anglade` with copy *"In his visual logic, traces are not static. They continue to evol"*, asset references (`favicon.image-6ZC672GS.svg`, `favicon-TJBRTTS6.png`, `index.html`, `index.js`), and grid rule `.Html_Visible { opacity: 1; }`.
4. **Interactive Detail & Feature Matrix (<article.Speakers_Item:nth(2)> — `Immo Schneider`)**:
   - Landmark `<article class="Speakers_Item Stage_Node">` framing `Immo Schneider` and `Joëlle Bitton` (*"Elodie Anglade is a media and interaction designer based in Switz"*) with `#ffffff` surface cards, `#bbbcc4` accents, and `canvas { position: absolute; width: 100%; height: 100%; }`.
5. **Colophon & Global Directory Footer (<footer.Footer_Main> — `https://imdday.ch/`)**:
   - Landmark `<footer class="Footer_Main">` anchoring `IMDDay 2026` footer links (`T ickets · L ineup · T imetable · G etting there · A bout`), copy *"Her work often sits at the intersection of image-making, ani"*, and `#8e8e8e` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Hero` · sticky/fixed elements: `2`

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: imdday-ch (IMDDay 2026)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `imdday-ch` (**IMDDay 2026** — `https://imdday.ch/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#b2b2b2` / `#bbbcc4`).
- **Identity & Domain Context**: Dirk Koy, born in 1977, is a Basel-based artist active in various fields of moving image creation. He is a digital world-builder who samp...
- **Primary Substrate**: `#b2b2b2` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#bbbcc4`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#b2b2b2` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#bbbcc4` accents.
  - **Grounded Typographic Hierarchy**: Uses `Neue Montreal` across display (`Getting there`) and body copy, paired with `Roboto Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1157px` container bounds (`gap: 0px 19.6922px`, padding `33.5386px`) with `cubic-bezier(0.37,0,0.63,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `imdday-ch` in your global stylesheet:

:root {
  /* IMDDay 2026 (imdday-ch) — Live-Grounded CSS Variables */
  --main-font: "Neue Montreal"; /* Typography / Scale Token (imdday-ch) */
  --text-xs: calc(0.4231rem + 0.8974vw); /* Typography Ink Token (imdday-ch) */
  --text-s: calc(-0.0962rem + 3.2051vw); /* Typography Ink Token (imdday-ch) */
  --text-m: calc(1.2019rem + 1.6026vw); /* Typography Ink Token (imdday-ch) */
  --text-l: calc(1.1731rem + 4.2308vw); /* Typography Ink Token (imdday-ch) */
  --text-xl: calc(0.4519rem + 7.4359vw); /* Typography Ink Token (imdday-ch) */
  --padding: calc(-33.8462px + 12.1795vw); /* Layout / Spatial Grid Token (imdday-ch) */
  --left-column: calc(1.2019rem + 14.1026vw); /* Layout / Spatial Grid Token (imdday-ch) */
  --space-xs: calc(7.6923px + 0.641vw); /* Layout / Spatial Grid Token (imdday-ch) */
  --space-s: calc(2.1538px + 2.1795vw); /* Layout / Spatial Grid Token (imdday-ch) */
  --space-m: calc(29.2308px + 1.6026vw); /* Layout / Spatial Grid Token (imdday-ch) */
  --space-l: calc(50.7692px + 2.5641vw); /* Layout / Spatial Grid Token (imdday-ch) */
  --ease-inout-sine: cubic-bezier(0.37, 0, 0.63, 1); /* Motion / Easing Token (imdday-ch) */
  --ease-in-cubic: cubic-bezier(0.32, 0, 0.67, 0); /* Motion / Easing Token (imdday-ch) */
  --ease-out-cubic: cubic-bezier(0.33, 1, 0.68, 1); /* Motion / Easing Token (imdday-ch) */
  --ease-inout-cubic: cubic-bezier(0.65, 0, 0.35, 1); /* Motion / Easing Token (imdday-ch) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#b2b2b2` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in live computed `footer` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#bbbcc4` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#bbbcc4` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#8e8e8e` — grounded in `.Speakers_Item { border-bottom: #8e8e8e }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×828px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1157px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `33.5386px` lateral canvas padding with `0px 19.6922px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1157px`, `gap: 0px 19.6922px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `33.5386px` horizontal padding
- **Media Queries**: `@media (min-width: 768px)`, `@media (min-width: 769px)`
- **Corner Radii**: `6px 6px 0px 0px`, `39.3843px`, `var(--bld-br)`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Neue Montreal`
- **Body Font Stack**: `Neue Montreal`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 114.307px`, `line-height: 114.307px`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 114.307px`, `line-height: 114.307px`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 19.6922px`, `line-height: 23.6306px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 19.6922px`, `line-height: 19.6922px`, `font-weight: 400`); CSS variables `--text-xs: calc(0.4231rem + 0.8974vw)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `imdday-ch` (`IMDDay 2026`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.Navigation_Main> — `imdday-ch`)**:
   - DOM & Selectors: Landmark `<header class="Navigation_Main">` (`116x400px`) hosting `IMDDay 2026` navigation (`T ickets · L ineup · T imetable · G etting there · A bout`), DOM attributes (`data-tp-style="plugin-default"`, `data-engine="three.js r181"`, `data-config="%7B%22speed%22:0.2,%2..."`, `data-id="lineup"`), and stylesheet rule `selection { background: a1a1a1; color: white; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.Navigation_Main> — `imdday-ch`)` (`imdday-ch`) adapts across `@media (min-width: 768px)`, `@media (min-width: 769px)` with `cubic-bezier(0.37,0,0.63,1)`, `cubic-bezier(0.32,0,0.67,0)`, `cubic-bezier(0.33,1,0.68,1)` transitions and links `T ickets · L ineup · T imetable · G etting there · A bout`.
2. **Hero Stage & Focal Lead (<article.Speakers_Item> — `Getting there`)**:
   - DOM & Selectors: Landmark `<article class="Speakers_Item Stage_Node">` presenting display lead `Getting there` and copy excerpt *"Dirk Koy, born in 1977, is a Basel-based artist active in various"* over `#b2b2b2` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1280×828px` desktop / `390×2616px` mobile) sets `#b2b2b2` background with `#ffffff` headline `Getting there`.
3. **Primary Showcase & Content Grid (<article.Stage_Node> — `Elodie Anglade`)**:
   - DOM & Selectors: Landmark `<article class="Speakers_Item Stage_Node">` rendering section `Elodie Anglade` with copy *"In his visual logic, traces are not static. They continue to evol"*, asset references (`favicon.image-6ZC672GS.svg`, `favicon-TJBRTTS6.png`, `index.html`, `index.js`), and grid rule `.Html_Visible { opacity: 1; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.Stage_Node> — `Elodie Anglade`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1157px`, `gap: 0px 19.6922px`) on desktop and Single-column vertical stack at `390px` viewport width with `33.5386px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.Speakers_Item:nth(2)> — `Immo Schneider`)**:
   - DOM & Selectors: Landmark `<article class="Speakers_Item Stage_Node">` framing `Immo Schneider` and `Joëlle Bitton` (*"Elodie Anglade is a media and interaction designer based in Switz"*) with `#ffffff` surface cards, `#bbbcc4` accents, and `canvas { position: absolute; width: 100%; height: 100%; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.Speakers_Item:nth(2)> — `Immo Schneider`)` uses `6px 6px 0px 0px`, `39.3843px`, `var(--bld-br)`, `2px` radii, `#bbbcc4` highlights, and assets (favicon.image-6ZC672GS.svg, favicon-TJBRTTS6.png, index.html).
5. **Colophon & Global Directory Footer (<footer.Footer_Main> — `https://imdday.ch/`)**:
   - DOM & Selectors: Landmark `<footer class="Footer_Main">` anchoring `IMDDay 2026` footer links (`T ickets · L ineup · T imetable · G etting there · A bout`), copy *"Her work often sits at the intersection of image-making, ani"*, and `#8e8e8e` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.Footer_Main> — `https://imdday.ch/`)` aligns to `1157px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `33.5386px` lateral canvas padding with `0px 19.6922px` grid gap and attributes (data-tp-style="plugin-default", data-engine="three.js r181", data-config="%7B%22speed%22:0.2,%2...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Dirk Koy, born in 1977, is a Basel-based artist active in various fields of moving..."*
- Copy Excerpt 2: *"In his visual logic, traces are not static. They continue to evolve and subtly uns..."*
- Copy Excerpt 3: *"Elodie Anglade is a media and interaction designer based in Switzerland, working a..."*
- Copy Excerpt 4: *"Her work often sits at the intersection of image-making, animation, and interactio..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.37,0,0.63,1)`, `cubic-bezier(0.32,0,0.67,0)`, `cubic-bezier(0.33,1,0.68,1)`
- **Extracted Stylesheet Rules (`imdday-ch`)**:
- `selection { background: a1a1a1; color: white; }`
- `.Html_Visible { opacity: 1; }`
- `canvas { position: absolute; width: 100%; height: 100%; }`
- `.Speakers_Main { padding: var(--padding); }`
- `.Speakers_Item { border-bottom: 1px solid 00000033; }`
- **Per-Selector Transition Rules**:
- **Selector `.tp-fldv_b`**: `transition: border-radius .2s ease-in-out .2s` extracted from `imdday-ch` stylesheet.
- **Selector `.tp-fldv_m`**: `transition: transform .2s ease-in-out` extracted from `imdday-ch` stylesheet.
- **Selector `.tp-fldv_c`**: `transition: height .2s ease-in-out,opacity .2s linear,padding .2s ease-in-out` extracted from `imdday-ch` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.37,0,0.63,1)`)**: Governs interactive state transitions across `<header.Navigation_Main>` and `<article.Stage_Node>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `wheel` vertical progression up to `8873px` across 1 distinct viewport chapters using WebGL/Canvas.
- **Vertical Chapter Sequence**: Hero (0%).

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `imdday-ch`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Hero | `2` | [desktop-step-01.webp](assets/desktop-step-01.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Hero | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `2319px` | `50%` | Section @ 50% | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `4639px` | `100%` | Footer | [mobile-step-03.webp](assets/mobile-step-03.webp) |

