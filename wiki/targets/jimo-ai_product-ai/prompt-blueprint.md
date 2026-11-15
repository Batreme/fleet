---
title: "UI Prompt Blueprint: jimo-ai_product-ai"
date: 2026-11-15
target: "jimo-ai_product-ai"
status: analyzed
capture: dom
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#7ab1fe` / `#171717`)"
---

# UI Design System & Master Generation Blueprint: jimo-ai_product-ai

> **AI Agent for User Onboarding in SaaS · Jimo** (https://jimo.ai/product/ai) — Jimo's Adoption Agent lives inside your SaaS. It guides users step by step, answers questions from your docs, and takes actions for them....

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **AI Agent for User Onboarding in SaaS · Jimo** (`https://jimo.ai/product/ai`). Jimo's Adoption Agent lives inside your SaaS. It guides users step by step, answers questions from your docs, and takes actions for them....
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#7ab1fe` / `#171717`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#7ab1fe` (`var(--acc)` in `:root`) paired with `#000` primary typography and `#171717` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`An agent in your SaaS that makes ado`) with `Inter Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1099px` container bounds (`gap: 6px`, padding `16px`) with `cubic-bezier(.22,1,.36,1)` easing and Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1099px` extracted from `jimo-ai_product-ai` stylesheet.
- **Canvas Lateral Padding & Spacing**: `16px` lateral canvas padding with `6px` grid gap.
- **Border Radius Scale**: `22px`, `999px`, `50%`, `17px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1099px`, `gap: 6px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#7ab1fe` | `var(--acc)` in `:root` |
| **Primary Typography Ink** | `#9cc0ff` | `var(--acc-text)` in `:root` |
| **Elevated Surface / Card Substrate** | `#2b7fff` | `var(--blue)` in `:root` |
| **Interactive Accent / Highlight** | `#171717` | `var(--color-neutral-900)` in `:root` |
| **Secondary / Muted Copy** | `#000` | `var(--color-black)` in `:root` |
| **Structural Hairline Border** | `#fff` | `var(--color-white)` in `:root` |
| **Variable Token (`--hair`)** | `#ffffff14` | `var(--hair)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ease` | `cubic-bezier(.22, 1, .36, 1)` | Motion / Easing Token |
| `--draw` | `cubic-bezier(.65, 0, .35, 1)` | Motion / Timing Token |
| `--glide` | `cubic-bezier(.32, .72, 0, 1)` | Motion / Timing Token |
| `--acc` | `#7ab1fe` | Color / Atmospheric Token |
| `--acc-text` | `#9cc0ff` | Typography Ink Token |
| `--blue` | `#2b7fff` | Color / Atmospheric Token |
| `--hair` | `#ffffff14` | Color / Atmospheric Token |
| `--pad` | `40px` | Layout / Spatial Grid Token |
| `--card-w` | `480px` | Dimension / Scale Token |
| `--code` | `13px` | Dimension / Scale Token |
| `--peek` | `45px` | Dimension / Scale Token |
| `--lift` | `0px` | Dimension / Scale Token |
| `--sc` | `.93` | Design System Custom Token |
| `--nd` | `.12s` | Motion / Timing Token |
| `--font-inter` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-jlp` | `"DM Sans", "DM Sans Fallback"` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Inter Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--code)`, `11px`, `13px`, `14px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--code)`, `11px`, `13px`, `14px`).
- **Body Copy**: rule `p` (`font-size: 32px`, `line-height: 1`, `letter-spacing: -.01em`, `font-weight: 400`).
- **Metadata & Navigation Labels**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 12px`, `line-height: 16px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.32,.72,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.bento-sdk-module__RcAs1W__root`**: `transition: opacity .5s cubic-bezier(.22,1,.36,1)` extracted from `jimo-ai_product-ai` stylesheet.
- **Selector `.bento-sdk-module__RcAs1W__stack`**: `transition: opacity .7s var(--ease), transform .7s var(--ease), filter .7s...` extracted from `jimo-ai_product-ai` stylesheet.
- **Selector `.bento-sdk-module__RcAs1W__str`**: `transition: color .3s,text-shadow .3s` extracted from `jimo-ai_product-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.jlp-fnav>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — AI Agent for User Onboarding in SaaS · Jim │
│ ====================================================================== │
│ [ <header.jlp-fnav>        | Products · Use Case · Pricing · Custom ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative>                                   |   │
│ | H1: An agent in your SaaS that makes adoption skyrock...         |   │
│ | Substrate: #7ab1fe    | Ink: #000       | Accent: #171717        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.relative>        ) max-w: 1099px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | One agent. Three modes .     |  | Guides users on the fly      | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 6px   ) | │
│ | [<header.jlp-fnav>] -> [<section.relative>] -> [<section.relative>]  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer-module_) | https://jimo.ai/product/ai         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.jlp-fnav> — `jimo-ai_product-ai`)**:
   - Landmark `<header class="jlp-fnav jlp-btn-dark">` hosting `AI Agent for User Onboarding in SaaS` navigation (`Products · Use Case · Pricing · Customers · Resources`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `ento-sdk-module__RcAs1W__root.is-... { opacity:1;pointer-events:auto }`.
2. **Hero Stage & Focal Lead (<section.relative> — `An agent in your SaaS that makes a`)**:
   - Landmark `<section class="relative z-20">` presenting display lead `An agent in your SaaS that makes adoption skyrock...` and copy excerpt *"Adoption Agent New Guides, answers and acts in your product"* over `#7ab1fe` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `One agent. Three modes .`)**:
   - Landmark `<section class="relative">` rendering section `One agent. Three modes .` with copy *"Adoption Agent New"*, asset references (`5c285b27cdda1fe8-s.p.0yo6-5yoeeud...`, `83afe278b6a6bb3c-s.p.0q-301v4kxxn...`, `gt-walsheim-medium.ttf`, `gt-walsheim-regular.ttf`), and grid rule `.bento-sdk-module__RcAs1W__scene { transform-origin:0 0;width:100%;height:100%;position:absolute;top:0;left... }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Guides users on the fly`)**:
   - Landmark `<section class="relative">` framing `Guides users on the fly` and `Answers contextual questions` (*"Guides, answers and acts in your product"*) with `#2b7fff` surface cards, `#171717` accents, and `.bento-sdk-module__RcAs1W__frame { --pad:24px;--card-w:440px;--code:12px;--w:330px }`.
