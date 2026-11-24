---
title: "UI Prompt Blueprint: ads-apple-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "ads-apple-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 3
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#2997ff` accent)"
---

# UI Design System & Master Generation Blueprint: ads-apple-com

> **Apple Ads** (http://ads.apple.com) — Reach customers where only Apple Ads can take you. Learn how to grow your business with ads on the App Store, Apple Maps, Apple News, MLS...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Apple Ads** (`http://ads.apple.com`). Reach customers where only Apple Ads can take you. Learn how to grow your business with ads on the App Store, Apple Maps, Apple News, MLS...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#2997ff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#2997ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `SF Pro Display` for display copy (`Advertising that works for everyone.`) with `SF Pro Text`.
  - **Calibrated Spatial Grid & Motion**: Combines `1260px` container bounds (`gap: 56px`, padding `22px`) with `cubic-bezier(.4,0,.6,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=6127px` / doc `7027px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1260px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `22px` lateral canvas padding with `56px` grid gap.
- **Border Radius Scale**: `5px`, `6px`, `980px`, `var(--sk-button-border-radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1260px`, `gap: 56px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `22px` horizontal padding.
- **Extracted CSS Media Queries**: `@media only screen and (max-width: 833px)`, `@media only screen and (max-width: 480px)`, `@media only screen and (max-width: 1023px)`, `@media only screen and (max-width: 734px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e8e8ed` | live computed `nav` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#2997ff` | `ooter-dark a.ac-gf-block .ac-gf... { color: #2997ff }` |
| **Secondary / Muted Copy** | `#888888` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#d2d2d7` | `var(--buystrip-border-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--r-localnav-height` | `52px` | Layout / Spatial Grid Token |
| `--r-localnav-stacked-height` | `66px` | Layout / Spatial Grid Token |
| `--r-localnav-viewport-large-min-width` | `1024px` | Layout / Spatial Grid Token |
| `--r-localnav-viewport-large-query` | `(min-width: 1024px)` | Layout / Spatial Grid Token |
| `--r-localnav-viewport-medium-min-width` | `768px` | Layout / Spatial Grid Token |
| `--r-localnav-viewport-medium-max-width` | `1023px` | Layout / Spatial Grid Token |
| `--r-localnav-viewport-medium-query` | `(min-width: 768px)` | Layout / Spatial Grid Token |
| `--r-localnav-viewport-small-min-width` | `320px` | Layout / Spatial Grid Token |
| `--r-localnav-viewport-small-max-width` | `767px` | Layout / Spatial Grid Token |
| `--r-localnav-viewport-small-query` | `(min-width: 320px)` | Layout / Spatial Grid Token |
| `--sk-body-text-color` | `rgb(29, 29, 31)` | Typography Ink Token |
| `--sk-headline-text-color` | `rgb(29, 29, 31)` | Typography Ink Token |
| `--sk-body-background-color` | `rgb(255, 255, 255)` | Canvas / Surface Token |
| `--sk-body-font-stack` | `text` | Typography / Scale Token |
| `--sk-default-stacked-margin` | `.4em` | Layout / Spatial Grid Token |
| `--sk-paragraph-plus-element-margin` | `.8em` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `SF Pro Display`.
- **Primary Body Stack**: `SF Pro Text`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80px`, `line-height: 84px`, `font-weight: 600`, `letter-spacing: -1.2px`); CSS variables `--sk-button-display: inline-block`, `--sk-badge-display: initial`; rule `h1` (`font-size: 40px`, `font-weight: 500`).
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 56px`, `line-height: 60px`, `font-weight: 600`).
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 25px`, `font-weight: 400`, `letter-spacing: -0.374px`); CSS variables `--sk-body-font-stack: text`, `--sk-paragraph-plus-element-margin: .8em`, `--sk-paragraph-plus-headline-margin: 1.6em`; rule `p` (`font-size: 12px`, `line-height: 1.33337`, `letter-spacing: -.01em`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 25px`, `font-weight: 400`, `letter-spacing: -0.374px`); CSS variables `--r-localnav-viewport-small-min-width: 320px`, `--r-localnav-viewport-small-max-width: 767px`, `--r-localnav-viewport-small-query: (min-width: 320px)`; rule `small` (`font-size: 1em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.25,.1,.3,1)`, `cubic-bezier(1,.1,0,.3)`.

### Per-Element Transition & Choreography Rules
- **Selector `media only screen and (max-width:...`**: `transition: transform .3s ease` extracted from `ads-apple-com` stylesheet.
- **Selector `panded .ac-gf-directory-column-se...`**: `transition: transform 300ms ease` extracted from `ads-apple-com` stylesheet.
- **Selector `obalnav.globalnav-block-transitio...`**: `transition: none!important` extracted from `ads-apple-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.6,1)`)**: Governs interactive state transitions across `<nav.localnav>` and `<section.heroPanel-video-v1>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `7027px`, deepest scrollY reached `6127px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Hover Physics (`primary_cta` · `Get started`)**: `backgroundColor`: `rgb(0, 113, 227)` -> `rgb(0, 118, 223)` (`transition-duration: 0s`, `timing: ease`).
- **Route Transition Architecture**: First internal navigation (`/app-store`) measured as `MPA` in `1384ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Apple Ads                                  │
│ ====================================================================== │
│ [ <nav.localnav> (1440x44px)          |  Ads · Local Nav Open Menu  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero-panel-cb> (w=1440px)                     | │
│ | H1: Advertising that works for everyone.                           | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #2997ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.heroPanel-video-v) max-w: 1260px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Run ads on Apple Maps. The m |  | Experiences only Apple can d | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.callout-text-with) — Spark discovery where | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.js>         ) | http://ads.apple.com                 │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 56px)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.localnav>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero-panel-cb>) — 390px Vertical Lead         | │
│ | H1: Advertising that works for everyone.                           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.heroPanel-vid) — 1-Col Stack              | │
│ | [ Item 1: Run ads on Apple Maps. The most direct route to r...   ] | │
│ | [ Item 2: Experiences only Apple can deliver.                    ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.callout-text-wi) — 1-Col (Spark discovery wh) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.js>         ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.localnav> — `ads-apple-com`)**:
   - Landmark `<nav class="localnav localnav--custom-background">` (`1440x44px`) hosting `Apple Ads` navigation (` Ads · Local Nav Open Menu · Local Nav Close Menu · App Store · Apple Maps`), DOM attributes (`data-anim-scroll-group="body"`, `data-sticky="sticky"`, `data-tracking-title="App Store"`, `data-tracking-title="Apple Maps"`), and stylesheet rule `font-face { font-family: "Apple Icons 100"; src: url("../assets/ac-footer/legacy/app... }`.
2. **Hero Stage & Focal Lead (<section.hero-panel-cb> — `Advertising that works for everyon`)**:
   - Landmark `<section class="hero-panel-cb heroPanel-video-v1">` presenting display lead `Advertising that works for everyone.` and copy excerpt *"Promote your brand in the places people love and trust. Apple Ads"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.heroPanel-video-v1> — `Run ads on Apple Maps. The most di`)**:
   - Landmark `<section class="hero-panel-cb heroPanel-video-v1">` rendering section `Run ads on Apple Maps. The most direct route to r...` with copy *"Promote your brand in the places people love and trust."*, asset references (`favicon.ico`, `180_touch.png`, `ads.apple.com`, `globalheader.css`), and grid rule `ac-globalfooter { font-weight: normal; -webkit-text-size-adjust: 100%; text-size-adjust: 100% }`.
4. **Interactive Detail & Feature Matrix (<section.callout-text-with-gradient> — `Experiences only Apple can deliver`)**:
   - Landmark `<section class="callout-text-with-gradient section-content--fixed">` framing `Experiences only Apple can deliver.` and `Spark discovery where downloads happen.` (*"Apple Ads purposefully integrates your advertising where millions"*) with `#e8e8ed` surface cards, `#2997ff` accents, and `after { box-sizing: content-box; margin: 0; padding: 0; pointer-events: auto; le... }`.
5. **Colophon & Global Directory Footer (<footer.js> — `http://ads.apple.com`)**:
   - Landmark `<footer class="js sa-footer">` anchoring `Apple Ads` footer links (` Ads · Local Nav Open Menu · Local Nav Close Menu · App Store · Apple Maps`), copy *"Creating opportunity — and helping you grow your business — "*, and `#d2d2d7` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Run ads on Apple Maps. The most direct route to r...` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `14%`): Active landmark `Advertising that works for everyone.` · sticky/fixed elements: `1`
- **Step 03** (`y=1700px`, `28%`): Active landmark `Experiences only Apple can deliver.` · sticky/fixed elements: `1`
- **Step 04** (`y=2550px`, `42%`): Active landmark `Over 850 million people visit the App Store every...` · sticky/fixed elements: `1`
- **Step 05** (`y=4250px`, `69%`): Active landmark `Brands count on Apple Ads.` · sticky/fixed elements: `1`
- **Step 06** (`y=5100px`, `83%`): Active landmark `Find your next advertising opportunity.` · sticky/fixed elements: `1`
- **Step 07** (`y=5950px`, `97%`): Active landmark `Footer` · sticky/fixed elements: `1`
- **Step 08** (`y=6127px`, `100%`): Active landmark `Advertising with Apple` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Other Route (`/app-store`)**: `https://ads.apple.com/app-store` — H1: `Spark discovery where downloads happen.`, scrollHeight `12434px`, transition `MPA` (`1384ms`)
- **Other Route (`/maps`)**: `https://ads.apple.com/maps` — H1: `Route customers to your business on Apple Maps.`, scrollHeight `7968px`, transition `direct` (`1640ms`)
- **Other Route (`/apple-news`)**: `https://ads.apple.com/apple-news` — H1: `Engage readers within the topics they care about.`, scrollHeight `7763px`, transition `direct` (`1780ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: ads-apple-com (Apple Ads)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `ads-apple-com` (**Apple Ads** — `http://ads.apple.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#2997ff` accent).
- **Identity & Domain Context**: Reach customers where only Apple Ads can take you. Learn how to grow your business with ads on the App Store, Apple Maps, Apple News, MLS...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#2997ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#2997ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `SF Pro Display` for display copy (`Advertising that works for everyone.`) with `SF Pro Text`.
  - **Calibrated Spatial Grid & Motion**: Combines `1260px` container bounds (`gap: 56px`, padding `22px`) with `cubic-bezier(.4,0,.6,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `ads-apple-com` in your global stylesheet:

:root {
  /* Apple Ads (ads-apple-com) — Live-Grounded CSS Variables */
  --r-localnav-height: 52px; /* Layout / Spatial Grid Token (ads-apple-com) */
  --r-localnav-stacked-height: 66px; /* Layout / Spatial Grid Token (ads-apple-com) */
  --r-localnav-viewport-large-min-width: 1024px; /* Layout / Spatial Grid Token (ads-apple-com) */
  --r-localnav-viewport-large-query: (min-width: 1024px); /* Layout / Spatial Grid Token (ads-apple-com) */
  --r-localnav-viewport-medium-min-width: 768px; /* Layout / Spatial Grid Token (ads-apple-com) */
  --r-localnav-viewport-medium-max-width: 1023px; /* Layout / Spatial Grid Token (ads-apple-com) */
  --r-localnav-viewport-medium-query: (min-width: 768px); /* Layout / Spatial Grid Token (ads-apple-com) */
  --r-localnav-viewport-small-min-width: 320px; /* Layout / Spatial Grid Token (ads-apple-com) */
  --r-localnav-viewport-small-max-width: 767px; /* Layout / Spatial Grid Token (ads-apple-com) */
  --r-localnav-viewport-small-query: (min-width: 320px); /* Layout / Spatial Grid Token (ads-apple-com) */
  --sk-body-text-color: rgb(29, 29, 31); /* Typography Ink Token (ads-apple-com) */
  --sk-headline-text-color: rgb(29, 29, 31); /* Typography Ink Token (ads-apple-com) */
  --sk-body-background-color: rgb(255, 255, 255); /* Canvas / Surface Token (ads-apple-com) */
  --sk-body-font-stack: text; /* Typography / Scale Token (ads-apple-com) */
  --sk-default-stacked-margin: .4em; /* Layout / Spatial Grid Token (ads-apple-com) */
  --sk-paragraph-plus-element-margin: .8em; /* Typography / Scale Token (ads-apple-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#e8e8ed` — grounded in live computed `nav` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#2997ff` — grounded in `ooter-dark a.ac-gf-block .ac-gf... { color: #2997ff }`
- **Secondary / Muted Copy**: `#888888` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#d2d2d7` — grounded in `var(--buystrip-border-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1260px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `22px` lateral canvas padding with `56px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1260px`, `gap: 56px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `22px` horizontal padding
- **Media Queries**: `@media only screen and (max-width: 833px)`, `@media only screen and (max-width: 480px)`, `@media only screen and (max-width: 1023px)`, `@media only screen and (max-width: 734px)`
- **Corner Radii**: `5px`, `6px`, `980px`, `var(--sk-button-border-radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `SF Pro Display`
- **Body Font Stack**: `SF Pro Text`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 80px`, `line-height: 84px`, `font-weight: 600`, `letter-spacing: -1.2px`); CSS variables `--sk-button-display: inline-block`, `--sk-badge-display: initial`; rule `h1` (`font-size: 40px`, `font-weight: 500`)
- **H2 Section Rule**: live computed `h3 (primary section heading)` (`font-size: 56px`, `line-height: 60px`, `font-weight: 600`)
- **Body Copy Rule**: live computed `body` (`font-size: 17px`, `line-height: 25px`, `font-weight: 400`, `letter-spacing: -0.374px`); CSS variables `--sk-body-font-stack: text`, `--sk-paragraph-plus-element-margin: .8em`, `--sk-paragraph-plus-headline-margin: 1.6em`; rule `p` (`font-size: 12px`, `line-height: 1.33337`, `letter-spacing: -.01em`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 17px`, `line-height: 25px`, `font-weight: 400`, `letter-spacing: -0.374px`); CSS variables `--r-localnav-viewport-small-min-width: 320px`, `--r-localnav-viewport-small-max-width: 767px`, `--r-localnav-viewport-small-query: (min-width: 320px)`; rule `small` (`font-size: 1em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `ads-apple-com` (`Apple Ads`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.localnav> — `ads-apple-com`)**:
   - DOM & Selectors: Landmark `<nav class="localnav localnav--custom-background">` (`1440x44px`) hosting `Apple Ads` navigation (` Ads · Local Nav Open Menu · Local Nav Close Menu · App Store · Apple Maps`), DOM attributes (`data-anim-scroll-group="body"`, `data-sticky="sticky"`, `data-tracking-title="App Store"`, `data-tracking-title="Apple Maps"`), and stylesheet rule `font-face { font-family: "Apple Icons 100"; src: url("../assets/ac-footer/legacy/app... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.localnav> — `ads-apple-com`)` (`ads-apple-com`) adapts across `@media only screen and (max-width: 833px)`, `@media only screen and (max-width: 480px)`, `@media only screen and (max-width: 1023px)`, `@media only screen and (max-width: 734px)` with `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.25,.1,.3,1)`, `cubic-bezier(1,.1,0,.3)` transitions and links ` Ads · Local Nav Open Menu · Local Nav Close Menu · App Store · Apple Maps`.
2. **Hero Stage & Focal Lead (<section.hero-panel-cb> — `Advertising that works for everyon`)**:
   - DOM & Selectors: Landmark `<section class="hero-panel-cb heroPanel-video-v1">` presenting display lead `Advertising that works for everyone.` and copy excerpt *"Promote your brand in the places people love and trust. Apple Ads"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#ffffff` background with `#000000` headline `Advertising that works for everyone.`.
3. **Primary Showcase & Content Grid (<section.heroPanel-video-v1> — `Run ads on Apple Maps. The most di`)**:
   - DOM & Selectors: Landmark `<section class="hero-panel-cb heroPanel-video-v1">` rendering section `Run ads on Apple Maps. The most direct route to r...` with copy *"Promote your brand in the places people love and trust."*, asset references (`favicon.ico`, `180_touch.png`, `ads.apple.com`, `globalheader.css`), and grid rule `ac-globalfooter { font-weight: normal; -webkit-text-size-adjust: 100%; text-size-adjust: 100% }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.heroPanel-video-v1> — `Run ads on Apple Maps. The most di`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1260px`, `gap: 56px`) on desktop and Single-column vertical stack at `390px` viewport width with `22px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.callout-text-with-gradient> — `Experiences only Apple can deliver`)**:
   - DOM & Selectors: Landmark `<section class="callout-text-with-gradient section-content--fixed">` framing `Experiences only Apple can deliver.` and `Spark discovery where downloads happen.` (*"Apple Ads purposefully integrates your advertising where millions"*) with `#e8e8ed` surface cards, `#2997ff` accents, and `after { box-sizing: content-box; margin: 0; padding: 0; pointer-events: auto; le... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.callout-text-with-gradient> — `Experiences only Apple can deliver`)` uses `5px`, `6px`, `980px`, `var(--sk-button-border-radius)` radii, `#2997ff` highlights, and assets (favicon.ico, 180_touch.png, ads.apple.com).
5. **Colophon & Global Directory Footer (<footer.js> — `http://ads.apple.com`)**:
   - DOM & Selectors: Landmark `<footer class="js sa-footer">` anchoring `Apple Ads` footer links (` Ads · Local Nav Open Menu · Local Nav Close Menu · App Store · Apple Maps`), copy *"Creating opportunity — and helping you grow your business — "*, and `#d2d2d7` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.js> — `http://ads.apple.com`)` aligns to `1260px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `22px` lateral canvas padding with `56px` grid gap and attributes (data-anim-scroll-group="body", data-sticky="sticky", data-tracking-title="App Store").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Promote your brand in the places people love and trust. Apple Ads purposefully int..."*
