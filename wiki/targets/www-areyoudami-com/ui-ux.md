# UI & UX Architecture: www-areyoudami-com

## Overview & Design Identity
- **Target**: `www-areyoudami-com` (**AreyouDami. — Damilare Olawoyin, Creative Director**)
- **Production URL**: [https://www.areyoudami.com](https://www.areyoudami.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#111`)
- **Summary**: Damilare Olawoyin (AreyouDami.) — creative director & editor based in Lagos. Bringing stories that push emotions. Edit. Color. VFX.
- **Total Clean CSS Variables Extracted**: `52` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-6xl: clamp(2.25rem, 1.63rem + 2.65vw, 3.75rem)`, `--text-6xl--line-height: 1.05`, `--font-display: var(--font-work-sans), "Arial", system-ui, sans-serif`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: clamp(1.1875rem, 1.06rem + .55vw, 1.5rem)`, `--text-2xl--line-height: 1.25`
- **Body Copy**: CSS variables `--text-base: clamp(.875rem, .82rem + .22vw, 1rem)`, `--text-base--line-height: 1.55`
- **Metadata & Labels**: CSS variables `--text-xs: clamp(.6875rem, .66rem + .11vw, .75rem)`, `--text-xs--line-height: 1.45`, `--text-sm: clamp(.75rem, .7rem + .22vw, .875rem)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fc0` | `var(--color-primary)` in `:root` |
| **Interactive Accent / Highlight** | `#111` | `var(--color-ink)` in `:root` |
| **Secondary / Muted Copy** | `#8e8e93` | `var(--color-subtext)` in `:root` |
| **Structural Hairline Border** | `#0000` | `textarea { background-color: #0000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-inter` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-work-sans` | `"Work Sans", "Work Sans Fallback"` | Typography / Scale Token |
| `--iris` | `0%` | Dimension / Scale Token |
| `--font-sans` | `var(--font-inter), ui-sans-serif, system-ui, sans-serif` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--text-xs` | `clamp(.6875rem, .66rem + .11vw, .75rem)` | Typography Ink Token |
| `--text-xs--line-height` | `1.45` | Typography Ink Token |
| `--text-sm` | `clamp(.75rem, .7rem + .22vw, .875rem)` | Typography Ink Token |
| `--text-sm--line-height` | `1.5` | Typography Ink Token |
| `--text-base` | `clamp(.875rem, .82rem + .22vw, 1rem)` | Typography Ink Token |
| `--text-base--line-height` | `1.55` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `www-areyoudami-com`)**:
   - Landmark `<header class="fixed top-5">` hosting `AreyouDami. — Damilare Olawoyin, Cre` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-snap="true"`, `data-snap="true"`, `data-tag="true"`), and stylesheet rule `nter_7b064e0d-module__MOT0tq__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.relative> — `AreyouDami.`)**:
   - Landmark `<section class="relative isolate">` presenting display lead `AreyouDami.` and copy excerpt *"AreyouDami. AreyouDami. AreyouDami. AreyouDami. AreyouDami. Areyo"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `American Cola`)**:
   - Landmark `<section class="relative bg-ink">` rendering section `American Cola` with copy *"Digital Commercial"*, asset references (`7ddd198311ba7843-s.p.3kq6k02b2ysv...`, `83afe278b6a6bb3c-s.p.2bn3s6zvc0dy...`, `hero-poster.jpg`, `cssda-special-kudos-white.svg`), and grid rule `inter_7b064e0d-module__MOT0tq__va... { --font-inter:"Inter", "Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<article.relative> — `Trace Sessions With FOLA`)**:
   - Landmark `<article class="relative w-full">` framing `Trace Sessions With FOLA` and `Victoria Orenze - Father We Are Grateful` (*"00:00:01 / 00:00:05"*) with `#fc0` surface cards, `#111` accents, and `sans_2c8a97c2-module__lkoJJW__cla... { font-family:Work Sans,Work Sans Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.areyoudami.com`)**:
   - Landmark `<footer class="relative overflow-hidden">` anchoring `AreyouDami. — Damilare Olawoyin,` footer links (`Overview · Index · Archive · About · Contact`), copy *"Trace Sessions With FOLA"*, and `#0000` structural dividers.
