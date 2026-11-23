---
title: "UI & UX Architecture: www-vibr-studio"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-vibr-studio

## Overview & Design Identity
- **Target**: `www-vibr-studio` (**Vibr — Figma to code for designers who ship**)
- **Production URL**: [https://www.vibr.studio/](https://www.vibr.studio/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#faf6ec` / `#586aea`)
- **Summary**: Your design is the code. Vibr compiles your Figma file into a responsive Next.js site you own, edit with Claude Code or Codex and ship. J...
- **Total Clean CSS Variables Extracted**: `87` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Onest`
- **Body Font Stack**: `grain`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80px`, `line-height: 72px`, `font-weight: 900`); CSS variables `--m-h1: 32px`, `--m-h1-lh: 1.1`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60.048px`, `line-height: 60.048px`, `font-weight: 600`, `letter-spacing: -1.5012px`); CSS variables `--m-h2: 24px`, `--m-h2-lh: 1.2`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--m-body: 16px`, `--m-body-lh: 1.4`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#faf6ec` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f5f5f7` | `var(--bg)` in `:root` |
| **Interactive Accent / Highlight** | `#586aea` | live computed `a` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#6e6e73` | `var(--text-secondary)` in `:root` |
| **Structural Hairline Border** | `#e6e3d9` | `var(--border)` in `:root` (`00000014`) |
| **Variable Token (`--surface`)** | `#ffffff` | `var(--surface)` in `:root` |
| **Variable Token (`--surface-hover`)** | `#e8e8ed` | `var(--surface-hover)` in `:root` |
| **Variable Token (`--text`)** | `#1d1d1f` | `var(--text)` in `:root` |
| **Variable Token (`--text-tertiary`)** | `#aeaeb2` | `var(--text-tertiary)` in `:root` |
| **Variable Token (`--accent`)** | `#6e5ce6` | `var(--accent)` in `:root` |
| **Variable Token (`--accent-hover`)** | `#5b48d4` | `var(--accent-hover)` in `:root` |
| **Variable Token (`--success`)** | `#30d158` | `var(--success)` in `:root` |
| **Variable Token (`--error`)** | `#ff453a` | `var(--error)` in `:root` |
| **Variable Token (`--coal`)** | `#40474b` | `var(--coal)` in `:root` |
| **Variable Token (`--dusty-brick`)** | `#d97070` | `var(--dusty-brick)` in `:root` |
| **Variable Token (`--warm-stone`)** | `#b8afa8` | `var(--warm-stone)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#f5f5f7` | Canvas / Surface Token |
| `--surface` | `#fff` | Canvas / Surface Token |
| `--surface-hover` | `#e8e8ed` | Canvas / Surface Token |
| `--surface-elevated` | `#fff` | Canvas / Surface Token |
| `--text` | `#1d1d1f` | Typography Ink Token |
| `--text-secondary` | `#6e6e73` | Typography Ink Token |
| `--text-tertiary` | `#aeaeb2` | Typography Ink Token |
| `--accent` | `#6e5ce6` | Brand / Palette Token |
| `--accent-hover` | `#5b48d4` | Brand / Palette Token |
| `--border` | `#00000014` | Elevation / Border Token |
| `--success` | `#30d158` | Color / Atmospheric Token |
| `--error` | `#ff453a` | Color / Atmospheric Token |
| `--sand` | `#faf6ec` | Color / Atmospheric Token |
| `--coal` | `#40474b` | Color / Atmospheric Token |
| `--dusty-brick` | `#d97070` | Color / Atmospheric Token |
| `--warm-stone` | `#b8afa8` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hero-module__sup1Jq__hero> — `www-vibr-studio`)**:
   - Landmark `<header class="hero-module__sup1Jq__hero">` (`1440x900px`) hosting `Vibr — Figma to code for designers w` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`), and stylesheet rule `.about-me-module__qpLcqW__headlin... { width:100%;display:block }`.
2. **Hero Stage & Focal Lead (<main.landing-page-module__p_mWBW__page> — `VIBR : FIGMA TO CODE FOR DESIGNERS`)**:
   - Landmark `<main class="landing-page-module__p_mWBW__page">` presenting display lead `VIBR : FIGMA TO CODE FOR DESIGNERS WHO SHIP` and copy excerpt *"Your design is the code - Your design is the code - Your design i"* over `#faf6ec` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<main.landing-page-module__p_mWBW__page:nth(2)> — `Vibr : Figma to code for designers`)**:
   - Landmark `<main class="landing-page-module__p_mWBW__page">` rendering section `Vibr : Figma to code for designers who ship` with copy *"Your design is the code -"*, asset references (`83afe278b6a6bb3c-s.p.3a6ba036.woff2`, `8780dfd0812b997c-s.p.5704523e.woff2`, `8800dfc60902df36-s.p.d48c4d68.woff2`, `Grain_Variable_Trial-s.p.2731fd70...`), and grid rule `.about-me-module__qpLcqW__authorIcon { flex-shrink:0;width:22px;height:22px;position:relative }`.
4. **Interactive Detail & Feature Matrix (<main.landing-page-module__p_mWBW__page:nth(3)> — `Vibr starts with your actual desig`)**:
   - Landmark `<main class="landing-page-module__p_mWBW__page">` framing `Vibr starts with your actual design.` and `Figma Build your sections` (*": Figma to code for designers who ship"*) with `#f5f5f7` surface cards, `#586aea` accents, and `.about-me-module__qpLcqW__authorG... { width:62.5%;height:62.5%;position:absolute;top:18.87%;left:18.75%;overfl... }`.
5. **Colophon & Global Directory Footer (<footer.landing-footer-module__8-2yDa__root> — `https://www.vibr.studio/`)**:
   - Landmark `<footer class="landing-footer-module__8-2yDa__root">` anchoring `Vibr — Figma to code for designe` footer links (`Overview · Index · Archive · About · Contact`), copy *"Vibr Studio came out of years of handoff frustration. I got "*, and `#e6e3d9` structural dividers.
