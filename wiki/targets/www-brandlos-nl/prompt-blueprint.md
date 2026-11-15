---
title: "UI Prompt Blueprint: www-brandlos-nl"
date: 2026-11-15
target: "[[overview|www-brandlos-nl]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#f4f4f4` canvas, `#040404` ink, `#3a39ff` accent)"
---

# UI Design System & Master Generation Blueprint: www-brandlos-nl

> **Brandlos · Het creatieve bureau van Limburg** (https://www.brandlos.nl) — Creatief bureau in Limburg. Wij bouwen merken met lef en karakter: van strategie en identiteit tot campagnes die opvallen. Geen grijze mu...

![Desktop Viewport Capture (1440x9524)](file:///root/projects/fleet/wiki/targets/www-brandlos-nl/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Brandlos · Het creatieve bureau van Limburg** (`https://www.brandlos.nl`). Creatief bureau in Limburg. Wij bouwen merken met lef en karakter: van strategie en identiteit tot campagnes die opvallen. Geen grijze mu...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f4f4f4` canvas, `#040404` ink, `#3a39ff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f4f4f4` (`var(--_global-vars---light)` in `:root`) paired with `#040404` primary typography and `#3a39ff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Vastagogrotesk` for display copy (`Omdat gewoon te gewoontjes is`) with `Arial` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(0.22,1,0.36,1)` easing and GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-brandlos-nl/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×9524px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `www-brandlos-nl` stylesheet.
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `15px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f4f4` | `var(--_global-vars---light)` in `:root` |
| **Primary Typography Ink** | `#040404` | `var(--_global-vars---dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fbd050` | `var(--_global-vars---accent-1)` in `:root` |
| **Interactive Accent / Highlight** | `#3a39ff` | `var(--_global-vars---accent-2)` in `:root` |
| **Secondary / Muted Copy** | `#ff5b23` | `var(--_global-vars---accent-5)` in `:root` |
| **Structural Hairline Border** | `#ade6ed` | `var(--_global-vars---accent-3)` in `:root` |
| **Variable Token (`--_global-vars---accent-4`)** | `#e9a2e4` | `var(--_global-vars---accent-4)` in `:root` |
| **Variable Token (`--_global-vars---grey`)** | `#b7b7b7` | `var(--_global-vars---grey)` in `:root` |
| **Variable Token (`--swiper-theme-color`)** | `#007aff` | `var(--swiper-theme-color)` in stylesheet |
| **Variable Token (`--swiper-preloader-color`)** | `#fff` | `var(--swiper-preloader-color)` in stylesheet |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_global-vars---light` | `#f4f4f4` | Canvas / Surface Token |
| `--_global-vars---dark` | `#040404` | Canvas / Surface Token |
| `--_global-vars---accent-1` | `#fbd050` | Brand / Palette Token |
| `--_global-vars---accent-2` | `#3a39ff` | Brand / Palette Token |
| `--_global-vars---accent-5` | `#ff5b23` | Brand / Palette Token |
| `--_global-vars---accent-3` | `#ade6ed` | Brand / Palette Token |
| `--_global-vars---accent-4` | `#e9a2e4` | Brand / Palette Token |
| `--_global-vars---grey` | `#b7b7b7` | Color / Atmospheric Token |
| `--underline-scale` | `1` | Design System Custom Token |
| `--pt-color` | `#fbd050` | Brand / Palette Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--swiper-preloader-color` | `#fff` | Brand / Palette Token |
| `--swiper-navigation-size` | `44px` | Layout / Spatial Grid Token |
| `--www-brandlos-nl-bg` | `#f4f4f4` | Canvas Substrate (from `var(--_global-vars---light)` in `:root`) |
| `--www-brandlos-nl-ink` | `#040404` | Primary Typography Ink (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Vastagogrotesk`.
- **Primary Body Stack**: `Arial`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`).
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.22,1,0.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-brandlos-nl` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-brandlos-nl` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-brandlos-nl` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,1,0.36,1)`)**: Governs interactive state transitions across `<header.w-mod-js>` and `<section.home-showreel>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Brandlos · Het creatieve bureau van Limbur │
│ ====================================================================== │
│ [ <header.w-mod-js>        | Toestemming · Details · [#IABV2SETTING ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.home-hero>                                  |   │
│ | H1: Omdat gewoon te gewoontjes is                                |   │
│ | Substrate: #f4f4f4    | Ink: #040404    | Accent: #3a39ff        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.home-showreel>   ) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Kijk mam, dit hebben wij gem |  | Strategisch sterk, grafisch  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.w-mod-js>] -> [<section.home-hero] -> [<section.home-show]  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.CybotCookiebot) | https://www.brandlos.nl            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-brandlos-nl`)**:
   - Landmark `<header class="w-mod-js">` hosting `Brandlos · Het creatieve bureau van ` navigation (`Toestemming · Details · [#IABV2SETTINGS#] · Over · Details tonen`), DOM attributes (`data-wf-domain="www.brandlos.nl"`, `data-wf-page="6a60a2741f0d39e46e0880df"`, `data-wf-site="6a60a2731f0d39e46e0880dc"`, `data-nosnippet`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `Omdat gewoon te gewoontjes is`)**:
   - Landmark `<section class="home-hero">` presenting display lead `Omdat gewoon te gewoontjes is` and copy excerpt *"Toestemmingsselectie"* over `#f4f4f4` canvas and `#040404` ink.
