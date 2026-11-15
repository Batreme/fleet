# UI & UX Architecture: exspeedia-com

## Overview & Design Identity
- **Target**: `exspeedia-com` (**Official IShowSpeed Travel Site Powered by Expedia**)
- **Production URL**: [https://exspeedia.com](https://exspeedia.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fbf8e6` / `#fae26a`)
- **Summary**: The official IShowSpeed travel website powered by Expedia. Book trips inspired by Speed’s real travels, enter sweepstakes, and earn rewards.
- **Total Clean CSS Variables Extracted**: `398` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Centra No2`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: 1.5rem`, `line-height: 1.2`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.5rem`, `line-height: 1.25`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: .75em`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fbf8e6` | `var(--color-yellow-50)` in `:root` |
| **Primary Typography Ink** | `#f9f2cf` | `var(--color-yellow-100)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f8e99e` | `var(--color-yellow-200)` in `:root` |
| **Interactive Accent / Highlight** | `#fae26a` | `var(--color-yellow-300)` in `:root` |
| **Secondary / Muted Copy** | `#fddb32` | `var(--color-yellow-400)` in `:root` |
| **Structural Hairline Border** | `#ffd60a` | `var(--color-yellow-500)` in `:root` |

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
   - Landmark `<header class="grid">` hosting `Official IShowSpeed Travel Site Powe` navigation (`More information`), DOM attributes (`data-navigate-track="reload"`, `data-document-language="true"`, `data-domain-script="019d9c05-c22b-757a-b8..."`, `data-v-app`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.ot-sdk-row> — `Go places like`)**:
   - Landmark `<section class="ot-sdk-row ot-cat-grp">` presenting display lead `Go places like` and copy excerpt *"Accept All Cookies"* over `#fbf8e6` canvas and `#ffd60a` ink.
3. **Primary Showcase & Content Grid (<section.ot-hide> — `Privacy Preference Center`)**:
   - Landmark `<section class="ot-hide ot-pc-scrollbar">` rendering section `Privacy Preference Center` with copy *"checkbox label label"*, asset references (`speed-cdn.expedia.com`, `d2848tzd1fqvrv.cloudfront.net`, `cdn.usefathom.com`, `favicon-96x96.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.fixed> — `Manage Consent Preferences`)**:
   - Landmark `<section class="fixed">` framing `Manage Consent Preferences` and `Cookie List` (*"Confirm My Choices"*) with `#f8e99e` surface cards, `#fae26a` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.inset-0> — `https://exspeedia.com`)**:
   - Landmark `<footer class="inset-0">` anchoring `Official IShowSpeed Travel Site ` footer links (`More information`), copy *"Manage Consent Preferences"*, and `#ffd60a` structural dividers.
