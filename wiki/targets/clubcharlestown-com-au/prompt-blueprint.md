---
title: "UI Prompt Blueprint: clubcharlestown-com-au"
date: 2026-11-15
target: "[[overview|clubcharlestown-com-au]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#98A2B3` ink, `#344054` accent)"
---

# UI Design System & Master Generation Blueprint: clubcharlestown-com-au

> **Home · Club Charlestown** (https://clubcharlestown.com.au/) — We're a vibrant, family-friendly club where everyone belongs. Come in and discover a place to relax, have fun, and connect with friends a...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/clubcharlestown-com-au/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Home · Club Charlestown** (`https://clubcharlestown.com.au/`). We're a vibrant, family-friendly club where everyone belongs. Come in and discover a place to relax, have fun, and connect with friends a...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#98A2B3` ink, `#344054` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000000` (`var(--fieldset-color)` in `:root`) paired with `#98A2B3` primary typography and `#344054` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Roboto` for display copy (`Welcome to Club Charlestown`) with `gotham-xnarrow` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1024px` container bounds (`gap: var(--row-gap)`, padding `5px`) with `cubic-bezier(0.77,0,0.175,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/clubcharlestown-com-au/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1024px` extracted from `clubcharlestown-com-au` stylesheet.
- **Canvas Lateral Padding & Spacing**: `5px` lateral canvas padding with `var(--row-gap)` grid gap.
- **Border Radius Scale**: `var(--border-radius)`, `3px`, `2px`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1024px`, `gap: var(--row-gap)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `5px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:1024px)`, `@media (max-width:767px)`, `@media (min-width:-1)`, `@media (max-width:1366px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | `var(--fieldset-color)` in `:root` |
| **Primary Typography Ink** | `#444444` | `var(--title-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#98A2B3` | `var(--form-desc-color)` in `:root` |
| **Interactive Accent / Highlight** | `#344054` | `var(--label-color)` in `:root` |
| **Secondary / Muted Copy** | `#F04438` | `var(--required-color)` in `:root` |
| **Structural Hairline Border** | `#667085` | `var(--description-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--direction-multiplier` | `1` | Design System Custom Token |
| `--flex-direction` | `initial` | Design System Custom Token |
| `--flex-wrap` | `initial` | Layout / Spatial Grid Token |
| `--justify-content` | `initial` | Design System Custom Token |
| `--align-items` | `initial` | Design System Custom Token |
| `--align-content` | `initial` | Design System Custom Token |
| `--gap` | `initial` | Layout / Spatial Grid Token |
| `--flex-basis` | `initial` | Design System Custom Token |
| `--flex-grow` | `initial` | Design System Custom Token |
| `--flex-shrink` | `initial` | Typography Ink Token |
| `--order` | `initial` | Design System Custom Token |
| `--align-self` | `initial` | Design System Custom Token |
| `--page-title-display` | `block` | Design System Custom Token |
| `--border-radius` | `0` | Elevation / Border Token |
| `--border-top-width` | `0px` | Layout / Spatial Grid Token |
| `--border-right-width` | `0px` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Roboto`.
- **Primary Body Stack**: `gotham-xnarrow`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`, `--n-menu-wrapper-display: flex`.
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2.5em`, `100px`, `15px`, `13px`, `16px`).
- **Body Copy**: rule `p` (`font-size: var(--form-desc-size)`).
- **Metadata & Navigation Labels**: CSS variables `--label-color: #344054`, `--label-padding: 0px 0px 5px 0px`, `--check-label-color: #1D2939`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.77,0,0.175,1)`, `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.2,0,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `entor .elementor-background-video...`**: `transition: opacity 1s` extracted from `clubcharlestown-com-au` stylesheet.
- **Selector `.elementor-custom-embed-play svg`**: `transition: all .5s` extracted from `clubcharlestown-com-au` stylesheet.
- **Selector `.elementor-ken-burns`**: `transition: 10s` extracted from `clubcharlestown-com-au` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.77,0,0.175,1)`)**: Governs interactive state transitions across `<header.elementor>` and `<main.site-main>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Home · Club Charlestown                    │
│ ====================================================================== │
│ [ <header.elementor>       | What's On What's On · What's On · Func ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.site-main>                                     |   │
│ | H1: Welcome to Club Charlestown                                  |   │
│ | Substrate: #000000    | Ink: #98A2B3    | Accent: #344054        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.site-main>          ) max-w: 1024px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Beyond a Club, It's a Commun |  | Club Lambton                 | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.elementor>] -> [<main.site-main>] -> [<main.site-main>] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.elementor>    ) | https://clubcharlestown.com.au/    │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.elementor> — `clubcharlestown-com-au`)**:
   - Landmark `<header class="elementor elementor-27">` hosting `Home · Club Charlestown` navigation (`What's On What's On · What's On · Functions · Courtesy Bus · Bowls Bowls`), DOM attributes (`data-elementor-device-mode="desktop"`, `data-elementor-type="header"`, `data-elementor-id="27"`, `data-elementor-post-type="elementor_library"`), and stylesheet rule `.tk-gotham-xnarrow { font-family: "gotham-xnarrow",sans-serif; }`.
2. **Hero Stage & Focal Lead (<main.site-main> — `Welcome to Club Charlestown`)**:
   - Landmark `<main class="site-main post-7">` presenting display lead `Welcome to Club Charlestown` and copy excerpt *"Club Lambton Venue Club Lambton Venue"* over `#000000` canvas and `#98A2B3` ink.
3. **Primary Showcase & Content Grid (<main.site-main> — `Beyond a Club, It's a Community`)**:
   - Landmark `<main class="site-main post-7">` rendering section `Beyond a Club, It's a Community` with copy *"Club Lambton Venue"*, asset references (`recaptcha__en.js`, `www.googletagmanager.com`, `embed`, `ckx4srt.css`), and grid rule `.tk-gotham-narrow { font-family: "gotham-narrow",sans-serif; }`.
4. **Interactive Detail & Feature Matrix (<main.site-main> — `Club Lambton`)**:
   - Landmark `<main class="site-main post-7">` framing `Club Lambton` and `Where Locals Meet` (*"Drink & Dine Drink & Dine"*) with `#98A2B3` surface cards, `#344054` accents, and `.tk-gotham-condensed { font-family: "gotham-condensed",sans-serif; }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://clubcharlestown.com.au/`)**:
   - Landmark `<footer class="elementor elementor-63">` anchoring `Home · Club Charlestown` footer links (`What's On What's On · What's On · Functions · Courtesy Bus · Bowls Bowls`), copy *"Memberships Memberships"*, and `#667085` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: clubcharlestown-com-au (Home · Club Charlestown)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `clubcharlestown-com-au` (**Home · Club Charlestown** — `https://clubcharlestown.com.au/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#98A2B3` ink, `#344054` accent).
