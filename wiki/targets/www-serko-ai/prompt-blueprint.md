---
title: "UI Prompt Blueprint: www-serko-ai"
date: 2026-11-15
target: "www-serko-ai"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#b93fce` / `#f6f6f6`)"
---

# UI Design System & Master Generation Blueprint: www-serko-ai

> **Serko.ai · AI Travel Agent** (https://www.serko.ai) — Explore a smarter way to manage business travel with Serko.ai, the AI-native travel platform. It learns how you like to travel and handle...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Serko.ai · AI Travel Agent** (`https://www.serko.ai`). Explore a smarter way to manage business travel with Serko.ai, the AI-native travel platform. It learns how you like to travel and handle...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#b93fce` / `#f6f6f6`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#b93fce` (`var(--library---swatch--purple-500)` in `:root`) paired with `#f6f6f6` primary typography and `#f6f6f6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Jokker` for display copy (`AI travel agent`) with `pretty` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `var(--max-width--main)` container bounds (`gap: var(--_spacing---space--2)`, padding `1.5rem`) with `cubic-bezier(0.525,0,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×11035px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `var(--max-width--main)` extracted from `www-serko-ai` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1.5rem` lateral canvas padding with `var(--_spacing---space--2)` grid gap.
- **Border Radius Scale**: `var(--radius--medium)`, `var(--radius--small)`, `.75rem`, `var(--radius--main)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--max-width--main)`, `gap: var(--_spacing---space--2)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#b93fce` | `var(--library---swatch--purple-500)` in `:root` |
| **Primary Typography Ink** | `#0078d4` | `var(--library---swatch--blue-500)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f13931` | `var(--_swatch---error)` in `:root` |
| **Interactive Accent / Highlight** | `#f6f6f6` | `var(--_swatch---light-2)` in `:root` |
| **Secondary / Muted Copy** | `#e8f3fe` | `var(--_swatch---light-3)` in `:root` |
| **Structural Hairline Border** | `#c0f2b5` | `var(--_swatch---positive-200)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--library_text-style---font-family` | `var(--library_typography---font--primary-family)` | Typography Ink Token |
| `--library_text-style---font-size` | `var(--library_typography---font-size--text-main)` | Typography Ink Token |
| `--library_text-style---line-height` | `var(--library_typography---line-height--1-5)` | Typography Ink Token |
| `--library_text-style---font-weight` | `var(--library_typography---font--primary-medium)` | Typography Ink Token |
| `--library_heading-style---margin-top` | `var(--library_spacing---space--4)` | Typography Ink Token |
| `--library_heading-style---margin-bottom` | `var(--library_spacing---space--4)` | Typography Ink Token |
| `--library_heading-style---font-family` | `var(--library_typography---font--primary-family)` | Typography Ink Token |
| `--library_heading-style---font-size` | `var(--library_typography---font-size--text-main)` | Typography Ink Token |
| `--library_heading-style---line-height` | `var(--library_typography---line-height--1-5)` | Typography Ink Token |
| `--library_heading-style---font-weight` | `var(--library_typography---font--primary-regular)` | Typography Ink Token |
| `--library_heading-style---letter-spacing` | `var(--library_typography---letter-spacing--0em)` | Typography Ink Token |
| `--library_text-style---margin-top` | `var(--library_spacing---space--4)` | Typography Ink Token |
| `--library_text-style---margin-bottom` | `var(--library_spacing---space--4)` | Typography Ink Token |
| `--library_spacing---space--6` | `2rem` | Layout / Spatial Grid Token |
| `--library_text-style---letter-spacing` | `var(--library_typography---letter-spacing--0em)` | Typography Ink Token |
| `--library_spacing---space--7` | `3rem` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Jokker`.
- **Primary Body Stack**: `pretty`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--library_typography---font-size--h1: 5.25rem`, `--library_typography---font-size--display: 6rem`, `--osano-display-position: "bottom-left"`.
- **Section Heading (`H2`)**: CSS variables `--library_typography---font-size--h2: 4rem`.
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--library_typography---font-s...`, `var(--_typography---font-size--te...`, `var(--_text-style---font-size)`, `var(--_heading-style---font-size)`, `var(--_typography---font-size--h4)`).
- **Metadata & Navigation Labels**: CSS variables `--library_heading-style---letter-spacing: var(--library_typography---letter-spacing--0em)`, `--library_text-style---letter-spacing: var(--library_typography---letter-spacing--0em)`, `--library_spacing---section-space--small: 5rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.525,0,0,1)`, `cubic-bezier(.22,1.15,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `www-serko-ai` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `www-serko-ai` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-serko-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.525,0,0,1)`)**: Governs interactive state transitions across `<header.nav1_header>` and `<section.feature1_wrap>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Serko.ai · AI Travel Agent                 │
│ ====================================================================== │
│ [ <header.nav1_header>     | Home · Platform · For companies · Abou ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero1_wrap>                                 |   │
│ | H1: AI travel agent                                              |   │
│ | Substrate: #b93fce    | Ink: #f6f6f6    | Accent: #f6f6f6        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.feature1_wrap>   ) max-w: var(--max-widt |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | The last travel agent you’ll |  | Stress-free cancellation     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.nav1_heade] -> [<section.hero1_wra] -> [<section.feature1_] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.osano-cm-windo) | https://www.serko.ai               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.nav1_header> — `www-serko-ai`)**:
   - Landmark `<header class="nav1_header">` hosting `Serko.ai · AI Travel Agent` navigation (`Home · Platform · For companies · About · Log in`), DOM attributes (`data-wf-domain="www.serko.ai"`, `data-wf-page="6aa12b65e6dd0b96a2a83430"`, `data-wf-site="6aa12b65e6dd0b96a2a8345b"`, `data-wf-intellimize-customer-id="117114932"`), and stylesheet rule `img { object-fit:cover;width:100%;max-width:100% }`.
2. **Hero Stage & Focal Lead (<section.hero1_wrap> — `AI travel agent`)**:
   - Landmark `<section class="hero1_wrap u-gradient-bg-1">` presenting display lead `AI travel agent` and copy excerpt *"Opens in a new window"* over `#b93fce` canvas and `#f6f6f6` ink.
3. **Primary Showcase & Content Grid (<section.feature1_wrap> — `The last travel agent you’ll ever `)**:
   - Landmark `<section class="feature1_wrap u-background-3">` rendering section `The last travel agent you’ll ever need.` with copy *"Opens an external website"*, asset references (`cdn.prod.website-files.com`, `serko-ai.webflow.shared.96cab25cb...`, `serko-ai.webflow.6aa12b65e6dd0b96...`, `gtm.js`), and grid rule `strong { font-weight:700 }`.
4. **Interactive Detail & Feature Matrix (<section.feature2_wrap> — `Stress-free cancellation`)**:
   - Landmark `<section class="feature2_wrap">` framing `Stress-free cancellation` and `Book like it's refundable. Because it is.` (*"Opens an external website in a new window"*) with `#f13931` surface cards, `#f6f6f6` accents, and `blockquote { border-style:none;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.osano-cm-window> — `https://www.serko.ai`)**:
   - Landmark `<footer class="osano-cm-window">` anchoring `Serko.ai · AI Travel Agent` footer links (`Home · Platform · For companies · About · Log in`), copy *"<!---->Close this consent banner<!---->"*, and `#c0f2b5` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-serko-ai (Serko.ai · AI Travel Agent)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-serko-ai` (**Serko.ai · AI Travel Agent** — `https://www.serko.ai`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#b93fce` / `#f6f6f6`).
- **Identity & Domain Context**: Explore a smarter way to manage business travel with Serko.ai, the AI-native travel platform. It learns how you like to travel and handle...
- **Primary Substrate**: `#b93fce` (`var(--library---swatch--purple-500)` in `:root`), **Primary Ink**: `#f6f6f6`, **Accent / Highlight**: `#f6f6f6`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#b93fce` (`var(--library---swatch--purple-500)` in `:root`) paired with `#f6f6f6` primary typography and `#f6f6f6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Jokker` for display copy (`AI travel agent`) with `pretty` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `var(--max-width--main)` container bounds (`gap: var(--_spacing---space--2)`, padding `1.5rem`) with `cubic-bezier(0.525,0,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-serko-ai` in your global stylesheet:

:root {
  /* Serko.ai · AI Travel Agent (www-serko-ai) — Ground-Truth Extracted CSS Variables */
  --library_text-style---font-family: var(--library_typography---font--primary-family); /* Typography Ink Token (www-serko-ai) */
  --library_text-style---font-size: var(--library_typography---font-size--text-main); /* Typography Ink Token (www-serko-ai) */
  --library_text-style---line-height: var(--library_typography---line-height--1-5); /* Typography Ink Token (www-serko-ai) */
  --library_text-style---font-weight: var(--library_typography---font--primary-medium); /* Typography Ink Token (www-serko-ai) */
  --library_heading-style---margin-top: var(--library_spacing---space--4); /* Typography Ink Token (www-serko-ai) */
  --library_heading-style---margin-bottom: var(--library_spacing---space--4); /* Typography Ink Token (www-serko-ai) */
  --library_heading-style---font-family: var(--library_typography---font--primary-family); /* Typography Ink Token (www-serko-ai) */
  --library_heading-style---font-size: var(--library_typography---font-size--text-main); /* Typography Ink Token (www-serko-ai) */
  --library_heading-style---line-height: var(--library_typography---line-height--1-5); /* Typography Ink Token (www-serko-ai) */
  --library_heading-style---font-weight: var(--library_typography---font--primary-regular); /* Typography Ink Token (www-serko-ai) */
  --library_heading-style---letter-spacing: var(--library_typography---letter-spacing--0em); /* Typography Ink Token (www-serko-ai) */
  --library_text-style---margin-top: var(--library_spacing---space--4); /* Typography Ink Token (www-serko-ai) */
  --library_text-style---margin-bottom: var(--library_spacing---space--4); /* Typography Ink Token (www-serko-ai) */
  --library_spacing---space--6: 2rem; /* Layout / Spatial Grid Token (www-serko-ai) */
  --library_text-style---letter-spacing: var(--library_typography---letter-spacing--0em); /* Typography Ink Token (www-serko-ai) */
  --library_spacing---space--7: 3rem; /* Layout / Spatial Grid Token (www-serko-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#b93fce` — grounded in `var(--library---swatch--purple-500)` in `:root`
- **Primary Typography Ink**: `#0078d4` — grounded in `var(--library---swatch--blue-500)` in `:root`
- **Elevated Surface / Card Substrate**: `#f13931` — grounded in `var(--_swatch---error)` in `:root`
- **Interactive Accent / Highlight**: `#f6f6f6` — grounded in `var(--_swatch---light-2)` in `:root`
- **Secondary / Muted Copy**: `#e8f3fe` — grounded in `var(--_swatch---light-3)` in `:root`
- **Structural Hairline Border**: `#c0f2b5` — grounded in `var(--_swatch---positive-200)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×11035px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `var(--max-width--main)` extracted from `www-serko-ai` stylesheet
- **Padding & Gutters**: `1.5rem` lateral canvas padding with `var(--_spacing---space--2)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--max-width--main)`, `gap: var(--_spacing---space--2)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `var(--radius--medium)`, `var(--radius--small)`, `.75rem`, `var(--radius--main)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Jokker`
- **Body Font Stack**: `pretty`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--library_typography---font-size--h1: 5.25rem`, `--library_typography---font-size--display: 6rem`, `--osano-display-position: "bottom-left"`
- **H2 Section Rule**: CSS variables `--library_typography---font-size--h2: 4rem`
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--library_typography---font-s...`, `var(--_typography---font-size--te...`, `var(--_text-style---font-size)`, `var(--_heading-style---font-size)`, `var(--_typography---font-size--h4)`)
- **Metadata & Index Rule**: CSS variables `--library_heading-style---letter-spacing: var(--library_typography---letter-spacing--0em)`, `--library_text-style---letter-spacing: var(--library_typography---letter-spacing--0em)`, `--library_spacing---section-space--small: 5rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-serko-ai` (`Serko.ai · AI Travel Agent`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.nav1_header> — `www-serko-ai`)**:
   - DOM & Selectors: Landmark `<header class="nav1_header">` hosting `Serko.ai · AI Travel Agent` navigation (`Home · Platform · For companies · About · Log in`), DOM attributes (`data-wf-domain="www.serko.ai"`, `data-wf-page="6aa12b65e6dd0b96a2a83430"`, `data-wf-site="6aa12b65e6dd0b96a2a8345b"`, `data-wf-intellimize-customer-id="117114932"`), and stylesheet rule `img { object-fit:cover;width:100%;max-width:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.nav1_header> — `www-serko-ai`)` (`www-serko-ai`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(0.525,0,0,1)`, `cubic-bezier(.22,1.15,.36,1)` transitions and links `Home · Platform · For companies · About · Log in`.
2. **Hero Stage & Focal Lead (<section.hero1_wrap> — `AI travel agent`)**:
   - DOM & Selectors: Landmark `<section class="hero1_wrap u-gradient-bg-1">` presenting display lead `AI travel agent` and copy excerpt *"Opens in a new window"* over `#b93fce` canvas and `#f6f6f6` ink.
   - Responsive Contract: Hero stage (`1440×11035px` desktop / `390×2400px` mobile) sets `#b93fce` background with `#f6f6f6` headline `AI travel agent`.
3. **Primary Showcase & Content Grid (<section.feature1_wrap> — `The last travel agent you’ll ever `)**:
   - DOM & Selectors: Landmark `<section class="feature1_wrap u-background-3">` rendering section `The last travel agent you’ll ever need.` with copy *"Opens an external website"*, asset references (`cdn.prod.website-files.com`, `serko-ai.webflow.shared.96cab25cb...`, `serko-ai.webflow.6aa12b65e6dd0b96...`, `gtm.js`), and grid rule `strong { font-weight:700 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.feature1_wrap> — `The last travel agent you’ll ever `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--max-width--main)`, `gap: var(--_spacing---space--2)`) on desktop and Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.feature2_wrap> — `Stress-free cancellation`)**:
   - DOM & Selectors: Landmark `<section class="feature2_wrap">` framing `Stress-free cancellation` and `Book like it's refundable. Because it is.` (*"Opens an external website in a new window"*) with `#f13931` surface cards, `#f6f6f6` accents, and `blockquote { border-style:none;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.feature2_wrap> — `Stress-free cancellation`)` uses `var(--radius--medium)`, `var(--radius--small)`, `.75rem`, `var(--radius--main)` radii, `#f6f6f6` highlights, and assets (cdn.prod.website-files.com, serko-ai.webflow.shared.96cab25cb..., serko-ai.webflow.6aa12b65e6dd0b96...).
5. **Colophon & Global Directory Footer (<footer.osano-cm-window> — `https://www.serko.ai`)**:
   - DOM & Selectors: Landmark `<footer class="osano-cm-window">` anchoring `Serko.ai · AI Travel Agent` footer links (`Home · Platform · For companies · About · Log in`), copy *"<!---->Close this consent banner<!---->"*, and `#c0f2b5` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.osano-cm-window> — `https://www.serko.ai`)` aligns to `var(--max-width--main)` extracted from `www-serko-ai` stylesheet with `1.5rem` lateral canvas padding with `var(--_spacing---space--2)` grid gap and attributes (data-wf-domain="www.serko.ai", data-wf-page="6aa12b65e6dd0b96a2a83430", data-wf-site="6aa12b65e6dd0b96a2a8345b").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Opens in a new window"*
- Copy Excerpt 2: *"Opens an external website"*
- Copy Excerpt 3: *"Opens an external website in a new window"*
- Copy Excerpt 4: *"<!---->Close this consent banner<!---->"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.525,0,0,1)`, `cubic-bezier(.22,1.15,.36,1)`
- **Extracted Stylesheet Rules (`www-serko-ai`)**:
- `img { object-fit:cover;width:100%;max-width:100% }`
- `strong { font-weight:700 }`
- `blockquote { border-style:none;padding:0 }`
- `figure { margin-bottom:0 }`
- `.u-rich-text p { margin-top:var(--_text-style---margin-top);margin-bottom:var(--_text-sty... }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `www-serko-ai` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `www-serko-ai` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-serko-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.525,0,0,1)`)**: Governs interactive state transitions across `<header.nav1_header>` and `<section.feature1_wrap>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-serko-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
