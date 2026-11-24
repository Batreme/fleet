---
title: "UI & UX Architecture: www-memedia-de"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-memedia-de

## Overview & Design Identity
- **Target**: `www-memedia-de` (**Webdesign München für nachhaltig denkende Unternehmer**)
- **Production URL**: [https://www.memedia.de](https://www.memedia.de)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1a1a1a` ink, `#f03714` accent)
- **Summary**: Die Web-Experten für nachhaltig denkende Unternehmer: Strategie, Konzeption, Design und Umsetzung aus München. Websites, die Anfragen bri...
- **Total Clean CSS Variables Extracted**: `62` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 112px`, `line-height: 112px`, `font-weight: 600`, `letter-spacing: -3.92px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 53.76px`, `font-weight: 600`, `letter-spacing: -0.72px`); CSS variables `--fs-h2: clamp(2rem,1.6rem + 1.556vw,3rem)`, `--fs-h2-s: clamp(1.625rem,1.3rem + 1vw,2.25rem)`; rule `h2` (`font-size: 1rem`, `font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 28.8px`, `font-weight: 400`); CSS variables `--fs-body: clamp(1.0625rem,1rem + .15vw,1.125rem)`; rule `p` (`font-size: var(--fs-body)`, `line-height: 1.6`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 28.8px`, `font-weight: 400`); CSS variables `--fs-small: .9375rem`, `--fs-label: .8125rem`; rule `.meta` (`font-size: var(--fs-small)`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1a1a1a` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f4f4f2` | `var(--surface-2)` in `:root` |
| **Interactive Accent / Highlight** | `#f03714` | `var(--brand)` in `:root` |
| **Secondary / Muted Copy** | `#666665` | `var(--ink-muted)` in `:root` |
| **Structural Hairline Border** | `#d8d8d6` | `var(--line)` in `:root` |
| **Variable Token (`--muted-on-dark`)** | `#b4b4b3` | `var(--muted-on-dark)` in `:root` |
| **Variable Token (`--label-on-dark`)** | `#9a9a99` | `var(--label-on-dark)` in `:root` |
| **Variable Token (`--line-soft`)** | `#ececea` | `var(--line-soft)` in `:root` |
| **Variable Token (`--line-dark`)** | `#414140` | `var(--line-dark)` in `:root` |
| **Variable Token (`--surface-3`)** | `#eaeae8` | `var(--surface-3)` in `:root` |
| **Variable Token (`--cta`)** | `#e0320f` | `var(--cta)` in `:root` |
| **Variable Token (`--brand-text`)** | `#c42a0c` | `var(--brand-text)` in `:root` |
| **Variable Token (`--coral`)** | `#ff9d80` | `var(--coral)` in `:root` |
| **Variable Token (`--lime`)** | `#e6f84a` | `var(--lime)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#1a1a1a` | Typography Ink Token |
| `--ink-muted` | `#666665` | Typography Ink Token |
| `--ink-inverse` | `#ffffff` | Typography Ink Token |
| `--muted-on-dark` | `#b4b4b3` | Canvas / Surface Token |
| `--label-on-dark` | `#9a9a99` | Canvas / Surface Token |
| `--line` | `#d8d8d6` | Color / Atmospheric Token |
| `--line-soft` | `#ececea` | Color / Atmospheric Token |
| `--line-dark` | `#414140` | Canvas / Surface Token |
| `--surface` | `#ffffff` | Canvas / Surface Token |
| `--surface-2` | `#f4f4f2` | Canvas / Surface Token |
| `--surface-3` | `#eaeae8` | Canvas / Surface Token |
| `--brand` | `#f03714` | Brand / Palette Token |
| `--cta` | `#e0320f` | Brand / Palette Token |
| `--brand-text` | `#c42a0c` | Typography Ink Token |
| `--coral` | `#ff9d80` | Color / Atmospheric Token |
| `--lime` | `#e6f84a` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-memedia-de`)**:
   - Landmark `<header class="site-header">` (`1440x98px`) hosting `Webdesign München für nachhaltig den` navigation (`Alle Leistungen · Konzeption & UX · Design · Umsetzung · Betreuung & Support`), DOM attributes (`data-bereich="/leistungen/"`, `data-bereich="/technologien/"`, `data-bereich="/produkte/ /web-check..."`, `data-bereich="/referenzen/"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.wp-block-group> — `Die Web-Experten für nachhaltig de`)**:
   - Landmark `<section class="wp-block-group hero">` presenting display lead `Die Web-Experten für nachhaltig denkende Unterneh...` and copy excerpt *"NICHT IRGENDEINE WEBSITE."* over `#ffffff` canvas and `#1a1a1a` ink.
3. **Primary Showcase & Content Grid (<section.intro> — `Was willst du eigentlich? Eine sch`)**:
   - Landmark `<section class="wp-block-group intro">` rendering section `Was willst du eigentlich? Eine schöne Website?` with copy *"Die Web-Experten für"*, asset references (`poppins-latin-600-normal.woff2`, `poppins-latin-500-normal.woff2`, `favicon.svg`, `apple-touch-icon.png`), and grid rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100%;scroll-behavior:smoo... }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Du willst eine hübsche Website?`)**:
   - Landmark `<section class="wp-block-group section">` framing `Du willst eine hübsche Website?` and `Du willst eine technisch optimierte Website?` (*"nachhaltig denkende"*) with `#f4f4f2` surface cards, `#f03714` accents, and `video { display:block;max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.gr-foot> — `https://www.memedia.de`)**:
   - Landmark `<footer class="gr-foot">` anchoring `Webdesign München für nachhaltig` footer links (`Alle Leistungen · Konzeption & UX · Design · Umsetzung · Betreuung & Support`), copy *"Nicht irgendeine Website."*, and `#d8d8d6` structural dividers.
