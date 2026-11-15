---
title: "UI Prompt Blueprint: www-peryton-film-com"
date: 2026-11-15
target: "[[overview|www-peryton-film-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#eae0d0` / `#0009`)"
---

# UI Design System & Master Generation Blueprint: www-peryton-film-com

> **Werbefilm & Social Ads aus Gießen · Peryton Film** (https://www.peryton-film.com/) — Werbefilme, Imagefilme und Social Ads aus Gießen, von Mittelhessen bis Frankfurt. Über 200 Unternehmen vertrauen Peryton Film. Jetzt Erst...

![Desktop Viewport Capture (1440x24773)](file:///root/projects/fleet/wiki/targets/www-peryton-film-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Werbefilm & Social Ads aus Gießen · Peryton Film** (`https://www.peryton-film.com/`). Werbefilme, Imagefilme und Social Ads aus Gießen, von Mittelhessen bis Frankfurt. Über 200 Unternehmen vertrauen Peryton Film. Jetzt Erst...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#eae0d0` / `#0009`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#eae0d0` (`var(--color-scheme-1--text-light)` in `:root`) paired with `#0009` primary typography and `#0009` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Ppmuseum` for display copy (`Mit Videomarketing vom Geheimtipp zu`) with `Instrumentsans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `100rem` container bounds (`gap: 16px`, padding `1.25rem`) with `cubic-bezier(.215,.61,.355,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-peryton-film-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×24773px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `100rem` extracted from `www-peryton-film-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1.25rem` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `999rem`, `999px`, `0%`, `12.5%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100rem`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.25rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#eae0d0` | `var(--color-scheme-1--text-light)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--_primitives---colors--white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ecc779` | `var(--color-scheme-1--accent)` in `:root` |
| **Interactive Accent / Highlight** | `#0009` | `var(--_primitives---opacity--neutral-darkest-60)` in `:root` |
| **Secondary / Muted Copy** | `#fff9` | `var(--_primitives---opacity--white-60)` in `:root` |
| **Structural Hairline Border** | `#fff6` | `var(--_primitives---opacity--white-40)` in `:root` |
| **Variable Token (`--color-scheme-1--border`)** | `#ffffff73` | `var(--color-scheme-1--border)` in `:root` |
| **Variable Token (`--shadow-border`)** | `#ecc77980` | `var(--shadow-border)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-scheme-1--background-dark` | `var(--color-scheme-1--brand-base)` | Canvas / Surface Token |
| `--_typography---font-styles--body` | `Instrumentsans,Arial,sans-serif` | Typography / Scale Token |
| `--color-scheme-1--text-light` | `#eae0d0` | Canvas / Surface Token |
| `--_typography---font-styles--heading` | `Ppmuseum,Arial,sans-serif` | Typography Ink Token |
| `--color-scheme-1--text-dark` | `var(--color-scheme-1--brand-base)` | Canvas / Surface Token |
| `--_primitives---colors--white` | `#fff` | Canvas / Surface Token |
| `--color-scheme-1--border` | `#ffffff73` | Brand / Palette Token |
| `--color-scheme-1--accent` | `#ecc779` | Brand / Palette Token |
| `--_primitives---colors--neutral-darkest` | `black` | Canvas / Surface Token |
| `--_primitives---opacity--transparent` | `transparent` | Design System Custom Token |
| `--shadow-border` | `#ecc77980` | Elevation / Border Token |
| `--_primitives---opacity--neutral-darkest-60` | `#0009` | Canvas / Surface Token |
| `--_primitives---opacity--white-60` | `#fff9` | Canvas / Surface Token |
| `--_ui-styles---stroke--border-width` | `1px` | Layout / Spatial Grid Token |
| `--_ui-styles---radius--medium` | `1rem` | Elevation / Border Token |
| `--color-scheme-1--foreground` | `var(--_primitives---colors--neutral-lightest)` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Ppmuseum`.
- **Primary Body Stack**: `Instrumentsans`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `4rem`, `3rem`, `2.5rem`, `2rem`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `4rem`, `3rem`, `2.5rem`, `2rem`).
- **Body Copy**: CSS variables `--_typography---font-styles--body: Instrumentsans,Arial,sans-serif`, `--pery-font-body: Instrumentsans, Arial, sans-serif`.
- **Metadata & Navigation Labels**: CSS variables `--_ui-styles---radius--small: .5rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(0.65,0,0.35,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.slider-arrow`**: `transition: all .2s` extracted from `www-peryton-film-com` stylesheet.
- **Selector `.bold-nav__word`**: `transition: all .2s` extracted from `www-peryton-film-com` stylesheet.
- **Selector `.testimonial-wrapper`**: `transition: all .2s` extracted from `www-peryton-film-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.215,.61,.355,1)`)**: Governs interactive state transitions across `<nav.bold-nav-full>` and `<section.main-section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Werbefilm & Social Ads aus Gießen · Peryto │
│ ====================================================================== │
│ [ <nav.bold-nav-full>      | Home · Über Uns · Referenzen · Leistun ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.main-section>                               |   │
│ | H1: Mit Videomarketing vom Geheimtipp zum                        |   │
│ | Substrate: #eae0d0    | Ink: #0009      | Accent: #0009          |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.main-section>    ) max-w: 100rem         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | HYPE                         |  | Videomarketing               | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<nav.bold-nav-full] -> [<section.main-sect] -> [<section.main-sect] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer-wrap>  ) | https://www.peryton-film.com/      │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.bold-nav-full> — `www-peryton-film-com`)**:
   - Landmark `<nav class="bold-nav-full">` hosting `Werbefilm & Social Ads aus Gießen · ` navigation (`Home · Über Uns · Referenzen · Leistungen · Kontakt`), DOM attributes (`data-wf-domain="www.peryton-film.com"`, `data-wf-page="69ef0496c745ba2d70c01ce3"`, `data-wf-site="69ef0495c745ba2d70c01c8a"`, `data-website-id="6378536d-081a-43d7-a7..."`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.main-section> — `Mit Videomarketing vom Geheimtipp `)**:
   - Landmark `<section class="main-section overflow-hidden">` presenting display lead `Mit Videomarketing vom Geheimtipp zum` and copy excerpt *"Antrieb zünden Antrieb zünden"* over `#eae0d0` canvas and `#0009` ink.
3. **Primary Showcase & Content Grid (<section.main-section> — `HYPE`)**:
   - Landmark `<section class="main-section is-mask">` rendering section `HYPE` with copy *"Strategische Werbefilme und Social Ads aus Gießen, von Mittelhess"*, asset references (`cdn.prod.website-files.com`, `peryton-film.shared.c549ade3f.min...`, `peryton-film.69ef0496c745ba2d70c0...`, `69f9d75c7d46e2ad8d6fab7f_logo_fav...`), and grid rule `.lenis.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.main-section> — `Videomarketing`)**:
   - Landmark `<section class="main-section overflow-hidden">` framing `Videomarketing` and `Infrastruktur` (*"Unendliche Möglichkeiten."*) with `#ecc779` surface cards, `#0009` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.footer-wrap> — `https://www.peryton-film.com/`)**:
   - Landmark `<footer class="footer-wrap">` anchoring `Werbefilm & Social Ads aus Gieße` footer links (`Home · Über Uns · Referenzen · Leistungen · Kontakt`), copy *"“Nicht zu vergleichen mit anderen Agenturen & Filmproduktion"*, and `#fff6` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-peryton-film-com (Werbefilm & Social Ads aus Gießen · Peryton Film)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-peryton-film-com` (**Werbefilm & Social Ads aus Gießen · Peryton Film** — `https://www.peryton-film.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#eae0d0` / `#0009`).
- **Identity & Domain Context**: Werbefilme, Imagefilme und Social Ads aus Gießen, von Mittelhessen bis Frankfurt. Über 200 Unternehmen vertrauen Peryton Film. Jetzt Erst...
- **Primary Substrate**: `#eae0d0` (`var(--color-scheme-1--text-light)` in `:root`), **Primary Ink**: `#0009`, **Accent / Highlight**: `#0009`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#eae0d0` (`var(--color-scheme-1--text-light)` in `:root`) paired with `#0009` primary typography and `#0009` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Ppmuseum` for display copy (`Mit Videomarketing vom Geheimtipp zu`) with `Instrumentsans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `100rem` container bounds (`gap: 16px`, padding `1.25rem`) with `cubic-bezier(.215,.61,.355,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-peryton-film-com` in your global stylesheet:

:root {
  /* Werbefilm & Social Ads aus Gießen · Peryton Film (www-peryton-film-com) — Ground-Truth Extracted CSS Variables */
  --color-scheme-1--background-dark: var(--color-scheme-1--brand-base); /* Canvas / Surface Token (www-peryton-film-com) */
  --_typography---font-styles--body: Instrumentsans,Arial,sans-serif; /* Typography / Scale Token (www-peryton-film-com) */
  --color-scheme-1--text-light: #eae0d0; /* Canvas / Surface Token (www-peryton-film-com) */
  --_typography---font-styles--heading: Ppmuseum,Arial,sans-serif; /* Typography Ink Token (www-peryton-film-com) */
  --color-scheme-1--text-dark: var(--color-scheme-1--brand-base); /* Canvas / Surface Token (www-peryton-film-com) */
  --_primitives---colors--white: #fff; /* Canvas / Surface Token (www-peryton-film-com) */
  --color-scheme-1--border: #ffffff73; /* Brand / Palette Token (www-peryton-film-com) */
  --color-scheme-1--accent: #ecc779; /* Brand / Palette Token (www-peryton-film-com) */
  --_primitives---colors--neutral-darkest: black; /* Canvas / Surface Token (www-peryton-film-com) */
  --_primitives---opacity--transparent: transparent; /* Design System Custom Token (www-peryton-film-com) */
  --shadow-border: #ecc77980; /* Elevation / Border Token (www-peryton-film-com) */
  --_primitives---opacity--neutral-darkest-60: #0009; /* Canvas / Surface Token (www-peryton-film-com) */
  --_primitives---opacity--white-60: #fff9; /* Canvas / Surface Token (www-peryton-film-com) */
  --_ui-styles---stroke--border-width: 1px; /* Layout / Spatial Grid Token (www-peryton-film-com) */
  --_ui-styles---radius--medium: 1rem; /* Elevation / Border Token (www-peryton-film-com) */
  --color-scheme-1--foreground: var(--_primitives---colors--neutral-lightest); /* Typography Ink Token (www-peryton-film-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#eae0d0` — grounded in `var(--color-scheme-1--text-light)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--_primitives---colors--white)` in `:root`
- **Elevated Surface / Card Substrate**: `#ecc779` — grounded in `var(--color-scheme-1--accent)` in `:root`
- **Interactive Accent / Highlight**: `#0009` — grounded in `var(--_primitives---opacity--neutral-darkest-60)` in `:root`
- **Secondary / Muted Copy**: `#fff9` — grounded in `var(--_primitives---opacity--white-60)` in `:root`
- **Structural Hairline Border**: `#fff6` — grounded in `var(--_primitives---opacity--white-40)` in `:root`
- **Variable Token (`--color-scheme-1--border`)**: `#ffffff73` — grounded in `var(--color-scheme-1--border)` in `:root`
- **Variable Token (`--shadow-border`)**: `#ecc77980` — grounded in `var(--shadow-border)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×24773px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `100rem` extracted from `www-peryton-film-com` stylesheet
- **Padding & Gutters**: `1.25rem` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100rem`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.25rem` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `999rem`, `999px`, `0%`, `12.5%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Ppmuseum`
- **Body Font Stack**: `Instrumentsans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `4rem`, `3rem`, `2.5rem`, `2rem`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `4rem`, `3rem`, `2.5rem`, `2rem`)
- **Body Copy Rule**: CSS variables `--_typography---font-styles--body: Instrumentsans,Arial,sans-serif`, `--pery-font-body: Instrumentsans, Arial, sans-serif`
- **Metadata & Index Rule**: CSS variables `--_ui-styles---radius--small: .5rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-peryton-film-com` (`Werbefilm & Social Ads aus Gießen · Peryton Film`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.bold-nav-full> — `www-peryton-film-com`)**:
   - DOM & Selectors: Landmark `<nav class="bold-nav-full">` hosting `Werbefilm & Social Ads aus Gießen · ` navigation (`Home · Über Uns · Referenzen · Leistungen · Kontakt`), DOM attributes (`data-wf-domain="www.peryton-film.com"`, `data-wf-page="69ef0496c745ba2d70c01ce3"`, `data-wf-site="69ef0495c745ba2d70c01c8a"`, `data-website-id="6378536d-081a-43d7-a7..."`), and stylesheet rule `html.lenis body { height:auto }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.bold-nav-full> — `www-peryton-film-com`)` (`www-peryton-film-com`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(0.65,0,0.35,1)` transitions and links `Home · Über Uns · Referenzen · Leistungen · Kontakt`.
2. **Hero Stage & Focal Lead (<section.main-section> — `Mit Videomarketing vom Geheimtipp `)**:
   - DOM & Selectors: Landmark `<section class="main-section overflow-hidden">` presenting display lead `Mit Videomarketing vom Geheimtipp zum` and copy excerpt *"Antrieb zünden Antrieb zünden"* over `#eae0d0` canvas and `#0009` ink.
   - Responsive Contract: Hero stage (`1440×24773px` desktop / `390×2400px` mobile) sets `#eae0d0` background with `#0009` headline `Mit Videomarketing vom Geheimtipp zum`.
3. **Primary Showcase & Content Grid (<section.main-section> — `HYPE`)**:
   - DOM & Selectors: Landmark `<section class="main-section is-mask">` rendering section `HYPE` with copy *"Strategische Werbefilme und Social Ads aus Gießen, von Mittelhess"*, asset references (`cdn.prod.website-files.com`, `peryton-film.shared.c549ade3f.min...`, `peryton-film.69ef0496c745ba2d70c0...`, `69f9d75c7d46e2ad8d6fab7f_logo_fav...`), and grid rule `.lenis.lenis-stopped { overflow:clip }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.main-section> — `HYPE`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100rem`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `1.25rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.main-section> — `Videomarketing`)**:
   - DOM & Selectors: Landmark `<section class="main-section overflow-hidden">` framing `Videomarketing` and `Infrastruktur` (*"Unendliche Möglichkeiten."*) with `#ecc779` surface cards, `#0009` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.main-section> — `Videomarketing`)` uses `999rem`, `999px`, `0%`, `12.5%` radii, `#0009` highlights, and assets (cdn.prod.website-files.com, peryton-film.shared.c549ade3f.min..., peryton-film.69ef0496c745ba2d70c0...).
5. **Colophon & Global Directory Footer (<footer.footer-wrap> — `https://www.peryton-film.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer-wrap">` anchoring `Werbefilm & Social Ads aus Gieße` footer links (`Home · Über Uns · Referenzen · Leistungen · Kontakt`), copy *"“Nicht zu vergleichen mit anderen Agenturen & Filmproduktion"*, and `#fff6` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer-wrap> — `https://www.peryton-film.com/`)` aligns to `100rem` extracted from `www-peryton-film-com` stylesheet with `1.25rem` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.peryton-film.com", data-wf-page="69ef0496c745ba2d70c01ce3", data-wf-site="69ef0495c745ba2d70c01c8a").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Antrieb zünden Antrieb zünden"*
- Copy Excerpt 2: *"Strategische Werbefilme und Social Ads aus Gießen, von Mittelhessen bis Frankfurt...."*
- Copy Excerpt 3: *"Unendliche Möglichkeiten."*
- Copy Excerpt 4: *"“Nicht zu vergleichen mit anderen Agenturen & Filmproduktionen...” Anja Löwe Press..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(0.65,0,0.35,1)`
- **Extracted Stylesheet Rules (`www-peryton-film-com`)**:
- `html.lenis body { height:auto }`
- `.lenis.lenis-stopped { overflow:clip }`
- `.lenis.lenis-smooth iframe { pointer-events:none }`
- `img { max-width:100%;display:inline-block }`
- `label { margin-bottom:.25rem;font-weight:500 }`
- **Per-Selector Transition Rules**:
- **Selector `.slider-arrow`**: `transition: all .2s` extracted from `www-peryton-film-com` stylesheet.
- **Selector `.bold-nav__word`**: `transition: all .2s` extracted from `www-peryton-film-com` stylesheet.
- **Selector `.testimonial-wrapper`**: `transition: all .2s` extracted from `www-peryton-film-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.215,.61,.355,1)`)**: Governs interactive state transitions across `<nav.bold-nav-full>` and `<section.main-section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-peryton-film-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
