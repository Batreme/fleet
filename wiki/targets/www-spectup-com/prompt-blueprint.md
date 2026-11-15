---
title: "UI Prompt Blueprint: www-spectup-com"
date: 2026-11-15
target: "www-spectup-com"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#121212` / `#8A8A8A`)"
---

# UI Design System & Master Generation Blueprint: www-spectup-com

> **Private Capital Advisory: Capital Raising and M&A · spectup** (https://www.spectup.com/) — Private capital advisory with $760M+ advised, raised or placed since 2022: capital raising for companies and funds, fund placement and M&...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Private Capital Advisory: Capital Raising and M&A · spectup** (`https://www.spectup.com/`). Private capital advisory with $760M+ advised, raised or placed since 2022: capital raising for companies and funds, fund placement and M&...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#121212` / `#8A8A8A`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#121212` (`var(--ck-ink)` in `:root`) paired with `#FAFAFA` primary typography and `#8A8A8A` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`Private capital advisory : A c c e s`) with `A5A5A3` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `60ch` container bounds (`gap: 16px`, padding `16px`) with `cubic-bezier(.16,1,.3,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `60ch` extracted from `www-spectup-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `16px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `14px`, `999px`, `50%`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 60ch`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:721px)`, `@media (min-width:901px)`, `@media (max-width:720px)`, `@media (max-width:340px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#121212` | `var(--ck-ink)` in `:root` |
| **Primary Typography Ink** | `#FAFAFA` | `var(--ck-light)` in `:root` |
| **Elevated Surface / Card Substrate** | `#F8F32B` | `var(--ck-yellow)` in `:root` |
| **Interactive Accent / Highlight** | `#8A8A8A` | `var(--ck-grey)` in `:root` |
| **Secondary / Muted Copy** | `#A5A5A3` | `var(--ck-body)` in `:root` |
| **Structural Hairline Border** | `#8E8E8C` | `var(--ck-fine)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ck-ink` | `#121212` | Typography Ink Token |
| `--ck-light` | `#FAFAFA` | Canvas / Surface Token |
| `--ck-yellow` | `#F8F32B` | Color / Atmospheric Token |
| `--ck-line` | `rgba(250,250,250,.14)` | Color / Atmospheric Token |
| `--ck-line-2` | `rgba(250,250,250,.24)` | Color / Atmospheric Token |
| `--ck-grey` | `#8A8A8A` | Color / Atmospheric Token |
| `--ck-body` | `#A5A5A3` | Color / Atmospheric Token |
| `--ck-fine` | `#8E8E8C` | Color / Atmospheric Token |
| `--ck-mono` | `ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace` | Typography / Scale Token |
| `--ck-e` | `var(--e,cubic-bezier(.16,1,.3,1))` | Motion / Timing Token |
| `--ck-e-in` | `var(--e-in,cubic-bezier(.7,0,.84,0))` | Motion / Timing Token |
| `--ck-d1` | `320ms` | Motion / Timing Token |
| `--ck-d2` | `700ms` | Motion / Timing Token |
| `--ck-d3` | `1200ms` | Motion / Timing Token |
| `--ck-fade` | `var(--d-fade,460ms)` | Design System Custom Token |
| `--ck-rise-d` | `var(--d-rise,520ms)` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `A5A5A3`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--t-h1: clamp(30px,4.2vw,64px)`, `--kh-h1: 196.0px`; rule `.h1` (`font-size: clamp(19px,min(2.05vw,3.3vh),...`, `letter-spacing: -.018em`, `font-weight: 400`).
- **Section Heading (`H2`)**: CSS variables `--t-h2: clamp(22px,2.5vw,36px)`; rule `h2` (`font-size: clamp(24px,2.9vw,52px)`, `line-height: 1.06`, `letter-spacing: -.032em`, `font-weight: 500`).
- **Body Copy**: CSS variables `--ck-body: #A5A5A3`, `--t-body: 15px`; rule `p` (`font-size: 13px`, `line-height: 1.6`).
- **Metadata & Navigation Labels**: CSS variables `--ck-mono: ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace`, `--t-meta: 12.5px`, `--mono: ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace`; rule `.meta` (`font-size: var(--t-meta)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.7,0,.84,0)`, `cubic-bezier(.4,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.ckpanel`**: `transition: opacity var(--ck-d1) var(--ck-e-in),transform var(--ck-d1) var...` extracted from `www-spectup-com` stylesheet.
- **Selector `.ckpanel.ck-on`**: `transition: opacity var(--ck-fade) var(--ck-e),transform var(--ck-rise-d)...` extracted from `www-spectup-com` stylesheet.
- **Selector `.ckx`**: `transition: color var(--ck-d1)` extracted from `www-spectup-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<nav.mo>` and `<section.s--light>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Private Capital Advisory: Capital Raising  │
│ ====================================================================== │
│ [ <nav.mo>                 | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.kh>                                         |   │
│ | H1: Private capital advisory : A c c e s s t o p r i...          |   │
│ | Substrate: #121212    | Ink: #FAFAFA    | Accent: #8A8A8A        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.s--light>        ) max-w: 60ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | spectup’s track record       |  | How we get capital raises, M | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<nav.mo>] -> [<section.kh>] -> [<section.s--light>] |               │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.ft>           ) | https://www.spectup.com/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.mo> — `www-spectup-com`)**:
   - Landmark `<nav class="mo">` hosting `Private Capital Advisory: Capital Ra` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-nosnippet`, `data-mnbound="1"`, `data-l="The firm"`, `data-lf-cf`), and stylesheet rule `.cknote { width:min(372px,calc(100vw - 32px));padding:16px 18px 6px }`.
2. **Hero Stage & Focal Lead (<section.kh> — `Private capital advisory : A c c e`)**:
   - Landmark `<section class="kh in">` presenting display lead `Private capital advisory : A c c e s s t o p r i...` and copy excerpt *"Startup fundraising"* over `#121212` canvas and `#FAFAFA` ink.
3. **Primary Showcase & Content Grid (<section.s--light> — `spectup’s track record`)**:
   - Landmark `<section class="s--light offrest">` rendering section `spectup’s track record` with copy *"Capital introduction"*, asset references (`favicon.ico`, `favicon-32.png`, `favicon-192.png`, `apple-touch-icon.png`), and grid rule `.ckhd { display:flex;align-items:center;justify-content:space-between;gap:16px;m... }`.
4. **Interactive Detail & Feature Matrix (<section.s--light> — `How we get capital raises, M&A dea`)**:
   - Landmark `<section class="s--light s--flush">` framing `How we get capital raises, M&A deals and secondar...` and `Private capital advisory: capital raising and M&A` (*"Secondary advisory"*) with `#F8F32B` surface cards, `#8A8A8A` accents, and `.ckix { font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;font-weig... }`.
5. **Colophon & Global Directory Footer (<footer.ft> — `https://www.spectup.com/`)**:
   - Landmark `<footer class="ft has-canvas">` anchoring `Private Capital Advisory: Capita` footer links (`Overview · Index · Archive · About · Contact`), copy *"Everything we publish"*, and `#8E8E8C` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-spectup-com (Private Capital Advisory: Capital Raising and M&A · spectup)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-spectup-com` (**Private Capital Advisory: Capital Raising and M&A · spectup** — `https://www.spectup.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#121212` / `#8A8A8A`).
- **Identity & Domain Context**: Private capital advisory with $760M+ advised, raised or placed since 2022: capital raising for companies and funds, fund placement and M&...
- **Primary Substrate**: `#121212` (`var(--ck-ink)` in `:root`), **Primary Ink**: `#FAFAFA`, **Accent / Highlight**: `#8A8A8A`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#121212` (`var(--ck-ink)` in `:root`) paired with `#FAFAFA` primary typography and `#8A8A8A` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`Private capital advisory : A c c e s`) with `A5A5A3` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `60ch` container bounds (`gap: 16px`, padding `16px`) with `cubic-bezier(.16,1,.3,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-spectup-com` in your global stylesheet:

:root {
  /* Private Capital Advisory: Capital Raising and M&A · spectup (www-spectup-com) — Ground-Truth Extracted CSS Variables */
  --ck-ink: #121212; /* Typography Ink Token (www-spectup-com) */
  --ck-light: #FAFAFA; /* Canvas / Surface Token (www-spectup-com) */
  --ck-yellow: #F8F32B; /* Color / Atmospheric Token (www-spectup-com) */
  --ck-line: rgba(250,250,250,.14); /* Color / Atmospheric Token (www-spectup-com) */
  --ck-line-2: rgba(250,250,250,.24); /* Color / Atmospheric Token (www-spectup-com) */
  --ck-grey: #8A8A8A; /* Color / Atmospheric Token (www-spectup-com) */
  --ck-body: #A5A5A3; /* Color / Atmospheric Token (www-spectup-com) */
  --ck-fine: #8E8E8C; /* Color / Atmospheric Token (www-spectup-com) */
  --ck-mono: ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace; /* Typography / Scale Token (www-spectup-com) */
  --ck-e: var(--e,cubic-bezier(.16,1,.3,1)); /* Motion / Timing Token (www-spectup-com) */
  --ck-e-in: var(--e-in,cubic-bezier(.7,0,.84,0)); /* Motion / Timing Token (www-spectup-com) */
  --ck-d1: 320ms; /* Motion / Timing Token (www-spectup-com) */
  --ck-d2: 700ms; /* Motion / Timing Token (www-spectup-com) */
  --ck-d3: 1200ms; /* Motion / Timing Token (www-spectup-com) */
  --ck-fade: var(--d-fade,460ms); /* Design System Custom Token (www-spectup-com) */
  --ck-rise-d: var(--d-rise,520ms); /* Design System Custom Token (www-spectup-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#121212` — grounded in `var(--ck-ink)` in `:root`
- **Primary Typography Ink**: `#FAFAFA` — grounded in `var(--ck-light)` in `:root`
- **Elevated Surface / Card Substrate**: `#F8F32B` — grounded in `var(--ck-yellow)` in `:root`
- **Interactive Accent / Highlight**: `#8A8A8A` — grounded in `var(--ck-grey)` in `:root`
- **Secondary / Muted Copy**: `#A5A5A3` — grounded in `var(--ck-body)` in `:root`
- **Structural Hairline Border**: `#8E8E8C` — grounded in `var(--ck-fine)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `60ch` extracted from `www-spectup-com` stylesheet
- **Padding & Gutters**: `16px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 60ch`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding
- **Media Queries**: `@media (min-width:721px)`, `@media (min-width:901px)`, `@media (max-width:720px)`, `@media (max-width:340px)`
- **Corner Radii**: `14px`, `999px`, `50%`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `A5A5A3`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--t-h1: clamp(30px,4.2vw,64px)`, `--kh-h1: 196.0px`; rule `.h1` (`font-size: clamp(19px,min(2.05vw,3.3vh),...`, `letter-spacing: -.018em`, `font-weight: 400`)
- **H2 Section Rule**: CSS variables `--t-h2: clamp(22px,2.5vw,36px)`; rule `h2` (`font-size: clamp(24px,2.9vw,52px)`, `line-height: 1.06`, `letter-spacing: -.032em`, `font-weight: 500`)
- **Body Copy Rule**: CSS variables `--ck-body: #A5A5A3`, `--t-body: 15px`; rule `p` (`font-size: 13px`, `line-height: 1.6`)
- **Metadata & Index Rule**: CSS variables `--ck-mono: ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace`, `--t-meta: 12.5px`, `--mono: ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace`; rule `.meta` (`font-size: var(--t-meta)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-spectup-com` (`Private Capital Advisory: Capital Raising and M&A · spectup`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.mo> — `www-spectup-com`)**:
   - DOM & Selectors: Landmark `<nav class="mo">` hosting `Private Capital Advisory: Capital Ra` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-nosnippet`, `data-mnbound="1"`, `data-l="The firm"`, `data-lf-cf`), and stylesheet rule `.cknote { width:min(372px,calc(100vw - 32px));padding:16px 18px 6px }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.mo> — `www-spectup-com`)` (`www-spectup-com`) adapts across `@media (min-width:721px)`, `@media (min-width:901px)`, `@media (max-width:720px)`, `@media (max-width:340px)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.7,0,.84,0)`, `cubic-bezier(.4,0,1,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.kh> — `Private capital advisory : A c c e`)**:
   - DOM & Selectors: Landmark `<section class="kh in">` presenting display lead `Private capital advisory : A c c e s s t o p r i...` and copy excerpt *"Startup fundraising"* over `#121212` canvas and `#FAFAFA` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#121212` background with `#FAFAFA` headline `Private capital advisory : A c c e s s t o p r i...`.
3. **Primary Showcase & Content Grid (<section.s--light> — `spectup’s track record`)**:
   - DOM & Selectors: Landmark `<section class="s--light offrest">` rendering section `spectup’s track record` with copy *"Capital introduction"*, asset references (`favicon.ico`, `favicon-32.png`, `favicon-192.png`, `apple-touch-icon.png`), and grid rule `.ckhd { display:flex;align-items:center;justify-content:space-between;gap:16px;m... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.s--light> — `spectup’s track record`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 60ch`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `16px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.s--light> — `How we get capital raises, M&A dea`)**:
   - DOM & Selectors: Landmark `<section class="s--light s--flush">` framing `How we get capital raises, M&A deals and secondar...` and `Private capital advisory: capital raising and M&A` (*"Secondary advisory"*) with `#F8F32B` surface cards, `#8A8A8A` accents, and `.ckix { font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;font-weig... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.s--light> — `How we get capital raises, M&A dea`)` uses `14px`, `999px`, `50%`, `4px` radii, `#8A8A8A` highlights, and assets (favicon.ico, favicon-32.png, favicon-192.png).
5. **Colophon & Global Directory Footer (<footer.ft> — `https://www.spectup.com/`)**:
   - DOM & Selectors: Landmark `<footer class="ft has-canvas">` anchoring `Private Capital Advisory: Capita` footer links (`Overview · Index · Archive · About · Contact`), copy *"Everything we publish"*, and `#8E8E8C` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.ft> — `https://www.spectup.com/`)` aligns to `60ch` extracted from `www-spectup-com` stylesheet with `16px` lateral canvas padding with `16px` grid gap and attributes (data-nosnippet, data-mnbound="1", data-l="The firm").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Startup fundraising"*
- Copy Excerpt 2: *"Capital introduction"*
- Copy Excerpt 3: *"Secondary advisory"*
- Copy Excerpt 4: *"Everything we publish"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.7,0,.84,0)`, `cubic-bezier(.4,0,1,1)`
- **Extracted Stylesheet Rules (`www-spectup-com`)**:
- `.cknote { width:min(372px,calc(100vw - 32px));padding:16px 18px 6px }`
- `.ckhd { display:flex;align-items:center;justify-content:space-between;gap:16px;m... }`
- `.ckix { font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;font-weig... }`
- `.ckx svg { position:relative;width:10px;height:10px;fill:none;stroke:currentColor;s... }`
- `.ckx:hover { color:var(--ck-t1) }`
- **Per-Selector Transition Rules**:
- **Selector `.ckpanel`**: `transition: opacity var(--ck-d1) var(--ck-e-in),transform var(--ck-d1) var...` extracted from `www-spectup-com` stylesheet.
- **Selector `.ckpanel.ck-on`**: `transition: opacity var(--ck-fade) var(--ck-e),transform var(--ck-rise-d)...` extracted from `www-spectup-com` stylesheet.
- **Selector `.ckx`**: `transition: color var(--ck-d1)` extracted from `www-spectup-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<nav.mo>` and `<section.s--light>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-spectup-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
