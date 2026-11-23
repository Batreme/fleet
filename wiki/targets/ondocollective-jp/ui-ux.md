---
title: "UI & UX Architecture: ondocollective-jp"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: ondocollective-jp

## Overview & Design Identity
- **Target**: `ondocollective-jp` (**Ondo Collective**)
- **Production URL**: [https://ondocollective.jp/](https://ondocollective.jp/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f3e5de` / `#008000`)
- **Summary**: Ondo Collectiveは、ブランドの背景にある文脈を読み解き、理念やコンセプトの言語化からロゴ・キービジュアル・Webまでを一貫して手がけるクリエイティブ・コレクティブです。東京を拠点に、ブランドの世界観づくりを支援します。
- **Total Clean CSS Variables Extracted**: `56` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Ondo-96e094e12386a431`
- **Body Font Stack**: `Gen Interface JP-aa1df9adf44a6d02`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 57.6px`, `font-weight: 400`, `letter-spacing: -0.96px`); rule `.title` (`font-size: var(--title-font-size)`, `line-height: 1.2`, `letter-spacing: -.02em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 59.6572px`, `line-height: 71.5886px`, `font-weight: 400`, `letter-spacing: -1.19314px`)
- **Body Copy**: live computed `body` (`font-size: 14.4px`, `line-height: 16.56px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14.4px`, `line-height: 16.56px`, `font-weight: 400`); CSS variables `--letter-spacing-base: .03em`; rule `.label` (`font-size: 14rem`, `line-height: 1.2`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f3e5de` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#003c26` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.l-footer { background: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#008000` | `.c-copy-button__label { background: green }` (`#008000`) |
| **Secondary / Muted Copy** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#d5cac4` | `var(--color-border-gray)` in `:root` |
| **Variable Token (`--color-deep-green`)** | `#002c1c` | `var(--color-deep-green)` in `:root` |
| **Variable Token (`--color-error`)** | `#a3402c` | `var(--color-error)` in `:root` |
| **Variable Token (`--color-filter-black`)** | `#0009` | `var(--color-filter-black)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--col-gap` | `20rem` | Layout / Spatial Grid Token |
| `--grid-padding` | `24rem` | Layout / Spatial Grid Token |
| `--grid-repeat` | `12` | Layout / Spatial Grid Token |
| `--poppins` | `var(--font-poppins)` | Design System Custom Token |
| `--ondo` | `var(--font-ondo)` | Design System Custom Token |
| `--gen-interface` | `var(--font-gen-interface)` | Design System Custom Token |
| `--shippori-mincho` | `var(--font-shippori-mincho)` | Dimension / Scale Token |
| `--letter-spacing-base` | `.03em` | Typography / Scale Token |
| `--line-height-base` | `1.85` | Typography / Scale Token |
| `--color-text-white` | `#fff` | Canvas / Surface Token |
| `--color-bg-white` | `#f3e5de` | Canvas / Surface Token |
| `--color-green` | `#003c26` | Brand / Palette Token |
| `--color-deep-green` | `#002c1c` | Brand / Palette Token |
| `--color-border-gray` | `#d5cac4` | Brand / Palette Token |
| `--color-error` | `#a3402c` | Brand / Palette Token |
| `--color-filter-black` | `#0009` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.l-header> — `ondocollective-jp`)**:
   - Landmark `<header class="l-header">` (`1440x131px`) hosting `Ondo Collective` navigation (`Home Home · Projects Projects · Visuals Visuals · Contact Contact`), DOM attributes (`data-color="white"`, `data-visible="false"`, `data-menu="closed"`, `data-hover="fade"`), and stylesheet rule `after { box-sizing:inherit }`.
2. **Hero Stage & Focal Lead (<section.p-home-mv> — `We weave context`)**:
   - Landmark `<section class="p-home-mv">` presenting display lead `We weave context` and copy excerpt *"Before it becomes words, there are traces — unseen, unnamed, yet "* over `#f3e5de` canvas and `#003c26` ink.
3. **Primary Showcase & Content Grid (<section.p-home-philosophy> — `Before it becomes words`)**:
   - Landmark `<section class="p-home-philosophy">` rendering section `Before it becomes words` with copy *"事業の背景、歴史、温度。 まだ言葉になっていない違和感や、 静かに漂う気配。 私たちは、そのかけらを拾い集め、 ひとつの文脈へと編"*, asset references (`gtm.js`, `favicon.ico`, `icon-96x96.png`, `icon-32x32.png`), and grid rule `html { -webkit-text-size-adjust:100%;-webkit-tap-highlight-color:transparent;li... }`.
4. **Interactive Detail & Feature Matrix (<section.p-home-introduction> — `Introduction`)**:
   - Landmark `<section class="p-home-introduction">` framing `Introduction` and `About Ondo Collective` (*"文脈から、ブランドの世界観を立ち上げる クリエイティブ・コレクティブ"*) with `#ffffff` surface cards, `#008000` accents, and `main { display:block }`.
5. **Colophon & Global Directory Footer (<footer.l-footer> — `https://ondocollective.jp/`)**:
   - Landmark `<footer class="l-footer">` anchoring `Ondo Collective` footer links (`Home Home · Projects Projects · Visuals Visuals · Contact Contact`), copy *"想いや価値観、これまでの歩み、関わってきた人たちとのつながり。 そうしたひとつひとつの積み重ねが、ブランドらしさを形づく"*, and `#d5cac4` structural dividers.
