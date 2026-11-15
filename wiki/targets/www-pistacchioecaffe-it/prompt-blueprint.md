---
title: "UI Prompt Blueprint: www-pistacchioecaffe-it"
date: 2026-11-15
target: "www-pistacchioecaffe-it"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#465565` canvas, `#ffba00` ink, `#a00` accent)"
---

# UI Design System & Master Generation Blueprint: www-pistacchioecaffe-it

> **Pistacchio & Caffè** (http://www.pistacchioecaffe.it) — Scopri il mondo di Francesca, interior designer e stylist. Dal design d'interni allo styling personalizzato, troverai soluzioni creative...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Pistacchio & Caffè** (`http://www.pistacchioecaffe.it`). Scopri il mondo di Francesca, interior designer e stylist. Dal design d'interni allo styling personalizzato, troverai soluzioni creative...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#465565` canvas, `#ffba00` ink, `#a00` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#465565` (`var(--text-main-color)` in `:root`) paired with `#ffba00` primary typography and `#a00` accents.
  - **Extracted Typographic Hierarchy**: Pairs `utendobold` for display copy (`Benvenuti nel mio mondo!`) with `utendolight` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1180px` container bounds (`gap: 20px`, padding `15px`) with `cubic-bezier(0.645,0.045,0.355,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×7079px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1180px` extracted from `www-pistacchioecaffe-it` stylesheet.
- **Canvas Lateral Padding & Spacing**: `15px` lateral canvas padding with `20px` grid gap.
- **Border Radius Scale**: `1px`, `100%`, `20px`, `10px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1180px`, `gap: 20px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `15px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (min-device-width: 821px) and (max-device-widt...`, `@media screen and (min-width: 481px) and (max-width: 820px), scr...`, `@media screen and (max-width: 480px)`, `@media screen and (min-device-width: 1025px) and (max-device-wid...`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#465565` | `var(--text-main-color)` in `:root` |
| **Primary Typography Ink** | `#720eec` | `var(--woocommerce)` in `:root` |
| **Elevated Surface / Card Substrate** | `#007518` | `var(--wc-green)` in `:root` |
| **Interactive Accent / Highlight** | `#a00` | `var(--wc-red)` in `:root` |
| **Secondary / Muted Copy** | `#ffba00` | `var(--wc-orange)` in `:root` |
| **Structural Hairline Border** | `#2ea2cc` | `var(--wc-blue)` in `:root` |
| **Variable Token (`--wc-primary-text`)** | `#fcfbfe` | `var(--wc-primary-text)` in `:root` |
| **Variable Token (`--wc-secondary`)** | `#e9e6ed` | `var(--wc-secondary)` in `:root` |
| **Variable Token (`--wc-secondary-text`)** | `#515151` | `var(--wc-secondary-text)` in `:root` |
| **Variable Token (`--wc-highlight`)** | `#958e09` | `var(--wc-highlight)` in `:root` |
| **Variable Token (`--wc-content-bg`)** | `#fff` | `var(--wc-content-bg)` in `:root` |
| **Variable Token (`--wc-subtext`)** | `#767676` | `var(--wc-subtext)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--text-main-color` | `#465565` | Typography Ink Token |
| `--app-height` | `100%` | Layout / Spatial Grid Token |
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
| `--wc-highligh-text` | `white` | Typography Ink Token |
| `--wc-content-bg` | `#fff` | Canvas / Surface Token |
| `--wc-subtext` | `#767676` | Typography Ink Token |
| `--wc-form-border-color` | `rgba(32, 7, 7, 0.8)` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `utendobold`.
- **Primary Body Stack**: `utendolight`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 3vw`, `line-height: 1.2`, `font-weight: normal`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2.5vw`).
- **Body Copy**: rule `body` (`font-size: 18px`, `line-height: 30px`, `font-weight: normal`).
- **Metadata & Navigation Labels**: rule `.label` (`font-size: 17px !important`, `line-height: 1 !important`, `font-weight: normal !impor...`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.645,0.045,0.355,1)`, `cubic-bezier(0.165,0.84,0.44,1)`, `cubic-bezier(0.895,0.03,0.685,0.22)`.

### Per-Element Transition & Choreography Rules
- **Selector `.hamburger`**: `transition: 0.15s` extracted from `www-pistacchioecaffe-it` stylesheet.
- **Selector `.hamburger-inner::after`**: `transition: 0.15s` extracted from `www-pistacchioecaffe-it` stylesheet.
- **Selector `.hamburger--3dx .hamburger-inner`**: `transition: transform 0.15s cubic-bezier(0.645,0.045,0.355,1), backgrou...` extracted from `www-pistacchioecaffe-it` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.645,0.045,0.355,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<article.post-7>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Pistacchio & Caffè                         │
│ ====================================================================== │
│ [ <header.site-header>     | contattami · 0,00 €                    ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.post-7>                                     |   │
│ | H1: Benvenuti nel mio mondo!                                     |   │
│ | Substrate: #465565    | Ink: #ffba00    | Accent: #a00           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.post-7>          ) max-w: 1180px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | E colore sia.                |  | Osa.                         | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 20px  ) | │
│ | [<header.site-heade] -> [<article.post-7>] -> [<article.post-7>] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | http://www.pistacchioecaffe.it     │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `www-pistacchioecaffe-it`)**:
   - Landmark `<header class="site-header">` hosting `Pistacchio & Caffè` navigation (`contattami · 0,00 €`), DOM attributes (`data-cmp-ab="2"`, `data-cmp-info="10"`, `data-cmp-ab="2"`, `data-cmp-info="2"`), and stylesheet rule `urger.is-active .hamburger-inner:... { background-color: FFFAF0; }`.
2. **Hero Stage & Focal Lead (<article.post-7> — `Benvenuti nel mio mondo!`)**:
   - Landmark `<article class="post-7 page">` presenting display lead `Benvenuti nel mio mondo!` and copy excerpt *"Benvenuti nel mio mondo!"* over `#465565` canvas and `#ffba00` ink.
3. **Primary Showcase & Content Grid (<article.post-7> — `E colore sia.`)**:
   - Landmark `<article class="post-7 page">` rendering section `E colore sia.` with copy *"Ciao, sono Francesca, interior designer e stylist. Ascolto, proge"*, asset references (`30300652.js`, `core-it.js`, `recaptcha__en.js`, `jquery.min.js`), and grid rule `.hamburger-inner { display: block; top: 50%; margin-top: -1px; }`.
4. **Interactive Detail & Feature Matrix (<article.post-7> — `Osa.`)**:
   - Landmark `<article class="post-7 page">` framing `Osa.` and `Progetto per te.` (*"Amo disegnare e scrivere, ognuna di queste passioni è entrata pre"*) with `#007518` surface cards, `#a00` accents, and `.hamburger-inner::after { content: ""; display: block; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `http://www.pistacchioecaffe.it`)**:
   - Landmark `<footer class="site-footer contenitore-flex">` anchoring `Pistacchio & Caffè` footer links (`contattami · 0,00 €`), copy *"Potrei definire il mio stile POP_MINIMALE ma non dimentico m"*, and `#2ea2cc` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-pistacchioecaffe-it (Pistacchio & Caffè)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-pistacchioecaffe-it` (**Pistacchio & Caffè** — `http://www.pistacchioecaffe.it`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#465565` canvas, `#ffba00` ink, `#a00` accent).
- **Identity & Domain Context**: Scopri il mondo di Francesca, interior designer e stylist. Dal design d'interni allo styling personalizzato, troverai soluzioni creative...
- **Primary Substrate**: `#465565` (`var(--text-main-color)` in `:root`), **Primary Ink**: `#ffba00`, **Accent / Highlight**: `#a00`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#465565` (`var(--text-main-color)` in `:root`) paired with `#ffba00` primary typography and `#a00` accents.
  - **Extracted Typographic Hierarchy**: Pairs `utendobold` for display copy (`Benvenuti nel mio mondo!`) with `utendolight` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1180px` container bounds (`gap: 20px`, padding `15px`) with `cubic-bezier(0.645,0.045,0.355,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-pistacchioecaffe-it` in your global stylesheet:

:root {
  /* Pistacchio & Caffè (www-pistacchioecaffe-it) — Ground-Truth Extracted CSS Variables */
  --text-main-color: #465565; /* Typography Ink Token (www-pistacchioecaffe-it) */
  --app-height: 100%; /* Layout / Spatial Grid Token (www-pistacchioecaffe-it) */
  --woocommerce: #720eec; /* Color / Atmospheric Token (www-pistacchioecaffe-it) */
  --wc-green: #007518; /* Color / Atmospheric Token (www-pistacchioecaffe-it) */
  --wc-red: #a00; /* Color / Atmospheric Token (www-pistacchioecaffe-it) */
  --wc-orange: #ffba00; /* Color / Atmospheric Token (www-pistacchioecaffe-it) */
  --wc-blue: #2ea2cc; /* Color / Atmospheric Token (www-pistacchioecaffe-it) */
  --wc-primary: #720eec; /* Brand / Palette Token (www-pistacchioecaffe-it) */
  --wc-primary-text: #fcfbfe; /* Typography Ink Token (www-pistacchioecaffe-it) */
  --wc-secondary: #e9e6ed; /* Brand / Palette Token (www-pistacchioecaffe-it) */
  --wc-secondary-text: #515151; /* Typography Ink Token (www-pistacchioecaffe-it) */
  --wc-highlight: #958e09; /* Canvas / Surface Token (www-pistacchioecaffe-it) */
  --wc-highligh-text: white; /* Typography Ink Token (www-pistacchioecaffe-it) */
  --wc-content-bg: #fff; /* Canvas / Surface Token (www-pistacchioecaffe-it) */
  --wc-subtext: #767676; /* Typography Ink Token (www-pistacchioecaffe-it) */
  --wc-form-border-color: rgba(32, 7, 7, 0.8); /* Brand / Palette Token (www-pistacchioecaffe-it) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#465565` — grounded in `var(--text-main-color)` in `:root`
- **Primary Typography Ink**: `#720eec` — grounded in `var(--woocommerce)` in `:root`
- **Elevated Surface / Card Substrate**: `#007518` — grounded in `var(--wc-green)` in `:root`
- **Interactive Accent / Highlight**: `#a00` — grounded in `var(--wc-red)` in `:root`
- **Secondary / Muted Copy**: `#ffba00` — grounded in `var(--wc-orange)` in `:root`
- **Structural Hairline Border**: `#2ea2cc` — grounded in `var(--wc-blue)` in `:root`
- **Variable Token (`--wc-primary-text`)**: `#fcfbfe` — grounded in `var(--wc-primary-text)` in `:root`
- **Variable Token (`--wc-secondary`)**: `#e9e6ed` — grounded in `var(--wc-secondary)` in `:root`
- **Variable Token (`--wc-secondary-text`)**: `#515151` — grounded in `var(--wc-secondary-text)` in `:root`
- **Variable Token (`--wc-highlight`)**: `#958e09` — grounded in `var(--wc-highlight)` in `:root`
- **Variable Token (`--wc-content-bg`)**: `#fff` — grounded in `var(--wc-content-bg)` in `:root`
- **Variable Token (`--wc-subtext`)**: `#767676` — grounded in `var(--wc-subtext)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×7079px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1180px` extracted from `www-pistacchioecaffe-it` stylesheet
- **Padding & Gutters**: `15px` lateral canvas padding with `20px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1180px`, `gap: 20px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `15px` horizontal padding
- **Media Queries**: `@media screen and (min-device-width: 821px) and (max-device-widt...`, `@media screen and (min-width: 481px) and (max-width: 820px), scr...`, `@media screen and (max-width: 480px)`, `@media screen and (min-device-width: 1025px) and (max-device-wid...`
- **Corner Radii**: `1px`, `100%`, `20px`, `10px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `utendobold`
- **Body Font Stack**: `utendolight`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 3vw`, `line-height: 1.2`, `font-weight: normal`)
- **H2 Section Rule**: rule `h2` (`font-size: 2.5vw`)
- **Body Copy Rule**: rule `body` (`font-size: 18px`, `line-height: 30px`, `font-weight: normal`)
- **Metadata & Index Rule**: rule `.label` (`font-size: 17px !important`, `line-height: 1 !important`, `font-weight: normal !impor...`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-pistacchioecaffe-it` (`Pistacchio & Caffè`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `www-pistacchioecaffe-it`)**:
   - DOM & Selectors: Landmark `<header class="site-header">` hosting `Pistacchio & Caffè` navigation (`contattami · 0,00 €`), DOM attributes (`data-cmp-ab="2"`, `data-cmp-info="10"`, `data-cmp-ab="2"`, `data-cmp-info="2"`), and stylesheet rule `urger.is-active .hamburger-inner:... { background-color: FFFAF0; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `www-pistacchioecaffe-it`)` (`www-pistacchioecaffe-it`) adapts across `@media screen and (min-device-width: 821px) and (max-device-widt...`, `@media screen and (min-width: 481px) and (max-width: 820px), scr...`, `@media screen and (max-width: 480px)`, `@media screen and (min-device-width: 1025px) and (max-device-wid...` with `cubic-bezier(0.645,0.045,0.355,1)`, `cubic-bezier(0.165,0.84,0.44,1)`, `cubic-bezier(0.895,0.03,0.685,0.22)` transitions and links `contattami · 0,00 €`.
2. **Hero Stage & Focal Lead (<article.post-7> — `Benvenuti nel mio mondo!`)**:
   - DOM & Selectors: Landmark `<article class="post-7 page">` presenting display lead `Benvenuti nel mio mondo!` and copy excerpt *"Benvenuti nel mio mondo!"* over `#465565` canvas and `#ffba00` ink.
   - Responsive Contract: Hero stage (`1440×7079px` desktop / `390×2400px` mobile) sets `#465565` background with `#ffba00` headline `Benvenuti nel mio mondo!`.
3. **Primary Showcase & Content Grid (<article.post-7> — `E colore sia.`)**:
   - DOM & Selectors: Landmark `<article class="post-7 page">` rendering section `E colore sia.` with copy *"Ciao, sono Francesca, interior designer e stylist. Ascolto, proge"*, asset references (`30300652.js`, `core-it.js`, `recaptcha__en.js`, `jquery.min.js`), and grid rule `.hamburger-inner { display: block; top: 50%; margin-top: -1px; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.post-7> — `E colore sia.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1180px`, `gap: 20px`) on desktop and Single-column vertical stack at `390px` viewport width with `15px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.post-7> — `Osa.`)**:
   - DOM & Selectors: Landmark `<article class="post-7 page">` framing `Osa.` and `Progetto per te.` (*"Amo disegnare e scrivere, ognuna di queste passioni è entrata pre"*) with `#007518` surface cards, `#a00` accents, and `.hamburger-inner::after { content: ""; display: block; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.post-7> — `Osa.`)` uses `1px`, `100%`, `20px`, `10px` radii, `#a00` highlights, and assets (30300652.js, core-it.js, recaptcha__en.js).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `http://www.pistacchioecaffe.it`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer contenitore-flex">` anchoring `Pistacchio & Caffè` footer links (`contattami · 0,00 €`), copy *"Potrei definire il mio stile POP_MINIMALE ma non dimentico m"*, and `#2ea2cc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `http://www.pistacchioecaffe.it`)` aligns to `1180px` extracted from `www-pistacchioecaffe-it` stylesheet with `15px` lateral canvas padding with `20px` grid gap and attributes (data-cmp-ab="2", data-cmp-info="10", data-cmp-ab="2").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Benvenuti nel mio mondo!"*
- Copy Excerpt 2: *"Ciao, sono Francesca, interior designer e stylist. Ascolto, progetto, realizzo."*
- Copy Excerpt 3: *"Amo disegnare e scrivere, ognuna di queste passioni è entrata prepotentemente nel..."*
- Copy Excerpt 4: *"Potrei definire il mio stile POP_MINIMALE ma non dimentico mai colore e romanticismo."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.645,0.045,0.355,1)`, `cubic-bezier(0.165,0.84,0.44,1)`, `cubic-bezier(0.895,0.03,0.685,0.22)`
- **Extracted Stylesheet Rules (`www-pistacchioecaffe-it`)**:
- `urger.is-active .hamburger-inner:... { background-color: FFFAF0; }`
- `.hamburger-inner { display: block; top: 50%; margin-top: -1px; }`
- `.hamburger-inner::after { content: ""; display: block; }`
- `.hamburger-inner::before { top: -7px; }`
- `.hamburger--3dx .hamburger-box { perspective: 80px; }`
- **Per-Selector Transition Rules**:
- **Selector `.hamburger`**: `transition: 0.15s` extracted from `www-pistacchioecaffe-it` stylesheet.
- **Selector `.hamburger-inner::after`**: `transition: 0.15s` extracted from `www-pistacchioecaffe-it` stylesheet.
- **Selector `.hamburger--3dx .hamburger-inner`**: `transition: transform 0.15s cubic-bezier(0.645,0.045,0.355,1), backgrou...` extracted from `www-pistacchioecaffe-it` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.645,0.045,0.355,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<article.post-7>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-pistacchioecaffe-it`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
