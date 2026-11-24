---
title: "UI & UX Architecture: web-smith-de"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: web-smith-de

## Overview & Design Identity
- **Target**: `web-smith-de` (**Internetagentur Ostwestfalen: Websites & SEO · Web Smith**)
- **Production URL**: [https://web-smith.de](https://web-smith.de)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0a1320` ink, `#0000ff` accent)
- **Summary**: Websites, SEO und individuelle Software: Web Smith ist deine Internetagentur aus Ostwestfalen – mit kostenlosem Website-Check und Konfigu...
- **Total Clean CSS Variables Extracted**: `23` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Plus Jakarta Sans`
- **Body Font Stack**: `Plus Jakarta Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 76px`, `line-height: 79.04px`, `font-weight: 800`, `letter-spacing: -1.52px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 42.4px`, `font-weight: 800`, `letter-spacing: -0.8px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0a1320` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f7f8fa` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ff` | `a:hover { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#aeb8c7` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#dce2ea` | `var(--line)` in `:root` |
| **Variable Token (`--navy-2`)** | `#121e31` | `var(--navy-2)` in `:root` |
| **Variable Token (`--blue`)** | `#1d4fd8` | `var(--blue)` in `:root` |
| **Variable Token (`--blue-dark`)** | `#163faf` | `var(--blue-dark)` in `:root` |
| **Variable Token (`--brand`)** | `#3478f6` | `var(--brand)` in `:root` |
| **Variable Token (`--blue-soft`)** | `#8fb5fa` | `var(--blue-soft)` in `:root` |
| **Variable Token (`--text`)** | `#4a5566` | `var(--text)` in `:root` |
| **Variable Token (`--line-2`)** | `#cbd3df` | `var(--line-2)` in `:root` |
| **Variable Token (`--bg-soft`)** | `#f5f7fa` | `var(--bg-soft)` in `:root` |
| **Variable Token (`--chip`)** | `#f2f5f9` | `var(--chip)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--navy` | `#0a1320` | Layout / Spatial Grid Token |
| `--navy-2` | `#121e31` | Layout / Spatial Grid Token |
| `--blue` | `#1d4fd8` | Color / Atmospheric Token |
| `--blue-dark` | `#163faf` | Canvas / Surface Token |
| `--brand` | `#3478f6` | Brand / Palette Token |
| `--blue-soft` | `#8fb5fa` | Color / Atmospheric Token |
| `--text` | `#4a5566` | Typography Ink Token |
| `--muted` | `#aeb8c7` | Color / Atmospheric Token |
| `--line` | `#dce2ea` | Color / Atmospheric Token |
| `--line-2` | `#cbd3df` | Color / Atmospheric Token |
| `--bg-soft` | `#f5f7fa` | Canvas / Surface Token |
| `--bg-hero` | `#f7f8fa` | Canvas / Surface Token |
| `--chip` | `#f2f5f9` | Color / Atmospheric Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--radius` | `28px` | Elevation / Border Token |
| `--wrap` | `1180px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hd> — `web-smith-de`)**:
   - Landmark `<header class="hd">` (`1440x84px`) hosting `Internetagentur Ostwestfalen: Websit` navigation (`Referenzen · Über uns`), DOM attributes (`data-astro-cid-nen7h5rs`, `data-hd`, `data-dd-item`, `data-dd-btn`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero> — `WIR ENTWICKELN DIGITALE LÖSUNGEN D`)**:
   - Landmark `<section class="hero">` presenting display lead `WIR ENTWICKELN DIGITALE LÖSUNGEN DIE WIRKEN.` and copy excerpt *"Websites, SEO und individuelle Software für Unternehmen – schnell"* over `#ffffff` canvas and `#0a1320` ink.
3. **Primary Showcase & Content Grid (<section.mq> — `Wir entwickeln digitale Lösungen d`)**:
   - Landmark `<section class="mq">` rendering section `Wir entwickeln digitale Lösungen die wirken .` with copy *"Webdesign, Webentwicklung, SEO & SEA, Branding, Apps & APIs, KI-L"*, asset references (`favicon.ico`, `favicon.svg`, `favicon-32.png`, `favicon-192.png`), and grid rule `html { -webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:... }`.
4. **Interactive Detail & Feature Matrix (<section.sec> — `Alles, was dein Unternehmen online`)**:
   - Landmark `<section class="sec sec--blob">` framing `Alles, was dein Unternehmen online sichtbar macht.` and `Webentwicklung` (*"online sichtbar macht."*) with `#f7f8fa` surface cards, `#0000ff` accents, and `svg { max-width:100%;display:block }`.
5. **Colophon & Global Directory Footer (<footer.ft> — `https://web-smith.de`)**:
   - Landmark `<footer class="ft">` anchoring `Internetagentur Ostwestfalen: We` footer links (`Referenzen · Über uns`), copy *"Moderne Websites, Shops und Systeme – schnell, sicher und ge"*, and `#dce2ea` structural dividers.
