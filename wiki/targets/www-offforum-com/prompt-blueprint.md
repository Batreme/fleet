---
title: "UI Prompt Blueprint: www-offforum-com"
date: 2026-11-15
target: "www-offforum-com"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#c5c5c5` accent)"
---

# UI Design System & Master Generation Blueprint: www-offforum-com

> **A WEEK OF DESIGN, ART & DIGITAL CULTURE · FORUM · SEPT 15, 2027 · OFFF S...** (https://www.offforum.com/) — A one-week festival convening designers, artists, and digital culture practitioners.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **A WEEK OF DESIGN, ART & DIGITAL CULTURE · FORUM · SEPT 15, 2027 · OFFF S...** (`https://www.offforum.com/`). A one-week festival convening designers, artists, and digital culture practitioners.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#c5c5c5` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#c5c5c5` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Baikal` for display copy (`A WEEK OF DESIGN, ART & DIGITAL CULT`) with `Forvm` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `66.6667%` container bounds (`gap: 0px (flush layout)`, padding `var(--spacing-gutter)`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×1397px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `66.6667%` extracted from `www-offforum-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--spacing-gutter)` lateral canvas padding with `0px (flush layout)` grid gap.
- **Border Radius Scale**: `2147483647px`, `40px`, `var(--radius)`, `var(--box-radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 66.6667%`, `gap: 0px (flush layout)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing-gutter)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=40rem)`, `@media (width>=80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ee3338` | `var(--color-red)` in `:root` |
| **Interactive Accent / Highlight** | `#c5c5c5` | `var(--color-grey)` in `:root` |
| **Secondary / Muted Copy** | `#0000` | `textarea { background-color: #0000 }` |
| **Structural Hairline Border** | `#000000` | `html { background-color: black }` (`#000000`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--spacing` | `.1rem` | Layout / Spatial Grid Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--ease-in-out` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--aspect-video` | `16 / 9` | Design System Custom Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--font-baikal` | `"Baikal", sans-serif` | Typography / Scale Token |
| `--font-forvm` | `"Forvm", serif` | Typography / Scale Token |
| `--text-body-mobile` | `1.8rem` | Typography Ink Token |
| `--text-body-mobile--line-height` | `2rem` | Typography Ink Token |
| `--text-body-mobile--font-weight` | `600` | Typography Ink Token |
| `--text-body-mobile--letter-spacing` | `-.04em` | Typography Ink Token |
| `--text-body-desktop` | `2.4rem` | Typography Ink Token |
| `--text-body-desktop--line-height` | `2.6rem` | Typography Ink Token |
| `--text-body-desktop--font-weight` | `600` | Typography Ink Token |
| `--text-body-desktop--letter-spacing` | `-.04em` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Baikal`.
- **Primary Body Stack**: `Forvm`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-h1-mobile-offf: 3.2rem`, `--text-h1-mobile-offf--line-height: 3.1rem`, `--text-h1-mobile-offf--font-weight: 600`.
- **Section Heading (`H2`)**: CSS variables `--text-h2-mobile-offf: 3.2rem`, `--text-h2-mobile-offf--line-height: 3.1rem`, `--text-h2-mobile-offf--font-weight: 600`; rule `h2` (`font-size: var(--text-body-mobile)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`, `font-weight: var(--tw-font...`).
- **Body Copy**: CSS variables `--text-body-mobile: 1.8rem`, `--text-body-mobile--line-height: 2rem`, `--text-body-mobile--font-weight: 600`.
- **Metadata & Navigation Labels**: CSS variables `--text-body-mobile--letter-spacing: -.04em`, `--text-body-desktop--letter-spacing: -.04em`, `--text-body-2-mobile--letter-spacing: -.02em`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.76,0,.24,1)`, `cubic-bezier(.87,0,.13,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-offforum-com` stylesheet.
- **Selector `.button-basic-primary`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-offforum-com` stylesheet.
- **Selector `.button-basic-secondary`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-offforum-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.header>` and `<main.min-h-screen>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — A WEEK OF DESIGN, ART & DIGITAL CULTURE ·  │
│ ====================================================================== │
│ [ <header.header>          | About                                  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.min-h-screen>                                  |   │
│ | H1: A WEEK OF DESIGN, ART & DIGITAL CULTURE · FORUM ·...         |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #c5c5c5        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.min-h-screen>       ) max-w: 66.6667%       |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Join our community and get u |  | Our cookies and those of our | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px (f) | │
│ | [<header.header>] -> [<main.min-h-screen] -> [<main.min-h-screen] |  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.container-main) | https://www.offforum.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `www-offforum-com`)**:
   - Landmark `<header class="header h-header-height">` hosting `A WEEK OF DESIGN, ART & DIGITAL CULT` navigation (`About`), DOM attributes (`data-svg-origin="609.3610229492188 0"`, `data-svg-origin="-0.09765620529651642..."`, `data-nuxt-data="nuxt-app"`, `data-ssr="true"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.min-h-screen> — `A WEEK OF DESIGN, ART & DIGITAL CU`)**:
   - Landmark `<main class="min-h-screen">` presenting display lead `A WEEK OF DESIGN, ART & DIGITAL CULTURE · FORUM ·...` and copy excerpt *"We use cookies on this site"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.min-h-screen> — `Join our community and get updates`)**:
   - Landmark `<main class="min-h-screen">` rendering section `Join our community and get updates, offers, and e...` with copy *"Our cookies and those of our partners help improve your experienc"*, asset references (`gtm.js`, `entry.CI2s3_W4.css`, `_payload.json`, `f8tcD554.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.min-h-screen> — `Our cookies and those of our partn`)**:
   - Landmark `<main class="min-h-screen">` framing `Our cookies and those of our partners help impro` and `Allow necessary cookies` (*"Allow necessary cookies"*) with `#ee3338` surface cards, `#c5c5c5` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.container-main> — `https://www.offforum.com/`)**:
   - Landmark `<footer class="container-main">` anchoring `A WEEK OF DESIGN, ART & DIGITAL ` footer links (`About`), copy *"GET YOUR FORUM TICKET"*, and `#000000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-offforum-com (A WEEK OF DESIGN, ART & DIGITAL CULTURE · FORUM · SEPT 15, 2027 · OFFF S...)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-offforum-com` (**A WEEK OF DESIGN, ART & DIGITAL CULTURE · FORUM · SEPT 15, 2027 · OFFF S...** — `https://www.offforum.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#c5c5c5` accent).
- **Identity & Domain Context**: A one-week festival convening designers, artists, and digital culture practitioners.
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#c5c5c5`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#c5c5c5` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Baikal` for display copy (`A WEEK OF DESIGN, ART & DIGITAL CULT`) with `Forvm` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `66.6667%` container bounds (`gap: 0px (flush layout)`, padding `var(--spacing-gutter)`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-offforum-com` in your global stylesheet:

:root {
  /* A WEEK OF DESIGN, ART & DIGITAL CULTURE · FORUM · SEPT 15, 2027 · OFFF S... (www-offforum-com) — Ground-Truth Extracted CSS Variables */
  --spacing: .1rem; /* Layout / Spatial Grid Token (www-offforum-com) */
  --font-weight-semibold: 600; /* Typography / Scale Token (www-offforum-com) */
  --ease-in-out: cubic-bezier(.4, 0, .2, 1); /* Motion / Easing Token (www-offforum-com) */
  --aspect-video: 16 / 9; /* Design System Custom Token (www-offforum-com) */
  --default-transition-duration: .15s; /* Motion / Easing Token (www-offforum-com) */
  --default-transition-timing-function: cubic-bezier(.4, 0, .2, 1); /* Motion / Easing Token (www-offforum-com) */
  --font-baikal: "Baikal", sans-serif; /* Typography / Scale Token (www-offforum-com) */
  --font-forvm: "Forvm", serif; /* Typography / Scale Token (www-offforum-com) */
  --text-body-mobile: 1.8rem; /* Typography Ink Token (www-offforum-com) */
  --text-body-mobile--line-height: 2rem; /* Typography Ink Token (www-offforum-com) */
  --text-body-mobile--font-weight: 600; /* Typography Ink Token (www-offforum-com) */
  --text-body-mobile--letter-spacing: -.04em; /* Typography Ink Token (www-offforum-com) */
  --text-body-desktop: 2.4rem; /* Typography Ink Token (www-offforum-com) */
  --text-body-desktop--line-height: 2.6rem; /* Typography Ink Token (www-offforum-com) */
  --text-body-desktop--font-weight: 600; /* Typography Ink Token (www-offforum-com) */
  --text-body-desktop--letter-spacing: -.04em; /* Typography Ink Token (www-offforum-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#ee3338` — grounded in `var(--color-red)` in `:root`
- **Interactive Accent / Highlight**: `#c5c5c5` — grounded in `var(--color-grey)` in `:root`
- **Secondary / Muted Copy**: `#0000` — grounded in `textarea { background-color: #0000 }`
- **Structural Hairline Border**: `#000000` — grounded in `html { background-color: black }` (`#000000`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×1397px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `66.6667%` extracted from `www-offforum-com` stylesheet
- **Padding & Gutters**: `var(--spacing-gutter)` lateral canvas padding with `0px (flush layout)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 66.6667%`, `gap: 0px (flush layout)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing-gutter)` horizontal padding
- **Media Queries**: `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=40rem)`, `@media (width>=80rem)`
- **Corner Radii**: `2147483647px`, `40px`, `var(--radius)`, `var(--box-radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Baikal`
- **Body Font Stack**: `Forvm`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-h1-mobile-offf: 3.2rem`, `--text-h1-mobile-offf--line-height: 3.1rem`, `--text-h1-mobile-offf--font-weight: 600`
- **H2 Section Rule**: CSS variables `--text-h2-mobile-offf: 3.2rem`, `--text-h2-mobile-offf--line-height: 3.1rem`, `--text-h2-mobile-offf--font-weight: 600`; rule `h2` (`font-size: var(--text-body-mobile)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`, `font-weight: var(--tw-font...`)
- **Body Copy Rule**: CSS variables `--text-body-mobile: 1.8rem`, `--text-body-mobile--line-height: 2rem`, `--text-body-mobile--font-weight: 600`
- **Metadata & Index Rule**: CSS variables `--text-body-mobile--letter-spacing: -.04em`, `--text-body-desktop--letter-spacing: -.04em`, `--text-body-2-mobile--letter-spacing: -.02em`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-offforum-com` (`A WEEK OF DESIGN, ART & DIGITAL CULTURE · FORUM · SEPT 15, 2027 · OFFF S...`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `www-offforum-com`)**:
   - DOM & Selectors: Landmark `<header class="header h-header-height">` hosting `A WEEK OF DESIGN, ART & DIGITAL CULT` navigation (`About`), DOM attributes (`data-svg-origin="609.3610229492188 0"`, `data-svg-origin="-0.09765620529651642..."`, `data-nuxt-data="nuxt-app"`, `data-ssr="true"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `www-offforum-com`)` (`www-offforum-com`) adapts across `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=40rem)`, `@media (width>=80rem)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.76,0,.24,1)`, `cubic-bezier(.87,0,.13,1)` transitions and links `About`.
2. **Hero Stage & Focal Lead (<main.min-h-screen> — `A WEEK OF DESIGN, ART & DIGITAL CU`)**:
   - DOM & Selectors: Landmark `<main class="min-h-screen">` presenting display lead `A WEEK OF DESIGN, ART & DIGITAL CULTURE · FORUM ·...` and copy excerpt *"We use cookies on this site"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×1397px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `A WEEK OF DESIGN, ART & DIGITAL CULTURE · FORUM ·...`.
3. **Primary Showcase & Content Grid (<main.min-h-screen> — `Join our community and get updates`)**:
   - DOM & Selectors: Landmark `<main class="min-h-screen">` rendering section `Join our community and get updates, offers, and e...` with copy *"Our cookies and those of our partners help improve your experienc"*, asset references (`gtm.js`, `entry.CI2s3_W4.css`, `_payload.json`, `f8tcD554.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.min-h-screen> — `Join our community and get updates`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 66.6667%`, `gap: 0px (flush layout)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing-gutter)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.min-h-screen> — `Our cookies and those of our partn`)**:
   - DOM & Selectors: Landmark `<main class="min-h-screen">` framing `Our cookies and those of our partners help impro` and `Allow necessary cookies` (*"Allow necessary cookies"*) with `#ee3338` surface cards, `#c5c5c5` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.min-h-screen> — `Our cookies and those of our partn`)` uses `2147483647px`, `40px`, `var(--radius)`, `var(--box-radius)` radii, `#c5c5c5` highlights, and assets (gtm.js, entry.CI2s3_W4.css, _payload.json).
5. **Colophon & Global Directory Footer (<footer.container-main> — `https://www.offforum.com/`)**:
   - DOM & Selectors: Landmark `<footer class="container-main">` anchoring `A WEEK OF DESIGN, ART & DIGITAL ` footer links (`About`), copy *"GET YOUR FORUM TICKET"*, and `#000000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.container-main> — `https://www.offforum.com/`)` aligns to `66.6667%` extracted from `www-offforum-com` stylesheet with `var(--spacing-gutter)` lateral canvas padding with `0px (flush layout)` grid gap and attributes (data-svg-origin="609.3610229492188 0", data-svg-origin="-0.09765620529651642...", data-nuxt-data="nuxt-app").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We use cookies on this site"*
- Copy Excerpt 2: *"Our cookies and those of our partners help improve your experience and analyze you..."*
- Copy Excerpt 3: *"Allow necessary cookies"*
- Copy Excerpt 4: *"GET YOUR FORUM TICKET"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.76,0,.24,1)`, `cubic-bezier(.87,0,.13,1)`
- **Extracted Stylesheet Rules (`www-offforum-com`)**:
- `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-offforum-com` stylesheet.
- **Selector `.button-basic-primary`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-offforum-com` stylesheet.
- **Selector `.button-basic-secondary`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-offforum-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.header>` and `<main.min-h-screen>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-offforum-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