- **Identity & Domain Context**: We're a vibrant, family-friendly club where everyone belongs. Come in and discover a place to relax, have fun, and connect with friends a...
- **Primary Substrate**: `#000000` (`var(--fieldset-color)` in `:root`), **Primary Ink**: `#98A2B3`, **Accent / Highlight**: `#344054`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000000` (`var(--fieldset-color)` in `:root`) paired with `#98A2B3` primary typography and `#344054` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Roboto` for display copy (`Welcome to Club Charlestown`) with `gotham-xnarrow` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1024px` container bounds (`gap: var(--row-gap)`, padding `5px`) with `cubic-bezier(0.77,0,0.175,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `clubcharlestown-com-au` in your global stylesheet:

:root {
  /* Home · Club Charlestown (clubcharlestown-com-au) — Ground-Truth Extracted CSS Variables */
  --direction-multiplier: 1; /* Design System Custom Token (clubcharlestown-com-au) */
  --flex-direction: initial; /* Design System Custom Token (clubcharlestown-com-au) */
  --flex-wrap: initial; /* Layout / Spatial Grid Token (clubcharlestown-com-au) */
  --justify-content: initial; /* Design System Custom Token (clubcharlestown-com-au) */
  --align-items: initial; /* Design System Custom Token (clubcharlestown-com-au) */
  --align-content: initial; /* Design System Custom Token (clubcharlestown-com-au) */
  --gap: initial; /* Layout / Spatial Grid Token (clubcharlestown-com-au) */
  --flex-basis: initial; /* Design System Custom Token (clubcharlestown-com-au) */
  --flex-grow: initial; /* Design System Custom Token (clubcharlestown-com-au) */
  --flex-shrink: initial; /* Typography Ink Token (clubcharlestown-com-au) */
  --order: initial; /* Design System Custom Token (clubcharlestown-com-au) */
  --align-self: initial; /* Design System Custom Token (clubcharlestown-com-au) */
  --page-title-display: block; /* Design System Custom Token (clubcharlestown-com-au) */
  --border-radius: 0; /* Elevation / Border Token (clubcharlestown-com-au) */
  --border-top-width: 0px; /* Layout / Spatial Grid Token (clubcharlestown-com-au) */
  --border-right-width: 0px; /* Layout / Spatial Grid Token (clubcharlestown-com-au) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in `var(--fieldset-color)` in `:root`
- **Primary Typography Ink**: `#444444` — grounded in `var(--title-color)` in `:root`
- **Elevated Surface / Card Substrate**: `#98A2B3` — grounded in `var(--form-desc-color)` in `:root`
- **Interactive Accent / Highlight**: `#344054` — grounded in `var(--label-color)` in `:root`
- **Secondary / Muted Copy**: `#F04438` — grounded in `var(--required-color)` in `:root`
- **Structural Hairline Border**: `#667085` — grounded in `var(--description-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1024px` extracted from `clubcharlestown-com-au` stylesheet
- **Padding & Gutters**: `5px` lateral canvas padding with `var(--row-gap)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1024px`, `gap: var(--row-gap)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `5px` horizontal padding
- **Media Queries**: `@media (max-width:1024px)`, `@media (max-width:767px)`, `@media (min-width:-1)`, `@media (max-width:1366px)`
- **Corner Radii**: `var(--border-radius)`, `3px`, `2px`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Roboto`
- **Body Font Stack**: `gotham-xnarrow`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--page-title-display: block`, `--display: flex`, `--n-menu-wrapper-display: flex`
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2.5em`, `100px`, `15px`, `13px`, `16px`)
- **Body Copy Rule**: rule `p` (`font-size: var(--form-desc-size)`)
- **Metadata & Index Rule**: CSS variables `--label-color: #344054`, `--label-padding: 0px 0px 5px 0px`, `--check-label-color: #000000`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `clubcharlestown-com-au` (`Home · Club Charlestown`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.elementor> — `clubcharlestown-com-au`)**:
   - DOM & Selectors: Landmark `<header class="elementor elementor-27">` hosting `Home · Club Charlestown` navigation (`What's On What's On · What's On · Functions · Courtesy Bus · Bowls Bowls`), DOM attributes (`data-elementor-device-mode="desktop"`, `data-elementor-type="header"`, `data-elementor-id="27"`, `data-elementor-post-type="elementor_library"`), and stylesheet rule `.tk-gotham-xnarrow { font-family: "gotham-xnarrow",sans-serif; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.elementor> — `clubcharlestown-com-au`)` (`clubcharlestown-com-au`) adapts across `@media (max-width:1024px)`, `@media (max-width:767px)`, `@media (min-width:-1)`, `@media (max-width:1366px)` with `cubic-bezier(0.77,0,0.175,1)`, `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.2,0,0,1)` transitions and links `What's On What's On · What's On · Functions · Courtesy Bus · Bowls Bowls`.
2. **Hero Stage & Focal Lead (<main.site-main> — `Welcome to Club Charlestown`)**:
   - DOM & Selectors: Landmark `<main class="site-main post-7">` presenting display lead `Welcome to Club Charlestown` and copy excerpt *"Club Lambton Venue Club Lambton Venue"* over `#000000` canvas and `#98A2B3` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000000` background with `#98A2B3` headline `Welcome to Club Charlestown`.
3. **Primary Showcase & Content Grid (<main.site-main> — `Beyond a Club, It's a Community`)**:
   - DOM & Selectors: Landmark `<main class="site-main post-7">` rendering section `Beyond a Club, It's a Community` with copy *"Club Lambton Venue"*, asset references (`recaptcha__en.js`, `www.googletagmanager.com`, `embed`, `ckx4srt.css`), and grid rule `.tk-gotham-narrow { font-family: "gotham-narrow",sans-serif; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.site-main> — `Beyond a Club, It's a Community`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1024px`, `gap: var(--row-gap)`) on desktop and Single-column vertical stack at `390px` viewport width with `5px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.site-main> — `Club Lambton`)**:
   - DOM & Selectors: Landmark `<main class="site-main post-7">` framing `Club Lambton` and `Where Locals Meet` (*"Drink & Dine Drink & Dine"*) with `#98A2B3` surface cards, `#344054` accents, and `.tk-gotham-condensed { font-family: "gotham-condensed",sans-serif; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.site-main> — `Club Lambton`)` uses `var(--border-radius)`, `3px`, `2px`, `4px` radii, `#344054` highlights, and assets (recaptcha__en.js, www.googletagmanager.com, embed).
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://clubcharlestown.com.au/`)**:
   - DOM & Selectors: Landmark `<footer class="elementor elementor-63">` anchoring `Home · Club Charlestown` footer links (`What's On What's On · What's On · Functions · Courtesy Bus · Bowls Bowls`), copy *"Memberships Memberships"*, and `#667085` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.elementor> — `https://clubcharlestown.com.au/`)` aligns to `1024px` extracted from `clubcharlestown-com-au` stylesheet with `5px` lateral canvas padding with `var(--row-gap)` grid gap and attributes (data-elementor-device-mode="desktop", data-elementor-type="header", data-elementor-id="27").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Club Lambton Venue Club Lambton Venue"*
- Copy Excerpt 2: *"Club Lambton Venue"*
- Copy Excerpt 3: *"Drink & Dine Drink & Dine"*
- Copy Excerpt 4: *"Memberships Memberships"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.77,0,0.175,1)`, `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.2,0,0,1)`
- **Extracted Stylesheet Rules (`clubcharlestown-com-au`)**:
- `.tk-gotham-xnarrow { font-family: "gotham-xnarrow",sans-serif; }`
- `.tk-gotham-narrow { font-family: "gotham-narrow",sans-serif; }`
- `.tk-gotham-condensed { font-family: "gotham-condensed",sans-serif; }`
- `.tk-gotham { font-family: "gotham",sans-serif; }`
- `root { --direction-multiplier:1 }`
- **Per-Selector Transition Rules**:
- **Selector `entor .elementor-background-video...`**: `transition: opacity 1s` extracted from `clubcharlestown-com-au` stylesheet.
- **Selector `.elementor-custom-embed-play svg`**: `transition: all .5s` extracted from `clubcharlestown-com-au` stylesheet.
- **Selector `.elementor-ken-burns`**: `transition: 10s` extracted from `clubcharlestown-com-au` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.77,0,0.175,1)`)**: Governs interactive state transitions across `<header.elementor>` and `<main.site-main>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `clubcharlestown-com-au`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