3. **Primary Showcase & Content Grid (<section.home-showreel> — `Kijk mam, dit hebben wij gemaakt`)**:
   - Landmark `<section class="home-showreel">` rendering section `Kijk mam, dit hebben wij gemaakt` with copy *"Noodzakelijk 5 Noodzakelijke cookies helpen een website bruikbaar"*, asset references (`cdn.prod.website-files.com`, `brandlos-nl.webflow.shared.3ea0ad...`, `cc.js`, `configuration.js`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.home-about> — `Strategisch sterk, grafisch verdom`)**:
   - Landmark `<section class="home-about">` framing `Strategisch sterk, grafisch verdomd goed` and `Vrienden van Brandlos` (*"Cloudflare 1 Meer informatie over deze aanbieder cf.turnstile.u D"*) with `#fbd050` surface cards, `#3a39ff` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.CybotCookiebotDialogContentWrapper> — `https://www.brandlos.nl`)**:
   - Landmark `<footer class="CybotCookiebotDialogContentWrapper">` anchoring `Brandlos · Het creatieve bureau ` footer links (`Toestemming · Details · [#IABV2SETTINGS#] · Over · Details tonen`), copy *"Meer informatie over deze aanbieder"*, and `#ade6ed` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-brandlos-nl (Brandlos · Het creatieve bureau van Limburg)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-brandlos-nl` (**Brandlos · Het creatieve bureau van Limburg** — `https://www.brandlos.nl`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f4f4f4` canvas, `#040404` ink, `#3a39ff` accent).
- **Identity & Domain Context**: Creatief bureau in Limburg. Wij bouwen merken met lef en karakter: van strategie en identiteit tot campagnes die opvallen. Geen grijze mu...
- **Primary Substrate**: `#f4f4f4` (`var(--_global-vars---light)` in `:root`), **Primary Ink**: `#040404`, **Accent / Highlight**: `#3a39ff`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f4f4f4` (`var(--_global-vars---light)` in `:root`) paired with `#040404` primary typography and `#3a39ff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Vastagogrotesk` for display copy (`Omdat gewoon te gewoontjes is`) with `Arial` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(0.22,1,0.36,1)` easing and GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-brandlos-nl` in your global stylesheet:

