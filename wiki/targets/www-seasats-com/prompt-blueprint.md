---
title: "UI Prompt Blueprint: www-seasats-com"
date: 2026-11-15
target: "[[overview|www-seasats-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#2b3922` / `#4e9a85`)"
---

# UI Design System & Master Generation Blueprint: www-seasats-com

> **Seasats · Ocean Autonomy That Works** (https://www.seasats.com/) — Missions completed for defense, science, and commercial customers around the world.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-seasats-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Seasats · Ocean Autonomy That Works** (`https://www.seasats.com/`). Missions completed for defense, science, and commercial customers around the world.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#2b3922` / `#4e9a85`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#2b3922` (`var(--icon-background)` in `:root`) paired with `#fff` primary typography and `#4e9a85` accents.
  - **Extracted Typographic Hierarchy**: Pairs `seasonMix` for display copy (`Ocean Autonomy That Works`) with `seasonMix Fallback` and `supplyMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1023px` container bounds (`gap: 3.2rem`, padding `.4rem`) with `cubic-bezier(.215,.61,.355,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-seasats-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1023px` extracted from `www-seasats-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.4rem` lateral canvas padding with `3.2rem` grid gap.
- **Border Radius Scale**: `var(--radius)`, `.4rem`, `.2rem`, `1.2rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023px`, `gap: 3.2rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.4rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:1023px)`, `@media screen and (max-width:519px)`, `@media screen and (min-width:1024px)`, `@media screen and (min-width:1024px)and (pointer:coarse)and (hov...`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#2b3922` | `var(--icon-background)` in `:root` |
| **Primary Typography Ink** | `#fffdfd` | `var(--icon-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--colorText)` in `:root` |
| **Interactive Accent / Highlight** | `#4e9a85` | `var(--modal-barBackgroundColor)` in `:root` |
| **Secondary / Muted Copy** | `#e3ede4` | `var(--button-background)` in `:root` |
| **Structural Hairline Border** | `#232323` | `var(--formField-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--icon-background` | `#2b3922` | Canvas / Surface Token |
| `--icon-color` | `#fffdfd` | Brand / Palette Token |
| `--icon-size` | `3rem` | Layout / Spatial Grid Token |
| `--icon-progress` | `1` | Design System Custom Token |
| `--colorText` | `#fff` | Typography Ink Token |
| `--button-outline` | `#fffdfd` | Elevation / Border Token |
| `--gridLayout-columns` | `var(--columns)` | Layout / Spatial Grid Token |
| `--button-maskPadding` | `0.1rem` | Layout / Spatial Grid Token |
| `--button-maskFade` | `0.1rem` | Dimension / Scale Token |
| `--paddingTop` | `6.4rem` | Layout / Spatial Grid Token |
| `--paddingBottom` | `6.4rem` | Layout / Spatial Grid Token |
| `--modal-contentMaxWidth` | `60.8rem` | Layout / Spatial Grid Token |
| `--modal-contentBackgroundColor` | `#fffdfd` | Canvas / Surface Token |
| `--modal-barBackgroundColor` | `#4e9a85` | Canvas / Surface Token |
| `--modal-barColor` | `#fffdfd` | Brand / Palette Token |
| `--button-background` | `#e3ede4` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `seasonMix`.
- **Primary Body Stack**: `seasonMix Fallback`.
- **Technical / Metadata Stack**: `supplyMono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 4.8rem`, `line-height: 1`, `letter-spacing: -.01em`, `font-weight: 400`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2.4rem`, `line-height: 1.2`, `letter-spacing: 0`, `font-weight: 400`).
- **Body Copy**: CSS variables `--body-adjustOffset: calc(59.8rem / -2)`, `--body-adjustScale: 0.66`, `--body-adjustScalePrecise: 0.585`.
- **Metadata & Navigation Labels**: CSS variables `--fontSupplyMono: "supplyMono","supplyMono Fallback",monospace`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.19,1,.22,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.AnimatedText_char__T7_D3`**: `transition: calc(.6s - var(--char-amt)*12ms) cubic-bezier(.215,.61,.355,1)` extracted from `www-seasats-com` stylesheet.
- **Selector `Button_icon__6so9o[data-icon=plus...`**: `transition: transform .5s ease` extracted from `www-seasats-com` stylesheet.
- **Selector `on_icon__6so9o[data-icon=arrow-ri...`**: `transition: .5s ease` extracted from `www-seasats-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.215,.61,.355,1)`)**: Governs interactive state transitions across `<header.Header_container__U6gzw>` and `<main.browser-ui-overlay--top>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Seasats · Ocean Autonomy That Works        │
│ ====================================================================== │
│ [ <header.Header_container | Home · 01 Capabilities · 02 Past Missi ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.browser-ui-overlay>                            |   │
│ | H1: Ocean Autonomy That Works                                    |   │
│ | Substrate: #2b3922    | Ink: #fff       | Accent: #4e9a85        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.browser-ui-overlay--) max-w: 1023px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Deploy in minutes.           |  | Detect from miles.           | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 3.2rem) | │
│ | [<header.Header_con] -> [<main.browser-ui-o] -> [<main.browser-ui-o] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://www.seasats.com/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.Header_container__U6gzw> — `www-seasats-com`)**:
   - Landmark `<header class="Header_container__U6gzw">` hosting `Seasats · Ocean Autonomy That Works` navigation (`Home · 01 Capabilities · 02 Past Missions · Products · 01 Comparison`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.not-found_title__bgpas { font-size:min(36rem,36vh) }`.
