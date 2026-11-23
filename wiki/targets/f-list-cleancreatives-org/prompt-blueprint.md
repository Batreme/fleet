---
title: "UI Prompt Blueprint: f-list-cleancreatives-org"
date: 2026-11-23
captured_at: 2026-11-23
target: "f-list-cleancreatives-org"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1d1d1d` ink, `#ffff00` accent)"
---

# UI Design System & Master Generation Blueprint: f-list-cleancreatives-org

> **F-List 2026** (https://f-list.cleancreatives.org/) — Search the F-List 2026 to uncover the 802 advertising and PR agencies behind 1,321 documented fossil fuel contracts worldwide.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **F-List 2026** (`https://f-list.cleancreatives.org/`). Search the F-List 2026 to uncover the 802 advertising and PR agencies behind 1,321 documented fossil fuel contracts worldwide.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1d1d1d` ink, `#ffff00` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1d1d1d` primary typography and `#ffff00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `roc-grotesk-compressed` for display copy (`THE CREATIVE COVER-UP`) with `roc-grotesk` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1472px` container bounds (`gap: .75rem`, padding `7px`) with `cubic-bezier(0.4,0,0.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1472px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `7px` lateral canvas padding with `.75rem` grid gap.
- **Border Radius Scale**: `5.008px`, `2px`, `3px`, `.313rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1472px`, `gap: .75rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `7px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 479px)`, `@media (min-width: 769px)`, `@media (min-width: 480px)`, `@media (min-width: 1701px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1d1d1d` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#edcc4b` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffff00` | `header nav a:hover { color: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#edcc4b` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#f2f2f2` | `var(--cmplz_banner_border_color)` in `:root` |
| **Variable Token (`--fl-grey-1`)** | `#cacaca` | `var(--fl-grey-1)` in `:root` |
| **Variable Token (`--fl-grey-2`)** | `#7d7d7d` | `var(--fl-grey-2)` in `:root` |
| **Variable Token (`--fl-cream`)** | `#eceae3` | `var(--fl-cream)` in `:root` |
| **Variable Token (`--fl-green`)** | `#5da279` | `var(--fl-green)` in `:root` |
| **Variable Token (`--fl-red`)** | `#ff5037` | `var(--fl-red)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--fl-black-pure` | `#1D1D1D` | Canvas / Surface Token |
| `--fl-black-text` | `#1D1D1D` | Canvas / Surface Token |
| `--fl-white` | `#FFF` | Canvas / Surface Token |
| `--fl-grey-1` | `#CACACA` | Color / Atmospheric Token |
| `--fl-grey-2` | `#7D7D7D` | Color / Atmospheric Token |
| `--fl-cream` | `#ECEAE3` | Color / Atmospheric Token |
| `--fl-yellow` | `#EDCC4B` | Color / Atmospheric Token |
| `--fl-green` | `#5DA279` | Color / Atmospheric Token |
| `--fl-red` | `#FF5037` | Color / Atmospheric Token |
| `--font-longform-family` | `"roc-grotesk", sans-serif` | Typography / Scale Token |
| `--font-longform-line-height` | `165%` | Typography / Scale Token |
| `--font-longform-size` | `1.25rem` | Typography / Scale Token |
| `--font-longform-style` | `normal` | Typography / Scale Token |
| `--font-longform-weight` | `400` | Typography / Scale Token |
| `--font-longform-weight-bold` | `600` | Typography / Scale Token |
| `--font-longform-paragraph-margin` | `2.125rem 0 0 0` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `roc-grotesk-compressed`.
- **Primary Body Stack**: `roc-grotesk`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 132.951px`, `line-height: 99.7133px`, `font-weight: 700`); rule `,.h1` (`font-size: 4.5rem`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 86.1638px`, `line-height: 73.2393px`, `font-weight: 600`); rule `h2` (`font-size: 17px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-longform-paragraph-margin: 2.125rem 0 0 0`, `--cmplz_category_body_font_size: 12px`; rule `p` (`font-size: 16px`, `line-height: 24px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `small` (`line-height: 100%`, `font-weight: 300`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.4,0,0.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `popular_post_widget .template-4 l...`**: `transition: -webkit-transform 0.35s` extracted from `f-list-cleancreatives-org` stylesheet.
- **Selector `tics_popular_post_widget .templat...`**: `transition: -webkit-transform 0.35s` extracted from `f-list-cleancreatives-org` stylesheet.
- **Selector `r_post_widget .template-4 li p.ic...`**: `transition: -webkit-transform 0.35s` extracted from `f-list-cleancreatives-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.2,1)`)**: Governs interactive state transitions across `<header.browser-chrome>` and `<section.call-intro>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — F-List 2026                                │
│ ====================================================================== │
│ [ <header.browser-chrome (1440x95px)  | The report · The F-List · Di ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: THE CREATIVE COVER-UP                                          | │
│ | Substrate: #ffffff | Ink: #1d1d1d | Accent: #ffff00                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.call-intro>) max-w: 1472px                 | │
│ | +------------------------------+  +------------------------------+ | │
│ | | The Creative Cover-up        |  | Functional Always active     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.redacted>) — The technical storage         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.page-templat) | https://f-list.cleancreatives.org/   │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .75rem)     │
│ ====================================================================== │
│ [ HEADER BAR (<header.browser-chrome> ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: THE CREATIVE COVER-UP                                          | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.call-intro>) — 1-Col Stack                | │
│ | [ Item 1: The Creative Cover-up                                  ] | │
│ | [ Item 2: Functional Always active                               ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.redacted>) — 1-Col (The technical stor)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.page-templat) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.browser-chrome> — `f-list-cleancreatives-org`)**:
   - Landmark `<header class="browser-chrome">` (`1440x95px`) hosting `F-List 2026` navigation (`The report · The F-List · Dirty work · Take Action`), DOM attributes (`data-cmplz="1"`, `data-nosnippet="true"`, `data-prefix="fas"`, `data-icon="times"`), and stylesheet rule `opular_post_widget .icon-comment:... { content: "\e900"; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `THE CREATIVE COVER-UP`)**:
   - Landmark `<section class="hero home">` presenting display lead `THE CREATIVE COVER-UP` and copy excerpt *"The agencies providing cover for the fossil fuel industry."* over `#ffffff` canvas and `#1d1d1d` ink.
