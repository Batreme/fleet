---
title: "UI & UX Architecture: grail-app-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: grail-app-com

## Overview & Design Identity
- **Target**: `grail-app-com` (**Grail: Real-world quests, every day**)
- **Production URL**: [https://grail-app.com/](https://grail-app.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#c9a24a`)
- **Summary**: Grail pulls you out of autopilot with one real-world quest a day. Grow four stats: Strength, Intellect, Charisma, Wisdom. When you gradua...
- **Total Clean CSS Variables Extracted**: `84` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Pangaia`
- **Body Font Stack**: `Switzer`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 145.377px`, `line-height: 127.932px`, `font-weight: 300`, `letter-spacing: -1.45377px`); rule `h1` (`font-size: 44px`, `line-height: 1.05`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: normal`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 14px`, `line-height: 1.45`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-mono: "SF Mono", ui-monospace, "Menlo", monospace`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1c1c1e` | `var(--shell-text)` in `:root` |
| **Interactive Accent / Highlight** | `#c9a24a` | `var(--accent)` in `:root` |
| **Secondary / Muted Copy** | `#71717a` | `var(--landing-text-secondary)` in `:root` |
| **Structural Hairline Border** | `#010102` | `var(--landing-border)` in `:root` (`18181b0f`) |
| **Variable Token (`--bg-secondary`)** | `#f2f2f7` | `var(--bg-secondary)` in `:root` |
| **Variable Token (`--text-secondary`)** | `#8e8e93` | `var(--text-secondary)` in `:root` |
| **Variable Token (`--text-tertiary`)** | `#c7c7cc` | `var(--text-tertiary)` in `:root` |
| **Variable Token (`--text-quaternary`)** | `#d1d1d6` | `var(--text-quaternary)` in `:root` |
| **Variable Token (`--tint`)** | `#007aff` | `var(--tint)` in `:root` |
| **Variable Token (`--destructive`)** | `#ff3b30` | `var(--destructive)` in `:root` |
| **Variable Token (`--warning`)** | `#ff9500` | `var(--warning)` in `:root` |
| **Variable Token (`--success`)** | `#34c759` | `var(--success)` in `:root` |
| **Variable Token (`--glass-bg`)** | `#fffc` | `var(--glass-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg-primary` | `#fff` | Canvas / Surface Token |
| `--bg-secondary` | `#f2f2f7` | Canvas / Surface Token |
| `--bg-grouped` | `#f2f2f7` | Canvas / Surface Token |
| `--bg-card` | `#00000008` | Canvas / Surface Token |
| `--text-primary` | `#000` | Typography Ink Token |
| `--text-secondary` | `#8e8e93` | Typography Ink Token |
| `--text-tertiary` | `#c7c7cc` | Typography Ink Token |
| `--text-quaternary` | `#d1d1d6` | Typography Ink Token |
| `--tint` | `#007aff` | Canvas / Surface Token |
| `--tint-light` | `#007aff1a` | Canvas / Surface Token |
| `--destructive` | `#ff3b30` | Color / Atmospheric Token |
| `--destructive-light` | `#ff3b301a` | Canvas / Surface Token |
| `--warning` | `#ff9500` | Color / Atmospheric Token |
| `--success` | `#34c759` | Color / Atmospheric Token |
| `--glass-bg` | `#fffc` | Canvas / Surface Token |
| `--glass-border` | `#0000000f` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `grail-app-com`)**:
   - Landmark `<header class="lenis">` (`1440x900px`) hosting `Grail: Real-world quests, every day` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-controls="true"`, `data-guild-title="true"`, `data-tile="true"`, `data-side="right"`), and stylesheet rule `._root_1bp3t_1 { color:efe9f2;font-family:var(--font-sans);--accent:c9a24a;background:000... }`.
2. **Hero Stage & Focal Lead (<section.home-root> — `RECLAIMYOURLIFE`)**:
   - Landmark `<section class="home-root">` presenting display lead `RECLAIMYOURLIFE` and copy excerpt *"One real-world quest a day. Four stats that go up when you do thi"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.sr-only> — `Everyone's out living. You're watc`)**:
   - Landmark `<section class="sr-only">` rendering section `Everyone's out living. You're watching them do it...` with copy *"Same week, over and over, until you can't tell them apart. You ke"*, asset references (`Fav.svg`, `Fav.png`, `Switzer-Variable.woff2`, `PPPangaia-Light.woff2`), and grid rule `._embed_1bp3t_12 { --accent:c9a24a;position:absolute;inset:0;overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<section> — `Same week, over and over, until yo`)**:
   - Landmark `<section>` landmark framing `Same week, over and over, until you can't tell t` and `Now there’s a clock on it. Forty-eight hours to ` (*"Now there’s a clock on it. Forty-eight hours to go do the thing, "*) with `#1c1c1e` surface cards, `#c9a24a` accents, and `._canvas_1bp3t_19 { touch-action:pan-y;width:100%;height:100%;display:block;position:absolut... }`.
5. **Colophon & Global Directory Footer (<footer> — `https://grail-app.com/`)**:
   - Landmark `<footer>` landmark anchoring `Grail: Real-world quests, every ` footer links (`Overview · Index · Archive · About · Contact`), copy *"Not 24, since a day is too easy to lose to work or weather o"*, and `#010102` structural dividers.
