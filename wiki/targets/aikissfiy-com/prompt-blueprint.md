---
title: "UI Prompt Blueprint: aikissfiy-com"
date: 2026-11-15
target: "[[overview|aikissfiy-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#0f172a` ink, `#64748b` accent)"
---

# UI Design System & Master Generation Blueprint: aikissfiy-com

> **Free AI Kissing Video Generator: Create AI Kiss Videos Online - AIKissfiy** (https://aikissfiy.com) — Description: AIKissfiy creates realistic AI kissing videos from your photos. Choose different kiss styles, keep faces recognizable, and e...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/aikissfiy-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Free AI Kissing Video Generator: Create AI Kiss Videos Online - AIKissfiy** (`https://aikissfiy.com`). Description: AIKissfiy creates realistic AI kissing videos from your photos. Choose different kiss styles, keep faces recognizable, and e...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#0f172a` ink, `#64748b` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--aikiss-surface-solid)` in `:root`) paired with `#0f172a` primary typography and `#64748b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Plus Jakarta Sans` for display copy (`Free AI Kissing Video Generator`) with `Inter` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `800px` container bounds (`gap: .5rem`, padding `13px`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/aikissfiy-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `800px` extracted from `aikissfiy-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `13px` lateral canvas padding with `.5rem` grid gap.
- **Border Radius Scale**: `27px`, `9999px`, `30px`, `.75rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 800px`, `gap: .5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `13px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:768px)`, `@media (min-width:1280px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1024px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--aikiss-surface-solid)` in `:root` |
| **Primary Typography Ink** | `#0f172a` | `var(--aikiss-text)` in `:root` |
| **Elevated Surface / Card Substrate** | `#475569` | `var(--aikiss-muted)` in `:root` |
| **Interactive Accent / Highlight** | `#64748b` | `var(--aikiss-soft-muted)` in `:root` |
| **Secondary / Muted Copy** | `#6c63ff` | `var(--halo-border-fallback)` in `:root` |
| **Structural Hairline Border** | `#ffdce5` | `var(--hologram-pink)` in `:root` |
| **Variable Token (`--gradient-primary`)** | `#8b81ff` | `var(--gradient-primary)` in `:root` |
| **Variable Token (`--gradient-primary`)** | `#b941ff` | `var(--gradient-primary)` in `:root` |
| **Variable Token (`--gradient-primary`)** | `#ec4899` | `var(--gradient-primary)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `Inter,system-ui,sans-serif` | Typography / Scale Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--aikiss-section-bg` | `transparent` | Canvas / Surface Token |
| `--aikiss-surface-solid` | `#fff` | Canvas / Surface Token |
| `--aikiss-surface-muted` | `rgba(248,250,252,.82)` | Canvas / Surface Token |
| `--aikiss-border` | `rgba(99,102,241,.2)` | Elevation / Border Token |
| `--aikiss-border-strong` | `rgba(99,102,241,.34)` | Elevation / Border Token |
| `--aikiss-text` | `#0f172a` | Typography Ink Token |
| `--aikiss-muted` | `#475569` | Color / Atmospheric Token |
| `--aikiss-soft-muted` | `#64748b` | Color / Atmospheric Token |
| `--aikiss-glow-primary` | `rgba(108,99,255,.2)` | Brand / Palette Token |
| `--aikiss-glow-secondary` | `rgba(236,72,153,.14)` | Brand / Palette Token |
| `--gradient-primary` | `linear-gradient(135deg,#6c63ff,#8b81ff 30%,#b941ff 66%,#ec4899)` | Brand / Palette Token |
| `--aikiss-inner-highlight` | `hsla(0,0%,100%,.78)` | Canvas / Surface Token |
| `--aikiss-shadow` | `0 24px 60px rgba(15,23,42,.1)` | Elevation / Border Token |
| `--aikiss-tool-shell` | `hsla(0,0%,100%,.58)` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Plus Jakarta Sans`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: 1.11111`, `--text-5xl: 3rem`; rule `h1` (`font-size: 2em!important`).
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`, `--text-3xl: 1.875rem`; rule `h2` (`line-height: 1.33`, `font-weight: 600`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`, `--ak-font-size-base: 14px`.
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1.33333`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(0,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `guage-popover-leave-active[data-v...`**: `transition: opacity .12s ease,transform .12s ease` extracted from `aikissfiy-com` stylesheet.
- **Selector `.overlay-scrollbar__thumb[data-v-...`**: `transition: background-color .15s ease,width .15s ease` extracted from `aikissfiy-com` stylesheet.
- **Selector `.btn:before`**: `transition: .5s` extracted from `aikissfiy-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.navigate-new>` and `<section.flex>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Free AI Kissing Video Generator: Create AI │
│ ====================================================================== │
│ [ <header.navigate-new>    | Home · Nano Banana Pro · AI Effects    ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.flex>                                       |   │
│ | H1: Free AI Kissing Video Generator                              |   │
│ | Substrate: #fff       | Ink: #0f172a    | Accent: #64748b        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.flex>            ) max-w: 800px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Realistic                    |  | Diverse                      | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .5rem ) | │
│ | [<header.navigate-n] -> [<section.flex>] -> [<section.flex>] |       │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.w-full>       ) | https://aikissfiy.com              │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.navigate-new> — `aikissfiy-com`)**:
   - Landmark `<header class="navigate-new sticky">` hosting `Free AI Kissing Video Generator: Cre` navigation (`Home · Nano Banana Pro · AI Effects`), DOM attributes (`data-hid="page-structured-data"`, `data-gtag`, `data-v-8a6150fd`, `data-v-a6b3f275`), and stylesheet rule `before { border:1px solid hsla(0,0%,100%,.68);border-radius:27px;content:"";inset... }`.
2. **Hero Stage & Focal Lead (<section.flex> — `Free AI Kissing Video Generator`)**:
   - Landmark `<section class="flex flex-col">` presenting display lead `Free AI Kissing Video Generator` and copy excerpt *"AI Kissing Generator"* over `#fff` canvas and `#0f172a` ink.
3. **Primary Showcase & Content Grid (<section.flex> — `Realistic`)**:
   - Landmark `<section class="flex flex-col">` rendering section `Realistic` with copy *"Love Compatibility"*, asset references (`cdn.aikissfiy.com`, `entry.D5yMvS4u.css`, `OverlayScrollbar.CrLIJdLh.css`, `LanguageSwitch.BsPr10ru.css`), and grid rule `webkit-scrollbar { display:none }`.
4. **Interactive Detail & Feature Matrix (<section.flex> — `Diverse`)**:
   - Landmark `<section class="flex flex-col">` framing `Diverse` and `Fast` (*"AI Character Generator"*) with `#475569` surface cards, `#64748b` accents, and `body { line-height:inherit;margin:0 }`.
5. **Colophon & Global Directory Footer (<footer.w-full> — `https://aikissfiy.com`)**:
   - Landmark `<footer class="w-full border-t">` anchoring `Free AI Kissing Video Generator:` footer links (`Home · Nano Banana Pro · AI Effects`), copy *"AI Kissing Generator Hot"*, and `#ffdce5` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: aikissfiy-com (Free AI Kissing Video Generator: Create AI Kiss Videos Online - AIKissfiy)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `aikissfiy-com` (**Free AI Kissing Video Generator: Create AI Kiss Videos Online - AIKissfiy** — `https://aikissfiy.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#0f172a` ink, `#64748b` accent).
- **Identity & Domain Context**: Description: AIKissfiy creates realistic AI kissing videos from your photos. Choose different kiss styles, keep faces recognizable, and e...
- **Primary Substrate**: `#fff` (`var(--aikiss-surface-solid)` in `:root`), **Primary Ink**: `#0f172a`, **Accent / Highlight**: `#64748b`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--aikiss-surface-solid)` in `:root`) paired with `#0f172a` primary typography and `#64748b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Plus Jakarta Sans` for display copy (`Free AI Kissing Video Generator`) with `Inter` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `800px` container bounds (`gap: .5rem`, padding `13px`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `aikissfiy-com` in your global stylesheet:

:root {
  /* Free AI Kissing Video Generator: Create AI Kiss Videos Online - AIKissfiy (aikissfiy-com) — Ground-Truth Extracted CSS Variables */
  --font-sans: Inter,system-ui,sans-serif; /* Typography / Scale Token (aikissfiy-com) */
  --default-font-family: var(--font-sans); /* Typography / Scale Token (aikissfiy-com) */
  --aikiss-section-bg: transparent; /* Canvas / Surface Token (aikissfiy-com) */
  --aikiss-surface-solid: #fff; /* Canvas / Surface Token (aikissfiy-com) */
  --aikiss-surface-muted: rgba(248,250,252,.82); /* Canvas / Surface Token (aikissfiy-com) */
  --aikiss-border: rgba(99,102,241,.2); /* Elevation / Border Token (aikissfiy-com) */
  --aikiss-border-strong: rgba(99,102,241,.34); /* Elevation / Border Token (aikissfiy-com) */
  --aikiss-text: #0f172a; /* Typography Ink Token (aikissfiy-com) */
  --aikiss-muted: #475569; /* Color / Atmospheric Token (aikissfiy-com) */
  --aikiss-soft-muted: #64748b; /* Color / Atmospheric Token (aikissfiy-com) */
  --aikiss-glow-primary: rgba(108,99,255,.2); /* Brand / Palette Token (aikissfiy-com) */
  --aikiss-glow-secondary: rgba(236,72,153,.14); /* Brand / Palette Token (aikissfiy-com) */
  --gradient-primary: linear-gradient(135deg,#6c63ff,#8b81ff 30%,#b941ff 66%,#ec4899); /* Brand / Palette Token (aikissfiy-com) */
  --aikiss-inner-highlight: hsla(0,0%,100%,.78); /* Canvas / Surface Token (aikissfiy-com) */
  --aikiss-shadow: 0 24px 60px rgba(15,23,42,.1); /* Elevation / Border Token (aikissfiy-com) */
  --aikiss-tool-shell: hsla(0,0%,100%,.58); /* Color / Atmospheric Token (aikissfiy-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--aikiss-surface-solid)` in `:root`
- **Primary Typography Ink**: `#0f172a` — grounded in `var(--aikiss-text)` in `:root`
- **Elevated Surface / Card Substrate**: `#475569` — grounded in `var(--aikiss-muted)` in `:root`
- **Interactive Accent / Highlight**: `#64748b` — grounded in `var(--aikiss-soft-muted)` in `:root`
- **Secondary / Muted Copy**: `#6c63ff` — grounded in `var(--halo-border-fallback)` in `:root`
- **Structural Hairline Border**: `#ffdce5` — grounded in `var(--hologram-pink)` in `:root`
- **Variable Token (`--gradient-primary`)**: `#8b81ff` — grounded in `var(--gradient-primary)` in `:root`
- **Variable Token (`--gradient-primary`)**: `#b941ff` — grounded in `var(--gradient-primary)` in `:root`
- **Variable Token (`--gradient-primary`)**: `#ec4899` — grounded in `var(--gradient-primary)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `800px` extracted from `aikissfiy-com` stylesheet
- **Padding & Gutters**: `13px` lateral canvas padding with `.5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 800px`, `gap: .5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `13px` horizontal padding
- **Media Queries**: `@media (min-width:768px)`, `@media (min-width:1280px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1024px)`
- **Corner Radii**: `27px`, `9999px`, `30px`, `.75rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Plus Jakarta Sans`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: 1.11111`, `--text-5xl: 3rem`; rule `h1` (`font-size: 2em!important`)
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`, `--text-3xl: 1.875rem`; rule `h2` (`line-height: 1.33`, `font-weight: 600`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`, `--ak-font-size-base: 14px`
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1.33333`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `aikissfiy-com` (`Free AI Kissing Video Generator: Create AI Kiss Videos Online - AIKissfiy`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.navigate-new> — `aikissfiy-com`)**:
   - DOM & Selectors: Landmark `<header class="navigate-new sticky">` hosting `Free AI Kissing Video Generator: Cre` navigation (`Home · Nano Banana Pro · AI Effects`), DOM attributes (`data-hid="page-structured-data"`, `data-gtag`, `data-v-8a6150fd`, `data-v-a6b3f275`), and stylesheet rule `before { border:1px solid hsla(0,0%,100%,.68);border-radius:27px;content:"";inset... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.navigate-new> — `aikissfiy-com`)` (`aikissfiy-com`) adapts across `@media (min-width:768px)`, `@media (min-width:1280px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1024px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(0,0,.2,1)` transitions and links `Home · Nano Banana Pro · AI Effects`.
2. **Hero Stage & Focal Lead (<section.flex> — `Free AI Kissing Video Generator`)**:
   - DOM & Selectors: Landmark `<section class="flex flex-col">` presenting display lead `Free AI Kissing Video Generator` and copy excerpt *"AI Kissing Generator"* over `#fff` canvas and `#0f172a` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fff` background with `#0f172a` headline `Free AI Kissing Video Generator`.
3. **Primary Showcase & Content Grid (<section.flex> — `Realistic`)**:
   - DOM & Selectors: Landmark `<section class="flex flex-col">` rendering section `Realistic` with copy *"Love Compatibility"*, asset references (`cdn.aikissfiy.com`, `entry.D5yMvS4u.css`, `OverlayScrollbar.CrLIJdLh.css`, `LanguageSwitch.BsPr10ru.css`), and grid rule `webkit-scrollbar { display:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.flex> — `Realistic`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 800px`, `gap: .5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `13px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.flex> — `Diverse`)**:
   - DOM & Selectors: Landmark `<section class="flex flex-col">` framing `Diverse` and `Fast` (*"AI Character Generator"*) with `#475569` surface cards, `#64748b` accents, and `body { line-height:inherit;margin:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.flex> — `Diverse`)` uses `27px`, `9999px`, `30px`, `.75rem` radii, `#64748b` highlights, and assets (cdn.aikissfiy.com, entry.D5yMvS4u.css, OverlayScrollbar.CrLIJdLh.css).
5. **Colophon & Global Directory Footer (<footer.w-full> — `https://aikissfiy.com`)**:
   - DOM & Selectors: Landmark `<footer class="w-full border-t">` anchoring `Free AI Kissing Video Generator:` footer links (`Home · Nano Banana Pro · AI Effects`), copy *"AI Kissing Generator Hot"*, and `#ffdce5` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.w-full> — `https://aikissfiy.com`)` aligns to `800px` extracted from `aikissfiy-com` stylesheet with `13px` lateral canvas padding with `.5rem` grid gap and attributes (data-hid="page-structured-data", data-gtag, data-v-8a6150fd).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"AI Kissing Generator"*
- Copy Excerpt 2: *"Love Compatibility"*
- Copy Excerpt 3: *"AI Character Generator"*
- Copy Excerpt 4: *"AI Kissing Generator Hot"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(0,0,.2,1)`
- **Extracted Stylesheet Rules (`aikissfiy-com`)**:
- `before { border:1px solid hsla(0,0%,100%,.68);border-radius:27px;content:"";inset... }`
- `webkit-scrollbar { display:none }`
- `body { line-height:inherit;margin:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- **Per-Selector Transition Rules**:
- **Selector `guage-popover-leave-active[data-v...`**: `transition: opacity .12s ease,transform .12s ease` extracted from `aikissfiy-com` stylesheet.
- **Selector `.overlay-scrollbar__thumb[data-v-...`**: `transition: background-color .15s ease,width .15s ease` extracted from `aikissfiy-com` stylesheet.
- **Selector `.btn:before`**: `transition: .5s` extracted from `aikissfiy-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.navigate-new>` and `<section.flex>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `aikissfiy-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
