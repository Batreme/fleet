---
title: "UI & UX Architecture: lifetimepastapass-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: lifetimepastapass-com

## Overview & Design Identity
- **Target**: `lifetimepastapass-com` (**LIFETIME PASTA PASS · BRADEN'S INFINITE TOUR OF ITALY**)
- **Production URL**: [https://lifetimepastapass.com](https://lifetimepastapass.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×1656px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0a` / `#ffff00`)
- **Summary**: Braden is an Olive Garden Lifetime Pasta Pass holder. Now the internet votes on what he eats next. Live results, vote history, and the fu...
- **Total Clean CSS Variables Extracted**: `528` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `VT323`
- **Body Font Stack**: `VT323`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--header-logo-display: none`, `--header-logo-inverse-display: block`; rule `h1` (`line-height: var(--line-height--di...`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 20.8px`, `line-height: normal`, `font-weight: 700`, `letter-spacing: 1px`); rule `h2` (`font-size: 1.1rem`)
- **Body Copy**: live computed `body` (`font-size: 19px`, `line-height: normal`, `font-weight: 400`); CSS variables `--body-font: 'VT323', monospace`, `--font-paragraph--line-height: 1`, `--body-text-font-weight: 400`; rule `body` (`font-size: 19px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 19px`, `line-height: normal`, `font-weight: 400`); CSS variables `--checkbox-label-padding: 8px`, `--image-height-small: calc(var(--image-height-basis) * 2)`, `--pill-label-padding-inline: var(--padding-xs)`; rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0a0a` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f5f5f5` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#141414` | live computed `nav` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffff00` | `.mp-btn:hover { background: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#ff2079` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#747775` | `var(--chat-messenger-color--outline-active)` in `:root` |
| **Variable Token (`--neon-green`)** | `#39ff14` | `var(--neon-green)` in `:root` |
| **Variable Token (`--neon-yellow`)** | `#ffe900` | `var(--neon-yellow)` in `:root` |
| **Variable Token (`--neon-cyan`)** | `#00e5ff` | `var(--neon-cyan)` in `:root` |
| **Variable Token (`--trophy-bronze`)** | `#d98a3d` | `var(--trophy-bronze)` in `:root` |
| **Variable Token (`--trophy-silver`)** | `#d8d8e2` | `var(--trophy-silver)` in `:root` |
| **Variable Token (`--trophy-gold`)** | `#ffd700` | `var(--trophy-gold)` in `:root` |
| **Variable Token (`--bada-bing`)** | `#ff7a3d` | `var(--bada-bing)` in `:root` |
| **Variable Token (`--bada-boom`)** | `#ff2b1f` | `var(--bada-boom)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#0a0a0a` | Canvas / Surface Token |
| `--bg-panel` | `#141414` | Canvas / Surface Token |
| `--neon-green` | `#39ff14` | Color / Atmospheric Token |
| `--neon-pink` | `#ff2079` | Typography Ink Token |
| `--neon-yellow` | `#ffe900` | Color / Atmospheric Token |
| `--neon-cyan` | `#00e5ff` | Color / Atmospheric Token |
| `--white` | `#f5f5f5` | Canvas / Surface Token |
| `--pixel-font` | `'Press Start 2P', monospace` | Typography / Scale Token |
| `--body-font` | `'VT323', monospace` | Typography / Scale Token |
| `--trophy-bronze` | `#d98a3d` | Color / Atmospheric Token |
| `--trophy-silver` | `#d8d8e2` | Color / Atmospheric Token |
| `--trophy-gold` | `#ffd700` | Color / Atmospheric Token |
| `--bada-bing` | `#ff7a3d` | Color / Atmospheric Token |
| `--bada-boom` | `#ff2b1f` | Color / Atmospheric Token |
| `--hover-lift-amount` | `4px` | Dimension / Scale Token |
| `--hover-scale-amount` | `1.03` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `lifetimepastapass-com`)**:
   - Landmark `<header class="site-header">` (`1440x66px`) hosting `LIFETIME PASTA PASS · BRADEN'S INFIN` navigation (`Home · Trophy Case · OG Merch Gallery · Backstory · Get in Touch`), DOM attributes (`data-address="braden@lifetimepastap..."`, `data-track="mailapp"`, `data-category="Pasta"`, `data-category="Pasta"`), and stylesheet rule `h3 { font-family: var(--pixel-font); text-transform: uppercase; letter-spacin... }`.
2. **Hero Stage & Focal Lead (<section.poll-section> — `Vote on what a LIFETIME PASTA PASS`)**:
   - Landmark `<section class="poll-section">` presenting display lead `Vote on what a LIFETIME PASTA PASS holder eats next` and copy excerpt *"Use discount code PASTAPASS for 10% off Newks Hot Sauce!"* over `#0a0a0a` canvas and `#f5f5f5` ink.
3. **Primary Showcase & Content Grid (<section.visits-section> — `Second Sauce`)**:
   - Landmark `<section class="visits-section">` rendering section `Second Sauce` with copy *"LIFETIME PASTA PASS"*, asset references (`fonts.googleapis.com`, `css2`, `style.css`, `card.png (Lifetime Pasta Pass card)`), and grid rule `.site-header { position: sticky; top: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.visits-section:nth(2)> — `Embed This Poll`)**:
   - Landmark `<section class="visits-section">` framing `Embed This Poll` and `Things are heating up!` (*"33% (10) Continue your pasta adventure to unlock new roles, and u"*) with `#141414` surface cards, `#ffff00` accents, and `.site-nav.open { right: 0; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://lifetimepastapass.com`)**:
   - Landmark `<footer class="site-footer">` anchoring `LIFETIME PASTA PASS · BRADEN'S I` footer links (`Home · Trophy Case · OG Merch Gallery · Backstory · Get in Touch`), copy *"Continue your pasta adventure to unlock new roles, and use t"*, and `#747775` structural dividers.