5. **Colophon & Global Directory Footer (<footer.footer-module__d_pQKq__root> — `https://jimo.ai/product/ai`)**:
   - Landmark `<footer class="footer-module__d_pQKq__root">` anchoring `AI Agent for User Onboarding in ` footer links (`Products · Use Case · Pricing · Customers · Resources`), copy *"Interface knowledge"*, and `#fff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: jimo-ai_product-ai (AI Agent for User Onboarding in SaaS · Jimo)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `jimo-ai_product-ai` (**AI Agent for User Onboarding in SaaS · Jimo** — `https://jimo.ai/product/ai`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#7ab1fe` / `#171717`).
- **Identity & Domain Context**: Jimo's Adoption Agent lives inside your SaaS. It guides users step by step, answers questions from your docs, and takes actions for them....
- **Primary Substrate**: `#7ab1fe` (`var(--acc)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#171717`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#7ab1fe` (`var(--acc)` in `:root`) paired with `#000` primary typography and `#171717` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`An agent in your SaaS that makes ado`) with `Inter Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1099px` container bounds (`gap: 6px`, padding `16px`) with `cubic-bezier(.22,1,.36,1)` easing and Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `jimo-ai_product-ai` in your global stylesheet:

:root {
  /* AI Agent for User Onboarding in SaaS · Jimo (jimo-ai_product-ai) — Ground-Truth Extracted CSS Variables */
  --ease: cubic-bezier(.22, 1, .36, 1); /* Motion / Easing Token (jimo-ai_product-ai) */
  --draw: cubic-bezier(.65, 0, .35, 1); /* Motion / Timing Token (jimo-ai_product-ai) */
  --glide: cubic-bezier(.32, .72, 0, 1); /* Motion / Timing Token (jimo-ai_product-ai) */
  --acc: #7ab1fe; /* Color / Atmospheric Token (jimo-ai_product-ai) */
  --acc-text: #9cc0ff; /* Typography Ink Token (jimo-ai_product-ai) */
  --blue: #2b7fff; /* Color / Atmospheric Token (jimo-ai_product-ai) */
  --hair: #ffffff14; /* Color / Atmospheric Token (jimo-ai_product-ai) */
  --pad: 40px; /* Layout / Spatial Grid Token (jimo-ai_product-ai) */
  --card-w: 480px; /* Dimension / Scale Token (jimo-ai_product-ai) */
  --code: 13px; /* Dimension / Scale Token (jimo-ai_product-ai) */
  --peek: 45px; /* Dimension / Scale Token (jimo-ai_product-ai) */
  --lift: 0px; /* Dimension / Scale Token (jimo-ai_product-ai) */
  --sc: .93; /* Design System Custom Token (jimo-ai_product-ai) */
  --nd: .12s; /* Motion / Timing Token (jimo-ai_product-ai) */
  --font-inter: "Inter", "Inter Fallback"; /* Typography / Scale Token (jimo-ai_product-ai) */
  --font-jlp: "DM Sans", "DM Sans Fallback"; /* Typography / Scale Token (jimo-ai_product-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#7ab1fe` — grounded in `var(--acc)` in `:root`
- **Primary Typography Ink**: `#9cc0ff` — grounded in `var(--acc-text)` in `:root`
- **Elevated Surface / Card Substrate**: `#2b7fff` — grounded in `var(--blue)` in `:root`
- **Interactive Accent / Highlight**: `#171717` — grounded in `var(--color-neutral-900)` in `:root`
- **Secondary / Muted Copy**: `#000` — grounded in `var(--color-black)` in `:root`
- **Structural Hairline Border**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Variable Token (`--hair`)**: `#ffffff14` — grounded in `var(--hair)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1099px` extracted from `jimo-ai_product-ai` stylesheet
- **Padding & Gutters**: `16px` lateral canvas padding with `6px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1099px`, `gap: 6px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`
- **Corner Radii**: `22px`, `999px`, `50%`, `17px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--code)`, `11px`, `13px`, `14px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--code)`, `11px`, `13px`, `14px`)
- **Body Copy Rule**: rule `p` (`font-size: 32px`, `line-height: 1`, `letter-spacing: -.01em`, `font-weight: 400`)
- **Metadata & Index Rule**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 12px`, `line-height: 16px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `jimo-ai_product-ai` (`AI Agent for User Onboarding in SaaS · Jimo`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.jlp-fnav> — `jimo-ai_product-ai`)**:
   - DOM & Selectors: Landmark `<header class="jlp-fnav jlp-btn-dark">` hosting `AI Agent for User Onboarding in SaaS` navigation (`Products · Use Case · Pricing · Customers · Resources`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `ento-sdk-module__RcAs1W__root.is-... { opacity:1;pointer-events:auto }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.jlp-fnav> — `jimo-ai_product-ai`)` (`jimo-ai_product-ai`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)` with `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.32,.72,0,1)` transitions and links `Products · Use Case · Pricing · Customers · Resources`.
2. **Hero Stage & Focal Lead (<section.relative> — `An agent in your SaaS that makes a`)**:
   - DOM & Selectors: Landmark `<section class="relative z-20">` presenting display lead `An agent in your SaaS that makes adoption skyrock...` and copy excerpt *"Adoption Agent New Guides, answers and acts in your product"* over `#7ab1fe` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#7ab1fe` background with `#000` headline `An agent in your SaaS that makes adoption skyrock...`.
3. **Primary Showcase & Content Grid (<section.relative> — `One agent. Three modes .`)**:
   - DOM & Selectors: Landmark `<section class="relative">` rendering section `One agent. Three modes .` with copy *"Adoption Agent New"*, asset references (`5c285b27cdda1fe8-s.p.0yo6-5yoeeud...`, `83afe278b6a6bb3c-s.p.0q-301v4kxxn...`, `gt-walsheim-medium.ttf`, `gt-walsheim-regular.ttf`), and grid rule `.bento-sdk-module__RcAs1W__scene { transform-origin:0 0;width:100%;height:100%;position:absolute;top:0;left... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.relative> — `One agent. Three modes .`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1099px`, `gap: 6px`) on desktop and Single-column vertical stack at `390px` viewport width with `16px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Guides users on the fly`)**:
   - DOM & Selectors: Landmark `<section class="relative">` framing `Guides users on the fly` and `Answers contextual questions` (*"Guides, answers and acts in your product"*) with `#2b7fff` surface cards, `#171717` accents, and `.bento-sdk-module__RcAs1W__frame { --pad:24px;--card-w:440px;--code:12px;--w:330px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.relative> — `Guides users on the fly`)` uses `22px`, `999px`, `50%`, `17px` radii, `#171717` highlights, and assets (5c285b27cdda1fe8-s.p.0yo6-5yoeeud..., 83afe278b6a6bb3c-s.p.0q-301v4kxxn..., gt-walsheim-medium.ttf).
5. **Colophon & Global Directory Footer (<footer.footer-module__d_pQKq__root> — `https://jimo.ai/product/ai`)**:
   - DOM & Selectors: Landmark `<footer class="footer-module__d_pQKq__root">` anchoring `AI Agent for User Onboarding in ` footer links (`Products · Use Case · Pricing · Customers · Resources`), copy *"Interface knowledge"*, and `#fff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer-module__d_pQKq__root> — `https://jimo.ai/product/ai`)` aligns to `1099px` extracted from `jimo-ai_product-ai` stylesheet with `16px` lateral canvas padding with `6px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Adoption Agent New Guides, answers and acts in your product"*
- Copy Excerpt 2: *"Adoption Agent New"*
- Copy Excerpt 3: *"Guides, answers and acts in your product"*
- Copy Excerpt 4: *"Interface knowledge"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.32,.72,0,1)`
- **Extracted Stylesheet Rules (`jimo-ai_product-ai`)**:
- `ento-sdk-module__RcAs1W__root.is-... { opacity:1;pointer-events:auto }`
- `.bento-sdk-module__RcAs1W__scene { transform-origin:0 0;width:100%;height:100%;position:absolute;top:0;left... }`
- `.bento-sdk-module__RcAs1W__frame { --pad:24px;--card-w:440px;--code:12px;--w:330px }`
- `.bento-sdk-module__RcAs1W__card { left:var(--pad);top:calc(var(--s) + var(--peek));width:var(--card-w);hei... }`
- `.bento-sdk-module__RcAs1W__bar { border-bottom:1px solid var(--hair);align-items:center;gap:6px;height:44... }`
- **Per-Selector Transition Rules**:
- **Selector `.bento-sdk-module__RcAs1W__root`**: `transition: opacity .5s cubic-bezier(.22,1,.36,1)` extracted from `jimo-ai_product-ai` stylesheet.
- **Selector `.bento-sdk-module__RcAs1W__stack`**: `transition: opacity .7s var(--ease), transform .7s var(--ease), filter .7s...` extracted from `jimo-ai_product-ai` stylesheet.
- **Selector `.bento-sdk-module__RcAs1W__str`**: `transition: color .3s,text-shadow .3s` extracted from `jimo-ai_product-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.jlp-fnav>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `jimo-ai_product-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
