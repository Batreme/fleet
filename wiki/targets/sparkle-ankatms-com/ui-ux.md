---
title: "UI & UX Architecture: sparkle-ankatms-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: sparkle-ankatms-com

## Overview & Design Identity
- **Target**: `sparkle-ankatms-com` (**Kids Reward Chart & Chore App · Sparkle**)
- **Production URL**: [https://sparkle.ankatms.com](https://sparkle.ankatms.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fbfaf6` / `#ff3b30`)
- **Summary**: Organize tasks, earn stars and choose rewards together. Sparkle is a private reward-chart app for families and groups on iPhone and iPad....
- **Total Clean CSS Variables Extracted**: `31` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `SF Pro Display`
- **Body Font Stack**: `SF Pro Display`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 123.1px`, `line-height: 103.404px`, `font-weight: 820`, `letter-spacing: -7.1398px`); rule `h1` (`font-size: clamp(2.3rem,4.5vw,4rem)`, `line-height: 1.15`, `letter-spacing: -.035em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 84.96px`, `line-height: 79.8624px`, `font-weight: 800`, `letter-spacing: -4.248px`); rule `h2` (`font-size: clamp(1.6rem,3vw,2.3rem)`, `line-height: 1.3`, `letter-spacing: -.025em`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 26.35px`, `font-weight: 400`); rule `p` (`font-size: .9rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14.4px`, `line-height: 21.6px`, `font-weight: 500`); rule `small` (`font-size: 13px`, `font-weight: 650`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fbfaf6` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1c1736` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | live computed `p` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff3b30` | `.ctl-badge.is-hot { background: #ff3b30 }` |
| **Secondary / Muted Copy** | `#b85f00` | `var(--amber-ink)` in `:root` |
| **Structural Hairline Border** | `#e3dfef` | `.search-steps li { border: #e3dfef }` |
| **Variable Token (`--ink-2`)** | `#48425f` | `var(--ink-2)` in `:root` |
| **Variable Token (`--ink-3`)** | `#68637d` | `var(--ink-3)` in `:root` |
| **Variable Token (`--violet`)** | `#6b4ff0` | `var(--violet)` in `:root` |
| **Variable Token (`--violet-2`)** | `#8d75ff` | `var(--violet-2)` in `:root` |
| **Variable Token (`--gold`)** | `#f5a623` | `var(--gold)` in `:root` |
| **Variable Token (`--gold-2`)** | `#ffcf4a` | `var(--gold-2)` in `:root` |
| **Variable Token (`--rose`)** | `#e2478f` | `var(--rose)` in `:root` |
| **Variable Token (`--mint`)** | `#22c55e` | `var(--mint)` in `:root` |
| **Variable Token (`--night-ink`)** | `#f5f2ff` | `var(--night-ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#1c1736` | Typography Ink Token |
| `--ink-2` | `#48425f` | Typography Ink Token |
| `--ink-3` | `#68637d` | Typography Ink Token |
| `--paper` | `#fbfaf6` | Canvas / Surface Token |
| `--violet` | `#6b4ff0` | Color / Atmospheric Token |
| `--violet-2` | `#8d75ff` | Color / Atmospheric Token |
| `--gold` | `#f5a623` | Color / Atmospheric Token |
| `--gold-2` | `#ffcf4a` | Color / Atmospheric Token |
| `--amber-ink` | `#b85f00` | Typography Ink Token |
| `--rose` | `#e2478f` | Color / Atmospheric Token |
| `--mint` | `#22c55e` | Color / Atmospheric Token |
| `--night-ink` | `#f5f2ff` | Typography Ink Token |
| `--sky-top` | `rgb(255 247 236)` | Color / Atmospheric Token |
| `--sky-bottom` | `rgb(244 238 255)` | Color / Atmospheric Token |
| `--glow-a` | `rgb(255 214 168 / 0.6)` | Color / Atmospheric Token |
| `--glow-b` | `rgb(203 184 255 / 0.6)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `sparkle-ankatms-com`)**:
   - Landmark `<header class="nav">` (`1440x76px`) hosting `Kids Reward Chart & Chore App · Spar` navigation (`English · Deutsch · Español · Français · Türkçe`), DOM attributes (`data-nav`, `data-logo`, `data-hud`, `data-hud-count`), and stylesheet rule `.search-languages a { color:inherit;text-decoration:underline;text-underline-offset:.2em }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Stars Today. Habits Tomorrow.`)**:
   - Landmark `<section class="hero">` presenting display lead `Stars Today. Habits Tomorrow.` and copy excerpt *"A reward-chart app for families and groups"* over `#fbfaf6` canvas and `#1c1736` ink.
3. **Primary Showcase & Content Grid (<section.scene> — `S t a r s T o d a y . H a b i t s `)**:
   - Landmark `<section class="scene scene--tasks">` rendering section `S t a r s T o d a y . H a b i t s T o m o r r o w .` with copy *"Sparkle turns everyday tasks into stars children can see, collect"*, asset references (`favicon-32.png`, `apple-touch-icon.png`, `avatar-luca.jpg`, `sparkle-story.css`), and grid rule `.search-page img { display:block;max-width:100%;height:auto }`.
4. **Interactive Detail & Feature Matrix (<article.tcard> — `Everyday tasks become achievements`)**:
   - Landmark `<article class="tcard">` framing `Everyday tasks become achievements.` and `Write something` (*"Watch the film 0:30"*) with `#ffffff` surface cards, `#ff3b30` accents, and `.search-page a { color:4c3fba;text-underline-offset:.2em }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://sparkle.ankatms.com`)**:
   - Landmark `<footer class="foot">` anchoring `Kids Reward Chart & Chore App · ` footer links (`English · Deutsch · Español · Français · Türkçe`), copy *"Get Moving 30 minutes of movement. Sport, dance… 30 min 3 st"*, and `#e3dfef` structural dividers.
