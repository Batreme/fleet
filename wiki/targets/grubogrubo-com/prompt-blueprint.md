---
title: "UI Prompt Blueprint: grubogrubo-com"
date: 2026-11-15
target: "grubogrubo-com"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#4c0aaf` / `#bcb8c5`)"
---

# UI Design System & Master Generation Blueprint: grubogrubo-com

> **GruboGrubo — Creative Ideas & Visual Production Studio · Warsaw** (https://grubogrubo.com) — Independent creative studio in Warsaw: creative concepts, campaigns, storytelling, animation, 3D, CGI and interactive experiences.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **GruboGrubo — Creative Ideas & Visual Production Studio · Warsaw** (`https://grubogrubo.com`). Independent creative studio in Warsaw: creative concepts, campaigns, storytelling, animation, 3D, CGI and interactive experiences.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#4c0aaf` / `#bcb8c5`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#4c0aaf` (`var(--acid)` in `:root`) paired with `#ffffff` primary typography and `#bcb8c5` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Arial` for display copy (`IDEA`) with `Arial Black` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `620px` container bounds (`gap: 22px`, padding `8px`) with `cubic-bezier(.19,1,.22,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×10408px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `620px` extracted from `grubogrubo-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `8px` lateral canvas padding with `22px` grid gap.
- **Border Radius Scale**: `40px`, `13px`, `25px`, `24px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 620px`, `gap: 22px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:620px)`, `@media (max-width:750px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1150px) and (max-height:680px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#4c0aaf` | `var(--acid)` in `:root` |
| **Primary Typography Ink** | `#f5f4f0` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#c3a0ec` | `var(--fx-accent)` in `:root` |
| **Interactive Accent / Highlight** | `#bcb8c5` | `.cookie-settings-launcher button { color: #bcb8c5 }` |
| **Secondary / Muted Copy** | `#494551` | `.cookie-settings-launcher button { border: #494551 }` |
| **Structural Hairline Border** | `#ffffff` | `kie-settings-launcher button:fo... { color: white }` (`#ffffff`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--acid` | `#4c0aaf` | Color / Atmospheric Token |
| `--paper` | `#f5f4f0` | Canvas / Surface Token |
| `--violet` | `#4c0aaf` | Color / Atmospheric Token |
| `--accent` | `var(--violet)` | Brand / Palette Token |
| `--fx-accent` | `#c3a0ec` | Brand / Palette Token |
| `--mx` | `50%` | Dimension / Scale Token |
| `--my` | `50%` | Dimension / Scale Token |
| `--reveal-delay` | `0ms` | Motion / Easing Token |
| `--grubogrubo-com-bg` | `#4c0aaf` | Canvas Substrate (from `var(--acid)` in `:root`) |
| `--grubogrubo-com-ink` | `#ffffff` | Primary Typography Ink (stylesheet-derived) |
| `--grubogrubo-com-surface` | `#c3a0ec` | Surface Substrate (stylesheet-derived) |
| `--grubogrubo-com-accent` | `#bcb8c5` | Interactive Accent (stylesheet-derived) |
| `--grubogrubo-com-muted` | `#494551` | Secondary Ink (stylesheet-derived) |
| `--grubogrubo-com-border` | `#ffffff` | Structural Border (stylesheet-derived) |
| `--grubogrubo-com-container` | `620px` | Container Bound (stylesheet-derived) |
| `--grubogrubo-com-gap` | `22px` | Grid Gutter (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Arial`.
- **Primary Body Stack**: `Arial Black`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(33px,3vw,54px)`, `line-height: .89`, `letter-spacing: -.06em`, `font-weight: 800`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(70px,12vw,210px)`, `line-height: .84`, `letter-spacing: -.092em`).
- **Body Copy**: rule `p` (`font-size: 12px`, `line-height: 1.5`).
- **Metadata & Navigation Labels**: rule `nav` (`font-size: 10px`, `letter-spacing: .13em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.17,.84,.18,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.site-header nav a`**: `transition: opacity .2s` extracted from `grubogrubo-com` stylesheet.
- **Selector `.chapter`**: `transition: left .55s ease,right .55s ease,opacity .45s ease` extracted from `grubogrubo-com` stylesheet.
- **Selector `.chapter-enter`**: `transition: background .25s,color .25s,transform .25s` extracted from `grubogrubo-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.19,1,.22,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.about>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — GruboGrubo — Creative Ideas & Visual Produ │
│ ====================================================================== │
│ [ <header.site-header>     | WORK · STUDIO · INSIGHTS · ABOUT US ·  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.intro>                                      |   │
│ | H1: IDEA                                                         |   │
│ | Substrate: #4c0aaf    | Ink: #ffffff    | Accent: #bcb8c5        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.about>           ) max-w: 620px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | WE DON’T THINK SMALL.        |  | THE IDEA COMES FIRST.        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 22px  ) | │
│ | [<header.site-heade] -> [<section.intro>] -> [<section.about>] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.contact>      ) | https://grubogrubo.com             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `grubogrubo-com`)**:
   - Landmark `<header class="site-header">` hosting `GruboGrubo — Creative Ideas & Visual` navigation (`WORK · STUDIO · INSIGHTS · ABOUT US · CONTACT ↗`), DOM attributes (`data-language="en"`, `data-i18n="manifest"`, `data-i18n="navWork"`, `data-i18n="navStudio"`), and stylesheet rule `.cookie-settings-launcher { position:fixed;left:12px;bottom:12px;z-index:40 }`.
2. **Hero Stage & Focal Lead (<section.intro> — `IDEA`)**:
   - Landmark `<section class="intro">` presenting display lead `IDEA` and copy excerpt *"WE TURN COMPLEX THINGS INTO COMPELLING EXPERIENCES."* over `#4c0aaf` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.about> — `WE DON’T THINK SMALL.`)**:
   - Landmark `<section class="about">` rendering section `WE DON’T THINK SMALL.` with copy *"Ideas that shift perspectives. Concepts, campaigns and storytelli"*, asset references (`style.css`, `cookie-consent.css`, `header-logo.png (GRUBO)`, `maciej-scroll.mp4`), and grid rule `settings-launcher button:focus-vi... { opacity:1;background:4c0aaf;color:white }`.
4. **Interactive Detail & Feature Matrix (<section.team> — `THE IDEA COMES FIRST.`)**:
   - Landmark `<section class="team founder-cinematic">` framing `THE IDEA COMES FIRST.` and `Advertising films` (*"INDEPENDENT CREATIVE STUDIO"*) with `#c3a0ec` surface cards, `#bcb8c5` accents, and `.cookie-banner strong { font-size:14px }`.
5. **Colophon & Global Directory Footer (<footer.contact> — `https://grubogrubo.com`)**:
   - Landmark `<footer class="contact">` anchoring `GruboGrubo — Creative Ideas & Vi` footer links (`WORK · STUDIO · INSIGHTS · ABOUT US · CONTACT ↗`), copy *"Ideas. Stories. Images. Products. Experiences. Whatever the "*, and `#ffffff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: grubogrubo-com (GruboGrubo — Creative Ideas & Visual Production Studio · Warsaw)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `grubogrubo-com` (**GruboGrubo — Creative Ideas & Visual Production Studio · Warsaw** — `https://grubogrubo.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#4c0aaf` / `#bcb8c5`).
- **Identity & Domain Context**: Independent creative studio in Warsaw: creative concepts, campaigns, storytelling, animation, 3D, CGI and interactive experiences.
- **Primary Substrate**: `#4c0aaf` (`var(--acid)` in `:root`), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#bcb8c5`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#4c0aaf` (`var(--acid)` in `:root`) paired with `#ffffff` primary typography and `#bcb8c5` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Arial` for display copy (`IDEA`) with `Arial Black` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `620px` container bounds (`gap: 22px`, padding `8px`) with `cubic-bezier(.19,1,.22,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `grubogrubo-com` in your global stylesheet:

:root {
  /* GruboGrubo — Creative Ideas & Visual Production Studio · Warsaw (grubogrubo-com) — Ground-Truth Extracted CSS Variables */
  --acid: #4c0aaf; /* Color / Atmospheric Token (grubogrubo-com) */
  --paper: #f5f4f0; /* Canvas / Surface Token (grubogrubo-com) */
  --violet: #4c0aaf; /* Color / Atmospheric Token (grubogrubo-com) */
  --accent: var(--violet); /* Brand / Palette Token (grubogrubo-com) */
  --fx-accent: #c3a0ec; /* Brand / Palette Token (grubogrubo-com) */
  --mx: 50%; /* Dimension / Scale Token (grubogrubo-com) */
  --my: 50%; /* Dimension / Scale Token (grubogrubo-com) */
  --reveal-delay: 0ms; /* Motion / Easing Token (grubogrubo-com) */
  --grubogrubo-com-bg: #4c0aaf; /* Canvas Substrate (from `var(--acid)` in `:root`) (grubogrubo-com) */
  --grubogrubo-com-ink: #ffffff; /* Primary Typography Ink (stylesheet-derived) (grubogrubo-com) */
  --grubogrubo-com-surface: #c3a0ec; /* Surface Substrate (stylesheet-derived) (grubogrubo-com) */
  --grubogrubo-com-accent: #bcb8c5; /* Interactive Accent (stylesheet-derived) (grubogrubo-com) */
  --grubogrubo-com-muted: #494551; /* Secondary Ink (stylesheet-derived) (grubogrubo-com) */
  --grubogrubo-com-border: #ffffff; /* Structural Border (stylesheet-derived) (grubogrubo-com) */
  --grubogrubo-com-container: 620px; /* Container Bound (stylesheet-derived) (grubogrubo-com) */
  --grubogrubo-com-gap: 22px; /* Grid Gutter (stylesheet-derived) (grubogrubo-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#4c0aaf` — grounded in `var(--acid)` in `:root`
- **Primary Typography Ink**: `#f5f4f0` — grounded in `var(--paper)` in `:root`
- **Elevated Surface / Card Substrate**: `#c3a0ec` — grounded in `var(--fx-accent)` in `:root`
- **Interactive Accent / Highlight**: `#bcb8c5` — grounded in `.cookie-settings-launcher button { color: #bcb8c5 }`
- **Secondary / Muted Copy**: `#494551` — grounded in `.cookie-settings-launcher button { border: #494551 }`
- **Structural Hairline Border**: `#ffffff` — grounded in `kie-settings-launcher button:fo... { color: white }` (`#ffffff`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×10408px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `620px` extracted from `grubogrubo-com` stylesheet
- **Padding & Gutters**: `8px` lateral canvas padding with `22px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 620px`, `gap: 22px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding
- **Media Queries**: `@media (max-width:620px)`, `@media (max-width:750px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1150px) and (max-height:680px)`
- **Corner Radii**: `40px`, `13px`, `25px`, `24px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Arial`
- **Body Font Stack**: `Arial Black`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: rule `h1` (`font-size: clamp(33px,3vw,54px)`, `line-height: .89`, `letter-spacing: -.06em`, `font-weight: 800`)
- **H2 Section Rule**: rule `h2` (`font-size: clamp(70px,12vw,210px)`, `line-height: .84`, `letter-spacing: -.092em`)
- **Body Copy Rule**: rule `p` (`font-size: 12px`, `line-height: 1.5`)
- **Metadata & Index Rule**: rule `nav` (`font-size: 10px`, `letter-spacing: .13em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `grubogrubo-com` (`GruboGrubo — Creative Ideas & Visual Production Studio · Warsaw`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `grubogrubo-com`)**:
   - DOM & Selectors: Landmark `<header class="site-header">` hosting `GruboGrubo — Creative Ideas & Visual` navigation (`WORK · STUDIO · INSIGHTS · ABOUT US · CONTACT ↗`), DOM attributes (`data-language="en"`, `data-i18n="manifest"`, `data-i18n="navWork"`, `data-i18n="navStudio"`), and stylesheet rule `.cookie-settings-launcher { position:fixed;left:12px;bottom:12px;z-index:40 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `grubogrubo-com`)` (`grubogrubo-com`) adapts across `@media (max-width:620px)`, `@media (max-width:750px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1150px) and (max-height:680px)` with `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.17,.84,.18,1)` transitions and links `WORK · STUDIO · INSIGHTS · ABOUT US · CONTACT ↗`.
2. **Hero Stage & Focal Lead (<section.intro> — `IDEA`)**:
   - DOM & Selectors: Landmark `<section class="intro">` presenting display lead `IDEA` and copy excerpt *"WE TURN COMPLEX THINGS INTO COMPELLING EXPERIENCES."* over `#4c0aaf` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×10408px` desktop / `390×2400px` mobile) sets `#4c0aaf` background with `#ffffff` headline `IDEA`.
3. **Primary Showcase & Content Grid (<section.about> — `WE DON’T THINK SMALL.`)**:
   - DOM & Selectors: Landmark `<section class="about">` rendering section `WE DON’T THINK SMALL.` with copy *"Ideas that shift perspectives. Concepts, campaigns and storytelli"*, asset references (`style.css`, `cookie-consent.css`, `header-logo.png (GRUBO)`, `maciej-scroll.mp4`), and grid rule `settings-launcher button:focus-vi... { opacity:1;background:4c0aaf;color:white }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.about> — `WE DON’T THINK SMALL.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 620px`, `gap: 22px`) on desktop and Single-column vertical stack at `390px` viewport width with `8px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.team> — `THE IDEA COMES FIRST.`)**:
   - DOM & Selectors: Landmark `<section class="team founder-cinematic">` framing `THE IDEA COMES FIRST.` and `Advertising films` (*"INDEPENDENT CREATIVE STUDIO"*) with `#c3a0ec` surface cards, `#bcb8c5` accents, and `.cookie-banner strong { font-size:14px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.team> — `THE IDEA COMES FIRST.`)` uses `40px`, `13px`, `25px`, `24px` radii, `#bcb8c5` highlights, and assets (style.css, cookie-consent.css, header-logo.png (GRUBO)).
5. **Colophon & Global Directory Footer (<footer.contact> — `https://grubogrubo.com`)**:
   - DOM & Selectors: Landmark `<footer class="contact">` anchoring `GruboGrubo — Creative Ideas & Vi` footer links (`WORK · STUDIO · INSIGHTS · ABOUT US · CONTACT ↗`), copy *"Ideas. Stories. Images. Products. Experiences. Whatever the "*, and `#ffffff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.contact> — `https://grubogrubo.com`)` aligns to `620px` extracted from `grubogrubo-com` stylesheet with `8px` lateral canvas padding with `22px` grid gap and attributes (data-language="en", data-i18n="manifest", data-i18n="navWork").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"WE TURN COMPLEX THINGS INTO COMPELLING EXPERIENCES."*
- Copy Excerpt 2: *"Ideas that shift perspectives. Concepts, campaigns and storytelling."*
- Copy Excerpt 3: *"INDEPENDENT CREATIVE STUDIO"*
- Copy Excerpt 4: *"Ideas. Stories. Images. Products. Experiences. Whatever the challenge, we make it..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.17,.84,.18,1)`
- **Extracted Stylesheet Rules (`grubogrubo-com`)**:
- `.cookie-settings-launcher { position:fixed;left:12px;bottom:12px;z-index:40 }`
- `settings-launcher button:focus-vi... { opacity:1;background:4c0aaf;color:white }`
- `.cookie-banner strong { font-size:14px }`
- `.cookie-banner p { font-size:12px;line-height:1.5;color:c5bdce;margin:8px 0 0 }`
- `.cookie-actions { display:flex;gap:8px;flex:none }`
- **Per-Selector Transition Rules**:
- **Selector `.site-header nav a`**: `transition: opacity .2s` extracted from `grubogrubo-com` stylesheet.
- **Selector `.chapter`**: `transition: left .55s ease,right .55s ease,opacity .45s ease` extracted from `grubogrubo-com` stylesheet.
- **Selector `.chapter-enter`**: `transition: background .25s,color .25s,transform .25s` extracted from `grubogrubo-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.19,1,.22,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.about>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `grubogrubo-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
