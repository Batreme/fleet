---
title: "UI Prompt Blueprint: alexandracapitanescu-com"
date: 2026-11-15
target: "[[overview|alexandracapitanescu-com]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#ba1818` canvas, `#e2d9d0` ink, `#0000` accent)"
---

# UI Design System & Master Generation Blueprint: alexandracapitanescu-com

> **Alexandra Căpitănescu - Official Website** (https://alexandracapitanescu.com/) — Romanian artist Alexandra Căpitănescu and her band blend alternative rock, raw emotion and explosive live energy.

![Desktop Viewport Capture (1440x11875)](file:///root/projects/fleet/wiki/targets/alexandracapitanescu-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Alexandra Căpitănescu - Official Website** (`https://alexandracapitanescu.com/`). Romanian artist Alexandra Căpitănescu and her band blend alternative rock, raw emotion and explosive live energy.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#ba1818` canvas, `#e2d9d0` ink, `#0000` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ba1818` (`var(--color-red)` in `:root`) paired with `#e2d9d0` primary typography and `#0000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `hershey` for display copy (`Alexandra Căpitănescu`) with `hershey Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: var(--spacing)`, padding `88px`) with `cubic-bezier(.16,1,.3,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/alexandracapitanescu-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×11875px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1440px` extracted from `alexandracapitanescu-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `88px` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `.25rem`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `88px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:48rem)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (max-width:767px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ba1818` | `var(--color-red)` in `:root` |
| **Primary Typography Ink** | `#e2d9d0` | `var(--color-cream)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0b090a` | `var(--color-ink)` in `:root` |
| **Interactive Accent / Highlight** | `#0000` | `textarea { background-color: #0000 }` |
| **Secondary / Muted Copy** | `#ff0000` | `::selection { background: red }` (`#ff0000`) |
| **Structural Hairline Border** | `#000` | `.intro-mask { background: #000 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-hershey-noailles` | `"hershey", "hershey Fallback"` | Typography / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-2xl` | `1.5rem` | Typography Ink Token |
| `--text-2xl--line-height` | `calc(2 / 1.5)` | Typography Ink Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-red` | `#ba1818` | Brand / Palette Token |
| `--color-cream` | `#e2d9d0` | Brand / Palette Token |
| `--color-ink` | `#0b090a` | Typography Ink Token |
| `--font-display` | `"Times New Roman", Times, serif` | Typography / Scale Token |
| `--font-body` | `Arial, Helvetica, sans-serif` | Typography / Scale Token |
| `--font-hershey` | `var(--font-hershey-noailles), "Times New Roman", serif` | Typography / Scale Token |
| `--intro-total` | `4.7s` | Motion / Timing Token |
| `--ease-out-expo` | `cubic-bezier(.16, 1, .3, 1)` | Motion / Easing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `hershey`.
- **Primary Body Stack**: `hershey Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: "Times New Roman", Times, serif`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `.section-title` (`font-size: clamp(56px,6.6vw,110px)`).
- **Body Copy**: CSS variables `--font-body: Arial, Helvetica, sans-serif`; rule `p` (`font-size: clamp(18px,1.6vw,22px)`, `line-height: 1.2`).
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 10px`, `letter-spacing: .14em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.7,0,.84,0)`, `cubic-bezier(.76,0,.24,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.site-logo`**: `transition: transform .7s var(--ease-out-expo)` extracted from `alexandracapitanescu-com` stylesheet.
- **Selector `.menu-button`**: `transition: background-color .3s,color .3s` extracted from `alexandracapitanescu-com` stylesheet.
- **Selector `.menu-button:before`**: `transition: inset .4s var(--ease-out-expo)` extracted from `alexandracapitanescu-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.relative>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.relative>` and `<section.relative>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Alexandra Căpitănescu - Official Website   │
│ ====================================================================== │
│ [ <header.site-header>     | Tickets Tour dates · ( ) Meet the band ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative>                                   |   │
│ | H1: Alexandra Căpitănescu                                        |   │
│ | Substrate: #ba1818    | Ink: #e2d9d0    | Accent: #0000          |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.relative>        ) max-w: 1440px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | The Sound Of Our Story       |  | Choke Me                     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.site-heade] -> [<section.relative>] -> [<section.relative>] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | https://alexandracapitanescu.com/  │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `alexandracapitanescu-com`)**:
   - Landmark `<header class="site-header intro-reveal">` hosting `Alexandra Căpitănescu - Official Web` navigation (`Tickets Tour dates · ( ) Meet the band · News From the road · Fan Art Made by you · Merch Official shop`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-side="left"`, `data-accent="true"`), and stylesheet rule `font-face { font-family:hershey;src:url(../media/HersheyNoaillesTimes-s.p.2873syaszu... }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Alexandra Căpitănescu`)**:
   - Landmark `<section class="relative flex">` presenting display lead `Alexandra Căpitănescu` and copy excerpt *"Music Releases & videos"* over `#ba1818` canvas and `#e2d9d0` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `The Sound Of Our Story`)**:
   - Landmark `<section class="relative mx-auto">` rendering section `The Sound Of Our Story` with copy *"Tickets Tour dates"*, asset references (`1uywzyker6zod.css`, `2j1ir--xjy6fe.css`, `1dx8d72ay49iv.js`, `0s2cptn1mmf6r.js`), and grid rule `.RhbOdG_className { font-family:hershey,hershey Fallback }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Choke Me`)**:
   - Landmark `<section class="relative bg-ink">` framing `Choke Me` and `We Are Making “Noise”` (*"News From the road"*) with `#0b090a` surface cards, `#0000` accents, and `.RhbOdG_variable { --font-hershey-noailles:"hershey", "hershey Fallback" }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://alexandracapitanescu.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Alexandra Căpitănescu - Official` footer links (`Tickets Tour dates · ( ) Meet the band · News From the road · Fan Art Made by you · Merch Official shop`), copy *"Fan Art Made by you"*, and `#000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: alexandracapitanescu-com (Alexandra Căpitănescu - Official Website)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `alexandracapitanescu-com` (**Alexandra Căpitănescu - Official Website** — `https://alexandracapitanescu.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#ba1818` canvas, `#e2d9d0` ink, `#0000` accent).
- **Identity & Domain Context**: Romanian artist Alexandra Căpitănescu and her band blend alternative rock, raw emotion and explosive live energy.
- **Primary Substrate**: `#ba1818` (`var(--color-red)` in `:root`), **Primary Ink**: `#e2d9d0`, **Accent / Highlight**: `#0000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ba1818` (`var(--color-red)` in `:root`) paired with `#e2d9d0` primary typography and `#0000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `hershey` for display copy (`Alexandra Căpitănescu`) with `hershey Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: var(--spacing)`, padding `88px`) with `cubic-bezier(.16,1,.3,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `alexandracapitanescu-com` in your global stylesheet:

:root {
  /* Alexandra Căpitănescu - Official Website (alexandracapitanescu-com) — Ground-Truth Extracted CSS Variables */
  --font-hershey-noailles: "hershey", "hershey Fallback"; /* Typography / Scale Token (alexandracapitanescu-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (alexandracapitanescu-com) */
  --text-xs: .75rem; /* Typography Ink Token (alexandracapitanescu-com) */
  --text-xs--line-height: calc(1 / .75); /* Typography Ink Token (alexandracapitanescu-com) */
  --text-2xl: 1.5rem; /* Typography Ink Token (alexandracapitanescu-com) */
  --text-2xl--line-height: calc(2 / 1.5); /* Typography Ink Token (alexandracapitanescu-com) */
  --default-font-family: var(--font-sans); /* Typography / Scale Token (alexandracapitanescu-com) */
  --default-mono-font-family: var(--font-mono); /* Typography / Scale Token (alexandracapitanescu-com) */
  --color-red: #ba1818; /* Brand / Palette Token (alexandracapitanescu-com) */
  --color-cream: #e2d9d0; /* Brand / Palette Token (alexandracapitanescu-com) */
  --color-ink: #0b090a; /* Typography Ink Token (alexandracapitanescu-com) */
  --font-display: "Times New Roman", Times, serif; /* Typography / Scale Token (alexandracapitanescu-com) */
  --font-body: Arial, Helvetica, sans-serif; /* Typography / Scale Token (alexandracapitanescu-com) */
  --font-hershey: var(--font-hershey-noailles), "Times New Roman", serif; /* Typography / Scale Token (alexandracapitanescu-com) */
  --intro-total: 4.7s; /* Motion / Timing Token (alexandracapitanescu-com) */
  --ease-out-expo: cubic-bezier(.16, 1, .3, 1); /* Motion / Easing Token (alexandracapitanescu-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ba1818` — grounded in `var(--color-red)` in `:root`
- **Primary Typography Ink**: `#e2d9d0` — grounded in `var(--color-cream)` in `:root`
- **Elevated Surface / Card Substrate**: `#0b090a` — grounded in `var(--color-ink)` in `:root`
- **Interactive Accent / Highlight**: `#0000` — grounded in `textarea { background-color: #0000 }`
- **Secondary / Muted Copy**: `#ff0000` — grounded in `::selection { background: red }` (`#ff0000`)
- **Structural Hairline Border**: `#000` — grounded in `.intro-mask { background: #000 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×11875px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` extracted from `alexandracapitanescu-com` stylesheet
- **Padding & Gutters**: `88px` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `88px` horizontal padding
- **Media Queries**: `@media (min-width:48rem)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (max-width:767px)`
- **Corner Radii**: `.25rem`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `hershey`
- **Body Font Stack**: `hershey Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--font-display: "Times New Roman", Times, serif`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `.section-title` (`font-size: clamp(56px,6.6vw,110px)`)
- **Body Copy Rule**: CSS variables `--font-body: Arial, Helvetica, sans-serif`; rule `p` (`font-size: clamp(18px,1.6vw,22px)`, `line-height: 1.2`)
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 10px`, `letter-spacing: .14em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `alexandracapitanescu-com` (`Alexandra Căpitănescu - Official Website`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `alexandracapitanescu-com`)**:
   - DOM & Selectors: Landmark `<header class="site-header intro-reveal">` hosting `Alexandra Căpitănescu - Official Web` navigation (`Tickets Tour dates · ( ) Meet the band · News From the road · Fan Art Made by you · Merch Official shop`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-side="left"`, `data-accent="true"`), and stylesheet rule `font-face { font-family:hershey;src:url(../media/HersheyNoaillesTimes-s.p.2873syaszu... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `alexandracapitanescu-com`)` (`alexandracapitanescu-com`) adapts across `@media (min-width:48rem)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (max-width:767px)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.7,0,.84,0)`, `cubic-bezier(.76,0,.24,1)` transitions and links `Tickets Tour dates · ( ) Meet the band · News From the road · Fan Art Made by you · Merch Official shop`.
2. **Hero Stage & Focal Lead (<section.relative> — `Alexandra Căpitănescu`)**:
   - DOM & Selectors: Landmark `<section class="relative flex">` presenting display lead `Alexandra Căpitănescu` and copy excerpt *"Music Releases & videos"* over `#ba1818` canvas and `#e2d9d0` ink.
   - Responsive Contract: Hero stage (`1440×11875px` desktop / `390×2400px` mobile) sets `#ba1818` background with `#e2d9d0` headline `Alexandra Căpitănescu`.
3. **Primary Showcase & Content Grid (<section.relative> — `The Sound Of Our Story`)**:
   - DOM & Selectors: Landmark `<section class="relative mx-auto">` rendering section `The Sound Of Our Story` with copy *"Tickets Tour dates"*, asset references (`1uywzyker6zod.css`, `2j1ir--xjy6fe.css`, `1dx8d72ay49iv.js`, `0s2cptn1mmf6r.js`), and grid rule `.RhbOdG_className { font-family:hershey,hershey Fallback }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.relative> — `The Sound Of Our Story`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `88px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Choke Me`)**:
   - DOM & Selectors: Landmark `<section class="relative bg-ink">` framing `Choke Me` and `We Are Making “Noise”` (*"News From the road"*) with `#0b090a` surface cards, `#0000` accents, and `.RhbOdG_variable { --font-hershey-noailles:"hershey", "hershey Fallback" }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.relative> — `Choke Me`)` uses `.25rem`, `50%` radii, `#0000` highlights, and assets (1uywzyker6zod.css, 2j1ir--xjy6fe.css, 1dx8d72ay49iv.js).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://alexandracapitanescu.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `Alexandra Căpitănescu - Official` footer links (`Tickets Tour dates · ( ) Meet the band · News From the road · Fan Art Made by you · Merch Official shop`), copy *"Fan Art Made by you"*, and `#000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://alexandracapitanescu.com/`)` aligns to `1440px` extracted from `alexandracapitanescu-com` stylesheet with `88px` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-precedence="next", data-precedence="next", data-side="left").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Music Releases & videos"*
- Copy Excerpt 2: *"Tickets Tour dates"*
- Copy Excerpt 3: *"News From the road"*
- Copy Excerpt 4: *"Fan Art Made by you"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.7,0,.84,0)`, `cubic-bezier(.76,0,.24,1)`
- **Extracted Stylesheet Rules (`alexandracapitanescu-com`)**:
- `font-face { font-family:hershey;src:url(../media/HersheyNoaillesTimes-s.p.2873syaszu... }`
- `.RhbOdG_className { font-family:hershey,hershey Fallback }`
- `.RhbOdG_variable { --font-hershey-noailles:"hershey", "hershey Fallback" }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- **Per-Selector Transition Rules**:
- **Selector `.site-logo`**: `transition: transform .7s var(--ease-out-expo)` extracted from `alexandracapitanescu-com` stylesheet.
- **Selector `.menu-button`**: `transition: background-color .3s,color .3s` extracted from `alexandracapitanescu-com` stylesheet.
- **Selector `.menu-button:before`**: `transition: inset .4s var(--ease-out-expo)` extracted from `alexandracapitanescu-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.relative>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.relative>` and `<section.relative>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `alexandracapitanescu-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
