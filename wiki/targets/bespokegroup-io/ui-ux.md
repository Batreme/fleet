# UI & UX Architecture: bespokegroup-io

## Overview & Design Identity
- **Target**: `bespokegroup-io` (**Bespoke Group · Private Wealth & Estate Planning Advisory**)
- **Production URL**: [https://bespokegroup.io/](https://bespokegroup.io/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#474747` ink, `#9c9c9c` accent)
- **Summary**: Bespoke Group provides expert wealth management, estate planning, and advisory services for HNWIs and families. Tailored strategies for a...
- **Total Clean CSS Variables Extracted**: `23` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Booton`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 42px`, `line-height: 50px`)
- **Section Heading (`H2`)**: rule `h2` (`letter-spacing: -.02em`, `font-weight: 300`)
- **Body Copy**: rule `p` (`letter-spacing: 0!important`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `64px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#f4f5f2` | `var(--color-off-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#cdcdcd` | `var(--color-grey-300)` in `:root` |
| **Interactive Accent / Highlight** | `#9c9c9c` | `var(--color-grey-400)` in `:root` |
| **Secondary / Muted Copy** | `#636363` | `var(--color-grey-600)` in `:root` |
| **Structural Hairline Border** | `#474747` | `var(--color-grey-700)` in `:root` |
| **Variable Token (`--color-grey-900`)** | `#2a2a2a` | `var(--color-grey-900)` in `:root` |
| **Variable Token (`--color-grey-1000`)** | `#0d0d0d` | `var(--color-grey-1000)` in `:root` |
| **Variable Token (`--color-black`)** | `#000` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-off-black`)** | `#333` | `var(--color-off-black)` in `:root` |
| **Variable Token (`--color-linen`)** | `#f7e9e0` | `var(--color-linen)` in `:root` |
| **Variable Token (`--color-champagne`)** | `#dac9be` | `var(--color-champagne)` in `:root` |
| **Variable Token (`--color-beige`)** | `#ebcfbc` | `var(--color-beige)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cubic-easing` | `cubic-bezier(0.215,0.61,0.355,1)` | Motion / Easing Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-off-white` | `#f4f5f2` | Canvas / Surface Token |
| `--color-grey-300` | `#cdcdcd` | Brand / Palette Token |
| `--color-grey-400` | `#9c9c9c` | Brand / Palette Token |
| `--color-grey-500` | `grey` | Brand / Palette Token |
| `--color-grey-600` | `#636363` | Brand / Palette Token |
| `--color-grey-700` | `#474747` | Brand / Palette Token |
| `--color-grey-800` | `#474747` | Brand / Palette Token |
| `--color-grey-900` | `#2a2a2a` | Brand / Palette Token |
| `--color-grey-1000` | `#0d0d0d` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-off-black` | `#333` | Canvas / Surface Token |
| `--color-linen` | `#f7e9e0` | Brand / Palette Token |
| `--color-champagne` | `#dac9be` | Brand / Palette Token |
| `--color-beige` | `#ebcfbc` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `bespokegroup-io`)**:
   - Landmark `<header class="header header--dark">` hosting `Bespoke Group · Private Wealth & Est` navigation (`S e r v i c e s · A d v i s o r y · A b o u t · P e o p l e · R e s o u r c e s`), DOM attributes (`data-cfasync="false"`, `data-pagespeed-no-defer`, `data-cfasync="false"`, `data-cfasync="false"`), and stylesheet rule `before { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.acf_hero-scene> — `Bespoke Wealth Operating Systems`)**:
   - Landmark `<section class="acf_hero-scene">` presenting display lead `Bespoke Wealth Operating Systems` and copy excerpt *"We value your privacy"* over `#fff` canvas and `#474747` ink.
3. **Primary Showcase & Content Grid (<section.acf_text-animation> — `Transform Chaos into Order`)**:
   - Landmark `<section class="acf_text-animation">` rendering section `Transform Chaos into Order` with copy *"We use cookies to enhance your browsing experience, serve persona"*, asset references (`gtm.js`, `www.googletagmanager.com`, `hero.home_.webp`, `logomark.png`), and grid rule `strong { font-weight:bolder }`.
4. **Interactive Detail & Feature Matrix (<article.acf_text-animation__content> — `We help the world’s most successfu`)**:
   - Landmark `<article class="acf_text-animation__content grid">` framing `We help the world’s most successful entrepreneurs...` and `Tailored and Integrated Wealth Systems` (*"Customise Consent Preferences"*) with `#cdcdcd` surface cards, `#9c9c9c` accents, and `samp { font-family:ui-monospace,SFMono-Regular,Consolas,Liberation Mono,Menlo,m... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://bespokegroup.io/`)**:
   - Landmark `<footer class="footer footer--no-newsletter">` anchoring `Bespoke Group · Private Wealth &` footer links (`S e r v i c e s · A d v i s o r y · A b o u t · P e o p l e · R e s o u r c e s`), copy *"We use cookies to help you navigate efficiently and perform "*, and `#474747` structural dividers.
