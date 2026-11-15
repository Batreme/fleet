# UI & UX Architecture: loopsii-com

## Overview & Design Identity
- **Target**: `loopsii-com` (**Loopsii: the all-in-one app for freelancers**)
- **Production URL**: [https://loopsii.com/](https://loopsii.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f0f0f0` / `#fff`)
- **Summary**: Loopsii is the all-in-one app for freelancers: CRM, project management, time tracking, AI notes from client calls and dictation. 14-day f...
- **Total Clean CSS Variables Extracted**: `158` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Saans VF-1156b2189454d62c`
- **Body Font Stack**: `Saans VF-1156b2189454d62c fallback: Arial`
- **Monospace / Technical Font Stack**: `Geist Mono-c001706f58ecc7d6`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(14.4px, 16 * var(--spacing)`, `clamp(16px, 20 * var(--spacing)`, `clamp(14.4px, 18 * var(--spacing)`, `clamp(16.2px, 18 * var(--spacing)`, `clamp(12.6px, 14 * var(--spacing)`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: calc(28 * var(--spacing))`, `letter-spacing: -.01em`)
- **Body Copy**: CSS variables `--font-body: var(--font-title)`
- **Metadata & Labels**: CSS variables `--tp-label-foreground-color: #fff9`, `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f0f0f0` | `var(--color-grey)` in `:root` |
| **Primary Typography Ink** | `#c5c5c5` | `var(--color-dark-grey)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `var(--color-white)` in `:root` |
| **Secondary / Muted Copy** | `#c4f041` | `var(--color-main)` in `:root` |
| **Structural Hairline Border** | `#e0f661` | `var(--color-lime-light)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-body` | `var(--font-title)` | Typography / Scale Token |
| `--dw` | `1920` | Design System Custom Token |
| `--dh` | `900` | Design System Custom Token |
| `--to-vh` | `var(--dh) * 100vh` | Layout / Spatial Grid Token |
| `--screen-h` | `100lvh` | Dimension / Scale Token |
| `--size-unit` | `16` | Layout / Spatial Grid Token |
| `--hand-scale` | `1.5` | Design System Custom Token |
| `--size-container-ideal` | `1920` | Layout / Spatial Grid Token |
| `--size-container-min` | `1200px` | Layout / Spatial Grid Token |
| `--size-container-max` | `2560px` | Layout / Spatial Grid Token |
| `--size-container` | `clamp(var(--size-container-min), 100vw, var(--size-container-max))` | Layout / Spatial Grid Token |
| `--ease` | `.8s cubic-bezier(.84, 0, .16, 1)` | Motion / Easing Token |
| `--fast-ease` | `.6s cubic-bezier(.84, 0, .16, 1)` | Motion / Easing Token |
| `--smooth` | `cubic-bezier(.76, 0, .24, 1)` | Motion / Timing Token |
| `--color-ease` | `.4s ease-out` | Brand / Palette Token |
| `--multiplier` | `.2` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.is-loading> — `loopsii-com`)**:
   - Landmark `<header class="is-loading">` hosting `Loopsii: the all-in-one app for free` navigation (`W h y L o o p s i i · F e a t u r e s · P r i c i n g`), DOM attributes (`data-transition="wrapper"`, `data-loader`, `data-module="NavMorph"`, `data-track="nav-logo"`), and stylesheet rule `root { --font-title:"Saans VF-1156b2189454d62c","Saans VF-1156b2189454d62c fall... }`.
2. **Hero Stage & Focal Lead (<section.intro> — `Loopsii, the all-in-one app for fr`)**:
   - Landmark `<section class="intro relative">` presenting display lead `Loopsii, the all-in-one app for freelancers` and copy excerpt *"W h y L o o p s i i"* over `#f0f0f0` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.distraction> — `The all-in-one app for freelancers`)**:
   - Landmark `<section class="distraction relative">` rendering section `The all-in-one app for freelancers. Like a person...` with copy *"S i g n u p f o r f r e e"*, asset references (`f1306f12b629075b.woff2`, `fd3499837a53ca88.woff2`, `favicon.ico`, `favicon.svg`), and grid rule `.v-text { writing-mode:vertical-lr }`.
4. **Interactive Detail & Feature Matrix (<section.app-demo> — `Loopsii helps freelance designers `)**:
   - Landmark `<section class="app-demo relative">` framing `Loopsii helps freelance designers and developers...` and `That's why Loopsii exists` (*"Start your loop here"*) with `#000` surface cards, `#fff` accents, and `.display { font-size:calc(164 * var(--spacing));letter-spacing:-.02em;font-variatio... }`.
5. **Colophon & Global Directory Footer (<footer.fixed> — `https://loopsii.com/`)**:
   - Landmark `<footer class="fixed">` anchoring `Loopsii: the all-in-one app for ` footer links (`W h y L o o p s i i · F e a t u r e s · P r i c i n g`), copy *"One account, all your clients, one simple workflow"*, and `#e0f661` structural dividers.
