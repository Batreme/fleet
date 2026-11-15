---
title: "UI Prompt Blueprint: launch-joinautopilot-com"
date: 2026-11-15
target: "[[overview|launch-joinautopilot-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f1f2f3` / `#3cbe69`)"
---

# UI Design System & Master Generation Blueprint: launch-joinautopilot-com

> **Home** (https://launch.joinautopilot.com) — Instant access to the world's capital. Become a Pilot and launch your first fund in minutes. Join top performers managing $1.2B+ in assets.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Home** (`https://launch.joinautopilot.com`). Instant access to the world's capital. Become a Pilot and launch your first fund in minutes. Join top performers managing $1.2B+ in assets.
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f1f2f3` / `#3cbe69`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f1f2f3` (`var(--_design-system---color--primary-light)` in `:root`) paired with `#0d0d0d` primary typography and `#3cbe69` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Fkgrotesk` for display copy (`A u t o p i l o t`) with `clamp(.875rem` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.47,0,.745,.715)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `launch-joinautopilot-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `20px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f1f2f3` | `var(--_design-system---color--primary-light)` in `:root` |
| **Primary Typography Ink** | `#0d0d0d` | `var(--_design-system---color--primary-dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fcfcfc` | `var(--_design-system---color--surface-background)` in `:root` |
| **Interactive Accent / Highlight** | `#3cbe69` | `var(--_design-system---color--green)` in `:root` |
| **Secondary / Muted Copy** | `#141414` | `var(--_design-system---color--hover-on-light)` in `:root` |
| **Structural Hairline Border** | `#dcdde0` | `var(--_design-system---color--hover-on-dark)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_design-system---role--bg` | `var(--_design-system---color--surface-background)` | Canvas / Surface Token |
| `--_design-system---font--primary` | `Fkgrotesk,Arial,sans-serif` | Brand / Palette Token |
| `--_design-system---role--fg` | `var(--_design-system---color--primary-dark)` | Typography Ink Token |
| `--_design-system---font-size--body` | `clamp(.875rem,.843137rem + .130719vw,1rem)` | Typography / Scale Token |
| `--_design-system---line-height--body` | `1.3` | Typography / Scale Token |
| `--_design-system---font-weight--body` | `400` | Typography / Scale Token |
| `--_design-system---letter-spacing--body` | `-.01em` | Typography / Scale Token |
| `--_design-system---font-size--h1` | `clamp(5.75rem,4.98529rem + 3.13726vw,8.75rem)` | Typography / Scale Token |
| `--_design-system---line-height--h1` | `1` | Typography / Scale Token |
| `--_design-system---font-weight--h1` | `400` | Typography / Scale Token |
| `--_design-system---letter-spacing--h1` | `-.06em` | Typography / Scale Token |
| `--_design-system---font-size--h2` | `clamp(3.5rem,3.11765rem + 1.56863vw,5rem)` | Typography / Scale Token |
| `--_design-system---line-height--h2` | `1.02` | Typography / Scale Token |
| `--_design-system---font-weight--h2` | `400` | Typography / Scale Token |
| `--_design-system---letter-spacing--h2` | `-.05em` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Fkgrotesk`.
- **Primary Body Stack**: `clamp(.875rem`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--_design-system---font-size--h1: clamp(5.75rem,4.98529rem + 3.13726vw,8.75rem)`, `--_design-system---line-height--h1: 1`, `--_design-system---font-weight--h1: 400`.
- **Section Heading (`H2`)**: CSS variables `--_design-system---font-size--h2: clamp(3.5rem,3.11765rem + 1.56863vw,5rem)`, `--_design-system---line-height--h2: 1.02`, `--_design-system---font-weight--h2: 400`; rule `h2` (`font-size: var(--font-size-h3)`, `line-height: var(--line-height-h3-...`, `letter-spacing: var(--letter-spacing-...`).
- **Body Copy**: CSS variables `--_design-system---font-size--body: clamp(.875rem,.843137rem + .130719vw,1rem)`, `--_design-system---line-height--body: 1.3`, `--_design-system---font-weight--body: 400`; rule `,p` (`font-size: var(--font-size-body)`, `line-height: var(--line-height-body)`, `letter-spacing: var(--letter-spacing-...`, `font-weight: var(--font-we...`).
- **Metadata & Navigation Labels**: CSS variables `--_design-system---letter-spacing--body: -.01em`, `--_design-system---letter-spacing--h1: -.06em`, `--_design-system---letter-spacing--h2: -.05em`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.47,0,.745,.715)`, `cubic-bezier(.39,.575,.565,1)`, `cubic-bezier(.445,.05,.55,.95)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `launch-joinautopilot-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `launch-joinautopilot-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `launch-joinautopilot-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.47,0,.745,.715)`)**: Governs interactive state transitions across `<header.header_wrap>` and `<section.steps_wrap>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Home                                       │
│ ====================================================================== │
│ [ <header.header_wrap>     | N e w s News · F A Q FAQ · Careers · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.home_hero_wrap>                             |   │
│ | H1: A u t o p i l o t                                            |   │
│ | Substrate: #f1f2f3    | Ink: #0d0d0d    | Accent: #3cbe69        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.steps_wrap>      ) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | T h i s i s w h e r e i t g  |  | P i c k y o u r s t o c k s  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.header_wra] -> [<section.home_hero] -> [<section.steps_wra] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.home_footer_wr) | https://launch.joinautopilot.com   │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header_wrap> — `launch-joinautopilot-com`)**:
   - Landmark `<header class="header_wrap">` hosting `Home` navigation (`N e w s News · F A Q FAQ · Careers · Contact · X/Twitter`), DOM attributes (`data-wf-domain="launch.joinautopilot.com"`, `data-wf-page="6a2d51f45ce6148dcfffd71a"`, `data-wf-site="6a07168d6f6cfe1d38b6d627"`, `data-route="home"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.home_hero_wrap> — `A u t o p i l o t`)**:
   - Landmark `<section class="home_hero_wrap">` presenting display lead `A u t o p i l o t` and copy excerpt *"Access to main content"* over `#f1f2f3` canvas and `#0d0d0d` ink.