3. **Primary Showcase & Content Grid (<section.call-intro> — `The Creative Cover-up`)**:
   - Landmark `<section class="call-intro flex">` rendering section `The Creative Cover-up` with copy *"Functional Always active"*, asset references (`xmlrpc.php`, `www.googletagmanager.com`, `flist2026.b-cdn.net`, `embed`), and grid rule `s_popular_post_widget .icon-chat:... { content: "\e900"; }`.
4. **Interactive Detail & Feature Matrix (<section.redacted> — `Functional Always active`)**:
   - Landmark `<section class="redacted bg-cream">` framing `Functional Always active` and `The technical storage or access is strictly nece` (*"The technical storage or access is strictly necessary for the leg"*) with `#edcc4b` surface cards, `#ffff00` accents, and `s_popular_post_widget .icon-talk:... { content: "\e900"; }`.
5. **Colophon & Global Directory Footer (<footer.page-template> — `https://f-list.cleancreatives.org/`)**:
   - Landmark `<footer class="page-template">` anchoring `F-List 2026` footer links (`The report · The F-List · Dirty work · Take Action`), copy *"The technical storage or access is necessary for the legitim"*, and `#f2f2f2` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: f-list-cleancreatives-org (F-List 2026)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `f-list-cleancreatives-org` (**F-List 2026** — `https://f-list.cleancreatives.org/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1d1d1d` ink, `#ffff00` accent).
- **Identity & Domain Context**: Search the F-List 2026 to uncover the 802 advertising and PR agencies behind 1,321 documented fossil fuel contracts worldwide.
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#1d1d1d`, **Accent / Highlight**: `#ffff00`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1d1d1d` primary typography and `#ffff00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `roc-grotesk-compressed` for display copy (`THE CREATIVE COVER-UP`) with `roc-grotesk` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1472px` container bounds (`gap: .75rem`, padding `7px`) with `cubic-bezier(0.4,0,0.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `f-list-cleancreatives-org` in your global stylesheet:

