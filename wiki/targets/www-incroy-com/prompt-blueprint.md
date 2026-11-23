---
title: "UI Prompt Blueprint: www-incroy-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-incroy-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0082f3` accent)"
---

# UI Design System & Master Generation Blueprint: www-incroy-com

> **Incroy · Webflow Certified Development Agency** (https://www.incroy.com/) — Incroy is a Webflow agency serving medium to large businesses. We handle design, development, copywriting, and ongoing site management un...

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Incroy · Webflow Certified Development Agency** (`https://www.incroy.com/`). Incroy is a Webflow agency serving medium to large businesses. We handle design, development, copywriting, and ongoing site management un...
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0082f3` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0082f3` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Suisseintl Book` for display copy (`We might not be your first, but we’l`) with `Inter` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1008px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.32,.72,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1008px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1008px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#6053e5` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--link-color--link-primary` | `var(--base-color-brand--brand-primary)` | Typography Ink Token |
| `--background-color--background-primary` | `var(--base-color-neutral--black)` | Canvas / Surface Token |
| `--text-color--text-alternate` | `var(--base-color-neutral--white)` | Typography Ink Token |
| `--text-color--text-primary` | `var(--base-color-neutral--black)` | Typography Ink Token |
| `--text-color--text-secondary` | `var(--base-color-neutral--neutral-darker)` | Typography Ink Token |
| `--background-color--background-success` | `var(--base-color-system--success-green)` | Canvas / Surface Token |
| `--text-color--text-success` | `var(--base-color-system--success-green-dark)` | Typography Ink Token |
| `--base-color-neutral--white` | `#fff` | Canvas / Surface Token |
| `--border-color--border-primary` | `var(--base-color-neutral--neutral-lightest)` | Brand / Palette Token |
| `--background-color--background-alternate` | `var(--base-color-neutral--white)` | Canvas / Surface Token |
| `--background-color--background-secondary` | `var(--base-color-brand--brand-primary)` | Canvas / Surface Token |
| `--background-color--background-tertiary` | `var(--base-color-brand--pink)` | Canvas / Surface Token |
| `--background-color--background-error` | `var(--base-color-system--error-red)` | Canvas / Surface Token |
| `--text-color--text-error` | `var(--base-color-system--error-red-dark)` | Typography Ink Token |
| `--border-color--border-subtle` | `var(--base-color-neutral--neutral-dark)` | Brand / Palette Token |
| `--background-color--background-warning` | `var(--base-color-system--warning-yellow)` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Suisseintl Book`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 62px`, `line-height: 66.96px`, `font-weight: 400`, `letter-spacing: -3.41px`); rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 60px`, `font-weight: 400`, `letter-spacing: -2.16px`); rule `h2` (`font-size: 32px`, `line-height: 36px`).
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 23.994px`, `font-weight: 600`, `letter-spacing: -0.27px`); rule `body` (`font-size: 14px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 21.328px`, `font-weight: 600`, `letter-spacing: -0.27px`); rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.32,.72,0,1)`, `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.322,.014,0,.99)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-incroy-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-incroy-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-incroy-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.32,.72,0,1)`)**: Governs interactive state transitions across `<nav.navigation>` and `<section.section-dots:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine, Lottie Vector Animation Player, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Incroy · Webflow Certified Development Age │
│ ====================================================================== │
│ [ <nav.navigation> (1248x101px)       | H o m e · W o r k · P r o c  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.section-dots> (w=1440px)                      | │
│ | H1: We might not be your first, but we’ll certainly b...           | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #0082f3                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section-dots:nth() max-w: 1008px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | W e m i g h t n o t b e y o  |  | W h a t i n t h e w o r l d  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.section-dots:nth() — T h a t ’ s w h e r e | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.hide>       ) | https://www.incroy.com/              │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.navigation>        ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.section-dots>) — 390px Vertical Lead          | │
│ | H1: We might not be your first, but we’ll certainly b...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.section-dots:) — 1-Col Stack              | │
│ | [ Item 1: W e m i g h t n o t b e y o u r f i r s t , b u t...   ] | │
│ | [ Item 2: W h a t i n t h e w o r l d w i d e w e b h a s h...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.section-dots:nt) — 1-Col (T h a t ’ s w h e ) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.hide>       ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.navigation> — `www-incroy-com`)**:
   - Landmark `<nav class="navigation">` (`1248x101px`) hosting `Incroy · Webflow Certified Developme` navigation (`H o m e · W o r k · P r o c e s s · W h o a r e w e ? · C o n t a c t`), DOM attributes (`data-wf-domain="www.incroy.com"`, `data-wf-page="6a21b959b61cf447eaaeea89"`, `data-wf-site="6a21b956b61cf447eaaeea3c"`, `data-page-theme="light"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.section-dots> — `We might not be your first, but we`)**:
   - Landmark `<section class="section-dots">` presenting display lead `We might not be your first, but we’ll certainly b...` and copy excerpt *"If you need a beautiful website that reflects your name, your mes"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.section-dots:nth(2)> — `W e m i g h t n o t b e y o u r f `)**:
   - Landmark `<section class="section-dots">` rendering section `W e m i g h t n o t b e y o u r f i r s t , b u t...` with copy *"I f y o u n e e d a b e a u t i f u l w e b s i t e t h a t r e f"*, asset references (`cdn.prod.website-files.com`, `incroy-v2.shared.e656a73ee.css`, `clarity.js`, `pw6po7h0ab`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section-dots:nth(3)> — `W h a t i n t h e w o r l d w i d `)**:
   - Landmark `<section class="section-dots">` framing `W h a t i n t h e w o r l d w i d e w e b h a s h...` and `T h a t ’ s w h e r e w e c o m e i n` (*"L e t ’ s g o s i t e s e e i n g"*) with `#ffff00` surface cards, `#0082f3` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.hide> — `https://www.incroy.com/`)**:
   - Landmark `<footer class="hide">` anchoring `Incroy · Webflow Certified Devel` footer links (`H o m e · W o r k · P r o c e s s · W h o a r e w e ? · C o n t a c t`), copy *"W e d e s i g n a n d d e v e l o p w e b s i t e s t h a t "*, and `#e2e2e2` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-incroy-com (Incroy · Webflow Certified Development Agency)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-incroy-com` (**Incroy · Webflow Certified Development Agency** — `https://www.incroy.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0082f3` accent).
- **Identity & Domain Context**: Incroy is a Webflow agency serving medium to large businesses. We handle design, development, copywriting, and ongoing site management un...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#0082f3`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0082f3` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Suisseintl Book` for display copy (`We might not be your first, but we’l`) with `Inter` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1008px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.32,.72,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-incroy-com` in your global stylesheet:

:root {
  /* Incroy · Webflow Certified Development Agency (www-incroy-com) — Live-Grounded CSS Variables */
  --link-color--link-primary: var(--base-color-brand--brand-primary); /* Typography Ink Token (www-incroy-com) */
  --background-color--background-primary: var(--base-color-neutral--black); /* Canvas / Surface Token (www-incroy-com) */
  --text-color--text-alternate: var(--base-color-neutral--white); /* Typography Ink Token (www-incroy-com) */
  --text-color--text-primary: var(--base-color-neutral--black); /* Typography Ink Token (www-incroy-com) */
  --text-color--text-secondary: var(--base-color-neutral--neutral-darker); /* Typography Ink Token (www-incroy-com) */
  --background-color--background-success: var(--base-color-system--success-green); /* Canvas / Surface Token (www-incroy-com) */
  --text-color--text-success: var(--base-color-system--success-green-dark); /* Typography Ink Token (www-incroy-com) */
  --base-color-neutral--white: #fff; /* Canvas / Surface Token (www-incroy-com) */
  --border-color--border-primary: var(--base-color-neutral--neutral-lightest); /* Brand / Palette Token (www-incroy-com) */
  --background-color--background-alternate: var(--base-color-neutral--white); /* Canvas / Surface Token (www-incroy-com) */
  --background-color--background-secondary: var(--base-color-brand--brand-primary); /* Canvas / Surface Token (www-incroy-com) */
  --background-color--background-tertiary: var(--base-color-brand--pink); /* Canvas / Surface Token (www-incroy-com) */
  --background-color--background-error: var(--base-color-system--error-red); /* Canvas / Surface Token (www-incroy-com) */
  --text-color--text-error: var(--base-color-system--error-red-dark); /* Typography Ink Token (www-incroy-com) */
  --border-color--border-subtle: var(--base-color-neutral--neutral-dark); /* Brand / Palette Token (www-incroy-com) */
  --background-color--background-warning: var(--base-color-system--warning-yellow); /* Canvas / Surface Token (www-incroy-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffff00` — grounded in `mark { background: #ffff00 }`
- **Interactive Accent / Highlight**: `#0082f3` — grounded in `.w-dropdown-link.w--current { color: #0082f3 }`
- **Secondary / Muted Copy**: `#6053e5` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#e2e2e2` — grounded in `blockquote { border-left: #e2e2e2 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1008px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1008px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Suisseintl Book`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 62px`, `line-height: 66.96px`, `font-weight: 400`, `letter-spacing: -3.41px`); rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: live computed `h2` (`font-size: 48px`, `line-height: 60px`, `font-weight: 400`, `letter-spacing: -2.16px`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy Rule**: live computed `body` (`font-size: 18px`, `line-height: 23.994px`, `font-weight: 600`, `letter-spacing: -0.27px`); rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 21.328px`, `font-weight: 600`, `letter-spacing: -0.27px`); rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-incroy-com` (`Incroy · Webflow Certified Development Agency`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.navigation> — `www-incroy-com`)**:
   - DOM & Selectors: Landmark `<nav class="navigation">` (`1248x101px`) hosting `Incroy · Webflow Certified Developme` navigation (`H o m e · W o r k · P r o c e s s · W h o a r e w e ? · C o n t a c t`), DOM attributes (`data-wf-domain="www.incroy.com"`, `data-wf-page="6a21b959b61cf447eaaeea89"`, `data-wf-site="6a21b956b61cf447eaaeea3c"`, `data-page-theme="light"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.navigation> — `www-incroy-com`)` (`www-incroy-com`) adapts across `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)` with `cubic-bezier(.32,.72,0,1)`, `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.322,.014,0,.99)` transitions and links `H o m e · W o r k · P r o c e s s · W h o a r e w e ? · C o n t a c t`.
2. **Hero Stage & Focal Lead (<section.section-dots> — `We might not be your first, but we`)**:
   - DOM & Selectors: Landmark `<section class="section-dots">` presenting display lead `We might not be your first, but we’ll certainly b...` and copy excerpt *"If you need a beautiful website that reflects your name, your mes"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#000000` headline `We might not be your first, but we’ll certainly b...`.
3. **Primary Showcase & Content Grid (<section.section-dots:nth(2)> — `W e m i g h t n o t b e y o u r f `)**:
   - DOM & Selectors: Landmark `<section class="section-dots">` rendering section `W e m i g h t n o t b e y o u r f i r s t , b u t...` with copy *"I f y o u n e e d a b e a u t i f u l w e b s i t e t h a t r e f"*, asset references (`cdn.prod.website-files.com`, `incroy-v2.shared.e656a73ee.css`, `clarity.js`, `pw6po7h0ab`), and grid rule `body { margin: 0; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section-dots:nth(2)> — `W e m i g h t n o t b e y o u r f `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1008px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section-dots:nth(3)> — `W h a t i n t h e w o r l d w i d `)**:
   - DOM & Selectors: Landmark `<section class="section-dots">` framing `W h a t i n t h e w o r l d w i d e w e b h a s h...` and `T h a t ’ s w h e r e w e c o m e i n` (*"L e t ’ s g o s i t e s e e i n g"*) with `#ffff00` surface cards, `#0082f3` accents, and `summary { display: block; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section-dots:nth(3)> — `W h a t i n t h e w o r l d w i d `)` uses `3px`, `100%`, `50%`, `2px` radii, `#0082f3` highlights, and assets (cdn.prod.website-files.com, incroy-v2.shared.e656a73ee.css, clarity.js).
5. **Colophon & Global Directory Footer (<footer.hide> — `https://www.incroy.com/`)**:
   - DOM & Selectors: Landmark `<footer class="hide">` anchoring `Incroy · Webflow Certified Devel` footer links (`H o m e · W o r k · P r o c e s s · W h o a r e w e ? · C o n t a c t`), copy *"W e d e s i g n a n d d e v e l o p w e b s i t e s t h a t "*, and `#e2e2e2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.hide> — `https://www.incroy.com/`)` aligns to `1008px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.incroy.com", data-wf-page="6a21b959b61cf447eaaeea89", data-wf-site="6a21b956b61cf447eaaeea3c").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"If you need a beautiful website that reflects your name, your message, and your bu..."*
- Copy Excerpt 2: *"I f y o u n e e d a b e a u t i f u l w e b s i t e t h a t r e f l e c t s y o u..."*
- Copy Excerpt 3: *"L e t ’ s g o s i t e s e e i n g"*
- Copy Excerpt 4: *"W e d e s i g n a n d d e v e l o p w e b s i t e s t h a t l o o k g r e a t , d..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.32,.72,0,1)`, `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.322,.014,0,.99)`
- **Extracted Stylesheet Rules (`www-incroy-com`)**:
- `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`
- `body { margin: 0; }`
- `summary { display: block; }`
- `video { vertical-align: baseline; display: inline-block; }`
- `template { display: none; }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-incroy-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-incroy-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-incroy-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.32,.72,0,1)`)**: Governs interactive state transitions across `<nav.navigation>` and `<section.section-dots:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine, Lottie Vector Animation Player, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-incroy-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
