---
title: "UI Prompt Blueprint: www-plugandplaydesign-co-uk"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-plugandplaydesign-co-uk"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 2
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#fafafa` canvas, `#080808` ink, `#808080` accent)"
---

# UI Design System & Master Generation Blueprint: www-plugandplaydesign-co-uk

> **Web Design Agency London & Guildford · Plug & Play** (https://www.plugandplaydesign.co.uk/) — Award-winning web design agency in London and Guildford. High-performance websites and digital retainers that drive measurable growth.

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Web Design Agency London & Guildford · Plug & Play** (`https://www.plugandplaydesign.co.uk/`). Award-winning web design agency in London and Guildford. High-performance websites and digital retainers that drive measurable growth.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fafafa` canvas, `#080808` ink, `#808080` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#fafafa` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#080808` primary typography and `#808080` accents.
  - **Grounded Typographic Hierarchy**: Uses `Geist` across display (`Web Design Agency in London and Surr`) and body copy, paired with `Geist Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1328px` container bounds (`gap: 8px`, padding `48px`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=14400px` / doc `17101px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1328px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `48px` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `3.35544e+07px`, `.25rem`, `var(--radius-cursor-tooltip)`, `var(--radius-full)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1328px`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `48px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:67.5rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fafafa` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#080808` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.bg-white { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#808080` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#808080` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#808080` | hairline divider derived from live computed `p` `color` (`computed_styles.json`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--page-margin` | `1rem` | Layout / Spatial Grid Token |
| `--content-width` | `calc(100vw - 2rem)` | Layout / Spatial Grid Token |
| `--spacing-scrolling-copy` | `calc((var(--scrolling-items-width) - 2.5rem) * 6 / 10)` | Typography Ink Token |
| `--spacing-scrolling-media` | `calc((var(--scrolling-items-width) - 2.5rem) * 4 / 10)` | Layout / Spatial Grid Token |
| `--spacing-scrolling-media-adjacent` | `calc((var(--scrolling-items-width) - 2.5rem) * 4.5 / 10)` | Layout / Spatial Grid Token |
| `--spacing-scrolling-expanded` | `calc((var(--scrolling-items-width) - 2.5rem) * 5.5 / 10)` | Layout / Spatial Grid Token |
| `--background` | `var(--color-grey-50)` | Canvas / Surface Token |
| `--background-secondary` | `var(--color-grey-100)` | Canvas / Surface Token |
| `--background-tertiary` | `var(--color-grey-200)` | Canvas / Surface Token |
| `--background-raised` | `var(--color-white)` | Canvas / Surface Token |
| `--background-glass` | `#fafafa01` | Canvas / Surface Token |
| `--foreground` | `var(--color-grey-950)` | Typography Ink Token |
| `--foreground-secondary` | `var(--color-grey-700)` | Typography Ink Token |
| `--foreground-tertiary` | `var(--color-grey-500)` | Typography Ink Token |
| `--foreground-inactive` | `var(--color-grey-400)` | Typography Ink Token |
| `--foreground-muted` | `var(--color-grey-600)` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Geist`.
- **Primary Body Stack**: `Geist`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 14px`, `line-height: 19.6px`, `font-weight: 400`, `letter-spacing: -0.28px`); rule `h1` (`font-size: var(--text-body-sm)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 32px`, `line-height: 38.4px`, `font-weight: 400`, `letter-spacing: -0.64px`); rule `h2` (`font-size: var(--text-body-sm)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-body-sm: .875rem`, `--text-body-sm--line-height: 1.4`, `--text-body-sm--letter-spacing: -.02em`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: "Geist Mono",ui-monospace,"SF Mono",Menlo,monospace`, `--default-mono-font-family: var(--font-mono)`, `--text-caption: .75rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.7,.2,.18,.85)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-plugandplaydesign-co-uk` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-plugandplaydesign-co-uk` stylesheet.
- **Selector `opacity\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-plugandplaydesign-co-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.inset-x-0>` and `<section.bg-background>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `17101px`, deepest scrollY reached `14400px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Nav / Drawer Probe (`Services`)**: Triggered visual change (pixel diff `65.17`, captured in `assets/state-nav.webp`); revealed links: Book a 30 min intro call, Our Work, Insights, About Us, Contact us, Visit CookieYes website.
- **Hover Physics (`primary_cta` · `Our Work`)**: Computed transition `0.2s` / `cubic-bezier(0, 0, 0.2, 1)` (no static color/transform shift captured at rest).
- **Interactive Control Probe (`accordion` · `Senior expertise, from brief to b...`)**: Triggered visual diff `14.099` (attr `false -> true`, captured in `assets/state-interactive.webp`).
- **Route Transition Architecture**: First internal navigation (`/work/chambers/`) measured as `direct` in `887ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Web Design Agency London & Guildford · Plu │
│ ====================================================================== │
│ [ <header.inset-x-0> (1440x60px)      | Web Design · Branding · Digi ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.px-page> (w=1440px)                           | │
│ | H1: Web Design Agency in London and Surrey                         | │
│ | Substrate: #fafafa | Ink: #080808 | Accent: #808080                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.bg-background>) max-w: 1328px              | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Web Design Agency            |  | Websites that drive results, | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.w-screen>) — Critical thinking. Cr         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bg-backgroun) | https://www.plugandplaydesign.co.uk  │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.inset-x-0>      ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.px-page>) — 390px Vertical Lead               | │
│ | H1: Web Design Agency in London and Surrey                         | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.bg-background) — 1-Col Stack              | │
│ | [ Item 1: Web Design Agency                                      ] | │
│ | [ Item 2: Websites that drive results, digital retainers th...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.w-screen>) — 1-Col (Critical thinking.)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bg-backgroun) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `www-plugandplaydesign-co-uk`)**:
   - Landmark `<header class="inset-x-0 z-40">` (`1440x60px`) hosting `Web Design Agency London & Guildford` navigation (`Web Design · Branding · Digital Marketing · UX / UI Design · eCommerce`), DOM attributes (`data-hero-enter`, `data-precedence="next"`, `data-precedence="next"`, `data-domain="plugandplaydesign.co.uk"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.px-page> — `Web Design Agency in London and Su`)**:
   - Landmark `<section class="px-page pt-section">` presenting display lead `Web Design Agency in London and Surrey` and copy excerpt *"Plug and Play is a creative web design agency based in Guildford,"* over `#fafafa` canvas and `#080808` ink.
