---
title: "UI Prompt Blueprint: www-gerd-web-de"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-gerd-web-de"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#080c16` canvas, `#f5edff` ink, `#00f0ff` accent)"
---

# UI Design System & Master Generation Blueprint: www-gerd-web-de

> **Gerd Web 3 Second - Design** (https://www.gerd-web.de) — Design ist unsere Leidenschaft. Wir begleiten Ihr Webprojekt ganzheitlich – vom prägnanten Logo über ausdrucksstarke Bildwelten bis hin z...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Gerd Web 3 Second - Design** (`https://www.gerd-web.de`). Design ist unsere Leidenschaft. Wir begleiten Ihr Webprojekt ganzheitlich – vom prägnanten Logo über ausdrucksstarke Bildwelten bis hin z...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#080c16` canvas, `#f5edff` ink, `#00f0ff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#080c16` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f5edff` primary typography and `#00f0ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Dancing Script` for display copy (`Webdesign mit Charakter`) with `Segoe UI` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1100px` container bounds (`gap: 40px`, padding `24px`) with `cubic-bezier(0.4,0,0.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1100px` (live computed `main` `max-width`).
- **Canvas Lateral Padding & Spacing**: `24px` lateral canvas padding with `40px` grid gap.
- **Border Radius Scale**: `8px`, `50%`, `16px`, `12px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1100px`, `gap: 40px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `24px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 768px)`, `@media (max-width: 480px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#080c16` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f5edff` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#241038` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#00f0ff` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#94a3b8` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#00f0ff` | `var(--btn-border)` in `:root` |
| **Variable Token (`--bg-center`)** | `#101c36` | `var(--bg-center)` in `:root` |
| **Variable Token (`--active-color`)** | `#a855f7` | `var(--active-color)` in `:root` |
| **Variable Token (`--cursor-ring-color`)** | `#d8b4fe` | `var(--cursor-ring-color)` in `:root` |
| **Variable Token (`--text-color`)** | `#e6edf8` | `var(--text-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg-base` | `#080c16` | Canvas / Surface Token |
| `--bg-center` | `#101c36` | Canvas / Surface Token |
| `--card-bg` | `rgba(14, 23, 42, 0.7)` | Canvas / Surface Token |
| `--net-color` | `#00f0ff` | Brand / Palette Token |
| `--net-glow` | `rgba(0, 240, 255, 0.35)` | Color / Atmospheric Token |
| `--btn-bg` | `rgba(13, 22, 41, 0.88)` | Canvas / Surface Token |
| `--btn-border` | `#00f0ff` | Elevation / Border Token |
| `--btn-hover-border` | `#00f0ff` | Elevation / Border Token |
| `--btn-hover-glow` | `rgba(0, 240, 255, 0.7)` | Color / Atmospheric Token |
| `--active-color` | `#a855f7` | Brand / Palette Token |
| `--active-glow` | `rgba(168, 85, 247, 0.75)` | Color / Atmospheric Token |
| `--cursor-ring-color` | `#d8b4fe` | Brand / Palette Token |
| `--cursor-ring-glow` | `rgba(168, 85, 247, 0.85)` | Elevation / Border Token |
| `--text-color` | `#e6edf8` | Typography Ink Token |
| `--text-muted` | `#94a3b8` | Typography Ink Token |
| `--section-spacing` | `40px` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Dancing Script`.
- **Primary Body Stack**: `Segoe UI`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: observed font-size ladder: `30px`, `16px`, `13px`, `13.3333px`, `12px`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 30px`, `line-height: 40.5px`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.3,0,0.2,1)`, `cubic-bezier(0.25,1,0.5,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `#custom-cursor`**: `transition: opacity 0.08s ease, border-color 0.18s ease, box-shadow 0.18s...` extracted from `www-gerd-web-de` stylesheet.
- **Selector `#cursor-dot`**: `transition: opacity 0.2s ease` extracted from `www-gerd-web-de` stylesheet.
- **Selector `#cursor-logo`**: `transition: opacity 0.15s ease, transform 0.65s cubic-bezier(0.4,0,0.2,1)` extracted from `www-gerd-web-de` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.2,1)`)**: Governs interactive state transitions across `<nav.menu-container>` and `<section.impressum-section:nth(2)>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.impressum-section>` and `<section.impressum-section:nth(2)>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Gerd Web 3 Second - Design                 │
│ ====================================================================== │
│ [ <nav.menu-container> (610x43px)     | Home · Web · Plakate · Spiel ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.impressum-section> (w=1100px)                 | │
│ | H1: Webdesign mit Charakter                                        | │
│ | Substrate: #080c16 | Ink: #f5edff | Accent: #00f0ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.impressum-section) max-w: 1100px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Design für Werbung und Unter |  | Fotografie & Porträts        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.impressum-section) — Über mich             | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sound-contro) | https://www.gerd-web.de              │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 40px)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.menu-container>    ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.impressum-secti) — 390px Vertical Lead        | │
│ | H1: Webdesign mit Charakter                                        | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.impressum-sec) — 1-Col Stack              | │
│ | [ Item 1: Design für Werbung und Unterhaltung                    ] | │
│ | [ Item 2: Fotografie & Porträts                                  ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.impressum-secti) — 1-Col (Über mich)        | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sound-contro) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.menu-container> — `www-gerd-web-de`)**:
   - Landmark `<nav class="menu-container">` (`610x43px`) hosting `Gerd Web 3 Second - Design` navigation (`Home · Web · Plakate · Spiele · Foto`), DOM attributes (`data-target="www-gerd-web-de"`), and stylesheet rule `cursor-dot { opacity: 0 !important; }`.
