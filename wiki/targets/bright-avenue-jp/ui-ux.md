---
title: "UI & UX Architecture: bright-avenue-jp"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: bright-avenue-jp

## Overview & Design Identity
- **Target**: `bright-avenue-jp` (**株式会社ブライトアベニュー · 不動産買取再販事業・リノベーション事業**)
- **Production URL**: [https://bright-avenue.jp/](https://bright-avenue.jp/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1280×828px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#609aae` / `#0000ff`)
- **Summary**: 株式会社ブライトアベニューは、関東エリアを中心に不動産買取再販サービスを展開しています。
- **Total Clean CSS Variables Extracted**: `154` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `YakuHanJP`
- **Body Font Stack**: `YakuHanJP`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: observed font-size ladder: `24px`, `18px`, `14px`, `210px`, `10px`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: 32.4px`, `font-weight: 400`); rule `h2` (`font-size: 3rem`, `line-height: 1.4`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 14px`, `font-weight: 400`); rule `p` (`font-size: 1.4rem`, `line-height: 1.75`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 14px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#609aae` | live computed `section` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h2` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ff` | `.c-btn._bgBlue { background: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#afa3a3` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#4e4d4d` | `var(--top-line-reveal-color)` in `:root` |
| **Variable Token (`--color-text`)** | `#333333` | `var(--color-text)` in `:root` |
| **Variable Token (`--color-background`)** | `#f6f6f6` | `var(--color-background)` in `:root` |
| **Variable Token (`--color-beige-1`)** | `#d9d4d4` | `var(--color-beige-1)` in `:root` |
| **Variable Token (`--color-beige-2`)** | `#e3d3d3` | `var(--color-beige-2)` in `:root` |
| **Variable Token (`--color-gray-1`)** | `#ededed` | `var(--color-gray-1)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--scrollbar-width` | `15px` | Layout / Spatial Grid Token |
| `--bottom-offset` | `1px` | Dimension / Scale Token |
| `--line-width` | `1px` | Layout / Spatial Grid Token |
| `--window-width` | `calc(100vw - var(--scrollbar-width))` | Layout / Spatial Grid Token |
| `--grid-outer` | `4rem` | Layout / Spatial Grid Token |
| `--grid-outer-sp` | `1.5rem` | Layout / Spatial Grid Token |
| `--grid-gap` | `4rem` | Layout / Spatial Grid Token |
| `--five-column-grid--liquid` | `calc((100% - var(--grid-gap) * 4) / 5)` | Layout / Spatial Grid Token |
| `--color-text` | `#333333` | Typography Ink Token |
| `--color-background` | `#f6f6f6` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-beige-1` | `#D9D4D4` | Brand / Palette Token |
| `--color-beige-2` | `#e3d3d3` | Brand / Palette Token |
| `--color-beige-3` | `#afa3a3` | Brand / Palette Token |
| `--color-blue-1` | `#609aae` | Brand / Palette Token |
| `--color-gray-1` | `#ededed` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Persistent Left Sidebar Navigation (<aside.p-top-case__filter> — `306×846px` at `x=40`)**:
   - Fixed/sticky left rail `<aside class="p-top-case__filter u-scrollBar-hidden">` (`306px` wide) paired with top bar `<header class="l-header is-nav-white">` hosting `株式会社ブライトアベニュー · 不動産買取再販事業・リノベー` navigation (`会 会 社 社 情 情 報 報 · 販 販 売 売 実 実 績 績 · 事 事 業 業 内 内 容 容 · お お 知 知 ら ら せ せ · 採 採 用 用 情 情 報 報`), DOM attributes (`data-nav="company"`, `data-header-hover-rotate-bound="true"`, `data-nav="feature"`, `data-header-hover-rotate-bound="true"`), and rule `body { margin:0;padding:0;border:none }`.
2. **Hero Stage & Focal Lead (<section.p-top-fv> — `断熱リノベーションで 中古マンションの価値を塗り替える`)**:
   - Landmark `<section class="p-top-fv">` inside `1425px` main stage presenting display lead `断熱リノベーションで 中古マンションの価値を塗り替える` and copy excerpt *"B R I G H T A V E N U E F O R W A R D W I D T H H O P E ."* over `#609aae` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.p-top-message> — `断熱リノベーションで 中古マンションの 価値を塗り替える`)**:
   - Landmark `<section class="p-top-message">` rendering section `断熱リノベーションで 中古マンションの 価値を塗り替える` with copy *"B r i g h t A v e n u e F o r w a r d W i d t h H o p e ."*, asset references (`favicon.png`, `top_fv-poster-sp.avif`, `top_fv-poster-blur-frame.webp`, `fonts.googleapis.com`), and grid rule `section { margin:0;padding:0;border:0;list-style-type:none }`.
4. **Interactive Detail & Feature Matrix (<section.p-top-service> — `2. リノベーション事業`)**:
   - Landmark `<section class="p-top-service">` framing `2. リノベーション事業` and `私たちの特徴 私たちの特徴` (*"都内マンションの仕入れ・高断熱リノベーション・再販を通じて、 取引に関わるすべての方の期待に応えてきました。 どんな物件にも誠実に"*) with `#dddddd` surface cards, `#0000ff` accents, and `table { border:none;border-collapse:collapse;border-spacing:0 }`.
5. **Colophon & Global Directory Footer (<footer.l-footer> — `https://bright-avenue.jp/`)**:
   - Landmark `<footer class="l-footer">` anchoring `株式会社ブライトアベニュー · 不動産買取再販事業・リノベーショ` footer links (`会 会 社 社 情 情 報 報 · 販 販 売 売 実 実 績 績 · 事 事 業 業 内 内 容 容 · お お 知 知 ら ら せ せ · 採 採 用 用 情 情 報 報`), copy *"都内マンションの仕入れ・高断熱リノベーション・再販を通じて、"*, and `#4e4d4d` structural dividers.
