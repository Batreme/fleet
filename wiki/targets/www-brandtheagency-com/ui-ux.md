# UI & UX Architecture: www-brandtheagency-com

## Overview & Design Identity
- **Target**: `www-brandtheagency-com` (**BR& – Creating brands that make you smile**)
- **Production URL**: [https://www.brandtheagency.com/](https://www.brandtheagency.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#0000`)
- **Summary**: BR& is a creative agency based in Dubai offering branding, marketing, strategy, advertising and social media services. Blending local exp...
- **Total Clean CSS Variables Extracted**: `1044` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Pixelify Sans`
- **Body Font Stack**: `squarespace-ui-font`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--sqsp-heading-1-color: hsla(var(--black-hsl),1)`, `--heading-1-size: 4.6rem`, `--heading-1-size-value: 4.6`; rule `.title` (`font-size: 1rem`, `line-height: 1.4`, `font-weight: 500`)
- **Section Heading (`H2`)**: CSS variables `--image-block-collage-image-subtitle-color: hsla(var(--black-hsl),1)`, `--image-block-card-image-subtitle-color: hsla(var(--black-hsl),1)`, `--image-block-poster-image-subtitle-color: hsla(var(--white-hsl),1)`
- **Body Copy**: CSS variables `--paragraphSmallColor: hsla(var(--black-hsl),1)`, `--sqsp-paragraph-3-color: hsla(var(--black-hsl),1)`, `--paragraphLargeColor: hsla(var(--black-hsl),1)`; rule `p` (`line-height: 1.68em`)
- **Metadata & Labels**: CSS variables `--tweak-form-block-caption-color-on-background: #000`, `--paragraphSmallColor: hsla(var(--black-hsl),1)`, `--tweak-paragraph-small-color-on-background: hsla(var(--black-hsl),1)`; rule `.caption` (`font-size: 12px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--tweak-form-block-title-color-on-background)` in `:root` |
| **Primary Typography Ink** | `#b7d8ad` | `var(--c1)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0037d3` | `var(--c2)` in `:root` |
| **Interactive Accent / Highlight** | `#0000` | `.s3sJjVHu8Sy6uWa6 { background-color: #0000 }` |
| **Secondary / Muted Copy** | `#eee` | `verlay-hover .image-caption-wra... { color: #eee }` |
| **Structural Hairline Border** | `#bbb` | `ion-overlay-hover .image-captio... { color: #bbb }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--tweak-form-block-title-color-on-background` | `#000` | Canvas / Surface Token |
| `--tweak-form-block-caption-color-on-background` | `#000` | Canvas / Surface Token |
| `--tweak-form-block-option-color-on-background` | `#000` | Canvas / Surface Token |
| `--overlap-image-width-flex-offset` | `calc((var(--image-block-overlap-image-width) - 50%) * 2)` | Layout / Spatial Grid Token |
| `--overlap-title-width-offset` | `50%` | Layout / Spatial Grid Token |
| `--collage-image-width-flex-offset` | `calc((var(--image-block-collage-image-width) - 50%) * 2)` | Layout / Spatial Grid Token |
| `--collage-content-width-flex-offset` | `calc((var(--image-block-collage-image-content-width) - 50%) * 2)` | Layout / Spatial Grid Token |
| `--fallback-white-hsl` | `0, 0%, 98%` | Canvas / Surface Token |
| `--fallback-black-hsl` | `0, 0%, 0%` | Canvas / Surface Token |
| `--solid-alpha-modifier` | `1` | Design System Custom Token |
| `--solid-hover-alpha-modifier` | `0.6` | Design System Custom Token |
| `--outline-hover-alpha-modifier` | `0.4` | Elevation / Border Token |
| `--inverted-solid-hover-alpha-modifier` | `var(--solid-hover-alpha-modifier)` | Design System Custom Token |
| `--inverted-outline-hover-alpha-modifier` | `var(--outline-hover-alpha-modifier)` | Elevation / Border Token |
| `--solid-focus-alpha-modifier` | `1` | Design System Custom Token |
| `--outline-focus-alpha-modifier` | `0.4` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.yui3-js-enabled> — `www-brandtheagency-com`)**:
   - Landmark `<header class="yui3-js-enabled">` hosting `BR& – Creating brands that make you ` navigation (`Subscribe · our services · projects · careers · contact us`), DOM attributes (`data-sqsp-font-ids="6a313988fd7025398af25..."`, `data-name="static-context"`, `data-sqs-type="cookiepreferencesgetter"`, `data-motion-style="m-6b08526a3060ed6bcdf2"`), and stylesheet rule `.fvDxPINFKaIQHxAo { animation-name:spin;animation-duration:1s;animation-timing-function:line... }`.
2. **Hero Stage & Focal Lead (<section.gdpr-cookie-banner> — `creating brands that make you smil`)**:
   - Landmark `<section class="gdpr-cookie-banner BOTTOM">` presenting display lead `creating brands that make you smile` and copy excerpt *"Select “Accept all” to agree to our use of cookies and similar te"* over `#000` canvas and `#eee` ink.
3. **Primary Showcase & Content Grid (<article.page-regions> — `creating brands that make you smil`)**:
   - Landmark `<article class="page-regions">` rendering section `creating brands that make you smile creating bran...` with copy *"creating brands that make you smile"*, asset references (`favicon.ico`, `www.brandtheagency.com`, `BR%26_banner.jpg`, `images.squarespace-cdn.com`), and grid rule `.Ullcl0nljcxhHnEM { animation-name:fadeout;animation-iteration-count:1 }`.
4. **Interactive Detail & Feature Matrix (<section.region> — `Give us your email, we will send y`)**:
   - Landmark `<section class="region">` framing `Give us your email, we will send you cool stuff` and `subscribe to our newsletter` (*"subscribe to our newsletter"*) with `#0037d3` surface cards, `#0000` accents, and `.IL7wXbP6N7YXaIOk { animation-name:fadein;animation-iteration-count:1 }`.
5. **Colophon & Global Directory Footer (<footer.sections> — `https://www.brandtheagency.com/`)**:
   - Landmark `<footer class="sections">` anchoring `BR& – Creating brands that make ` footer links (`Subscribe · our services · projects · careers · contact us`), copy *"Terms & Conditions"*, and `#bbb` structural dividers.