2. **Hero Stage & Focal Lead (<section.impressum-section> — `Webdesign mit Charakter`)**:
   - Landmark `<section class="impressum-section">` presenting display lead `Webdesign mit Charakter` and copy excerpt *"Design ist unsere Leidenschaft. Wir begleiten Ihr Webprojekt ganz"* over `#080c16` canvas and `#f5edff` ink.
3. **Primary Showcase & Content Grid (<section.impressum-section:nth(2)> — `Design für Werbung und Unterhaltun`)**:
   - Landmark `<section class="impressum-section">` rendering section `Design für Werbung und Unterhaltung` with copy *"Jede Website wird von Grund auf individuell konzipiert und passge"*, asset references (`logo.png (Logo)`, `banner-index.jpg (Willkommen Banner)`, `index-webseite.jpg (Titelbild Startseite)`, `index-design.jpg (Fotografie Startseite)`), and grid rule `custom-cursor.hovering { box-shadow: 0 0 18px var(--active-glow), 0 0 28px rgba(168, 85, 247, 0.6); }`.
4. **Interactive Detail & Feature Matrix (<section.impressum-section:nth(3)> — `Fotografie & Porträts`)**:
   - Landmark `<section class="impressum-section">` framing `Fotografie & Porträts` and `Über mich` (*"Neben Webseiten gestalten wir unter anderem Interfaces und Visual"*) with `#241038` surface cards, `#00f0ff` accents, and `cursor-logo.rotated { opacity: 1; }`.
