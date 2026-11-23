---
title: "UI & UX Architecture: fontsight-xyz"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: fontsight-xyz

## Overview & Design Identity
- **Target**: `fontsight-xyz` (**Fontsight: What Font Is That? Font Finder for Chrome**)
- **Production URL**: [https://fontsight.xyz/](https://fontsight.xyz/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffd84a` / `#ffff00`)
- **Summary**: What font is that? Point at any text to see the typeface that actually rendered, who made it, and the CSS to use it. A free font finder f...
- **Total Clean CSS Variables Extracted**: `42` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 164.16px`, `line-height: 164.16px`, `font-weight: 400`); CSS variables `--display: "Bricolage Grotesque", "Inter", system-ui, sans-serif`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 109.44px`, `line-height: 98.496px`, `font-weight: 800`, `letter-spacing: -1.6416px`); rule `.h2` (`font-size: clamp(44px,6.4vw,104px)`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`); rule `p` (`font-size: 15.5px`, `line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`); CSS variables `--mono: "Geist Mono", ui-monospace, "SF Mono", Menlo, monospace`; rule `small` (`letter-spacing: normal`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffd84a` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0b0b0c` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fffdf6` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffff00` | `.btn .tagline { background: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#ff9acd` | `var(--pink)` in `:root` |
| **Structural Hairline Border** | `#fedb5b` | `var(--card-line)` in `:root` (`f4f4f11a`) |
| **Variable Token (`--blue`)** | `#2e44ff` | `var(--blue)` in `:root` |
| **Variable Token (`--tomato`)** | `#ff5a36` | `var(--tomato)` in `:root` |
| **Variable Token (`--card`)** | `#1c1c1b` | `var(--card)` in `:root` |
| **Variable Token (`--card-well`)** | `#262625` | `var(--card-well)` in `:root` |
| **Variable Token (`--card-row`)** | `#2b2b2a` | `var(--card-row)` in `:root` |
| **Variable Token (`--card-line`)** | `#f4f4f1` | `var(--card-line)` in `:root` |
| **Variable Token (`--card-soft`)** | `#9b9a94` | `var(--card-soft)` in `:root` |
| **Variable Token (`--warn`)** | `#f2b544` | `var(--warn)` in `:root` |
| **Variable Token (`--go`)** | `#5be38a` | `var(--go)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--yellow` | `#ffd84a` | Color / Atmospheric Token |
| `--blue` | `#2e44ff` | Color / Atmospheric Token |
| `--pink` | `#ff9acd` | Typography Ink Token |
| `--tomato` | `#ff5a36` | Color / Atmospheric Token |
| `--ink` | `#0b0b0c` | Typography Ink Token |
| `--paper` | `#fffdf6` | Canvas / Surface Token |
| `--ink-2` | `#0b0b0cad` | Typography Ink Token |
| `--paper-2` | `#fffdf6db` | Canvas / Surface Token |
| `--card` | `#1c1c1b` | Color / Atmospheric Token |
| `--card-well` | `#262625` | Color / Atmospheric Token |
| `--card-row` | `#2b2b2a` | Color / Atmospheric Token |
| `--card-line` | `#f4f4f11a` | Color / Atmospheric Token |
| `--card-ink` | `#f4f4f1` | Typography Ink Token |
| `--card-soft` | `#9b9a94` | Color / Atmospheric Token |
| `--warn` | `#f2b544` | Color / Atmospheric Token |
| `--go` | `#5be38a` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `fontsight-xyz`)**:
   - Landmark `<header class="nav wrap">` (`1360x90px`) hosting `Fontsight: What Font Is That? Font F` navigation (`How it works · Fallbacks · Try on · Test drive · Foundries`), DOM attributes (`data-browser="chrome"`, `data-site="GQEJOPOH"`, `data-noinspect`, `data-store`), and stylesheet rule `img { max-width:100% }`.
2. **Hero Stage & Focal Lead (<section.hero> — `What font is that? W h a t f o n t`)**:
   - Landmark `<section class="hero">` presenting display lead `What font is that? W h a t f o n t i s t h a t ?` and copy excerpt *"Point at any text to see the typeface that actually rendered, who"* over `#ffd84a` canvas and `#0b0b0c` ink.
3. **Primary Showcase & Content Grid (<section.demo> — `Point at any text to see the typef`)**:
   - Landmark `<section class="demo">` rendering section `Point at any text to see the typeface that actua` with copy *"Add to Chrome Brave"*, asset references (`bricolage-grotesque-latin-standar...`, `inter-latin-opsz-normal.BwkfbSeq....`, `favicon.ico`, `favicon.svg`), and grid rule `html { scroll-behavior:smooth;background:var(--ink);overscroll-behavior-y:none }`.
4. **Interactive Detail & Feature Matrix (<section.fallback> — `Add to Chrome Brave`)**:
   - Landmark `<section class="fallback">` framing `Add to Chrome Brave` and `What font is that?` (*"What font is that?"*) with `#fffdf6` surface cards, `#ffff00` accents, and `selection { background:var(--ink);color:var(--yellow) }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://fontsight.xyz/`)**:
   - Landmark `<footer class="footer">` anchoring `Fontsight: What Font Is That? Fo` footer links (`How it works · Fallbacks · Try on · Test drive · Foundries`), copy *"Bricolage Grotesque ExtraBold"*, and `#fedb5b` structural dividers.
