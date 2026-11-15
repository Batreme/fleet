# UI & UX Architecture: www-xantium-com

## Overview & Design Identity
- **Target**: `www-xantium-com` (**Xantium**)
- **Production URL**: [https://www.xantium.com](https://www.xantium.com)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#221f25` ink, `#084432` accent)
- **Summary**: Xantium
- **Total Clean CSS Variables Extracted**: `43` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--font-body: system-ui,sans-serif`
- **Metadata & Labels**: CSS variables `--font-space-mono: "Space Mono","Space Mono Fallback"`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#221f25` | `var(--color-cache-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f5f5f2` | `var(--color-circuit-ivory)` in `:root` |
| **Interactive Accent / Highlight** | `#084432` | `var(--color-neural-moss)` in `:root` |
| **Secondary / Muted Copy** | `#00bf8b` | `var(--color-mint-engine)` in `:root` |
| **Structural Hairline Border** | `#c9ff8b` | `var(--color-data-beam)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-inter` | `"Inter","Inter Fallback"` | Typography / Scale Token |
| `--font-space-mono` | `"Space Mono","Space Mono Fallback"` | Typography / Scale Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-4xl` | `56rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1/.75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25/.875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5/1)` | Typography Ink Token |
| `--text-xl` | `1.25rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `www-xantium-com`)**:
   - Landmark `<header class="pointer-events-none absolute">` hosting `Xantium` navigation (`Home · How We Work · Our Culture · Our Team · Careers`), DOM attributes (`data-precedence="next"`, `data-nimg="fill"`, `data-nimg="fill"`, `data-nimg="fill"`), and stylesheet rule `nter_fe8b9d92-module__LINzvG__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.py-16> — `We build technology enhanced by hu`)**:
   - Landmark `<section class="py-16 relative">` presenting display lead `We build technology enhanced by human insight to...` and copy excerpt *"At Xantium, quantitative researchers, developers, fundamental ana"* over `#fff` canvas and `#221f25` ink.
3. **Primary Showcase & Content Grid (<section.py-16> — `What We Do`)**:
   - Landmark `<section class="py-16 relative">` rendering section `What We Do` with copy *"We are a global multi-strategy investment firm integrating quanti"*, asset references (`28e60ca39c9ae554-s.p.7a4e9fcc.woff2`, `83afe278b6a6bb3c-s.p.3a6ba036.woff2`, `8d05cfa5faa8406c-s.p.4adea45d.woff2`, `d7a0600e467cf0bd-s.p.20ecb425.woff2`), and grid rule `inter_fe8b9d92-module__LINzvG__va... { --font-inter:"Inter","Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.py-16> — `At a Glance`)**:
   - Landmark `<section class="py-16 relative">` framing `At a Glance` and `Founded in 2019 as part of Tudor Group` (*"If you're drawn to complex problems and collaborative discovery, "*) with `#f5f5f2` surface cards, `#084432` accents, and `mono_e13c1f09-module__VyLqqa__cla... { font-family:Space Mono,Space Mono Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.xantium.com`)**:
   - Landmark `<footer class="relative z-10">` anchoring `Xantium` footer links (`Home · How We Work · Our Culture · Our Team · Careers`), copy *"Global presence, market breadth, scale"*, and `#c9ff8b` structural dividers.
