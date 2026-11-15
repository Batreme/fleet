# UI & UX Architecture: kissbranding-co-uk

## Overview & Design Identity
- **Target**: `kissbranding-co-uk` (**Kiss · Brands that Kiss**)
- **Production URL**: [https://kissbranding.co.uk/](https://kissbranding.co.uk/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#f3eddf`)
- **Summary**: Brand strategy and identity for founder-led and investor-backed businesses at the moments that matter. Transform Award-winning studio in...
- **Total Clean CSS Variables Extracted**: `95` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `TT Commons Pro`
- **Body Font Stack**: `PP Migra`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-24)`, `var(--text-14)`)
- **Section Heading (`H2`)**: CSS variables `--tac-subtitle-font-family: "PP Migra",serif`, `--tac-subtitle-font-size: 3.2rem`, `--tac-subtitle-font-weight: var(--tac-font-weight)`; rule `h2` (`font-size: var(--text-24)`, `line-height: 120%`, `letter-spacing: 0`, `font-weight: var(--font-we...`)
- **Body Copy**: CSS variables `--font-body: "tt-commons-pro","TT Commons Pro",sans-serif`, `--font-body-condensed: "tt-commons-pro-condensed","TT Commons Pro Condensed",sans-serif`; rule `p` (`font-size: var(--text-14)`, `line-height: 140%`, `letter-spacing: 0`, `font-weight: var(--font-we...`)
- **Metadata & Labels**: CSS variables `--tac-letter-spacing: .04rem`, `--tac-btn-letter-spacing: var(--tac-letter-spacing)`, `--tac-close-btn-letter-spacing: var(--tac-letter-spacing)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#00f` | `var(--color-blue)` in `:root` |
| **Interactive Accent / Highlight** | `#f3eddf` | `var(--color-light)` in `:root` |
| **Secondary / Muted Copy** | `#e70000` | `var(--color-red)` in `:root` |
| **Structural Hairline Border** | `#0000` | `textarea { background-color: #0000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--spacing-container` | `var(--padding-container)` | Layout / Spatial Grid Token |
| `--spacing-grid` | `1rem` | Layout / Spatial Grid Token |
| `--spacing-0` | `0` | Layout / Spatial Grid Token |
| `--spacing` | `.1rem` | Layout / Spatial Grid Token |
| `--font-body` | `"tt-commons-pro","TT Commons Pro",sans-serif` | Typography / Scale Token |
| `--font-body-condensed` | `"tt-commons-pro-condensed","TT Commons Pro Condensed",sans-serif` | Typography / Scale Token |
| `--font-heading` | `"PP Migra",serif` | Typography Ink Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--font-weight-extrabold` | `800` | Typography / Scale Token |
| `--text-10` | `1rem` | Typography Ink Token |
| `--text-12` | `1.2rem` | Typography Ink Token |
| `--text-14` | `1.4rem` | Typography Ink Token |
| `--text-16` | `1.6rem` | Typography Ink Token |
| `--text-20` | `2rem` | Typography Ink Token |
| `--text-24` | `2.4rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `kissbranding-co-uk`)**:
   - Landmark `<header class="fixed w-full">` hosting `Kiss · Brands that Kiss` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-taxi-reload`, `data-frames-count="22"`, `data-frames-directory-uri="https://kissbranding...."`, `data-clone="true"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<div.mobile-wrapper> — `Kiss · Brands that Kiss`)**:
   - Landmark `<div class="mobile-wrapper bg-white">` presenting display lead `Kiss · Brands that Kiss` and copy excerpt *"46 The Calls, Leeds, LS2 7EY"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<div.mobile-wrapper> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="mobile-wrapper bg-white">` rendering section `Featured Work & Interactive Showcase` with copy *"Privacy and Cookie Policy"*, asset references (`tarteaucitron.min.js`, `apple-touch-icon-57x57.png`, `apple-touch-icon-60x60.png`, `apple-touch-icon-72x72.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<div.mobile-wrapper> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="mobile-wrapper bg-white">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Terms and Legal Notices"*) with `#00f` surface cards, `#f3eddf` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.yoast-schema-graph> — `https://kissbranding.co.uk/`)**:
   - Landmark `<footer class="yoast-schema-graph">` anchoring `Kiss · Brands that Kiss` footer links (`Overview · Index · Archive · About · Contact`), copy *"Website by Beaucoup"*, and `#0000` structural dividers.
