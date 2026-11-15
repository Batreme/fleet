---
title: "UI Prompt Blueprint: zeyraglow-com"
date: 2026-11-15
target: "[[overview|zeyraglow-com]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#720eec` canvas, `#fcfbfe` ink, `#ffba00` accent)"
---

# UI Design System & Master Generation Blueprint: zeyraglow-com

> **Zeyra Glow · Natural Body Care Products in the UAE** (https://zeyraglow.com/) — Discover natural body care products by Zeyra Glow, made with comfortable, skin-friendly ingredients for simple everyday care. Shop online...

![Desktop Viewport Capture (1440x4520)](file:///root/projects/fleet/wiki/targets/zeyraglow-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Zeyra Glow · Natural Body Care Products in the UAE** (`https://zeyraglow.com/`). Discover natural body care products by Zeyra Glow, made with comfortable, skin-friendly ingredients for simple everyday care. Shop online...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#720eec` canvas, `#fcfbfe` ink, `#ffba00` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#720eec` (`var(--woocommerce)` in `:root`) paired with `#fcfbfe` primary typography and `#ffba00` accents.
  - **Extracted Typographic Hierarchy**: Pairs `WooCommerce` for display copy (`Body care you'll actually keep using`) with `TikTok Sans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `474px` container bounds (`gap: var(--row-gap)`, padding `2.5rem`) with `cubic-bezier(.795,-.035,0,1)` easing and Swiper Touch Carousel Engine, Lottie Vector Animation Player.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/zeyraglow-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×4520px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `474px` extracted from `zeyraglow-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `2.5rem` lateral canvas padding with `var(--row-gap)` grid gap.
- **Border Radius Scale**: `4px`, `8px`, `3px`, `var(--wc-form-border-radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 474px`, `gap: var(--row-gap)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (min-width:673px)`, `@media screen and (min-width:1040px)`, `@media screen and (min-width:1110px)`, `@media screen and (min-width:1218px)`.

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
| **Variable Token (`--wc-content-bg`)** | `#fff` | `var(--wc-content-bg)` in `:root` |
| **Variable Token (`--wc-subtext`)** | `#767676` | `var(--wc-subtext)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
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
| `--wc-form-border-radius` | `4px` | Elevation / Border Token |
| `--wc-form-border-width` | `1px` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `WooCommerce`.
- **Primary Body Stack**: `TikTok Sans`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: 28px`, `line-height: 1.1`, `letter-spacing: 0.01em`, `font-weight: 500`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 28px`, `line-height: .96`, `letter-spacing: 0.001em`, `font-weight: 500`).
- **Body Copy**: CSS variables `--e-global-typography-v4-zg-body-font-family: var(--za-font-fam)`, `--e-global-typography-v4-zg-body-font-size: var(--zg-b-desk-to-tab)`, `--e-global-typography-v4-zg-body-font-weight: 400`; rule `p` (`font-size: 15px`, `line-height: 1.6`, `font-weight: 300`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 15px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.795,-.035,0,1)`, `cubic-bezier(.58,.3,.005,1)`, `cubic-bezier(0.22,1,0.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `aceholder]:focus::-webkit-input-p...`**: `transition: opacity .5s .5s ease` extracted from `zeyraglow-com` stylesheet.
- **Selector `mages .woocommerce-product-galler...`**: `transition: all cubic-bezier(.795,-.035,0,1) .5s` extracted from `zeyraglow-com` stylesheet.
- **Selector `textarea`**: `transition: all .3s` extracted from `zeyraglow-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.795,-.035,0,1)`)**: Governs interactive state transitions across `<header.elementor>` and `<section.products>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine, Lottie Vector Animation Player, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Zeyra Glow · Natural Body Care Products in │
│ ====================================================================== │
│ [ <header.elementor>       | Our story · Shop                       ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Body care you'll actually keep using                         |   │
│ | Substrate: #720eec    | Ink: #fcfbfe    | Accent: #ffba00        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.products>        ) max-w: 474px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Glow Nila Body Cream         |  | Glow Nila Body Scrub         | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.elementor>] -> [<section.hero>] -> [<section.products>] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.cart-footer>  ) | https://zeyraglow.com/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.elementor> — `zeyraglow-com`)**:
   - Landmark `<header class="elementor elementor-1083">` hosting `Zeyra Glow · Natural Body Care Produ` navigation (`Our story · Shop`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `merce-page .woocommerce-message .... { float:right }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Body care you'll actually keep usi`)**:
   - Landmark `<section class="hero">` presenting display lead `Body care you'll actually keep using` and copy excerpt *"Taxes, shipping and promos are calculated at checkout."* over `#720eec` canvas and `#fcfbfe` ink.
3. **Primary Showcase & Content Grid (<section.products> — `Glow Nila Body Cream`)**:
   - Landmark `<section class="products">` rendering section `Glow Nila Body Cream` with copy *"Taxes, shipping and promos are"*, asset references (`fonts.googleapis.com`, `embed`, `woocommerce-layout.css`, `woocommerce-smallscreen.css`), and grid rule `.woocommerce-page .col2-set { width:100% }`.
4. **Interactive Detail & Feature Matrix (<article.p-card> — `Glow Nila Body Scrub`)**:
   - Landmark `<article class="p-card">` framing `Glow Nila Body Scrub` and `Glow Nila Powder` (*"calculated at checkout."*) with `#a00` surface cards, `#ffba00` accents, and `.woocommerce-page .col2-set::before { content:" ";display:table }`.
5. **Colophon & Global Directory Footer (<footer.cart-footer> — `https://zeyraglow.com/`)**:
   - Landmark `<footer class="cart-footer cart-footer--empty">` anchoring `Zeyra Glow · Natural Body Care P` footer links (`Our story · Shop`), copy *"Inspired by Moroccan beauty rituals and crafted with natural"*, and `#fcfbfe` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: zeyraglow-com (Zeyra Glow · Natural Body Care Products in the UAE)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `zeyraglow-com` (**Zeyra Glow · Natural Body Care Products in the UAE** — `https://zeyraglow.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#720eec` canvas, `#fcfbfe` ink, `#ffba00` accent).
- **Identity & Domain Context**: Discover natural body care products by Zeyra Glow, made with comfortable, skin-friendly ingredients for simple everyday care. Shop online...
- **Primary Substrate**: `#720eec` (`var(--woocommerce)` in `:root`), **Primary Ink**: `#fcfbfe`, **Accent / Highlight**: `#ffba00`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#720eec` (`var(--woocommerce)` in `:root`) paired with `#fcfbfe` primary typography and `#ffba00` accents.
  - **Extracted Typographic Hierarchy**: Pairs `WooCommerce` for display copy (`Body care you'll actually keep using`) with `TikTok Sans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `474px` container bounds (`gap: var(--row-gap)`, padding `2.5rem`) with `cubic-bezier(.795,-.035,0,1)` easing and Swiper Touch Carousel Engine, Lottie Vector Animation Player.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `zeyraglow-com` in your global stylesheet:

:root {
  /* Zeyra Glow · Natural Body Care Products in the UAE (zeyraglow-com) — Ground-Truth Extracted CSS Variables */
  --woocommerce: #720eec; /* Color / Atmospheric Token (zeyraglow-com) */
  --wc-green: #007518; /* Color / Atmospheric Token (zeyraglow-com) */
  --wc-red: #a00; /* Color / Atmospheric Token (zeyraglow-com) */
  --wc-orange: #ffba00; /* Color / Atmospheric Token (zeyraglow-com) */
  --wc-blue: #2ea2cc; /* Color / Atmospheric Token (zeyraglow-com) */
  --wc-primary: #720eec; /* Brand / Palette Token (zeyraglow-com) */
  --wc-primary-text: #fcfbfe; /* Typography Ink Token (zeyraglow-com) */
  --wc-secondary: #e9e6ed; /* Brand / Palette Token (zeyraglow-com) */
  --wc-secondary-text: #515151; /* Typography Ink Token (zeyraglow-com) */
  --wc-highlight: #958e09; /* Canvas / Surface Token (zeyraglow-com) */
  --wc-highligh-text: white; /* Typography Ink Token (zeyraglow-com) */
  --wc-content-bg: #fff; /* Canvas / Surface Token (zeyraglow-com) */
  --wc-subtext: #767676; /* Typography Ink Token (zeyraglow-com) */
  --wc-form-border-color: rgba(32, 7, 7, 0.8); /* Brand / Palette Token (zeyraglow-com) */
  --wc-form-border-radius: 4px; /* Elevation / Border Token (zeyraglow-com) */
  --wc-form-border-width: 1px; /* Layout / Spatial Grid Token (zeyraglow-com) */
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
- **Variable Token (`--wc-content-bg`)**: `#fff` — grounded in `var(--wc-content-bg)` in `:root`
- **Variable Token (`--wc-subtext`)**: `#767676` — grounded in `var(--wc-subtext)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×4520px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `474px` extracted from `zeyraglow-com` stylesheet
- **Padding & Gutters**: `2.5rem` lateral canvas padding with `var(--row-gap)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 474px`, `gap: var(--row-gap)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2.5rem` horizontal padding
- **Media Queries**: `@media screen and (min-width:673px)`, `@media screen and (min-width:1040px)`, `@media screen and (min-width:1110px)`, `@media screen and (min-width:1218px)`
- **Corner Radii**: `4px`, `8px`, `3px`, `var(--wc-form-border-radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `WooCommerce`
- **Body Font Stack**: `TikTok Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: 28px`, `line-height: 1.1`, `letter-spacing: 0.01em`, `font-weight: 500`)
- **H2 Section Rule**: rule `h2` (`font-size: 28px`, `line-height: .96`, `letter-spacing: 0.001em`, `font-weight: 500`)
- **Body Copy Rule**: CSS variables `--e-global-typography-v4-zg-body-font-family: var(--za-font-fam)`, `--e-global-typography-v4-zg-body-font-size: var(--zg-b-desk-to-tab)`, `--e-global-typography-v4-zg-body-font-weight: 400`; rule `p` (`font-size: 15px`, `line-height: 1.6`, `font-weight: 300`)
- **Metadata & Index Rule**: rule `small` (`font-size: 15px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `zeyraglow-com` (`Zeyra Glow · Natural Body Care Products in the UAE`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.elementor> — `zeyraglow-com`)**:
   - DOM & Selectors: Landmark `<header class="elementor elementor-1083">` hosting `Zeyra Glow · Natural Body Care Produ` navigation (`Our story · Shop`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `merce-page .woocommerce-message .... { float:right }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.elementor> — `zeyraglow-com`)` (`zeyraglow-com`) adapts across `@media screen and (min-width:673px)`, `@media screen and (min-width:1040px)`, `@media screen and (min-width:1110px)`, `@media screen and (min-width:1218px)` with `cubic-bezier(.795,-.035,0,1)`, `cubic-bezier(.58,.3,.005,1)`, `cubic-bezier(0.22,1,0.36,1)` transitions and links `Our story · Shop`.
2. **Hero Stage & Focal Lead (<section.hero> — `Body care you'll actually keep usi`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Body care you'll actually keep using` and copy excerpt *"Taxes, shipping and promos are calculated at checkout."* over `#720eec` canvas and `#fcfbfe` ink.
   - Responsive Contract: Hero stage (`1440×4520px` desktop / `390×2400px` mobile) sets `#720eec` background with `#fcfbfe` headline `Body care you'll actually keep using`.
3. **Primary Showcase & Content Grid (<section.products> — `Glow Nila Body Cream`)**:
   - DOM & Selectors: Landmark `<section class="products">` rendering section `Glow Nila Body Cream` with copy *"Taxes, shipping and promos are"*, asset references (`fonts.googleapis.com`, `embed`, `woocommerce-layout.css`, `woocommerce-smallscreen.css`), and grid rule `.woocommerce-page .col2-set { width:100% }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.products> — `Glow Nila Body Cream`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 474px`, `gap: var(--row-gap)`) on desktop and Single-column vertical stack at `390px` viewport width with `2.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.p-card> — `Glow Nila Body Scrub`)**:
   - DOM & Selectors: Landmark `<article class="p-card">` framing `Glow Nila Body Scrub` and `Glow Nila Powder` (*"calculated at checkout."*) with `#a00` surface cards, `#ffba00` accents, and `.woocommerce-page .col2-set::before { content:" ";display:table }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.p-card> — `Glow Nila Body Scrub`)` uses `4px`, `8px`, `3px`, `var(--wc-form-border-radius)` radii, `#ffba00` highlights, and assets (fonts.googleapis.com, embed, woocommerce-layout.css).
