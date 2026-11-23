---
title: "UI & UX Architecture: www-areyoudami-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-areyoudami-com

## Overview & Design Identity
- **Target**: `www-areyoudami-com` (**AreyouDami. — Damilare Olawoyin, Creative Director**)
- **Production URL**: [https://www.areyoudami.com](https://www.areyoudami.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#111111` / `#ffcc00`)
- **Summary**: Damilare Olawoyin (AreyouDami.) — creative director & editor based in Lagos. Bringing stories that push emotions. Edit. Color. VFX.
- **Total Clean CSS Variables Extracted**: `52` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-6xl: clamp(2.25rem, 1.63rem + 2.65vw, 3.75rem)`, `--text-6xl--line-height: 1.05`, `--font-display: var(--font-work-sans), "Arial", system-ui, sans-serif`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 62.4px`, `font-weight: 800`, `letter-spacing: -1px`); CSS variables `--text-2xl: clamp(1.1875rem, 1.06rem + .55vw, 1.5rem)`, `--text-2xl--line-height: 1.25`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: clamp(.875rem, .82rem + .22vw, 1rem)`, `--text-base--line-height: 1.55`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: clamp(.6875rem, .66rem + .11vw, .75rem)`, `--text-xs--line-height: 1.45`, `--text-sm: clamp(.75rem, .7rem + .22vw, .875rem)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#111111` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.bg-black { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#ffcc00` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#8e8e93` | `var(--color-subtext)` in `:root` |
| **Structural Hairline Border** | `#705c0a` | `40 { border-color: #705c0a }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--lightningcss-dark` | `initial` | Canvas / Surface Token |
| `--grain-density` | `1` | Design System Custom Token |
| `--grain-size` | `.5` | Layout / Spatial Grid Token |
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

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-5> — `www-areyoudami-com`)**:
   - Landmark `<header class="top-5 fixed">` (`290x56px`) hosting `AreyouDami. — Damilare Olawoyin, Cre` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-snap="true"`, `data-snap="true"`, `data-tag="true"`), and stylesheet rule `nter_7b064e0d-module__MOT0tq__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.bg-ink> — `AreyouDami.`)**:
   - Landmark `<section class="bg-ink relative">` presenting display lead `AreyouDami.` and copy excerpt *"AreyouDami. AreyouDami. AreyouDami. AreyouDami. AreyouDami. Areyo"* over `#111111` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.text-paper> — `American Cola`)**:
   - Landmark `<section class="bg-ink text-paper">` rendering section `American Cola` with copy *"Digital Commercial"*, asset references (`7ddd198311ba7843-s.p.3kq6k02b2ysv...`, `83afe278b6a6bb3c-s.p.2bn3s6zvc0dy...`, `hero-poster.jpg`, `cssda-special-kudos-white.svg`), and grid rule `inter_7b064e0d-module__MOT0tq__va... { --font-inter:"Inter", "Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<article.relative> — `Trace Sessions With FOLA`)**:
   - Landmark `<article class="relative w-full">` framing `Trace Sessions With FOLA` and `Victoria Orenze - Father We Are Grateful` (*"00:00:01 / 00:00:05"*) with `#000000` surface cards, `#ffcc00` accents, and `sans_2c8a97c2-module__lkoJJW__cla... { font-family:Work Sans,Work Sans Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.bg-ink> — `https://www.areyoudami.com`)**:
   - Landmark `<footer class="bg-ink relative">` anchoring `AreyouDami. — Damilare Olawoyin,` footer links (`Overview · Index · Archive · About · Contact`), copy *"Trace Sessions With FOLA"*, and `#705c0a` structural dividers.
