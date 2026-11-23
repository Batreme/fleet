---
title: "UI Prompt Blueprint: www-quintadamalia-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-quintadamalia-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1e1e1e` ink, `#007fff` accent)"
---

# UI Design System & Master Generation Blueprint: www-quintadamalia-com

> **Quinta D. Amália - Redefining Luxury Living in Portugal** (https://www.quintadamalia.com/) — Set in the heart of Vila Nova de Gaia, Quinta D. Amália is more than a residence - it’s a lifestyle defined by exclusivity, wellness & na...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Quinta D. Amália - Redefining Luxury Living in Portugal** (`https://www.quintadamalia.com/`). Set in the heart of Vila Nova de Gaia, Quinta D. Amália is more than a residence - it’s a lifestyle defined by exclusivity, wellness & na...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1e1e1e` ink, `#007fff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1e1e1e` primary typography and `#007fff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Marcellus` for display copy (`Where luxury meets serenity`) with `Syne` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1870px` container bounds (`gap: 1rem`, padding `57.6px`) with `cubic-bezier(.28,.84,.42,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1870px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `57.6px` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `999px`, `100px`, `50%`, `0.375rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1870px`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `57.6px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:800px) and (orientation:landscape),...`, `@media all and (max-width:900px)`, `@media (prefers-reduced-motion:no-preference)`, `@media (min-width:1200px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1e1e1e` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f5f7f5` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#007fff` | `a.ui-button:active { background: #007fff }` |
| **Secondary / Muted Copy** | `#7a7a7a` | `var(--e-global-color-text)` in `:root` |
| **Structural Hairline Border** | `#9ec5fe` | `var(--bs-primary-border-subtle)` in `:root` |
| **Variable Token (`--bs-blue`)** | `#0d6efd` | `var(--bs-blue)` in `:root` |
| **Variable Token (`--bs-indigo`)** | `#6610f2` | `var(--bs-indigo)` in `:root` |
| **Variable Token (`--bs-purple`)** | `#6f42c1` | `var(--bs-purple)` in `:root` |
| **Variable Token (`--bs-pink`)** | `#d63384` | `var(--bs-pink)` in `:root` |
| **Variable Token (`--bs-red`)** | `#dc3545` | `var(--bs-red)` in `:root` |
| **Variable Token (`--bs-orange`)** | `#fd7e14` | `var(--bs-orange)` in `:root` |
| **Variable Token (`--bs-yellow`)** | `#ffc107` | `var(--bs-yellow)` in `:root` |
| **Variable Token (`--bs-green`)** | `#198754` | `var(--bs-green)` in `:root` |
| **Variable Token (`--bs-teal`)** | `#20c997` | `var(--bs-teal)` in `:root` |
| **Variable Token (`--bs-cyan`)** | `#0dcaf0` | `var(--bs-cyan)` in `:root` |
| **Variable Token (`--bs-black`)** | `#000000` | `var(--bs-black)` in `:root` |
| **Variable Token (`--bs-gray`)** | `#6c757d` | `var(--bs-gray)` in `:root` |
| **Variable Token (`--bs-gray-dark`)** | `#343a40` | `var(--bs-gray-dark)` in `:root` |
| **Variable Token (`--bs-gray-100`)** | `#f8f9fa` | `var(--bs-gray-100)` in `:root` |
| **Variable Token (`--bs-gray-200`)** | `#e9ecef` | `var(--bs-gray-200)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bs-blue` | `#0d6efd` | Color / Atmospheric Token |
| `--bs-indigo` | `#6610f2` | Color / Atmospheric Token |
| `--bs-purple` | `#6f42c1` | Color / Atmospheric Token |
| `--bs-pink` | `#d63384` | Typography Ink Token |
| `--bs-red` | `#dc3545` | Color / Atmospheric Token |
| `--bs-orange` | `#fd7e14` | Color / Atmospheric Token |
| `--bs-yellow` | `#ffc107` | Color / Atmospheric Token |
| `--bs-green` | `#198754` | Color / Atmospheric Token |
| `--bs-teal` | `#20c997` | Color / Atmospheric Token |
| `--bs-cyan` | `#0dcaf0` | Color / Atmospheric Token |
| `--bs-black` | `#000` | Canvas / Surface Token |
| `--bs-white` | `#fff` | Canvas / Surface Token |
| `--bs-gray` | `#6c757d` | Color / Atmospheric Token |
| `--bs-gray-dark` | `#343a40` | Canvas / Surface Token |
| `--bs-gray-100` | `#f8f9fa` | Color / Atmospheric Token |
| `--bs-gray-200` | `#e9ecef` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Marcellus`.
- **Primary Body Stack**: `Syne`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 140px`, `line-height: 140px`, `font-weight: 400`, `letter-spacing: -5.6px`); CSS variables `--page-title-display: block`, `--display: flex`; rule `,h1` (`font-size: calc(1.375rem + 1.5vw)`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 20px`, `line-height: 28px`, `font-weight: 400`); rule `,h2` (`font-size: calc(1.325rem + .9vw)`).
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 26px`, `font-weight: 400`); CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `p` (`font-size: 22px`, `line-height: 1.36`, `letter-spacing: -.02em`, `font-weight: 500`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 26px`, `font-weight: 400`); rule `small` (`font-size: 12px`, `line-height: 14px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.28,.84,.42,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(0.4,0,0.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.themepure-theme-btn`**: `transition: 0.3s` extracted from `www-quintadamalia-com` stylesheet.
- **Selector `.themepure-theme-btn-line-effect:...`**: `transition: 0.4s` extracted from `www-quintadamalia-com` stylesheet.
- **Selector `.tp-pdt-meta-social-btn`**: `transition: 0.3s` extracted from `www-quintadamalia-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.28,.84,.42,1)`)**: Governs interactive state transitions across `<header.qda-header>` and `<div.elementor-385>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Quinta D. Amália - Redefining Luxury Livin │
│ ====================================================================== │
│ [ <header.qda-header> (1440x66px)     | Home · About · Apartments ·  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.elementor> (w=1440px)                             | │
│ | H1: Where luxury meets serenity                                    | │
│ | Substrate: #ffffff | Ink: #1e1e1e | Accent: #007fff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.elementor-385>) max-w: 1870px                  | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Quinta D. Amália is more tha |  | Every residence is a masterp | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<div.elementor:nth(2)>) — With construction beg     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.home>       ) | https://www.quintadamalia.com/       │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.qda-header>     ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<div.elementor>) — 390px Vertical Lead                 | │
│ | H1: Where luxury meets serenity                                    | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<div.elementor-385>) — 1-Col Stack                 | │
│ | [ Item 1: Quinta D. Amália is more than a residence - it’s       ] | │
│ | [ Item 2: Every residence is a masterpiece of craftsmanshi       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<div.elementor:nth(2)>) — 1-Col (With construction ) | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.home>       ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.qda-header> — `www-quintadamalia-com`)**:
   - Landmark `<header class="qda-header is-stuck">` (`1440x66px`) hosting `Quinta D. Amália - Redefining Luxury` navigation (`Home · About · Apartments · Lifestyle · Contact`), DOM attributes (`data-rocket-preload`, `data-wpr-hosted-gf-parameters="family=Big+Shoulders+..."`, `data-wpr-hosted-gf-parameters="family=Big+Shoulders+..."`, `data-wpr-hosted-gf-parameters`), and stylesheet rule `.themepure-theme-btn:hover { background-color:var(--tp-common-white);border-color:var(--tp-common-bla... }`.
