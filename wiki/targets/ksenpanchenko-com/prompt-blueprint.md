---
title: "UI Prompt Blueprint: ksenpanchenko-com"
date: 2026-11-15
target: "[[overview|ksenpanchenko-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#a8a8a6`)"
---

# UI Design System & Master Generation Blueprint: ksenpanchenko-com

> **Ksen Panchenko — UX/UI & Product Designer in Dublin · FinTech & SaaS** (https://ksenpanchenko.com/) — Ksen (Kseniia) Panchenko, independent UX/UI & Product Designer in Dublin: websites, products and design systems for FinTech and SaaS — pl...

![Desktop Viewport Capture (1440x8165)](file:///root/projects/fleet/wiki/targets/ksenpanchenko-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Ksen Panchenko — UX/UI & Product Designer in Dublin · FinTech & SaaS** (`https://ksenpanchenko.com/`). Ksen (Kseniia) Panchenko, independent UX/UI & Product Designer in Dublin: websites, products and design systems for FinTech and SaaS — pl...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#a8a8a6`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffffff` (`var(--color-neutral-0)` in `:root`) paired with `#2b2b2b` primary typography and `#a8a8a6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `GeistSans` for display copy (`Ksen Panchenko — UX/UI & Product Des`) with `GeistSans Fallback` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `300px` container bounds (`gap: 4px`, padding `4px`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/ksenpanchenko-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×8165px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `300px` extracted from `ksenpanchenko-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `4px` lateral canvas padding with `4px` grid gap.
- **Border Radius Scale**: `14px`, `999px`, `12%`, `11%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 300px`, `gap: 4px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-height:820px)`, `@media (max-height:640px)`, `@media (max-width:1023px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--color-neutral-0)` in `:root` |
| **Primary Typography Ink** | `#f4f1ec` | `var(--color-neutral-50)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f1f0ec` | `var(--color-neutral-100)` in `:root` |
| **Interactive Accent / Highlight** | `#a8a8a6` | `var(--color-neutral-400)` in `:root` |
| **Secondary / Muted Copy** | `#6b6b6b` | `var(--color-neutral-500)` in `:root` |
| **Structural Hairline Border** | `#2b2b2b` | `var(--color-neutral-800)` in `:root` |
| **Variable Token (`--color-neutral-950`)** | `#141414` | `var(--color-neutral-950)` in `:root` |
| **Variable Token (`--color-orange-500`)** | `#ff5c2e` | `var(--color-orange-500)` in `:root` |
| **Variable Token (`--color-orange-600`)** | `#e8461a` | `var(--color-orange-600)` in `:root` |
| **Variable Token (`--color-green-500`)** | `#4dd973` | `var(--color-green-500)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--gap` | `6cqw` | Layout / Spatial Grid Token |
| `--stage` | `min(816px,calc(100vh - var(--component-nav-height)))` | Dimension / Scale Token |
| `--ts` | `64` | Design System Custom Token |
| `--font-geist-sans` | `"GeistSans","GeistSans Fallback"` | Typography / Scale Token |
| `--font-serif-loaded` | `"serif","serif Fallback",Georgia,serif` | Typography / Scale Token |
| `--color-neutral-0` | `#ffffff` | Brand / Palette Token |
| `--color-neutral-50` | `#f4f1ec` | Brand / Palette Token |
| `--color-neutral-100` | `#f1f0ec` | Brand / Palette Token |
| `--color-neutral-400` | `#a8a8a6` | Brand / Palette Token |
| `--color-neutral-500` | `#6b6b6b` | Brand / Palette Token |
| `--color-neutral-800` | `#2b2b2b` | Brand / Palette Token |
| `--color-neutral-950` | `#141414` | Brand / Palette Token |
| `--color-orange-500` | `#ff5c2e` | Brand / Palette Token |
| `--color-orange-600` | `#e8461a` | Brand / Palette Token |
| `--color-green-500` | `#4dd973` | Brand / Palette Token |
| `--font-family-serif` | `var(--font-serif-loaded,"Instrument Serif"),Georgia,serif` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `GeistSans`.
- **Primary Body Stack**: `GeistSans Fallback`.
- **Technical / Metadata Stack**: `JetBrains Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--type-display-size: 220px`, `--type-display-line-height: 198px`, `--type-display-letter-spacing: -6.6px`.
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `14px`, `13px`, `32px`, `52px`, `12px`).
- **Body Copy**: CSS variables `--type-body-lead-size: 24px`, `--type-body-lead-line-height: 31.2px`, `--type-body-lead-letter-spacing: 0px`; rule `p` (`font-size: 16px`, `line-height: 24px`).
- **Metadata & Navigation Labels**: CSS variables `--font-family-mono: "JetBrains Mono",ui-monospace,monospace`, `--type-display-letter-spacing: -6.6px`, `--type-heading-large-letter-spacing: 0px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.22,1.18,.36,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.sw__reel`**: `transition: opacity .55s var(--ease-out),visibility 0s .55s` extracted from `ksenpanchenko-com` stylesheet.
- **Selector `.sw__reel.is-active`**: `transition: opacity .55s var(--ease-out) .08s,visibility 0s` extracted from `ksenpanchenko-com` stylesheet.
- **Selector `.cs-next__reel) .sw__reel img`**: `transition: none` extracted from `ksenpanchenko-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.sw>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Ksen Panchenko — UX/UI & Product Designer  │
│ ====================================================================== │
│ [ <header.nav>             | Work · About                           ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Ksen Panchenko — UX/UI & Product Designer in Dubl...         |   │
│ | Substrate: #ffffff    | Ink: #2b2b2b    | Accent: #a8a8a6        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.sw>              ) max-w: 300px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Selected work                |  | Services                     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 4px   ) | │
│ | [<header.nav>] -> [<section.hero>] -> [<section.sw>] |               │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://ksenpanchenko.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.nav> — `ksenpanchenko-com`)**:
   - Landmark `<header class="nav">` hosting `Ksen Panchenko — UX/UI & Product Des` navigation (`Work · About`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-end="1"`), and stylesheet rule `.sw__reel.is-active { opacity:1;visibility:visible;transition:opacity .55s var(--ease-out) .08... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Ksen Panchenko — UX/UI & Product D`)**:
   - Landmark `<section class="hero">` presenting display lead `Ksen Panchenko — UX/UI & Product Designer in Dubl...` and copy excerpt *"Available for projects"* over `#ffffff` canvas and `#2b2b2b` ink.