:root {
  /* Brandlos · Het creatieve bureau van Limburg (www-brandlos-nl) — Ground-Truth Extracted CSS Variables */
  --w-backdrop-animation: initial; /* Motion / Easing Token (www-brandlos-nl) */
  --_global-vars---light: #f4f4f4; /* Canvas / Surface Token (www-brandlos-nl) */
  --_global-vars---dark: #040404; /* Canvas / Surface Token (www-brandlos-nl) */
  --_global-vars---accent-1: #fbd050; /* Brand / Palette Token (www-brandlos-nl) */
  --_global-vars---accent-2: #3a39ff; /* Brand / Palette Token (www-brandlos-nl) */
  --_global-vars---accent-5: #ff5b23; /* Brand / Palette Token (www-brandlos-nl) */
  --_global-vars---accent-3: #ade6ed; /* Brand / Palette Token (www-brandlos-nl) */
  --_global-vars---accent-4: #e9a2e4; /* Brand / Palette Token (www-brandlos-nl) */
  --_global-vars---grey: #b7b7b7; /* Color / Atmospheric Token (www-brandlos-nl) */
  --underline-scale: 1; /* Design System Custom Token (www-brandlos-nl) */
  --pt-color: #fbd050; /* Brand / Palette Token (www-brandlos-nl) */
  --swiper-theme-color: #007aff; /* Brand / Palette Token (www-brandlos-nl) */
  --swiper-preloader-color: #fff; /* Brand / Palette Token (www-brandlos-nl) */
  --swiper-navigation-size: 44px; /* Layout / Spatial Grid Token (www-brandlos-nl) */
  --www-brandlos-nl-bg: #f4f4f4; /* Canvas Substrate (from `var(--_global-vars---light)` in `:root`) (www-brandlos-nl) */
  --www-brandlos-nl-ink: #040404; /* Primary Typography Ink (stylesheet-derived) (www-brandlos-nl) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f4f4f4` — grounded in `var(--_global-vars---light)` in `:root`
- **Primary Typography Ink**: `#040404` — grounded in `var(--_global-vars---dark)` in `:root`
- **Elevated Surface / Card Substrate**: `#fbd050` — grounded in `var(--_global-vars---accent-1)` in `:root`
- **Interactive Accent / Highlight**: `#3a39ff` — grounded in `var(--_global-vars---accent-2)` in `:root`
- **Secondary / Muted Copy**: `#ff5b23` — grounded in `var(--_global-vars---accent-5)` in `:root`
- **Structural Hairline Border**: `#ade6ed` — grounded in `var(--_global-vars---accent-3)` in `:root`
- **Variable Token (`--_global-vars---accent-4`)**: `#e9a2e4` — grounded in `var(--_global-vars---accent-4)` in `:root`
- **Variable Token (`--_global-vars---grey`)**: `#b7b7b7` — grounded in `var(--_global-vars---grey)` in `:root`
- **Variable Token (`--swiper-theme-color`)**: `#007aff` — grounded in `var(--swiper-theme-color)` in stylesheet
- **Variable Token (`--swiper-preloader-color`)**: `#fff` — grounded in `var(--swiper-preloader-color)` in stylesheet

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×9524px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `www-brandlos-nl` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `15px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Vastagogrotesk`
- **Body Font Stack**: `Arial`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy Rule**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Index Rule**: rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-brandlos-nl` (`Brandlos · Het creatieve bureau van Limburg`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-brandlos-nl`)**:
   - DOM & Selectors: Landmark `<header class="w-mod-js">` hosting `Brandlos · Het creatieve bureau van ` navigation (`Toestemming · Details · [#IABV2SETTINGS#] · Over · Details tonen`), DOM attributes (`data-wf-domain="www.brandlos.nl"`, `data-wf-page="6a60a2741f0d39e46e0880df"`, `data-wf-site="6a60a2731f0d39e46e0880dc"`, `data-nosnippet`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.w-mod-js> — `www-brandlos-nl`)` (`www-brandlos-nl`) adapts across `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)` with `cubic-bezier(0.22,1,0.36,1)` transitions and links `Toestemming · Details · [#IABV2SETTINGS#] · Over · Details tonen`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `Omdat gewoon te gewoontjes is`)**:
   - DOM & Selectors: Landmark `<section class="home-hero">` presenting display lead `Omdat gewoon te gewoontjes is` and copy excerpt *"Toestemmingsselectie"* over `#f4f4f4` canvas and `#040404` ink.
   - Responsive Contract: Hero stage (`1440×9524px` desktop / `390×2400px` mobile) sets `#f4f4f4` background with `#040404` headline `Omdat gewoon te gewoontjes is`.
3. **Primary Showcase & Content Grid (<section.home-showreel> — `Kijk mam, dit hebben wij gemaakt`)**:
   - DOM & Selectors: Landmark `<section class="home-showreel">` rendering section `Kijk mam, dit hebben wij gemaakt` with copy *"Noodzakelijk 5 Noodzakelijke cookies helpen een website bruikbaar"*, asset references (`cdn.prod.website-files.com`, `brandlos-nl.webflow.shared.3ea0ad...`, `cc.js`, `configuration.js`), and grid rule `body { margin: 0; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.home-showreel> — `Kijk mam, dit hebben wij gemaakt`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.home-about> — `Strategisch sterk, grafisch verdom`)**:
   - DOM & Selectors: Landmark `<section class="home-about">` framing `Strategisch sterk, grafisch verdomd goed` and `Vrienden van Brandlos` (*"Cloudflare 1 Meer informatie over deze aanbieder cf.turnstile.u D"*) with `#fbd050` surface cards, `#3a39ff` accents, and `summary { display: block; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.home-about> — `Strategisch sterk, grafisch verdom`)` uses `3px`, `100%`, `50%`, `15px` radii, `#3a39ff` highlights, and assets (cdn.prod.website-files.com, brandlos-nl.webflow.shared.3ea0ad..., cc.js).
5. **Colophon & Global Directory Footer (<footer.CybotCookiebotDialogContentWrapper> — `https://www.brandlos.nl`)**:
   - DOM & Selectors: Landmark `<footer class="CybotCookiebotDialogContentWrapper">` anchoring `Brandlos · Het creatieve bureau ` footer links (`Toestemming · Details · [#IABV2SETTINGS#] · Over · Details tonen`), copy *"Meer informatie over deze aanbieder"*, and `#ade6ed` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.CybotCookiebotDialogContentWrapper> — `https://www.brandlos.nl`)` aligns to `940px` extracted from `www-brandlos-nl` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.brandlos.nl", data-wf-page="6a60a2741f0d39e46e0880df", data-wf-site="6a60a2731f0d39e46e0880dc").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Toestemmingsselectie"*
- Copy Excerpt 2: *"Noodzakelijk 5 Noodzakelijke cookies helpen een website bruikbaarder te maken, doo..."*
- Copy Excerpt 3: *"Cloudflare 1 Meer informatie over deze aanbieder cf.turnstile.u Deze cookie wordt..."*
- Copy Excerpt 4: *"Meer informatie over deze aanbieder"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.22,1,0.36,1)`
- **Extracted Stylesheet Rules (`www-brandlos-nl`)**:
- `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`
- `body { margin: 0; }`
- `summary { display: block; }`
- `video { vertical-align: baseline; display: inline-block; }`
- `template { display: none; }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-brandlos-nl` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-brandlos-nl` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-brandlos-nl` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,1,0.36,1)`)**: Governs interactive state transitions across `<header.w-mod-js>` and `<section.home-showreel>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-brandlos-nl`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
