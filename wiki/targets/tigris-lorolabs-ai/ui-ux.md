---
title: "UI & UX Architecture: tigris-lorolabs-ai"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: tigris-lorolabs-ai

## Overview & Design Identity
- **Target**: `tigris-lorolabs-ai` (**TIGRIS · Instinct, in Its Rarest Form**)
- **Production URL**: [https://tigris.lorolabs.ai/](https://tigris.lorolabs.ai/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#20060e` / `#f2d38a`)
- **Summary**: Maison Tigris. Sculptural high jewellery in gold, rubies and diamonds. Discover the collection and explore a private viewing.
- **Total Clean CSS Variables Extracted**: `9` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Bodoni Moda`
- **Body Font Stack**: `Space Grotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 227.52px`, `line-height: 216.144px`, `font-weight: 600`, `letter-spacing: 7.9632px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 63px`, `line-height: 64.26px`, `font-weight: 600`); rule `.section-title` (`font-size: clamp(2.6rem,7svh,5rem)`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 300`); rule `p` (`font-size: .75rem`, `letter-spacing: .22em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 11.52px`, `line-height: normal`, `font-weight: 300`, `letter-spacing: 3.2256px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#20060e` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f5e9d6` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#200610` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#f2d38a` | live computed `a` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#c9a24a` | `.product-details dt { color: #c9a24a }` |
| **Structural Hairline Border** | `#3e2219` | `.piece__media { border: #3e2219 }` |
| **Variable Token (`--burgundy`)** | `#4a0e1a` | `var(--burgundy)` in `:root` |
| **Variable Token (`--oxblood`)** | `#24060e` | `var(--oxblood)` in `:root` |
| **Variable Token (`--void`)** | `#120309` | `var(--void)` in `:root` |
| **Variable Token (`--ruby`)** | `#9b1b30` | `var(--ruby)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--burgundy` | `#4a0e1a` | Color / Atmospheric Token |
| `--oxblood` | `#24060e` | Color / Atmospheric Token |
| `--void` | `#120309` | Color / Atmospheric Token |
| `--gold` | `#c9a24a` | Color / Atmospheric Token |
| `--gold-hi` | `#f2d38a` | Color / Atmospheric Token |
| `--ruby` | `#9b1b30` | Color / Atmospheric Token |
| `--cream` | `#f5e9d6` | Color / Atmospheric Token |
| `--serif` | `"Bodoni Moda", "Didot", serif` | Typography / Scale Token |
| `--grot` | `"Space Grotesk", system-ui, sans-serif` | Dimension / Scale Token |
| `--tigris-lorolabs--bg` | `#20060e` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--tigris-lorolabs--ink` | `#f5e9d6` | Primary Typography Ink (computed-derived) |
| `--tigris-lorolabs--surface` | `#200610` | Surface Substrate (computed-derived) |
| `--tigris-lorolabs--accent` | `#f2d38a` | Interactive Accent (computed-derived) |
| `--tigris-lorolabs--muted` | `#c9a24a` | Secondary Ink (computed-derived) |
| `--tigris-lorolabs--border` | `#3e2219` | Structural Border (computed-derived) |
| `--tigris-lorolabs--container` | `1440px` | Container Bound (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `tigris-lorolabs-ai`)**:
   - Landmark `<header class="nav">` (`1440x88px`) hosting `TIGRIS · Instinct, in Its Rarest For` navigation (`Collection · Heritage · Acquire`), DOM attributes (`data-hover`, `data-variant="gold"`, `data-variant="enamel"`, `data-variant="pave"`), and stylesheet rule `html { scrollbar-width:thin;scrollbar-color:var(--gold) var(--void);background:... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `TIGRIS`)**:
   - Landmark `<section class="hero">` presenting display lead `TIGRIS` and copy excerpt *"Instinct, in its rarest form."* over `#20060e` canvas and `#f5e9d6` ink.
3. **Primary Showcase & Content Grid (<section.manifesto> — `A stripe, held in gold.`)**:
   - Landmark `<section class="manifesto">` rendering section `A stripe, held in gold.` with copy *"Scroll to discover"*, asset references (`manifest.webmanifest`, `icon-192.png`, `bodoni-moda-latin-normal.woff2`, `space-grotesk-latin-normal.woff2`), and grid rule `html.lenis body { height:auto }`.
4. **Interactive Detail & Feature Matrix (<section.stripes> — `Power, unbroken.`)**:
   - Landmark `<section class="stripes">` framing `Power, unbroken.` and `From Gold to Enamel` (*"A stripe, remembered in gold."*) with `#200610` surface cards, `#f2d38a` accents, and `.lenis.lenis-smooth { scroll-behavior:auto!important }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://tigris.lorolabs.ai/`)**:
   - Landmark `<footer class="footer">` anchoring `TIGRIS · Instinct, in Its Rarest` footer links (`Collection · Heritage · Acquire`), copy *"Our story begins at dusk. A tiger crosses the river; its str"*, and `#3e2219` structural dividers.
