---
title: "UI Prompt Blueprint: www-fixchocolatier-com"
date: 2026-11-15
target: "[[overview|www-fixchocolatier-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#3a1402` / `#000`)"
---

# UI Design System & Master Generation Blueprint: www-fixchocolatier-com

> **FIX Dessert Chocolatier · The Original Dubai Chocolate** (https://www.fixchocolatier.com/) — Discover FIX Dessert Chocolatier, the original Dubai chocolate bar. Shop our viral kunafa, pistachio and pecan bars. Order daily on Careem.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-fixchocolatier-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **FIX Dessert Chocolatier · The Original Dubai Chocolate** (`https://www.fixchocolatier.com/`). Discover FIX Dessert Chocolatier, the original Dubai chocolate bar. Shop our viral kunafa, pistachio and pecan bars. Order daily on Careem.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#3a1402` / `#000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#3a1402` (`var(--bg-color)` in `:root`) paired with `#fff` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `sharpSans` for display copy (`Can’t get Knafeh of it™`) with `sharpSans Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `180px` container bounds (`gap: .25rem`, padding `8px`) with `cubic-bezier(.16,1,.3,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-fixchocolatier-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `180px` extracted from `www-fixchocolatier-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `8px` lateral canvas padding with `.25rem` grid gap.
- **Border Radius Scale**: `.3rem`, `4px`, `50%`, `.3125rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 180px`, `gap: .25rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:400px),(max-height:550px)`, `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:991px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#3a1402` | `var(--bg-color)` in `:root` |
| **Primary Typography Ink** | `#742f3d` | `var(--shadow-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ccc` | `tepicker__month-year-read-view-... { border: #ccc }` |
| **Interactive Accent / Highlight** | `#000` | `.react-datepicker { color: #000 }` |
| **Secondary / Muted Copy** | `#fff` | `.react-datepicker { background-color: #fff }` |
| **Structural Hairline Border** | `#aeaeae` | `.react-datepicker { border: #aeaeae }` |
| **Variable Token (`--hover-bg-color`)** | `#3a140280` | `var(--hover-bg-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sharpsans` | `"sharpSans", "sharpSans Fallback"` | Typography / Scale Token |
| `--font-sydney` | `"sydney", Segoe UI` | Typography / Scale Token |
| `--bg-color` | `#3a1402` | Canvas / Surface Token |
| `--dot-color` | `white` | Brand / Palette Token |
| `--hover-bg-color` | `#3a140280` | Canvas / Surface Token |
| `--inactive-opacity` | `0` | Design System Custom Token |
| `--marquee-duration` | `3s` | Motion / Easing Token |
| `--marquee-easing` | `cubic-bezier(.05,0,.95,1)` | Motion / Easing Token |
| `--shadow-color` | `#742f3d` | Brand / Palette Token |
| `--switch-translate` | `3.99rem` | Dimension / Scale Token |
| `--t-duration` | `2s` | Motion / Easing Token |
| `--original-font-size` | `10px` | Typography / Scale Token |
| `--page-bg` | `rgb(98, 53, 41)` | Canvas / Surface Token |
| `--bg-gradient` | `none` | Canvas / Surface Token |
| `--bg-noise` | `none` | Canvas / Surface Token |
| `--scrim-rgb` | `98, 53, 41` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `sharpSans`.
- **Primary Body Stack**: `sharpSans Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `,.h1` (`font-size: 9rem`, `line-height: 1`, `letter-spacing: 0`, `font-weight: 800`).
- **Section Heading (`H2`)**: rule `,.h2` (`font-size: 6rem`, `line-height: 1`, `letter-spacing: 0`, `font-weight: 800`).
- **Body Copy**: rule `p` (`font-size: 3rem`, `line-height: 1`, `font-weight: 400`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.8rem`, `.944rem`, `20px`, `12px`, `1.44rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `ct-datepicker__year-text--holiday...`**: `transition: visibility,opacity .3s ease-in-out` extracted from `www-fixchocolatier-com` stylesheet.
- **Selector `ct-datepicker__year-text--disable...`**: `transition: visibility,opacity .3s ease-in-out` extracted from `www-fixchocolatier-com` stylesheet.
- **Selector `.transition`**: `transition: .15s` extracted from `www-fixchocolatier-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.pointer-events-none>` and `<main.home-main>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — FIX Dessert Chocolatier · The Original Dub │
│ ====================================================================== │
│ [ <header.pointer-events-n | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.home-main>                                     |   │
│ | H1: Can’t get Knafeh of it™                                      |   │
│ | Substrate: #3a1402    | Ink: #fff       | Accent: #000           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.home-main>          ) max-w: 180px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | CATCH ME IF PECAN            |  | BUTTER TO BE SAFE THAN SALTY | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .25rem) | │
│ | [<header.pointer-ev] -> [<main.home-main>] -> [<main.home-main>] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.fixed>        ) | https://www.fixchocolatier.com/    │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `www-fixchocolatier-com`)**:
   - Landmark `<header class="pointer-events-none absolute">` hosting `FIX Dessert Chocolatier · The Origin` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-engine="three.js r181"`), and stylesheet rule `sans_96245405-module__S_0vUq__cla... { font-family:sharpSans,sharpSans Fallback }`.
2. **Hero Stage & Focal Lead (<main.home-main> — `Can’t get Knafeh of it™`)**:
   - Landmark `<main class="home-main relative">` presenting display lead `Can’t get Knafeh of it™` and copy excerpt *"Collections Hero Bars Midnight Edition Bars Gifting & Sharing Lim"* over `#3a1402` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.home-main> — `CATCH ME IF PECAN`)**:
   - Landmark `<main class="home-main relative">` rendering section `CATCH ME IF PECAN` with copy *"Midnight Edition Bars"*, asset references (`SharpSansNo1_Extrabold-s.p.17c.ux...`, `SharpSansNo1_Semibold-s.p.141-gcw...`, `SydneyAlternate_Regular.p.0-s3cp4...`, `0~ky31xm0y.v6.css`), and grid rule `psans_96245405-module__S_0vUq__va... { --font-sharpsans:"sharpSans", "sharpSans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<main.home-main> — `BUTTER TO BE SAFE THAN SALTY`)**:
   - Landmark `<main class="home-main relative">` framing `BUTTER TO BE SAFE THAN SALTY` and `PICK UP A PRETZEL` (*"Limited Edition Bars"*) with `#ccc` surface cards, `#000` accents, and `dney_ed2b677e-module__XJDjNq__cla... { font-family:sydney,Segoe UI }`.
5. **Colophon & Global Directory Footer (<footer.fixed> — `https://www.fixchocolatier.com/`)**:
   - Landmark `<footer class="fixed">` anchoring `FIX Dessert Chocolatier · The Or` footer links (`Overview · Index · Archive · About · Contact`), copy *"The Original Dubai Chocolate"*, and `#aeaeae` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-fixchocolatier-com (FIX Dessert Chocolatier · The Original Dubai Chocolate)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-fixchocolatier-com` (**FIX Dessert Chocolatier · The Original Dubai Chocolate** — `https://www.fixchocolatier.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#3a1402` / `#000`).
- **Identity & Domain Context**: Discover FIX Dessert Chocolatier, the original Dubai chocolate bar. Shop our viral kunafa, pistachio and pecan bars. Order daily on Careem.
- **Primary Substrate**: `#3a1402` (`var(--bg-color)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#3a1402` (`var(--bg-color)` in `:root`) paired with `#fff` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `sharpSans` for display copy (`Can’t get Knafeh of it™`) with `sharpSans Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `180px` container bounds (`gap: .25rem`, padding `8px`) with `cubic-bezier(.16,1,.3,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-fixchocolatier-com` in your global stylesheet:

:root {
  /* FIX Dessert Chocolatier · The Original Dubai Chocolate (www-fixchocolatier-com) — Ground-Truth Extracted CSS Variables */
  --font-sharpsans: "sharpSans", "sharpSans Fallback"; /* Typography / Scale Token (www-fixchocolatier-com) */
  --font-sydney: "sydney", Segoe UI; /* Typography / Scale Token (www-fixchocolatier-com) */
  --bg-color: #3a1402; /* Canvas / Surface Token (www-fixchocolatier-com) */
  --dot-color: white; /* Brand / Palette Token (www-fixchocolatier-com) */
  --hover-bg-color: #3a140280; /* Canvas / Surface Token (www-fixchocolatier-com) */
  --inactive-opacity: 0; /* Design System Custom Token (www-fixchocolatier-com) */
  --marquee-duration: 3s; /* Motion / Easing Token (www-fixchocolatier-com) */
  --marquee-easing: cubic-bezier(.05,0,.95,1); /* Motion / Easing Token (www-fixchocolatier-com) */
  --shadow-color: #742f3d; /* Brand / Palette Token (www-fixchocolatier-com) */
  --switch-translate: 3.99rem; /* Dimension / Scale Token (www-fixchocolatier-com) */
  --t-duration: 2s; /* Motion / Easing Token (www-fixchocolatier-com) */
  --original-font-size: 10px; /* Typography / Scale Token (www-fixchocolatier-com) */
  --page-bg: rgb(98, 53, 41); /* Canvas / Surface Token (www-fixchocolatier-com) */
  --bg-gradient: none; /* Canvas / Surface Token (www-fixchocolatier-com) */
  --bg-noise: none; /* Canvas / Surface Token (www-fixchocolatier-com) */
  --scrim-rgb: 98, 53, 41; /* Design System Custom Token (www-fixchocolatier-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#3a1402` — grounded in `var(--bg-color)` in `:root`
- **Primary Typography Ink**: `#742f3d` — grounded in `var(--shadow-color)` in `:root`
- **Elevated Surface / Card Substrate**: `#ccc` — grounded in `tepicker__month-year-read-view-... { border: #ccc }`
- **Interactive Accent / Highlight**: `#000` — grounded in `.react-datepicker { color: #000 }`
- **Secondary / Muted Copy**: `#fff` — grounded in `.react-datepicker { background-color: #fff }`
- **Structural Hairline Border**: `#aeaeae` — grounded in `.react-datepicker { border: #aeaeae }`
- **Variable Token (`--hover-bg-color`)**: `#3a140280` — grounded in `var(--hover-bg-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `180px` extracted from `www-fixchocolatier-com` stylesheet
- **Padding & Gutters**: `8px` lateral canvas padding with `.25rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 180px`, `gap: .25rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding
- **Media Queries**: `@media (max-width:400px),(max-height:550px)`, `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:991px)`
- **Corner Radii**: `.3rem`, `4px`, `50%`, `.3125rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `sharpSans`
- **Body Font Stack**: `sharpSans Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: rule `,.h1` (`font-size: 9rem`, `line-height: 1`, `letter-spacing: 0`, `font-weight: 800`)
- **H2 Section Rule**: rule `,.h2` (`font-size: 6rem`, `line-height: 1`, `letter-spacing: 0`, `font-weight: 800`)
- **Body Copy Rule**: rule `p` (`font-size: 3rem`, `line-height: 1`, `font-weight: 400`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.8rem`, `.944rem`, `20px`, `12px`, `1.44rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-fixchocolatier-com` (`FIX Dessert Chocolatier · The Original Dubai Chocolate`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `www-fixchocolatier-com`)**:
   - DOM & Selectors: Landmark `<header class="pointer-events-none absolute">` hosting `FIX Dessert Chocolatier · The Origin` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-engine="three.js r181"`), and stylesheet rule `sans_96245405-module__S_0vUq__cla... { font-family:sharpSans,sharpSans Fallback }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.pointer-events-none> — `www-fixchocolatier-com`)` (`www-fixchocolatier-com`) adapts across `@media (max-width:400px),(max-height:550px)`, `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:991px)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<main.home-main> — `Can’t get Knafeh of it™`)**:
   - DOM & Selectors: Landmark `<main class="home-main relative">` presenting display lead `Can’t get Knafeh of it™` and copy excerpt *"Collections Hero Bars Midnight Edition Bars Gifting & Sharing Lim"* over `#3a1402` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#3a1402` background with `#fff` headline `Can’t get Knafeh of it™`.
3. **Primary Showcase & Content Grid (<main.home-main> — `CATCH ME IF PECAN`)**:
   - DOM & Selectors: Landmark `<main class="home-main relative">` rendering section `CATCH ME IF PECAN` with copy *"Midnight Edition Bars"*, asset references (`SharpSansNo1_Extrabold-s.p.17c.ux...`, `SharpSansNo1_Semibold-s.p.141-gcw...`, `SydneyAlternate_Regular.p.0-s3cp4...`, `0~ky31xm0y.v6.css`), and grid rule `psans_96245405-module__S_0vUq__va... { --font-sharpsans:"sharpSans", "sharpSans Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.home-main> — `CATCH ME IF PECAN`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 180px`, `gap: .25rem`) on desktop and Single-column vertical stack at `390px` viewport width with `8px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.home-main> — `BUTTER TO BE SAFE THAN SALTY`)**:
   - DOM & Selectors: Landmark `<main class="home-main relative">` framing `BUTTER TO BE SAFE THAN SALTY` and `PICK UP A PRETZEL` (*"Limited Edition Bars"*) with `#ccc` surface cards, `#000` accents, and `dney_ed2b677e-module__XJDjNq__cla... { font-family:sydney,Segoe UI }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.home-main> — `BUTTER TO BE SAFE THAN SALTY`)` uses `.3rem`, `4px`, `50%`, `.3125rem` radii, `#000` highlights, and assets (SharpSansNo1_Extrabold-s.p.17c.ux..., SharpSansNo1_Semibold-s.p.141-gcw..., SydneyAlternate_Regular.p.0-s3cp4...).
5. **Colophon & Global Directory Footer (<footer.fixed> — `https://www.fixchocolatier.com/`)**:
   - DOM & Selectors: Landmark `<footer class="fixed">` anchoring `FIX Dessert Chocolatier · The Or` footer links (`Overview · Index · Archive · About · Contact`), copy *"The Original Dubai Chocolate"*, and `#aeaeae` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.fixed> — `https://www.fixchocolatier.com/`)` aligns to `180px` extracted from `www-fixchocolatier-com` stylesheet with `8px` lateral canvas padding with `.25rem` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Collections Hero Bars Midnight Edition Bars Gifting & Sharing Limited Edition Bars"*
- Copy Excerpt 2: *"Midnight Edition Bars"*
- Copy Excerpt 3: *"Limited Edition Bars"*
- Copy Excerpt 4: *"The Original Dubai Chocolate"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-fixchocolatier-com`)**:
- `sans_96245405-module__S_0vUq__cla... { font-family:sharpSans,sharpSans Fallback }`
- `psans_96245405-module__S_0vUq__va... { --font-sharpsans:"sharpSans", "sharpSans Fallback" }`
- `dney_ed2b677e-module__XJDjNq__cla... { font-family:sydney,Segoe UI }`
- `ydney_ed2b677e-module__XJDjNq__va... { --font-sydney:"sydney", Segoe UI }`
- `icker__month-year-read-view--down... { content:"";border:3px solid ccc;border-width:3px 3px 0 0;width:9px;heigh... }`
- **Per-Selector Transition Rules**:
- **Selector `ct-datepicker__year-text--holiday...`**: `transition: visibility,opacity .3s ease-in-out` extracted from `www-fixchocolatier-com` stylesheet.
- **Selector `ct-datepicker__year-text--disable...`**: `transition: visibility,opacity .3s ease-in-out` extracted from `www-fixchocolatier-com` stylesheet.
- **Selector `.transition`**: `transition: .15s` extracted from `www-fixchocolatier-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.pointer-events-none>` and `<main.home-main>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-fixchocolatier-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
