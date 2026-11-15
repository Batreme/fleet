# UI & UX Architecture: www-brandlos-nl

## Overview & Design Identity
- **Target**: `www-brandlos-nl` (**Brandlos · Het creatieve bureau van Limburg**)
- **Production URL**: [https://www.brandlos.nl](https://www.brandlos.nl)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f4f4f4` canvas, `#040404` ink, `#3a39ff` accent)
- **Summary**: Creatief bureau in Limburg. Wij bouwen merken met lef en karakter: van strategie en identiteit tot campagnes die opvallen. Geen grijze mu...
- **Total Clean CSS Variables Extracted**: `11` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Vastagogrotesk`
- **Body Font Stack**: `Arial`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f4f4` | `var(--_global-vars---light)` in `:root` |
| **Primary Typography Ink** | `#040404` | `var(--_global-vars---dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fbd050` | `var(--_global-vars---accent-1)` in `:root` |
| **Interactive Accent / Highlight** | `#3a39ff` | `var(--_global-vars---accent-2)` in `:root` |
| **Secondary / Muted Copy** | `#ff5b23` | `var(--_global-vars---accent-5)` in `:root` |
| **Structural Hairline Border** | `#ade6ed` | `var(--_global-vars---accent-3)` in `:root` |
| **Variable Token (`--_global-vars---accent-4`)** | `#e9a2e4` | `var(--_global-vars---accent-4)` in `:root` |
| **Variable Token (`--_global-vars---grey`)** | `#b7b7b7` | `var(--_global-vars---grey)` in `:root` |
| **Variable Token (`--swiper-theme-color`)** | `#007aff` | `var(--swiper-theme-color)` in stylesheet |
| **Variable Token (`--swiper-preloader-color`)** | `#fff` | `var(--swiper-preloader-color)` in stylesheet |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_global-vars---light` | `#f4f4f4` | Canvas / Surface Token |
| `--_global-vars---dark` | `#040404` | Canvas / Surface Token |
| `--_global-vars---accent-1` | `#fbd050` | Brand / Palette Token |
| `--_global-vars---accent-2` | `#3a39ff` | Brand / Palette Token |
| `--_global-vars---accent-5` | `#ff5b23` | Brand / Palette Token |
| `--_global-vars---accent-3` | `#ade6ed` | Brand / Palette Token |
| `--_global-vars---accent-4` | `#e9a2e4` | Brand / Palette Token |
| `--_global-vars---grey` | `#b7b7b7` | Color / Atmospheric Token |
| `--underline-scale` | `1` | Design System Custom Token |
| `--pt-color` | `#fbd050` | Brand / Palette Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--swiper-preloader-color` | `#fff` | Brand / Palette Token |
| `--swiper-navigation-size` | `44px` | Layout / Spatial Grid Token |
| `--www-brandlos-nl-bg` | `#f4f4f4` | Canvas Substrate (from `var(--_global-vars---light)` in `:root`) |
| `--www-brandlos-nl-ink` | `#040404` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-brandlos-nl`)**:
   - Landmark `<header class="w-mod-js">` hosting `Brandlos · Het creatieve bureau van ` navigation (`Toestemming · Details · [#IABV2SETTINGS#] · Over · Details tonen`), DOM attributes (`data-wf-domain="www.brandlos.nl"`, `data-wf-page="6a60a2741f0d39e46e0880df"`, `data-wf-site="6a60a2731f0d39e46e0880dc"`, `data-nosnippet`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `Omdat gewoon te gewoontjes is`)**:
   - Landmark `<section class="home-hero">` presenting display lead `Omdat gewoon te gewoontjes is` and copy excerpt *"Toestemmingsselectie"* over `#f4f4f4` canvas and `#040404` ink.
3. **Primary Showcase & Content Grid (<section.home-showreel> — `Kijk mam, dit hebben wij gemaakt`)**:
   - Landmark `<section class="home-showreel">` rendering section `Kijk mam, dit hebben wij gemaakt` with copy *"Noodzakelijk 5 Noodzakelijke cookies helpen een website bruikbaar"*, asset references (`cdn.prod.website-files.com`, `brandlos-nl.webflow.shared.3ea0ad...`, `cc.js`, `configuration.js`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.home-about> — `Strategisch sterk, grafisch verdom`)**:
   - Landmark `<section class="home-about">` framing `Strategisch sterk, grafisch verdomd goed` and `Vrienden van Brandlos` (*"Cloudflare 1 Meer informatie over deze aanbieder cf.turnstile.u D"*) with `#fbd050` surface cards, `#3a39ff` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.CybotCookiebotDialogContentWrapper> — `https://www.brandlos.nl`)**:
   - Landmark `<footer class="CybotCookiebotDialogContentWrapper">` anchoring `Brandlos · Het creatieve bureau ` footer links (`Toestemming · Details · [#IABV2SETTINGS#] · Over · Details tonen`), copy *"Meer informatie over deze aanbieder"*, and `#ade6ed` structural dividers.
