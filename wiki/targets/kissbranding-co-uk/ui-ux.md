---
title: "UI & UX Architecture: kissbranding-co-uk"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: kissbranding-co-uk

## Overview & Design Identity
- **Target**: `kissbranding-co-uk` (**Kiss · Brands that Kiss**)
- **Production URL**: [https://kissbranding.co.uk/](https://kissbranding.co.uk/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#008300`)
- **Summary**: Brand strategy and identity for founder-led and investor-backed businesses at the moments that matter. Transform Award-winning studio in...
- **Total Clean CSS Variables Extracted**: `95` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Apple Color Emoji`
- **Body Font Stack**: `Apple Color Emoji`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: observed font-size ladder: `10px`, `72px`, `14px`, `1em`, `80%`
- **Section Heading (`H2`)**: CSS variables `--tac-subtitle-font-family: "PP Migra",serif`, `--tac-subtitle-font-size: 3.2rem`, `--tac-subtitle-font-weight: var(--tac-font-weight)`; rule `h2` (`font-size: var(--text-24)`, `line-height: 120%`, `letter-spacing: 0`, `font-weight: var(--font-we...`)
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-body: "tt-commons-pro","TT Commons Pro",sans-serif`, `--font-body-condensed: "tt-commons-pro-condensed","TT Commons Pro Condensed",sans-serif`; rule `p` (`font-size: var(--text-14)`, `line-height: 140%`, `letter-spacing: 0`, `font-weight: var(--font-we...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 72px`, `line-height: 72px`, `font-weight: 400`, `letter-spacing: -1px`); CSS variables `--tac-letter-spacing: .04rem`, `--tac-btn-letter-spacing: var(--tac-letter-spacing)`, `--tac-close-btn-letter-spacing: var(--tac-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ff0000` | `.bg-red { background-color: red }` (`#ff0000`) |
| **Interactive Accent / Highlight** | `#008300` | `.tarteaucitronCTAButton { background: #008300 }` |
| **Secondary / Muted Copy** | `#333333` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#333333` | `#tarteaucitron .tarteaucitronBo... { border: #333333 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--size` | `375` | Layout / Spatial Grid Token |
| `--padding-container` | `2rem` | Layout / Spatial Grid Token |
| `--vw` | `100vw` | Layout / Spatial Grid Token |
| `--vh` | `calc(var(--vh-initial,1vh)*100)` | Layout / Spatial Grid Token |
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

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `kissbranding-co-uk`)**:
   - Landmark `<header class="pointer-events-none fixed">` (`1440x131px`) hosting `Kiss · Brands that Kiss` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-taxi-reload`, `data-frames-count="22"`, `data-frames-directory-uri="https://kissbranding...."`, `data-clone="true"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<div.mobile-wrapper> — `Kiss · Brands that Kiss`)**:
   - Landmark `<div class="mobile-wrapper bg-white">` presenting display lead `Kiss · Brands that Kiss` and copy excerpt *"Cookie preferences"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<div.bg-white> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="mobile-wrapper bg-white">` rendering section `Featured Work & Interactive Showcase` with copy *"Preference for all services"*, asset references (`tarteaucitron.min.js`, `apple-touch-icon-57x57.png`, `apple-touch-icon-60x60.png`, `apple-touch-icon-72x72.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<div.mobile-wrapper:nth(2)> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="mobile-wrapper bg-white">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Mandatory cookies This site uses cookies necessary for its proper"*) with `#ff0000` surface cards, `#008300` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.yoast-schema-graph> — `https://kissbranding.co.uk/`)**:
   - Landmark `<footer class="yoast-schema-graph">` anchoring `Kiss · Brands that Kiss` footer links (`Overview · Index · Archive · About · Contact`), copy *"This site uses cookies necessary for its proper functioning "*, and `#333333` structural dividers.
