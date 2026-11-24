---
title: "UI & UX Architecture: kindi-land"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: kindi-land

## Overview & Design Identity
- **Target**: `kindi-land` (**Kindi & Kitir — a confectionery manufacturer in Turkmenistan**)
- **Production URL**: [https://kindi.land/](https://kindi.land/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×1744px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff0000`)
- **Summary**: We have been producing crackers, cookies, and rusks for local and international markets since 2019.
- **Total Clean CSS Variables Extracted**: `118` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `customFont2`
- **Body Font Stack**: `Outfit`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 96px`, `line-height: 96px`, `font-weight: 400`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 72px`, `font-weight: 400`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#171717` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fcfcfc` | `var(--card)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0000` | `.sm-scope .sm-socials-link:hover { color: #ff0000 }` |
| **Secondary / Muted Copy** | `#707070` | `var(--sidebar-foreground)` in `:root` |
| **Structural Hairline Border** | `#dfdfdf` | `var(--border)` in `:root` |
| **Variable Token (`--popover-foreground`)** | `#525252` | `var(--popover-foreground)` in `:root` |
| **Variable Token (`--primary`)** | `#3d3dc2` | `var(--primary)` in `:root` |
| **Variable Token (`--secondary`)** | `#fdfdfd` | `var(--secondary)` in `:root` |
| **Variable Token (`--muted`)** | `#ededed` | `var(--muted)` in `:root` |
| **Variable Token (`--muted-foreground`)** | `#202020` | `var(--muted-foreground)` in `:root` |
| **Variable Token (`--destructive`)** | `#ca3214` | `var(--destructive)` in `:root` |
| **Variable Token (`--destructive-foreground`)** | `#fffcfc` | `var(--destructive-foreground)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `#fff` | Canvas / Surface Token |
| `--foreground` | `#171717` | Typography Ink Token |
| `--card` | `#fcfcfc` | Color / Atmospheric Token |
| `--card-foreground` | `#171717` | Typography Ink Token |
| `--popover` | `#fcfcfc` | Color / Atmospheric Token |
| `--popover-foreground` | `#525252` | Typography Ink Token |
| `--primary` | `#3d3dc2` | Brand / Palette Token |
| `--primary-foreground` | `#fff` | Typography Ink Token |
| `--secondary` | `#fdfdfd` | Brand / Palette Token |
| `--secondary-foreground` | `#171717` | Typography Ink Token |
| `--muted` | `#ededed` | Color / Atmospheric Token |
| `--muted-foreground` | `#202020` | Typography Ink Token |
| `--accent` | `#ededed` | Brand / Palette Token |
| `--accent-foreground` | `#202020` | Typography Ink Token |
| `--destructive` | `#ca3214` | Color / Atmospheric Token |
| `--destructive-foreground` | `#fffcfc` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.staggered-menu-header> — `kindi-land`)**:
   - Landmark `<header class="staggered-menu-header pointer-events-none">` (`1440x102px`) hosting `Kindi & Kitir — a confectionery manu` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-position="right"`, `data-index="1"`, `data-index="2"`), and stylesheet rule `font_69087933-module__VMELHW__cla... { font-family:customFont,customFont Fallback }`.
2. **Hero Stage & Focal Lead (<section.relative> — `CONFECTIONERY MANUFACTURER`)**:
   - Landmark `<section class="relative h-full">` presenting display lead `CONFECTIONERY MANUFACTURER` and copy excerpt *"We source high‑quality grains and spices to create snacks you can"* over `#ffffff` canvas and `#171717` ink.
3. **Primary Showcase & Content Grid (<section.py-24> — `confectionery manufacturer`)**:
   - Landmark `<section class="py-24 flex">` rendering section `confectionery manufacturer` with copy *"WE OFFER QUALITY PARTNERSHIP"*, asset references (`49ed31c42e0eea42.css`, `e2dcd0ad6001165c.js`, `1175336dc77a2bf9.js`, `ac3a7ffed65b3ce5.js`), and grid rule `mfont_69087933-module__VMELHW__va... { --font-custom:"customFont","customFont Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.pb-20> — `We have been producing crackers, c`)**:
   - Landmark `<section class="pb-20 relative">` framing `We have been producing crackers, cookies, and cro...` and `Every batch is tested so flavor, crunch, and fre` (*"Every batch is tested so flavor, crunch, and freshness are always"*) with `#fcfcfc` surface cards, `#ff0000` accents, and `font-face { font-family:customFont2;src:url(../media/custom2-s.p.afe4611e.woff2)form... }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://kindi.land/`)**:
   - Landmark `<footer class="relative z-10">` anchoring `Kindi & Kitir — a confectionery ` footer links (`Overview · Index · Archive · About · Contact`), copy *"From kids to grown‑ups, our products are made to be shared a"*, and `#dfdfdf` structural dividers.
