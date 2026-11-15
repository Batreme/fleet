---
title: "UI Prompt Blueprint: about-centra-com"
date: 2026-11-15
target: "[[overview|about-centra-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#d9d9d9` canvas, `#191919` ink, `#f85943` accent)"
---

# UI Design System & Master Generation Blueprint: about-centra-com

> **Centra? Centra! The definitive guide.** (https://about.centra.com) — The commerce platform for fashion brands.

![Desktop Viewport Capture (1440x6253)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Centra? Centra! The definitive guide.** (`https://about.centra.com`). The commerce platform for fashion brands.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#d9d9d9` canvas, `#191919` ink, `#f85943` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#d9d9d9` (`var(--_colours---mono--200)` in `:root`) paired with `#191919` primary typography and `#f85943` accents.
  - **Extracted Typographic Hierarchy**: Pairs `neue-haas-grotesk-display` for display copy (`Centra? Centra!`) with `neue-haas-grotesk-text` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.4,0,.2,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×6253px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `about-centra-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#d9d9d9` | `var(--_colours---mono--200)` in `:root` |
| **Primary Typography Ink** | `#fecf48` | `var(--_colours---yellow--main)` in `:root` |
| **Elevated Surface / Card Substrate** | `#191919` | `var(--_colours---mono--800)` in `:root` |
| **Interactive Accent / Highlight** | `#f85943` | `var(--_colours---red--main)` in `:root` |
| **Secondary / Muted Copy** | `#333` | `var(--_colours---mono--600)` in `:root` |
| **Structural Hairline Border** | `#1cad56` | `var(--_colours---green--main)` in `:root` |
| **Variable Token (`--_colours---blue--main`)** | `#1d80f6` | `var(--_colours---blue--main)` in `:root` |
| **Variable Token (`--_colours---mono--400`)** | `#787878` | `var(--_colours---mono--400)` in `:root` |
| **Variable Token (`--_colours---mono--700`)** | `#252525` | `var(--_colours---mono--700)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_colours---mono--0` | `white` | Typography / Scale Token |
| `--_colours---mono--900` | `black` | Typography / Scale Token |
| `--_colours---mono--300` | `darkgrey` | Typography / Scale Token |
| `--_colours---mono--200` | `#d9d9d9` | Typography / Scale Token |
| `--padding-inner-md` | `40px` | Layout / Spatial Grid Token |
| `--_colours---yellow--main` | `#fecf48` | Layout / Spatial Grid Token |
| `--padding-section-xl` | `90px` | Layout / Spatial Grid Token |
| `--padding-inner-sm` | `20px` | Layout / Spatial Grid Token |
| `--_colours---mono--800` | `#191919` | Typography / Scale Token |
| `--_colours---red--main` | `#f85943` | Layout / Spatial Grid Token |
| `--_colours---mono--600` | `#333` | Typography / Scale Token |
| `--_colours---green--main` | `#1cad56` | Layout / Spatial Grid Token |
| `--_colours---blue--main` | `#1d80f6` | Layout / Spatial Grid Token |
| `--padding-inner-lg` | `80px` | Layout / Spatial Grid Token |
| `--_colours---mono--400` | `#787878` | Typography / Scale Token |
| `--_colours---mono--700` | `#252525` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `neue-haas-grotesk-display`.
- **Primary Body Stack**: `neue-haas-grotesk-text`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`).
- **Body Copy**: rule `p` (`font-size: inherit`, `font-weight: inherit`).
- **Metadata & Navigation Labels**: CSS variables `--_colours---mono--0: white`, `--_colours---mono--900: black`, `--_colours---mono--300: darkgrey`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `about-centra-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `about-centra-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `about-centra-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.navigation-glass-wrapper>` and `<section.section-parallax>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Centra? Centra! The definitive guide.      │
│ ====================================================================== │
│ [ <nav.navigation-glass-wr | 13 ½ Centra Facts · Brands on Centra   ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.heading-animation>                          |   │
│ | H1: Centra? Centra!                                              |   │
│ | Substrate: #d9d9d9    | Ink: #191919    | Accent: #f85943        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section-parallax>) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Yes, it’s us. Centra. The fa |  | Centra preview in 60 seconds | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<nav.navigation-gl] -> [<section.heading-a] -> [<section.section-p] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wf-neuehaasgro) | https://about.centra.com           │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.navigation-glass-wrapper> — `about-centra-com`)**:
   - Landmark `<nav class="navigation-glass-wrapper mobile-navigation">` hosting `Centra? Centra! The definitive guide` navigation (`13 ½ Centra Facts · Brands on Centra`), DOM attributes (`data-wf-domain="about.centra.com"`, `data-wf-page="6a0af5d1e1f707540842bee4"`, `data-wf-site="6a0af5d1e1f707540842bf02"`, `data-cbid="93a8c043-1906-4454-86..."`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.heading-animation> — `Centra? Centra!`)**:
   - Landmark `<section class="heading-animation">` presenting display lead `Centra? Centra!` and copy excerpt *"Necessary 10 Necessary cookies help make a website usable by enab"* over `#d9d9d9` canvas and `#191919` ink.
3. **Primary Showcase & Content Grid (<section.section-parallax> — `Yes, it’s us. Centra. The famously`)**:
   - Landmark `<section class="section-parallax">` rendering section `Yes, it’s us. Centra. The famously unfamous comme...` with copy *"Cookiebot 1 Learn more about this provider CookieConsent Stores t"*, asset references (`cdn.prod.website-files.com`, `centra-centra.webflow.shared.3f63...`, `cc.js`, `configuration.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section-call-to-action> — `Centra preview in 60 seconds`)**:
   - Landmark `<section class="section-call-to-action">` framing `Centra preview in 60 seconds` and `Learn more about this provider` (*"Learn more about this provider"*) with `#191919` surface cards, `#f85943` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.wf-neuehaasgrotesktext-n4-active> — `https://about.centra.com`)**:
   - Landmark `<footer class="wf-neuehaasgrotesktext-n4-active">` anchoring `Centra? Centra! The definitive g` footer links (`13 ½ Centra Facts · Brands on Centra`), copy *"Stores the user's cookie consent state for the current domai"*, and `#1cad56` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: about-centra-com (Centra? Centra! The definitive guide.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `about-centra-com` (**Centra? Centra! The definitive guide.** — `https://about.centra.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#d9d9d9` canvas, `#191919` ink, `#f85943` accent).
- **Identity & Domain Context**: The commerce platform for fashion brands.
- **Primary Substrate**: `#d9d9d9` (`var(--_colours---mono--200)` in `:root`), **Primary Ink**: `#191919`, **Accent / Highlight**: `#f85943`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#d9d9d9` (`var(--_colours---mono--200)` in `:root`) paired with `#191919` primary typography and `#f85943` accents.
  - **Extracted Typographic Hierarchy**: Pairs `neue-haas-grotesk-display` for display copy (`Centra? Centra!`) with `neue-haas-grotesk-text` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.4,0,.2,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `about-centra-com` in your global stylesheet:

:root {
  /* Centra? Centra! The definitive guide. (about-centra-com) — Ground-Truth Extracted CSS Variables */
  --_colours---mono--0: white; /* Typography / Scale Token (about-centra-com) */
  --_colours---mono--900: black; /* Typography / Scale Token (about-centra-com) */
  --_colours---mono--300: darkgrey; /* Typography / Scale Token (about-centra-com) */
  --_colours---mono--200: #d9d9d9; /* Typography / Scale Token (about-centra-com) */
  --padding-inner-md: 40px; /* Layout / Spatial Grid Token (about-centra-com) */
  --_colours---yellow--main: #fecf48; /* Layout / Spatial Grid Token (about-centra-com) */
  --padding-section-xl: 90px; /* Layout / Spatial Grid Token (about-centra-com) */
  --padding-inner-sm: 20px; /* Layout / Spatial Grid Token (about-centra-com) */
  --_colours---mono--800: #191919; /* Typography / Scale Token (about-centra-com) */
  --_colours---red--main: #f85943; /* Layout / Spatial Grid Token (about-centra-com) */
  --_colours---mono--600: #333; /* Typography / Scale Token (about-centra-com) */
  --_colours---green--main: #1cad56; /* Layout / Spatial Grid Token (about-centra-com) */
  --_colours---blue--main: #1d80f6; /* Layout / Spatial Grid Token (about-centra-com) */
  --padding-inner-lg: 80px; /* Layout / Spatial Grid Token (about-centra-com) */
  --_colours---mono--400: #787878; /* Typography / Scale Token (about-centra-com) */
  --_colours---mono--700: #252525; /* Typography / Scale Token (about-centra-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#d9d9d9` — grounded in `var(--_colours---mono--200)` in `:root`
- **Primary Typography Ink**: `#fecf48` — grounded in `var(--_colours---yellow--main)` in `:root`
- **Elevated Surface / Card Substrate**: `#191919` — grounded in `var(--_colours---mono--800)` in `:root`
- **Interactive Accent / Highlight**: `#f85943` — grounded in `var(--_colours---red--main)` in `:root`
- **Secondary / Muted Copy**: `#333` — grounded in `var(--_colours---mono--600)` in `:root`
- **Structural Hairline Border**: `#1cad56` — grounded in `var(--_colours---green--main)` in `:root`
- **Variable Token (`--_colours---blue--main`)**: `#1d80f6` — grounded in `var(--_colours---blue--main)` in `:root`
- **Variable Token (`--_colours---mono--400`)**: `#787878` — grounded in `var(--_colours---mono--400)` in `:root`
- **Variable Token (`--_colours---mono--700`)**: `#252525` — grounded in `var(--_colours---mono--700)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×6253px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `about-centra-com` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `neue-haas-grotesk-display`
- **Body Font Stack**: `neue-haas-grotesk-text`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Body Copy Rule**: rule `p` (`font-size: inherit`, `font-weight: inherit`)
- **Metadata & Index Rule**: CSS variables `--_colours---mono--0: white`, `--_colours---mono--900: black`, `--_colours---mono--300: darkgrey`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `about-centra-com` (`Centra? Centra! The definitive guide.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.navigation-glass-wrapper> — `about-centra-com`)**:
   - DOM & Selectors: Landmark `<nav class="navigation-glass-wrapper mobile-navigation">` hosting `Centra? Centra! The definitive guide` navigation (`13 ½ Centra Facts · Brands on Centra`), DOM attributes (`data-wf-domain="about.centra.com"`, `data-wf-page="6a0af5d1e1f707540842bee4"`, `data-wf-site="6a0af5d1e1f707540842bf02"`, `data-cbid="93a8c043-1906-4454-86..."`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.navigation-glass-wrapper> — `about-centra-com`)` (`about-centra-com`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(.4,0,.2,1)` transitions and links `13 ½ Centra Facts · Brands on Centra`.
2. **Hero Stage & Focal Lead (<section.heading-animation> — `Centra? Centra!`)**:
   - DOM & Selectors: Landmark `<section class="heading-animation">` presenting display lead `Centra? Centra!` and copy excerpt *"Necessary 10 Necessary cookies help make a website usable by enab"* over `#d9d9d9` canvas and `#191919` ink.
   - Responsive Contract: Hero stage (`1440×6253px` desktop / `390×2400px` mobile) sets `#d9d9d9` background with `#191919` headline `Centra? Centra!`.
3. **Primary Showcase & Content Grid (<section.section-parallax> — `Yes, it’s us. Centra. The famously`)**:
   - DOM & Selectors: Landmark `<section class="section-parallax">` rendering section `Yes, it’s us. Centra. The famously unfamous comme...` with copy *"Cookiebot 1 Learn more about this provider CookieConsent Stores t"*, asset references (`cdn.prod.website-files.com`, `centra-centra.webflow.shared.3f63...`, `cc.js`, `configuration.js`), and grid rule `summary { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section-parallax> — `Yes, it’s us. Centra. The famously`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section-call-to-action> — `Centra preview in 60 seconds`)**:
   - DOM & Selectors: Landmark `<section class="section-call-to-action">` framing `Centra preview in 60 seconds` and `Learn more about this provider` (*"Learn more about this provider"*) with `#191919` surface cards, `#f85943` accents, and `video { vertical-align:baseline;display:inline-block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section-call-to-action> — `Centra preview in 60 seconds`)` uses `3px`, `100%`, `50%`, `2px` radii, `#f85943` highlights, and assets (cdn.prod.website-files.com, centra-centra.webflow.shared.3f63..., cc.js).
5. **Colophon & Global Directory Footer (<footer.wf-neuehaasgrotesktext-n4-active> — `https://about.centra.com`)**:
   - DOM & Selectors: Landmark `<footer class="wf-neuehaasgrotesktext-n4-active">` anchoring `Centra? Centra! The definitive g` footer links (`13 ½ Centra Facts · Brands on Centra`), copy *"Stores the user's cookie consent state for the current domai"*, and `#1cad56` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wf-neuehaasgrotesktext-n4-active> — `https://about.centra.com`)` aligns to `940px` extracted from `about-centra-com` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="about.centra.com", data-wf-page="6a0af5d1e1f707540842bee4", data-wf-site="6a0af5d1e1f707540842bf02").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Necessary 10 Necessary cookies help make a website usable by enabling basic functi..."*
- Copy Excerpt 2: *"Cookiebot 1 Learn more about this provider CookieConsent Stores the user's cookie..."*
- Copy Excerpt 3: *"Learn more about this provider"*
- Copy Excerpt 4: *"Stores the user's cookie consent state for the current domain"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`about-centra-com`)**:
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`
- `summary { display:block }`
- `video { vertical-align:baseline;display:inline-block }`
- `template { display:none }`
- `strong { font-weight:700 }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `about-centra-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `about-centra-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `about-centra-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.navigation-glass-wrapper>` and `<section.section-parallax>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `about-centra-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
