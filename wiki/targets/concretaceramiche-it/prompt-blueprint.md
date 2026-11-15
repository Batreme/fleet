---
title: "UI Prompt Blueprint: concretaceramiche-it"
date: 2026-11-15
target: "concretaceramiche-it"
status: analyzed
capture: specimen
capture_desktop: dom
capture_mobile: specimen
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#720eec` canvas, `#fcfbfe` ink, `#ffba00` accent)"
---

# UI Design System & Master Generation Blueprint: concretaceramiche-it

> **Concreta Ceramiche Artigianali Fatte a Mano** (https://concretaceramiche.it/) — Ceramiche artigianali uniche, realizzate a mano nei Castelli Romani. Gres, stampa 3D e tradizione familiare in ogni pezzo. Scopri la coll...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Concreta Ceramiche Artigianali Fatte a Mano** (`https://concretaceramiche.it/`). Ceramiche artigianali uniche, realizzate a mano nei Castelli Romani. Gres, stampa 3D e tradizione familiare in ogni pezzo. Scopri la coll...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#720eec` canvas, `#fcfbfe` ink, `#ffba00` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#720eec` (`var(--woocommerce)` in `:root`) paired with `#fcfbfe` primary typography and `#ffba00` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Elgoc` for display copy (`ConCreta ceramiche artigianali Roma`) with `Inter` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `200px` container bounds (`gap: 50px`, padding `10px`) with `cubic-bezier(.075,.82,.165,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×9047px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `200px` extracted from `concretaceramiche-it` stylesheet.
- **Canvas Lateral Padding & Spacing**: `10px` lateral canvas padding with `50px` grid gap.
- **Border Radius Scale**: `3px`, `4px`, `23px`, `14px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 200px`, `gap: 50px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:576px)`, `@media (min-width:768px)`, `@media (min-width:992px)`, `@media (min-width:1200px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#720eec` | `var(--woocommerce)` in `:root` |
| **Primary Typography Ink** | `#008a20` | `var(--wc-green)` in `:root` |
| **Elevated Surface / Card Substrate** | `#a00` | `var(--wc-red)` in `:root` |
| **Interactive Accent / Highlight** | `#ffba00` | `var(--wc-orange)` in `:root` |
| **Secondary / Muted Copy** | `#2ea2cc` | `var(--wc-blue)` in `:root` |
| **Structural Hairline Border** | `#fcfbfe` | `var(--wc-primary-text)` in `:root` |
| **Variable Token (`--wc-secondary`)** | `#e9e6ed` | `var(--wc-secondary)` in `:root` |
| **Variable Token (`--wc-secondary-text`)** | `#515151` | `var(--wc-secondary-text)` in `:root` |
| **Variable Token (`--wc-highlight`)** | `#958e09` | `var(--wc-highlight)` in `:root` |
| **Variable Token (`--wc-content-bg`)** | `#fff` | `var(--wc-content-bg)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--border-radius` | `10px` | Elevation / Border Token |
| `--border-radius-md` | `20px` | Elevation / Border Token |
| `--padding-top-hero` | `102px` | Layout / Spatial Grid Token |
| `--padding-top-hero-home` | `380px` | Layout / Spatial Grid Token |
| `--woocommerce` | `#720eec` | Color / Atmospheric Token |
| `--wc-green` | `#008a20` | Color / Atmospheric Token |
| `--wc-red` | `#a00` | Color / Atmospheric Token |
| `--wc-orange` | `#ffba00` | Color / Atmospheric Token |
| `--wc-blue` | `#2ea2cc` | Color / Atmospheric Token |
| `--wc-primary` | `#720eec` | Brand / Palette Token |
| `--wc-primary-text` | `#fcfbfe` | Typography Ink Token |
| `--wc-secondary` | `#e9e6ed` | Brand / Palette Token |
| `--wc-secondary-text` | `#515151` | Typography Ink Token |
| `--wc-highlight` | `#958e09` | Canvas / Surface Token |
| `--wc-highligh-text` | `white` | Typography Ink Token |
| `--wc-content-bg` | `#fff` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Elgoc`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 25px`, `line-height: 32px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `14px`, `1rem`, `80%`, `75%`, `1em`).
- **Body Copy**: CSS variables `--cmplz_category_body_font_size: 12px`; rule `p` (`font-weight: 500`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 15px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.075,.82,.165,1)`, `cubic-bezier(.68,-.55,.265,1.55)`, `cubic-bezier(.19,1,.22,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `p a:hover`**: `transition: opacity .4s ease` extracted from `concretaceramiche-it` stylesheet.
- **Selector `media(max-width:1199px)`**: `transition: opacity .4s ease` extracted from `concretaceramiche-it` stylesheet.
- **Selector `data-animation=lines][class*=anim...`**: `transition: opacity .4s ease` extracted from `concretaceramiche-it` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.075,.82,.165,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<section.logo>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Concreta Ceramiche Artigianali Fatte a Man │
│ ====================================================================== │
│ [ <header.fixed>           | h o m e h o m e · c o r s i c o r s i  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.rank-math-schema>                           |   │
│ | H1: ConCreta ceramiche artigianali Roma                          |   │
│ | Substrate: #720eec    | Ink: #fcfbfe    | Accent: #ffba00        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.logo>            ) max-w: 200px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | La ceramica artigianale pren |  | Oggetti in ceramica nati dal | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 50px  ) | │
│ | [<header.fixed>] -> [<section.rank-math] -> [<section.logo>] |       │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.page-template>) | https://concretaceramiche.it/      │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.fixed> — `concretaceramiche-it`)**:
   - Landmark `<header class="fixed">` hosting `Concreta Ceramiche Artigianali Fatte` navigation (`h o m e h o m e · c o r s i c o r s i · S h o p S h o p · EN · Home`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `.cmplz-video.cmplz-iframe-styles { background-color:transparent }`.
2. **Hero Stage & Focal Lead (<section.rank-math-schema> — `ConCreta ceramiche artigianali Rom`)**:
   - Landmark `<section class="rank-math-schema">` presenting display lead `ConCreta ceramiche artigianali Roma` and copy excerpt *"Funzionale Sempre attivo"* over `#720eec` canvas and `#fcfbfe` ink.
3. **Primary Showcase & Content Grid (<section.logo> — `La ceramica artigianale prende for`)**:
   - Landmark `<section class="logo">` rendering section `La ceramica artigianale prende forma tra gesti an...` with copy *"L'archiviazione tecnica o l'accesso sono strettamente necessari a"*, asset references (`Elgoc-Bold.woff2`, `Elgoc-Regular.woff2`, `Inter28pt-Medium.woff2`, `Inter28pt-Regular.woff2`), and grid rule `.cmplz-video.cmplz-hidden { visibility:hidden !important }`.
4. **Interactive Detail & Feature Matrix (<section.wp-singular> — `Oggetti in ceramica nati dall’inco`)**:
   - Landmark `<section class="wp-singular">` framing `Oggetti in ceramica nati dall’incontro tra tecnic...` and `Un luogo dove la terra diventa forma e prende vita` (*"L'archiviazione tecnica o l'accesso sono necessari per lo scopo l"*) with `#a00` surface cards, `#ffba00` accents, and `.cmplz-blocked-content-notice { display:none }`.
5. **Colophon & Global Directory Footer (<footer.page-template> — `https://concretaceramiche.it/`)**:
   - Landmark `<footer class="page-template">` anchoring `Concreta Ceramiche Artigianali F` footer links (`h o m e h o m e · c o r s i c o r s i · S h o p S h o p · EN · Home`), copy *"L'archiviazione tecnica o l'accesso che viene utilizzato esc"*, and `#fcfbfe` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: concretaceramiche-it (Concreta Ceramiche Artigianali Fatte a Mano)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `concretaceramiche-it` (**Concreta Ceramiche Artigianali Fatte a Mano** — `https://concretaceramiche.it/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#720eec` canvas, `#fcfbfe` ink, `#ffba00` accent).
- **Identity & Domain Context**: Ceramiche artigianali uniche, realizzate a mano nei Castelli Romani. Gres, stampa 3D e tradizione familiare in ogni pezzo. Scopri la coll...
- **Primary Substrate**: `#720eec` (`var(--woocommerce)` in `:root`), **Primary Ink**: `#fcfbfe`, **Accent / Highlight**: `#ffba00`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#720eec` (`var(--woocommerce)` in `:root`) paired with `#fcfbfe` primary typography and `#ffba00` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Elgoc` for display copy (`ConCreta ceramiche artigianali Roma`) with `Inter` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `200px` container bounds (`gap: 50px`, padding `10px`) with `cubic-bezier(.075,.82,.165,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `concretaceramiche-it` in your global stylesheet:

:root {
  /* Concreta Ceramiche Artigianali Fatte a Mano (concretaceramiche-it) — Ground-Truth Extracted CSS Variables */
  --border-radius: 10px; /* Elevation / Border Token (concretaceramiche-it) */
  --border-radius-md: 20px; /* Elevation / Border Token (concretaceramiche-it) */
  --padding-top-hero: 102px; /* Layout / Spatial Grid Token (concretaceramiche-it) */
  --padding-top-hero-home: 380px; /* Layout / Spatial Grid Token (concretaceramiche-it) */
  --woocommerce: #720eec; /* Color / Atmospheric Token (concretaceramiche-it) */
  --wc-green: #008a20; /* Color / Atmospheric Token (concretaceramiche-it) */
  --wc-red: #a00; /* Color / Atmospheric Token (concretaceramiche-it) */
  --wc-orange: #ffba00; /* Color / Atmospheric Token (concretaceramiche-it) */
  --wc-blue: #2ea2cc; /* Color / Atmospheric Token (concretaceramiche-it) */
  --wc-primary: #720eec; /* Brand / Palette Token (concretaceramiche-it) */
  --wc-primary-text: #fcfbfe; /* Typography Ink Token (concretaceramiche-it) */
  --wc-secondary: #e9e6ed; /* Brand / Palette Token (concretaceramiche-it) */
  --wc-secondary-text: #515151; /* Typography Ink Token (concretaceramiche-it) */
  --wc-highlight: #958e09; /* Canvas / Surface Token (concretaceramiche-it) */
  --wc-highligh-text: white; /* Typography Ink Token (concretaceramiche-it) */
  --wc-content-bg: #fff; /* Canvas / Surface Token (concretaceramiche-it) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#720eec` — grounded in `var(--woocommerce)` in `:root`
- **Primary Typography Ink**: `#008a20` — grounded in `var(--wc-green)` in `:root`
- **Elevated Surface / Card Substrate**: `#a00` — grounded in `var(--wc-red)` in `:root`
- **Interactive Accent / Highlight**: `#ffba00` — grounded in `var(--wc-orange)` in `:root`
- **Secondary / Muted Copy**: `#2ea2cc` — grounded in `var(--wc-blue)` in `:root`
- **Structural Hairline Border**: `#fcfbfe` — grounded in `var(--wc-primary-text)` in `:root`
- **Variable Token (`--wc-secondary`)**: `#e9e6ed` — grounded in `var(--wc-secondary)` in `:root`
- **Variable Token (`--wc-secondary-text`)**: `#515151` — grounded in `var(--wc-secondary-text)` in `:root`
- **Variable Token (`--wc-highlight`)**: `#958e09` — grounded in `var(--wc-highlight)` in `:root`
- **Variable Token (`--wc-content-bg`)**: `#fff` — grounded in `var(--wc-content-bg)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×9047px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `200px` extracted from `concretaceramiche-it` stylesheet
- **Padding & Gutters**: `10px` lateral canvas padding with `50px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 200px`, `gap: 50px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding
- **Media Queries**: `@media (min-width:576px)`, `@media (min-width:768px)`, `@media (min-width:992px)`, `@media (min-width:1200px)`
- **Corner Radii**: `3px`, `4px`, `23px`, `14px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Elgoc`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: rule `h1` (`font-size: 25px`, `line-height: 32px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `14px`, `1rem`, `80%`, `75%`, `1em`)
- **Body Copy Rule**: CSS variables `--cmplz_category_body_font_size: 12px`; rule `p` (`font-weight: 500`)
- **Metadata & Index Rule**: rule `small` (`font-size: 15px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `concretaceramiche-it` (`Concreta Ceramiche Artigianali Fatte a Mano`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.fixed> — `concretaceramiche-it`)**:
   - DOM & Selectors: Landmark `<header class="fixed">` hosting `Concreta Ceramiche Artigianali Fatte` navigation (`h o m e h o m e · c o r s i c o r s i · S h o p S h o p · EN · Home`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `.cmplz-video.cmplz-iframe-styles { background-color:transparent }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.fixed> — `concretaceramiche-it`)` (`concretaceramiche-it`) adapts across `@media (min-width:576px)`, `@media (min-width:768px)`, `@media (min-width:992px)`, `@media (min-width:1200px)` with `cubic-bezier(.075,.82,.165,1)`, `cubic-bezier(.68,-.55,.265,1.55)`, `cubic-bezier(.19,1,.22,1)` transitions and links `h o m e h o m e · c o r s i c o r s i · S h o p S h o p · EN · Home`.
2. **Hero Stage & Focal Lead (<section.rank-math-schema> — `ConCreta ceramiche artigianali Rom`)**:
   - DOM & Selectors: Landmark `<section class="rank-math-schema">` presenting display lead `ConCreta ceramiche artigianali Roma` and copy excerpt *"Funzionale Sempre attivo"* over `#720eec` canvas and `#fcfbfe` ink.
   - Responsive Contract: Hero stage (`1440×9047px` desktop / `390×2400px` mobile) sets `#720eec` background with `#fcfbfe` headline `ConCreta ceramiche artigianali Roma`.
3. **Primary Showcase & Content Grid (<section.logo> — `La ceramica artigianale prende for`)**:
   - DOM & Selectors: Landmark `<section class="logo">` rendering section `La ceramica artigianale prende forma tra gesti an...` with copy *"L'archiviazione tecnica o l'accesso sono strettamente necessari a"*, asset references (`Elgoc-Bold.woff2`, `Elgoc-Regular.woff2`, `Inter28pt-Medium.woff2`, `Inter28pt-Regular.woff2`), and grid rule `.cmplz-video.cmplz-hidden { visibility:hidden !important }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.logo> — `La ceramica artigianale prende for`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 200px`, `gap: 50px`) on desktop and Single-column vertical stack at `390px` viewport width with `10px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.wp-singular> — `Oggetti in ceramica nati dall’inco`)**:
   - DOM & Selectors: Landmark `<section class="wp-singular">` framing `Oggetti in ceramica nati dall’incontro tra tecnic...` and `Un luogo dove la terra diventa forma e prende vita` (*"L'archiviazione tecnica o l'accesso sono necessari per lo scopo l"*) with `#a00` surface cards, `#ffba00` accents, and `.cmplz-blocked-content-notice { display:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.wp-singular> — `Oggetti in ceramica nati dall’inco`)` uses `3px`, `4px`, `23px`, `14px` radii, `#ffba00` highlights, and assets (Elgoc-Bold.woff2, Elgoc-Regular.woff2, Inter28pt-Medium.woff2).
5. **Colophon & Global Directory Footer (<footer.page-template> — `https://concretaceramiche.it/`)**:
   - DOM & Selectors: Landmark `<footer class="page-template">` anchoring `Concreta Ceramiche Artigianali F` footer links (`h o m e h o m e · c o r s i c o r s i · S h o p S h o p · EN · Home`), copy *"L'archiviazione tecnica o l'accesso che viene utilizzato esc"*, and `#fcfbfe` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.page-template> — `https://concretaceramiche.it/`)` aligns to `200px` extracted from `concretaceramiche-it` stylesheet with `10px` lateral canvas padding with `50px` grid gap and attributes (data-wp-strategy="defer", data-wp-strategy="defer", data-wp-strategy="defer").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Funzionale Sempre attivo"*
- Copy Excerpt 2: *"L'archiviazione tecnica o l'accesso sono strettamente necessari al fine legittimo..."*
- Copy Excerpt 3: *"L'archiviazione tecnica o l'accesso sono necessari per lo scopo legittimo di memor..."*
- Copy Excerpt 4: *"L'archiviazione tecnica o l'accesso che viene utilizzato esclusivamente per scopi..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.075,.82,.165,1)`, `cubic-bezier(.68,-.55,.265,1.55)`, `cubic-bezier(.19,1,.22,1)`
- **Extracted Stylesheet Rules (`concretaceramiche-it`)**:
- `.cmplz-video.cmplz-iframe-styles { background-color:transparent }`
- `.cmplz-video.cmplz-hidden { visibility:hidden !important }`
- `.cmplz-blocked-content-notice { display:none }`
- `.cmplz-placeholder-parent { height:inherit }`
- `wp-video .cmplz-blocked-content-n... { display:block }`
- **Per-Selector Transition Rules**:
- **Selector `p a:hover`**: `transition: opacity .4s ease` extracted from `concretaceramiche-it` stylesheet.
- **Selector `media(max-width:1199px)`**: `transition: opacity .4s ease` extracted from `concretaceramiche-it` stylesheet.
- **Selector `data-animation=lines][class*=anim...`**: `transition: opacity .4s ease` extracted from `concretaceramiche-it` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.075,.82,.165,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<section.logo>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `concretaceramiche-it`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
