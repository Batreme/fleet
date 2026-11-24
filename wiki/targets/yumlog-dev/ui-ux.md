---
title: "UI & UX Architecture: yumlog-dev"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: yumlog-dev

## Overview & Design Identity
- **Target**: `yumlog-dev` (**YumLog — the calorie tracker you can talk to, for Apple Watch and iPhone**)
- **Production URL**: [https://yumlog.dev/](https://yumlog.dev/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#ffc93c` accent)
- **Summary**: Say what you ate and YumLog logs the calories, protein, carbs and fat. Voice logging on Apple Watch, chat and photos on iPhone, restauran...
- **Total Clean CSS Variables Extracted**: `31` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ui-rounded`
- **Body Font Stack**: `SF Pro Text`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 100px`, `line-height: 92px`, `font-weight: 900`, `letter-spacing: -3.5px`); CSS variables `--display: ui-rounded, "SF Pro Rounded", "Nunito", system-ui, sans-serif`; rule `h1` (`font-size: clamp(52px, 7vw, 100px)`, `line-height: 0.92`, `letter-spacing: -0.035em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 92px`, `line-height: 90.16px`, `font-weight: 900`, `letter-spacing: -2.3px`); rule `h2` (`font-size: clamp(40px, 5.4vw, 72px)`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 26.35px`, `font-weight: 400`); rule `p` (`font-size: 20px`, `line-height: 1.6`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 23.25px`, `font-weight: 600`); rule `.label` (`font-size: 12px`, `line-height: 1.25`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e7e8fb` | `var(--panel)` in `:root` |
| **Interactive Accent / Highlight** | `#ffc93c` | `var(--pineapple)` in `:root` |
| **Secondary / Muted Copy** | `#6f6d85` | `var(--ink-3)` in `:root` |
| **Structural Hairline Border** | `#e8e8ea` | `var(--line)` in `:root` (`rgb(29 27 44 / 0.1)`) |
| **Variable Token (`--coral`)** | `#f2533a` | `var(--coral)` in `:root` |
| **Variable Token (`--coral-deep`)** | `#e53e30` | `var(--coral-deep)` in `:root` |
| **Variable Token (`--coral-light`)** | `#ff8d6b` | `var(--coral-light)` in `:root` |
| **Variable Token (`--nori`)** | `#10231b` | `var(--nori)` in `:root` |
| **Variable Token (`--nori-2`)** | `#1b3a2d` | `var(--nori-2)` in `:root` |
| **Variable Token (`--salmon`)** | `#ff8a5c` | `var(--salmon)` in `:root` |
| **Variable Token (`--donut`)** | `#ffc3d6` | `var(--donut)` in `:root` |
| **Variable Token (`--melon`)** | `#1f7a45` | `var(--melon)` in `:root` |
| **Variable Token (`--night`)** | `#131119` | `var(--night)` in `:root` |
| **Variable Token (`--ink`)** | `#1d1b2c` | `var(--ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ground` | `#fff` | Color / Atmospheric Token |
| `--coral` | `#f2533a` | Color / Atmospheric Token |
| `--coral-deep` | `#e53e30` | Color / Atmospheric Token |
| `--coral-light` | `#ff8d6b` | Canvas / Surface Token |
| `--pineapple` | `#ffc93c` | Color / Atmospheric Token |
| `--nori` | `#10231b` | Color / Atmospheric Token |
| `--nori-2` | `#1b3a2d` | Color / Atmospheric Token |
| `--salmon` | `#ff8a5c` | Color / Atmospheric Token |
| `--donut` | `#ffc3d6` | Color / Atmospheric Token |
| `--melon` | `#1f7a45` | Color / Atmospheric Token |
| `--night` | `#131119` | Color / Atmospheric Token |
| `--display` | `ui-rounded, "SF Pro Rounded", "Nunito", system-ui, sans-serif` | Dimension / Scale Token |
| `--shadow-soft` | `0 1px 2px rgb(40 30 90 / 0.06), 0 8px 24px -6px rgb(40 30 90 / 0.16)` | Elevation / Border Token |
| `--shadow-lift` | `0 2px 4px rgb(40 30 90 / 0.08), 0 30px 70px -20px rgb(40 30 90 / 0.4)` | Elevation / Border Token |
| `--gutter` | `32px` | Layout / Spatial Grid Token |
| `--ink` | `#1d1b2c` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top> — `yumlog-dev`)**:
   - Landmark `<header class="top">` (`1440x72px`) hosting `YumLog — the calorie tracker you can` navigation (`How it works · Features · Rings · Questions`), DOM attributes (`data-reveal`, `data-sequence="0.5 2.6"`, `data-cycle="8"`, `data-step="1"`), and stylesheet rule `.closing { --ink: 1d1b2c; --ink-2: 4c4a60; --ink-3: 6f6d85; --line: rgb(29 27 44 /... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `The calorie tracker you can talk t`)**:
   - Landmark `<section class="hero">` presenting display lead `The calorie tracker you can talk to` and copy excerpt *"Say “two eggs and toast with butter” to your Apple Watch. Breakfa"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.facts> — `Like texting someone what you ate.`)**:
   - Landmark `<section class="facts wrap">` rendering section `Like texting someone what you ate.` with copy *"“Two eggs and toast”"*, asset references (`favicon.png`, `apple-touch-icon.png`, `home.css`, `site.js`), and grid rule `after { box-sizing: border-box; }`.
4. **Interactive Detail & Feature Matrix (<section.how> — `Two eggs and toast with butter for`)**:
   - Landmark `<section class="how wrap">` framing `Two eggs and toast with butter for breakfast.` and `Can I fit a burger and fries in for lunch?` (*"“Actually, three eggs”"*) with `#e7e8fb` surface cards, `#ffc93c` accents, and `html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://yumlog.dev/`)**:
   - Landmark `<footer class="foot">` anchoring `YumLog — the calorie tracker you` footer links (`How it works · Features · Rings · Questions`), copy *"“How’s my week going?”"*, and `#e8e8ea` structural dividers.
