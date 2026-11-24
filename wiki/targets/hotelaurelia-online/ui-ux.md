---
title: "UI & UX Architecture: hotelaurelia-online"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: hotelaurelia-online

## Overview & Design Identity
- **Target**: `hotelaurelia-online` (**Villa Aurelia — Butik Lüks Otel & Rezervasyon**)
- **Production URL**: [https://hotelaurelia.online/](https://hotelaurelia.online/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f8f5f2` canvas, `#252e37` ink, `#e8d9b8` accent)
- **Summary**: Villa Aurelia; sakin, sinematik bir kaçamak olarak tasarlanmış butik lüks otel. Odalar, gastronomi, deneyimler, düğünler ve doğrudan reze...
- **Total Clean CSS Variables Extracted**: `86` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `La Graziela`
- **Body Font Stack**: `Berlingske Serif`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 187.2px`, `line-height: 177.84px`, `font-weight: 400`, `letter-spacing: -3.744px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 66.24px`, `line-height: 67.5648px`, `font-weight: 500`, `letter-spacing: -1.3248px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 300`); rule `,body` (`font-weight: 300`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 18px`, `font-weight: 500`, `letter-spacing: 2.4px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f8f5f2` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#252e37` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--normal-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#e8d9b8` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#b8a58a` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e5e7eb` | `:after { border-color: #e5e7eb }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `36 30% 96%` | Canvas / Surface Token |
| `--foreground` | `210 20% 18%` | Typography Ink Token |
| `--card` | `36 30% 98%` | Dimension / Scale Token |
| `--card-foreground` | `210 20% 18%` | Typography Ink Token |
| `--popover` | `36 30% 96%` | Dimension / Scale Token |
| `--popover-foreground` | `210 20% 18%` | Typography Ink Token |
| `--primary` | `200 55% 48%` | Brand / Palette Token |
| `--primary-foreground` | `36 30% 98%` | Typography Ink Token |
| `--secondary` | `36 22% 90%` | Brand / Palette Token |
| `--secondary-foreground` | `210 20% 18%` | Typography Ink Token |
| `--muted` | `36 18% 92%` | Dimension / Scale Token |
| `--muted-foreground` | `210 12% 42%` | Typography Ink Token |
| `--accent` | `38 55% 58%` | Brand / Palette Token |
| `--accent-foreground` | `210 20% 18%` | Typography Ink Token |
| `--destructive` | `0 60% 50%` | Dimension / Scale Token |
| `--destructive-foreground` | `36 30% 98%` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-0> — `hotelaurelia-online`)**:
   - Landmark `<header class="top-0 inset-x-0">` (`1440x128px`) hosting `Villa Aurelia — Butik Lüks Otel & Re` navigation (`ODALAR · GASTRONOMİ · DENEYİMLER · JOURNAL`), DOM attributes (`data-artifact-kind="dwl_content_hash"`, `data-artifact-id="b530ed7030d66d8b94f08..."`, `data-commit-sha="8f86fc78813222994402b..."`, `data-context-token="v1.eyJwcm9qZWN0X2lkIj..."`), and stylesheet rule `after { box-sizing:border-box;border-width:0;border-style:solid;border-color:e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.rune-revealed> — `La dolce vita`)**:
   - Landmark `<section class="rune-revealed rune-reveal-up">` presenting display lead `La dolce vita` and copy excerpt *"titizlikle tasarlanmış."* over `#f8f5f2` canvas and `#252e37` ink.
3. **Primary Showcase & Content Grid (<section.rune-reveal-up> — `titizlikle tasarlanmış.`)**:
   - Landmark `<section class="rune-revealed rune-reveal-up">` rendering section `titizlikle tasarlanmış.` with copy *"Villa Aurelia; mimariye, ışığa ve orada yaşanan hayata duyulan de"*, asset references (`favicon.png`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.au-about-reveal> — `Villa Aurelia; mimariye, ışığa ve `)**:
   - Landmark `<section class="au-about-reveal rune-revealed">` framing `Villa Aurelia; mimariye, ışığa ve orada yaşanan ` and `huzur bulmak için ideal yer` (*"huzur bulmak için ideal yer"*) with `#ffffff` surface cards, `#e8d9b8` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://hotelaurelia.online/`)**:
   - Landmark `<footer class="relative overflow-hidden">` anchoring `Villa Aurelia — Butik Lüks Otel ` footer links (`ODALAR · GASTRONOMİ · DENEYİMLER · JOURNAL`), copy *"oluşan bir mevsim."*, and `#e5e7eb` structural dividers.