3. **Primary Showcase & Content Grid (<section.sw> — `Selected work`)**:
   - Landmark `<section class="sw">` rendering section `Selected work` with copy *"Dublin 19:22 GMT+0"*, asset references (`7cb8e1b9ab81be17-s.p.woff2`, `dbccb4a9e22cbf0d-s.p.woff2`, `e872e3f251959e82-s.p.woff2`, `kseniia-cutout.webp`), and grid rule `.sw__reel img { position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacit... }`.
4. **Interactive Detail & Feature Matrix (<section.philo> — `Services`)**:
   - Landmark `<section class="philo">` framing `Services` and `Product & UX` (*"E m a i l m e Email me"*) with `#f1f0ec` surface cards, `#a8a8a6` accents, and `.sw__reel.is-active .sw__win { translate:0 0 }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://ksenpanchenko.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Ksen Panchenko — UX/UI & Product` footer links (`Work · About`), copy *"Gold London Design Awards 2026 · Emerald24 · UI Design"*, and `#2b2b2b` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: ksenpanchenko-com (Ksen Panchenko — UX/UI & Product Designer in Dublin · FinTech & SaaS)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `ksenpanchenko-com` (**Ksen Panchenko — UX/UI & Product Designer in Dublin · FinTech & SaaS** — `https://ksenpanchenko.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#a8a8a6`).
- **Identity & Domain Context**: Ksen (Kseniia) Panchenko, independent UX/UI & Product Designer in Dublin: websites, products and design systems for FinTech and SaaS — pl...
- **Primary Substrate**: `#ffffff` (`var(--color-neutral-0)` in `:root`), **Primary Ink**: `#2b2b2b`, **Accent / Highlight**: `#a8a8a6`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffffff` (`var(--color-neutral-0)` in `:root`) paired with `#2b2b2b` primary typography and `#a8a8a6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `GeistSans` for display copy (`Ksen Panchenko — UX/UI & Product Des`) with `GeistSans Fallback` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `300px` container bounds (`gap: 4px`, padding `4px`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `ksenpanchenko-com` in your global stylesheet:

:root {
  /* Ksen Panchenko — UX/UI & Product Designer in Dublin · FinTech & SaaS (ksenpanchenko-com) — Ground-Truth Extracted CSS Variables */
  --gap: 6cqw; /* Layout / Spatial Grid Token (ksenpanchenko-com) */
  --stage: min(816px,calc(100vh - var(--component-nav-height))); /* Dimension / Scale Token (ksenpanchenko-com) */
  --ts: 64; /* Design System Custom Token (ksenpanchenko-com) */
  --font-geist-sans: "GeistSans","GeistSans Fallback"; /* Typography / Scale Token (ksenpanchenko-com) */
  --font-serif-loaded: "serif","serif Fallback",Georgia,serif; /* Typography / Scale Token (ksenpanchenko-com) */
  --color-neutral-0: #ffffff; /* Brand / Palette Token (ksenpanchenko-com) */
  --color-neutral-50: #f4f1ec; /* Brand / Palette Token (ksenpanchenko-com) */
  --color-neutral-100: #f1f0ec; /* Brand / Palette Token (ksenpanchenko-com) */
  --color-neutral-400: #a8a8a6; /* Brand / Palette Token (ksenpanchenko-com) */
  --color-neutral-500: #6b6b6b; /* Brand / Palette Token (ksenpanchenko-com) */
  --color-neutral-800: #2b2b2b; /* Brand / Palette Token (ksenpanchenko-com) */
  --color-neutral-950: #141414; /* Brand / Palette Token (ksenpanchenko-com) */
  --color-orange-500: #ff5c2e; /* Brand / Palette Token (ksenpanchenko-com) */
  --color-orange-600: #e8461a; /* Brand / Palette Token (ksenpanchenko-com) */
  --color-green-500: #4dd973; /* Brand / Palette Token (ksenpanchenko-com) */
  --font-family-serif: var(--font-serif-loaded,"Instrument Serif"),Georgia,serif; /* Typography / Scale Token (ksenpanchenko-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in `var(--color-neutral-0)` in `:root`
- **Primary Typography Ink**: `#f4f1ec` — grounded in `var(--color-neutral-50)` in `:root`
- **Elevated Surface / Card Substrate**: `#f1f0ec` — grounded in `var(--color-neutral-100)` in `:root`
- **Interactive Accent / Highlight**: `#a8a8a6` — grounded in `var(--color-neutral-400)` in `:root`
- **Secondary / Muted Copy**: `#6b6b6b` — grounded in `var(--color-neutral-500)` in `:root`
- **Structural Hairline Border**: `#2b2b2b` — grounded in `var(--color-neutral-800)` in `:root`
- **Variable Token (`--color-neutral-950`)**: `#141414` — grounded in `var(--color-neutral-950)` in `:root`
- **Variable Token (`--color-orange-500`)**: `#ff5c2e` — grounded in `var(--color-orange-500)` in `:root`
- **Variable Token (`--color-orange-600`)**: `#e8461a` — grounded in `var(--color-orange-600)` in `:root`
- **Variable Token (`--color-green-500`)**: `#4dd973` — grounded in `var(--color-green-500)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×8165px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `300px` extracted from `ksenpanchenko-com` stylesheet
- **Padding & Gutters**: `4px` lateral canvas padding with `4px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 300px`, `gap: 4px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-height:820px)`, `@media (max-height:640px)`, `@media (max-width:1023px)`
- **Corner Radii**: `14px`, `999px`, `12%`, `11%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `GeistSans`
- **Body Font Stack**: `GeistSans Fallback`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **H1 Display Rule**: CSS variables `--type-display-size: 220px`, `--type-display-line-height: 198px`, `--type-display-letter-spacing: -6.6px`
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `14px`, `13px`, `32px`, `52px`, `12px`)
- **Body Copy Rule**: CSS variables `--type-body-lead-size: 24px`, `--type-body-lead-line-height: 31.2px`, `--type-body-lead-letter-spacing: 0px`; rule `p` (`font-size: 16px`, `line-height: 24px`)
- **Metadata & Index Rule**: CSS variables `--font-family-mono: "JetBrains Mono",ui-monospace,monospace`, `--type-display-letter-spacing: -6.6px`, `--type-heading-large-letter-spacing: 0px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `ksenpanchenko-com` (`Ksen Panchenko — UX/UI & Product Designer in Dublin · FinTech & SaaS`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.nav> — `ksenpanchenko-com`)**:
   - DOM & Selectors: Landmark `<header class="nav">` hosting `Ksen Panchenko — UX/UI & Product Des` navigation (`Work · About`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-end="1"`), and stylesheet rule `.sw__reel.is-active { opacity:1;visibility:visible;transition:opacity .55s var(--ease-out) .08... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.nav> — `ksenpanchenko-com`)` (`ksenpanchenko-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (max-height:820px)`, `@media (max-height:640px)`, `@media (max-width:1023px)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.22,1.18,.36,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `Work · About`.
2. **Hero Stage & Focal Lead (<section.hero> — `Ksen Panchenko — UX/UI & Product D`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Ksen Panchenko — UX/UI & Product Designer in Dubl...` and copy excerpt *"Available for projects"* over `#ffffff` canvas and `#2b2b2b` ink.
   - Responsive Contract: Hero stage (`1440×8165px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#2b2b2b` headline `Ksen Panchenko — UX/UI & Product Designer in Dubl...`.
3. **Primary Showcase & Content Grid (<section.sw> — `Selected work`)**:
   - DOM & Selectors: Landmark `<section class="sw">` rendering section `Selected work` with copy *"Dublin 19:22 GMT+0"*, asset references (`7cb8e1b9ab81be17-s.p.woff2`, `dbccb4a9e22cbf0d-s.p.woff2`, `e872e3f251959e82-s.p.woff2`, `kseniia-cutout.webp`), and grid rule `.sw__reel img { position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacit... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.sw> — `Selected work`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 300px`, `gap: 4px`) on desktop and Single-column vertical stack at `390px` viewport width with `4px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.philo> — `Services`)**:
   - DOM & Selectors: Landmark `<section class="philo">` framing `Services` and `Product & UX` (*"E m a i l m e Email me"*) with `#f1f0ec` surface cards, `#a8a8a6` accents, and `.sw__reel.is-active .sw__win { translate:0 0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.philo> — `Services`)` uses `14px`, `999px`, `12%`, `11%` radii, `#a8a8a6` highlights, and assets (7cb8e1b9ab81be17-s.p.woff2, dbccb4a9e22cbf0d-s.p.woff2, e872e3f251959e82-s.p.woff2).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://ksenpanchenko.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Ksen Panchenko — UX/UI & Product` footer links (`Work · About`), copy *"Gold London Design Awards 2026 · Emerald24 · UI Design"*, and `#2b2b2b` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://ksenpanchenko.com/`)` aligns to `300px` extracted from `ksenpanchenko-com` stylesheet with `4px` lateral canvas padding with `4px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Available for projects"*
- Copy Excerpt 2: *"Dublin 19:22 GMT+0"*
- Copy Excerpt 3: *"E m a i l m e Email me"*
- Copy Excerpt 4: *"Gold London Design Awards 2026 · Emerald24 · UI Design"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.22,1.18,.36,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`ksenpanchenko-com`)**:
- `.sw__reel.is-active { opacity:1;visibility:visible;transition:opacity .55s var(--ease-out) .08... }`
- `.sw__reel img { position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacit... }`
- `.sw__reel.is-active .sw__win { translate:0 0 }`
- `.sw__bar i { width:clamp(4px,.75cqw,8px);height:clamp(4px,.75cqw,8px);border-radius:9... }`
- `.sw__screen { position:relative;aspect-ratio:1600/906 }`
- **Per-Selector Transition Rules**:
- **Selector `.sw__reel`**: `transition: opacity .55s var(--ease-out),visibility 0s .55s` extracted from `ksenpanchenko-com` stylesheet.
- **Selector `.sw__reel.is-active`**: `transition: opacity .55s var(--ease-out) .08s,visibility 0s` extracted from `ksenpanchenko-com` stylesheet.
- **Selector `.cs-next__reel) .sw__reel img`**: `transition: none` extracted from `ksenpanchenko-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.sw>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `ksenpanchenko-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
