---
title: "UI & UX Architecture: thenest-pl_en"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: thenest-pl_en

## Overview & Design Identity
- **Target**: `thenest-pl_en` (**The Nest — a registered business address in central Warsaw**)
- **Production URL**: [https://thenest.pl/en](https://thenest.pl/en)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4968px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#003a40` ink, `#9b7739` accent)
- **Summary**: Register your Polish company at Piękna 49 in central Warsaw. Virtual office from 109 PLN/mo net, private offices quoted individually, mai...
- **Total Clean CSS Variables Extracted**: `138` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Bodoni Moda`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 18.4px`, `line-height: 25.3px`, `font-weight: 400`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 68.8px`, `line-height: 67.424px`, `font-weight: 400`, `letter-spacing: -1.376px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#003a40` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fafaf8` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#9b7739` | `var(--brand-gold)` in `:root` |
| **Secondary / Muted Copy** | `#6b7280` | `var(--muted-foreground)` in `:root` |
| **Structural Hairline Border** | `#e5e7eb` | `var(--border)` in `:root` |
| **Variable Token (`--secondary`)** | `#f5f5f5` | `var(--secondary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--brand-teal` | `#003a40` | Brand / Palette Token |
| `--brand-gold` | `#9b7739` | Brand / Palette Token |
| `--brand-white` | `#fff` | Canvas / Surface Token |
| `--background` | `#fff` | Canvas / Surface Token |
| `--foreground` | `#003a40` | Typography Ink Token |
| `--card` | `#fff` | Color / Atmospheric Token |
| `--card-foreground` | `#003a40` | Typography Ink Token |
| `--popover` | `#fff` | Color / Atmospheric Token |
| `--popover-foreground` | `#003a40` | Typography Ink Token |
| `--primary` | `#003a40` | Brand / Palette Token |
| `--primary-foreground` | `#fff` | Typography Ink Token |
| `--secondary` | `#f5f5f5` | Brand / Palette Token |
| `--secondary-foreground` | `#003a40` | Typography Ink Token |
| `--muted` | `#f5f5f5` | Color / Atmospheric Token |
| `--muted-foreground` | `#6b7280` | Typography Ink Token |
| `--accent` | `#9b7739` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-0> — `thenest-pl_en`)**:
   - Landmark `<header class="top-0 left-0">` (`1440x64px`) hosting `The Nest — a registered business add` navigation (`About Us · Offers · News & Insights · FAQ · Contact`), DOM attributes (`data-scroll-behavior="smooth"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.rd-serif { font-family:var(--font-display), "Iowan Old Style", Palatino, Georgia, s... }`.
2. **Hero Stage & Focal Lead (<section.bg-cream> — `A Warsaw business address for your`)**:
   - Landmark `<section class="bg-cream relative">` presenting display lead `A Warsaw business address for your company. Piękn...` and copy excerpt *"An address at Piękna 49 for your KRS or CEIDG registration — a vi"* over `#ffffff` canvas and `#003a40` ink.
3. **Primary Showcase & Content Grid (<section.text-teal> — `Register your company at a real ad`)**:
   - Landmark `<section class="bg-cream text-teal">` rendering section `Register your company at a real address.` with copy *"Register your company"*, asset references (`7665c2bcc9077b83-s.p.3nqaju0iyo2m...`, `cd9c266256ef2177-s.p.0ia0bwd-fjee...`, `thenest-logo-white.svg`, `2qf24jap9hfz0.css`), and grid rule `.rd-rule { border-color:var(--rd-rule) }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Everything under one address. Offi`)**:
   - Landmark `<section class="relative overflow-hidden">` framing `Everything under one address. Office , mail , roo...` and `Office to rent — once you outgrow the virtual office` (*"at a real address."*) with `#fafaf8` surface cards, `#9b7739` accents, and `.rd-rule-strong { border-color:var(--rd-rule-strong) }`.
5. **Colophon & Global Directory Footer (<footer.border-border> — `https://thenest.pl/en`)**:
   - Landmark `<footer class="border-border bg-background">` anchoring `The Nest — a registered business` footer links (`About Us · Offers · News & Insights · FAQ · Contact`), copy *"Used by more than 500 companies since 2018, including founde"*, and `#e5e7eb` structural dividers.
