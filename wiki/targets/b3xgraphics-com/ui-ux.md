# UI & UX Architecture: b3xgraphics-com

## Overview & Design Identity
- **Target**: `b3xgraphics-com` (**B3X Graphics · Freelance Sports Art Director & Designer**)
- **Production URL**: [https://b3xgraphics.com/](https://b3xgraphics.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#04b5ff` canvas, `#a00` ink, `#008a20` accent)
- **Summary**: B3X Graphics: freelance art direction and design specialising in sport. Branding, campaign design and socials content for some of the big...
- **Total Clean CSS Variables Extracted**: `192` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `B3XH Aileron`
- **Body Font Stack**: `B3XH FA`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`, `--cc-font-display: 'Palma Heavy', sans-serif`; rule `h1` (`font-size: 2.5rem`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2rem`)
- **Body Copy**: CSS variables `--cc-font-body: 'Aileron', sans-serif`; rule `body` (`font-size: 1rem`, `line-height: 1.5`, `font-weight: 400`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `1rem`, `13px`, `12px`, `14.6px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#04b5ff` | `var(--b3xh-sky)` in `:root` |
| **Primary Typography Ink** | `#03b2cb` | `var(--PhoneInput-color--focus)` in `:root` |
| **Elevated Surface / Card Substrate** | `#720eec` | `var(--woocommerce)` in `:root` |
| **Interactive Accent / Highlight** | `#008a20` | `var(--wc-green)` in `:root` |
| **Secondary / Muted Copy** | `#a00` | `var(--wc-red)` in `:root` |
| **Structural Hairline Border** | `#ffba00` | `var(--wc-orange)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--b3xh-side` | `clamp(20px,2.2vw,50px)` | Dimension / Scale Token |
| `--b3xh-max` | `1820px` | Dimension / Scale Token |
| `--b3xh-sky` | `#04b5ff` | Color / Atmospheric Token |
| `--b3xh-glass` | `linear-gradient(155deg,rgba(9,26,54,0.66) 0%,rgba(3,13,30,0.74) 100%)` | Color / Atmospheric Token |
| `--PhoneInput-color--focus` | `#03b2cb` | Brand / Palette Token |
| `--PhoneInputInternationalIconPhone-opacity` | `0.8` | Canvas / Surface Token |
| `--PhoneInputInternationalIconGlobe-opacity` | `0.65` | Canvas / Surface Token |
| `--PhoneInputCountrySelect-marginRight` | `0.35em` | Layout / Spatial Grid Token |
| `--PhoneInputCountrySelectArrow-width` | `0.3em` | Brand / Palette Token |
| `--PhoneInputCountrySelectArrow-marginLeft` | `var(--PhoneInputCountrySelect-marginRight)` | Brand / Palette Token |
| `--PhoneInputCountrySelectArrow-borderWidth` | `1px` | Brand / Palette Token |
| `--PhoneInputCountrySelectArrow-opacity` | `0.45` | Brand / Palette Token |
| `--PhoneInputCountrySelectArrow-color` | `currentColor` | Brand / Palette Token |
| `--PhoneInputCountrySelectArrow-color--focus` | `var(--PhoneInput-color--focus)` | Brand / Palette Token |
| `--PhoneInputCountrySelectArrow-transform` | `rotate(45deg)` | Brand / Palette Token |
| `--PhoneInputCountryFlag-aspectRatio` | `1.5` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.b3xh-bar> — `b3xgraphics-com`)**:
   - Landmark `<header class="b3xh-bar">` hosting `B3X Graphics · Freelance Sports Art ` navigation (`Home · Projects · The Lab · About · Shop`), DOM attributes (`data-b3xh-page="home"`, `data-b3xh-bound="1"`, `data-elementor-type="wp-page"`, `data-elementor-id="1301"`), and stylesheet rule `after { box-sizing:border-box; }`.
2. **Hero Stage & Focal Lead (<section.b3xr-feat> — `B3X Graphics Studio`)**:
   - Landmark `<section class="b3xr-feat">` presenting display lead `B3X Graphics Studio` and copy excerpt *"Available for new projects"* over `#04b5ff` canvas and `#a00` ink.
3. **Primary Showcase & Content Grid (<section.b3xt> — `Freelance Art Director & Designer`)**:
   - Landmark `<section class="b3xt b3xt-armed">` rendering section `Freelance Art Director & Designer` with copy *"I work with some of the biggest brands in sport"*, asset references (`favicon.svg`, `chrome.css`, `chrome.js`, `fonts.css`), and grid rule `.b3xh .b3xh-defs { position:absolute;width:0;height:0;overflow:hidden;pointer-events:none; }`.
4. **Interactive Detail & Feature Matrix (<section.b3xt> — `Featured projects`)**:
   - Landmark `<section class="b3xt b3xt-armed">` framing `Featured projects` and `2025/26 WSL Champions` (*"2025/26 WSL Champions Social Media"*) with `#720eec` surface cards, `#008a20` accents, and `.b3xh .b3xh-burger:active { background:transparent;color:fff;border:0; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://b3xgraphics.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `B3X Graphics · Freelance Sports ` footer links (`Home · Projects · The Lab · About · Shop`), copy *"Spurs 1901 Anniversary Social Media"*, and `#ffba00` structural dividers.