2. **Hero Stage & Focal Lead (<div.elementor> — `Where luxury meets serenity`)**:
   - Landmark `<div class="elementor elementor-385">` presenting display lead `Where luxury meets serenity` and copy excerpt *"Quinta D. Amália is more than a residence - it’s a lifestyle defi"* over `#ffffff` canvas and `#1e1e1e` ink.
3. **Primary Showcase & Content Grid (<div.elementor-385> — `Quinta D. Amália is more than a re`)**:
   - Landmark `<div class="elementor elementor-385">` rendering section `Quinta D. Amália is more than a residence - it’s` with copy *"Every residence is a masterpiece of craftsmanship, featuring prem"*, asset references (`0486c33379293b947859233762b05.css`, `8vIH7w4qzmVxm2BL9A.woff2`, `marcellus-weo_ebrok8hqldviaf81vvo...`, `css2`), and grid rule `.themepure-theme-btn span { display:inline-block }`.
4. **Interactive Detail & Feature Matrix (<div.elementor:nth(2)> — `Every residence is a masterpiece o`)**:
   - Landmark `<div class="elementor elementor-385">` framing `Every residence is a masterpiece of craftsmanshi` and `With construction beginning in Q4 2026, Quinta D` (*"With construction beginning in Q4 2026, Quinta D. Amália is poise"*) with `#f5f7f5` surface cards, `#007fff` accents, and `.themepure-theme-btn img { object-fit:cover }`.