3. **Primary Showcase & Content Grid (<section.steps_wrap> — `T h i s i s w h e r e i t g e t s `)**:
   - Landmark `<section class="steps_wrap l-section">` rendering section `T h i s i s w h e r e i t g e t s f u n . This is...` with copy *"M e n u Menu C l o s e Close"*, asset references (`cdn.prod.website-files.com`, `ob-autopilot.shared.8ecce8ba9.min...`, `6a316c0692d4727f15940a67_favicon.png`, `6a316c0605a3b4d0e37557a7_favicon.png`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.billackman_wrap> — `P i c k y o u r s t o c k s . Pick`)**:
   - Landmark `<section class="billackman_wrap l-section">` framing `P i c k y o u r s t o c k s . Pick your stocks.` and `B i l l A c k m a n t o o k 1 0 y e a r s t o r a...` (*"H a l l o f F a m e Hall of Fame"*) with `#fcfcfc` surface cards, `#3cbe69` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.home_footer_wrap> — `https://launch.joinautopilot.com`)**:
   - Landmark `<footer class="home_footer_wrap l-section">` anchoring `Home` footer links (`N e w s News · F A Q FAQ · Careers · Contact · X/Twitter`), copy *"M o n e t i z a t i o n Monetization"*, and `#dcdde0` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: launch-joinautopilot-com (Home)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `launch-joinautopilot-com` (**Home** — `https://launch.joinautopilot.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f1f2f3` / `#3cbe69`).
- **Identity & Domain Context**: Instant access to the world's capital. Become a Pilot and launch your first fund in minutes. Join top performers managing $1.2B+ in assets.
- **Primary Substrate**: `#f1f2f3` (`var(--_design-system---color--primary-light)` in `:root`), **Primary Ink**: `#0d0d0d`, **Accent / Highlight**: `#3cbe69`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f1f2f3` (`var(--_design-system---color--primary-light)` in `:root`) paired with `#0d0d0d` primary typography and `#3cbe69` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Fkgrotesk` for display copy (`A u t o p i l o t`) with `clamp(.875rem` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.47,0,.745,.715)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `launch-joinautopilot-com` in your global stylesheet:

