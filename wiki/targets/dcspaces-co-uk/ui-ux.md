---
title: "UI & UX Architecture: dcspaces-co-uk"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: dcspaces-co-uk

## Overview & Design Identity
- **Target**: `dcspaces-co-uk` (**Chorley Builders · Extensions & Renovations · DC Carpentry**)
- **Production URL**: [https://dcspaces.co.uk/](https://dcspaces.co.uk/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f4f1e9` canvas, `#343631` ink, `#6c8f6c` accent)
- **Summary**: Family-run builders in Chorley. House extensions, wall and chimney breast removals, kitchens and bespoke staircases across Lancashire. Fr...
- **Total Clean CSS Variables Extracted**: `29` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Satoshi`
- **Body Font Stack**: `Satoshi`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 73.6px`, `line-height: 73.6px`, `font-weight: 700`, `letter-spacing: -3.312px`); CSS variables `--cc-font-display: 'Satoshi', system-ui, sans-serif`; rule `h1` (`font-size: clamp(2.6rem, 5.6vw, 4.6rem)`, `line-height: 1`, `letter-spacing: -.045em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 56px`, `line-height: 57.12px`, `font-weight: 700`, `letter-spacing: -2.24px`); rule `h2` (`font-size: clamp(1.5rem, 2.4vw, 2.1rem)`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 27.2px`, `font-weight: 400`); CSS variables `--cc-font-body: 'Satoshi', system-ui, sans-serif`; rule `p` (`font-size: .9rem`, `line-height: 1.55`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 27.2px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f1e9` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#343631` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f2f1ed` | `var(--cc-paper)` in `:root` |
| **Interactive Accent / Highlight** | `#6c8f6c` | `var(--brand-2)` in `:root` |
| **Secondary / Muted Copy** | `#767d86` | `var(--ink-3)` in `:root` |
| **Structural Hairline Border** | `#e0ddd6` | `var(--line)` in `:root` (`rgba(20,22,26,.09)`) |
| **Variable Token (`--cc-ink`)** | `#14161a` | `var(--cc-ink)` in `:root` |
| **Variable Token (`--cc-green`)** | `#344c3a` | `var(--cc-green)` in `:root` |
| **Variable Token (`--cc-forest`)** | `#2e432f` | `var(--cc-forest)` in `:root` |
| **Variable Token (`--cc-sage`)** | `#dfe5dc` | `var(--cc-sage)` in `:root` |
| **Variable Token (`--cc-sand`)** | `#e8e2d4` | `var(--cc-sand)` in `:root` |
| **Variable Token (`--cc-on-deep`)** | `#ffffff` | `var(--cc-on-deep)` in `:root` |
| **Variable Token (`--ink-2`)** | `#4a5058` | `var(--ink-2)` in `:root` |
| **Variable Token (`--paper-2`)** | `#e8e6e0` | `var(--paper-2)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cc-ink` | `#14161a` | Typography Ink Token |
| `--cc-green` | `#344c3a` | Color / Atmospheric Token |
| `--cc-forest` | `#2e432f` | Color / Atmospheric Token |
| `--cc-sage` | `#dfe5dc` | Color / Atmospheric Token |
| `--cc-sand` | `#e8e2d4` | Color / Atmospheric Token |
| `--cc-paper` | `#f2f1ed` | Canvas / Surface Token |
| `--cc-deep` | `#14161a` | Color / Atmospheric Token |
| `--cc-on-deep` | `#ffffff` | Color / Atmospheric Token |
| `--cc-font-display` | `'Satoshi', system-ui, sans-serif` | Typography / Scale Token |
| `--cc-font-body` | `'Satoshi', system-ui, sans-serif` | Typography / Scale Token |
| `--ink` | `#14161A` | Typography Ink Token |
| `--ink-2` | `#4A5058` | Typography Ink Token |
| `--ink-3` | `#767D86` | Typography Ink Token |
| `--paper` | `#F2F1ED` | Canvas / Surface Token |
| `--paper-2` | `#E8E6E0` | Canvas / Surface Token |
| `--white` | `#FFFFFF` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hdr> — `dcspaces-co-uk`)**:
   - Landmark `<header class="hdr">` (`1440x86px`) hosting `Chorley Builders · Extensions & Reno` navigation (`Home · About · All services · Extensions · Projects`), DOM attributes (`data-carousel`, `data-dir="prev"`, `data-dir="next"`, `data-dir="prev"`), and stylesheet rule `.dcc-hp { position: absolute !important; left: -9999px !important; width: 1px; hei... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Building & Renovation Specialists `)**:
   - Landmark `<section class="hero is-ready">` presenting display lead `Building & Renovation Specialists Across Chorley...` and copy excerpt *"CRAFTING UNIQUE SPACES"* over `#f4f1e9` canvas and `#343631` ink.
3. **Primary Showcase & Content Grid (<section.opening> — `Everything your house needs, from `)**:
   - Landmark `<section class="opening">` rendering section `Everything your house needs, from one team` with copy *"Crafting unique spaces"*, asset references (`favicon.png`, `apple-touch-icon.png`, `satoshi-900.woff2`, `satoshi-400.woff2`), and grid rule `.dcc-msg--ok { background: e6ebe3; color: 2e432f; border: 1px solid rgba(52,76,58,.25); }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Home Extensions`)**:
   - Landmark `<section class="section">` framing `Home Extensions` and `Loft Conversions` (*"Whether you’re planning a home extension, full renovation, loft c"*) with `#f2f1ed` surface cards, `#6c8f6c` accents, and `.dcc-msg--err { background: f6e8e4; color: 7a2e1f; border: 1px solid rgba(122,46,31,.22); }`.
5. **Colophon & Global Directory Footer (<footer.ftr> — `https://dcspaces.co.uk/`)**:
   - Landmark `<footer class="ftr">` anchoring `Chorley Builders · Extensions & ` footer links (`Home · About · All services · Extensions · Projects`), copy *"As a family-run business, we combine skilled craftsmanship w"*, and `#e0ddd6` structural dividers.
