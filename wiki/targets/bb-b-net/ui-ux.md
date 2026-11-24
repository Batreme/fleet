---
title: "UI & UX Architecture: bb-b-net"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: bb-b-net

## Overview & Design Identity
- **Target**: `bb-b-net` (**Agence de Communication b2b et Marketing Industriel- bb&b**)
- **Production URL**: [https://bb-b.net](https://bb-b.net)
- **Final Redirected URL**: [https://www.bb-b.net/](https://www.bb-b.net/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#fa4500` accent)
- **Summary**: bb&b agence conseil en marketing industriel et communication B2B, basée à Paris. Contactez-nous pour tous vos projets !
- **Total Clean CSS Variables Extracted**: `70` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Söhne Kraftig`
- **Body Font Stack**: `Söhne`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`, `letter-spacing: 0.4px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-6xl: 3.75rem`
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 40px`, `line-height: 50px`, `font-weight: 400`); CSS variables `--text-3xl: 1.875rem`, `--text-3xl--line-height: calc(2.25 / 1.875)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `main` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f0efeb` | `.bg-gray-light { background-color: #f0efeb }` |
| **Interactive Accent / Highlight** | `#fa4500` | `var(--bbb-link-color-hover)` in `:root` |
| **Secondary / Muted Copy** | `#808080` | `.text-gray-400 { color: gray }` (`#808080`) |
| **Structural Hairline Border** | `#f0efeb` | `.border-border-light { border-color: #f0efeb }` |
| **Variable Token (`--bbb-link-color-active`)** | `#8b0000` | `var(--bbb-link-color-active)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bbb-list-bullet` | `url(/bbb-list-bullet.svg)` | Design System Custom Token |
| `--bbb-link-color` | `#000` | Typography Ink Token |
| `--bbb-link-color-hover` | `#fa4500` | Typography Ink Token |
| `--bbb-link-color-active` | `#8b0000` | Typography Ink Token |
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-orange-400` | `oklch(75% .183 55.934)` | Brand / Palette Token |
| `--color-orange-500` | `oklch(70.5% .213 47.604)` | Brand / Palette Token |
| `--color-green-400` | `oklch(79.2% .209 151.711)` | Brand / Palette Token |
| `--color-green-600` | `oklch(62.7% .194 149.214)` | Brand / Palette Token |
| `--color-gray-300` | `oklch(87.2% .01 258.338)` | Brand / Palette Token |
| `--color-gray-400` | `oklch(70.7% .022 261.325)` | Brand / Palette Token |
| `--color-gray-500` | `oklch(55.1% .027 264.364)` | Brand / Palette Token |
| `--color-gray-600` | `oklch(44.6% .03 256.802)` | Brand / Palette Token |
| `--color-gray-700` | `oklch(37.3% .034 259.733)` | Brand / Palette Token |
| `--color-neutral-100` | `oklch(97% 0 0)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.inset-x-0> — `bb-b-net`)**:
   - Landmark `<nav class="inset-x-0 top-0">` (`1440x64px`) hosting `Agence de Communication b2b et Marke` navigation (`Accueil · Agence · Compétences · Références · Blog`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/css/653..."`, `data-ueto="ueto_d354e50f6e"`, `data-cky-tag="revisit-consent"`), and stylesheet rule `font-face { font-family: 'Söhne Kraftig'; src: url('/fonts/soehne-kraftig.woff2') fo... }`.
2. **Hero Stage & Focal Lead (<section.relative> — `MARKETING ET COMMUNICATION POUR LE`)**:
   - Landmark `<section class="relative flex">` presenting display lead `MARKETING ET COMMUNICATION POUR LE MONDE INDUSTRI...` and copy excerpt *"bb&b est une agence conseil en marketing et communication B2B, sp"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.w-full> — `Marketing et communication pour le`)**:
   - Landmark `<section class="relative w-full">` rendering section `Marketing et communication pour le monde industri...` with copy *"faire rayonner les entreprises industrielles et technologiques en"*, asset references (`webpack-4e4475af75d05841.js`, `813956296145205`, `fbevents.js`, `lftracker_v1_YEgkB8lB6dx4ep3Z.js`), and grid rule `.Toastify__toast-container--top-left { top:var(--toastify-toast-top);left:var(--toastify-toast-left) }`.
4. **Interactive Detail & Feature Matrix (<section.pt-6> — `Industries, technologies et b2b`)**:
   - Landmark `<section class="pt-6 bg-white">` framing `Industries, technologies et b2b` and `Une agence singulière` (*"la compréhension des enjeux techniques, la solide expérience des "*) with `#f0efeb` surface cards, `#fa4500` accents, and `.Toastify__toast-container--top-c... { top:var(--toastify-toast-top);left:50%;transform:translate(-50%);align-i... }`.
5. **Colophon & Global Directory Footer (<footer.w-full> — `https://bb-b.net`)**:
   - Landmark `<footer class="w-full flex">` anchoring `Agence de Communication b2b et M` footer links (`Accueil · Agence · Compétences · Références · Blog`), copy *"structurer, créer, déployer."*, and `#f0efeb` structural dividers.