:root {
  /* F-List 2026 (f-list-cleancreatives-org) — Live-Grounded CSS Variables */
  --fl-black-pure: #1D1D1D; /* Canvas / Surface Token (f-list-cleancreatives-org) */
  --fl-black-text: #1D1D1D; /* Canvas / Surface Token (f-list-cleancreatives-org) */
  --fl-white: #FFF; /* Canvas / Surface Token (f-list-cleancreatives-org) */
  --fl-grey-1: #CACACA; /* Color / Atmospheric Token (f-list-cleancreatives-org) */
  --fl-grey-2: #7D7D7D; /* Color / Atmospheric Token (f-list-cleancreatives-org) */
  --fl-cream: #ECEAE3; /* Color / Atmospheric Token (f-list-cleancreatives-org) */
  --fl-yellow: #EDCC4B; /* Color / Atmospheric Token (f-list-cleancreatives-org) */
  --fl-green: #5DA279; /* Color / Atmospheric Token (f-list-cleancreatives-org) */
  --fl-red: #FF5037; /* Color / Atmospheric Token (f-list-cleancreatives-org) */
  --font-longform-family: "roc-grotesk", sans-serif; /* Typography / Scale Token (f-list-cleancreatives-org) */
  --font-longform-line-height: 165%; /* Typography / Scale Token (f-list-cleancreatives-org) */
  --font-longform-size: 1.25rem; /* Typography / Scale Token (f-list-cleancreatives-org) */
  --font-longform-style: normal; /* Typography / Scale Token (f-list-cleancreatives-org) */
  --font-longform-weight: 400; /* Typography / Scale Token (f-list-cleancreatives-org) */
  --font-longform-weight-bold: 600; /* Typography / Scale Token (f-list-cleancreatives-org) */
  --font-longform-paragraph-margin: 2.125rem 0 0 0; /* Typography / Scale Token (f-list-cleancreatives-org) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#1d1d1d` — grounded in live computed `body` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#edcc4b` — grounded in live computed `footer` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#ffff00` — grounded in `header nav a:hover { color: yellow }` (`#ffff00`)
- **Secondary / Muted Copy**: `#edcc4b` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#f2f2f2` — grounded in `var(--cmplz_banner_border_color)` in `:root`
- **Variable Token (`--fl-grey-1`)**: `#cacaca` — grounded in `var(--fl-grey-1)` in `:root`
- **Variable Token (`--fl-grey-2`)**: `#7d7d7d` — grounded in `var(--fl-grey-2)` in `:root`
- **Variable Token (`--fl-cream`)**: `#eceae3` — grounded in `var(--fl-cream)` in `:root`
- **Variable Token (`--fl-green`)**: `#5da279` — grounded in `var(--fl-green)` in `:root`
- **Variable Token (`--fl-red`)**: `#ff5037` — grounded in `var(--fl-red)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1472px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `7px` lateral canvas padding with `.75rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1472px`, `gap: .75rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `7px` horizontal padding
- **Media Queries**: `@media (max-width: 479px)`, `@media (min-width: 769px)`, `@media (min-width: 480px)`, `@media (min-width: 1701px)`
- **Corner Radii**: `5.008px`, `2px`, `3px`, `.313rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `roc-grotesk-compressed`
- **Body Font Stack**: `roc-grotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 132.951px`, `line-height: 99.7133px`, `font-weight: 700`); rule `,.h1` (`font-size: 4.5rem`)
- **H2 Section Rule**: live computed `h2` (`font-size: 86.1638px`, `line-height: 73.2393px`, `font-weight: 600`); rule `h2` (`font-size: 17px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-longform-paragraph-margin: 2.125rem 0 0 0`, `--cmplz_category_body_font_size: 12px`; rule `p` (`font-size: 16px`, `line-height: 24px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `small` (`line-height: 100%`, `font-weight: 300`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `f-list-cleancreatives-org` (`F-List 2026`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.browser-chrome> — `f-list-cleancreatives-org`)**:
   - DOM & Selectors: Landmark `<header class="browser-chrome">` (`1440x95px`) hosting `F-List 2026` navigation (`The report · The F-List · Dirty work · Take Action`), DOM attributes (`data-cmplz="1"`, `data-nosnippet="true"`, `data-prefix="fas"`, `data-icon="times"`), and stylesheet rule `opular_post_widget .icon-comment:... { content: "\e900"; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.browser-chrome> — `f-list-cleancreatives-org`)` (`f-list-cleancreatives-org`) adapts across `@media (max-width: 479px)`, `@media (min-width: 769px)`, `@media (min-width: 480px)`, `@media (min-width: 1701px)` with `cubic-bezier(0.4,0,0.2,1)` transitions and links `The report · The F-List · Dirty work · Take Action`.
2. **Hero Stage & Focal Lead (<section.hero> — `THE CREATIVE COVER-UP`)**:
   - DOM & Selectors: Landmark `<section class="hero home">` presenting display lead `THE CREATIVE COVER-UP` and copy excerpt *"The agencies providing cover for the fossil fuel industry."* over `#ffffff` canvas and `#1d1d1d` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#1d1d1d` headline `THE CREATIVE COVER-UP`.
3. **Primary Showcase & Content Grid (<section.call-intro> — `The Creative Cover-up`)**:
   - DOM & Selectors: Landmark `<section class="call-intro flex">` rendering section `The Creative Cover-up` with copy *"Functional Always active"*, asset references (`xmlrpc.php`, `www.googletagmanager.com`, `flist2026.b-cdn.net`, `embed`), and grid rule `s_popular_post_widget .icon-chat:... { content: "\e900"; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.call-intro> — `The Creative Cover-up`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1472px`, `gap: .75rem`) on desktop and Single-column vertical stack at `390px` viewport width with `7px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.redacted> — `Functional Always active`)**:
   - DOM & Selectors: Landmark `<section class="redacted bg-cream">` framing `Functional Always active` and `The technical storage or access is strictly nece` (*"The technical storage or access is strictly necessary for the leg"*) with `#edcc4b` surface cards, `#ffff00` accents, and `s_popular_post_widget .icon-talk:... { content: "\e900"; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.redacted> — `Functional Always active`)` uses `5.008px`, `2px`, `3px`, `.313rem` radii, `#ffff00` highlights, and assets (xmlrpc.php, www.googletagmanager.com, flist2026.b-cdn.net).
5. **Colophon & Global Directory Footer (<footer.page-template> — `https://f-list.cleancreatives.org/`)**:
   - DOM & Selectors: Landmark `<footer class="page-template">` anchoring `F-List 2026` footer links (`The report · The F-List · Dirty work · Take Action`), copy *"The technical storage or access is necessary for the legitim"*, and `#f2f2f2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.page-template> — `https://f-list.cleancreatives.org/`)` aligns to `1472px` (non-`@media` desktop container stylesheet rule) with `7px` lateral canvas padding with `.75rem` grid gap and attributes (data-cmplz="1", data-nosnippet="true", data-prefix="fas").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"The agencies providing cover for the fossil fuel industry."*
- Copy Excerpt 2: *"Functional Always active"*
- Copy Excerpt 3: *"The technical storage or access is strictly necessary for the legitimate purpose o..."*
- Copy Excerpt 4: *"The technical storage or access is necessary for the legitimate purpose of storing..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.4,0,0.2,1)`
- **Extracted Stylesheet Rules (`f-list-cleancreatives-org`)**:
- `opular_post_widget .icon-comment:... { content: "\e900"; }`
- `s_popular_post_widget .icon-chat:... { content: "\e900"; }`
- `s_popular_post_widget .icon-talk:... { content: "\e900"; }`
- `popular_post_widget .icon-bubble:... { content: "\e900"; }`
- `popular_post_widget .icon-folder:... { content: "\e92f"; }`
- **Per-Selector Transition Rules**:
- **Selector `popular_post_widget .template-4 l...`**: `transition: -webkit-transform 0.35s` extracted from `f-list-cleancreatives-org` stylesheet.
- **Selector `tics_popular_post_widget .templat...`**: `transition: -webkit-transform 0.35s` extracted from `f-list-cleancreatives-org` stylesheet.
- **Selector `r_post_widget .template-4 li p.ic...`**: `transition: -webkit-transform 0.35s` extracted from `f-list-cleancreatives-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.2,1)`)**: Governs interactive state transitions across `<header.browser-chrome>` and `<section.call-intro>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `f-list-cleancreatives-org`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