5. **Colophon & Global Directory Footer (<footer.sound-control> — `https://www.gerd-web.de`)**:
   - Landmark `<footer class="sound-control">` anchoring `Gerd Web 3 Second - Design` footer links (`Home · Web · Plakate · Spiele · Foto`), copy *"Ob Smartphone, Tablet oder Desktop: Dank Responsive Design p"*, and `#00f0ff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-gerd-web-de (Gerd Web 3 Second - Design)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-gerd-web-de` (**Gerd Web 3 Second - Design** — `https://www.gerd-web.de`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#080c16` canvas, `#f5edff` ink, `#00f0ff` accent).
- **Identity & Domain Context**: Design ist unsere Leidenschaft. Wir begleiten Ihr Webprojekt ganzheitlich – vom prägnanten Logo über ausdrucksstarke Bildwelten bis hin z...
- **Primary Substrate**: `#080c16` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#f5edff`, **Accent / Highlight**: `#00f0ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#080c16` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f5edff` primary typography and `#00f0ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Dancing Script` for display copy (`Webdesign mit Charakter`) with `Segoe UI` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1100px` container bounds (`gap: 40px`, padding `24px`) with `cubic-bezier(0.4,0,0.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-gerd-web-de` in your global stylesheet:

:root {
  /* Gerd Web 3 Second - Design (www-gerd-web-de) — Live-Grounded CSS Variables */
  --bg-base: #080c16; /* Canvas / Surface Token (www-gerd-web-de) */
  --bg-center: #101c36; /* Canvas / Surface Token (www-gerd-web-de) */
  --card-bg: rgba(14, 23, 42, 0.7); /* Canvas / Surface Token (www-gerd-web-de) */
  --net-color: #00f0ff; /* Brand / Palette Token (www-gerd-web-de) */
  --net-glow: rgba(0, 240, 255, 0.35); /* Color / Atmospheric Token (www-gerd-web-de) */
  --btn-bg: rgba(13, 22, 41, 0.88); /* Canvas / Surface Token (www-gerd-web-de) */
  --btn-border: #00f0ff; /* Elevation / Border Token (www-gerd-web-de) */
  --btn-hover-border: #00f0ff; /* Elevation / Border Token (www-gerd-web-de) */
  --btn-hover-glow: rgba(0, 240, 255, 0.7); /* Color / Atmospheric Token (www-gerd-web-de) */
  --active-color: #a855f7; /* Brand / Palette Token (www-gerd-web-de) */
  --active-glow: rgba(168, 85, 247, 0.75); /* Color / Atmospheric Token (www-gerd-web-de) */
  --cursor-ring-color: #d8b4fe; /* Brand / Palette Token (www-gerd-web-de) */
  --cursor-ring-glow: rgba(168, 85, 247, 0.85); /* Elevation / Border Token (www-gerd-web-de) */
  --text-color: #e6edf8; /* Typography Ink Token (www-gerd-web-de) */
  --text-muted: #94a3b8; /* Typography Ink Token (www-gerd-web-de) */
  --section-spacing: 40px; /* Layout / Spatial Grid Token (www-gerd-web-de) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#080c16` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#f5edff` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#241038` — grounded in live computed `a` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#00f0ff` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#94a3b8` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#00f0ff` — grounded in `var(--btn-border)` in `:root`
- **Variable Token (`--bg-center`)**: `#101c36` — grounded in `var(--bg-center)` in `:root`
- **Variable Token (`--active-color`)**: `#a855f7` — grounded in `var(--active-color)` in `:root`
- **Variable Token (`--cursor-ring-color`)**: `#d8b4fe` — grounded in `var(--cursor-ring-color)` in `:root`
- **Variable Token (`--text-color`)**: `#e6edf8` — grounded in `var(--text-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1100px` (live computed `main` `max-width`)
- **Padding & Gutters**: `24px` lateral canvas padding with `40px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1100px`, `gap: 40px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `24px` horizontal padding
- **Media Queries**: `@media (max-width: 768px)`, `@media (max-width: 480px)`
- **Corner Radii**: `8px`, `50%`, `16px`, `12px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Dancing Script`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: observed font-size ladder: `30px`, `16px`, `13px`, `13.3333px`, `12px`
- **H2 Section Rule**: live computed `h2` (`font-size: 30px`, `line-height: 40.5px`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-gerd-web-de` (`Gerd Web 3 Second - Design`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.menu-container> — `www-gerd-web-de`)**:
   - DOM & Selectors: Landmark `<nav class="menu-container">` (`610x43px`) hosting `Gerd Web 3 Second - Design` navigation (`Home · Web · Plakate · Spiele · Foto`), DOM attributes (`data-target="www-gerd-web-de"`), and stylesheet rule `cursor-dot { opacity: 0 !important; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.menu-container> — `www-gerd-web-de`)` (`www-gerd-web-de`) adapts across `@media (max-width: 768px)`, `@media (max-width: 480px)` with `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.3,0,0.2,1)`, `cubic-bezier(0.25,1,0.5,1)` transitions and links `Home · Web · Plakate · Spiele · Foto`.
2. **Hero Stage & Focal Lead (<section.impressum-section> — `Webdesign mit Charakter`)**:
   - DOM & Selectors: Landmark `<section class="impressum-section">` presenting display lead `Webdesign mit Charakter` and copy excerpt *"Design ist unsere Leidenschaft. Wir begleiten Ihr Webprojekt ganz"* over `#080c16` canvas and `#f5edff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#080c16` background with `#f5edff` headline `Webdesign mit Charakter`.
3. **Primary Showcase & Content Grid (<section.impressum-section:nth(2)> — `Design für Werbung und Unterhaltun`)**:
   - DOM & Selectors: Landmark `<section class="impressum-section">` rendering section `Design für Werbung und Unterhaltung` with copy *"Jede Website wird von Grund auf individuell konzipiert und passge"*, asset references (`logo.png (Logo)`, `banner-index.jpg (Willkommen Banner)`, `index-webseite.jpg (Titelbild Startseite)`, `index-design.jpg (Fotografie Startseite)`), and grid rule `custom-cursor.hovering { box-shadow: 0 0 18px var(--active-glow), 0 0 28px rgba(168, 85, 247, 0.6); }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.impressum-section:nth(2)> — `Design für Werbung und Unterhaltun`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1100px`, `gap: 40px`) on desktop and Single-column vertical stack at `390px` viewport width with `24px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.impressum-section:nth(3)> — `Fotografie & Porträts`)**:
   - DOM & Selectors: Landmark `<section class="impressum-section">` framing `Fotografie & Porträts` and `Über mich` (*"Neben Webseiten gestalten wir unter anderem Interfaces und Visual"*) with `#241038` surface cards, `#00f0ff` accents, and `cursor-logo.rotated { opacity: 1; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.impressum-section:nth(3)> — `Fotografie & Porträts`)` uses `8px`, `50%`, `16px`, `12px` radii, `#00f0ff` highlights, and assets (logo.png (Logo), banner-index.jpg (Willkommen Banner), index-webseite.jpg (Titelbild Startseite)).
5. **Colophon & Global Directory Footer (<footer.sound-control> — `https://www.gerd-web.de`)**:
   - DOM & Selectors: Landmark `<footer class="sound-control">` anchoring `Gerd Web 3 Second - Design` footer links (`Home · Web · Plakate · Spiele · Foto`), copy *"Ob Smartphone, Tablet oder Desktop: Dank Responsive Design p"*, and `#00f0ff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.sound-control> — `https://www.gerd-web.de`)` aligns to `1100px` (live computed `main` `max-width`) with `24px` lateral canvas padding with `40px` grid gap and attributes (www-gerd-web-de).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Design ist unsere Leidenschaft. Wir begleiten Ihr Webprojekt ganzheitlich – vom pr..."*
- Copy Excerpt 2: *"Jede Website wird von Grund auf individuell konzipiert und passgenau zugeschnitten."*
- Copy Excerpt 3: *"Neben Webseiten gestalten wir unter anderem Interfaces und Visuals für Spiele sowi..."*
- Copy Excerpt 4: *"Ob Smartphone, Tablet oder Desktop: Dank Responsive Design passen sich alle Elemen..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.3,0,0.2,1)`, `cubic-bezier(0.25,1,0.5,1)`
- **Extracted Stylesheet Rules (`www-gerd-web-de`)**:
- `cursor-dot { opacity: 0 !important; }`
- `custom-cursor.hovering { box-shadow: 0 0 18px var(--active-glow), 0 0 28px rgba(168, 85, 247, 0.6); }`
- `cursor-logo.rotated { opacity: 1; }`
- `body.page-fading-out { opacity: 0.15; }`
- `banner-container.scrolled .banner... { top: 10px; }`
- **Per-Selector Transition Rules**:
- **Selector `#custom-cursor`**: `transition: opacity 0.08s ease, border-color 0.18s ease, box-shadow 0.18s...` extracted from `www-gerd-web-de` stylesheet.
- **Selector `#cursor-dot`**: `transition: opacity 0.2s ease` extracted from `www-gerd-web-de` stylesheet.
- **Selector `#cursor-logo`**: `transition: opacity 0.15s ease, transform 0.65s cubic-bezier(0.4,0,0.2,1)` extracted from `www-gerd-web-de` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.2,1)`)**: Governs interactive state transitions across `<nav.menu-container>` and `<section.impressum-section:nth(2)>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.impressum-section>` and `<section.impressum-section:nth(2)>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-gerd-web-de`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