2. **Hero Stage & Focal Lead (<main.browser-ui-overlay> — `Ocean Autonomy That Works`)**:
   - Landmark `<main class="browser-ui-overlay">` presenting display lead `Ocean Autonomy That Works` and copy excerpt *"Ocean Autonomy That Works"* over `#2b3922` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.browser-ui-overlay--top> — `Deploy in minutes.`)**:
   - Landmark `<main class="browser-ui-overlay--top">` rendering section `Deploy in minutes.` with copy *"E x p l o r e p r o d u c t s E x p l o r e p r o d u c t s"*, asset references (`d11d81b0342c0709.css`, `a14bc365605f91b3.css`, `110e11ba57841c1c.css`, `5ef63a433e26978c.css`), and grid rule `.not-found_media__ko4tq { position:absolute;inset:0;background-image:linear-gradient(180deg,1d344a... }`.
4. **Interactive Detail & Feature Matrix (<main.ThemeBackground_background__xCT8k> — `Detect from miles.`)**:
   - Landmark `<main class="ThemeBackground_background__xCT8k">` framing `Detect from miles.` and `React at once.` (*"E x p l o r e p r o d u c t s"*) with `#fff` surface cards, `#4e9a85` accents, and `.AnimatedText_animatedText__MS50q { display:block;position:relative }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.seasats.com/`)**:
   - Landmark `<footer class="footer Footer_container__kRlyj">` anchoring `Seasats · Ocean Autonomy That Wo` footer links (`Home · 01 Capabilities · 02 Past Missions · Products · 01 Comparison`), copy *"The coordinates of the ghost fleet."*, and `#232323` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-seasats-com (Seasats · Ocean Autonomy That Works)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-seasats-com` (**Seasats · Ocean Autonomy That Works** — `https://www.seasats.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#2b3922` / `#4e9a85`).
