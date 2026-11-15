# UI & UX Architecture: madetodisrupt-com

## Overview & Design Identity
- **Target**: `madetodisrupt-com` (**Disrupt · Creative Brand Experience Agency**)
- **Production URL**: [https://madetodisrupt.com](https://madetodisrupt.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#6EC1E4` / `#61CE70`)
- **Summary**: Disrupt is a creative brand experience agency shaping strategy, identity, events and activations into ideas people can see, feel and expe...
- **Total Clean CSS Variables Extracted**: `226` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Clash Display`
- **Body Font Stack**: `Syne`
- **Monospace / Technical Font Stack**: `Courier 10 Pitch`
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`; rule `,h1` (`font-size: 2em`, `line-height: 1.2`)
- **Section Heading (`H2`)**: rule `,h2` (`font-size: 1.7em`, `line-height: 1.3`)
- **Body Copy**: rule `p` (`font-size: 16px`)
- **Metadata & Labels**: CSS variables `--ast-blog-meta-weight: 600`, `--srfm-color-input-label: var(--ast-global-color-2)`, `--mv-label-x: calc(var(--mv-base-x) + var(--mv-shift-x))`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#6EC1E4` | `var(--e-global-color-primary)` in `:root` |
| **Primary Typography Ink** | `#54595F` | `var(--e-global-color-secondary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#7A7A7A` | `var(--e-global-color-text)` in `:root` |
| **Interactive Accent / Highlight** | `#61CE70` | `var(--e-global-color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#ECEFF3` | `var(--ast-code-block-background)` in `:root` |
| **Structural Hairline Border** | `#F9FAFB` | `var(--ast-comment-inputs-background)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
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
| `--border-right-width` | `0px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.entry-header> — `madetodisrupt-com`)**:
   - Landmark `<header class="entry-header ast-no-thumbnail">` hosting `Disrupt · Creative Brand Experience ` navigation (`Home · Work · Services · Contact`), DOM attributes (`data-minify="1"`, `data-rocket-defer`, `data-rocket-prefetch`, `data-rocket-preload`), and stylesheet rule `.dashicons-admin-appearance:before { content:"\f100" }`.
2. **Hero Stage & Focal Lead (<article.post-10> — `BRANDS IN SESSION`)**:
   - Landmark `<article class="post-10 page">` presenting display lead `BRANDS IN SESSION` and copy excerpt *"Brand Therapy, Without the couch. Brand Therapy, Without the couc"* over `#6EC1E4` canvas and `#54595F` ink.
3. **Primary Showcase & Content Grid (<section.poc-tilt-section> — `WORK`)**:
   - Landmark `<section class="poc-tilt-section">` rendering section `WORK` with copy *"Brand Therapy, Without the couch."*, asset references (`recaptcha__en.js`, `script.js`, `www.gstatic.com`, `fonts.googleapis.com`), and grid rule `.dashicons-admin-collapse:before { content:"\f148" }`.
4. **Interactive Detail & Feature Matrix (<section.mxq-stage> — `The Story`)**:
   - Landmark `<section class="mxq-stage">` framing `The Story` and `Craft experiences that move people and shape how...` (*"START A SESSION START A SESSION"*) with `#7A7A7A` surface cards, `#61CE70` accents, and `.dashicons-admin-comments:before { content:"\f101" }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://madetodisrupt.com`)**:
   - Landmark `<footer class="elementor elementor-425">` anchoring `Disrupt · Creative Brand Experie` footer links (`Home · Work · Services · Contact`), copy *"Strategic brand therapy for identities, experiences, and act"*, and `#F9FAFB` structural dividers.
