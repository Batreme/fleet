# UI & UX Architecture: classe-squarespace-com

## Overview & Design Identity
- **Target**: `classe-squarespace-com` (**Common Language**)
- **Production URL**: [https://classe.squarespace.com/?password=demo](https://classe.squarespace.com/?password=demo)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#000` accent)
- **Summary**: Sun = Sol, Hey = Ehi, Yes = Oui
- **Total Clean CSS Variables Extracted**: `1155` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `squarespace-ui-font`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--sqsp-heading-1-color: hsla(var(--black-hsl),1)`, `--heading-1-size: 4rem`, `--heading-1-size-value: 4`; rule `.title` (`letter-spacing: .5px`, `font-weight: 500`)
- **Section Heading (`H2`)**: CSS variables `--image-block-collage-image-subtitle-color: hsla(var(--black-hsl),1)`, `--image-block-card-image-subtitle-color: hsla(var(--black-hsl),1)`, `--image-block-poster-image-subtitle-color: hsla(var(--white-hsl),1)`; rule `h2` (`font-size: clamp(32px,3vw,42px)!important`, `line-height: 1.02!important`, `letter-spacing: -.01em`, `font-weight: 400!important`)
- **Body Copy**: CSS variables `--paragraphSmallColor: hsla(var(--black-hsl),1)`, `--sqsp-paragraph-3-color: hsla(var(--black-hsl),1)`, `--paragraphLargeColor: hsla(var(--black-hsl),1)`; rule `p` (`font-size: 14px`, `line-height: 1.5em`)
- **Metadata & Labels**: CSS variables `--paragraphSmallColor: hsla(var(--black-hsl),1)`, `--tweak-paragraph-small-color-on-background: hsla(var(--black-hsl),1)`, `--tweak-form-block-caption-color-on-background: hsla(var(--black-hsl),1)`; rule `.caption` (`font-size: 12px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `.sqs-async-form-content .field-... { color: #fff }` |
| **Primary Typography Ink** | `#cc3b3b` | `.sqs-async-form-content .field-... { background: #cc3b3b }` |
| **Elevated Surface / Card Substrate** | `#999` | `orm-wrapper .field-list .sectio... { border-bottom: #999 }` |
| **Interactive Accent / Highlight** | `#000` | `-wrapper .field-list .field .fi... { color: #000 }` |
| **Secondary / Muted Copy** | `#fafafa` | `-wrapper .field-list .field .fi... { background: #fafafa }` |
| **Structural Hairline Border** | `#ccc` | `-wrapper .field-list .field .fi... { border: #ccc }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--tint` | `hsl(var(--accent-hsl))` | Canvas / Surface Token |
| `--tint-a` | `.35` | Canvas / Surface Token |
| `--gray` | `1` | Design System Custom Token |
| `--lift` | `18px` | Dimension / Scale Token |
| `--ink` | `var(--headingLargeColor, hsl(var(--darkAccent-hsl)))` | Typography Ink Token |
| `--wine` | `hsl(var(--accent-hsl))` | Color / Atmospheric Token |
| `--edge` | `hsl(var(--darkAccent-hsl))` | Color / Atmospheric Token |
| `--cream` | `hsl(var(--white-hsl))` | Color / Atmospheric Token |
| `--rose` | `hsl(var(--lightAccent-hsl))` | Color / Atmospheric Token |
| `--hi` | `hsl(var(--lightAccent-hsl))` | Color / Atmospheric Token |
| `--hi-text` | `hsl(var(--darkAccent-hsl))` | Typography Ink Token |
| `--stub` | `var(--wine)` | Design System Custom Token |
| `--sel-line` | `var(--edge)` | Design System Custom Token |
| `--sel-fill` | `var(--cream)` | Design System Custom Token |
| `--sel-size` | `11px` | Layout / Spatial Grid Token |
| `--sel-e` | `calc(var(--sel-size) / 2 - .75px)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `classe-squarespace-com`)**:
   - Landmark `<header class="header theme-col--primary">` hosting `Common Language` navigation (`Hero · Services · Faq's`), DOM attributes (`data-sqsp-font-ids="6a313e7a5ede88444e8c5..."`, `data-name="static-context"`, `data-animation-state="booted"`, `data-test="continue-to-cart"`), and stylesheet rule `.captcha-container.rendered { width:304px;margin-bottom:24px }`.
2. **Hero Stage & Focal Lead (<article.page-regions> — `Sofía`)**:
   - Landmark `<article class="page-regions">` presenting display lead `Sofía` and copy excerpt *"Start Your Lessons"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.region> — `Cece`)**:
   - Landmark `<section class="region">` rendering section `Cece` with copy *"Open Menu Close Menu"*, asset references (`favicon.ico`, `classe.squarespace.com`, `images.squarespace-cdn.com`, `file.squarespace-cdn.com`), and grid rule `captcha-container.rendered.align-... { margin-left:auto;margin-right:auto }`.
4. **Interactive Detail & Feature Matrix (<section.page-section> — `Connor`)**:
   - Landmark `<section class="page-section user-items-list-section">` framing `Connor` and `Amélie` (*"Sun = Sol, Hey = Ehi, Yes = Oui"*) with `#999` surface cards, `#000` accents, and `.captcha-container.rendered.align... { margin-left:auto }`.
5. **Colophon & Global Directory Footer (<footer.sections> — `https://classe.squarespace.com/?password=demo`)**:
   - Landmark `<footer class="sections">` anchoring `Common Language` footer links (`Hero · Services · Faq's`), copy *"Sofía Spanish Sol means sun Meet Sofía"*, and `#ccc` structural dividers.
