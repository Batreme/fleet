---
title: "UI Prompt Blueprint: pankow-band"
date: 2026-11-15
target: "[[overview|pankow-band]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fff7ee` canvas, `#000000` ink, `#ddd` accent)"
---

# UI Design System & Master Generation Blueprint: pankow-band

> **Die Pankow Zeitmaschine - Website der Berliner Rockband PANKOW** (https://pankow.band) — Die PANKOW Zeitmaschine ist die Band-Website der Rolling Stones des Ostens mit Diskografie, Videos, Chronik, Fangeschichten und Bildern a...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/pankow-band/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Die Pankow Zeitmaschine - Website der Berliner Rockband PANKOW** (`https://pankow.band`). Die PANKOW Zeitmaschine ist die Band-Website der Rolling Stones des Ostens mit Diskografie, Videos, Chronik, Fangeschichten und Bildern a...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fff7ee` canvas, `#000000` ink, `#ddd` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff7ee` (`var(--farbe-schrift-auf-dunkel)` in `:root`) paired with `#000000` primary typography and `#ddd` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Rowdies` for display copy (`Die Pankow-Zeitmaschine`) with `Poppins` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `90%` container bounds (`gap: 0.5rem`, padding `0.75rem`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/pankow-band/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `90%` extracted from `pankow-band` stylesheet.
- **Canvas Lateral Padding & Spacing**: `0.75rem` lateral canvas padding with `0.5rem` grid gap.
- **Border Radius Scale**: `5px`, `12px`, `10px`, `0.25rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 90%`, `gap: 0.5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `0.75rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-height: 52rem)`, `@media (max-width: 600px)`, `@media (prefers-reduced-motion: reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff7ee` | `var(--farbe-schrift-auf-dunkel)` in `:root` |
| **Primary Typography Ink** | `#080808` | `var(--farbe-schrift-auf-hell)` in `:root` |
| **Elevated Surface / Card Substrate** | `#B82608` | `var(--farbe-fokus)` in `:root` |
| **Interactive Accent / Highlight** | `#ddd` | `var(--zeitmaschine-card-border)` in `:root` |
| **Secondary / Muted Copy** | `#000000` | `html { background: black }` (`#000000`) |
| **Structural Hairline Border** | `#BA0108` | `.section-title-h2 { background-color: #BA0108 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--farbe-schrift-auf-dunkel` | `#fff7ee` | Color / Atmospheric Token |
| `--farbe-schrift-auf-hell` | `#080808` | Color / Atmospheric Token |
| `--farbe-link` | `rgba(181, 47, 14, 0.7)` | Typography Ink Token |
| `--farbe-link-auf-dunkel` | `rgb(185, 93, 71)` | Typography Ink Token |
| `--farbe-fokus` | `#B82608` | Color / Atmospheric Token |
| `--farbe-headline` | `rgba(181, 47, 14, 0.8)` | Color / Atmospheric Token |
| `--zeitmaschine-card-passive-mehr-bg` | `rgba(255, 255, 255, 0.3)` | Canvas / Surface Token |
| `--zeitmaschine-card-active-mehr-bg` | `rgba(181, 47, 14, 0.3)` | Canvas / Surface Token |
| `--overlay-article-bg` | `rgba(181, 47, 14, 0.2)` | Canvas / Surface Token |
| `--overlay-nav-elemente-color-lightbg` | `rgba(181, 47, 14, 0.6)` | Canvas / Surface Token |
| `--overlay-nav-elemente-color-darkbg` | `rgba(246, 100, 64, 0.4)` | Canvas / Surface Token |
| `--zeitmaschine-card-border` | `#ddd` | Elevation / Border Token |
| `--zeitmaschine-card-active-weniger-bg` | `url("../bgs/zeitmaschine/pankow-card-bg-weniger-active.jpg")` | Canvas / Surface Token |
| `--zeitmaschine-card-passive-weniger-bg` | `url("../bgs/zeitmaschine/pankow-card-bg-weniger-passive.jpg")` | Canvas / Surface Token |
| `--menu-width-closed` | `6rem` | Layout / Spatial Grid Token |
| `--menu-width-open` | `400px` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Rowdies`.
- **Primary Body Stack**: `Poppins`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(2rem, 5vw, 3rem)`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(1.2rem, 2.2vw, 2rem)`).
- **Body Copy**: rule `p` (`font-size: clamp(1.05rem, 2vw, 1.35rem)`, `line-height: 1.55`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `1.2rem`, `clamp(1.05rem, 2vw, 1.35rem)`, `2rem`, `0.9rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.main-menu-shell`**: `transition: width 0.1s ease 0.5s, height 0.1s ease 0.5s` extracted from `pankow-band` stylesheet.
- **Selector `.main-menu-state:checked+.main-me...`**: `transition: width 0.1s ease, height 0.1s ease, padding 0.1s ease` extracted from `pankow-band` stylesheet.
- **Selector `.main-menu-shell img`**: `transition: opacity 0.4s ease 0.1s` extracted from `pankow-band` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Die Pankow Zeitmaschine - Website der Berl │
│ ====================================================================== │
│ [ <header.font-global>     | Home · Info · Zeitmaschine · Kontakt   ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Die Pankow-Zeitmaschine                                      |   │
│ | Substrate: #fff7ee    | Ink: #000000    | Accent: #ddd           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.info>            ) max-w: 90%            |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Willkommen auf der Website d |  | Deine Technik ist leider zu  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0.5rem) | │
│ | [<header.font-globa] -> [<section.hero>] -> [<section.info>] |       │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.main-menu>    ) | https://pankow.band                │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.font-global> — `pankow-band`)**:
   - Landmark `<header class="font-global">` hosting `Die Pankow Zeitmaschine - Website de` navigation (`Home · Info · Zeitmaschine · Kontakt`), DOM attributes (`data-nav-anchor="main"`, `data-nav-anchor="info"`, `data-nav-anchor="zeitmaschine"`, `data-nav-anchor="kontakt"`), and stylesheet rule `font-palette-values --palette0 { font-family: "pankow-icons"; base-palette: 0; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Die Pankow-Zeitmaschine`)**:
   - Landmark `<section class="hero">` presenting display lead `Die Pankow-Zeitmaschine` and copy excerpt *"Zum Inhalt springen"* over `#fff7ee` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.info> — `Willkommen auf der Website der Ban`)**:
   - Landmark `<section class="info inhalts-section">` rendering section `Willkommen auf der Website der Band PANKOW (1981-...` with copy *"Ich habe mir einen Ort gewünscht, an dem man sich an die Band PAN"*, asset references (`favicon.ico`, `rubik-dirt-v2-latin-regular.woff2`, `pankow-hero-grunge-overlay-unten....`, `major.css`), and grid rule `.palette0 { font-palette: --palette0; color: currentColor; }`.
4. **Interactive Detail & Feature Matrix (<section.zeitmaschine-compat-message> — `Deine Technik ist leider zu alt od`)**:
   - Landmark `<section class="zeitmaschine-compat-message">` framing `Deine Technik ist leider zu alt oder Du lässt kei...` and `ALBEN` (*"Mein Dank geht an Monika Herold von SoulSite Design für die Zusam"*) with `#B82608` surface cards, `#ddd` accents, and `.icon-arrows-vertical:before { content: "\fb85"; }`.
5. **Colophon & Global Directory Footer (<footer.main-menu> — `https://pankow.band`)**:
   - Landmark `<footer class="main-menu">` anchoring `Die Pankow Zeitmaschine - Websit` footer links (`Home · Info · Zeitmaschine · Kontakt`), copy *"Stöbere mit der Zeitmaschine durch die Band-Historie, alle A"*, and `#BA0108` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: pankow-band (Die Pankow Zeitmaschine - Website der Berliner Rockband PANKOW)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `pankow-band` (**Die Pankow Zeitmaschine - Website der Berliner Rockband PANKOW** — `https://pankow.band`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff7ee` canvas, `#000000` ink, `#ddd` accent).
- **Identity & Domain Context**: Die PANKOW Zeitmaschine ist die Band-Website der Rolling Stones des Ostens mit Diskografie, Videos, Chronik, Fangeschichten und Bildern a...
- **Primary Substrate**: `#fff7ee` (`var(--farbe-schrift-auf-dunkel)` in `:root`), **Primary Ink**: `#000000`, **Accent / Highlight**: `#ddd`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff7ee` (`var(--farbe-schrift-auf-dunkel)` in `:root`) paired with `#000000` primary typography and `#ddd` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Rowdies` for display copy (`Die Pankow-Zeitmaschine`) with `Poppins` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `90%` container bounds (`gap: 0.5rem`, padding `0.75rem`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `pankow-band` in your global stylesheet:

:root {
  /* Die Pankow Zeitmaschine - Website der Berliner Rockband PANKOW (pankow-band) — Ground-Truth Extracted CSS Variables */
  --farbe-schrift-auf-dunkel: #fff7ee; /* Color / Atmospheric Token (pankow-band) */
  --farbe-schrift-auf-hell: #080808; /* Color / Atmospheric Token (pankow-band) */
  --farbe-link: rgba(181, 47, 14, 0.7); /* Typography Ink Token (pankow-band) */
  --farbe-link-auf-dunkel: rgb(185, 93, 71); /* Typography Ink Token (pankow-band) */
  --farbe-fokus: #B82608; /* Color / Atmospheric Token (pankow-band) */
  --farbe-headline: rgba(181, 47, 14, 0.8); /* Color / Atmospheric Token (pankow-band) */
  --zeitmaschine-card-passive-mehr-bg: rgba(255, 255, 255, 0.3); /* Canvas / Surface Token (pankow-band) */
  --zeitmaschine-card-active-mehr-bg: rgba(181, 47, 14, 0.3); /* Canvas / Surface Token (pankow-band) */
  --overlay-article-bg: rgba(181, 47, 14, 0.2); /* Canvas / Surface Token (pankow-band) */
  --overlay-nav-elemente-color-lightbg: rgba(181, 47, 14, 0.6); /* Canvas / Surface Token (pankow-band) */
  --overlay-nav-elemente-color-darkbg: rgba(246, 100, 64, 0.4); /* Canvas / Surface Token (pankow-band) */
  --zeitmaschine-card-border: #ddd; /* Elevation / Border Token (pankow-band) */
  --zeitmaschine-card-active-weniger-bg: url("../bgs/zeitmaschine/pankow-card-bg-weniger-active.jpg"); /* Canvas / Surface Token (pankow-band) */
  --zeitmaschine-card-passive-weniger-bg: url("../bgs/zeitmaschine/pankow-card-bg-weniger-passive.jpg"); /* Canvas / Surface Token (pankow-band) */
  --menu-width-closed: 6rem; /* Layout / Spatial Grid Token (pankow-band) */
  --menu-width-open: 400px; /* Layout / Spatial Grid Token (pankow-band) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff7ee` — grounded in `var(--farbe-schrift-auf-dunkel)` in `:root`
- **Primary Typography Ink**: `#080808` — grounded in `var(--farbe-schrift-auf-hell)` in `:root`
- **Elevated Surface / Card Substrate**: `#B82608` — grounded in `var(--farbe-fokus)` in `:root`
- **Interactive Accent / Highlight**: `#ddd` — grounded in `var(--zeitmaschine-card-border)` in `:root`
- **Secondary / Muted Copy**: `#000000` — grounded in `html { background: black }` (`#000000`)
- **Structural Hairline Border**: `#BA0108` — grounded in `.section-title-h2 { background-color: #BA0108 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `90%` extracted from `pankow-band` stylesheet
- **Padding & Gutters**: `0.75rem` lateral canvas padding with `0.5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 90%`, `gap: 0.5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `0.75rem` horizontal padding
- **Media Queries**: `@media (min-height: 52rem)`, `@media (max-width: 600px)`, `@media (prefers-reduced-motion: reduce)`
- **Corner Radii**: `5px`, `12px`, `10px`, `0.25rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Rowdies`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: clamp(2rem, 5vw, 3rem)`)
- **H2 Section Rule**: rule `h2` (`font-size: clamp(1.2rem, 2.2vw, 2rem)`)
- **Body Copy Rule**: rule `p` (`font-size: clamp(1.05rem, 2vw, 1.35rem)`, `line-height: 1.55`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `1.2rem`, `clamp(1.05rem, 2vw, 1.35rem)`, `2rem`, `0.9rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `pankow-band` (`Die Pankow Zeitmaschine - Website der Berliner Rockband PANKOW`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.font-global> — `pankow-band`)**:
   - DOM & Selectors: Landmark `<header class="font-global">` hosting `Die Pankow Zeitmaschine - Website de` navigation (`Home · Info · Zeitmaschine · Kontakt`), DOM attributes (`data-nav-anchor="main"`, `data-nav-anchor="info"`, `data-nav-anchor="zeitmaschine"`, `data-nav-anchor="kontakt"`), and stylesheet rule `font-palette-values --palette0 { font-family: "pankow-icons"; base-palette: 0; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.font-global> — `pankow-band`)` (`pankow-band`) adapts across `@media (min-height: 52rem)`, `@media (max-width: 600px)`, `@media (prefers-reduced-motion: reduce)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Home · Info · Zeitmaschine · Kontakt`.
2. **Hero Stage & Focal Lead (<section.hero> — `Die Pankow-Zeitmaschine`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Die Pankow-Zeitmaschine` and copy excerpt *"Zum Inhalt springen"* over `#fff7ee` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fff7ee` background with `#000000` headline `Die Pankow-Zeitmaschine`.
3. **Primary Showcase & Content Grid (<section.info> — `Willkommen auf der Website der Ban`)**:
   - DOM & Selectors: Landmark `<section class="info inhalts-section">` rendering section `Willkommen auf der Website der Band PANKOW (1981-...` with copy *"Ich habe mir einen Ort gewünscht, an dem man sich an die Band PAN"*, asset references (`favicon.ico`, `rubik-dirt-v2-latin-regular.woff2`, `pankow-hero-grunge-overlay-unten....`, `major.css`), and grid rule `.palette0 { font-palette: --palette0; color: currentColor; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.info> — `Willkommen auf der Website der Ban`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 90%`, `gap: 0.5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `0.75rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.zeitmaschine-compat-message> — `Deine Technik ist leider zu alt od`)**:
   - DOM & Selectors: Landmark `<section class="zeitmaschine-compat-message">` framing `Deine Technik ist leider zu alt oder Du lässt kei...` and `ALBEN` (*"Mein Dank geht an Monika Herold von SoulSite Design für die Zusam"*) with `#B82608` surface cards, `#ddd` accents, and `.icon-arrows-vertical:before { content: "\fb85"; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.zeitmaschine-compat-message> — `Deine Technik ist leider zu alt od`)` uses `5px`, `12px`, `10px`, `0.25rem` radii, `#ddd` highlights, and assets (favicon.ico, rubik-dirt-v2-latin-regular.woff2, pankow-hero-grunge-overlay-unten....).
5. **Colophon & Global Directory Footer (<footer.main-menu> — `https://pankow.band`)**:
   - DOM & Selectors: Landmark `<footer class="main-menu">` anchoring `Die Pankow Zeitmaschine - Websit` footer links (`Home · Info · Zeitmaschine · Kontakt`), copy *"Stöbere mit der Zeitmaschine durch die Band-Historie, alle A"*, and `#BA0108` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.main-menu> — `https://pankow.band`)` aligns to `90%` extracted from `pankow-band` stylesheet with `0.75rem` lateral canvas padding with `0.5rem` grid gap and attributes (data-nav-anchor="main", data-nav-anchor="info", data-nav-anchor="zeitmaschine").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Zum Inhalt springen"*
- Copy Excerpt 2: *"Ich habe mir einen Ort gewünscht, an dem man sich an die Band PANKOW erinnern kann..."*
- Copy Excerpt 3: *"Mein Dank geht an Monika Herold von SoulSite Design für die Zusammenarbeit und fre..."*
- Copy Excerpt 4: *"Stöbere mit der Zeitmaschine durch die Band-Historie, alle Alben und legendäre Liv..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`pankow-band`)**:
- `font-palette-values --palette0 { font-family: "pankow-icons"; base-palette: 0; }`
- `.palette0 { font-palette: --palette0; color: currentColor; }`
- `.icon-arrows-vertical:before { content: "\fb85"; }`
- `.icon-mouse-scroll--fill:before { content: "\101b0"; }`
- `.icon-mouse-scroll--duotone:before { content: "\f83a"; }`
- **Per-Selector Transition Rules**:
- **Selector `.main-menu-shell`**: `transition: width 0.1s ease 0.5s, height 0.1s ease 0.5s` extracted from `pankow-band` stylesheet.
- **Selector `.main-menu-state:checked+.main-me...`**: `transition: width 0.1s ease, height 0.1s ease, padding 0.1s ease` extracted from `pankow-band` stylesheet.
- **Selector `.main-menu-shell img`**: `transition: opacity 0.4s ease 0.1s` extracted from `pankow-band` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `pankow-band`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
