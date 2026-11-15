# UI & UX Architecture: daddyyankee-com

## Overview & Design Identity
- **Target**: `daddyyankee-com` (**Daddy Yankee · Official Website**)
- **Production URL**: [https://daddyyankee.com/](https://daddyyankee.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ece8dc` / `#efee32`)
- **Summary**: The official Daddy Yankee website. Discover La Postal, his upcoming album, listen to his new single, and get the latest from Daddy Yankee.
- **Total Clean CSS Variables Extracted**: `101` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ABC Diatype Compressed`
- **Body Font Stack**: `Ayer`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Body Copy**: CSS variables `--_typography---body-family: "Inter Tight 500",Arial,sans-serif`, `--_theme---body: var(--_swatch---swatch--black)`, `--_typography---body-line-height: 1.2`
- **Metadata & Labels**: CSS variables `--text-style--body-small: max(1em,16px)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ece8dc` | `var(--_swatch---swatch--cream)` in `:root` |
| **Primary Typography Ink** | `#3465a7` | `var(--_swatch---swatch--blue)` in `:root` |
| **Elevated Surface / Card Substrate** | `#17376f` | `var(--_swatch---swatch--blue-dark)` in `:root` |
| **Interactive Accent / Highlight** | `#efee32` | `var(--_swatch---swatch--yellow)` in `:root` |
| **Secondary / Muted Copy** | `#e4332a` | `var(--_swatch---swatch--red)` in `:root` |
| **Structural Hairline Border** | `#244a98` | `var(--_swatch---swatch--blue-mid)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_theme---background` | `var(--_swatch---swatch--cream)` | Canvas / Surface Token |
| `--_typography---body-family` | `"Inter Tight 500",Arial,sans-serif` | Typography / Scale Token |
| `--_theme---body` | `var(--_swatch---swatch--black)` | Brand / Palette Token |
| `--size-font` | `calc(var(--size-container)/(var(--size-container-ideal)/var(--size-unit)))` | Typography / Scale Token |
| `--_typography---body-line-height` | `1.2` | Typography / Scale Token |
| `--_typography---body-weight` | `500` | Design System Custom Token |
| `--_typography---body-letter-space` | `-.03em` | Layout / Spatial Grid Token |
| `--_typography---heading-family` | `"ABC Diatype Compressed",Impact,sans-serif` | Typography Ink Token |
| `--text-style--64` | `4em` | Typography Ink Token |
| `--_typography---heading-line-height` | `.8` | Typography Ink Token |
| `--_typography---heading-weight` | `900` | Typography Ink Token |
| `--_typography---heading-letter-space` | `-.02em` | Typography Ink Token |
| `--text-style--32` | `2em` | Typography Ink Token |
| `--site-margin` | `.75em` | Layout / Spatial Grid Token |
| `--_swatch---swatch--cream` | `#ece8dc` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.bold-nav-full> — `daddyyankee-com`)**:
   - Landmark `<nav class="bold-nav-full">` hosting `Daddy Yankee · Official Website` navigation (`STORE · FOUNDATIONS · GLOBALIZATION · CRYSTALLIZATION · Store`), DOM attributes (`data-wf-domain="daddyyankee.com"`, `data-wf-page="6ab927d471adf53e60a6e4f4"`, `data-wf-site="6ab927d171adf53e60a6e4a4"`, `data-cky-tag="notice"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero_wrap> — `LA POSTAL`)**:
   - Landmark `<section class="hero_wrap u-section">` presenting display lead `LA POSTAL` and copy excerpt *"We value your privacy"* over `#ece8dc` canvas and `#17376f` ink.
3. **Primary Showcase & Content Grid (<section.portrait_wrap> — `2002`)**:
   - Landmark `<section class="portrait_wrap u-section">` rendering section `2002` with copy *"We use cookies to enhance your browsing experience, serve persona"*, asset references (`cdn.prod.website-files.com`, `daddy-yankee.webflow.shared.3af00...`, `script.js`, `gtm.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.tl_wrap> — `THE`)**:
   - Landmark `<section class="tl_wrap u-section">` framing `THE` and `RISE` (*"Customise Consent Preferences"*) with `#17376f` surface cards, `#efee32` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer_wrap> — `https://daddyyankee.com/`)**:
   - Landmark `<footer class="footer_wrap u-section">` anchoring `Daddy Yankee · Official Website` footer links (`STORE · FOUNDATIONS · GLOBALIZATION · CRYSTALLIZATION · Store`), copy *"We use cookies to help you navigate efficiently and perform "*, and `#244a98` structural dividers.
