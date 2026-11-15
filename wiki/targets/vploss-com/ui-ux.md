# UI & UX Architecture: vploss-com

## Overview & Design Identity
- **Target**: `vploss-com` (**VPLOSS**)
- **Production URL**: [https://vploss.com](https://vploss.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#171717`)
- **Summary**: VPLOSS, the fashion label of designer Vincent Ploss: the New York and Paris Fashion Week 2026 collections, with every runway look to rent.
- **Total Clean CSS Variables Extracted**: `65` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Monument Extended`
- **Body Font Stack**: `PP Monument Narrow`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.75rem`, `11.5px`, `clamp(1.4rem,2.4vw,2.2rem)`, `10.5px`, `14px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.75rem`, `11.5px`, `clamp(1.4rem,2.4vw,2.2rem)`, `10.5px`, `14px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.75rem`, `11.5px`, `clamp(1.4rem,2.4vw,2.2rem)`, `10.5px`, `14px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.75rem`, `11.5px`, `clamp(1.4rem,2.4vw,2.2rem)`, `10.5px`, `14px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-bg)` in `:root` |
| **Primary Typography Ink** | `#030303` | `var(--color-fg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0a0a0a` | `var(--color-corridor-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#171717` | `var(--color-grey-9)` in `:root` |
| **Secondary / Muted Copy** | `#d4d4d4` | `var(--color-grey-83)` in `:root` |
| **Structural Hairline Border** | `#f5f5f5` | `var(--color-grey-96)` in `:root` |
| **Variable Token (`--color-pfw`)** | `#ff5100` | `var(--color-pfw)` in `:root` |
| **Variable Token (`--color-accent-red`)** | `#ed3833` | `var(--color-accent-red)` in `:root` |
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
   - Landmark `<header class="lenis">` hosting `VPLOSS` navigation (`LOOKS L O O K S · RENT R E N T`), DOM attributes (`data-cover-scroll`, `data-astro-exec`, `data-header-panel`, `data-header-fade`), and stylesheet rule `._mobileFade_a9xy0_50 { display:block }`.
2. **Hero Stage & Focal Lead (<section.heroPin> — `VPLOSS`)**:
   - Landmark `<section class="heroPin">` presenting display lead `VPLOSS` and copy excerpt *"CAMPAIGN C A M P A I G N"* over `#fff` canvas and `#030303` ink.
3. **Primary Showcase & Content Grid (<section#film> — `NYFW '26`)**:
   - Landmark `<section id="film">` rendering section `NYFW '26` with copy *"ABOUT VPLOSS A B O U T V P L O S S"*, asset references (`favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `gnExpanded_a9xy0_95 ._navLink_a9x... { color:030303 }`.
4. **Interactive Detail & Feature Matrix (<section#looks> — `Campaigns`)**:
   - Landmark `<section id="looks">` framing `Campaigns` and `My Partners` (*"A B O U T V P L O S S"*) with `#0a0a0a` surface cards, `#171717` accents, and `nded_a9xy0_95 ._navLink_a9xy0_108... { opacity:.85 }`.
5. **Colophon & Global Directory Footer (<footer#footer> — `https://vploss.com`)**:
   - Landmark `<footer id="footer">` anchoring `VPLOSS` footer links (`LOOKS L O O K S · RENT R E N T`), copy *"SUPPORT ME S U P P O R T M E"*, and `#f5f5f5` structural dividers.
