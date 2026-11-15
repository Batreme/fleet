# UI & UX Architecture: ringpopcandy-com

## Overview & Design Identity
- **Target**: `ringpopcandy-com` (**Ring Pop® — Candy for Every Celebration**)
- **Production URL**: [https://ringpopcandy.com/](https://ringpopcandy.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#2B3990` accent)
- **Summary**: Ring Pop turns any occasion into a celebration: birthdays, weddings, game days, wins. Shop the collections and find Ring Pop at a store n...
- **Total Clean CSS Variables Extracted**: `984` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `hwt-artz`
- **Body Font Stack**: `area-normal`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--x-shell-disclosure-display: block`, `--x-shell-order-summary-display: none`, `--x-shell-content-display: grid`; rule `h1` (`font-size: var(--text-lg)`, `line-height: var(--tw-leading, var...`)
- **Section Heading (`H2`)**: CSS variables `--font-heading-h2: 'Ringold', Helvetica, Arial, sans-serif`, `--font-heading-h2-weight: 400`, `--h2-font-case: uppercase`; rule `h2` (`font-size: var(--text-lg)`, `line-height: var(--tw-leading, var...`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`, `--color-body-text: #141723`; rule `p` (`font-size: var(--font-body-size-large-mo...`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `.label` (`font-size: 1.5rem`, `line-height: 1.083em`, `letter-spacing: -.0225rem`, `font-weight: 600`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#FFB925` | `var(--oke-stars-foregroundColor)` in `:root` |
| **Interactive Accent / Highlight** | `#2B3990` | `var(--oke-button-backgroundColor)` in `:root` |
| **Secondary / Muted Copy** | `#FF8300` | `var(--oke-text-secondaryColor)` in `:root` |
| **Structural Hairline Border** | `#FFFFFF` | `var(--oke-avatar-placeholderTextColor)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-red-600` | `oklch(57.7% .245 27.325)` | Brand / Palette Token |
| `--color-gray-100` | `oklch(96.7% .003 264.542)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `1.5` | Typography Ink Token |
| `--text-lg` | `1.125rem` | Typography Ink Token |
| `--text-lg--line-height` | `calc(1.75 / 1.125)` | Typography Ink Token |
| `--text-xl` | `1.25rem` | Typography Ink Token |
| `--text-xl--line-height` | `calc(1.75 / 1.25)` | Typography Ink Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `ringpopcandy-com`)**:
   - Landmark `<header class="header is-inview">` hosting `Ring Pop® — Candy for Every Celebrat` navigation (`Products · Explore · About`), DOM attributes (`data-toggler=".is-fixed"`, `data-id="CGMRQMBC77UCKR5263C0"`, `data-ot-ignore`, `data-source-attribution="shopify.exit_intersti..."`), and stylesheet rule `.footer__main { font-size:var(--footer-font-size);line-height:var(--footer-line-height);... }`.
2. **Hero Stage & Focal Lead (<section.mfr-core__hero-section> — `Ring Pop`)**:
   - Landmark `<section class="mfr-core__hero-section overflow-hidden">` presenting display lead `Ring Pop` and copy excerpt *"Press Option+1 for screen-reader mode, Option+0 to cancel"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.mfr-core__banner-with-box> — `A little Bling to Celebrate Your T`)**:
   - Landmark `<section class="mfr-core__banner-with-box grid-gutter-mobile">` rendering section `A little Bling to Celebrate Your Thing` with copy *"Accessibility Screen-Reader Guide, Feedback, and Issue Reporting "*, asset references (`main.ea8e9e85.js`, `identify_7e562ea6.js`, `main.MTAyNjc1NzVmOQ.js`, `events.js`), and grid rule `.footer__big-menu-list li a { position:relative;line-height:1.679em;letter-spacing:-.1rem }`.
4. **Interactive Detail & Feature Matrix (<section.mfr-core__scrolling-bar> — `The Sweetest Way To Say Yes!`)**:
   - Landmark `<section class="mfr-core__scrolling-bar">` framing `The Sweetest Way To Say Yes!` and `A ring for every thing.` (*"Explore Collections"*) with `#FFB925` surface cards, `#2B3990` accents, and `.footer__big-menu-list li a:hover... { -moz-transform:unset;-o-transform:unset;-ms-transform:unset;-webkit-tran... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://ringpopcandy.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Ring Pop® — Candy for Every Cele` footer links (`Products · Explore · About`), copy *"We respond within one business day. For press or wholesale, "*, and `#FFFFFF` structural dividers.
