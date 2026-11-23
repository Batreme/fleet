---
title: "UI & UX Architecture: carnilove-ashfall-studio"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: carnilove-ashfall-studio

## Overview & Design Identity
- **Target**: `carnilove-ashfall-studio` (**Carnilove · Home**)
- **Production URL**: [https://carnilove.ashfall.studio/](https://carnilove.ashfall.studio/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#74003d` / `#4a002a`)
- **Summary**: Rotate your device to portrait mode.
- **Total Clean CSS Variables Extracted**: `103` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Matter`
- **Body Font Stack**: `Matter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-h1: 16rem`, `--text-h1--line-height: 80%`, `--text-h1-mobile: 6.4rem`
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 97.2px`, `line-height: 78.732px`, `font-weight: 400`, `letter-spacing: -0.972px`); CSS variables `--text-h2: 10.8rem`, `--text-h2--line-height: 81%`, `--text-h2-mobile: 5rem`; rule `h2` (`font-size: var(--text-h4-mobile)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: calc(var(--tracking-t...`)
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: -0.15px`); CSS variables `--font-body: var(--font-multilingual)`, `--text-body-l: 1.7rem`, `--text-body-l--line-height: 190%`; rule `p` (`font-size: var(--text-body-s)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: calc(var(--tracking-t...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: -0.15px`); CSS variables `--default-mono-font-family: var(--font-mono)`, `--text-label: 1.4rem`, `--text-label--line-height: 100%`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#74003d` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fff3e4` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.bg-black { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#4a002a` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#f6e1ce` | live computed `main` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#800080` | `.border-purple-dark { border-color: #800080 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--size` | `375` | Layout / Spatial Grid Token |
| `--margin` | `2rem` | Layout / Spatial Grid Token |
| `--gutter` | `1rem` | Layout / Spatial Grid Token |
| `--header-height` | `6.5rem` | Layout / Spatial Grid Token |
| `--vw` | `100vw` | Layout / Spatial Grid Token |
| `--vh` | `calc(var(--vh-initial,1vh)*100)` | Layout / Spatial Grid Token |
| `--vh-dynamic` | `calc(var(--vh-initial-dynamic,1vh)*100)` | Layout / Spatial Grid Token |
| `--column` | `calc((var(--vw) - var(--margin)*2)/12)` | Layout / Spatial Grid Token |
| `--global-header-text` | `var(--color-purple-dark)` | Typography Ink Token |
| `--global-header-bg` | `var(--color-beige-light)` | Canvas / Surface Token |
| `--font-body` | `var(--font-multilingual)` | Typography / Scale Token |
| `--font-spark` | `var(--font-multilingual-bold)` | Typography / Scale Token |
| `--font-heading` | `var(--font-multilingual-bold)` | Typography Ink Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--spacing` | `.1rem` | Layout / Spatial Grid Token |
| `--breakpoint-xl` | `64.5rem` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `carnilove-ashfall-studio`)**:
   - Landmark `<header class="header top-0">` (`1440x72px`) hosting `Carnilove · Home` navigation (`Mission · Ambassadors · Blog · Contact · Dry Food`), DOM attributes (`data-astro-cid-sckkx6r4`, `data-src="https://images.ctfass..."`, `data-srcset="https://images.ctfass..."`, `data-sizes="100vw"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.dropdown-el> — `P U R E P R E S E N C E I N M O T `)**:
   - Landmark `<section class="dropdown-el flex">` presenting display lead `P U R E P R E S E N C E I N M O T I O N PURE PRES...` and copy excerpt *"Rotate your device to portrait mode."* over `#74003d` canvas and `#fff3e4` ink.
3. **Primary Showcase & Content Grid (<section.flex> — `S H A R P E N E D B Y N A T U R A `)**:
   - Landmark `<section class="dropdown-el flex">` rendering section `S H A R P E N E D B Y N A T U R A L E N E R G Y S...` with copy *"T R U S T T H E I R"*, asset references (`apple-touch-icon-57x57.png`, `apple-touch-icon-60x60.png`, `apple-touch-icon-72x72.png`, `apple-touch-icon-76x76.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.flex-col> — `f r e e t o b e f i e r c e l y a `)**:
   - Landmark `<section class="dropdown-el flex">` framing `f r e e t o b e f i e r c e l y a l i v e free to...` and `TRUST THEIRINSTINCT` (*"TRUST THEIRINSTINCT"*) with `#000000` surface cards, `#4a002a` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://carnilove.ashfall.studio/`)**:
   - Landmark `<footer class="footer gap-y-20">` anchoring `Carnilove · Home` footer links (`Mission · Ambassadors · Blog · Contact · Dry Food`), copy *"Real food that respects who they are — and who they’ve alway"*, and `#800080` structural dividers.