3. **Primary Showcase & Content Grid (<section.bg-background> — `Web Design Agency`)**:
   - Landmark `<section class="bg-background px-page">` rendering section `Web Design Agency` with copy *"Websites that drive results,"*, asset references (`ca4cfa437ae45d18.css`, `dd5d352a082118c1.css`, `webpack-43624c9fe997cbf4.js`, `cf303062-0b72e54636065547.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.w-screen> — `Websites that drive results, digit`)**:
   - Landmark `<section class="w-screen">` framing `Websites that drive results, digital retainers th...` and `Critical thinking. Creativity. Innovation.` (*"digital retainers that deliver growth."*) with `#ffffff` surface cards, `#808080` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.bg-background> — `https://www.plugandplaydesign.co.uk/`)**:
   - Landmark `<footer class="bg-background px-page">` anchoring `Web Design Agency London & Guild` footer links (`Web Design · Branding · Digital Marketing · UX / UI Design · eCommerce`), copy *"Trusted by ambitious organisations across every major sector"*, and `#808080` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Web Design Agency` · sticky/fixed elements: `2`
- **Step 02** (`y=850px`, `5%`): Active landmark `Section @ 5%` · sticky/fixed elements: `2`
- **Step 03** (`y=3400px`, `21%`): Active landmark `Critical thinking. Creativity. Innovation.` · sticky/fixed elements: `3`
- **Step 04** (`y=5950px`, `37%`): Active landmark `Chambers & Partners` · sticky/fixed elements: `2`
- **Step 05** (`y=8500px`, `52%`): Active landmark `Eco Online` · sticky/fixed elements: `2`
- **Step 06** (`y=11050px`, `68%`): Active landmark `Section @ 68%` · sticky/fixed elements: `3`
- **Step 07** (`y=13600px`, `84%`): Active landmark `Section @ 84%` · sticky/fixed elements: `2`
- **Step 08** (`y=14400px`, `89%`): Active landmark `Latest insights` · sticky/fixed elements: `2`

### Multi-Page Internal Route Map
- **Detail Route (`/work/chambers/`)**: `https://www.plugandplaydesign.co.uk/work/chambers/` — H1: `A 300,000-page enterprise transformation for the...`, scrollHeight `19729px`, transition `direct` (`887ms`)
- **About Route (`/about-us/`)**: `https://www.plugandplaydesign.co.uk/about-us/` — H1: `20 years of creating memorable digital experiences`, scrollHeight `7620px`, transition `direct` (`749ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-plugandplaydesign-co-uk (Web Design Agency London & Guildford · Plug & Play)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-plugandplaydesign-co-uk` (**Web Design Agency London & Guildford · Plug & Play** — `https://www.plugandplaydesign.co.uk/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fafafa` canvas, `#080808` ink, `#808080` accent).
- **Identity & Domain Context**: Award-winning web design agency in London and Guildford. High-performance websites and digital retainers that drive measurable growth.
- **Primary Substrate**: `#fafafa` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#080808`, **Accent / Highlight**: `#808080`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#fafafa` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#080808` primary typography and `#808080` accents.
  - **Grounded Typographic Hierarchy**: Uses `Geist` across display (`Web Design Agency in London and Surr`) and body copy, paired with `Geist Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1328px` container bounds (`gap: 8px`, padding `48px`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-plugandplaydesign-co-uk` in your global stylesheet:

:root {
  /* Web Design Agency London & Guildford · Plug & Play (www-plugandplaydesign-co-uk) — Live-Grounded CSS Variables */
  --page-margin: 1rem; /* Layout / Spatial Grid Token (www-plugandplaydesign-co-uk) */
  --content-width: calc(100vw - 2rem); /* Layout / Spatial Grid Token (www-plugandplaydesign-co-uk) */
  --spacing-scrolling-copy: calc((var(--scrolling-items-width) - 2.5rem) * 6 / 10); /* Typography Ink Token (www-plugandplaydesign-co-uk) */
  --spacing-scrolling-media: calc((var(--scrolling-items-width) - 2.5rem) * 4 / 10); /* Layout / Spatial Grid Token (www-plugandplaydesign-co-uk) */
  --spacing-scrolling-media-adjacent: calc((var(--scrolling-items-width) - 2.5rem) * 4.5 / 10); /* Layout / Spatial Grid Token (www-plugandplaydesign-co-uk) */
  --spacing-scrolling-expanded: calc((var(--scrolling-items-width) - 2.5rem) * 5.5 / 10); /* Layout / Spatial Grid Token (www-plugandplaydesign-co-uk) */
  --background: var(--color-grey-50); /* Canvas / Surface Token (www-plugandplaydesign-co-uk) */
  --background-secondary: var(--color-grey-100); /* Canvas / Surface Token (www-plugandplaydesign-co-uk) */
  --background-tertiary: var(--color-grey-200); /* Canvas / Surface Token (www-plugandplaydesign-co-uk) */
  --background-raised: var(--color-white); /* Canvas / Surface Token (www-plugandplaydesign-co-uk) */
  --background-glass: #fafafa01; /* Canvas / Surface Token (www-plugandplaydesign-co-uk) */
  --foreground: var(--color-grey-950); /* Typography Ink Token (www-plugandplaydesign-co-uk) */
  --foreground-secondary: var(--color-grey-700); /* Typography Ink Token (www-plugandplaydesign-co-uk) */
  --foreground-tertiary: var(--color-grey-500); /* Typography Ink Token (www-plugandplaydesign-co-uk) */
  --foreground-inactive: var(--color-grey-400); /* Typography Ink Token (www-plugandplaydesign-co-uk) */
  --foreground-muted: var(--color-grey-600); /* Typography Ink Token (www-plugandplaydesign-co-uk) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fafafa` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#080808` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `.bg-white { background-color: white }` (`#ffffff`)
- **Interactive Accent / Highlight**: `#808080` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#808080` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#808080` — grounded in hairline divider derived from live computed `p` `color` (`computed_styles.json`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1328px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `48px` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1328px`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `48px` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:67.5rem)`
- **Corner Radii**: `3.35544e+07px`, `.25rem`, `var(--radius-cursor-tooltip)`, `var(--radius-full)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 14px`, `line-height: 19.6px`, `font-weight: 400`, `letter-spacing: -0.28px`); rule `h1` (`font-size: var(--text-body-sm)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`)
- **H2 Section Rule**: live computed `h2` (`font-size: 32px`, `line-height: 38.4px`, `font-weight: 400`, `letter-spacing: -0.64px`); rule `h2` (`font-size: var(--text-body-sm)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-body-sm: .875rem`, `--text-body-sm--line-height: 1.4`, `--text-body-sm--letter-spacing: -.02em`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: "Geist Mono",ui-monospace,"SF Mono",Menlo,monospace`, `--default-mono-font-family: var(--font-mono)`, `--text-caption: .75rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-plugandplaydesign-co-uk` (`Web Design Agency London & Guildford · Plug & Play`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `www-plugandplaydesign-co-uk`)**:
   - DOM & Selectors: Landmark `<header class="inset-x-0 z-40">` (`1440x60px`) hosting `Web Design Agency London & Guildford` navigation (`Web Design · Branding · Digital Marketing · UX / UI Design · eCommerce`), DOM attributes (`data-hero-enter`, `data-precedence="next"`, `data-precedence="next"`, `data-domain="plugandplaydesign.co.uk"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.inset-x-0> — `www-plugandplaydesign-co-uk`)` (`www-plugandplaydesign-co-uk`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:67.5rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.7,.2,.18,.85)` transitions and links `Web Design · Branding · Digital Marketing · UX / UI Design · eCommerce`.
2. **Hero Stage & Focal Lead (<section.px-page> — `Web Design Agency in London and Su`)**:
   - DOM & Selectors: Landmark `<section class="px-page pt-section">` presenting display lead `Web Design Agency in London and Surrey` and copy excerpt *"Plug and Play is a creative web design agency based in Guildford,"* over `#fafafa` canvas and `#080808` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#fafafa` background with `#080808` headline `Web Design Agency in London and Surrey`.
3. **Primary Showcase & Content Grid (<section.bg-background> — `Web Design Agency`)**:
   - DOM & Selectors: Landmark `<section class="bg-background px-page">` rendering section `Web Design Agency` with copy *"Websites that drive results,"*, asset references (`ca4cfa437ae45d18.css`, `dd5d352a082118c1.css`, `webpack-43624c9fe997cbf4.js`, `cf303062-0b72e54636065547.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.bg-background> — `Web Design Agency`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1328px`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `48px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.w-screen> — `Websites that drive results, digit`)**:
   - DOM & Selectors: Landmark `<section class="w-screen">` framing `Websites that drive results, digital retainers th...` and `Critical thinking. Creativity. Innovation.` (*"digital retainers that deliver growth."*) with `#ffffff` surface cards, `#808080` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.w-screen> — `Websites that drive results, digit`)` uses `3.35544e+07px`, `.25rem`, `var(--radius-cursor-tooltip)`, `var(--radius-full)` radii, `#808080` highlights, and assets (ca4cfa437ae45d18.css, dd5d352a082118c1.css, webpack-43624c9fe997cbf4.js).
5. **Colophon & Global Directory Footer (<footer.bg-background> — `https://www.plugandplaydesign.co.uk/`)**:
   - DOM & Selectors: Landmark `<footer class="bg-background px-page">` anchoring `Web Design Agency London & Guild` footer links (`Web Design · Branding · Digital Marketing · UX / UI Design · eCommerce`), copy *"Trusted by ambitious organisations across every major sector"*, and `#808080` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.bg-background> — `https://www.plugandplaydesign.co.uk/`)` aligns to `1328px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `48px` lateral canvas padding with `8px` grid gap and attributes (data-hero-enter, data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Plug and Play is a creative web design agency based in Guildford, Surrey, serving..."*
- Copy Excerpt 2: *"Websites that drive results,"*
- Copy Excerpt 3: *"digital retainers that deliver growth."*
- Copy Excerpt 4: *"Trusted by ambitious organisations across every major sector"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.7,.2,.18,.85)`
- **Extracted Stylesheet Rules (`www-plugandplaydesign-co-uk`)**:
- `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-plugandplaydesign-co-uk` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-plugandplaydesign-co-uk` stylesheet.
- **Selector `opacity\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-plugandplaydesign-co-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.inset-x-0>` and `<section.bg-background>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `17101px` across 8 distinct viewport chapters.
- **Vertical Chapter Sequence**: Web Design Agency (0%) -> Section @ 5% (5%) -> Critical thinking. Creativi... (21%) -> Chambers & Partners (37%) -> Eco Online (52%) -> Section @ 68% (68%) -> Section @ 84% (84%) -> Latest insights (89%).
- **Navigation Drawer / Menu State**: Replicate interactive menu toggle (`Services`) with Escape-to-close keyboard handling.
- **Multi-Page Routes**: Scaffold internal routes `/work/chambers/` (detail, direct), `/about-us/` (about, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-plugandplaydesign-co-uk`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Web Design Agency | `2` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `5%` | Section @ 5% | `2` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `3400px` | `21%` | Critical thinking. Creativity. Innovation. | `3` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5950px` | `37%` | Chambers & Partners | `2` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `8500px` | `52%` | Eco Online | `2` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `11050px` | `68%` | Section @ 68% | `3` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `13600px` | `84%` | Section @ 84% | `2` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `14400px` | `89%` | Latest insights | `2` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Web Design Agency | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `7200px` | `50%` | Powerleague App | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `14400px` | `100%` | Web Design Agency in London and Surrey | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `nav_menu` | Nav/Menu opened (`Services`, diff `65.17`) | [state-nav.webp](assets/state-nav.webp) |
| `interactive_control` | Control `accordion` (`Senior expertise, from brief...`, diff `14.099`) | [state-interactive.webp](assets/state-interactive.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `detail` | `https://www.plugandplaydesign.co.uk/work/chambers/` | A 300,000-page enterprise transformat... | `19729px` | `direct` (`887ms`) | [subpage-01-work-chambers.webp](assets/subpage-01-work-chambers.webp) |
| `2` | `about` | `https://www.plugandplaydesign.co.uk/about-us/` | 20 years of creating memorable digita... | `7620px` | `direct` (`749ms`) | [subpage-02-about-us.webp](assets/subpage-02-about-us.webp) |

