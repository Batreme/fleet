---
title: "UI Prompt Blueprint: miligram-pt"
date: 2026-11-15
target: "[[overview|miligram-pt]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#720eec` canvas, `#fcfbfe` ink, `#ffba00` accent)"
---

# UI Design System & Master Generation Blueprint: miligram-pt

> **Miligram Brand Agency** (https://miligram.pt) — Somos uma agência de Branding, Design e Marketing Digital em Portugal. Criamos marcas, websites e experiências digitais que fazem negócio...

![Desktop Viewport Capture (1440x11905)](file:///root/projects/fleet/wiki/targets/miligram-pt/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Miligram Brand Agency** (`https://miligram.pt`). Somos uma agência de Branding, Design e Marketing Digital em Portugal. Criamos marcas, websites e experiências digitais que fazem negócio...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#720eec` canvas, `#fcfbfe` ink, `#ffba00` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#720eec` (`var(--woocommerce)` in `:root`) paired with `#fcfbfe` primary typography and `#ffba00` accents.
  - **Extracted Typographic Hierarchy**: Pairs `WooCommerce` for display copy (`Carrinho`) with `neue-haas-unica` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `768px` container bounds (`gap: 3px`, padding `10px`) with `cubic-bezier(0.65,0,0.35,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/miligram-pt/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×11905px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `768px` extracted from `miligram-pt` stylesheet.
- **Canvas Lateral Padding & Spacing**: `10px` lateral canvas padding with `3px` grid gap.
- **Border Radius Scale**: `3px`, `50%`, `20px`, `100%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 768px`, `gap: 3px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media screen and (max-width: 768px) and (min-width: 446px)`, `@media screen and (max-width: 446px)`, `@media (max-width:1024px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#720eec` | `var(--woocommerce)` in `:root` |
| **Primary Typography Ink** | `#007518` | `var(--wc-green)` in `:root` |
| **Elevated Surface / Card Substrate** | `#a00` | `var(--wc-red)` in `:root` |
| **Interactive Accent / Highlight** | `#ffba00` | `var(--wc-orange)` in `:root` |
| **Secondary / Muted Copy** | `#2ea2cc` | `var(--wc-blue)` in `:root` |
| **Structural Hairline Border** | `#fcfbfe` | `var(--wc-primary-text)` in `:root` |
| **Variable Token (`--wc-secondary`)** | `#e9e6ed` | `var(--wc-secondary)` in `:root` |
| **Variable Token (`--wc-secondary-text`)** | `#515151` | `var(--wc-secondary-text)` in `:root` |
| **Variable Token (`--wc-highlight`)** | `#958e09` | `var(--wc-highlight)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--column-gap` | `0px!important` | Layout / Spatial Grid Token |
| `--columns` | `1` | Layout / Spatial Grid Token |
| `--gap` | `20px` | Layout / Spatial Grid Token |
| `--spinner-color` | `rgba(100, 100, 100, 0.8)` | Brand / Palette Token |
| `--spinner-size` | `36px` | Layout / Spatial Grid Token |
| `--row-gap` | `20px` | Layout / Spatial Grid Token |
| `--woocommerce` | `#720eec` | Color / Atmospheric Token |
| `--wc-green` | `#007518` | Color / Atmospheric Token |
| `--wc-red` | `#a00` | Color / Atmospheric Token |
| `--wc-orange` | `#ffba00` | Color / Atmospheric Token |
| `--wc-blue` | `#2ea2cc` | Color / Atmospheric Token |
| `--wc-primary` | `#720eec` | Brand / Palette Token |
| `--wc-primary-text` | `#fcfbfe` | Typography Ink Token |
| `--wc-secondary` | `#e9e6ed` | Brand / Palette Token |
| `--wc-secondary-text` | `#515151` | Typography Ink Token |
| `--wc-highlight` | `#958e09` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `WooCommerce`.
- **Primary Body Stack**: `neue-haas-unica`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: 86px`, `line-height: 1.1em`, `font-weight: 300`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 64px`).
- **Body Copy**: rule `body` (`font-size: 62.5%`).
- **Metadata & Navigation Labels**: CSS variables `--e-global-typography-text-letter-spacing: -0.2px`, `--e-global-typography-f3906fe-letter-spacing: -0.2px`, `--e-global-typography-e59e9b9-letter-spacing: -0.2px`; rule `small` (`font-size: 15px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.65,0,0.35,1)`, `cubic-bezier(.795,-.035,0,1)`, `cubic-bezier(0.22,1,0.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `on .e-n-accordion-item-title-icon...`**: `transition: transform 0.4s cubic-bezier(0.65,0,0.35,1), opacity 0.3s ease` extracted from `miligram-pt` stylesheet.
- **Selector `ment-6884a37 .e-n-accordion-item-...`**: `transition: none !important` extracted from `miligram-pt` stylesheet.
- **Selector `media (prefers-reduced-motion: re...`**: `transition: none` extracted from `miligram-pt` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.65,0,0.35,1)`)**: Governs interactive state transitions across `<header.elementor>` and `<section.miligram-evolua>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Miligram Brand Agency                      │
│ ====================================================================== │
│ [ <header.elementor>       | Cultura · Serviços · Loja · Blog · PT  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.home>                                       |   │
│ | H1: Carrinho                                                     |   │
│ | Substrate: #720eec    | Ink: #fcfbfe    | Accent: #ffba00        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.miligram-evolua> ) max-w: 768px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Real Brands Content Photos V |  | for Real People              | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 3px   ) | │
│ | [<header.elementor>] -> [<section.home>] -> [<section.miligram-] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.elementor>    ) | https://miligram.pt                │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.elementor> — `miligram-pt`)**:
   - Landmark `<header class="elementor elementor-282">` hosting `Miligram Brand Agency` navigation (`Cultura · Serviços · Loja · Blog · PT`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.home> — `Carrinho`)**:
   - Landmark `<section class="home">` presenting display lead `Carrinho` and copy excerpt *"Pular para o conteúdo"* over `#720eec` canvas and `#fcfbfe` ink.
3. **Primary Showcase & Content Grid (<section.miligram-evolua> — `Real Brands Content Photos Videos `)**:
   - Landmark `<section class="miligram-evolua">` rendering section `Real Brands Content Photos Videos Design Websites` with copy *"O carrinho está vazio."*, asset references (`insight.min.js`, `oaiq.min.js`, `1509416_miligram.pt.js`, `gcm.min.js`), and grid rule `.lenis.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<article.miligram-evolua__block> — `for Real People`)**:
   - Landmark `<article class="miligram-evolua__block">` framing `for Real People` and `Aqui, o Branding é pensado como um todo.` (*"Brands Content Photos Videos Design Websites"*) with `#a00` surface cards, `#ffba00` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://miligram.pt`)**:
   - Landmark `<footer class="elementor elementor-371">` anchoring `Miligram Brand Agency` footer links (`Cultura · Serviços · Loja · Blog · PT`), copy *"Mais de 20 anos a redefinir o conceito de Branding. Da estra"*, and `#fcfbfe` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: miligram-pt (Miligram Brand Agency)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `miligram-pt` (**Miligram Brand Agency** — `https://miligram.pt`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#720eec` canvas, `#fcfbfe` ink, `#ffba00` accent).
- **Identity & Domain Context**: Somos uma agência de Branding, Design e Marketing Digital em Portugal. Criamos marcas, websites e experiências digitais que fazem negócio...
- **Primary Substrate**: `#720eec` (`var(--woocommerce)` in `:root`), **Primary Ink**: `#fcfbfe`, **Accent / Highlight**: `#ffba00`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#720eec` (`var(--woocommerce)` in `:root`) paired with `#fcfbfe` primary typography and `#ffba00` accents.
  - **Extracted Typographic Hierarchy**: Pairs `WooCommerce` for display copy (`Carrinho`) with `neue-haas-unica` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `768px` container bounds (`gap: 3px`, padding `10px`) with `cubic-bezier(0.65,0,0.35,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `miligram-pt` in your global stylesheet:

:root {
  /* Miligram Brand Agency (miligram-pt) — Ground-Truth Extracted CSS Variables */
  --column-gap: 0px!important; /* Layout / Spatial Grid Token (miligram-pt) */
  --columns: 1; /* Layout / Spatial Grid Token (miligram-pt) */
  --gap: 20px; /* Layout / Spatial Grid Token (miligram-pt) */
  --spinner-color: rgba(100, 100, 100, 0.8); /* Brand / Palette Token (miligram-pt) */
  --spinner-size: 36px; /* Layout / Spatial Grid Token (miligram-pt) */
  --row-gap: 20px; /* Layout / Spatial Grid Token (miligram-pt) */
  --woocommerce: #720eec; /* Color / Atmospheric Token (miligram-pt) */
  --wc-green: #007518; /* Color / Atmospheric Token (miligram-pt) */
  --wc-red: #a00; /* Color / Atmospheric Token (miligram-pt) */
  --wc-orange: #ffba00; /* Color / Atmospheric Token (miligram-pt) */
  --wc-blue: #2ea2cc; /* Color / Atmospheric Token (miligram-pt) */
  --wc-primary: #720eec; /* Brand / Palette Token (miligram-pt) */
  --wc-primary-text: #fcfbfe; /* Typography Ink Token (miligram-pt) */
  --wc-secondary: #e9e6ed; /* Brand / Palette Token (miligram-pt) */
  --wc-secondary-text: #515151; /* Typography Ink Token (miligram-pt) */
  --wc-highlight: #958e09; /* Canvas / Surface Token (miligram-pt) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#720eec` — grounded in `var(--woocommerce)` in `:root`
- **Primary Typography Ink**: `#007518` — grounded in `var(--wc-green)` in `:root`
- **Elevated Surface / Card Substrate**: `#a00` — grounded in `var(--wc-red)` in `:root`
- **Interactive Accent / Highlight**: `#ffba00` — grounded in `var(--wc-orange)` in `:root`
- **Secondary / Muted Copy**: `#2ea2cc` — grounded in `var(--wc-blue)` in `:root`
- **Structural Hairline Border**: `#fcfbfe` — grounded in `var(--wc-primary-text)` in `:root`
- **Variable Token (`--wc-secondary`)**: `#e9e6ed` — grounded in `var(--wc-secondary)` in `:root`
- **Variable Token (`--wc-secondary-text`)**: `#515151` — grounded in `var(--wc-secondary-text)` in `:root`
- **Variable Token (`--wc-highlight`)**: `#958e09` — grounded in `var(--wc-highlight)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×11905px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `768px` extracted from `miligram-pt` stylesheet
- **Padding & Gutters**: `10px` lateral canvas padding with `3px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 768px`, `gap: 3px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media screen and (max-width: 768px) and (min-width: 446px)`, `@media screen and (max-width: 446px)`, `@media (max-width:1024px)`
- **Corner Radii**: `3px`, `50%`, `20px`, `100%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `WooCommerce`
- **Body Font Stack**: `neue-haas-unica`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: 86px`, `line-height: 1.1em`, `font-weight: 300`)
- **H2 Section Rule**: rule `h2` (`font-size: 64px`)
- **Body Copy Rule**: rule `body` (`font-size: 62.5%`)
- **Metadata & Index Rule**: CSS variables `--e-global-typography-text-letter-spacing: -0.2px`, `--e-global-typography-f3906fe-letter-spacing: -0.2px`, `--e-global-typography-e59e9b9-letter-spacing: -0.2px`; rule `small` (`font-size: 15px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `miligram-pt` (`Miligram Brand Agency`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.elementor> — `miligram-pt`)**:
   - DOM & Selectors: Landmark `<header class="elementor elementor-282">` hosting `Miligram Brand Agency` navigation (`Cultura · Serviços · Loja · Blog · PT`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `html.lenis body { height:auto }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.elementor> — `miligram-pt`)` (`miligram-pt`) adapts across `@media (prefers-reduced-motion: reduce)`, `@media screen and (max-width: 768px) and (min-width: 446px)`, `@media screen and (max-width: 446px)`, `@media (max-width:1024px)` with `cubic-bezier(0.65,0,0.35,1)`, `cubic-bezier(.795,-.035,0,1)`, `cubic-bezier(0.22,1,0.36,1)` transitions and links `Cultura · Serviços · Loja · Blog · PT`.
2. **Hero Stage & Focal Lead (<section.home> — `Carrinho`)**:
   - DOM & Selectors: Landmark `<section class="home">` presenting display lead `Carrinho` and copy excerpt *"Pular para o conteúdo"* over `#720eec` canvas and `#fcfbfe` ink.
   - Responsive Contract: Hero stage (`1440×11905px` desktop / `390×2400px` mobile) sets `#720eec` background with `#fcfbfe` headline `Carrinho`.
3. **Primary Showcase & Content Grid (<section.miligram-evolua> — `Real Brands Content Photos Videos `)**:
   - DOM & Selectors: Landmark `<section class="miligram-evolua">` rendering section `Real Brands Content Photos Videos Design Websites` with copy *"O carrinho está vazio."*, asset references (`insight.min.js`, `oaiq.min.js`, `1509416_miligram.pt.js`, `gcm.min.js`), and grid rule `.lenis.lenis-stopped { overflow:clip }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.miligram-evolua> — `Real Brands Content Photos Videos `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 768px`, `gap: 3px`) on desktop and Single-column vertical stack at `390px` viewport width with `10px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.miligram-evolua__block> — `for Real People`)**:
   - DOM & Selectors: Landmark `<article class="miligram-evolua__block">` framing `for Real People` and `Aqui, o Branding é pensado como um todo.` (*"Brands Content Photos Videos Design Websites"*) with `#a00` surface cards, `#ffba00` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.miligram-evolua__block> — `for Real People`)` uses `3px`, `50%`, `20px`, `100%` radii, `#ffba00` highlights, and assets (insight.min.js, oaiq.min.js, 1509416_miligram.pt.js).
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://miligram.pt`)**:
   - DOM & Selectors: Landmark `<footer class="elementor elementor-371">` anchoring `Miligram Brand Agency` footer links (`Cultura · Serviços · Loja · Blog · PT`), copy *"Mais de 20 anos a redefinir o conceito de Branding. Da estra"*, and `#fcfbfe` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.elementor> — `https://miligram.pt`)` aligns to `768px` extracted from `miligram-pt` stylesheet with `10px` lateral canvas padding with `3px` grid gap and attributes (data-wp-strategy="defer", data-wp-strategy="defer", data-wp-strategy="defer").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Pular para o conteúdo"*
- Copy Excerpt 2: *"O carrinho está vazio."*
- Copy Excerpt 3: *"Brands Content Photos Videos Design Websites"*
- Copy Excerpt 4: *"Mais de 20 anos a redefinir o conceito de Branding. Da estratégia ao design, do di..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.65,0,0.35,1)`, `cubic-bezier(.795,-.035,0,1)`, `cubic-bezier(0.22,1,0.36,1)`
- **Extracted Stylesheet Rules (`miligram-pt`)**:
- `html.lenis body { height:auto }`
- `.lenis.lenis-stopped { overflow:clip }`
- `.lenis.lenis-smooth iframe { pointer-events:none }`
- `ccordion .e-n-accordion-item-titl... { display: grid !important; }`
- `e-n-accordion-item-title-icon .e-... { transform: rotate(0deg); opacity: 1; }`
- **Per-Selector Transition Rules**:
- **Selector `on .e-n-accordion-item-title-icon...`**: `transition: transform 0.4s cubic-bezier(0.65,0,0.35,1), opacity 0.3s ease` extracted from `miligram-pt` stylesheet.
- **Selector `ment-6884a37 .e-n-accordion-item-...`**: `transition: none !important` extracted from `miligram-pt` stylesheet.
- **Selector `media (prefers-reduced-motion: re...`**: `transition: none` extracted from `miligram-pt` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.65,0,0.35,1)`)**: Governs interactive state transitions across `<header.elementor>` and `<section.miligram-evolua>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `miligram-pt`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
