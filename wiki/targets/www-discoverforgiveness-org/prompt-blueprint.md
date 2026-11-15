---
title: "UI Prompt Blueprint: www-discoverforgiveness-org"
date: 2026-11-15
target: "[[overview|www-discoverforgiveness-org]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fefefb` canvas, `#433f35` ink, `#abaa9c` accent)"
---

# UI Design System & Master Generation Blueprint: www-discoverforgiveness-org

> **Discover Forgiveness · Templeton World Charity Foundation** (https://www.discoverforgiveness.org/) — Explore the transformative power of forgiveness at Discover Forgiveness. Our experts, from psychologists to spiritual leaders, offer insi...

![Desktop Viewport Capture (1440x6243)](file:///root/projects/fleet/wiki/targets/www-discoverforgiveness-org/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Discover Forgiveness · Templeton World Charity Foundation** (`https://www.discoverforgiveness.org/`). Explore the transformative power of forgiveness at Discover Forgiveness. Our experts, from psychologists to spiritual leaders, offer insi...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fefefb` canvas, `#433f35` ink, `#abaa9c` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fefefb` (`var(--off-white)` in `:root`) paired with `#433f35` primary typography and `#abaa9c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Area Normal` for display copy (`Discover Forgiveness`) with `Queens` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.445,.05,.55,.95)` easing and Swiper Touch Carousel Engine, Lottie Vector Animation Player.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-discoverforgiveness-org/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×6243px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `www-discoverforgiveness-org` stylesheet.
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fefefb` | `var(--off-white)` in `:root` |
| **Primary Typography Ink** | `#433f35` | `var(--dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6251d2` | `var(--purple3)` in `:root` |
| **Interactive Accent / Highlight** | `#abaa9c` | `var(--tan5)` in `:root` |
| **Secondary / Muted Copy** | `#fbfaf4` | `var(--tan)` in `:root` |
| **Structural Hairline Border** | `#777269` | `var(--dk-gray)` in `:root` |
| **Variable Token (`--purple_transp`)** | `#8170f033` | `var(--purple_transp)` in `:root` |
| **Variable Token (`--tan4`)** | `#cbc8be` | `var(--tan4)` in `:root` |
| **Variable Token (`--tan3`)** | `#e2e2d5` | `var(--tan3)` in `:root` |
| **Variable Token (`--tan2`)** | `#f0f0e5` | `var(--tan2)` in `:root` |
| **Variable Token (`--transparent`)** | `#0000` | `var(--transparent)` in `:root` |
| **Variable Token (`--purple1`)** | `#d8d8e9` | `var(--purple1)` in `:root` |
| **Variable Token (`--purple2`)** | `#bfbee0` | `var(--purple2)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--off-white` | `#fefefb` | Canvas / Surface Token |
| `--dark` | `#433f35` | Canvas / Surface Token |
| `--purple3` | `#6251d2` | Color / Atmospheric Token |
| `--black` | `black` | Canvas / Surface Token |
| `--white` | `white` | Canvas / Surface Token |
| `--tan5` | `#abaa9c` | Color / Atmospheric Token |
| `--tan` | `#fbfaf4` | Color / Atmospheric Token |
| `--purple_transp` | `#8170f033` | Color / Atmospheric Token |
| `--dk-gray` | `#777269` | Color / Atmospheric Token |
| `--tan4` | `#cbc8be` | Color / Atmospheric Token |
| `--tan3` | `#e2e2d5` | Color / Atmospheric Token |
| `--tan2` | `#f0f0e5` | Color / Atmospheric Token |
| `--transparent` | `#0000` | Color / Atmospheric Token |
| `--purple1` | `#d8d8e9` | Color / Atmospheric Token |
| `--purple2` | `#bfbee0` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Area Normal`.
- **Primary Body Stack**: `Queens`.
- **Technical / Metadata Stack**: `IBM Plex Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--blush1: #f5bccb`; rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: CSS variables `--blush2: #eab`; rule `h2` (`font-size: 32px`, `line-height: 36px`).
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.445,.05,.55,.95)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-discoverforgiveness-org` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-discoverforgiveness-org` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-discoverforgiveness-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.445,.05,.55,.95)`)**: Governs interactive state transitions across `<header.section_header37>` and `<section.section_layout349>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Discover Forgiveness · Templeton World Cha │
│ ====================================================================== │
│ [ <header.section_header37 | Educators · Faith Leaders · Anthropolo ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.section_layout134>                          |   │
│ | H1: Discover Forgiveness                                         |   │
│ | Substrate: #fefefb    | Ink: #433f35    | Accent: #abaa9c        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section_layout349) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | What is Discover forgiveness |  | Forgiveness Tools            | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.section_he] -> [<section.section_l] -> [<section.section_l] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer3_compon) | https://www.discoverforgiveness.or │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.section_header37> — `www-discoverforgiveness-org`)**:
   - Landmark `<header class="section_header37">` hosting `Discover Forgiveness · Templeton Wor` navigation (`Educators · Faith Leaders · Anthropology · Art · Digital Landscape`), DOM attributes (`data-wf-domain="www.discoverforgivene..."`, `data-wf-page="64b81f977202559487efb8c0"`, `data-wf-site="64b81f977202559487efb843"`, `data-animation="default"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.section_layout134> — `Discover Forgiveness`)**:
   - Landmark `<section class="section_layout134">` presenting display lead `Discover Forgiveness` and copy excerpt *"Discover Forgiveness"* over `#fefefb` canvas and `#433f35` ink.
3. **Primary Showcase & Content Grid (<section.section_layout349> — `What is Discover forgiveness?`)**:
   - Landmark `<section class="section_layout349">` rendering section `What is Discover forgiveness?` with copy *"Frontline workers include mental health professionals, faith lead"*, asset references (`cdn.prod.website-files.com`, `discover-forgiveness.webflow.shar...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section_blog41> — `Forgiveness Tools`)**:
   - Landmark `<section class="section_blog41">` framing `Forgiveness Tools` and `Research` (*"Curious About Forgiveness Science"*) with `#6251d2` surface cards, `#abaa9c` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer3_component> — `https://www.discoverforgiveness.org/`)**:
   - Landmark `<footer class="footer3_component">` anchoring `Discover Forgiveness · Templeton` footer links (`Educators · Faith Leaders · Anthropology · Art · Digital Landscape`), copy *"Mental Health Professionals"*, and `#777269` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-discoverforgiveness-org (Discover Forgiveness · Templeton World Charity Foundation)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-discoverforgiveness-org` (**Discover Forgiveness · Templeton World Charity Foundation** — `https://www.discoverforgiveness.org/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fefefb` canvas, `#433f35` ink, `#abaa9c` accent).
- **Identity & Domain Context**: Explore the transformative power of forgiveness at Discover Forgiveness. Our experts, from psychologists to spiritual leaders, offer insi...
- **Primary Substrate**: `#fefefb` (`var(--off-white)` in `:root`), **Primary Ink**: `#433f35`, **Accent / Highlight**: `#abaa9c`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fefefb` (`var(--off-white)` in `:root`) paired with `#433f35` primary typography and `#abaa9c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Area Normal` for display copy (`Discover Forgiveness`) with `Queens` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.445,.05,.55,.95)` easing and Swiper Touch Carousel Engine, Lottie Vector Animation Player.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-discoverforgiveness-org` in your global stylesheet:

:root {
  /* Discover Forgiveness · Templeton World Charity Foundation (www-discoverforgiveness-org) — Ground-Truth Extracted CSS Variables */
  --w-backdrop-animation: initial; /* Motion / Easing Token (www-discoverforgiveness-org) */
  --off-white: #fefefb; /* Canvas / Surface Token (www-discoverforgiveness-org) */
  --dark: #433f35; /* Canvas / Surface Token (www-discoverforgiveness-org) */
  --purple3: #6251d2; /* Color / Atmospheric Token (www-discoverforgiveness-org) */
  --black: black; /* Canvas / Surface Token (www-discoverforgiveness-org) */
  --white: white; /* Canvas / Surface Token (www-discoverforgiveness-org) */
  --tan5: #abaa9c; /* Color / Atmospheric Token (www-discoverforgiveness-org) */
  --tan: #fbfaf4; /* Color / Atmospheric Token (www-discoverforgiveness-org) */
  --purple_transp: #8170f033; /* Color / Atmospheric Token (www-discoverforgiveness-org) */
  --dk-gray: #777269; /* Color / Atmospheric Token (www-discoverforgiveness-org) */
  --tan4: #cbc8be; /* Color / Atmospheric Token (www-discoverforgiveness-org) */
  --tan3: #e2e2d5; /* Color / Atmospheric Token (www-discoverforgiveness-org) */
  --tan2: #f0f0e5; /* Color / Atmospheric Token (www-discoverforgiveness-org) */
  --transparent: #0000; /* Color / Atmospheric Token (www-discoverforgiveness-org) */
  --purple1: #d8d8e9; /* Color / Atmospheric Token (www-discoverforgiveness-org) */
  --purple2: #bfbee0; /* Color / Atmospheric Token (www-discoverforgiveness-org) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fefefb` — grounded in `var(--off-white)` in `:root`
- **Primary Typography Ink**: `#433f35` — grounded in `var(--dark)` in `:root`
- **Elevated Surface / Card Substrate**: `#6251d2` — grounded in `var(--purple3)` in `:root`
- **Interactive Accent / Highlight**: `#abaa9c` — grounded in `var(--tan5)` in `:root`
- **Secondary / Muted Copy**: `#fbfaf4` — grounded in `var(--tan)` in `:root`
- **Structural Hairline Border**: `#777269` — grounded in `var(--dk-gray)` in `:root`
- **Variable Token (`--purple_transp`)**: `#8170f033` — grounded in `var(--purple_transp)` in `:root`
- **Variable Token (`--tan4`)**: `#cbc8be` — grounded in `var(--tan4)` in `:root`
- **Variable Token (`--tan3`)**: `#e2e2d5` — grounded in `var(--tan3)` in `:root`
- **Variable Token (`--tan2`)**: `#f0f0e5` — grounded in `var(--tan2)` in `:root`
- **Variable Token (`--transparent`)**: `#0000` — grounded in `var(--transparent)` in `:root`
- **Variable Token (`--purple1`)**: `#d8d8e9` — grounded in `var(--purple1)` in `:root`
- **Variable Token (`--purple2`)**: `#bfbee0` — grounded in `var(--purple2)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×6243px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `www-discoverforgiveness-org` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Area Normal`
- **Body Font Stack**: `Queens`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **H1 Display Rule**: CSS variables `--blush1: #fefefb`; rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: CSS variables `--blush2: #fefefb`; rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy Rule**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Index Rule**: rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-discoverforgiveness-org` (`Discover Forgiveness · Templeton World Charity Foundation`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.section_header37> — `www-discoverforgiveness-org`)**:
   - DOM & Selectors: Landmark `<header class="section_header37">` hosting `Discover Forgiveness · Templeton Wor` navigation (`Educators · Faith Leaders · Anthropology · Art · Digital Landscape`), DOM attributes (`data-wf-domain="www.discoverforgivene..."`, `data-wf-page="64b81f977202559487efb8c0"`, `data-wf-site="64b81f977202559487efb843"`, `data-animation="default"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.section_header37> — `www-discoverforgiveness-org`)` (`www-discoverforgiveness-org`) adapts across `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)` with `cubic-bezier(.445,.05,.55,.95)` transitions and links `Educators · Faith Leaders · Anthropology · Art · Digital Landscape`.
2. **Hero Stage & Focal Lead (<section.section_layout134> — `Discover Forgiveness`)**:
   - DOM & Selectors: Landmark `<section class="section_layout134">` presenting display lead `Discover Forgiveness` and copy excerpt *"Discover Forgiveness"* over `#fefefb` canvas and `#433f35` ink.
   - Responsive Contract: Hero stage (`1440×6243px` desktop / `390×2400px` mobile) sets `#fefefb` background with `#433f35` headline `Discover Forgiveness`.
3. **Primary Showcase & Content Grid (<section.section_layout349> — `What is Discover forgiveness?`)**:
   - DOM & Selectors: Landmark `<section class="section_layout349">` rendering section `What is Discover forgiveness?` with copy *"Frontline workers include mental health professionals, faith lead"*, asset references (`cdn.prod.website-files.com`, `discover-forgiveness.webflow.shar...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section_layout349> — `What is Discover forgiveness?`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section_blog41> — `Forgiveness Tools`)**:
   - DOM & Selectors: Landmark `<section class="section_blog41">` framing `Forgiveness Tools` and `Research` (*"Curious About Forgiveness Science"*) with `#6251d2` surface cards, `#abaa9c` accents, and `summary { display: block; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section_blog41> — `Forgiveness Tools`)` uses `3px`, `100%`, `50%`, `2px` radii, `#abaa9c` highlights, and assets (cdn.prod.website-files.com, discover-forgiveness.webflow.shar..., fonts.googleapis.com).
5. **Colophon & Global Directory Footer (<footer.footer3_component> — `https://www.discoverforgiveness.org/`)**:
   - DOM & Selectors: Landmark `<footer class="footer3_component">` anchoring `Discover Forgiveness · Templeton` footer links (`Educators · Faith Leaders · Anthropology · Art · Digital Landscape`), copy *"Mental Health Professionals"*, and `#777269` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer3_component> — `https://www.discoverforgiveness.org/`)` aligns to `940px` extracted from `www-discoverforgiveness-org` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.discoverforgivene...", data-wf-page="64b81f977202559487efb8c0", data-wf-site="64b81f977202559487efb843").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Discover Forgiveness"*
- Copy Excerpt 2: *"Frontline workers include mental health professionals, faith leaders, and educator..."*
- Copy Excerpt 3: *"Curious About Forgiveness Science"*
- Copy Excerpt 4: *"Mental Health Professionals"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.445,.05,.55,.95)`
- **Extracted Stylesheet Rules (`www-discoverforgiveness-org`)**:
- `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`
- `body { margin: 0; }`
- `summary { display: block; }`
- `video { vertical-align: baseline; display: inline-block; }`
- `template { display: none; }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-discoverforgiveness-org` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-discoverforgiveness-org` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-discoverforgiveness-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.445,.05,.55,.95)`)**: Governs interactive state transitions across `<header.section_header37>` and `<section.section_layout349>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-discoverforgiveness-org`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
