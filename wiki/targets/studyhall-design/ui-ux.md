# UI & UX Architecture: studyhall-design

## Overview & Design Identity
- **Target**: `studyhall-design` (**Home · Study Hall ✶ Built to move you.**)
- **Production URL**: [https://studyhall.design/](https://studyhall.design/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#ededed`)
- **Summary**: A creative agency based in Oakland and partnering globally. We craft brand, motion, and interactive to help businesses resonate now and r...
- **Total Clean CSS Variables Extracted**: `213` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Montreal`
- **Body Font Stack**: `Kommuna`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-caption-serif-size)`, `.7em`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-caption-serif-size)`, `.7em`)
- **Body Copy**: CSS variables `--type-body-lg-mobile: 20`, `--type-body-lg-tablet: 20`, `--type-body-lg-desktop: 24`
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--type-small-mobile: 16`, `--type-small-tablet: 16`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fdffb6` | `var(--color-yellow)` in `:root` |
| **Interactive Accent / Highlight** | `#ededed` | `var(--color-gray)` in `:root` |
| **Secondary / Muted Copy** | `#cdcdcd` | `var(--color-form-bg)` in `:root` |
| **Structural Hairline Border** | `#b7b7b7` | `var(--color-gray-hover)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Neue Montreal", ui-sans-serif, system-ui, sans-serif` | Typography / Scale Token |
| `--font-serif` | `"PS Times", ui-serif, Georgia, "Times New Roman", serif` | Typography / Scale Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-700` | `oklch(50.5% .213 27.518)` | Brand / Palette Token |
| `--color-blue-500` | `oklch(62.3% .214 259.815)` | Brand / Palette Token |
| `--color-gray-200` | `oklch(92.8% .006 264.531)` | Brand / Palette Token |
| `--color-gray-800` | `oklch(27.8% .033 256.848)` | Brand / Palette Token |
| `--color-neutral-800` | `oklch(26.9% 0 none)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `calc(1 / var(--type-root-max-value) * 1rem)` | Layout / Spatial Grid Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--tracking-tighter` | `-.05em` | Typography / Scale Token |
| `--leading-normal` | `1.5` | Typography / Scale Token |
| `--radius-sm` | `.25rem` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.flex> — `studyhall-design`)**:
   - Landmark `<nav class="flex flex-col">` hosting `Home · Study Hall ✶ Built to move yo` navigation (`About · Work with us`), DOM attributes (`data-module="nav-footer-hide"`, `data-module="nav-drawer-hover"`, `data-module="nav-drawer"`, `data-media-hover-trigger`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.pb-gy> — `We're in the business of making th`)**:
   - Landmark `<section class="pb-gy">` presenting display lead `We're in the business of making things move. Bran...` and copy excerpt *"W o r k w i t h u s Work with us"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.py-gy> — `San Francisco Running Company Bran`)**:
   - Landmark `<section class="py-gy px-gx">` rendering section `San Francisco Running Company Brand Identity` with copy *"W o r k w i t h u s"*, asset references (`594ac8afc003a31c157eba4bb9a25ab65...`, `cdn.sanity.io`, `stream.mux.com`, `7198ba5e4c2149645a79f387b2a12f5ce...`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.py-gy> — `Recent Work`)**:
   - Landmark `<section class="py-gy flex">` framing `Recent Work` and `Awards & Publications` (*"San Francisco Running Company Brand Identity Motion Brand Identit"*) with `#fdffb6` surface cards, `#ededed` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.mb-18> — `https://studyhall.design/`)**:
   - Landmark `<footer class="mb-18 pt-24">` anchoring `Home · Study Hall ✶ Built to mov` footer links (`About · Work with us`), copy *"San Francisco Running Company"*, and `#b7b7b7` structural dividers.
