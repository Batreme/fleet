# UI & UX Architecture: southandstonestudio-com

## Overview & Design Identity
- **Target**: `southandstonestudio-com` (**South & Stone Studio · Web Design & Brand Identity**)
- **Production URL**: [http://southandstonestudio.com](http://southandstonestudio.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#eee` / `#7A7A7A`)
- **Summary**: Websites written and built by Kelli Covey, a novelist and designer. Custom sites and brand identities for small businesses, with prices p...
- **Total Clean CSS Variables Extracted**: `113` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Caveat`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: clamp(2.7rem,7.6vw,8.2rem)`, `line-height: .92`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(1.5rem,2.4vw,2rem)`, `line-height: 1.1`, `letter-spacing: -.02em`, `font-weight: 760`)
- **Body Copy**: rule `p` (`font-size: clamp(2rem,5.4vw,5.2rem)`, `line-height: .98`, `letter-spacing: -.035em`, `font-weight: 780`)
- **Metadata & Labels**: rule `small` (`font-size: .85rem`, `font-weight: 650`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#eee` | `var(--edd-blocks-light-grey)` in `:root` |
| **Primary Typography Ink** | `#6EC1E4` | `var(--e-global-color-primary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#54595F` | `var(--e-global-color-secondary)` in `:root` |
| **Interactive Accent / Highlight** | `#7A7A7A` | `var(--e-global-color-text)` in `:root` |
| **Secondary / Muted Copy** | `#61CE70` | `var(--e-global-color-accent)` in `:root` |
| **Structural Hairline Border** | `#000` | `var(--sx-black)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--edd-blocks-light-grey` | `#eee` | Canvas / Surface Token |
| `--direction-multiplier` | `1` | Design System Custom Token |
| `--flex-direction` | `initial` | Design System Custom Token |
| `--flex-wrap` | `initial` | Layout / Spatial Grid Token |
| `--justify-content` | `initial` | Design System Custom Token |
| `--align-items` | `initial` | Design System Custom Token |
| `--align-content` | `initial` | Design System Custom Token |
| `--gap` | `initial` | Layout / Spatial Grid Token |
| `--flex-basis` | `initial` | Design System Custom Token |
| `--flex-grow` | `initial` | Design System Custom Token |
| `--flex-shrink` | `initial` | Typography Ink Token |
| `--order` | `initial` | Design System Custom Token |
| `--align-self` | `initial` | Design System Custom Token |
| `--page-title-display` | `block` | Design System Custom Token |
| `--border-radius` | `0` | Elevation / Border Token |
| `--border-top-width` | `0px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sx-head> — `southandstonestudio-com`)**:
   - Landmark `<header class="sx-head">` hosting `South & Stone Studio · Web Design & ` navigation (`Services · Portfolio · Industries · Estimate Desk · Shop`), DOM attributes (`data-domain="southandstonestudio.com"`, `data-elementor-device-mode="desktop"`, `data-sx-industry`, `data-trade="contractors"`), and stylesheet rule `.elementor .e-div-block-base { min-width:30px;padding:10px;display:block; }`.
2. **Hero Stage & Focal Lead (<section.sx-hero> — `Every website has a better version`)**:
   - Landmark `<section class="sx-hero">` presenting display lead `Every website has a better version.` and copy excerpt *"Get a free redline"* over `#eee` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.sx-sec> — `Drag the red line. Watch a website`)**:
   - Landmark `<section class="sx-sec sx-t-bone">` rendering section `Drag the red line. Watch a website start selling.` with copy *"Live Try the live demo Holloway Home Repair"*, asset references (`cdn-reach.hostinger.com`, `js.stripe.com`, `embed`, `south-stone-favicon.png`), and grid rule `.elementor .e-flexbox-base { padding:10px;display:flex;flex-direction:row; }`.
4. **Interactive Detail & Feature Matrix (<section.sx-fst-band> — `Can a customer find your phone num`)**:
   - Landmark `<section class="sx-fst-band">` framing `Can a customer find your phone number in five sec...` and `Four ways in. Every one priced.` (*"Try the live demo Holloway Home Repair"*) with `#54595F` surface cards, `#7A7A7A` accents, and `.elementor .e-tabs-base { padding-block-start:0px;display:flex;flex-direction:column;gap:30px; }`.
5. **Colophon & Global Directory Footer (<footer.sx-foot> — `http://southandstonestudio.com`)**:
   - Landmark `<footer class="sx-foot">` anchoring `South & Stone Studio · Web Desig` footer links (`Services · Portfolio · Industries · Estimate Desk · Shop`), copy *"Websites for contractors from $1,250"*, and `#000` structural dividers.
