# UI & UX Architecture: monument-tv

## Overview & Design Identity
- **Target**: `monument-tv` (**Homepage - Monument**)
- **Production URL**: [https://monument.tv/](https://monument.tv/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#760000` / `#020202`)
- **Summary**: Monument is an independent creative production company specializing in unscripted television, documentary, and reality tv. We deliver inn...
- **Total Clean CSS Variables Extracted**: `83` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `neue-haas-grotesk-text`
- **Body Font Stack**: `obviously-narrow`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `1rem`, `1.375rem`, `4.2666666667vw`, `2.0833333333vw`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2rem`, `line-height: 1`, `letter-spacing: -.02em`, `font-weight: 500`)
- **Body Copy**: rule `p` (`font-size: 0.75rem`)
- **Metadata & Labels**: CSS variables `--letter-spacing: 0`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#760000` | `var(--japanese-maple)` in `:root` |
| **Primary Typography Ink** | `#eee3d1` | `var(--aths-special)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f85e34` | `var(--flamingo)` in `:root` |
| **Interactive Accent / Highlight** | `#020202` | `var(--black)` in `:root` |
| **Secondary / Muted Copy** | `#ce1f1a` | `var(--thunderbird)` in `:root` |
| **Structural Hairline Border** | `#3b758b` | `var(--ming)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--underline-width` | `0%` | Layout / Spatial Grid Token |
| `--hover-duration` | `0.3s` | Motion / Easing Token |
| `--japanese-maple` | `#760000` | Color / Atmospheric Token |
| `--aths-special` | `#eee3d1` | Color / Atmospheric Token |
| `--flamingo` | `#f85e34` | Color / Atmospheric Token |
| `--box-padding` | `3rem` | Layout / Spatial Grid Token |
| `--global-padding` | `0.75rem` | Layout / Spatial Grid Token |
| `--font-size` | `1.5rem` | Typography / Scale Token |
| `--pin-spacing` | `2.25` | Layout / Spatial Grid Token |
| `--pin` | `0` | Design System Custom Token |
| `--line-height` | `1` | Typography / Scale Token |
| `--padding` | `0.625rem` | Layout / Spatial Grid Token |
| `--clip-right` | `100%` | Dimension / Scale Token |
| `--clip-left` | `100%` | Dimension / Scale Token |
| `--dheight` | `calc(var(--dvh) + 1px)` | Layout / Spatial Grid Token |
| `--text-transform` | `normal` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.no-scrollbar> — `monument-tv`)**:
   - Landmark `<header class="no-scrollbar">` hosting `Homepage - Monument` navigation (`Work · About · Team · Casting · Press`), DOM attributes (`data-parent`, `data-template="homepage"`, `data-component="navbar"`, `data-component="vector-grid"`), and stylesheet rule `before { box-sizing:inherit;-webkit-tap-highlight-color:rgba(0,0,0,0) }`.
2. **Hero Stage & Focal Lead (<section.cookieconsent> — `Thank you for reaching out`)**:
   - Landmark `<section class="cookieconsent is-inview">` presenting display lead `Thank you for reaching out` and copy excerpt *"We and our partners use cookies and other technologies to improve"* over `#760000` canvas and `#eee3d1` ink.
3. **Primary Showcase & Content Grid (<section.cookieconsent__module> — `Pitch us your idea. We’re eager to`)**:
   - Landmark `<section class="cookieconsent__module cookieconsent__main">` rendering section `Pitch us your idea. We’re eager to hear` with copy *"Manage preferences"*, asset references (`essential.css`, `breeze-prefetch-links.min.js`, `common.js`, `vendors-common.js`), and grid rule `video { height:auto;max-width:100% }`.
4. **Interactive Detail & Feature Matrix (<section.cookieconsent__actions> — `We're looking forward to hearing f`)**:
   - Landmark `<section class="cookieconsent__actions">` framing `We're looking forward to hearing from you.` and `Broken. Beyond Repair?` (*"Essential Essential cookies enable basic functions and are necess"*) with `#f85e34` surface cards, `#020202` accents, and `.main-preloader { font-size:1.375rem;font-size:var(--font-size,1.375rem);padding:var(--box... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://monument.tv/`)**:
   - Landmark `<footer class="footer sticky-root">` anchoring `Homepage - Monument` footer links (`Work · About · Team · Casting · Press`), copy *"Essential cookies enable basic functions and are necessary f"*, and `#3b758b` structural dividers.
