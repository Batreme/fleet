---
title: "UI Prompt Blueprint: thestudiobyjuliegranger-com"
date: 2026-11-15
target: "[[overview|thestudiobyjuliegranger-com]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#7a00df` canvas, `#FFFDE2` ink, `#006ba1` accent)"
---

# UI Design System & Master Generation Blueprint: thestudiobyjuliegranger-com

> **The Studio by Julie Granger** (https://thestudiobyjuliegranger.com/) — Une méthode unique alliant barre, yoga et renforcement, développée depuis plus de 12 ans et déjà adoptée par des milliers de femmes à tra...

![Desktop Viewport Capture (1440x14258)](file:///root/projects/fleet/wiki/targets/thestudiobyjuliegranger-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **The Studio by Julie Granger** (`https://thestudiobyjuliegranger.com/`). Une méthode unique alliant barre, yoga et renforcement, développée depuis plus de 12 ans et déjà adoptée par des milliers de femmes à tra...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#7a00df` canvas, `#FFFDE2` ink, `#006ba1` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#7a00df` (`var(--wp-block-synced-color)` in `:root`) paired with `#FFFDE2` primary typography and `#006ba1` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Newsreader` for display copy (`Un corps sculpté avec élégance`) with `Open Sans` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `464px` container bounds (`gap: 16px`, padding `30px`) with `cubic-bezier(.25,.46,.45,.94)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/thestudiobyjuliegranger-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×14258px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `464px` extracted from `thestudiobyjuliegranger-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `30px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `10px`, `8px`, `50%`, `1px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 464px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `30px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:768px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1024px)`, `@media (prefers-reduced-motion:reduce)and (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Primary Typography Ink** | `#ddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Elevated Surface / Card Substrate** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Interactive Accent / Highlight** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Secondary / Muted Copy** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Structural Hairline Border** | `#FFFDE2` | `var(--mega-nav-cta-loader-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--gap` | `12px` | Layout / Spatial Grid Token |
| `--clip` | `0` | Design System Custom Token |
| `--radius` | `20px` | Elevation / Border Token |
| `--reviews-slides-per-view` | `1.2` | Design System Custom Token |
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |
| `--wp-admin-theme-color--rgb` | `0,124,186` | Brand / Palette Token |
| `--wp-admin-theme-color-darker-10` | `#006ba1` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-10--rgb` | `0,107,160.5` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20` | `#005a87` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20--rgb` | `0,90,135` | Canvas / Surface Token |
| `--wp-admin-border-width-focus` | `2px` | Layout / Spatial Grid Token |
| `--wp-admin--admin-bar--position-offset` | `var(--wp-admin--admin-bar--height,0px)` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Newsreader`.
- **Primary Body Stack**: `Open Sans`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `20px`, `16px`, `14px`, `28px`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 26px`, `line-height: 1.1`, `font-weight: 400`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `20px`, `16px`, `14px`, `28px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `20px`, `16px`, `14px`, `28px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.645,.045,.355,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.account-auth`**: `transition: .25s cubic-bezier(.25,.46,.45,.94)` extracted from `thestudiobyjuliegranger-com` stylesheet.
- **Selector `.account-auth__container`**: `transition: opacity .25s cubic-bezier(.25,.46,.45,.94),transform .35s cubi...` extracted from `thestudiobyjuliegranger-com` stylesheet.
- **Selector `.account-auth__close`**: `transition: border-color .2s ease,color .2s ease` extracted from `thestudiobyjuliegranger-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,.46,.45,.94)`)**: Governs interactive state transitions across `<header.mega-nav-header>` and `<section.logos>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — The Studio by Julie Granger                │
│ ====================================================================== │
│ [ <header.mega-nav-header> | Connexion · en · Connexion Connexion · ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Un corps sculpté avec élégance                               |   │
│ | Substrate: #7a00df    | Ink: #FFFDE2    | Accent: #006ba1        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.logos>           ) max-w: 464px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Une méthode complète pour sc |  | Barre                        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.mega-nav-h] -> [<section.hero>] -> [<section.logos>] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | https://thestudiobyjuliegranger.co │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.mega-nav-header> — `thestudiobyjuliegranger-com`)**:
   - Landmark `<header class="mega-nav-header">` hosting `The Studio by Julie Granger` navigation (`Connexion · en · Connexion Connexion · Méthode et Résultats`), DOM attributes (`data-legal-modal-bound="true"`, `data-cookie-notice-ready="true"`, `data-cfasync="false"`, `data-pagespeed-no-defer`), and stylesheet rule `.account-auth__backdrop { position:absolute;inset:0;background:rgba(71,64,64,.32);backdrop-filter:... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Un corps sculpté avec élégance`)**:
   - Landmark `<section class="hero hero--home">` presenting display lead `Un corps sculpté avec élégance` and copy excerpt *"Connexion Connexion"* over `#7a00df` canvas and `#FFFDE2` ink.
3. **Primary Showcase & Content Grid (<section.logos> — `Une méthode complète pour sculpter`)**:
   - Landmark `<section class="logos">` rendering section `Une méthode complète pour sculpter le corps` with copy *"E s s a i g r a t u i t"*, asset references (`clarity.js`, `z5quve8kus`, `matomo.js`, `gtm.js`), and grid rule `.account-auth__container--forgot { opacity:1;pointer-events:auto;transform:translateX(0);visibility:visible }`.
4. **Interactive Detail & Feature Matrix (<section.benefits> — `Barre`)**:
   - Landmark `<section class="benefits">` framing `Barre` and `Pilates` (*"Méthode et Résultats"*) with `#007cba` surface cards, `#006ba1` accents, and `.account-auth__inner { width:100%;max-width:464px;margin:auto }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://thestudiobyjuliegranger.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `The Studio by Julie Granger` footer links (`Connexion · en · Connexion Connexion · Méthode et Résultats`), copy *"The Studio par Julie Granger"*, and `#FFFDE2` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: thestudiobyjuliegranger-com (The Studio by Julie Granger)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `thestudiobyjuliegranger-com` (**The Studio by Julie Granger** — `https://thestudiobyjuliegranger.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#7a00df` canvas, `#FFFDE2` ink, `#006ba1` accent).
- **Identity & Domain Context**: Une méthode unique alliant barre, yoga et renforcement, développée depuis plus de 12 ans et déjà adoptée par des milliers de femmes à tra...
- **Primary Substrate**: `#7a00df` (`var(--wp-block-synced-color)` in `:root`), **Primary Ink**: `#FFFDE2`, **Accent / Highlight**: `#006ba1`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#7a00df` (`var(--wp-block-synced-color)` in `:root`) paired with `#FFFDE2` primary typography and `#006ba1` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Newsreader` for display copy (`Un corps sculpté avec élégance`) with `Open Sans` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `464px` container bounds (`gap: 16px`, padding `30px`) with `cubic-bezier(.25,.46,.45,.94)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `thestudiobyjuliegranger-com` in your global stylesheet:

:root {
  /* The Studio by Julie Granger (thestudiobyjuliegranger-com) — Ground-Truth Extracted CSS Variables */
  --gap: 12px; /* Layout / Spatial Grid Token (thestudiobyjuliegranger-com) */
  --clip: 0; /* Design System Custom Token (thestudiobyjuliegranger-com) */
  --radius: 20px; /* Elevation / Border Token (thestudiobyjuliegranger-com) */
  --reviews-slides-per-view: 1.2; /* Design System Custom Token (thestudiobyjuliegranger-com) */
  --wp-block-synced-color: #7a00df; /* Brand / Palette Token (thestudiobyjuliegranger-com) */
  --wp-block-synced-color--rgb: 122,0,223; /* Brand / Palette Token (thestudiobyjuliegranger-com) */
  --wp-bound-block-color: var(--wp-block-synced-color); /* Brand / Palette Token (thestudiobyjuliegranger-com) */
  --wp-editor-canvas-background: #ddd; /* Canvas / Surface Token (thestudiobyjuliegranger-com) */
  --wp-admin-theme-color: #007cba; /* Brand / Palette Token (thestudiobyjuliegranger-com) */
  --wp-admin-theme-color--rgb: 0,124,186; /* Brand / Palette Token (thestudiobyjuliegranger-com) */
  --wp-admin-theme-color-darker-10: #006ba1; /* Canvas / Surface Token (thestudiobyjuliegranger-com) */
  --wp-admin-theme-color-darker-10--rgb: 0,107,160.5; /* Canvas / Surface Token (thestudiobyjuliegranger-com) */
  --wp-admin-theme-color-darker-20: #005a87; /* Canvas / Surface Token (thestudiobyjuliegranger-com) */
  --wp-admin-theme-color-darker-20--rgb: 0,90,135; /* Canvas / Surface Token (thestudiobyjuliegranger-com) */
  --wp-admin-border-width-focus: 2px; /* Layout / Spatial Grid Token (thestudiobyjuliegranger-com) */
  --wp-admin--admin-bar--position-offset: var(--wp-admin--admin-bar--height,0px); /* Dimension / Scale Token (thestudiobyjuliegranger-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#7a00df` — grounded in `var(--wp-block-synced-color)` in `:root`
- **Primary Typography Ink**: `#ddd` — grounded in `var(--wp-editor-canvas-background)` in `:root`
- **Elevated Surface / Card Substrate**: `#007cba` — grounded in `var(--wp-admin-theme-color)` in `:root`
- **Interactive Accent / Highlight**: `#006ba1` — grounded in `var(--wp-admin-theme-color-darker-10)` in `:root`
- **Secondary / Muted Copy**: `#005a87` — grounded in `var(--wp-admin-theme-color-darker-20)` in `:root`
- **Structural Hairline Border**: `#FFFDE2` — grounded in `var(--mega-nav-cta-loader-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×14258px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `464px` extracted from `thestudiobyjuliegranger-com` stylesheet
- **Padding & Gutters**: `30px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 464px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `30px` horizontal padding
- **Media Queries**: `@media (min-width:768px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1024px)`, `@media (prefers-reduced-motion:reduce)and (min-width:768px)`
- **Corner Radii**: `10px`, `8px`, `50%`, `1px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Newsreader`
- **Body Font Stack**: `Open Sans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `20px`, `16px`, `14px`, `28px`)
- **H2 Section Rule**: rule `h2` (`font-size: 26px`, `line-height: 1.1`, `font-weight: 400`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `20px`, `16px`, `14px`, `28px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `20px`, `16px`, `14px`, `28px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `thestudiobyjuliegranger-com` (`The Studio by Julie Granger`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.mega-nav-header> — `thestudiobyjuliegranger-com`)**:
   - DOM & Selectors: Landmark `<header class="mega-nav-header">` hosting `The Studio by Julie Granger` navigation (`Connexion · en · Connexion Connexion · Méthode et Résultats`), DOM attributes (`data-legal-modal-bound="true"`, `data-cookie-notice-ready="true"`, `data-cfasync="false"`, `data-pagespeed-no-defer`), and stylesheet rule `.account-auth__backdrop { position:absolute;inset:0;background:rgba(71,64,64,.32);backdrop-filter:... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.mega-nav-header> — `thestudiobyjuliegranger-com`)` (`thestudiobyjuliegranger-com`) adapts across `@media (min-width:768px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1024px)`, `@media (prefers-reduced-motion:reduce)and (min-width:768px)` with `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.645,.045,.355,1)` transitions and links `Connexion · en · Connexion Connexion · Méthode et Résultats`.
2. **Hero Stage & Focal Lead (<section.hero> — `Un corps sculpté avec élégance`)**:
   - DOM & Selectors: Landmark `<section class="hero hero--home">` presenting display lead `Un corps sculpté avec élégance` and copy excerpt *"Connexion Connexion"* over `#7a00df` canvas and `#FFFDE2` ink.
   - Responsive Contract: Hero stage (`1440×14258px` desktop / `390×2400px` mobile) sets `#7a00df` background with `#FFFDE2` headline `Un corps sculpté avec élégance`.
3. **Primary Showcase & Content Grid (<section.logos> — `Une méthode complète pour sculpter`)**:
   - DOM & Selectors: Landmark `<section class="logos">` rendering section `Une méthode complète pour sculpter le corps` with copy *"E s s a i g r a t u i t"*, asset references (`clarity.js`, `z5quve8kus`, `matomo.js`, `gtm.js`), and grid rule `.account-auth__container--forgot { opacity:1;pointer-events:auto;transform:translateX(0);visibility:visible }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.logos> — `Une méthode complète pour sculpter`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 464px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `30px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.benefits> — `Barre`)**:
   - DOM & Selectors: Landmark `<section class="benefits">` framing `Barre` and `Pilates` (*"Méthode et Résultats"*) with `#007cba` surface cards, `#006ba1` accents, and `.account-auth__inner { width:100%;max-width:464px;margin:auto }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.benefits> — `Barre`)` uses `10px`, `8px`, `50%`, `1px` radii, `#006ba1` highlights, and assets (clarity.js, z5quve8kus, matomo.js).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://thestudiobyjuliegranger.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `The Studio by Julie Granger` footer links (`Connexion · en · Connexion Connexion · Méthode et Résultats`), copy *"The Studio par Julie Granger"*, and `#FFFDE2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://thestudiobyjuliegranger.com/`)` aligns to `464px` extracted from `thestudiobyjuliegranger-com` stylesheet with `30px` lateral canvas padding with `16px` grid gap and attributes (data-legal-modal-bound="true", data-cookie-notice-ready="true", data-cfasync="false").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Connexion Connexion"*
- Copy Excerpt 2: *"E s s a i g r a t u i t"*
- Copy Excerpt 3: *"Méthode et Résultats"*
- Copy Excerpt 4: *"The Studio par Julie Granger"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.645,.045,.355,1)`
- **Extracted Stylesheet Rules (`thestudiobyjuliegranger-com`)**:
- `.account-auth__backdrop { position:absolute;inset:0;background:rgba(71,64,64,.32);backdrop-filter:... }`
- `.account-auth__container--forgot { opacity:1;pointer-events:auto;transform:translateX(0);visibility:visible }`
- `.account-auth__inner { width:100%;max-width:464px;margin:auto }`
- `.account-auth__close svg { width:18px;height:18px }`
- `.account-auth__close:hover { border-color:c77878;color:c77878 }`
- **Per-Selector Transition Rules**:
- **Selector `.account-auth`**: `transition: .25s cubic-bezier(.25,.46,.45,.94)` extracted from `thestudiobyjuliegranger-com` stylesheet.
- **Selector `.account-auth__container`**: `transition: opacity .25s cubic-bezier(.25,.46,.45,.94),transform .35s cubi...` extracted from `thestudiobyjuliegranger-com` stylesheet.
- **Selector `.account-auth__close`**: `transition: border-color .2s ease,color .2s ease` extracted from `thestudiobyjuliegranger-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,.46,.45,.94)`)**: Governs interactive state transitions across `<header.mega-nav-header>` and `<section.logos>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `thestudiobyjuliegranger-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
