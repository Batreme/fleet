---
title: "UI Prompt Blueprint: tribeofgiants-com"
date: 2026-11-15
target: "[[overview|tribeofgiants-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fe7624` canvas, `#111` ink, `#f89a29` accent)"
---

# UI Design System & Master Generation Blueprint: tribeofgiants-com

> **Mindset Coaching & Personal Growth — The Tribe of Giants** (https://tribeofgiants.com/) — Name the pattern that's been running your life — then outgrow it. 12 guided journeys, Rimi your AI guide, the Mirror, and a tribe that wa...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/tribeofgiants-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Mindset Coaching & Personal Growth — The Tribe of Giants** (`https://tribeofgiants.com/`). Name the pattern that's been running your life — then outgrow it. 12 guided journeys, Rimi your AI guide, the Mirror, and a tribe that wa...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fe7624` canvas, `#111` ink, `#f89a29` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fe7624` (`var(--giant-orange)` in `:root`) paired with `#111` primary typography and `#f89a29` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Merriweather` for display copy (`Name the pattern that's been running`) with `Merriweather Fallback` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `600px` container bounds (`gap: 14px`, padding `1.25rem`) with `cubic-bezier(.2,.8,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/tribeofgiants-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `600px` extracted from `tribeofgiants-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1.25rem` lateral canvas padding with `14px` grid gap.
- **Border Radius Scale**: `10px`, `6px`, `8px`, `999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 14px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.25rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:600px)`, `@media (max-width:860px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:680px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fe7624` | `var(--giant-orange)` in `:root` |
| **Primary Typography Ink** | `#42abdb` | `var(--giant-blue)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0b9444` | `var(--growth-green)` in `:root` |
| **Interactive Accent / Highlight** | `#f89a29` | `var(--legacy-peach)` in `:root` |
| **Secondary / Muted Copy** | `#3b2313` | `var(--root-brown)` in `:root` |
| **Structural Hairline Border** | `#111` | `var(--foundation-black)` in `:root` |
| **Variable Token (`--potential-white`)** | `#fff` | `var(--potential-white)` in `:root` |
| **Variable Token (`--gold`)** | `#f2b25c` | `var(--gold)` in `:root` |
| **Variable Token (`--gold-deep`)** | `#c9a96a` | `var(--gold-deep)` in `:root` |
| **Variable Token (`--eyebrow`)** | `#a8430a` | `var(--eyebrow)` in `:root` |
| **Variable Token (`--lit`)** | `#ffffff61` | `var(--lit)` in `:root` |
| **Variable Token (`--bg`)** | `#f5efe3` | `var(--bg)` in `:root` |
| **Variable Token (`--surface`)** | `#fffcf6` | `var(--surface)` in `:root` |
| **Variable Token (`--surface-2`)** | `#f4ede0` | `var(--surface-2)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--giant-orange` | `#fe7624` | Color / Atmospheric Token |
| `--giant-blue` | `#42abdb` | Color / Atmospheric Token |
| `--growth-green` | `#0b9444` | Color / Atmospheric Token |
| `--legacy-peach` | `#f89a29` | Color / Atmospheric Token |
| `--root-brown` | `#3b2313` | Color / Atmospheric Token |
| `--foundation-black` | `#111` | Canvas / Surface Token |
| `--potential-white` | `#fff` | Canvas / Surface Token |
| `--font-heading` | `Merriweather, Georgia, serif` | Typography Ink Token |
| `--font-body` | `Lato, system-ui, sans-serif` | Typography / Scale Token |
| `--gold` | `#f2b25c` | Color / Atmospheric Token |
| `--gold-deep` | `#c9a96a` | Color / Atmospheric Token |
| `--eyebrow` | `#a8430a` | Color / Atmospheric Token |
| `--lit` | `#ffffff61` | Color / Atmospheric Token |
| `--bg` | `#f5efe3` | Canvas / Surface Token |
| `--surface` | `#fffcf6` | Canvas / Surface Token |
| `--surface-2` | `#f4ede0` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Merriweather`.
- **Primary Body Stack**: `Merriweather Fallback`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(24px,4vw,32px)`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.45em`).
- **Body Copy**: CSS variables `--font-body: Lato, system-ui, sans-serif`; rule `p` (`line-height: 1.7`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 13px`, `font-weight: 700`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.18,1.3,.4,1)`, `cubic-bezier(.4,-.1,.6,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.theme-toggle`**: `transition: background .15s,transform .12s` extracted from `tribeofgiants-com` stylesheet.
- **Selector `.mj-meter>i`**: `transition: width .5s cubic-bezier(.2,.8,.2,1)` extracted from `tribeofgiants-com` stylesheet.
- **Selector `.mj-giant-bar>i`**: `transition: width .5s` extracted from `tribeofgiants-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.lp-hero-cinema>` and `<section.lp-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Mindset Coaching & Personal Growth — The T │
│ ====================================================================== │
│ [ <header.lp-hero-cinema>  | Why the Tribe · Journeys · Blog · Podc ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.lp-section>                                 |   │
│ | H1: Name the pattern that's been running your life. T...         |   │
│ | Substrate: #fe7624    | Ink: #111       | Accent: #f89a29        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.lp-section>      ) max-w: 600px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | A day inside the Tribe       |  | One honest question          | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 14px  ) | │
│ | [<header.lp-hero-ci] -> [<section.lp-sectio] -> [<section.lp-sectio] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | https://tribeofgiants.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lp-hero-cinema> — `tribeofgiants-com`)**:
   - Landmark `<header class="lp-hero-cinema">` hosting `Mindset Coaching & Personal Growth —` navigation (`Why the Tribe · Journeys · Blog · Podcast · Books`), DOM attributes (`data-si="1"`, `data-theme="dark"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `iframe { max-width:100% }`.
2. **Hero Stage & Focal Lead (<section.lp-section> — `Name the pattern that's been runni`)**:
   - Landmark `<section class="lp-section ins">` presenting display lead `Name the pattern that's been running your life. T...` and copy excerpt *"The Tribe of Giants"* over `#fe7624` canvas and `#111` ink.
3. **Primary Showcase & Content Grid (<section.lp-section> — `A day inside the Tribe`)**:
   - Landmark `<section class="lp-section fbk-section">` rendering section `A day inside the Tribe` with copy *"Home of the 12 Journeys — where every Giant was once a Small"*, asset references (`248e1dc0efc99276-s.p.0dq1pb0w2tem...`, `345c85a432359eed-s.p.24jxsbewvqxg...`, `8e451580e5e95631-s.p.0ic9f6t6i9np...`, `9be384ea93fe3f49-s.p.0oq27de-d8s-...`), and grid rule `html { background:var(--bg) }`.
4. **Interactive Detail & Feature Matrix (<article.fbk-card> — `One honest question`)**:
   - Landmark `<article class="fbk-card">` framing `One honest question` and `Your page, read back` (*"You've read the books. You've heard the podcasts. You've collecte"*) with `#0b9444` surface cards, `#f89a29` accents, and `body { background:0 0 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://tribeofgiants.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Mindset Coaching & Personal Grow` footer links (`Why the Tribe · Journeys · Blog · Podcast · Books`), copy *"Join free, for life. Your seat in the Tribe, Journey 1 and t"*, and `#111` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: tribeofgiants-com (Mindset Coaching & Personal Growth — The Tribe of Giants)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `tribeofgiants-com` (**Mindset Coaching & Personal Growth — The Tribe of Giants** — `https://tribeofgiants.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fe7624` canvas, `#111` ink, `#f89a29` accent).
- **Identity & Domain Context**: Name the pattern that's been running your life — then outgrow it. 12 guided journeys, Rimi your AI guide, the Mirror, and a tribe that wa...
- **Primary Substrate**: `#fe7624` (`var(--giant-orange)` in `:root`), **Primary Ink**: `#111`, **Accent / Highlight**: `#f89a29`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fe7624` (`var(--giant-orange)` in `:root`) paired with `#111` primary typography and `#f89a29` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Merriweather` for display copy (`Name the pattern that's been running`) with `Merriweather Fallback` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `600px` container bounds (`gap: 14px`, padding `1.25rem`) with `cubic-bezier(.2,.8,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `tribeofgiants-com` in your global stylesheet:

:root {
  /* Mindset Coaching & Personal Growth — The Tribe of Giants (tribeofgiants-com) — Ground-Truth Extracted CSS Variables */
  --giant-orange: #fe7624; /* Color / Atmospheric Token (tribeofgiants-com) */
  --giant-blue: #42abdb; /* Color / Atmospheric Token (tribeofgiants-com) */
  --growth-green: #0b9444; /* Color / Atmospheric Token (tribeofgiants-com) */
  --legacy-peach: #f89a29; /* Color / Atmospheric Token (tribeofgiants-com) */
  --root-brown: #3b2313; /* Color / Atmospheric Token (tribeofgiants-com) */
  --foundation-black: #111; /* Canvas / Surface Token (tribeofgiants-com) */
  --potential-white: #fff; /* Canvas / Surface Token (tribeofgiants-com) */
  --font-heading: Merriweather, Georgia, serif; /* Typography Ink Token (tribeofgiants-com) */
  --font-body: Lato, system-ui, sans-serif; /* Typography / Scale Token (tribeofgiants-com) */
  --gold: #f2b25c; /* Color / Atmospheric Token (tribeofgiants-com) */
  --gold-deep: #c9a96a; /* Color / Atmospheric Token (tribeofgiants-com) */
  --eyebrow: #a8430a; /* Color / Atmospheric Token (tribeofgiants-com) */
  --lit: #ffffff61; /* Color / Atmospheric Token (tribeofgiants-com) */
  --bg: #f5efe3; /* Canvas / Surface Token (tribeofgiants-com) */
  --surface: #fffcf6; /* Canvas / Surface Token (tribeofgiants-com) */
  --surface-2: #f4ede0; /* Canvas / Surface Token (tribeofgiants-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fe7624` — grounded in `var(--giant-orange)` in `:root`
- **Primary Typography Ink**: `#42abdb` — grounded in `var(--giant-blue)` in `:root`
- **Elevated Surface / Card Substrate**: `#0b9444` — grounded in `var(--growth-green)` in `:root`
- **Interactive Accent / Highlight**: `#f89a29` — grounded in `var(--legacy-peach)` in `:root`
- **Secondary / Muted Copy**: `#3b2313` — grounded in `var(--root-brown)` in `:root`
- **Structural Hairline Border**: `#111` — grounded in `var(--foundation-black)` in `:root`
- **Variable Token (`--potential-white`)**: `#fff` — grounded in `var(--potential-white)` in `:root`
- **Variable Token (`--gold`)**: `#f2b25c` — grounded in `var(--gold)` in `:root`
- **Variable Token (`--gold-deep`)**: `#c9a96a` — grounded in `var(--gold-deep)` in `:root`
- **Variable Token (`--eyebrow`)**: `#a8430a` — grounded in `var(--eyebrow)` in `:root`
- **Variable Token (`--lit`)**: `#ffffff61` — grounded in `var(--lit)` in `:root`
- **Variable Token (`--bg`)**: `#f5efe3` — grounded in `var(--bg)` in `:root`
- **Variable Token (`--surface`)**: `#fffcf6` — grounded in `var(--surface)` in `:root`
- **Variable Token (`--surface-2`)**: `#f4ede0` — grounded in `var(--surface-2)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `600px` extracted from `tribeofgiants-com` stylesheet
- **Padding & Gutters**: `1.25rem` lateral canvas padding with `14px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 14px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.25rem` horizontal padding
- **Media Queries**: `@media (max-width:600px)`, `@media (max-width:860px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:680px)`
- **Corner Radii**: `10px`, `6px`, `8px`, `999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Merriweather`
- **Body Font Stack**: `Merriweather Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: clamp(24px,4vw,32px)`)
- **H2 Section Rule**: rule `h2` (`font-size: 1.45em`)
- **Body Copy Rule**: CSS variables `--font-body: Lato, system-ui, sans-serif`; rule `p` (`line-height: 1.7`)
- **Metadata & Index Rule**: rule `small` (`font-size: 13px`, `font-weight: 700`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `tribeofgiants-com` (`Mindset Coaching & Personal Growth — The Tribe of Giants`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lp-hero-cinema> — `tribeofgiants-com`)**:
   - DOM & Selectors: Landmark `<header class="lp-hero-cinema">` hosting `Mindset Coaching & Personal Growth —` navigation (`Why the Tribe · Journeys · Blog · Podcast · Books`), DOM attributes (`data-si="1"`, `data-theme="dark"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `iframe { max-width:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lp-hero-cinema> — `tribeofgiants-com`)` (`tribeofgiants-com`) adapts across `@media (max-width:600px)`, `@media (max-width:860px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:680px)` with `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.18,1.3,.4,1)`, `cubic-bezier(.4,-.1,.6,1)` transitions and links `Why the Tribe · Journeys · Blog · Podcast · Books`.
2. **Hero Stage & Focal Lead (<section.lp-section> — `Name the pattern that's been runni`)**:
   - DOM & Selectors: Landmark `<section class="lp-section ins">` presenting display lead `Name the pattern that's been running your life. T...` and copy excerpt *"The Tribe of Giants"* over `#fe7624` canvas and `#111` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fe7624` background with `#111` headline `Name the pattern that's been running your life. T...`.
3. **Primary Showcase & Content Grid (<section.lp-section> — `A day inside the Tribe`)**:
   - DOM & Selectors: Landmark `<section class="lp-section fbk-section">` rendering section `A day inside the Tribe` with copy *"Home of the 12 Journeys — where every Giant was once a Small"*, asset references (`248e1dc0efc99276-s.p.0dq1pb0w2tem...`, `345c85a432359eed-s.p.24jxsbewvqxg...`, `8e451580e5e95631-s.p.0ic9f6t6i9np...`, `9be384ea93fe3f49-s.p.0oq27de-d8s-...`), and grid rule `html { background:var(--bg) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.lp-section> — `A day inside the Tribe`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 14px`) on desktop and Single-column vertical stack at `390px` viewport width with `1.25rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.fbk-card> — `One honest question`)**:
   - DOM & Selectors: Landmark `<article class="fbk-card">` framing `One honest question` and `Your page, read back` (*"You've read the books. You've heard the podcasts. You've collecte"*) with `#0b9444` surface cards, `#f89a29` accents, and `body { background:0 0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.fbk-card> — `One honest question`)` uses `10px`, `6px`, `8px`, `999px` radii, `#f89a29` highlights, and assets (248e1dc0efc99276-s.p.0dq1pb0w2tem..., 345c85a432359eed-s.p.24jxsbewvqxg..., 8e451580e5e95631-s.p.0ic9f6t6i9np...).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://tribeofgiants.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `Mindset Coaching & Personal Grow` footer links (`Why the Tribe · Journeys · Blog · Podcast · Books`), copy *"Join free, for life. Your seat in the Tribe, Journey 1 and t"*, and `#111` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://tribeofgiants.com/`)` aligns to `600px` extracted from `tribeofgiants-com` stylesheet with `1.25rem` lateral canvas padding with `14px` grid gap and attributes (data-si="1", data-theme="dark", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"The Tribe of Giants"*
- Copy Excerpt 2: *"Home of the 12 Journeys — where every Giant was once a Small"*
- Copy Excerpt 3: *"You've read the books. You've heard the podcasts. You've collected insights that e..."*
- Copy Excerpt 4: *"Join free, for life. Your seat in the Tribe, Journey 1 and the daily Giant Quest a..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.18,1.3,.4,1)`, `cubic-bezier(.4,-.1,.6,1)`
- **Extracted Stylesheet Rules (`tribeofgiants-com`)**:
- `iframe { max-width:100% }`
- `html { background:var(--bg) }`
- `body { background:0 0 }`
- `button { font-family:var(--font-body);cursor:pointer }`
- `button:disabled { cursor:not-allowed;opacity:.55 }`
- **Per-Selector Transition Rules**:
- **Selector `.theme-toggle`**: `transition: background .15s,transform .12s` extracted from `tribeofgiants-com` stylesheet.
- **Selector `.mj-meter>i`**: `transition: width .5s cubic-bezier(.2,.8,.2,1)` extracted from `tribeofgiants-com` stylesheet.
- **Selector `.mj-giant-bar>i`**: `transition: width .5s` extracted from `tribeofgiants-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.lp-hero-cinema>` and `<section.lp-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `tribeofgiants-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
