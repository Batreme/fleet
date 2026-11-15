---
title: "UI Prompt Blueprint: b3xgraphics-com"
date: 2026-11-15
target: "[[overview|b3xgraphics-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#04b5ff` canvas, `#a00` ink, `#008a20` accent)"
---

# UI Design System & Master Generation Blueprint: b3xgraphics-com

> **B3X Graphics · Freelance Sports Art Director & Designer** (https://b3xgraphics.com/) — B3X Graphics: freelance art direction and design specialising in sport. Branding, campaign design and socials content for some of the big...

![Desktop Viewport Capture (1440x5914)](file:///root/projects/fleet/wiki/targets/b3xgraphics-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **B3X Graphics · Freelance Sports Art Director & Designer** (`https://b3xgraphics.com/`). B3X Graphics: freelance art direction and design specialising in sport. Branding, campaign design and socials content for some of the big...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#04b5ff` canvas, `#a00` ink, `#008a20` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#04b5ff` (`var(--b3xh-sky)` in `:root`) paired with `#a00` primary typography and `#008a20` accents.
  - **Extracted Typographic Hierarchy**: Pairs `B3XH Aileron` for display copy (`B3X Graphics Studio`) with `B3XH FA` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `var(--b3xh-max)` container bounds (`gap: 50px`, padding `12px`) with `cubic-bezier(.16,1,.3,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/b3xgraphics-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×5914px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `var(--b3xh-max)` extracted from `b3xgraphics-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `12px` lateral canvas padding with `50px` grid gap.
- **Border Radius Scale**: `26px`, `100px`, `22px`, `16px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--b3xh-max)`, `gap: 50px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `12px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:768px)`, `@media (max-width:1366px) and (min-width:768px)`, `@media (max-width:1024px) and (min-width:768px)`, `@media (max-width:1024px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#04b5ff` | `var(--b3xh-sky)` in `:root` |
| **Primary Typography Ink** | `#03b2cb` | `var(--PhoneInput-color--focus)` in `:root` |
| **Elevated Surface / Card Substrate** | `#720eec` | `var(--woocommerce)` in `:root` |
| **Interactive Accent / Highlight** | `#008a20` | `var(--wc-green)` in `:root` |
| **Secondary / Muted Copy** | `#a00` | `var(--wc-red)` in `:root` |
| **Structural Hairline Border** | `#ffba00` | `var(--wc-orange)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--b3xh-side` | `clamp(20px,2.2vw,50px)` | Dimension / Scale Token |
| `--b3xh-max` | `1820px` | Dimension / Scale Token |
| `--b3xh-sky` | `#04b5ff` | Color / Atmospheric Token |
| `--b3xh-glass` | `linear-gradient(155deg,rgba(9,26,54,0.66) 0%,rgba(3,13,30,0.74) 100%)` | Color / Atmospheric Token |
| `--PhoneInput-color--focus` | `#03b2cb` | Brand / Palette Token |
| `--PhoneInputInternationalIconPhone-opacity` | `0.8` | Canvas / Surface Token |
| `--PhoneInputInternationalIconGlobe-opacity` | `0.65` | Canvas / Surface Token |
| `--PhoneInputCountrySelect-marginRight` | `0.35em` | Layout / Spatial Grid Token |
| `--PhoneInputCountrySelectArrow-width` | `0.3em` | Brand / Palette Token |
| `--PhoneInputCountrySelectArrow-marginLeft` | `var(--PhoneInputCountrySelect-marginRight)` | Brand / Palette Token |
| `--PhoneInputCountrySelectArrow-borderWidth` | `1px` | Brand / Palette Token |
| `--PhoneInputCountrySelectArrow-opacity` | `0.45` | Brand / Palette Token |
| `--PhoneInputCountrySelectArrow-color` | `currentColor` | Brand / Palette Token |
| `--PhoneInputCountrySelectArrow-color--focus` | `var(--PhoneInput-color--focus)` | Brand / Palette Token |
| `--PhoneInputCountrySelectArrow-transform` | `rotate(45deg)` | Brand / Palette Token |
| `--PhoneInputCountryFlag-aspectRatio` | `1.5` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `B3XH Aileron`.
- **Primary Body Stack**: `B3XH FA`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`, `--cc-font-display: 'Palma Heavy', sans-serif`; rule `h1` (`font-size: 2.5rem`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2rem`).
- **Body Copy**: CSS variables `--cc-font-body: 'Aileron', sans-serif`; rule `body` (`font-size: 1rem`, `line-height: 1.5`, `font-weight: 400`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `1rem`, `13px`, `12px`, `14.6px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.45,0,.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.b3xh .b3xh-bar`**: `transition: left .45s cubic-bezier(.16,1,.3,1),right .45s cubic-bezier(.16...` extracted from `b3xgraphics-com` stylesheet.
- **Selector `.b3xh .b3xh-burger`**: `transition: .4s` extracted from `b3xgraphics-com` stylesheet.
- **Selector `.b3xh .b3xh-lines`**: `transition: all .4s ease` extracted from `b3xgraphics-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.b3xh-bar>` and `<section.b3xt>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — B3X Graphics · Freelance Sports Art Direct │
│ ====================================================================== │
│ [ <header.b3xh-bar>        | Home · Projects · The Lab · About · Sh ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.b3xr-feat>                                  |   │
│ | H1: B3X Graphics Studio                                          |   │
│ | Substrate: #04b5ff    | Ink: #a00       | Accent: #008a20        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.b3xt>            ) max-w: var(--b3xh-max |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Freelance Art Director & Des |  | Featured projects            | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 50px  ) | │
│ | [<header.b3xh-bar>] -> [<section.b3xr-feat] -> [<section.b3xt>] |    │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | https://b3xgraphics.com/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.b3xh-bar> — `b3xgraphics-com`)**:
   - Landmark `<header class="b3xh-bar">` hosting `B3X Graphics · Freelance Sports Art ` navigation (`Home · Projects · The Lab · About · Shop`), DOM attributes (`data-b3xh-page="home"`, `data-b3xh-bound="1"`, `data-elementor-type="wp-page"`, `data-elementor-id="1301"`), and stylesheet rule `after { box-sizing:border-box; }`.
2. **Hero Stage & Focal Lead (<section.b3xr-feat> — `B3X Graphics Studio`)**:
   - Landmark `<section class="b3xr-feat">` presenting display lead `B3X Graphics Studio` and copy excerpt *"Available for new projects"* over `#04b5ff` canvas and `#a00` ink.
3. **Primary Showcase & Content Grid (<section.b3xt> — `Freelance Art Director & Designer`)**:
   - Landmark `<section class="b3xt b3xt-armed">` rendering section `Freelance Art Director & Designer` with copy *"I work with some of the biggest brands in sport"*, asset references (`favicon.svg`, `chrome.css`, `chrome.js`, `fonts.css`), and grid rule `.b3xh .b3xh-defs { position:absolute;width:0;height:0;overflow:hidden;pointer-events:none; }`.
4. **Interactive Detail & Feature Matrix (<section.b3xt> — `Featured projects`)**:
   - Landmark `<section class="b3xt b3xt-armed">` framing `Featured projects` and `2025/26 WSL Champions` (*"2025/26 WSL Champions Social Media"*) with `#720eec` surface cards, `#008a20` accents, and `.b3xh .b3xh-burger:active { background:transparent;color:fff;border:0; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://b3xgraphics.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `B3X Graphics · Freelance Sports ` footer links (`Home · Projects · The Lab · About · Shop`), copy *"Spurs 1901 Anniversary Social Media"*, and `#ffba00` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: b3xgraphics-com (B3X Graphics · Freelance Sports Art Director & Designer)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `b3xgraphics-com` (**B3X Graphics · Freelance Sports Art Director & Designer** — `https://b3xgraphics.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#04b5ff` canvas, `#a00` ink, `#008a20` accent).
- **Identity & Domain Context**: B3X Graphics: freelance art direction and design specialising in sport. Branding, campaign design and socials content for some of the big...
- **Primary Substrate**: `#04b5ff` (`var(--b3xh-sky)` in `:root`), **Primary Ink**: `#a00`, **Accent / Highlight**: `#008a20`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#04b5ff` (`var(--b3xh-sky)` in `:root`) paired with `#a00` primary typography and `#008a20` accents.
  - **Extracted Typographic Hierarchy**: Pairs `B3XH Aileron` for display copy (`B3X Graphics Studio`) with `B3XH FA` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `var(--b3xh-max)` container bounds (`gap: 50px`, padding `12px`) with `cubic-bezier(.16,1,.3,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `b3xgraphics-com` in your global stylesheet:

:root {
  /* B3X Graphics · Freelance Sports Art Director & Designer (b3xgraphics-com) — Ground-Truth Extracted CSS Variables */
  --b3xh-side: clamp(20px,2.2vw,50px); /* Dimension / Scale Token (b3xgraphics-com) */
  --b3xh-max: 1820px; /* Dimension / Scale Token (b3xgraphics-com) */
  --b3xh-sky: #04b5ff; /* Color / Atmospheric Token (b3xgraphics-com) */
  --b3xh-glass: linear-gradient(155deg,rgba(9,26,54,0.66) 0%,rgba(3,13,30,0.74) 100%); /* Color / Atmospheric Token (b3xgraphics-com) */
  --PhoneInput-color--focus: #03b2cb; /* Brand / Palette Token (b3xgraphics-com) */
  --PhoneInputInternationalIconPhone-opacity: 0.8; /* Canvas / Surface Token (b3xgraphics-com) */
  --PhoneInputInternationalIconGlobe-opacity: 0.65; /* Canvas / Surface Token (b3xgraphics-com) */
  --PhoneInputCountrySelect-marginRight: 0.35em; /* Layout / Spatial Grid Token (b3xgraphics-com) */
  --PhoneInputCountrySelectArrow-width: 0.3em; /* Brand / Palette Token (b3xgraphics-com) */
  --PhoneInputCountrySelectArrow-marginLeft: var(--PhoneInputCountrySelect-marginRight); /* Brand / Palette Token (b3xgraphics-com) */
  --PhoneInputCountrySelectArrow-borderWidth: 1px; /* Brand / Palette Token (b3xgraphics-com) */
  --PhoneInputCountrySelectArrow-opacity: 0.45; /* Brand / Palette Token (b3xgraphics-com) */
  --PhoneInputCountrySelectArrow-color: currentColor; /* Brand / Palette Token (b3xgraphics-com) */
  --PhoneInputCountrySelectArrow-color--focus: var(--PhoneInput-color--focus); /* Brand / Palette Token (b3xgraphics-com) */
  --PhoneInputCountrySelectArrow-transform: rotate(45deg); /* Brand / Palette Token (b3xgraphics-com) */
  --PhoneInputCountryFlag-aspectRatio: 1.5; /* Design System Custom Token (b3xgraphics-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#04b5ff` — grounded in `var(--b3xh-sky)` in `:root`
- **Primary Typography Ink**: `#03b2cb` — grounded in `var(--PhoneInput-color--focus)` in `:root`
- **Elevated Surface / Card Substrate**: `#720eec` — grounded in `var(--woocommerce)` in `:root`
- **Interactive Accent / Highlight**: `#008a20` — grounded in `var(--wc-green)` in `:root`
- **Secondary / Muted Copy**: `#a00` — grounded in `var(--wc-red)` in `:root`
- **Structural Hairline Border**: `#ffba00` — grounded in `var(--wc-orange)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×5914px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `var(--b3xh-max)` extracted from `b3xgraphics-com` stylesheet
- **Padding & Gutters**: `12px` lateral canvas padding with `50px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--b3xh-max)`, `gap: 50px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `12px` horizontal padding
- **Media Queries**: `@media (min-width:768px)`, `@media (max-width:1366px) and (min-width:768px)`, `@media (max-width:1024px) and (min-width:768px)`, `@media (max-width:1024px)`
- **Corner Radii**: `26px`, `100px`, `22px`, `16px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `B3XH Aileron`
- **Body Font Stack**: `B3XH FA`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--page-title-display: block`, `--display: flex`, `--cc-font-display: 'Palma Heavy', sans-serif`; rule `h1` (`font-size: 2.5rem`)
- **H2 Section Rule**: rule `h2` (`font-size: 2rem`)
- **Body Copy Rule**: CSS variables `--cc-font-body: 'Aileron', sans-serif`; rule `body` (`font-size: 1rem`, `line-height: 1.5`, `font-weight: 400`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `1rem`, `13px`, `12px`, `14.6px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `b3xgraphics-com` (`B3X Graphics · Freelance Sports Art Director & Designer`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.b3xh-bar> — `b3xgraphics-com`)**:
   - DOM & Selectors: Landmark `<header class="b3xh-bar">` hosting `B3X Graphics · Freelance Sports Art ` navigation (`Home · Projects · The Lab · About · Shop`), DOM attributes (`data-b3xh-page="home"`, `data-b3xh-bound="1"`, `data-elementor-type="wp-page"`, `data-elementor-id="1301"`), and stylesheet rule `after { box-sizing:border-box; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.b3xh-bar> — `b3xgraphics-com`)` (`b3xgraphics-com`) adapts across `@media (min-width:768px)`, `@media (max-width:1366px) and (min-width:768px)`, `@media (max-width:1024px) and (min-width:768px)`, `@media (max-width:1024px)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.45,0,.25,1)` transitions and links `Home · Projects · The Lab · About · Shop`.
2. **Hero Stage & Focal Lead (<section.b3xr-feat> — `B3X Graphics Studio`)**:
   - DOM & Selectors: Landmark `<section class="b3xr-feat">` presenting display lead `B3X Graphics Studio` and copy excerpt *"Available for new projects"* over `#04b5ff` canvas and `#a00` ink.
   - Responsive Contract: Hero stage (`1440×5914px` desktop / `390×2400px` mobile) sets `#04b5ff` background with `#a00` headline `B3X Graphics Studio`.
3. **Primary Showcase & Content Grid (<section.b3xt> — `Freelance Art Director & Designer`)**:
   - DOM & Selectors: Landmark `<section class="b3xt b3xt-armed">` rendering section `Freelance Art Director & Designer` with copy *"I work with some of the biggest brands in sport"*, asset references (`favicon.svg`, `chrome.css`, `chrome.js`, `fonts.css`), and grid rule `.b3xh .b3xh-defs { position:absolute;width:0;height:0;overflow:hidden;pointer-events:none; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.b3xt> — `Freelance Art Director & Designer`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--b3xh-max)`, `gap: 50px`) on desktop and Single-column vertical stack at `390px` viewport width with `12px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.b3xt> — `Featured projects`)**:
   - DOM & Selectors: Landmark `<section class="b3xt b3xt-armed">` framing `Featured projects` and `2025/26 WSL Champions` (*"2025/26 WSL Champions Social Media"*) with `#720eec` surface cards, `#008a20` accents, and `.b3xh .b3xh-burger:active { background:transparent;color:fff;border:0; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.b3xt> — `Featured projects`)` uses `26px`, `100px`, `22px`, `16px` radii, `#008a20` highlights, and assets (favicon.svg, chrome.css, chrome.js).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://b3xgraphics.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `B3X Graphics · Freelance Sports ` footer links (`Home · Projects · The Lab · About · Shop`), copy *"Spurs 1901 Anniversary Social Media"*, and `#ffba00` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://b3xgraphics.com/`)` aligns to `var(--b3xh-max)` extracted from `b3xgraphics-com` stylesheet with `12px` lateral canvas padding with `50px` grid gap and attributes (data-b3xh-page="home", data-b3xh-bound="1", data-elementor-type="wp-page").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Available for new projects"*
