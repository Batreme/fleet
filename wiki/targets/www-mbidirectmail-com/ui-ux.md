# UI & UX Architecture: www-mbidirectmail-com

## Overview & Design Identity
- **Target**: `www-mbidirectmail-com` (**Direct Mail & Digital Marketing · Customer Acquisition · MBI**)
- **Production URL**: [https://www.mbidirectmail.com/](https://www.mbidirectmail.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#151515` / `#0A0A0C`)
- **Summary**: MBI Direct Mail + Digital helps businesses find, reach, and win new customers: direct mail, print, digital, and seminar marketing from on...
- **Total Clean CSS Variables Extracted**: `137` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback Mac`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 22px`, `line-height: 1.25`, `letter-spacing: .05em`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(38px,11.6vw,48px)`, `line-height: 1.0`, `letter-spacing: -.035em`, `font-weight: 100`)
- **Body Copy**: CSS variables `--body-d: #C9CBD1`, `--body-l: rgba(0, 0, 0, 0.66)`; rule `p` (`font-size: 16px`, `line-height: 1.55`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `17px`, `15px`, `16px`, `18px`, `24px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#151515` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#d71920` | `var(--signal)` in `:root` |
| **Elevated Surface / Card Substrate** | `#06070A` | `var(--dark)` in `:root` |
| **Interactive Accent / Highlight** | `#0A0A0C` | `var(--dark2)` in `:root` |
| **Secondary / Muted Copy** | `#151719` | `var(--foot)` in `:root` |
| **Structural Hairline Border** | `#F6F8FA` | `var(--paper)` in `:root` |
| **Variable Token (`--white`)** | `#FFFFFF` | `var(--white)` in `:root` |
| **Variable Token (`--ink-d`)** | `#F0F0F2` | `var(--ink-d)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#151515` | Typography Ink Token |
| `--signal` | `#d71920` | Color / Atmospheric Token |
| `--rule` | `rgba(21, 21, 21, 0.3)` | Color / Atmospheric Token |
| `--rule-on` | `rgba(21, 21, 21, 0.46)` | Color / Atmospheric Token |
| `--wall` | `rgba(21, 21, 21, 0.13)` | Color / Atmospheric Token |
| `--rail` | `16px` | Dimension / Scale Token |
| `--ctrl` | `40px` | Dimension / Scale Token |
| `--gap` | `14px` | Layout / Spatial Grid Token |
| `--nf-size` | `56px` | Layout / Spatial Grid Token |
| `--nf-blade-l` | `200px` | Dimension / Scale Token |
| `--dark` | `#06070A` | Canvas / Surface Token |
| `--dark2` | `#0A0A0C` | Canvas / Surface Token |
| `--foot` | `#151719` | Color / Atmospheric Token |
| `--paper` | `#F6F8FA` | Canvas / Surface Token |
| `--white` | `#FFFFFF` | Canvas / Surface Token |
| `--ink-d` | `#F0F0F2` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.hn-links> — `www-mbidirectmail-com`)**:
   - Landmark `<nav class="hn-links">` hosting `Direct Mail & Digital Marketing · Cu` navigation (`About · Capabilities · All capabilities → · Industries · Automotive 6`), DOM attributes (`data-tier="lite:cores2,mem4"`, `data-site-reveal`, `data-v-page-load-overlay="none"`, `data-v-hero-logo="wide"`), and stylesheet rule `.abt-band { margin-top: 28px; }`.
2. **Hero Stage & Focal Lead (<section.solutions-section> — `A Marketing Partner.`)**:
   - Landmark `<section class="solutions-section">` presenting display lead `A Marketing Partner.` and copy excerpt *"8 0 0 - 3 5 9 - 4 7 8 0"* over `#151515` canvas and `#F6F8FA` ink.
3. **Primary Showcase & Content Grid (<section.skip-link> — `We find the right audience. We are`)**:
   - Landmark `<section class="skip-link">` rendering section `We find the right audience. We are experts at kno...` with copy *"All capabilities →"*, asset references (`favicon.svg`, `favicon.ico`, `lenis.min.js`, `d3-array.min.js`), and grid rule `.abt-band-title { color: var(--ink); font-size: 15px; white-space: normal; }`.
4. **Interactive Detail & Feature Matrix (<section.plo-overlay> — `One partner. One team. Strategy to`)**:
   - Landmark `<section class="plo-overlay">` framing `One partner. One team. Strategy to delivery.` and `See what this looks like for your business.` (*"Printing Commercial and variable-data printing, in-house."*) with `#06070A` surface cards, `#0A0A0C` accents, and `.abt-band-rule { flex: 1 1 auto; }`.
5. **Colophon & Global Directory Footer (<footer.print-signoff> — `https://www.mbidirectmail.com/`)**:
   - Landmark `<footer class="print-signoff">` anchoring `Direct Mail & Digital Marketing ` footer links (`About · Capabilities · All capabilities → · Industries · Automotive 6`), copy *"Commercial and variable-data printing, in-house."*, and `#F6F8FA` structural dividers.
