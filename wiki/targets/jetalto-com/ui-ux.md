---
title: "UI & UX Architecture: jetalto-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: jetalto-com

## Overview & Design Identity
- **Target**: `jetalto-com` (**JetALto, Private Jet Charter · Fly Anywhere, On Your Schedule**)
- **Production URL**: [https://jetalto.com/](https://jetalto.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#faf7f2` canvas, `#0b1220` ink, `#000080` accent)
- **Summary**: Instant private jet charter quotes from vetted operators. On-demand flights to 5,000+ airports worldwide. Empty-leg alerts, transparent p...
- **Total Clean CSS Variables Extracted**: `47` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 73.44px`, `font-weight: 500`, `letter-spacing: -1.08px`); rule `h1` (`font-size: clamp(30px,4.4vw,52px)`, `line-height: 1.06`, `letter-spacing: -.01em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 44px`, `line-height: 48.4px`, `font-weight: 500`, `letter-spacing: -0.22px`); rule `h2` (`font-size: 26px`, `letter-spacing: -.005em`, `font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24.8px`, `font-weight: 400`); rule `body` (`font-size: 16px`, `line-height: 1.55`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24.8px`, `font-weight: 400`); rule `small` (`font-size: 11px`, `letter-spacing: .06em`, `font-weight: 600`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#faf7f2` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0b1220` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | live computed `header` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#000080` | `.nav .cta { background: navy }` (`#000080`) |
| **Secondary / Muted Copy** | `#5d6b82` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#e5ded1` | `var(--line)` in `:root` |
| **Variable Token (`--navy`)** | `#0a2540` | `var(--navy)` in `:root` |
| **Variable Token (`--navy-2`)** | `#122d4d` | `var(--navy-2)` in `:root` |
| **Variable Token (`--navy-3`)** | `#1a3860` | `var(--navy-3)` in `:root` |
| **Variable Token (`--paper-2`)** | `#f2ede4` | `var(--paper-2)` in `:root` |
| **Variable Token (`--gold`)** | `#c5964b` | `var(--gold)` in `:root` |
| **Variable Token (`--gold-2`)** | `#d4a24c` | `var(--gold-2)` in `:root` |
| **Variable Token (`--gold-soft`)** | `#f3e4c1` | `var(--gold-soft)` in `:root` |
| **Variable Token (`--danger`)** | `#b93a2a` | `var(--danger)` in `:root` |
| **Variable Token (`--ok`)** | `#1f7a4e` | `var(--ok)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--navy` | `#0a2540` | Layout / Spatial Grid Token |
| `--navy-2` | `#122d4d` | Layout / Spatial Grid Token |
| `--navy-3` | `#1a3860` | Layout / Spatial Grid Token |
| `--ink` | `#0b1220` | Typography Ink Token |
| `--paper` | `#faf7f2` | Canvas / Surface Token |
| `--paper-2` | `#f2ede4` | Canvas / Surface Token |
| `--line` | `#e5ded1` | Color / Atmospheric Token |
| `--muted` | `#5d6b82` | Color / Atmospheric Token |
| `--gold` | `#c5964b` | Color / Atmospheric Token |
| `--gold-2` | `#d4a24c` | Color / Atmospheric Token |
| `--gold-soft` | `#f3e4c1` | Color / Atmospheric Token |
| `--danger` | `#b93a2a` | Color / Atmospheric Token |
| `--ok` | `#1f7a4e` | Color / Atmospheric Token |
| `--radius` | `6px` | Elevation / Border Token |
| `--shadow-lg` | `0 40px 80px -30px rgba(10,37,64,.35), 0 8px 24px -8px rgba(10,37,64,.2)` | Elevation / Border Token |
| `--shadow-md` | `0 10px 24px -12px rgba(10,37,64,.25)` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `jetalto-com`)**:
   - Landmark `<header class="site-header">` (`1440x71px`) hosting `JetALto, Private Jet Charter · Fly A` navigation (`Home · Our Fleet · Destinations · Blog · Get a Quote`), DOM attributes (`data-step-panel="1"`, `data-lat="50.0333"`, `data-lon="8.5706"`, `data-min="1"`), and stylesheet rule `.phone-field .iti { width:100%;--iti-border-color:d8dee6;--iti-border-radius:8px;--iti-hover... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Private Jet Charters`)**:
   - Landmark `<section class="hero hero-wide">` presenting display lead `Private Jet Charters` and copy excerpt *"On-demand private jet charter quotes from 3,800+ vetted operators"* over `#faf7f2` canvas and `#0b1220` ink.
3. **Primary Showcase & Content Grid (<section.pad> — `Get a private jet charter quote`)**:
   - Landmark `<section class="pad step2-only">` rendering section `Get a private jet charter quote` with copy *"Global charter · 24 / 7 · Email support"*, asset references (`favicon.ico`, `favicon-16.png`, `favicon-32.png`, `favicon-96.png`), and grid rule `.phone-field .iti__country-container { max-width:130px }`.
4. **Interactive Detail & Feature Matrix (<section.section-dark> — `Almost done, where should we send `)**:
   - Landmark `<section class="pad section-dark">` framing `Almost done, where should we send it?` and `Get an instant charter quote` (*"Get an instant charter quote"*) with `#ffffff` surface cards, `#000080` accents, and `.phone-field .iti__selected-country { font:inherit;font-size:13px;color:0a2540;padding:0 8px 0 0;border-right:... }`.
5. **Colophon & Global Directory Footer (<footer.nav> — `https://jetalto.com/`)**:
   - Landmark `<footer class="nav">` anchoring `JetALto, Private Jet Charter · F` footer links (`Home · Our Fleet · Destinations · Blog · Get a Quote`), copy *"6 classes, 18 models"*, and `#e5ded1` structural dividers.
