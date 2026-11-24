---
title: "UI & UX Architecture: awmedia-marketing"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: awmedia-marketing

## Overview & Design Identity
- **Target**: `awmedia-marketing` (**AW Media & Marketing · UK Web Design Studio**)
- **Production URL**: [https://awmedia.marketing/](https://awmedia.marketing/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#f5f5f7` ink, `#ffffff` accent)
- **Summary**: Award-winning web design for ambitious UK businesses. Sheffield-based, UK-wide. Bespoke when the project demands it, AI-accelerated when...
- **Total Clean CSS Variables Extracted**: `65` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Rethink Sans`
- **Body Font Stack**: `Rethink Sans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 152.64px`, `line-height: 137.376px`, `font-weight: 700`, `letter-spacing: -8.3952px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 89.28px`, `line-height: 87.4944px`, `font-weight: 600`, `letter-spacing: -4.0176px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: clamp(38px,4.6vw,72px)`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: 16.5px`, `line-height: 1.62`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f5f5f7` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#111111` | `var(--card-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#ffffff` | `.cta-title.nf-num { background: #ffffff }` |
| **Secondary / Muted Copy** | `#888888` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#1a1a1a` | `var(--card-border)` in `:root` |
| **Variable Token (`--foreground`)** | `#ededed` | `var(--foreground)` in `:root` |
| **Variable Token (`--pink-dark`)** | `#d4d4d9` | `var(--pink-dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `#000` | Canvas / Surface Token |
| `--foreground` | `#ededed` | Typography Ink Token |
| `--pink` | `#fff` | Typography Ink Token |
| `--pink-dark` | `#d4d4d9` | Canvas / Surface Token |
| `--card-bg` | `#111` | Canvas / Surface Token |
| `--card-border` | `#1a1a1a` | Elevation / Border Token |
| `--muted` | `#888` | Color / Atmospheric Token |
| `--bg` | `#000` | Canvas / Surface Token |
| `--ink` | `#f5f5f7` | Typography Ink Token |
| `--ink-2` | `#f5f5f7a8` | Typography Ink Token |
| `--ink-3` | `#f5f5f76b` | Typography Ink Token |
| `--line` | `#ffffff17` | Color / Atmospheric Token |
| `--maxw` | `1280px` | Dimension / Scale Token |
| `--gutter` | `clamp(20px,4.6vw,64px)` | Layout / Spatial Grid Token |
| `--ease` | `cubic-bezier(.16,1,.3,1)` | Motion / Easing Token |
| `--r-xl` | `32px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `awmedia-marketing`)**:
   - Landmark `<header class="nav">` (`1440x60px`) hosting `AW Media & Marketing · UK Web Design` navigation (`How We Work · Industries · About · Blog`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-liquid="cursor"`, `data-liquid="pill"`), and stylesheet rule `.cta.nf { min-height:100svh;padding:calc(var(--nav-h) + 9vh) 0 12vh;place-items:ce... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Designed properly. Built faster.`)**:
   - Landmark `<section class="hero">` presenting display lead `Designed properly. Built faster.` and copy excerpt *"An award-⁠winning UK studio shipping bespoke websites at AI-⁠acce"* over `#000000` canvas and `#f5f5f7` ink.
3. **Primary Showcase & Content Grid (<section.built> — `Built like this.`)**:
   - Landmark `<section class="built">` rendering section `Built like this.` with copy *"UK Web Design Studio · Since 2016"*, asset references (`0dc02305a3505331-s.p.045lmq4bb63o...`, `aw-logo.png`, `04rv9lq_~p.97.css`, `0yrizplp3s9dt.css`), and grid rule `.hero-title.nf-title { letter-spacing:-.05em;margin-top:3vh;font-size:clamp(38px,4.6vw,76px);li... }`.
4. **Interactive Detail & Feature Matrix (<section.trusted> — `Award-winning design, AI-accelerat`)**:
   - Landmark `<section class="trusted">` framing `Award-winning design, AI-accelerated where it cou...` and `From idea to live. Sites that ship.` (*"Designed properly."*) with `#111111` surface cards, `#ffffff` accents, and `.hero-sub.nf-sub { max-width:520px;margin-top:28px }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://awmedia.marketing/`)**:
   - Landmark `<footer class="footer">` anchoring `AW Media & Marketing · UK Web De` footer links (`How We Work · Industries · About · Blog`), copy *"An award-winning UK studio shipping bespoke websites at AI-a"*, and `#1a1a1a` structural dividers.
