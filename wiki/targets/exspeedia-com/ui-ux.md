---
title: "UI & UX Architecture: exspeedia-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: exspeedia-com

## Overview & Design Identity
- **Target**: `exspeedia-com` (**Official IShowSpeed Travel Site Powered by Expedia**)
- **Production URL**: [https://exspeedia.com](https://exspeedia.com)
- **Final Redirected URL**: [https://speed.expedia.com/](https://speed.expedia.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#030c1d` / `#005aeb`)
- **Summary**: The official IShowSpeed travel website powered by Expedia. Book trips inspired by Speed’s real travels, enter sweepstakes, and earn rewards.
- **Total Clean CSS Variables Extracted**: `398` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Centra No2`
- **Body Font Stack**: `Centra No2`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 14.4px`, `font-weight: 800`, `letter-spacing: -3.52px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: 1.5rem`, `line-height: 1.2`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.5rem`, `line-height: 1.25`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: .75em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 13.008px`, `line-height: 19.512px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#030c1d` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `8 { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#005aeb` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#575b6e` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#808080` | `.border-gray-200 { border-color: #808080 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-serif` | `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif` | Typography / Scale Token |
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

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.grid> — `exspeedia-com`)**:
   - Landmark `<header class="grid">` (`1440px`) hosting `Official IShowSpeed Travel Site Powe` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-navigate-track="reload"`, `data-document-language="true"`, `data-domain-script="019d9c05-c22b-757a-b8..."`, `data-v-app`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.ot-sdk-row> — `GO PLACES LIKE`)**:
   - Landmark `<section class="ot-sdk-row ot-cat-grp">` presenting display lead `GO PLACES LIKE` and copy excerpt *"checkbox label label"* over `#030c1d` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.ot-hide> — `checkbox label label`)**:
   - Landmark `<section class="ot-hide ot-pc-scrollbar">` rendering section `checkbox label label` with copy *"GO PLACES LIKE"*, asset references (`speed-cdn.expedia.com`, `d2848tzd1fqvrv.cloudfront.net`, `cdn.usefathom.com`, `favicon-96x96.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.fixed> — `exspeedia-com Interactive Matrix`)**:
   - Landmark `<section class="fixed">` framing `exspeedia-com Interactive Matrix` and `exspeedia-com Archive & Directory` (*"checkbox label label"*) with `#000000` surface cards, `#005aeb` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.inset-0> — `https://exspeedia.com`)**:
   - Landmark `<footer class="inset-0">` anchoring `Official IShowSpeed Travel Site ` footer links (`Overview · Index · Archive · About · Contact`), copy *"exspeedia-com Interactive Matrix"*, and `#808080` structural dividers.
