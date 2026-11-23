---
title: "UI & UX Architecture: www-qissa-co-uk"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-qissa-co-uk

## Overview & Design Identity
- **Target**: `www-qissa-co-uk` (**Indian Restaurant in Sevenoaks, Kent · Qissa**)
- **Production URL**: [https://www.qissa.co.uk/](https://www.qissa.co.uk/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a1230` / `#0c1533`)
- **Summary**: Qissa — A Tale of Food. Modern Indian dining beneath the blossoms in the heart of Sevenoaks, Kent. Reserve a table or order takeaway. Rat...
- **Total Clean CSS Variables Extracted**: `26` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `Manrope`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 121.6px`, `line-height: 119.168px`, `font-weight: 330`, `letter-spacing: -2.432px`); CSS variables `--f-display: 'Cormorant Garamond', 'Times New Roman', serif`; rule `.hero-title` (`font-size: clamp(2rem,9vw,7.6rem)`, `letter-spacing: -.02em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 57.6px`, `line-height: 59.904px`, `font-weight: 340`, `letter-spacing: -0.864px`); rule `.h2` (`font-size: clamp(2rem,4.6vw,3.6rem)`, `letter-spacing: -.015em`, `font-weight: 340`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 350`); CSS variables `--f-body: 'Manrope', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`; rule `body` (`line-height: 1.6`, `font-weight: 350`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 350`); rule `small` (`font-size: .7rem`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0a1230` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f6f1e7` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#23282d` | `.wpcf7-spinner { background-color: #23282d }` |
| **Interactive Accent / Highlight** | `#0c1533` | `.cta-band { background: #0c1533 }` |
| **Secondary / Muted Copy** | `#05091a` | `var(--ink)` in `:root` |
| **Structural Hairline Border** | `#1e2c57` | `var(--navy-line)` in `:root` |
| **Variable Token (`--navy-2`)** | `#0e1838` | `var(--navy-2)` in `:root` |
| **Variable Token (`--navy-3`)** | `#16224a` | `var(--navy-3)` in `:root` |
| **Variable Token (`--gold`)** | `#c9a24b` | `var(--gold)` in `:root` |
| **Variable Token (`--gold-hi`)** | `#efd79a` | `var(--gold-hi)` in `:root` |
| **Variable Token (`--gold-deep`)** | `#9a7a34` | `var(--gold-deep)` in `:root` |
| **Variable Token (`--amber`)** | `#e9a85c` | `var(--amber)` in `:root` |
| **Variable Token (`--blossom`)** | `#e7a6c4` | `var(--blossom)` in `:root` |
| **Variable Token (`--blossom-2`)** | `#f2c6d9` | `var(--blossom-2)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#05091A` | Typography Ink Token |
| `--navy` | `#0A1230` | Layout / Spatial Grid Token |
| `--navy-2` | `#0E1838` | Layout / Spatial Grid Token |
| `--navy-3` | `#16224A` | Layout / Spatial Grid Token |
| `--navy-line` | `#1E2C57` | Layout / Spatial Grid Token |
| `--gold` | `#C9A24B` | Color / Atmospheric Token |
| `--gold-hi` | `#EFD79A` | Color / Atmospheric Token |
| `--gold-deep` | `#9A7A34` | Color / Atmospheric Token |
| `--amber` | `#E9A85C` | Color / Atmospheric Token |
| `--blossom` | `#E7A6C4` | Color / Atmospheric Token |
| `--blossom-2` | `#F2C6D9` | Color / Atmospheric Token |
| `--cream` | `#F6F1E7` | Color / Atmospheric Token |
| `--cream-dim` | `rgba(246,241,231,.70)` | Color / Atmospheric Token |
| `--cream-faint` | `rgba(246,241,231,.42)` | Color / Atmospheric Token |
| `--line` | `rgba(201,162,75,.22)` | Color / Atmospheric Token |
| `--line-soft` | `rgba(246,241,231,.10)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-qissa-co-uk`)**:
   - Landmark `<header class="site-header">` (`1440x133px`) hosting `Indian Restaurant in Sevenoaks, Kent` navigation (`00 Home · 01 Our Story · 02 The Menu · Food Menu · Drinks Menu`), DOM attributes (`data-u="contact"`, `data-d="qissa.co.uk"`, `data-tilt`, `data-count="4.8"`), and stylesheet rule `.wpcf7 .hidden-fields-container { display: none; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Qissa`)**:
   - Landmark `<section class="hero">` presenting display lead `Qissa` and copy excerpt *"Celebrating the flavors of India with dishes inspired by differen"* over `#0a1230` canvas and `#f6f1e7` ink.
3. **Primary Showcase & Content Grid (<section.section> — `A word that means a tale.`)**:
   - Landmark `<section class="section">` rendering section `A word that means a tale.` with copy *"Food is all about its story — the origin, the spices, the texture"*, asset references (`gtm.js`, `hero-poster.webp`, `favicon-96.png`, `favicon-32.png`), and grid rule `.wpcf7 form .wpcf7-response-output { margin: 2em 0.5em 1em; padding: 0.2em 1em; border: 2px solid 00a0d2; }`.
4. **Interactive Detail & Feature Matrix (<section.masterpieces> — `Crafted icons & signature plates.`)**:
   - Landmark `<section class="section masterpieces">` framing `Crafted icons & signature plates.` and `Explore the menu, course by course.` (*"‘Qissa’ tells the extraordinary stories behind the foods we eat: "*) with `#23282d` surface cards, `#0c1533` accents, and `form.submitting .wpcf7-response-o... { display: none; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.qissa.co.uk/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Indian Restaurant in Sevenoaks, ` footer links (`00 Home · 01 Our Story · 02 The Menu · Food Menu · Drinks Menu`), copy *"Qissa is a place of gathering, of celebrations, of business,"*, and `#1e2c57` structural dividers.
