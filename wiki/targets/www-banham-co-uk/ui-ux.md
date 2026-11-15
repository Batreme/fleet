# UI & UX Architecture: www-banham-co-uk

## Overview & Design Identity
- **Target**: `www-banham-co-uk` (**Banham · Experts in Security Services Since 1926**)
- **Production URL**: [https://www.banham.co.uk/](https://www.banham.co.uk/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#0000` canvas, `#000` ink, `#2b3239` accent)
- **Summary**: Welcome to Banham, market-leaders in the security industry since 1926, and the perfect people to help secure your property
- **Total Clean CSS Variables Extracted**: `138` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `IvarText`
- **Body Font Stack**: `IvarItalic`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--dfd-btn-display: inline-flex`, `--dfd-btn-group-display: flex`; rule `,h1` (`font-size: 2.25rem`, `line-height: 2.5rem`, `letter-spacing: .36px`)
- **Section Heading (`H2`)**: rule `,h2` (`font-size: 28px`, `line-height: 1.25`, `letter-spacing: .28px`)
- **Body Copy**: rule `p` (`font-size: .875rem`, `line-height: 1.25rem`)
- **Metadata & Labels**: rule `.label` (`font-size: 1rem`, `line-height: 1.5rem`, `font-weight: 600`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0000` | `var(--btn-stroke)` in `:root` |
| **Primary Typography Ink** | `#333e48` | `var(--btn-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--btn-color)` in `:root` |
| **Interactive Accent / Highlight** | `#2b3239` | `var(--btn-hover-bg)` in `:root` |
| **Secondary / Muted Copy** | `#000` | `var(--line-after)` in `:root` |
| **Structural Hairline Border** | `#8392a7` | `var(--color-cornflower-100)` in `:root` |
| **Variable Token (`--color-amsb_graystarts`)** | `#cbd5e0` | `var(--color-amsb_graystarts)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--btn-stroke` | `#0000` | Elevation / Border Token |
| `--btn-bg` | `#333e48` | Canvas / Surface Token |
| `--btn-color` | `#fff` | Brand / Palette Token |
| `--btn-hover-bg` | `#2b3239` | Canvas / Surface Token |
| `--btn-active-bg` | `#2b3239` | Canvas / Surface Token |
| `--line-after` | `#000` | Color / Atmospheric Token |
| `--line-before` | `#0000` | Color / Atmospheric Token |
| `--width-am-latter` | `32px` | Layout / Spatial Grid Token |
| `--width-am-brand` | `120px` | Brand / Palette Token |
| `--width-am-popup-content` | `600px` | Layout / Spatial Grid Token |
| `--height-am-latter` | `32px` | Layout / Spatial Grid Token |
| `--height-am-popup-content` | `415px` | Layout / Spatial Grid Token |
| `--background-size-size20` | `20px` | Canvas / Surface Token |
| `--color-cornflower-100` | `#8392a7` | Brand / Palette Token |
| `--padding-full` | `100%` | Layout / Spatial Grid Token |
| `--color-amsb_graystarts` | `#cbd5e0` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.page-header> — `www-banham-co-uk`)**:
   - Landmark `<header class="page-header">` hosting `Banham · Experts in Security Service` navigation (`Book a Survey · Locks · All Locks · Door Locks · Emergency Locksmiths`), DOM attributes (`data-mm-order="40"`, `data-mm-order="50"`, `data-ueto="ueto_4f22d9b1ed"`, `data-uid="zfDhhC1778"`), and stylesheet rule `container.chosen-with-drop .chose... { clip:auto;-webkit-clip-path:none;clip-path:none }`.
2. **Hero Stage & Focal Lead (<section.message> — `Which Banham products are you inte`)**:
   - Landmark `<section class="message global">` presenting display lead `Which Banham products are you interested in?` and copy excerpt *"Prefer to call? Reach us on 020 7819 3730"* over `#0000` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.storyblok-home> — `About Your Enquiry`)**:
   - Landmark `<section class="storyblok-home">` rendering section `About Your Enquiry` with copy *"Which Banham products are you interested in?"*, asset references (`styles.min.css`, `chosen.min.css`, `trustpilot.min.css`, `Banham_Logo_FA-04.png`), and grid rule `.chosen-container a { cursor:pointer }`.
4. **Interactive Detail & Feature Matrix (<section.fixed> — `We’ll need a little information ab`)**:
   - Landmark `<section class="fixed w-full">` framing `We’ll need a little information about you` and `Search for the property you’d like surveyed` (*"About Your Enquiry"*) with `#fff` surface cards, `#2b3239` accents, and `en-container .search-choice .grou... { margin-right:4px;overflow:hidden;white-space:nowrap;text-overflow:ellips... }`.
5. **Colophon & Global Directory Footer (<footer.footer-container> — `https://www.banham.co.uk/`)**:
   - Landmark `<footer class="footer-container">` anchoring `Banham · Experts in Security Ser` footer links (`Book a Survey · Locks · All Locks · Door Locks · Emergency Locksmiths`), copy *"We’ll need a little information about you"*, and `#8392a7` structural dividers.