5. **Colophon & Global Directory Footer (<footer.cart-footer> — `https://zeyraglow.com/`)**:
   - DOM & Selectors: Landmark `<footer class="cart-footer cart-footer--empty">` anchoring `Zeyra Glow · Natural Body Care P` footer links (`Our story · Shop`), copy *"Inspired by Moroccan beauty rituals and crafted with natural"*, and `#fcfbfe` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.cart-footer> — `https://zeyraglow.com/`)` aligns to `474px` extracted from `zeyraglow-com` stylesheet with `2.5rem` lateral canvas padding with `var(--row-gap)` grid gap and attributes (data-wp-strategy="defer", data-wp-strategy="defer", data-wp-strategy="defer").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Taxes, shipping and promos are calculated at checkout."*
- Copy Excerpt 2: *"Taxes, shipping and promos are"*
- Copy Excerpt 3: *"calculated at checkout."*
- Copy Excerpt 4: *"Inspired by Moroccan beauty rituals and crafted with natural ingredients for soft,..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.795,-.035,0,1)`, `cubic-bezier(.58,.3,.005,1)`, `cubic-bezier(0.22,1,0.36,1)`
- **Extracted Stylesheet Rules (`zeyraglow-com`)**:
- `merce-page .woocommerce-message .... { float:right }`
- `.woocommerce-page .col2-set { width:100% }`
- `.woocommerce-page .col2-set::before { content:" ";display:table }`
- `.woocommerce-page .col2-set::after { clear:both }`
- `.woocommerce-page .col2-set .col-1 { float:left;width:48% }`
- **Per-Selector Transition Rules**:
- **Selector `aceholder]:focus::-webkit-input-p...`**: `transition: opacity .5s .5s ease` extracted from `zeyraglow-com` stylesheet.
- **Selector `mages .woocommerce-product-galler...`**: `transition: all cubic-bezier(.795,-.035,0,1) .5s` extracted from `zeyraglow-com` stylesheet.
- **Selector `textarea`**: `transition: all .3s` extracted from `zeyraglow-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.795,-.035,0,1)`)**: Governs interactive state transitions across `<header.elementor>` and `<section.products>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine, Lottie Vector Animation Player, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `zeyraglow-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
