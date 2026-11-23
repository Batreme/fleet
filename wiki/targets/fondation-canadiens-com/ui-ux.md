---
title: "UI & UX Architecture: fondation-canadiens-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: fondation-canadiens-com

## Overview & Design Identity
- **Target**: `fondation-canadiens-com` (**Montreal Canadiens Children's Foundation - Play to thrive**)
- **Production URL**: [https://fondation.canadiens.com/](https://fondation.canadiens.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f4f4f4` / `#0000ff`)
- **Summary**: The Foundation encourages physical activity and the adoption of a healthy lifestyle among underprivileged youth from 4 to 17 years old.
- **Total Clean CSS Variables Extracted**: `190` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `bauhausvole`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 172.8px`, `line-height: 146.88px`, `font-weight: 600`, `letter-spacing: -5.184px`); CSS variables `--text-h1: calc(var(--font-size-h1)/var(--rem)*1rem)`, `--text-h1--line-height: .85`, `--text-h1--letter-spacing: -.03em`; rule `h1` (`font-size: var(--text-h1)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`, `font-weight: var(--font-we...`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 50px`, `line-height: 57.5px`, `font-weight: 600`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-h2: calc(var(--font-size-h2)/var(--rem)*1rem)`; rule `h2` (`font-size: var(--text-h4)`, `line-height: var(--tw-leading,var(...`, `font-weight: var(--font-we...`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 25.2px`, `font-weight: 500`); CSS variables `--text-body: 1rem`, `--text-body--line-height: 1.4`, `--font-size-body: 16`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 25.2px`, `font-weight: 500`); CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25/.875)`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f4f4` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#001a66` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.bg-white { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.prose-column .pill-btn:hover { background-color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#c3c3c3` | `.loader { border-color: #c3c3c3 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Poppins",sans-serif` | Typography / Scale Token |
| `--color-red-50` | `oklch(97.1% .013 17.38)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-800` | `oklch(44.4% .177 26.899)` | Brand / Palette Token |
| `--color-amber-500` | `oklch(76.9% .188 70.08)` | Brand / Palette Token |
| `--color-yellow-500` | `oklch(79.5% .184 86.047)` | Brand / Palette Token |
| `--color-green-500` | `oklch(72.3% .219 149.579)` | Brand / Palette Token |
| `--color-blue-500` | `oklch(62.3% .214 259.815)` | Brand / Palette Token |
| `--color-blue-600` | `oklch(54.6% .245 262.881)` | Brand / Palette Token |
| `--color-purple-500` | `oklch(62.7% .265 303.9)` | Brand / Palette Token |
| `--color-gray-50` | `oklch(98.5% .002 247.839)` | Brand / Palette Token |
| `--color-gray-100` | `oklch(96.7% .003 264.542)` | Brand / Palette Token |
| `--color-gray-200` | `oklch(92.8% .006 264.531)` | Brand / Palette Token |
| `--color-gray-300` | `oklch(87.2% .01 258.338)` | Brand / Palette Token |
| `--color-gray-400` | `oklch(70.7% .022 261.325)` | Brand / Palette Token |
| `--color-gray-600` | `oklch(44.6% .03 256.802)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.left-0> — `fondation-canadiens-com`)**:
   - Landmark `<header class="left-0 top-0">` (`1425x110px`) hosting `Montreal Canadiens Children's Founda` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sveltekit-preload-data="hover"`, `data-svg-origin="464 490"`, `data-svg-origin="857.5 300.5"`, `data-flip-id="auto-2"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<article.pt-margin> — `PLAY TO THRIVE`)**:
   - Landmark `<article class="pt-margin space-y-gutter">` presenting display lead `PLAY TO THRIVE` and copy excerpt *"For over 25 years, the Montreal Canadiens Children's Foundation h"* over `#f4f4f4` canvas and `#001a66` ink.
3. **Primary Showcase & Content Grid (<article.space-y-gutter> — `P l a y t o t h r i v e`)**:
   - Landmark `<article class="pt-margin space-y-gutter">` rendering section `P l a y t o t h r i v e` with copy *"Behind every rink and every program, there is a story of a child "*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `css2`, `favicon-96x96.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<article.bg-gray-light> — `News & Stories`)**:
   - Landmark `<article class="pt-margin space-y-gutter">` framing `News & Stories` and `A child discovering the fun of being active` (*"A child discovering the fun of being active"*) with `#ffffff` surface cards, `#0000ff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.px-margin> — `https://fondation.canadiens.com/`)**:
   - Landmark `<footer class="px-margin pb-30">` anchoring `Montreal Canadiens Children's Fo` footer links (`Overview · Index · Archive · About · Contact`), copy *"one skate stride at a time."*, and `#c3c3c3` structural dividers.
