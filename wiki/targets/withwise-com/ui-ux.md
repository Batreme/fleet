# UI & UX Architecture: withwise-com

## Overview & Design Identity
- **Target**: `withwise-com` (**Compliance-First Onboarding Software · Wise**)
- **Production URL**: [https://withwise.com/](https://withwise.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#1B1B1B` canvas, `#FFFDF1` ink, `#D3C0A0` accent)
- **Summary**: Wise is built for self-employed workforces. We protect you from compliance risks, help you onboard users digitally, and pay them securely.
- **Total Clean CSS Variables Extracted**: `795` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Open Sans`
- **Body Font Stack**: `Figtree`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--gf-field-pwd-str-ind-display: inline-block`, `--gf-local-display: block`; rule `h1` (`font-size: 35px`, `font-weight: 700`)
- **Section Heading (`H2`)**: rule `,.h2` (`font-size: 1.8125rem`, `line-height: 1.4`)
- **Body Copy**: rule `p` (`font-size: 16px`, `line-height: 20px`)
- **Metadata & Labels**: CSS variables `--gf-ctrl-label-font-size-primary: inherit`, `--gf-ctrl-label-font-size-secondary: inherit`, `--gf-ctrl-label-font-size-tertiary: inherit`; rule `small` (`line-height: 0`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#1B1B1B` | `var(--gf-color-primary)` in `:root` |
| **Primary Typography Ink** | `#FFFDF1` | `var(--gf-ctrl-bg-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#cc4b37` | `var(--gf-ctrl-border-color-error)` in `:root` |
| **Interactive Accent / Highlight** | `#D3C0A0` | `var(--gf-ctrl-border-color)` in `:root` |
| **Secondary / Muted Copy** | `#D81E5B` | `var(--gf-ctrl-btn-bg-color-primary)` in `:root` |
| **Structural Hairline Border** | `#C51B53` | `var(--gf-ctrl-btn-bg-color-hover-primary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--input-fz` | `1rem` | Dimension / Scale Token |
| `--input-lh` | `1.5` | Design System Custom Token |
| `--input-pt` | `0.6875rem` | Dimension / Scale Token |
| `--input-pb` | `0.6875rem` | Dimension / Scale Token |
| `--input-pl` | `1rem` | Dimension / Scale Token |
| `--input-pr` | `1rem` | Dimension / Scale Token |
| `--input-bd` | `1px` | Dimension / Scale Token |
| `--grid-col-gap` | `2.5rem` | Layout / Spatial Grid Token |
| `--section-width` | `77.5rem` | Layout / Spatial Grid Token |
| `--section-horizontal-padding` | `calc(var(--grid-col-gap, 2rem) * 0.5)` | Layout / Spatial Grid Token |
| `--gf-form-gap-x` | `2rem` | Layout / Spatial Grid Token |
| `--gf-form-gap-y` | `1.5rem` | Layout / Spatial Grid Token |
| `--gf-field-gap-x` | `var(--gf-form-gap-x)` | Layout / Spatial Grid Token |
| `--gf-field-gap-y` | `var(--gf-form-gap-y)` | Layout / Spatial Grid Token |
| `--gf-color-primary` | `#1B1B1B !important` | Brand / Palette Token |
| `--gf-field-list-btn-size` | `1.25rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `withwise-com`)**:
   - Landmark `<header class="header">` hosting `Compliance-First Onboarding Software` navigation (`Request a callback · Platform · See article · Industries`), DOM attributes (`data-scroll-dir-x="0"`, `data-scroll-dir-y="0"`, `data-loader="hs-scriptloader"`, `data-hsjs-portal="145539501"`), and stylesheet rule `.slick-list { position:relative;display:block;overflow:hidden;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.flx-section> — `Compliance-First Onboarding softwa`)**:
   - Landmark `<section class="flx-section flx-masthead-1">` presenting display lead `Compliance-First Onboarding software` and copy excerpt *"We value your privacy"* over `#1B1B1B` canvas and `#FFFDF1` ink.
3. **Primary Showcase & Content Grid (<section.flx-section> — `Stay compliant . Pay on time . Gro`)**:
   - Landmark `<section class="flx-section bg-type-dark">` rendering section `Stay compliant . Pay on time . Grow without the r...` with copy *"We use cookies to enhance your browsing experience, serve persona"*, asset references (`web-interactives-embed.js`, `banner.js`, `145539501.js`, `collectedforms.js`), and grid rule `.slick-list:focus { outline:none }`.
4. **Interactive Detail & Feature Matrix (<section.flx-section> — `Why It Matters`)**:
   - Landmark `<section class="flx-section bg-type-dark">` framing `Why It Matters` and `Compliance is a behaviour, not a document.` (*"Customise Consent Preferences"*) with `#cc4b37` surface cards, `#D3C0A0` accents, and `.slick-list.dragging { cursor:pointer;cursor:hand }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://withwise.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Compliance-First Onboarding Soft` footer links (`Request a callback · Platform · See article · Industries`), copy *"We use cookies to help you navigate efficiently and perform "*, and `#C51B53` structural dividers.
