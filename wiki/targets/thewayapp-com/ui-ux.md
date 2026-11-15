# UI & UX Architecture: thewayapp-com

## Overview & Design Identity
- **Target**: `thewayapp-com` (**The Way App - Meditation that lasts a lifetime — The Way**)
- **Production URL**: [https://thewayapp.com](https://thewayapp.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e8f2f0` / `#e6f2f0`)
- **Summary**: A long-term path of deep meditation training, guided by Zen Master Henry Shukman
- **Total Clean CSS Variables Extracted**: `228` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `nunito`
- **Body Font Stack**: `nunito Fallback`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80px`, `10px`, `12px`, `14px`, `18px`)
- **Section Heading (`H2`)**: CSS variables `--color-subtitle: var(--color-evergreen-default)`, `--color-card-subtitle: var(--color-obsidian-dark)`
- **Body Copy**: CSS variables `--color-body-text: var(--color-evergreen-default)`; rule `p` (`line-height: 1.2`)
- **Metadata & Labels**: CSS variables `--color-caption: var(--color-evergreen-default)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e8f2f0` | `var(--color-evergreen-light)` in `:root` |
| **Primary Typography Ink** | `#1c5349` | `var(--color-evergreen-default)` in `:root` |
| **Elevated Surface / Card Substrate** | `#122e28` | `var(--color-evergreen-dark)` in `:root` |
| **Interactive Accent / Highlight** | `#e6f2f0` | `var(--color-deepsea-light)` in `:root` |
| **Secondary / Muted Copy** | `#267768` | `var(--color-deepsea-default)` in `:root` |
| **Structural Hairline Border** | `#1a5249` | `var(--color-deepsea-dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--max-width-module-variation-content-wrapper` | `1320px!important` | Layout / Spatial Grid Token |
| `--width-module-variation-content-wrapper` | `91.6667vw!important` | Layout / Spatial Grid Token |
| `--font-sans` | `"nunito","nunito Fallback"` | Typography / Scale Token |
| `--_press-x` | `1` | Design System Custom Token |
| `--_press-y` | `0.3` | Design System Custom Token |
| `--_press-deg` | `0.5deg` | Design System Custom Token |
| `--media-width-cap` | `90vw` | Layout / Spatial Grid Token |
| `--media-height` | `min(calc(var(--media-width-cap) * 9 / 16),80vh)` | Layout / Spatial Grid Token |
| `--_card-radius` | `10px 8px 16px 17px/18px 17px 11px 15px` | Elevation / Border Token |
| `--logo-height-mobile` | `2.5rem` | Layout / Spatial Grid Token |
| `--blob-media-bleed` | `1.25` | Design System Custom Token |
| `--hero-height` | `clamp(480px,70vh,760px)` | Layout / Spatial Grid Token |
| `--hero-media-basis` | `min(var(--hero-height),50vw)` | Dimension / Scale Token |
| `--blob-corner-scale` | `1.2` | Design System Custom Token |
| `--parallax-y` | `0px` | Dimension / Scale Token |
| `--blob-shoulder` | `0.85` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.Header_header__gtmFw> — `thewayapp-com`)**:
   - Landmark `<header class="Header_header__gtmFw theme-light">` hosting `The Way App - Meditation that lasts ` navigation (`Skip to content`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.Default_embedWrapper__PB5mt { width:100% }`.
2. **Hero Stage & Focal Lead (<article.StaticNarrative_root__V_9OR> — `The end of your search. The start `)**:
   - Landmark `<article class="StaticNarrative_root__V_9OR">` presenting display lead `The end of your search. The start of your journey.` and copy excerpt *"The end of your search."* over `#e8f2f0` canvas and `#122e28` ink.
3. **Primary Showcase & Content Grid (<article.StaticNarrative_root__V_9OR> — `One way forward`)**:
   - Landmark `<article class="StaticNarrative_root__V_9OR">` rendering section `One way forward` with copy *"The start of your journey."*, asset references (`75aacf3429424351-s.p.woff2`, `df8e05a132a73a9c-s.p.woff2`, `95817d087ee99a00.css`, `6fc6cebf31cdec86.css`), and grid rule `.Default_embedWrapper__PB5mt iframe { width:100%!important;aspect-ratio:16/9;height:auto!important;display:block }`.
4. **Interactive Detail & Feature Matrix (<article.StaticNarrative_root__V_9OR> — `Meet your teacher: Henry Shukman`)**:
   - Landmark `<article class="StaticNarrative_root__V_9OR">` framing `Meet your teacher: Henry Shukman` and `A path that deepens with every step` (*"Most meditation apps give you countless options. The Way offers o"*) with `#122e28` surface cards, `#e6f2f0` accents, and `.Default_embedHeading__mSaeS { -webkit-margin-start:0;margin-inline-start:0;max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.type-ui-micro> — `https://thewayapp.com`)**:
   - Landmark `<footer class="type-ui-micro StaticNarrative_attribution__25nmb">` anchoring `The Way App - Meditation that la` footer links (`Skip to content`), copy *"I've finally been able to commit to daily meditation after y"*, and `#1a5249` structural dividers.