- Copy Excerpt 2: *"I work with some of the biggest brands in sport"*
- Copy Excerpt 3: *"2025/26 WSL Champions Social Media"*
- Copy Excerpt 4: *"Spurs 1901 Anniversary Social Media"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.45,0,.25,1)`
- **Extracted Stylesheet Rules (`b3xgraphics-com`)**:
- `after { box-sizing:border-box; }`
- `.b3xh .b3xh-defs { position:absolute;width:0;height:0;overflow:hidden;pointer-events:none; }`
- `.b3xh .b3xh-burger:active { background:transparent;color:fff;border:0; }`
- `.b3xh.is-open .b3xh-lines::before { top:0;transform:rotate(45deg); }`
- `.b3xh.is-open .b3xh-lines::after { top:0;transform:rotate(-45deg); }`
- **Per-Selector Transition Rules**:
- **Selector `.b3xh .b3xh-bar`**: `transition: left .45s cubic-bezier(.16,1,.3,1),right .45s cubic-bezier(.16...` extracted from `b3xgraphics-com` stylesheet.
- **Selector `.b3xh .b3xh-burger`**: `transition: .4s` extracted from `b3xgraphics-com` stylesheet.
- **Selector `.b3xh .b3xh-lines`**: `transition: all .4s ease` extracted from `b3xgraphics-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.b3xh-bar>` and `<section.b3xt>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `b3xgraphics-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
