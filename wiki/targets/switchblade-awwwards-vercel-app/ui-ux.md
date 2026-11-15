# UI & UX Architecture: switchblade-awwwards-vercel-app

## Overview & Design Identity
- **Target**: `switchblade-awwwards-vercel-app` (**SWITCHBLADE™**)
- **Production URL**: [https://switchblade-awwwards.vercel.app/](https://switchblade-awwwards.vercel.app/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#fb2c36` / `#f2ede4`)
- **Summary**: SWITCHBLADE™: a philosophy applied to whatever it touches. Strength, compassion, and intent, distilled into a mark for builders who refus...
- **Total Clean CSS Variables Extracted**: `58` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Averia Serif Libre`
- **Body Font Stack**: `Averia Serif Libre Fallback`
- **Monospace / Technical Font Stack**: `IBM Plex Sans`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-base)`, `var(--text-sm)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-base)`, `var(--text-sm)`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: CSS variables `--font-ibm-mono: "IBM Plex Mono", "IBM Plex Mono Fallback"`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--color-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Interactive Accent / Highlight** | `#f2ede4` | `var(--cream)` in `:root` |
| **Secondary / Muted Copy** | `#eae4da` | `var(--cream-2)` in `:root` |
| **Structural Hairline Border** | `#0d0d0d` | `var(--ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-averia` | `"Averia Serif Libre", "Averia Serif Libre Fallback"` | Typography / Scale Token |
| `--font-barlow` | `"barlow", "barlow Fallback"` | Typography / Scale Token |
| `--font-ibm` | `"IBM Plex Sans", "IBM Plex Sans Fallback"` | Typography / Scale Token |
| `--font-ibm-mono` | `"IBM Plex Mono", "IBM Plex Mono Fallback"` | Typography / Scale Token |
| `--font-inter` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-archivo` | `"Archivo", "Archivo Fallback"` | Typography / Scale Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `switchblade-awwwards-vercel-app`)**:
   - Landmark `<header class="lenis">` hosting `SWITCHBLADE™` navigation (`Home · Classics · Collaborate · Instagram · Collaboration`), DOM attributes (`data-scroll-behavior="smooth"`, `data-precedence="next"`, `data-engine="three.js r169"`, `data-sweep="true"`), and stylesheet rule `ibre_63ecb988-module__K5xa_q__cla... { font-family:Averia Serif Libre,Averia Serif Libre Fallback }`.
2. **Hero Stage & Focal Lead (<section.relative> — `The Rare And The Remaining`)**:
   - Landmark `<section class="relative h-screen">` presenting display lead `The Rare And The Remaining` and copy excerpt *"The Rare And The Remaining"* over `#fb2c36` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.site-px> — `The O rigins`)**:
   - Landmark `<section class="site-px">` rendering section `The O rigins` with copy *"An independent world where original pieces meet exceptional ideas"*, asset references (`03fc1b4a8d284b5e-s.p.0wiir8udbzjv...`, `063c621f808926da-s.p.0owiw8pss6ip...`, `1b9db6b14d5f23d9-s.p.287p25qttz2h...`, `1e7b70e7d87e0cff-s.p.3c8rqma_d2be...`), and grid rule `libre_63ecb988-module__K5xa_q__va... { --font-averia:"Averia Serif Libre", "Averia Serif Libre Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.site-px> — `The Brand Journey`)**:
   - Landmark `<section class="site-px">` framing `The Brand Journey` and `One Standard. Every Part Of Life.` (*"S W I T C H B L A D E"*) with `#fff` surface cards, `#f2ede4` accents, and `rlow_8b927dcc-module__7A2ffW__cla... { font-family:barlow,barlow Fallback }`.
5. **Colophon & Global Directory Footer (<footer.site-px> — `https://switchblade-awwwards.vercel.app/`)**:
   - Landmark `<footer class="site-px">` anchoring `SWITCHBLADE™` footer links (`Home · Classics · Collaborate · Instagram · Collaboration`), copy *"C o n v i c t i o n"*, and `#0d0d0d` structural dividers.