:root {
  /* Home (launch-joinautopilot-com) — Ground-Truth Extracted CSS Variables */
  --w-backdrop-animation: initial; /* Motion / Easing Token (launch-joinautopilot-com) */
  --_design-system---role--bg: var(--_design-system---color--surface-background); /* Canvas / Surface Token (launch-joinautopilot-com) */
  --_design-system---font--primary: Fkgrotesk,Arial,sans-serif; /* Brand / Palette Token (launch-joinautopilot-com) */
  --_design-system---role--fg: var(--_design-system---color--primary-dark); /* Typography Ink Token (launch-joinautopilot-com) */
  --_design-system---font-size--body: clamp(.875rem,.843137rem + .130719vw,1rem); /* Typography / Scale Token (launch-joinautopilot-com) */
  --_design-system---line-height--body: 1.3; /* Typography / Scale Token (launch-joinautopilot-com) */
  --_design-system---font-weight--body: 400; /* Typography / Scale Token (launch-joinautopilot-com) */
  --_design-system---letter-spacing--body: -.01em; /* Typography / Scale Token (launch-joinautopilot-com) */
  --_design-system---font-size--h1: clamp(5.75rem,4.98529rem + 3.13726vw,8.75rem); /* Typography / Scale Token (launch-joinautopilot-com) */
  --_design-system---line-height--h1: 1; /* Typography / Scale Token (launch-joinautopilot-com) */
  --_design-system---font-weight--h1: 400; /* Typography / Scale Token (launch-joinautopilot-com) */
  --_design-system---letter-spacing--h1: -.06em; /* Typography / Scale Token (launch-joinautopilot-com) */
  --_design-system---font-size--h2: clamp(3.5rem,3.11765rem + 1.56863vw,5rem); /* Typography / Scale Token (launch-joinautopilot-com) */
  --_design-system---line-height--h2: 1.02; /* Typography / Scale Token (launch-joinautopilot-com) */
  --_design-system---font-weight--h2: 400; /* Typography / Scale Token (launch-joinautopilot-com) */
  --_design-system---letter-spacing--h2: -.05em; /* Typography / Scale Token (launch-joinautopilot-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f1f2f3` — grounded in `var(--_design-system---color--primary-light)` in `:root`
- **Primary Typography Ink**: `#0d0d0d` — grounded in `var(--_design-system---color--primary-dark)` in `:root`
- **Elevated Surface / Card Substrate**: `#fcfcfc` — grounded in `var(--_design-system---color--surface-background)` in `:root`
- **Interactive Accent / Highlight**: `#3cbe69` — grounded in `var(--_design-system---color--green)` in `:root`
- **Secondary / Muted Copy**: `#141414` — grounded in `var(--_design-system---color--hover-on-light)` in `:root`
- **Structural Hairline Border**: `#dcdde0` — grounded in `var(--_design-system---color--hover-on-dark)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `launch-joinautopilot-com` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `20px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Fkgrotesk`
- **Body Font Stack**: `clamp(.875rem`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--_design-system---font-size--h1: clamp(5.75rem,4.98529rem + 3.13726vw,8.75rem)`, `--_design-system---line-height--h1: 1`, `--_design-system---font-weight--h1: 400`
- **H2 Section Rule**: CSS variables `--_design-system---font-size--h2: clamp(3.5rem,3.11765rem + 1.56863vw,5rem)`, `--_design-system---line-height--h2: 1.02`, `--_design-system---font-weight--h2: 400`; rule `h2` (`font-size: var(--font-size-h3)`, `line-height: var(--line-height-h3-...`, `letter-spacing: var(--letter-spacing-...`)
- **Body Copy Rule**: CSS variables `--_design-system---font-size--body: clamp(.875rem,.843137rem + .130719vw,1rem)`, `--_design-system---line-height--body: 1.3`, `--_design-system---font-weight--body: 400`; rule `,p` (`font-size: var(--font-size-body)`, `line-height: var(--line-height-body)`, `letter-spacing: var(--letter-spacing-...`, `font-weight: var(--font-we...`)
- **Metadata & Index Rule**: CSS variables `--_design-system---letter-spacing--body: -.01em`, `--_design-system---letter-spacing--h1: -.06em`, `--_design-system---letter-spacing--h2: -.05em`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `launch-joinautopilot-com` (`Home`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header_wrap> — `launch-joinautopilot-com`)**:
   - DOM & Selectors: Landmark `<header class="header_wrap">` hosting `Home` navigation (`N e w s News · F A Q FAQ · Careers · Contact · X/Twitter`), DOM attributes (`data-wf-domain="launch.joinautopilot.com"`, `data-wf-page="6a2d51f45ce6148dcfffd71a"`, `data-wf-site="6a07168d6f6cfe1d38b6d627"`, `data-route="home"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header_wrap> — `launch-joinautopilot-com`)` (`launch-joinautopilot-com`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(.47,0,.745,.715)`, `cubic-bezier(.39,.575,.565,1)`, `cubic-bezier(.445,.05,.55,.95)` transitions and links `N e w s News · F A Q FAQ · Careers · Contact · X/Twitter`.
2. **Hero Stage & Focal Lead (<section.home_hero_wrap> — `A u t o p i l o t`)**:
   - DOM & Selectors: Landmark `<section class="home_hero_wrap">` presenting display lead `A u t o p i l o t` and copy excerpt *"Access to main content"* over `#f1f2f3` canvas and `#0d0d0d` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f1f2f3` background with `#0d0d0d` headline `A u t o p i l o t`.
3. **Primary Showcase & Content Grid (<section.steps_wrap> — `T h i s i s w h e r e i t g e t s `)**:
   - DOM & Selectors: Landmark `<section class="steps_wrap l-section">` rendering section `T h i s i s w h e r e i t g e t s f u n . This is...` with copy *"M e n u Menu C l o s e Close"*, asset references (`cdn.prod.website-files.com`, `ob-autopilot.shared.8ecce8ba9.min...`, `6a316c0692d4727f15940a67_favicon.png`, `6a316c0605a3b4d0e37557a7_favicon.png`), and grid rule `summary { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.steps_wrap> — `T h i s i s w h e r e i t g e t s `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.billackman_wrap> — `P i c k y o u r s t o c k s . Pick`)**:
   - DOM & Selectors: Landmark `<section class="billackman_wrap l-section">` framing `P i c k y o u r s t o c k s . Pick your stocks.` and `B i l l A c k m a n t o o k 1 0 y e a r s t o r a...` (*"H a l l o f F a m e Hall of Fame"*) with `#fcfcfc` surface cards, `#3cbe69` accents, and `video { vertical-align:baseline;display:inline-block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.billackman_wrap> — `P i c k y o u r s t o c k s . Pick`)` uses `3px`, `100%`, `50%`, `20px` radii, `#3cbe69` highlights, and assets (cdn.prod.website-files.com, ob-autopilot.shared.8ecce8ba9.min..., 6a316c0692d4727f15940a67_favicon.png).
5. **Colophon & Global Directory Footer (<footer.home_footer_wrap> — `https://launch.joinautopilot.com`)**:
   - DOM & Selectors: Landmark `<footer class="home_footer_wrap l-section">` anchoring `Home` footer links (`N e w s News · F A Q FAQ · Careers · Contact · X/Twitter`), copy *"M o n e t i z a t i o n Monetization"*, and `#dcdde0` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.home_footer_wrap> — `https://launch.joinautopilot.com`)` aligns to `940px` extracted from `launch-joinautopilot-com` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="launch.joinautopilot.com", data-wf-page="6a2d51f45ce6148dcfffd71a", data-wf-site="6a07168d6f6cfe1d38b6d627").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Access to main content"*
- Copy Excerpt 2: *"M e n u Menu C l o s e Close"*
- Copy Excerpt 3: *"H a l l o f F a m e Hall of Fame"*
- Copy Excerpt 4: *"M o n e t i z a t i o n Monetization"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.47,0,.745,.715)`, `cubic-bezier(.39,.575,.565,1)`, `cubic-bezier(.445,.05,.55,.95)`
- **Extracted Stylesheet Rules (`launch-joinautopilot-com`)**:
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`
- `summary { display:block }`
- `video { vertical-align:baseline;display:inline-block }`
- `template { display:none }`
- `strong { font-weight:700 }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `launch-joinautopilot-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `launch-joinautopilot-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `launch-joinautopilot-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.47,0,.745,.715)`)**: Governs interactive state transitions across `<header.header_wrap>` and `<section.steps_wrap>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `launch-joinautopilot-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
