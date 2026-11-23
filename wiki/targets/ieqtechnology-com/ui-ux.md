---
title: "UI & UX Architecture: ieqtechnology-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: ieqtechnology-com

## Overview & Design Identity
- **Target**: `ieqtechnology-com` (**IEQ Technology · Innovation. Experience. Quality.**)
- **Production URL**: [https://ieqtechnology.com/](https://ieqtechnology.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0a0a0a` ink, `#0d91d0` accent)
- **Summary**: Managed IT, legacy system modernization, custom software and custom websites from a 100% U.S.-based team in Springfield, Oregon. Since 2011.
- **Total Clean CSS Variables Extracted**: `51` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cabin`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 108px`, `line-height: 99.36px`, `font-weight: 600`, `letter-spacing: -3.24px`); CSS variables `--font-display: "Cabin","Geist",ui-sans-serif,system-ui,sans-serif`; rule `h1` (`font-size: 34px`, `letter-spacing: -.03em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 61.2px`, `font-weight: 600`, `letter-spacing: -2.1px`); rule `.h2` (`font-size: clamp(40px,5vw,68px)`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); rule `p` (`font-size: 15px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--font-mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace`; rule `small` (`font-size: 12px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0a0a0a` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fafafa` | `var(--bg-2)` in `:root` |
| **Interactive Accent / Highlight** | `#0d91d0` | `var(--brand)` in `:root` |
| **Secondary / Muted Copy** | `#6b7280` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#0b80bd` | `var(--nav-line)` in `:root` |
| **Variable Token (`--ieq-teal`)** | `#074a6a` | `var(--ieq-teal)` in `:root` |
| **Variable Token (`--ieq-navy`)** | `#003e71` | `var(--ieq-navy)` in `:root` |
| **Variable Token (`--ieq-tint`)** | `#e1eff6` | `var(--ieq-tint)` in `:root` |
| **Variable Token (`--ieq-tint-2`)** | `#d5ebf6` | `var(--ieq-tint-2)` in `:root` |
| **Variable Token (`--bg-3`)** | `#f4f6f8` | `var(--bg-3)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif` | Typography / Scale Token |
| `--font-display` | `"Cabin","Geist",ui-sans-serif,system-ui,sans-serif` | Typography / Scale Token |
| `--font-mono` | `"Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace` | Typography / Scale Token |
| `--r-sm` | `6px` | Dimension / Scale Token |
| `--r-lg` | `16px` | Dimension / Scale Token |
| `--ease` | `cubic-bezier(.2,.7,.1,1)` | Motion / Easing Token |
| `--max` | `1440px` | Dimension / Scale Token |
| `--nav-h` | `76px` | Layout / Spatial Grid Token |
| `--ieq-blue` | `#0d91d0` | Color / Atmospheric Token |
| `--ieq-teal` | `#074a6a` | Color / Atmospheric Token |
| `--ieq-navy` | `#003e71` | Layout / Spatial Grid Token |
| `--ieq-tint` | `#e1eff6` | Canvas / Surface Token |
| `--ieq-tint-2` | `#d5ebf6` | Canvas / Surface Token |
| `--bg` | `#fff` | Canvas / Surface Token |
| `--bg-2` | `#fafafa` | Canvas / Surface Token |
| `--bg-3` | `#f4f6f8` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `ieqtechnology-com`)**:
   - Landmark `<header class="nav scrolled">` (`1440x77px`) hosting `IEQ Technology · Innovation. Experie` navigation (`About · Services · All services · Our Work · Awards`), DOM attributes (`data-theme="light"`, `data-k="nw"`, `data-k="ne"`, `data-k="sw"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Innovation. Experience. Quality. T`)**:
   - Landmark `<section class="hero">` presenting display lead `Innovation. Experience. Quality. THAT'S IEQ TECHN...` and copy excerpt *"Managed IT, legacy system modernization, custom software, and web"* over `#ffffff` canvas and `#0a0a0a` ink.
3. **Primary Showcase & Content Grid (<section.block> — `I nnovation. E xperience. Q uality`)**:
   - Landmark `<section class="block">` rendering section `I nnovation. E xperience. Q uality. That's IEQ Te...` with copy *"Business of the Year"*, asset references (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `sitemap.xml`), and grid rule `html { scroll-behavior:smooth;-webkit-text-size-adjust:100% }`.
4. **Interactive Detail & Feature Matrix (<section.block:nth(2)> — `Four core services. One dedicated `)**:
   - Landmark `<section class="block">` framing `Four core services. One dedicated local team.` and `Managed IT Services` (*"Springfield Chamber"*) with `#fafafa` surface cards, `#0d91d0` accents, and `svg { display:block }`.
5. **Colophon & Global Directory Footer (<footer.site-foot> — `https://ieqtechnology.com/`)**:
   - Landmark `<footer class="site-foot block">` anchoring `IEQ Technology · Innovation. Exp` footer links (`About · Services · All services · Our Work · Awards`), copy *"Q uality. That's IEQ Technology."*, and `#0b80bd` structural dividers.