5. **Colophon & Global Directory Footer (<footer.home> — `https://www.quintadamalia.com/`)**:
   - Landmark `<footer class="home">` anchoring `Quinta D. Amália - Redefining Lu` footer links (`Home · About · Apartments · Lifestyle · Contact`), copy *"Elegant Simplicity"*, and `#9ec5fe` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-quintadamalia-com (Quinta D. Amália - Redefining Luxury Living in Portugal)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-quintadamalia-com` (**Quinta D. Amália - Redefining Luxury Living in Portugal** — `https://www.quintadamalia.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1e1e1e` ink, `#007fff` accent).
- **Identity & Domain Context**: Set in the heart of Vila Nova de Gaia, Quinta D. Amália is more than a residence - it’s a lifestyle defined by exclusivity, wellness & na...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#1e1e1e`, **Accent / Highlight**: `#007fff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1e1e1e` primary typography and `#007fff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Marcellus` for display copy (`Where luxury meets serenity`) with `Syne` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1870px` container bounds (`gap: 1rem`, padding `57.6px`) with `cubic-bezier(.28,.84,.42,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-quintadamalia-com` in your global stylesheet:

:root {
  /* Quinta D. Amália - Redefining Luxury Living in Portugal (www-quintadamalia-com) — Live-Grounded CSS Variables */
  --bs-blue: #0d6efd; /* Color / Atmospheric Token (www-quintadamalia-com) */
  --bs-indigo: #6610f2; /* Color / Atmospheric Token (www-quintadamalia-com) */
  --bs-purple: #6f42c1; /* Color / Atmospheric Token (www-quintadamalia-com) */
  --bs-pink: #d63384; /* Typography Ink Token (www-quintadamalia-com) */
  --bs-red: #dc3545; /* Color / Atmospheric Token (www-quintadamalia-com) */
  --bs-orange: #fd7e14; /* Color / Atmospheric Token (www-quintadamalia-com) */
  --bs-yellow: #ffc107; /* Color / Atmospheric Token (www-quintadamalia-com) */
  --bs-green: #198754; /* Color / Atmospheric Token (www-quintadamalia-com) */
  --bs-teal: #20c997; /* Color / Atmospheric Token (www-quintadamalia-com) */
  --bs-cyan: #0dcaf0; /* Color / Atmospheric Token (www-quintadamalia-com) */
  --bs-black: #000; /* Canvas / Surface Token (www-quintadamalia-com) */
  --bs-white: #fff; /* Canvas / Surface Token (www-quintadamalia-com) */
  --bs-gray: #6c757d; /* Color / Atmospheric Token (www-quintadamalia-com) */
  --bs-gray-dark: #343a40; /* Canvas / Surface Token (www-quintadamalia-com) */
  --bs-gray-100: #f8f9fa; /* Color / Atmospheric Token (www-quintadamalia-com) */
  --bs-gray-200: #e9ecef; /* Color / Atmospheric Token (www-quintadamalia-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#1e1e1e` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f5f7f5` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#007fff` — grounded in `a.ui-button:active { background: #007fff }`
- **Secondary / Muted Copy**: `#7a7a7a` — grounded in `var(--e-global-color-text)` in `:root`
- **Structural Hairline Border**: `#9ec5fe` — grounded in `var(--bs-primary-border-subtle)` in `:root`
- **Variable Token (`--bs-blue`)**: `#0d6efd` — grounded in `var(--bs-blue)` in `:root`
- **Variable Token (`--bs-indigo`)**: `#6610f2` — grounded in `var(--bs-indigo)` in `:root`
- **Variable Token (`--bs-purple`)**: `#6f42c1` — grounded in `var(--bs-purple)` in `:root`
- **Variable Token (`--bs-pink`)**: `#d63384` — grounded in `var(--bs-pink)` in `:root`
- **Variable Token (`--bs-red`)**: `#dc3545` — grounded in `var(--bs-red)` in `:root`
- **Variable Token (`--bs-orange`)**: `#fd7e14` — grounded in `var(--bs-orange)` in `:root`
- **Variable Token (`--bs-yellow`)**: `#ffc107` — grounded in `var(--bs-yellow)` in `:root`
- **Variable Token (`--bs-green`)**: `#198754` — grounded in `var(--bs-green)` in `:root`
- **Variable Token (`--bs-teal`)**: `#20c997` — grounded in `var(--bs-teal)` in `:root`
- **Variable Token (`--bs-cyan`)**: `#0dcaf0` — grounded in `var(--bs-cyan)` in `:root`
- **Variable Token (`--bs-black`)**: `#000000` — grounded in `var(--bs-black)` in `:root`
- **Variable Token (`--bs-gray`)**: `#6c757d` — grounded in `var(--bs-gray)` in `:root`
- **Variable Token (`--bs-gray-dark`)**: `#343a40` — grounded in `var(--bs-gray-dark)` in `:root`
- **Variable Token (`--bs-gray-100`)**: `#f8f9fa` — grounded in `var(--bs-gray-100)` in `:root`
- **Variable Token (`--bs-gray-200`)**: `#e9ecef` — grounded in `var(--bs-gray-200)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1870px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `57.6px` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1870px`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `57.6px` horizontal padding
- **Media Queries**: `@media screen and (max-width:800px) and (orientation:landscape),...`, `@media all and (max-width:900px)`, `@media (prefers-reduced-motion:no-preference)`, `@media (min-width:1200px)`
- **Corner Radii**: `999px`, `100px`, `50%`, `0.375rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Marcellus`
- **Body Font Stack**: `Syne`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 140px`, `line-height: 140px`, `font-weight: 400`, `letter-spacing: -5.6px`); CSS variables `--page-title-display: block`, `--display: flex`; rule `,h1` (`font-size: calc(1.375rem + 1.5vw)`)
- **H2 Section Rule**: live computed `h2` (`font-size: 20px`, `line-height: 28px`, `font-weight: 400`); rule `,h2` (`font-size: calc(1.325rem + .9vw)`)
- **Body Copy Rule**: live computed `body` (`font-size: 14px`, `line-height: 26px`, `font-weight: 400`); CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `p` (`font-size: 22px`, `line-height: 1.36`, `letter-spacing: -.02em`, `font-weight: 500`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 14px`, `line-height: 26px`, `font-weight: 400`); rule `small` (`font-size: 12px`, `line-height: 14px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-quintadamalia-com` (`Quinta D. Amália - Redefining Luxury Living in Portugal`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.qda-header> — `www-quintadamalia-com`)**:
   - DOM & Selectors: Landmark `<header class="qda-header is-stuck">` (`1440x66px`) hosting `Quinta D. Amália - Redefining Luxury` navigation (`Home · About · Apartments · Lifestyle · Contact`), DOM attributes (`data-rocket-preload`, `data-wpr-hosted-gf-parameters="family=Big+Shoulders+..."`, `data-wpr-hosted-gf-parameters="family=Big+Shoulders+..."`, `data-wpr-hosted-gf-parameters`), and stylesheet rule `.themepure-theme-btn:hover { background-color:var(--tp-common-white);border-color:var(--tp-common-bla... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.qda-header> — `www-quintadamalia-com`)` (`www-quintadamalia-com`) adapts across `@media screen and (max-width:800px) and (orientation:landscape),...`, `@media all and (max-width:900px)`, `@media (prefers-reduced-motion:no-preference)`, `@media (min-width:1200px)` with `cubic-bezier(.28,.84,.42,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(0.4,0,0.2,1)` transitions and links `Home · About · Apartments · Lifestyle · Contact`.
2. **Hero Stage & Focal Lead (<div.elementor> — `Where luxury meets serenity`)**:
   - DOM & Selectors: Landmark `<div class="elementor elementor-385">` presenting display lead `Where luxury meets serenity` and copy excerpt *"Quinta D. Amália is more than a residence - it’s a lifestyle defi"* over `#ffffff` canvas and `#1e1e1e` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#1e1e1e` headline `Where luxury meets serenity`.
3. **Primary Showcase & Content Grid (<div.elementor-385> — `Quinta D. Amália is more than a re`)**:
   - DOM & Selectors: Landmark `<div class="elementor elementor-385">` rendering section `Quinta D. Amália is more than a residence - it’s` with copy *"Every residence is a masterpiece of craftsmanship, featuring prem"*, asset references (`0486c33379293b947859233762b05.css`, `8vIH7w4qzmVxm2BL9A.woff2`, `marcellus-weo_ebrok8hqldviaf81vvo...`, `css2`), and grid rule `.themepure-theme-btn span { display:inline-block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.elementor-385> — `Quinta D. Amália is more than a re`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1870px`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `57.6px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.elementor:nth(2)> — `Every residence is a masterpiece o`)**:
   - DOM & Selectors: Landmark `<div class="elementor elementor-385">` framing `Every residence is a masterpiece of craftsmanshi` and `With construction beginning in Q4 2026, Quinta D` (*"With construction beginning in Q4 2026, Quinta D. Amália is poise"*) with `#f5f7f5` surface cards, `#007fff` accents, and `.themepure-theme-btn img { object-fit:cover }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.elementor:nth(2)> — `Every residence is a masterpiece o`)` uses `999px`, `100px`, `50%`, `0.375rem` radii, `#007fff` highlights, and assets (0486c33379293b947859233762b05.css, 8vIH7w4qzmVxm2BL9A.woff2, marcellus-weo_ebrok8hqldviaf81vvo...).
5. **Colophon & Global Directory Footer (<footer.home> — `https://www.quintadamalia.com/`)**:
   - DOM & Selectors: Landmark `<footer class="home">` anchoring `Quinta D. Amália - Redefining Lu` footer links (`Home · About · Apartments · Lifestyle · Contact`), copy *"Elegant Simplicity"*, and `#9ec5fe` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.home> — `https://www.quintadamalia.com/`)` aligns to `1870px` (non-`@media` desktop container stylesheet rule) with `57.6px` lateral canvas padding with `1rem` grid gap and attributes (data-rocket-preload, data-wpr-hosted-gf-parameters="family=Big+Shoulders+...", data-wpr-hosted-gf-parameters="family=Big+Shoulders+...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Quinta D. Amália is more than a residence - it’s a lifestyle defined by exclusivit..."*
- Copy Excerpt 2: *"Every residence is a masterpiece of craftsmanship, featuring premium materials lik..."*
- Copy Excerpt 3: *"With construction beginning in Q4 2026, Quinta D. Amália is poised to become the r..."*
- Copy Excerpt 4: *"Elegant Simplicity"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.28,.84,.42,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(0.4,0,0.2,1)`
- **Extracted Stylesheet Rules (`www-quintadamalia-com`)**:
- `.themepure-theme-btn:hover { background-color:var(--tp-common-white);border-color:var(--tp-common-bla... }`
- `.themepure-theme-btn span { display:inline-block }`
- `.themepure-theme-btn img { object-fit:cover }`
- `.themepure-theme-btn-line-effect:... { background-color:fff;color:var(--tp-common-black) }`
- `ure-theme-btn-line-effect:hover::... { right:auto;left:0;width:100% }`
- **Per-Selector Transition Rules**:
- **Selector `.themepure-theme-btn`**: `transition: 0.3s` extracted from `www-quintadamalia-com` stylesheet.
- **Selector `.themepure-theme-btn-line-effect:...`**: `transition: 0.4s` extracted from `www-quintadamalia-com` stylesheet.
- **Selector `.tp-pdt-meta-social-btn`**: `transition: 0.3s` extracted from `www-quintadamalia-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.28,.84,.42,1)`)**: Governs interactive state transitions across `<header.qda-header>` and `<div.elementor-385>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-quintadamalia-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
