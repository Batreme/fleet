---
title: "UI & UX Architecture: phin-helenadang-work"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: phin-helenadang-work

## Overview & Design Identity
- **Target**: `phin-helenadang-work` (**PHIN PHIN · Saigon coffee, stirred by you**)
- **Production URL**: [https://phin.helenadang.work/](https://phin.helenadang.work/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4968px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffd23f` / `#ffffff`)
- **Summary**: PHIN PHIN is a made-up Saigon coffee shop. Watch your coffee drip, then stir it yourself. A concept by Helena Dang.
- **Total Clean CSS Variables Extracted**: `63` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Phudu`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 207.144px`, `line-height: 178.144px`, `font-weight: 900`, `letter-spacing: 3.10716px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 236.8px`, `line-height: 213.12px`, `font-weight: 900`, `letter-spacing: 1.184px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-body: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 800`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffd23f` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#111111` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffffff` | live computed `a` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#d7261e` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ff0000` | `.sign-lockup span { border-bottom: #ff0000 }` |
| **Variable Token (`--sign-yellow-shade`)** | `#f0a51f` | `var(--sign-yellow-shade)` in `:root` |
| **Variable Token (`--sign-red-shade`)** | `#a3170f` | `var(--sign-red-shade)` in `:root` |
| **Variable Token (`--enamel-blue`)** | `#1e4fd8` | `var(--enamel-blue)` in `:root` |
| **Variable Token (`--enamel-blue-shade`)** | `#1336a0` | `var(--enamel-blue-shade)` in `:root` |
| **Variable Token (`--tin-sky`)** | `#9fd3e6` | `var(--tin-sky)` in `:root` |
| **Variable Token (`--tin-sky-shade`)** | `#62a9c6` | `var(--tin-sky-shade)` in `:root` |
| **Variable Token (`--coffee`)** | `#5b2a12` | `var(--coffee)` in `:root` |
| **Variable Token (`--coffee-shade`)** | `#3a1708` | `var(--coffee-shade)` in `:root` |
| **Variable Token (`--caramel`)** | `#a8653a` | `var(--caramel)` in `:root` |
| **Variable Token (`--caramel-shade`)** | `#7e4524` | `var(--caramel-shade)` in `:root` |
| **Variable Token (`--milk`)** | `#fff1b8` | `var(--milk)` in `:root` |
| **Variable Token (`--milk-shade`)** | `#f2d77c` | `var(--milk-shade)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--sign-yellow` | `#ffd23f` | Color / Atmospheric Token |
| `--sign-yellow-shade` | `#f0a51f` | Color / Atmospheric Token |
| `--sign-red` | `#d7261e` | Color / Atmospheric Token |
| `--sign-red-shade` | `#a3170f` | Color / Atmospheric Token |
| `--enamel-blue` | `#1e4fd8` | Color / Atmospheric Token |
| `--enamel-blue-shade` | `#1336a0` | Color / Atmospheric Token |
| `--tin-sky` | `#9fd3e6` | Color / Atmospheric Token |
| `--tin-sky-shade` | `#62a9c6` | Color / Atmospheric Token |
| `--ink` | `#111` | Typography Ink Token |
| `--coffee` | `#5b2a12` | Color / Atmospheric Token |
| `--coffee-shade` | `#3a1708` | Color / Atmospheric Token |
| `--caramel` | `#a8653a` | Color / Atmospheric Token |
| `--caramel-shade` | `#7e4524` | Color / Atmospheric Token |
| `--milk` | `#fff1b8` | Color / Atmospheric Token |
| `--milk-shade` | `#f2d77c` | Color / Atmospheric Token |
| `--white` | `#fff` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `phin-helenadang-work`)**:
   - Landmark `<header class="site-header">` (`1440x88px`) hosting `PHIN PHIN · Saigon coffee, stirred b` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-js-only`, `data-from="sign-yellow"`, `data-to="tin-sky"`, `data-from="tin-sky"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.beat> — `PHIN PHIN`)**:
   - Landmark `<section class="beat beat-sign">` presenting display lead `PHIN PHIN` and copy excerpt *"Chuyên bán: đen đá · sữa đá · bạc xỉu"* over `#ffd23f` canvas and `#111111` ink.
3. **Primary Showcase & Content Grid (<section.beat-brew> — `Good coffee takes four minutes.`)**:
   - Landmark `<section class="beat beat-brew">` rendering section `Good coffee takes four minutes.` with copy *"330/2 Hẻm Mèo kính mời"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `index-BrMebdgu.js`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.beat-stir> — `Now stir. Like you mean it.`)**:
   - Landmark `<section class="beat beat-stir">` framing `Now stir. Like you mean it.` and `Pick your poison. (It's coffee.)` (*"Saigon coffee. Brewed slow, stirred by you."*) with `#ffffff` surface cards, `#ffffff` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.wrap> — `https://phin.helenadang.work/`)**:
   - Landmark `<footer class="wrap site-footer">` anchoring `PHIN PHIN · Saigon coffee, stirr` footer links (`Overview · Index · Archive · About · Contact`), copy *"Every cup drips through a little steel hat called a phin . Y"*, and `#ff0000` structural dividers.
