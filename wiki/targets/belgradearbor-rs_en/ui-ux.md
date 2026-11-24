---
title: "UI & UX Architecture: belgradearbor-rs_en"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: belgradearbor-rs_en

## Overview & Design Identity
- **Target**: `belgradearbor-rs_en` (**Belgrade Arbor · Residential & Business Complex in New Belgrade**)
- **Production URL**: [https://belgradearbor.rs/en](https://belgradearbor.rs/en)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fdfbef` / `#e7fd55`)
- **Summary**: Discover Belgrade Arbor - premium apartments and business spaces in New Belgrade. Explore residences, amenities, location, and availability.
- **Total Clean CSS Variables Extracted**: `61` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `editorialOld`
- **Body Font Stack**: `Apple Color Emoji`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 151.2px`, `line-height: 151.2px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 239.76px`, `line-height: 239.76px`, `font-weight: 300`)
- **Body Copy**: live computed `body` (`font-size: 15.984px`, `line-height: 23.976px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15.984px`, `line-height: 23.976px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fdfbef` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#2e3a26` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--card)` in `:root` |
| **Interactive Accent / Highlight** | `#e7fd55` | `.bg-accent { background-color: #e7fd55 }` |
| **Secondary / Muted Copy** | `#737373` | `var(--muted-foreground)` in `:root` |
| **Structural Hairline Border** | `#e5e5e5` | `var(--border)` in `:root` |
| **Variable Token (`--card-foreground`)** | `#0a0a0a` | `var(--card-foreground)` in `:root` |
| **Variable Token (`--primary`)** | `#171717` | `var(--primary)` in `:root` |
| **Variable Token (`--primary-foreground`)** | `#fafafa` | `var(--primary-foreground)` in `:root` |
| **Variable Token (`--secondary`)** | `#f5f5f5` | `var(--secondary)` in `:root` |
| **Variable Token (`--destructive`)** | `#e40014` | `var(--destructive)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--radius` | `.625rem` | Elevation / Border Token |
| `--background` | `var(--color-vanilla)` | Canvas / Surface Token |
| `--foreground` | `var(--color-pine-green)` | Typography Ink Token |
| `--card` | `#fff` | Color / Atmospheric Token |
| `--card-foreground` | `#0a0a0a` | Typography Ink Token |
| `--popover` | `#fff` | Color / Atmospheric Token |
| `--popover-foreground` | `#0a0a0a` | Typography Ink Token |
| `--primary` | `#171717` | Brand / Palette Token |
| `--primary-foreground` | `#fafafa` | Typography Ink Token |
| `--secondary` | `#f5f5f5` | Brand / Palette Token |
| `--secondary-foreground` | `#171717` | Typography Ink Token |
| `--muted` | `#f5f5f5` | Color / Atmospheric Token |
| `--muted-foreground` | `#737373` | Typography Ink Token |
| `--accent` | `#f5f5f5` | Brand / Palette Token |
| `--accent-foreground` | `#171717` | Typography Ink Token |
| `--destructive` | `#e40014` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.mt-12> — `belgradearbor-rs_en`)**:
   - Landmark `<nav class="mt-12 flex">` (`220x431px`) hosting `Belgrade Arbor · Residential & Busin` navigation (`Home Home · Business Business · Location Location · Amenities Amenities · Contact Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-cookieconsent="ignore"`), and stylesheet rule `.VqkbDq_className { font-family:Work Sans,Work Sans Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.relative> — `BELGRADE ARBOR`)**:
   - Landmark `<section class="relative">` presenting display lead `BELGRADE ARBOR` and copy excerpt *"BELGRADE ARBOR DESIGN"* over `#fdfbef` canvas and `#2e3a26` ink.
3. **Primary Showcase & Content Grid (<section.introduction-mobile> — `Belgrade Arbor`)**:
   - Landmark `<section class="introduction-mobile relative">` rendering section `Belgrade Arbor` with copy *"B E L G R A D E A R B O R D E S I G N"*, asset references (`0kbue0j55e2ep.css`, `2l_3j-qfad4j4.css`, `2zlpkz7lx5tcy.css`, `07bpw61iauvjs.js`), and grid rule `.VqkbDq_variable { --font-workSans:"Work Sans", "Work Sans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.z-1> — `The visual identity of Belgrade Ar`)**:
   - Landmark `<section class="z-1 relative">` framing `The visual identity of Belgrade Arbor is defined...` and `Belgrade Arbor isn't just another addition to the...` (*"Explore in 3d Explore in 3d"*) with `#ffffff` surface cards, `#e7fd55` accents, and `.UoXJ4a_className { font-family:editorialOld,editorialOld Fallback }`.
5. **Colophon & Global Directory Footer (<footer.to-vanilla> — `https://belgradearbor.rs/en`)**:
   - Landmark `<footer class="to-vanilla bg-linear-to-t">` anchoring `Belgrade Arbor · Residential & B` footer links (`Home Home · Business Business · Location Location · Amenities Amenities · Contact Contact`), copy *"A clear architectural vision, a carefully selected location,"*, and `#e5e5e5` structural dividers.