- Copy Excerpt 2: *"Promote your brand in the places people love and trust."*
- Copy Excerpt 3: *"Apple Ads purposefully integrates your advertising where millions go to experience..."*
- Copy Excerpt 4: *"Creating opportunity — and helping you grow your business — where only Apple can."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.25,.1,.3,1)`, `cubic-bezier(1,.1,0,.3)`
- **Extracted Stylesheet Rules (`ads-apple-com`)**:
- `font-face { font-family: "Apple Icons 100"; src: url("../assets/ac-footer/legacy/app... }`
- `ac-globalfooter { font-weight: normal; -webkit-text-size-adjust: 100%; text-size-adjust: 100% }`
- `after { box-sizing: content-box; margin: 0; padding: 0; pointer-events: auto; le... }`
- `ac-globalfooter section { display: block }`
- `ac-globalfooter img { border: 0; vertical-align: middle }`
- **Per-Selector Transition Rules**:
- **Selector `media only screen and (max-width:...`**: `transition: transform .3s ease` extracted from `ads-apple-com` stylesheet.
- **Selector `panded .ac-gf-directory-column-se...`**: `transition: transform 300ms ease` extracted from `ads-apple-com` stylesheet.
- **Selector `obalnav.globalnav-block-transitio...`**: `transition: none!important` extracted from `ads-apple-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.6,1)`)**: Governs interactive state transitions across `<nav.localnav>` and `<section.heroPanel-video-v1>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `7027px` across 8 distinct viewport chapters.
- **Vertical Chapter Sequence**: Run ads on Apple Maps. The... (0%) -> Advertising that works for... (14%) -> Experiences only Apple can... (28%) -> Over 850 million people vis... (42%) -> Brands count on Apple Ads. (69%) -> Find your next advertising... (83%) -> Footer (97%) -> Advertising with Apple (100%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `backgroundColor` with `0s ease`.
- **Multi-Page Routes**: Scaffold internal routes `/app-store` (other, MPA), `/maps` (other, direct), `/apple-news` (other, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `ads-apple-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Run ads on Apple Maps. The most direct route... | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `14%` | Advertising that works for everyone. | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `1700px` | `28%` | Experiences only Apple can deliver. | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `2550px` | `42%` | Over 850 million people visit the App Store e... | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `4250px` | `69%` | Brands count on Apple Ads. | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `5100px` | `83%` | Find your next advertising opportunity. | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `5950px` | `97%` | Footer | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `6127px` | `100%` | Advertising with Apple | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Run ads on Apple Maps. The most direct ro... | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `3682px` | `50%` | A loyal audience. | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `7450px` | `100%` | Advertising with Apple | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `other` | `https://ads.apple.com/app-store` | Spark discovery where downloads happen. | `12434px` | `MPA` (`1384ms`) | [subpage-01-app-store.webp](assets/subpage-01-app-store.webp) |
| `2` | `other` | `https://ads.apple.com/maps` | Route customers to your business on A... | `7968px` | `direct` (`1640ms`) | [subpage-02-maps.webp](assets/subpage-02-maps.webp) |
| `3` | `other` | `https://ads.apple.com/apple-news` | Engage readers within the topics they... | `7763px` | `direct` (`1780ms`) | [subpage-03-apple-news.webp](assets/subpage-03-apple-news.webp) |

