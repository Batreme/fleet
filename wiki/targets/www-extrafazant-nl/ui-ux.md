---
title: "UI & UX Architecture: www-extrafazant-nl"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-extrafazant-nl

## Overview & Design Identity
- **Target**: `www-extrafazant-nl` (**Extrafazant · Social Content, Video's & Animatie**)
- **Production URL**: [https://www.extrafazant.nl/](https://www.extrafazant.nl/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f4f4f4` canvas, `#101010` ink, `#0038ff` accent)
- **Summary**: Creatives die je merk in beweging brengen. Animatie, film en social content die blijft hangen. Snel schakelen, meedenken, geen lang burea...
- **Total Clean CSS Variables Extracted**: `166` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Helvetica Now Subset`
- **Body Font Stack**: `Helvetica Now Subset`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 144px`, `line-height: 115.2px`, `font-weight: 700`, `letter-spacing: -2.88px`); rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 96px`, `line-height: 76.8px`, `font-weight: 500`, `letter-spacing: -1.92px`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: 16.8px`, `font-weight: 500`, `letter-spacing: -0.48px`); CSS variables `--_paragraphs---paragraph-regular--font: var(--_fonts---fonts--paragraph)`, `--_theme---body-text: var(--_colors---swatch--black)`, `--_paragraphs---paragraph-regular--line-height: 1.4em`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 16.8px`, `font-weight: 500`, `letter-spacing: -0.48px`); CSS variables `--_headings---heading-xxl--letter-spacing: -.02em`, `--_headings---heading-xl--letter-spacing: -.02em`, `--_headings---heading-l--letter-spacing: -.02em`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f4f4` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#101010` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--button-052-color-background)` in `:root` |
| **Interactive Accent / Highlight** | `#0038ff` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#ff77cd` | `var(--_colors---swatch--pink)` in `:root` |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_theme---background` | `var(--_colors---swatch--off-white)` | Canvas / Surface Token |
| `--_paragraphs---paragraph-regular--font` | `var(--_fonts---fonts--paragraph)` | Typography / Scale Token |
| `--_theme---body-text` | `var(--_colors---swatch--black)` | Typography Ink Token |
| `--_paragraphs---paragraph-regular--line-height` | `1.4em` | Typography / Scale Token |
| `--_paragraphs---paragraph-regular--font-weight` | `var(--_fonts---font-weight--medium)` | Typography / Scale Token |
| `--_fonts---fonts--heading` | `"Helvetica Now Subset", Arial, sans-serif` | Typography Ink Token |
| `--_headings---heading-xxl--font-size` | `var(--_sizes---size--192px)` | Typography Ink Token |
| `--_headings---heading-xxl--line-height` | `.8em` | Typography Ink Token |
| `--_headings---heading-xxl--font-weight` | `var(--_fonts---font-weight--bold)` | Typography Ink Token |
| `--_headings---heading-xxl--letter-spacing` | `-.02em` | Typography Ink Token |
| `--_headings---heading-xl--font` | `var(--_fonts---fonts--heading)` | Typography Ink Token |
| `--_headings---heading-xl--font-size` | `var(--_sizes---size--128px)` | Typography Ink Token |
| `--_headings---heading-xl--font-weight` | `var(--_fonts---font-weight--bold)` | Typography Ink Token |
| `--_headings---heading-xl--letter-spacing` | `-.02em` | Typography Ink Token |
| `--_headings---heading-l--font` | `var(--_fonts---fonts--heading)` | Typography Ink Token |
| `--_headings---heading-l--font-size` | `var(--_sizes---size--96px)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.section_hero> — `www-extrafazant-nl`)**:
   - Landmark `<header class="section_hero">` (`1440x900px`) hosting `Extrafazant · Social Content, Video'` navigation (`Ontdek meer`), DOM attributes (`data-wf-domain="www.extrafazant.nl"`, `data-wf-page="6a7eba014f1644e9f15be500"`, `data-wf-site="6a7eba014f1644e9f15be52d"`, `data-page-ready`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.section_intro> — `BRENGT JE MERK IN BEWEGING`)**:
   - Landmark `<section class="section_intro">` presenting display lead `BRENGT JE MERK IN BEWEGING` and copy excerpt *"Geen loggggg bureauproces. Wij zijn een club makers die snel scha"* over `#f4f4f4` canvas and `#101010` ink.
3. **Primary Showcase & Content Grid (<section.section_featured> — `B r e n g t j e m e r k i n b e w `)**:
   - Landmark `<section class="section_featured theme-dark">` rendering section `B r e n g t j e m e r k i n b e w e g i n g` with copy *"Ontdek meer over ons"*, asset references (`cdn.prod.website-files.com`, `extrafazant-demo.webflow.shared.8...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section_services> — `De creatives van Extrafazant`)**:
   - Landmark `<section class="section_services">` framing `De creatives van Extrafazant` and `R e c e n t W e r k` (*"Zeg waar je mee zit. Wij maken het zichtbaar."*) with `#ffffff` surface cards, `#0038ff` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.extrafazant.nl/`)**:
   - Landmark `<footer class="footer theme-dark">` anchoring `Extrafazant · Social Content, Vi` footer links (`Ontdek meer`), copy *"Vooruit met je verhaal"*, and `#e2e2e2` structural dividers.
