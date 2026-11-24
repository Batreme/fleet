---
title: "UI & UX Architecture: www-blumjeffrey-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-blumjeffrey-com

## Overview & Design Identity
- **Target**: `www-blumjeffrey-com` (**Jeffrey Blum — AI Digital Creative Director**)
- **Production URL**: [https://www.blumjeffrey.com](https://www.blumjeffrey.com)
- **Final Redirected URL**: [https://blumjeffrey.com/](https://blumjeffrey.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#080808` canvas, `#f5f5f0` ink, `#378ef0` accent)
- **Summary**: Jeffrey Blum is a New York-based AI Digital Creative Director building creative systems, intelligent workflows, brand platforms, and digi...
- **Total Clean CSS Variables Extracted**: `56` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Barlow Condensed`
- **Body Font Stack**: `Barlow`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 138.24px`, `line-height: 121.651px`, `font-weight: 900`, `letter-spacing: -2.7648px`); rule `h1` (`font-size: clamp(64px,9.6vw,180px)`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 158.4px`, `line-height: 139.392px`, `font-weight: 900`, `letter-spacing: -3.168px`); rule `h2` (`font-size: clamp(64px,9vw,170px)`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 300`); rule `p` (`font-size: clamp(2rem,4vw,4rem)`, `line-height: .9`, `font-weight: 900`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 300`); CSS variables `--mono: "JetBrains Mono",ui-monospace,monospace`, `--ho-mono: "Barlow",sans-serif`; rule `small` (`font-size: .6rem`, `letter-spacing: .22em`, `font-weight: 600`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#080808` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f5f5f0` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#070707` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#378ef0` | `.home-v2 .damBtn { background: #378ef0 }` |
| **Secondary / Muted Copy** | `#888888` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#2a2a2a` | `var(--border)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--motion-instant` | `.12s` | Motion / Easing Token |
| `--motion-fast` | `.2s` | Motion / Easing Token |
| `--motion-medium` | `.3s` | Motion / Easing Token |
| `--motion-slow` | `.4s` | Motion / Easing Token |
| `--motion-reveal` | `.8s` | Motion / Easing Token |
| `--motion-hero` | `.9s` | Motion / Easing Token |
| `--motion-counter` | `1.1s` | Motion / Easing Token |
| `--motion-marquee` | `28s` | Motion / Easing Token |
| `--ease-standard` | `ease` | Motion / Easing Token |
| `--ease-linear` | `linear` | Motion / Easing Token |
| `--ease-pulse` | `ease-in-out` | Motion / Easing Token |
| `--ease-expressive` | `cubic-bezier(.16,1,.3,1)` | Motion / Easing Token |
| `--motion-shift-xs` | `4px` | Motion / Easing Token |
| `--motion-shift-sm` | `8px` | Motion / Easing Token |
| `--motion-shift-md` | `20px` | Motion / Easing Token |
| `--motion-shift-lg` | `32px` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.cs-hero> — `www-blumjeffrey-com`)**:
   - Landmark `<header class="cs-hero">` (`1440px`) hosting `Jeffrey Blum — AI Digital Creative D` navigation (`Work · Lab · Speaking · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-motion="gsap"`), and stylesheet rule `rlow_f90c7aff-module__zTBjaq__cla... { font-family:Barlow,Barlow Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.home> — `SHAPE VISION. BUILD SYSTEMS.`)**:
   - Landmark `<section class="home">` presenting display lead `SHAPE VISION. BUILD SYSTEMS.` and copy excerpt *"AI DIGITAL CREATIVE DIRECTOR · NEW YORK"* over `#080808` canvas and `#f5f5f0` ink.
3. **Primary Showcase & Content Grid (<section.home-v2> — `Shape vision. Build systems.`)**:
   - Landmark `<section class="home-v2">` rendering section `Shape vision. Build systems.` with copy *"AI Digital Creative Director · New York"*, asset references (`235a0ef330592118-s.p.b3cd1641.woff2`, `303804218d80822e-s.p.9b40bd6c.woff2`, `4f530f52d514af96-s.p.52297690.woff2`, `81cef6a21128489e-s.p.6cf41120.woff2`), and grid rule `arlow_f90c7aff-module__zTBjaq__va... { --fb:"Barlow","Barlow Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.clients-scene> — `Recent projects`)**:
   - Landmark `<section class="clients-scene">` framing `Recent projects` and `M·A·C Design System` (*"Hey, Jeffrey here. I design digital experiences and the intellige"*) with `#070707` surface cards, `#378ef0` accents, and `nsed_96399e51-module__mcdnOa__cla... { font-family:Barlow Condensed,Barlow Condensed Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.ft> — `https://www.blumjeffrey.com`)**:
   - Landmark `<footer class="ft fixed">` anchoring `Jeffrey Blum — AI Digital Creati` footer links (`Work · Lab · Speaking · About · Contact`), copy *"From Swiss watchmakers to global beauty. Digital products, c"*, and `#2a2a2a` structural dividers.
