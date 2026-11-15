# UI & UX Architecture: waverunmedia-com

## Overview & Design Identity
- **Target**: `waverunmedia-com` (**WaveRun Media**)
- **Production URL**: [https://waverunmedia.com/](https://waverunmedia.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#6c6c89` canvas, `#f7f7f8` ink, `#e5e5e9` accent)
- **Summary**: WaveRun Media captures the pulse of real stories that move markets and shape culture.
- **Total Clean CSS Variables Extracted**: `103` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Satoshi`
- **Body Font Stack**: `Satoshi`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `1.6rem`, `4.6rem`, `1em`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `1.6rem`, `4.6rem`, `1em`)
- **Body Copy**: CSS variables `--wndb--color--body: var(--wndb--color--surface)`
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `1.6rem`, `4.6rem`, `1em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#6c6c89` | `var(--wndb-gray)` in `:root` |
| **Primary Typography Ink** | `#f7f7f8` | `var(--wndb-gray-50)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ebebef` | `var(--wndb-gray-100)` in `:root` |
| **Interactive Accent / Highlight** | `#e5e5e9` | `var(--wndb-gray-150)` in `:root` |
| **Secondary / Muted Copy** | `#d1d1db` | `var(--wndb-gray-200)` in `:root` |
| **Structural Hairline Border** | `#a9a9bc` | `var(--wndb-gray-300)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--slide-media-height` | `98.8vw` | Layout / Spatial Grid Token |
| `--wndb-mask-color` | `rgba(0,0,0,.15)` | Brand / Palette Token |
| `--wndb-mask-position` | `50% 50% at 50% 20%` | Dimension / Scale Token |
| `--wndb-mask-opacity` | `0.35` | Design System Custom Token |
| `--wndb--max-w--prose` | `min(65ch,1100px)` | Layout / Spatial Grid Token |
| `--wndb--text-scale-factor` | `1` | Typography Ink Token |
| `--wndb--text--xs` | `0.75rem` | Typography Ink Token |
| `--wndb--text--sm` | `0.875rem` | Typography Ink Token |
| `--wndb--text--base` | `1rem` | Typography Ink Token |
| `--wndb--text--md` | `1.125rem` | Typography Ink Token |
| `--wndb--text--lg` | `1.5rem` | Typography Ink Token |
| `--wndb--text--xl` | `2.375rem` | Typography Ink Token |
| `--wndb--text--huge` | `clamp(2.75rem,1.4688rem + 2.5vw,3.5rem)` | Typography Ink Token |
| `--wndb--text-giga` | `clamp(3.25rem,2.546875rem + 2.25vw,4.375rem)` | Typography Ink Token |
| `--nfd-wb-anim-transition-duration` | `1400ms` | Motion / Easing Token |
| `--nfd-wb-anim-transition-delay` | `50ms` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `waverunmedia-com`)**:
   - Landmark `<header class="header js-header">` hosting `WaveRun Media` navigation (`Home · About · Partners · KWILL Advisors · ADTV`), DOM attributes (`data-globals="("ajax_url":"https://..."`, `data-video-ready="true"`, `data-video-ready="true"`, `data-from="center"`), and stylesheet rule `html { font-size:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<article.universal> — `the flow of culture`)**:
   - Landmark `<article class="universal">` presenting display lead `the flow of culture` and copy excerpt *"Partners KWILL Advisors ADTV PopArt Studio Dr. Lilly Approved NBA"* over `#6c6c89` canvas and `#f7f7f8` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `Stories in Motion`)**:
   - Landmark `<section class="hero hero--bottom">` rendering section `Stories in Motion` with copy *"Dr. Lilly Approved"*, asset references (`apple-icon-57x57.png`, `apple-icon-60x60.png`, `apple-icon-72x72.png`, `apple-icon-76x76.png`), and grid rule `a:active { outline:none }`.
4. **Interactive Detail & Feature Matrix (<section.slider-block> — `Flippin’ in Heels`)**:
   - Landmark `<section class="slider-block">` framing `Flippin’ in Heels` and `The Elevator Pitch` (*"WaveRun Media captures the pulse of real stories that move market"*) with `#ebebef` surface cards, `#e5e5e9` accents, and `strong { font-weight:700 }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://waverunmedia.com/`)**:
   - Landmark `<footer class="footer">` anchoring `WaveRun Media` footer links (`Home · About · Partners · KWILL Advisors · ADTV`), copy *"Flippin’ in Heels Featuring Rashauna Scott"*, and `#a9a9bc` structural dividers.
