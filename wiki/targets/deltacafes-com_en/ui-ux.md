# UI & UX Architecture: deltacafes-com_en

## Overview & Design Identity
- **Target**: `deltacafes-com_en` (**Delta, coffee with heart · Delta Cafés — The coffee of your life**)
- **Production URL**: [https://deltacafes.com/en](https://deltacafes.com/en)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#9e0212`)
- **Summary**: Discover Delta Cafés: Portuguese coffee heritage, culture, sustainability, and experiences from bean to cup for every coffee lover.
- **Total Clean CSS Variables Extracted**: `237` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `trade-gothic`
- **Body Font Stack**: `delta-season`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `clamp(18px,16.206px + 100vw * .00...`, `.51vw`, `.595vw`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 12px`, `line-height: 1.3em`, `letter-spacing: -.01em`, `font-weight: 700`)
- **Body Copy**: CSS variables `--body-backgroundColor: #2b1b14`; rule `p` (`font-size: clamp(18px,16.206px + 100vw *...`, `line-height: 1.2em`, `letter-spacing: -.02em`, `font-weight: 420`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `clamp(18px,16.206px + 100vw * .00...`, `.51vw`, `.595vw`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffd300` | `var(--color-geral-delta-yellow)` in `:root` |
| **Interactive Accent / Highlight** | `#9e0212` | `var(--color-geral-delta-darkRed)` in `:root` |
| **Secondary / Muted Copy** | `#e70025` | `var(--color-geral-delta-brightRed)` in `:root` |
| **Structural Hairline Border** | `#aca59e` | `var(--color-aged-oak-200)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--fontPairingTitle-color` | `var(--color-creme-100)` | Brand / Palette Token |
| `--button-color` | `var(--color-brown-500)` | Brand / Palette Token |
| `--button-backgroundColor` | `var(--color-creme-100)` | Canvas / Surface Token |
| `--icon-color` | `var(--footer-color, var(--color-creme-100))` | Brand / Palette Token |
| `--tag-color` | `var(--journalCard-color, var(--color-brown-500))` | Brand / Palette Token |
| `--button-accentColor` | `transparent` | Brand / Palette Token |
| `--tail-width` | `clamp(30px, 25.515px + 100vw * .0115, 45px)` | Layout / Spatial Grid Token |
| `--tail-height` | `clamp(12px, 10.206px + 100vw * .0046, 18px)` | Layout / Spatial Grid Token |
| `--circle-width` | `660` | Layout / Spatial Grid Token |
| `--initial-100vh` | `100vh` | Layout / Spatial Grid Token |
| `--native-scrollbar-width` | `0px` | Layout / Spatial Grid Token |
| `--computed-100vh` | `100vh` | Layout / Spatial Grid Token |
| `--computed-100vw` | `calc(100vw - var(--native-scrollbar-width))` | Layout / Spatial Grid Token |
| `--grid-columns` | `32` | Layout / Spatial Grid Token |
| `--grid-gap` | `clamp(12px, 8.412px + 100vw * .0092, 24px)` | Layout / Spatial Grid Token |
| `--grid-half-gap` | `calc(var(--grid-gap)*.5)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `deltacafes-com_en`)**:
   - Landmark `<header class="lenis">` hosting `Delta, coffee with heart · Delta Caf` navigation (`About Delta · The Azores Coffee · Products · The coffee cycle · Delta Sustainability`), DOM attributes (`data-website-id="0f29d428-885f-44b8-ae..."`, `data-component="scroller"`, `data-v-d2630b30`, `data-component="menu"`), and stylesheet rule `before { content:"";position:absolute;inset:0;z-index:1;background-color:var(--co... }`.
2. **Hero Stage & Focal Lead (<section.main> — `Delta Cafés`)**:
   - Landmark `<section class="main">` presenting display lead `Delta Cafés` and copy excerpt *"Business Solutions"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.scroller> — `Coffee Culture`)**:
   - Landmark `<section class="scroller">` rendering section `Coffee Culture` with copy *"Delta Cafés Our History About Delta The Azores coffee"*, asset references (`entry.D_EBu6YN.css`, `Footer.mdCQ3N1U.css`, `TransitionLogoMask.DT4Lfp-V.css`, `TagFlag.BCy09Tyz.css`), and grid rule `video { width:100%;height:100%;-o-object-fit:cover;object-fit:cover }`.
4. **Interactive Detail & Feature Matrix (<section.is-ready> — `Delta, coffee with heart.`)**:
   - Landmark `<section class="is-ready">` framing `Delta, coffee with heart.` and `The first Portuguese coffee.` (*"Coffee Culture Coffee Cycle Barista Academy Coffee Science Centre"*) with `#ffd300` surface cards, `#9e0212` accents, and `after { bottom:1px;background:0000004d }`.
5. **Colophon & Global Directory Footer (<footer.bg-mask-defs> — `https://deltacafes.com/en`)**:
   - Landmark `<footer class="bg-mask-defs">` anchoring `Delta, coffee with heart · Delta` footer links (`About Delta · The Azores Coffee · Products · The coffee cycle · Delta Sustainability`), copy *"Coffee Science Centre"*, and `#aca59e` structural dividers.
