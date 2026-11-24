---
title: "UI & UX Architecture: ross-oneill-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: ross-oneill-com

## Overview & Design Identity
- **Target**: `ross-oneill-com` (**Ross O'Neill · Freelance Web Developer and Designer in Perth**)
- **Production URL**: [https://ross-oneill.com/](https://ross-oneill.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4140px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#da0a2c` accent)
- **Summary**: Freelance web developer and designer in North Beach, Perth. Fast custom websites for WA businesses, built and looked after by the person...
- **Total Clean CSS Variables Extracted**: `360` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `DM Sans`
- **Body Font Stack**: `DM Sans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 60px`, `font-weight: 500`, `letter-spacing: -1.92px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `section` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `.bg-yellow-100 { background-color: yellow }` (`#ffff00`) |
| **Interactive Accent / Highlight** | `#da0a2c` | `var(--color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#808080` | `.text-gray-400 { color: gray }` (`#808080`) |
| **Structural Hairline Border** | `#f2f2f2` | `5 { border-color: #f2f2f2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-red-50` | `oklch(97.1% .013 17.38)` | Brand / Palette Token |
| `--color-red-100` | `oklch(93.6% .032 17.717)` | Brand / Palette Token |
| `--color-red-200` | `oklch(88.5% .062 18.334)` | Brand / Palette Token |
| `--color-red-300` | `oklch(80.8% .114 19.571)` | Brand / Palette Token |
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-600` | `oklch(57.7% .245 27.325)` | Brand / Palette Token |
| `--color-red-700` | `oklch(50.5% .213 27.518)` | Brand / Palette Token |
| `--color-red-800` | `oklch(44.4% .177 26.899)` | Brand / Palette Token |
| `--color-red-900` | `oklch(39.6% .141 25.723)` | Brand / Palette Token |
| `--color-red-950` | `oklch(25.8% .092 26.042)` | Brand / Palette Token |
| `--color-orange-50` | `oklch(98% .016 73.684)` | Brand / Palette Token |
| `--color-orange-100` | `oklch(95.4% .038 75.164)` | Brand / Palette Token |
| `--color-orange-200` | `oklch(90.1% .076 70.697)` | Brand / Palette Token |
| `--color-orange-300` | `oklch(83.7% .128 66.29)` | Brand / Palette Token |
| `--color-orange-400` | `oklch(75% .183 55.934)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header-content> — `ross-oneill-com`)**:
   - Landmark `<header class="header-content top-0">` (`1440x104px`) hosting `Ross O'Neill · Freelance Web Develop` navigation (`About Me · Plans · Work · Blog · Get in Touch`), DOM attributes (`data-astro-exec`, `data-cfasync="false"`, `data-icon="carbon:arrow-right"`, `data-icon="carbon:arrow-right"`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
2. **Hero Stage & Focal Lead (<section.py-28> — `Ross O'Neill, a Perth-based web de`)**:
   - Landmark `<section class="py-28 bg-white">` presenting display lead `Ross O'Neill, a Perth-based web developer who tra...` and copy excerpt *"Custom websites built from scratch. Clean code, lightning-fast pe"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.pb-12> — `Margaret River Region`)**:
   - Landmark `<section class="pb-12 bg-white">` rendering section `Margaret River Region` with copy *"Ross O'Neill, a Perth-based web developer who transforms designs "*, asset references (`favicon.ico`, `favicon.svg`, `sitemap-index.xml`, `static.cloudflareinsights.com`), and grid rule `host { z-index:1;margin-left:auto;margin-right:auto;display:block;position:rela... }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Capes Foundation`)**:
   - Landmark `<section class="relative py-12">` framing `Capes Foundation` and `Westmec Services` (*"Swipe to See Full Portfolio"*) with `#ffff00` surface cards, `#da0a2c` accents, and `.swiper { z-index:1;margin-left:auto;margin-right:auto;padding:0;list-style:none;d... }`.
5. **Colophon & Global Directory Footer (<footer.rounded-2xl> — `https://ross-oneill.com/`)**:
   - Landmark `<footer class="rounded-2xl m-4">` anchoring `Ross O'Neill · Freelance Web Dev` footer links (`About Me · Plans · Work · Blog · Get in Touch`), copy *"Monthly maintenance to keep your site secure, fast, and up-t"*, and `#f2f2f2` structural dividers.
