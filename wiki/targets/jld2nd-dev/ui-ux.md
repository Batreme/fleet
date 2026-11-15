# UI & UX Architecture: jld2nd-dev

## Overview & Design Identity
- **Target**: `jld2nd-dev` (**JLD'2nd – Designer & Developer**)
- **Production URL**: [https://jld2nd.dev](https://jld2nd.dev)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffd64f` canvas, `#212121` ink, `#616161` accent)
- **Summary**: I believe web design should be as expressive as the ideas behind it. Driven by curiosity, I explore new possibilities at the intersection...
- **Total Clean CSS Variables Extracted**: `53` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Mozilla Headline`
- **Body Font Stack**: `Minecraft`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--fs-display-2xl: clamp(3.75rem, 3.5536rem + .9821vw, 5.125rem)`, `--fs-display-xl: clamp(3.5rem, calc(3.4rem + .5vw), 4rem)`, `--fs-display-lg: clamp(3.125rem, 2.9018rem + 1.1161vw, 4.6875rem)`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `15px`, `2.1em`, `1.8em`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `15px`, `2.1em`, `1.8em`)
- **Metadata & Labels**: CSS variables `--fs-text-sm: .875rem`, `--fs-text-xs: .75rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffd64f` | `var(--color-primary)` in `:root` |
| **Primary Typography Ink** | `#fc5778` | `var(--color-secondary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#212121` | `var(--base-text-dark)` in `:root` |
| **Interactive Accent / Highlight** | `#616161` | `var(--base-text-medium)` in `:root` |
| **Secondary / Muted Copy** | `#9e9e9e` | `var(--base-text-light)` in `:root` |
| **Structural Hairline Border** | `#00b0f4` | `var(--base-text-info)` in `:root` |
| **Variable Token (`--base-text-success`)** | `#11b76b` | `var(--base-text-success)` in `:root` |
| **Variable Token (`--base-text-warning`)** | `#ffa100` | `var(--base-text-warning)` in `:root` |
| **Variable Token (`--base-text-danger`)** | `#fa4362` | `var(--base-text-danger)` in `:root` |
| **Variable Token (`--base-bg-info`)** | `#e5f3ff` | `var(--base-bg-info)` in `:root` |
| **Variable Token (`--base-bg-success`)** | `#e6f6ed` | `var(--base-bg-success)` in `:root` |
| **Variable Token (`--base-bg-warning`)** | `#fff2d7` | `var(--base-bg-warning)` in `:root` |
| **Variable Token (`--base-bg-danger`)** | `#ffe6ec` | `var(--base-bg-danger)` in `:root` |
| **Variable Token (`--base-bg-dark`)** | `#263238` | `var(--base-bg-dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--base-vh` | `1vh` | Layout / Spatial Grid Token |
| `--base-transition` | `all .2s` | Motion / Easing Token |
| `--color-primary` | `#ffd64f` | Brand / Palette Token |
| `--color-secondary` | `#fc5778` | Brand / Palette Token |
| `--base-text-dark` | `#212121` | Canvas / Surface Token |
| `--base-text-medium` | `#616161` | Typography Ink Token |
| `--base-text-light` | `#9e9e9e` | Canvas / Surface Token |
| `--base-text-info` | `#00b0f4` | Typography Ink Token |
| `--base-text-success` | `#11b76b` | Typography Ink Token |
| `--base-text-warning` | `#ffa100` | Typography Ink Token |
| `--base-text-danger` | `#fa4362` | Typography Ink Token |
| `--base-bg-info` | `#e5f3ff` | Canvas / Surface Token |
| `--base-bg-success` | `#e6f6ed` | Canvas / Surface Token |
| `--base-bg-warning` | `#fff2d7` | Canvas / Surface Token |
| `--base-bg-danger` | `#ffe6ec` | Canvas / Surface Token |
| `--base-bg-dark` | `#263238` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sticky> — `jld2nd-dev`)**:
   - Landmark `<header class="sticky">` hosting `JLD'2nd – Designer & Developer` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-no-grid`, `data-section="hero"`, `data-section="about"`, `data-section="pixels"`), and stylesheet rule `main-content:focus { outline:none }`.
2. **Hero Stage & Focal Lead (<section.section> — `T u r n i n g P i x e l s i n t o `)**:
   - Landmark `<section class="section">` presenting display lead `T u r n i n g P i x e l s i n t o M e m o r a b l...` and copy excerpt *"E x p e r i e n c e s ."* over `#ffd64f` canvas and `#212121` ink.
3. **Primary Showcase & Content Grid (<section.section> — `T h e C r e a t o r B e h i n d t `)**:
   - Landmark `<section class="section grid-container">` rendering section `T h e C r e a t o r B e h i n d t h e C o d e a n...` with copy *"t h o u g h t f u l"*, asset references (`favicon.ico`, `favicon-32x32.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `html { -webkit-text-size-adjust:100%;text-size-adjust:auto;line-height:1.15 }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `I t a l l s t a r t s w i t h t h `)**:
   - Landmark `<section class="section p-relative">` framing `I t a l l s t a r t s w i t h t h e p i x e l s .` and `T h i s i s w h e r e i d e a s t a k e s h a p e .` (*"s t r u c t u r e ,"*) with `#212121` surface cards, `#616161` accents, and `section { display:block }`.
5. **Colophon & Global Directory Footer (<footer.home-footer> — `https://jld2nd.dev`)**:
   - Landmark `<footer class="home-footer">` anchoring `JLD'2nd – Designer & Developer` footer links (`Overview · Index · Archive · About · Contact`), copy *"i n t e r a c t i o n ,"*, and `#00b0f4` structural dividers.