- **Identity & Domain Context**: Missions completed for defense, science, and commercial customers around the world.
- **Primary Substrate**: `#2b3922` (`var(--icon-background)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#4e9a85`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#2b3922` (`var(--icon-background)` in `:root`) paired with `#fff` primary typography and `#4e9a85` accents.
  - **Extracted Typographic Hierarchy**: Pairs `seasonMix` for display copy (`Ocean Autonomy That Works`) with `seasonMix Fallback` and `supplyMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1023px` container bounds (`gap: 3.2rem`, padding `.4rem`) with `cubic-bezier(.215,.61,.355,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-seasats-com` in your global stylesheet:

:root {
  /* Seasats · Ocean Autonomy That Works (www-seasats-com) — Ground-Truth Extracted CSS Variables */
  --icon-background: #2b3922; /* Canvas / Surface Token (www-seasats-com) */
  --icon-color: #fffdfd; /* Brand / Palette Token (www-seasats-com) */
  --icon-size: 3rem; /* Layout / Spatial Grid Token (www-seasats-com) */
  --icon-progress: 1; /* Design System Custom Token (www-seasats-com) */
  --colorText: #fff; /* Typography Ink Token (www-seasats-com) */
  --button-outline: #fffdfd; /* Elevation / Border Token (www-seasats-com) */
  --gridLayout-columns: var(--columns); /* Layout / Spatial Grid Token (www-seasats-com) */
  --button-maskPadding: 0.1rem; /* Layout / Spatial Grid Token (www-seasats-com) */
  --button-maskFade: 0.1rem; /* Dimension / Scale Token (www-seasats-com) */
  --paddingTop: 6.4rem; /* Layout / Spatial Grid Token (www-seasats-com) */
  --paddingBottom: 6.4rem; /* Layout / Spatial Grid Token (www-seasats-com) */
  --modal-contentMaxWidth: 60.8rem; /* Layout / Spatial Grid Token (www-seasats-com) */
  --modal-contentBackgroundColor: #fffdfd; /* Canvas / Surface Token (www-seasats-com) */
  --modal-barBackgroundColor: #4e9a85; /* Canvas / Surface Token (www-seasats-com) */
  --modal-barColor: #fffdfd; /* Brand / Palette Token (www-seasats-com) */
  --button-background: #e3ede4; /* Canvas / Surface Token (www-seasats-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#2b3922` — grounded in `var(--icon-background)` in `:root`
- **Primary Typography Ink**: `#fffdfd` — grounded in `var(--icon-color)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `var(--colorText)` in `:root`
- **Interactive Accent / Highlight**: `#4e9a85` — grounded in `var(--modal-barBackgroundColor)` in `:root`
- **Secondary / Muted Copy**: `#e3ede4` — grounded in `var(--button-background)` in `:root`
- **Structural Hairline Border**: `#232323` — grounded in `var(--formField-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1023px` extracted from `www-seasats-com` stylesheet
- **Padding & Gutters**: `.4rem` lateral canvas padding with `3.2rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023px`, `gap: 3.2rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.4rem` horizontal padding
- **Media Queries**: `@media screen and (max-width:1023px)`, `@media screen and (max-width:519px)`, `@media screen and (min-width:1024px)`, `@media screen and (min-width:1024px)and (pointer:coarse)and (hov...`
- **Corner Radii**: `var(--radius)`, `.4rem`, `.2rem`, `1.2rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `seasonMix`
- **Body Font Stack**: `seasonMix Fallback`
- **Monospace / Technical Font Stack**: `supplyMono`
- **H1 Display Rule**: rule `h1` (`font-size: 4.8rem`, `line-height: 1`, `letter-spacing: -.01em`, `font-weight: 400`)
- **H2 Section Rule**: rule `h2` (`font-size: 2.4rem`, `line-height: 1.2`, `letter-spacing: 0`, `font-weight: 400`)
- **Body Copy Rule**: CSS variables `--body-adjustOffset: calc(59.8rem / -2)`, `--body-adjustScale: 0.66`, `--body-adjustScalePrecise: 0.585`
- **Metadata & Index Rule**: CSS variables `--fontSupplyMono: "supplyMono","supplyMono Fallback",monospace`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-seasats-com` (`Seasats · Ocean Autonomy That Works`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.Header_container__U6gzw> — `www-seasats-com`)**:
   - DOM & Selectors: Landmark `<header class="Header_container__U6gzw">` hosting `Seasats · Ocean Autonomy That Works` navigation (`Home · 01 Capabilities · 02 Past Missions · Products · 01 Comparison`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.not-found_title__bgpas { font-size:min(36rem,36vh) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.Header_container__U6gzw> — `www-seasats-com`)` (`www-seasats-com`) adapts across `@media screen and (max-width:1023px)`, `@media screen and (max-width:519px)`, `@media screen and (min-width:1024px)`, `@media screen and (min-width:1024px)and (pointer:coarse)and (hov...` with `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.19,1,.22,1)` transitions and links `Home · 01 Capabilities · 02 Past Missions · Products · 01 Comparison`.
2. **Hero Stage & Focal Lead (<main.browser-ui-overlay> — `Ocean Autonomy That Works`)**:
   - DOM & Selectors: Landmark `<main class="browser-ui-overlay">` presenting display lead `Ocean Autonomy That Works` and copy excerpt *"Ocean Autonomy That Works"* over `#2b3922` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#2b3922` background with `#fff` headline `Ocean Autonomy That Works`.
3. **Primary Showcase & Content Grid (<main.browser-ui-overlay--top> — `Deploy in minutes.`)**:
   - DOM & Selectors: Landmark `<main class="browser-ui-overlay--top">` rendering section `Deploy in minutes.` with copy *"E x p l o r e p r o d u c t s E x p l o r e p r o d u c t s"*, asset references (`d11d81b0342c0709.css`, `a14bc365605f91b3.css`, `110e11ba57841c1c.css`, `5ef63a433e26978c.css`), and grid rule `.not-found_media__ko4tq { position:absolute;inset:0;background-image:linear-gradient(180deg,1d344a... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.browser-ui-overlay--top> — `Deploy in minutes.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023px`, `gap: 3.2rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.4rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.ThemeBackground_background__xCT8k> — `Detect from miles.`)**:
   - DOM & Selectors: Landmark `<main class="ThemeBackground_background__xCT8k">` framing `Detect from miles.` and `React at once.` (*"E x p l o r e p r o d u c t s"*) with `#fff` surface cards, `#4e9a85` accents, and `.AnimatedText_animatedText__MS50q { display:block;position:relative }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.ThemeBackground_background__xCT8k> — `Detect from miles.`)` uses `var(--radius)`, `.4rem`, `.2rem`, `1.2rem` radii, `#4e9a85` highlights, and assets (d11d81b0342c0709.css, a14bc365605f91b3.css, 110e11ba57841c1c.css).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.seasats.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer Footer_container__kRlyj">` anchoring `Seasats · Ocean Autonomy That Wo` footer links (`Home · 01 Capabilities · 02 Past Missions · Products · 01 Comparison`), copy *"The coordinates of the ghost fleet."*, and `#232323` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://www.seasats.com/`)` aligns to `1023px` extracted from `www-seasats-com` stylesheet with `.4rem` lateral canvas padding with `3.2rem` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Ocean Autonomy That Works"*
- Copy Excerpt 2: *"E x p l o r e p r o d u c t s E x p l o r e p r o d u c t s"*
- Copy Excerpt 3: *"E x p l o r e p r o d u c t s"*
- Copy Excerpt 4: *"The coordinates of the ghost fleet."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.19,1,.22,1)`
- **Extracted Stylesheet Rules (`www-seasats-com`)**:
- `.not-found_title__bgpas { font-size:min(36rem,36vh) }`
- `.not-found_media__ko4tq { position:absolute;inset:0;background-image:linear-gradient(180deg,1d344a... }`
- `.AnimatedText_animatedText__MS50q { display:block;position:relative }`
- `.AnimatedText_labelOriginal__hgz_O { display:block }`
- `.AnimatedText_labelCopy__BAC2o { color:var(--animatedText-hover-color,currentcolor) }`
- **Per-Selector Transition Rules**:
- **Selector `.AnimatedText_char__T7_D3`**: `transition: calc(.6s - var(--char-amt)*12ms) cubic-bezier(.215,.61,.355,1)` extracted from `www-seasats-com` stylesheet.
- **Selector `Button_icon__6so9o[data-icon=plus...`**: `transition: transform .5s ease` extracted from `www-seasats-com` stylesheet.
- **Selector `on_icon__6so9o[data-icon=arrow-ri...`**: `transition: .5s ease` extracted from `www-seasats-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.215,.61,.355,1)`)**: Governs interactive state transitions across `<header.Header_container__U6gzw>` and `<main.browser-ui-overlay--top>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-seasats-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
