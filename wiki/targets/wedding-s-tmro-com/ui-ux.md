---
title: "UI & UX Architecture: wedding-s-tmro-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: wedding-s-tmro-com

## Overview & Design Identity
- **Target**: `wedding-s-tmro-com` (**Wedding Invitation · Yuri & Tomoro**)
- **Production URL**: [https://wedding.s-tmro.com/](https://wedding.s-tmro.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f7f7f7` / `#333333`)
- **Summary**: 結婚式へのご招待です。日時は2026年11月29日（いい肉の日）、10:00に受付、10:30に開始です。会場は桜通線「国際センター」駅近くのレストラン「recipe」です。
- **Total Clean CSS Variables Extracted**: `16` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Stack Sans Notch`
- **Body Font Stack**: `Italianno`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 3em`, `font-weight: 700`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `body` (`line-height: 1`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 36px`, `line-height: 36px`, `font-weight: 400`, `letter-spacing: 0.72px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f7f7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `body { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#333333` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#333333` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#cccccc` | `hr { border-top: #cccccc }` |
| **Variable Token (`--s-color-27b6cb51`)** | `#f2f2f2` | `var(--s-color-27b6cb51)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--s-font-c796e0a2` | `'Stack Sans Notch'` | Typography / Scale Token |
| `--s-font-c89837a8` | `'Stack Sans Headline'` | Typography / Scale Token |
| `--s-font-e28f2a0c` | `'Stack Sans Text'` | Typography / Scale Token |
| `--s-font-75b0f13c` | `Italianno` | Typography / Scale Token |
| `--s-font-11bbee0d` | `'Zen Old Mincho'` | Typography / Scale Token |
| `--s-color-34930474` | `#333333ff` | Brand / Palette Token |
| `--s-color-27b6cb51` | `#f2f2f2ff` | Brand / Palette Token |
| `--s-color-c8b6c400` | `#f7f7f7ff` | Brand / Palette Token |
| `--s-color-c69a0a1a` | `rgb(240, 240, 240)` | Brand / Palette Token |
| `--s-color-54b90296` | `linear-gradient(90deg, #ffffffff, #ffffffff)` | Brand / Palette Token |
| `--s-color-eea30069` | `rgba(150, 150, 150, 0)` | Brand / Palette Token |
| `--s-color-e2b900cc` | `#333333` | Brand / Palette Token |
| `--img-current` | `var(--img-small)` | Design System Custom Token |
| `--gap-h` | `0px` | Layout / Spatial Grid Token |
| `--gap-v` | `0px` | Layout / Spatial Grid Token |
| `--ha` | `1` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `wedding-s-tmro-com`)**:
   - Landmark `<header class="lenis">` (`1440px`) hosting `Wedding Invitation · Yuri & Tomoro` navigation (`@recipe · MESSAGE · INFORMATION · YOUR REPLY · @recipe @recipe`), DOM attributes (`data-appear`, `data-inited-appear`, `data-sd-img-src="https://storage.googl..."`, `data-sd-img-src="https://storage.googl..."`), and stylesheet rule `html.lenis body { height: auto; }`.
2. **Hero Stage & Focal Lead (<section.section> — `Wedding Invitation · Yuri & Tomoro`)**:
   - Landmark `<section class="section">` presenting display lead `Wedding Invitation · Yuri & Tomoro` and copy excerpt *"Yuri Kunimatsu & Tomoro Sugawara Wedding Ceremony"* over `#f7f7f7` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.section:nth(2)> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="section">` rendering section `Featured Work & Interactive Showcase` with copy *"“ii-fuku-nohi” & “ii-niku-nohi”"*, asset references (`84a82c89-316b-4152-8b5a-bb944f91e1b1`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `.lenis-stopped { overflow: clip; }`.
4. **Interactive Detail & Feature Matrix (<section.section:nth(3)> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="section">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"mixture restaurant"*) with `#ffffff` surface cards, `#333333` accents, and `.lenis.lenis-smooth iframe { pointer-events: none; }`.
5. **Colophon & Global Directory Footer (<footer.section-inner> — `https://wedding.s-tmro.com/`)**:
   - Landmark `<footer class="section-inner">` anchoring `Wedding Invitation · Yuri & Tomo` footer links (`@recipe · MESSAGE · INFORMATION · YOUR REPLY · @recipe @recipe`), copy *"Good clothes Good meats Good Fortunes"*, and `#cccccc` structural dividers.
