# UI & UX Architecture: about-centra-com

## Overview & Design Identity
- **Target**: `about-centra-com` (**Centra? Centra! The definitive guide.**)
- **Production URL**: [https://about.centra.com](https://about.centra.com)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#d9d9d9` canvas, `#191919` ink, `#f85943` accent)
- **Summary**: The commerce platform for fashion brands.
- **Total Clean CSS Variables Extracted**: `150` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `neue-haas-grotesk-display`
- **Body Font Stack**: `neue-haas-grotesk-text`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Body Copy**: rule `p` (`font-size: inherit`, `font-weight: inherit`)
- **Metadata & Labels**: CSS variables `--_colours---mono--0: white`, `--_colours---mono--900: black`, `--_colours---mono--300: darkgrey`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#d9d9d9` | `var(--_colours---mono--200)` in `:root` |
| **Primary Typography Ink** | `#fecf48` | `var(--_colours---yellow--main)` in `:root` |
| **Elevated Surface / Card Substrate** | `#191919` | `var(--_colours---mono--800)` in `:root` |
| **Interactive Accent / Highlight** | `#f85943` | `var(--_colours---red--main)` in `:root` |
| **Secondary / Muted Copy** | `#333` | `var(--_colours---mono--600)` in `:root` |
| **Structural Hairline Border** | `#1cad56` | `var(--_colours---green--main)` in `:root` |
| **Variable Token (`--_colours---blue--main`)** | `#1d80f6` | `var(--_colours---blue--main)` in `:root` |
| **Variable Token (`--_colours---mono--400`)** | `#787878` | `var(--_colours---mono--400)` in `:root` |
| **Variable Token (`--_colours---mono--700`)** | `#252525` | `var(--_colours---mono--700)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_colours---mono--0` | `white` | Typography / Scale Token |
| `--_colours---mono--900` | `black` | Typography / Scale Token |
| `--_colours---mono--300` | `darkgrey` | Typography / Scale Token |
| `--_colours---mono--200` | `#d9d9d9` | Typography / Scale Token |
| `--padding-inner-md` | `40px` | Layout / Spatial Grid Token |
| `--_colours---yellow--main` | `#fecf48` | Layout / Spatial Grid Token |
| `--padding-section-xl` | `90px` | Layout / Spatial Grid Token |
| `--padding-inner-sm` | `20px` | Layout / Spatial Grid Token |
| `--_colours---mono--800` | `#191919` | Typography / Scale Token |
| `--_colours---red--main` | `#f85943` | Layout / Spatial Grid Token |
| `--_colours---mono--600` | `#333` | Typography / Scale Token |
| `--_colours---green--main` | `#1cad56` | Layout / Spatial Grid Token |
| `--_colours---blue--main` | `#1d80f6` | Layout / Spatial Grid Token |
| `--padding-inner-lg` | `80px` | Layout / Spatial Grid Token |
| `--_colours---mono--400` | `#787878` | Typography / Scale Token |
| `--_colours---mono--700` | `#252525` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.navigation-glass-wrapper> — `about-centra-com`)**:
   - Landmark `<nav class="navigation-glass-wrapper mobile-navigation">` hosting `Centra? Centra! The definitive guide` navigation (`13 ½ Centra Facts · Brands on Centra`), DOM attributes (`data-wf-domain="about.centra.com"`, `data-wf-page="6a0af5d1e1f707540842bee4"`, `data-wf-site="6a0af5d1e1f707540842bf02"`, `data-cbid="93a8c043-1906-4454-86..."`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.heading-animation> — `Centra? Centra!`)**:
   - Landmark `<section class="heading-animation">` presenting display lead `Centra? Centra!` and copy excerpt *"Necessary 10 Necessary cookies help make a website usable by enab"* over `#d9d9d9` canvas and `#191919` ink.
3. **Primary Showcase & Content Grid (<section.section-parallax> — `Yes, it’s us. Centra. The famously`)**:
   - Landmark `<section class="section-parallax">` rendering section `Yes, it’s us. Centra. The famously unfamous comme...` with copy *"Cookiebot 1 Learn more about this provider CookieConsent Stores t"*, asset references (`cdn.prod.website-files.com`, `centra-centra.webflow.shared.3f63...`, `cc.js`, `configuration.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section-call-to-action> — `Centra preview in 60 seconds`)**:
   - Landmark `<section class="section-call-to-action">` framing `Centra preview in 60 seconds` and `Learn more about this provider` (*"Learn more about this provider"*) with `#191919` surface cards, `#f85943` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.wf-neuehaasgrotesktext-n4-active> — `https://about.centra.com`)**:
   - Landmark `<footer class="wf-neuehaasgrotesktext-n4-active">` anchoring `Centra? Centra! The definitive g` footer links (`13 ½ Centra Facts · Brands on Centra`), copy *"Stores the user's cookie consent state for the current domai"*, and `#1cad56` structural dividers.
