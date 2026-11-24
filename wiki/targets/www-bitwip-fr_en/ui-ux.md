---
title: "UI & UX Architecture: www-bitwip-fr_en"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-bitwip-fr_en

## Overview & Design Identity
- **Target**: `www-bitwip-fr_en` (**Communications consulting agency for Overseas France · Bitwip**)
- **Production URL**: [https://www.bitwip.fr/en](https://www.bitwip.fr/en)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#121414` canvas, `#ffffff` ink, `#fc622a` accent)
- **Summary**: Communications consulting agency in Overseas France and Occitanie: strategy, branding, web and campaigns. French Guiana, Martinique, Guad...
- **Total Clean CSS Variables Extracted**: `186` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cabinet Grotesk`
- **Body Font Stack**: `Cabinet Grotesk`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 37.76px`, `line-height: 58.528px`, `font-weight: 400`); CSS variables `--t-h1: clamp(2.75rem,1.6rem + 4.6vw,6rem)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 91.84px`, `line-height: 90.0032px`, `font-weight: 500`, `letter-spacing: -3.6736px`); CSS variables `--t-h2: clamp(2.375rem,1.55rem + 3.4vw,5rem)`; rule `h2` (`font-size: var(--t-h3)`, `line-height: 1.12`, `letter-spacing: -.025em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 18.88px`, `line-height: 29.264px`, `font-weight: 400`); CSS variables `--t-body: clamp(1.0625rem,1rem + .2vw,1.1875rem)`; rule `p` (`font-size: clamp(1.625rem,.9rem + 1.6vw,...`, `line-height: 1.16`, `letter-spacing: -.03em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18.88px`, `line-height: 29.264px`, `font-weight: 400`); CSS variables `--f-label: "Clash Display","Cabinet Grotesk","Helvetica Neue",Arial,sans-serif`, `--t-small: .9375rem`, `--t-label: .75rem`; rule `.label` (`font-size: .6875rem`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#121414` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0a0a0a` | `.nav__bar::before { background: #0a0a0a }` |
| **Interactive Accent / Highlight** | `#fc622a` | live computed `a` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#b23c0b` | `var(--papaye-ink)` in `:root` |
| **Structural Hairline Border** | `#333535` | `var(--line)` in `:root` (`rgba(255,255,255,.14)`) |
| **Variable Token (`--noir`)** | `#000000` | `var(--noir)` in `:root` |
| **Variable Token (`--ink`)** | `#0b0b0b` | `var(--ink)` in `:root` |
| **Variable Token (`--ink-2`)** | `#141414` | `var(--ink-2)` in `:root` |
| **Variable Token (`--papaye-titre`)** | `#ee5520` | `var(--papaye-titre)` in `:root` |
| **Variable Token (`--papier`)** | `#f4efe7` | `var(--papier)` in `:root` |
| **Variable Token (`--papier-2`)** | `#eae3d8` | `var(--papier-2)` in `:root` |
| **Variable Token (`--encre`)** | `#121212` | `var(--encre)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--noir` | `#000` | Color / Atmospheric Token |
| `--ink` | `#0B0B0B` | Typography Ink Token |
| `--ink-2` | `#141414` | Typography Ink Token |
| `--papaye` | `#FC622A` | Color / Atmospheric Token |
| `--papaye-titre` | `#EE5520` | Color / Atmospheric Token |
| `--papaye-ink` | `#B23C0B` | Typography Ink Token |
| `--etoile-y` | `-.015em` | Dimension / Scale Token |
| `--etoile-h` | `.26em` | Dimension / Scale Token |
| `--etoile-w` | `.28em` | Dimension / Scale Token |
| `--papier` | `#F4EFE7` | Color / Atmospheric Token |
| `--papier-2` | `#EAE3D8` | Color / Atmospheric Token |
| `--blanc` | `#FFF` | Color / Atmospheric Token |
| `--encre` | `#121212` | Color / Atmospheric Token |
| `--txt` | `#FFF` | Color / Atmospheric Token |
| `--txt-2` | `rgba(255,255,255,.74)` | Color / Atmospheric Token |
| `--txt-3` | `rgba(255,255,255,.54)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `www-bitwip-fr_en`)**:
   - Landmark `<header class="nav nav--allegee">` (`721x76px`) hosting `Communications consulting agency for` navigation (`Services · All our services · Work · View all work · Culture & tourism`), DOM attributes (`data-gdifilm="direct"`, `data-page="accueil"`, `data-variante="allegee"`, `data-entree`), and stylesheet rule `root { --gc-x:0px }`.
2. **Hero Stage & Focal Lead (<section.hh> — `Bitwip, tech and creative communic`)**:
   - Landmark `<section class="hh mj">` presenting display lead `Bitwip, tech and creative communications agency T...` and copy excerpt *"Bitwip supports impact-driven projects in Overseas France and acr"* over `#121414` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.sec> — `We believe in meaningful communica`)**:
   - Landmark `<section class="sec papier">` rendering section `We believe in meaningful communication` with copy *"Bitwip, tech and creative communications agency"*, asset references (`mesure.js`, `consentement.js`, `favicon-b-fond-noir.webp`, `CabinetGrotesk-900.woff2`), and grid rule `after { box-sizing:border-box }`.
4. **Interactive Detail & Feature Matrix (<section.sec:nth(2)> — `Our services`)**:
   - Landmark `<section class="sec">` framing `Our services` and `Strategy & consulting` (*"The communications agency where"*) with `#0a0a0a` surface cards, `#fc622a` accents, and `html { -webkit-text-size-adjust:100%;text-size-adjust:100%;scroll-padding-top:1... }`.
5. **Colophon & Global Directory Footer (<footer.pied> — `https://www.bitwip.fr/en`)**:
   - Landmark `<footer class="pied">` anchoring `Communications consulting agency` footer links (`Services · All our services · Work · View all work · Culture & tourism`), copy *"c r e a t i v i t y"*, and `#333535` structural dividers.
