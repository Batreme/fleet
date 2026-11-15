# UI & UX Architecture: www-oceans-faith_moralcatch

## Overview & Design Identity
- **Target**: `www-oceans-faith_moralcatch` (**The Moral Catch: Fisheries & Ocean Justice — Faiths for Oceans**)
- **Production URL**: [https://www.oceans.faith/moralcatch](https://www.oceans.faith/moralcatch)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ff0` canvas, `#000` ink, `#fff` accent)
- **Summary**: Explore fisheries, ocean life and workers’ rights. Read The Moral Catch report, take the two-minute meal test, and use the faith institut...
- **Total Clean CSS Variables Extracted**: `1004` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `squarespace-ui-font`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--sqsp-heading-1-color: hsla(var(--black-hsl),1)`, `--heading-1-size: 4rem`, `--heading-1-size-value: 4`; rule `.title` (`letter-spacing: .5px`, `font-weight: 500`)
- **Section Heading (`H2`)**: CSS variables `--image-block-collage-image-subtitle-color: hsla(var(--black-hsl),1)`, `--image-block-card-image-subtitle-color: hsla(var(--black-hsl),1)`, `--image-block-poster-image-subtitle-color: hsla(var(--white-hsl),1)`
- **Body Copy**: CSS variables `--paragraphSmallColor: hsla(var(--black-hsl),1)`, `--sqsp-paragraph-3-color: hsla(var(--black-hsl),1)`, `--paragraphLargeColor: hsla(var(--black-hsl),1)`; rule `p` (`font-size: 14px`, `line-height: 1.5em`)
- **Metadata & Labels**: CSS variables `--paragraphSmallColor: hsla(var(--black-hsl),1)`, `--tweak-paragraph-small-color-on-background: hsla(var(--black-hsl),1)`, `--tweak-form-block-caption-color-on-background: hsla(var(--black-hsl),1)`; rule `.caption` (`font-size: 12px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ff0` | `mark { background: #ff0 }` |
| **Primary Typography Ink** | `#000` | `mark { color: #000 }` |
| **Elevated Surface / Card Substrate** | `#c0c0c0` | `fieldset { border: silver }` (`#c0c0c0`) |
| **Interactive Accent / Highlight** | `#fff` | `.sqs-cookie-banner-v2.DARK a { color: #fff }` |
| **Secondary / Muted Copy** | `#777` | `ner-v2.DARK.TEXT .sqs-cookie-ba... { border-bottom: #777 }` |
| **Structural Hairline Border** | `#eee` | `.sqs-cookie-banner-v2.LIGHT { background-color: #eee }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--white-hsl` | `0,100%,99.02%` | Canvas / Surface Token |
| `--sqsp-palette-lightest-color` | `hsla(0,100%,99.02%,1)` | Canvas / Surface Token |
| `--lightAccent-hsl` | `0,0%,96.08%` | Canvas / Surface Token |
| `--sqsp-palette-light-color` | `hsla(0,0%,96.08%,1)` | Canvas / Surface Token |
| `--accent-hsl` | `0,0%,85.1%` | Brand / Palette Token |
| `--sqsp-palette-accent-color` | `hsla(0,0%,85.1%,1)` | Brand / Palette Token |
| `--darkAccent-hsl` | `0,0%,47.45%` | Canvas / Surface Token |
| `--sqsp-palette-dark-color` | `hsla(0,0%,47.45%,1)` | Canvas / Surface Token |
| `--black-hsl` | `0,0%,0%` | Canvas / Surface Token |
| `--sqsp-palette-darkest-color` | `hsla(0,0%,0%,1)` | Canvas / Surface Token |
| `--safeLightAccent-hsl` | `0,0%,85.1%` | Canvas / Surface Token |
| `--safeDarkAccent-hsl` | `0,0%,0%` | Canvas / Surface Token |
| `--safeInverseAccent-hsl` | `0,0%,0%` | Brand / Palette Token |
| `--safeInverseLightAccent-hsl` | `0,0%,0%` | Canvas / Surface Token |
| `--safeInverseDarkAccent-hsl` | `0,0%,100%` | Canvas / Surface Token |
| `--course-item-nav-text-color` | `hsla(var(--black-hsl),1)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bright-inverse> — `www-oceans-faith_moralcatch`)**:
   - Landmark `<header class="bright-inverse header">` hosting `The Moral Catch: Fisheries & Ocean J` navigation (`SIGN THE DECLARATION · SIGNATORIES · POLICY PRIMERS · GLOSSARY · REPORT`), DOM attributes (`data-sqsp-font-ids="6a3139e4691a2d058d1a1..."`, `data-name="static-context"`, `data-animation-state="booted"`, `data-test="header"`), and stylesheet rule `summary { display:block }`.
2. **Hero Stage & Focal Lead (<article.page-regions> — `Stay Connected`)**:
   - Landmark `<article class="page-regions">` presenting display lead `Stay Connected` and copy excerpt *"HIGH AMBITION COALITION"* over `#ff0` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.region> — `HIGH AMBITION COALITION`)**:
   - Landmark `<section class="region">` rendering section `HIGH AMBITION COALITION` with copy *"MULTI-FAITH DECLARATION"*, asset references (`popup-overlay-f39ec8cdc95ccd84-mi...`, `popup-overlay-7afaba259a8e252a-mi...`, `favicon.ico`, `moralcatch`), and grid rule `video { display:inline-block }`.
4. **Interactive Detail & Feature Matrix (<section.page-section> — `MULTI-FAITH DECLARATION`)**:
   - Landmark `<section class="page-section full-bleed-section">` framing `MULTI-FAITH DECLARATION` and `SIGN THE DECLARATION` (*"SIGN THE DECLARATION"*) with `#c0c0c0` surface cards, `#fff` accents, and `template { display:none }`.
5. **Colophon & Global Directory Footer (<footer.sections> — `https://www.oceans.faith/moralcatch`)**:
   - Landmark `<footer class="sections">` anchoring `The Moral Catch: Fisheries & Oce` footer links (`SIGN THE DECLARATION · SIGNATORIES · POLICY PRIMERS · GLOSSARY · REPORT`), copy *"OCEAN INTERFAITH FORUM"*, and `#eee` structural dividers.
