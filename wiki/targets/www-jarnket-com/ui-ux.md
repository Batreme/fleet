---
title: "UI & UX Architecture: www-jarnket-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-jarnket-com

## Overview & Design Identity
- **Target**: `www-jarnket-com` (**JarnKet · Ketsadaphone Boutpanyda, web engineer in Vientiane**)
- **Production URL**: [https://www.jarnket.com/](https://www.jarnket.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5f5f5` / `#2563eb`)
- **Summary**: Software engineer in Vientiane, Laos and WorldSkills ASEAN 2025 Web Technologies Expert, building fast, accessible React and Next.js inte...
- **Total Clean CSS Variables Extracted**: `87` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Chakra Petch`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 151.176px`, `line-height: 123.965px`, `font-weight: 600`, `letter-spacing: -3.02353px`); CSS variables `--font-display: "Chakra Petch", "Chakra Petch Fallback"`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 129.6px`, `line-height: 111.456px`, `font-weight: 600`, `letter-spacing: -1.944px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-geist-mono: "Geist Mono", "Geist Mono Fallback"`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f5f5` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1a1a1a` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f4f5f7` | `var(--jk-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#2563eb` | `var(--site-accent)` in `:root` |
| **Secondary / Muted Copy** | `#62666e` | `var(--jk-muted)` in `:root` |
| **Structural Hairline Border** | `#d7d9dc` | `var(--jk-line)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `0 0% 96%` | Canvas / Surface Token |
| `--foreground` | `0 0% 10%` | Typography Ink Token |
| `--card` | `0 0% 98%` | Dimension / Scale Token |
| `--card-foreground` | `0 0% 10%` | Typography Ink Token |
| `--popover` | `0 0% 98%` | Dimension / Scale Token |
| `--popover-foreground` | `0 0% 10%` | Typography Ink Token |
| `--primary` | `0 0% 10%` | Brand / Palette Token |
| `--primary-foreground` | `0 0% 96%` | Typography Ink Token |
| `--secondary` | `0 0% 92%` | Brand / Palette Token |
| `--secondary-foreground` | `0 0% 10%` | Typography Ink Token |
| `--muted` | `0 0% 91%` | Dimension / Scale Token |
| `--muted-foreground` | `0 0% 40%` | Typography Ink Token |
| `--accent` | `0 0% 90%` | Brand / Palette Token |
| `--accent-foreground` | `0 0% 10%` | Typography Ink Token |
| `--destructive` | `0 72% 48%` | Dimension / Scale Token |
| `--destructive-foreground` | `0 0% 96%` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `www-jarnket-com`)**:
   - Landmark `<header class="inset-x-0 top-0">` (`1440x73px`) hosting `JarnKet · Ketsadaphone Boutpanyda, w` navigation (`Index · Work · Field notes · Gallery · GitHub`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/immutab..."`, `data-sdkn="@vercel/analytics/react"`, `data-sdkv="2.0.1"`), and stylesheet rule `._8NX9hq_className { font-family:Geist,Geist Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.relative> — `JARN KET`)**:
   - Landmark `<section class="relative">` presenting display lead `JARN KET` and copy excerpt *"Ketsadaphone Boutpanyda — building fast, accessible interfaces wi"* over `#f5f5f5` canvas and `#1a1a1a` ink.
3. **Primary Showcase & Content Grid (<section.jk-flood> — `J A R N K E T`)**:
   - Landmark `<section class="jk-flood pb-28">` rendering section `J A R N K E T` with copy *"Web Technologies Expert @ WorldSkills ASEAN 2025"*, asset references (`1ccf8ef962b3f693-s.p.2xt4dxqx4hw9...`, `797e433ab948586e-s.p.1v5bejj26fx9...`, `8457265da2739722-s.p.00okbctd204v...`, `caa3a2e1cccd8315-s.p.0zr6hhvz-h9n...`), and grid rule `._8NX9hq_variable { --font-geist:"Geist", "Geist Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.relative:nth(2)> — `T o o l k i t`)**:
   - Landmark `<section class="relative">` framing `T o o l k i t` and `UI & Styling` (*"Web Techologies Expert @World Skills ASEAN 2025 Software Engineer"*) with `#f4f5f7` surface cards, `#2563eb` accents, and `.z61v7q_className { font-family:Geist Mono,Geist Mono Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.jk-flood> — `https://www.jarnket.com/`)**:
   - Landmark `<footer class="jk-flood relative">` anchoring `JarnKet · Ketsadaphone Boutpanyd` footer links (`Index · Work · Field notes · Gallery · GitHub`), copy *"Web Techologies Expert @World Skills ASEAN 2025"*, and `#d7d9dc` structural dividers.
