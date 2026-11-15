# UI & UX Architecture: ads-apple-com

## Overview & Design Identity
- **Target**: `ads-apple-com` (**Apple Ads**)
- **Production URL**: [http://ads.apple.com](http://ads.apple.com)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f5f5f7` canvas, `#1d1d1f` ink, `#06c` accent)
- **Summary**: Reach customers where only Apple Ads can take you. Learn how to grow your business with ads on the App Store, Apple Maps, Apple News, MLS...
- **Total Clean CSS Variables Extracted**: `540` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Apple Legacy Chevron`
- **Body Font Stack**: `SF Pro Display`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--sk-button-display: inline-block`, `--sk-badge-display: initial`, `--sk-iconcontrol-display: inline-flex`; rule `h1` (`font-size: 1em`, `font-weight: 600`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 40px`, `line-height: 1.1`, `letter-spacing: 0em`, `font-weight: 600`)
- **Body Copy**: CSS variables `--sk-body-text-color: rgb(29, 29, 31)`, `--sk-body-background-color: rgb(255, 255, 255)`, `--sk-body-font-stack: text`; rule `p` (`font-size: 14px`, `line-height: 1.4285914286`, `letter-spacing: -.016em`, `font-weight: 400`)
- **Metadata & Labels**: CSS variables `--r-localnav-viewport-small-min-width: 320px`, `--r-localnav-viewport-small-max-width: 767px`, `--r-localnav-viewport-small-query: (min-width: 320px)`; rule `small` (`font-size: 1em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f5f7` | `var(--buystrip-background)` in `:root` |
| **Primary Typography Ink** | `#d2d2d7` | `var(--buystrip-border-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1d1d1f` | `var(--buystrip-text-color)` in `:root` |
| **Interactive Accent / Highlight** | `#06c` | `var(--buystrip-link-color)` in `:root` |
| **Secondary / Muted Copy** | `#6e6e73` | `var(--buystrip-icon-color)` in `:root` |
| **Structural Hairline Border** | `#424245` | `var(--footer-link-color)` in `:root` |
| **Variable Token (`--footer-pipe-color`)** | `#86868b` | `var(--footer-pipe-color)` in `:root` |
| **Variable Token (`--footer-directory-title-color-hover`)** | `#000` | `var(--footer-directory-title-color-hover)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--buystrip-background` | `#f5f5f7` | Canvas / Surface Token |
| `--buystrip-border-color` | `#d2d2d7` | Brand / Palette Token |
| `--buystrip-text-color` | `#1d1d1f` | Typography Ink Token |
| `--buystrip-link-color` | `#06c` | Typography Ink Token |
| `--buystrip-icon-color` | `#6e6e73` | Brand / Palette Token |
| `--buystrip-content-maxwidth` | `980px` | Layout / Spatial Grid Token |
| `--buystrip-content-padding` | `22px` | Layout / Spatial Grid Token |
| `--buystrip-items-padding-top` | `0` | Layout / Spatial Grid Token |
| `--buystrip-items-padding-bottom` | `56px` | Layout / Spatial Grid Token |
| `--footer-background` | `#f5f5f7` | Canvas / Surface Token |
| `--footer-border-color` | `#d2d2d7` | Brand / Palette Token |
| `--footer-text-color` | `#6e6e73` | Typography Ink Token |
| `--footer-link-color` | `#424245` | Typography Ink Token |
| `--footer-pipe-color` | `#86868b` | Brand / Palette Token |
| `--footer-directory-title-color` | `#1d1d1f` | Brand / Palette Token |
| `--footer-directory-title-color-hover` | `#000` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.localnav> — `ads-apple-com`)**:
   - Landmark `<nav class="localnav localnav--custom-background">` hosting `Apple Ads` navigation (` Ads · Local Nav Open Menu · Local Nav Close Menu · App Store · Apple Maps`), DOM attributes (`data-anim-scroll-group="body"`, `data-sticky="sticky"`, `data-tracking-title="App Store"`, `data-tracking-title="Apple Maps"`), and stylesheet rule `font-face { font-family: "Apple Icons 100"; src: url("../assets/ac-footer/legacy/app... }`.
2. **Hero Stage & Focal Lead (<section.hero-panel-cb> — `Enable JavaScript`)**:
   - Landmark `<section class="hero-panel-cb heroPanel-video-v1">` presenting display lead `Enable JavaScript` and copy excerpt *"Local Nav Open Menu"* over `#f5f5f7` canvas and `#1d1d1f` ink.
3. **Primary Showcase & Content Grid (<section.hero-panel-cb> — `Run ads on Apple Maps. The most di`)**:
   - Landmark `<section class="hero-panel-cb heroPanel-video-v1">` rendering section `Run ads on Apple Maps. The most direct route to r...` with copy *"Local Nav Close Menu"*, asset references (`favicon.ico`, `180_touch.png`, `ads.apple.com`, `globalheader.css`), and grid rule `ac-globalfooter { font-weight: normal; -webkit-text-size-adjust: 100%; text-size-adjust: 100% }`.
4. **Interactive Detail & Feature Matrix (<section.callout-text-with-gradient> — `Advertising that works for everyon`)**:
   - Landmark `<section class="callout-text-with-gradient section-content--fixed">` framing `Advertising that works for everyone.` and `Experiences only Apple can deliver.` (*"Please turn on JavaScript to view this page correctly."*) with `#1d1d1f` surface cards, `#06c` accents, and `after { box-sizing: content-box; margin: 0; padding: 0; pointer-events: auto; le... }`.
5. **Colophon & Global Directory Footer (<footer.js> — `http://ads.apple.com`)**:
   - Landmark `<footer class="js sa-footer">` anchoring `Apple Ads` footer links (` Ads · Local Nav Open Menu · Local Nav Close Menu · App Store · Apple Maps`), copy *"Promote your brand in the places people love and trust. Appl"*, and `#424245` structural dividers.
