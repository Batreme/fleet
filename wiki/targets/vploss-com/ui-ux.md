---
title: "UI & UX Architecture: vploss-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: vploss-com

## Overview & Design Identity
- **Target**: `vploss-com` (**VPLOSS**)
- **Production URL**: [https://vploss.com](https://vploss.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff2a2a`)
- **Summary**: VPLOSS, the fashion label of designer Vincent Ploss: the New York and Paris Fashion Week 2026 collections, with every runway look to rent.
- **Total Clean CSS Variables Extracted**: `65` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Monument Extended`
- **Body Font Stack**: `PP Monument Extended Fallback`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: normal`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 166.587px`, `line-height: 133.27px`, `font-weight: 900`, `letter-spacing: -4.16467px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#030303` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ed3833` | `._fill_iqn1v_19 { background: #ed3833 }` |
| **Interactive Accent / Highlight** | `#ff2a2a` | `._backToTopBtn_np885_286:hover { background-color: #ff2a2a }` |
| **Secondary / Muted Copy** | `#ed3833` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#d4d4d4` | `._buttonPrimary_1cyng_93:hover { border-color: #d4d4d4 }` |
| **Variable Token (`--color-corridor-bg`)** | `#0a0a0a` | `var(--color-corridor-bg)` in `:root` |
| **Variable Token (`--color-grey-9`)** | `#171717` | `var(--color-grey-9)` in `:root` |
| **Variable Token (`--color-grey-96`)** | `#f5f5f5` | `var(--color-grey-96)` in `:root` |
| **Variable Token (`--color-pfw`)** | `#ff5100` | `var(--color-pfw)` in `:root` |
| **Variable Token (`--color-paris-night`)** | `#0b0908` | `var(--color-paris-night)` in `:root` |
| **Variable Token (`--color-paris-chalk`)** | `#efe9e2` | `var(--color-paris-chalk)` in `:root` |
| **Variable Token (`--paris-ember`)** | `#a02707` | `var(--paris-ember)` in `:root` |
| **Variable Token (`--paris-flame`)** | `#f66f1d` | `var(--paris-flame)` in `:root` |
| **Variable Token (`--paris-orange`)** | `#ffb142` | `var(--paris-orange)` in `:root` |
| **Variable Token (`--paris-amber`)** | `#ffdd86` | `var(--paris-amber)` in `:root` |
| **Variable Token (`--paris-core`)** | `#fff8e2` | `var(--paris-core)` in `:root` |
| **Variable Token (`--paris-soot`)** | `#4d4642` | `var(--paris-soot)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-bg` | `#fff` | Canvas / Surface Token |
| `--color-fg` | `#030303` | Typography Ink Token |
| `--color-corridor-bg` | `#0a0a0a` | Canvas / Surface Token |
| `--color-grey-9` | `#171717` | Brand / Palette Token |
| `--color-grey-83` | `#d4d4d4` | Brand / Palette Token |
| `--color-grey-96` | `#f5f5f5` | Brand / Palette Token |
| `--color-pfw` | `#ff5100` | Brand / Palette Token |
| `--color-accent-red` | `#ed3833` | Brand / Palette Token |
| `--color-paris-night` | `#0b0908` | Brand / Palette Token |
| `--color-paris-chalk` | `#efe9e2` | Brand / Palette Token |
| `--paris-ember` | `#a02707` | Color / Atmospheric Token |
| `--paris-flame` | `#f66f1d` | Color / Atmospheric Token |
| `--paris-orange` | `#ffb142` | Color / Atmospheric Token |
| `--paris-amber` | `#ffdd86` | Color / Atmospheric Token |
| `--paris-core` | `#fff8e2` | Color / Atmospheric Token |
| `--paris-soot` | `#4d4642` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `vploss-com`)**:
   - Landmark `<header class="lenis">` (`1440x117px`) hosting `VPLOSS` navigation (`LOOKS L O O K S · RENT R E N T`), DOM attributes (`data-cover-scroll`, `data-astro-exec`, `data-header-panel`, `data-header-fade`), and stylesheet rule `._mobileFade_a9xy0_50 { display:block }`.
2. **Hero Stage & Focal Lead (<section.heroPin> — `VPLOSS`)**:
   - Landmark `<section class="heroPin">` presenting display lead `VPLOSS` and copy excerpt *"LOOKS FROM THE SHOW"* over `#ffffff` canvas and `#030303` ink.
3. **Primary Showcase & Content Grid (<section#film> — `NYFW '26`)**:
   - Landmark `<section id="film">` rendering section `NYFW '26` with copy *"Looks from the Show"*, asset references (`favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `gnExpanded_a9xy0_95 ._navLink_a9x... { color:030303 }`.
4. **Interactive Detail & Feature Matrix (<section#looks> — `Campaigns`)**:
   - Landmark `<section id="looks">` framing `Campaigns` and `My Partners` (*"New York Fashion Week 2026 The Hourglass, Pinned, Confined, Ideal"*) with `#ed3833` surface cards, `#ff2a2a` accents, and `nded_a9xy0_95 ._navLink_a9xy0_108... { opacity:.85 }`.
5. **Colophon & Global Directory Footer (<footer#footer> — `https://vploss.com`)**:
   - Landmark `<footer id="footer">` anchoring `VPLOSS` footer links (`LOOKS L O O K S · RENT R E N T`), copy *"The Hourglass, Pinned, Confined, Ideal, The Thread, Armour /"*, and `#d4d4d4` structural dividers.
