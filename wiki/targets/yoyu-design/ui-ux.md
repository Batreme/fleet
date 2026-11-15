# UI & UX Architecture: yoyu-design

## Overview & Design Identity
- **Target**: `yoyu-design` (**ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サービス**)
- **Production URL**: [https://yoyu.design/](https://yoyu.design/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#EDEFF4`)
- **Summary**: 園の業務としくみを整え、まず余裕をつくる。その余裕を、園が大切にする保育の実現へつなげる技術支援サービスです。
- **Total Clean CSS Variables Extracted**: `95` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `DotGothic16`
- **Body Font Stack**: `IBM Plex Sans JP`
- **Monospace / Technical Font Stack**: `IBM Plex Sans JP`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `8px`, `11px`, `14px`, `4.6153846154vw`, `20px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `8px`, `11px`, `14px`, `4.6153846154vw`, `20px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `8px`, `11px`, `14px`, `4.6153846154vw`, `20px`)
- **Metadata & Labels**: CSS variables `--pixel-small: 4px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | `var(--tag-background)` in `:root` |
| **Primary Typography Ink** | `#858890` | `var(--color-gray-dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#E2E4EA` | `var(--color-gray-heavy)` in `:root` |
| **Interactive Accent / Highlight** | `#EDEFF4` | `var(--color-gray-middle)` in `:root` |
| **Secondary / Muted Copy** | `#F6F8FB` | `var(--color-gray-light)` in `:root` |
| **Structural Hairline Border** | `#FFFFFF` | `var(--color-white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--menu-bar-delay` | `0ms` | Motion / Easing Token |
| `--idle-big-kid-base-size` | `540px` | Layout / Spatial Grid Token |
| `--idle-big-kid-rest-half` | `270px` | Dimension / Scale Token |
| `--idle-big-kid-center-offset` | `-68px` | Dimension / Scale Token |
| `--idle-big-kid-floor-offset` | `128px` | Dimension / Scale Token |
| `--idle-big-kid-actions-margin` | `64px` | Layout / Spatial Grid Token |
| `--idle-big-kid-actions-height` | `84px` | Layout / Spatial Grid Token |
| `--idle-big-kid-actions-bottom-limit` | `63px` | Dimension / Scale Token |
| `--idle-big-kid-glyph-origin-x` | `50%` | Dimension / Scale Token |
| `--idle-big-kid-glyph-origin-y` | `55.5556%` | Dimension / Scale Token |
| `--idle-big-kid-reveal-delay` | `.48s` | Motion / Easing Token |
| `--idle-big-kid-reveal-stagger` | `.16s` | Motion / Timing Token |
| `--idle-big-kid-reveal-duration` | `.32s` | Motion / Easing Token |
| `--idle-big-kid-fade-duration` | `.48s` | Motion / Easing Token |
| `--idle-big-kid-heart-x` | `0px` | Dimension / Scale Token |
| `--idle-big-kid-heart-y` | `0px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `yoyu-design`)**:
   - Landmark `<header class="site-header is-visible">` hosting `ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サービス` navigation (`QUICK TEST · 私たちからの提案 · サポート領域 · 事例紹介 · FAQ`), DOM attributes (`data-question-invasion-reveal-active="false"`, `data-question-invasion-reveal-start-scroll-y="2885"`, `data-question-invasion-covered="false"`, `data-question-content-visible="false"`), and stylesheet rule `.main-content { min-height:100svh }`.
2. **Hero Stage & Focal Lead (<section.first-view> — `私たちのご提案`)**:
   - Landmark `<section class="first-view">` presenting display lead `私たちのご提案` and copy excerpt *"園の余裕創出から理念実現まで、園づくりを支える技術支援サービス"* over `#000000` canvas and `#FFFFFF` ink.
3. **Primary Showcase & Content Grid (<section.quick-test> — `サービスの大まかな流れ`)**:
   - Landmark `<section class="quick-test is-idle">` rendering section `サービスの大まかな流れ` with copy *"システムを導入したのになぜか時間に追われていませんか？"*, asset references (`gtm.js`, `favicon-32.png`, `favicon.svg`, `apple-touch-icon.png`), and grid rule `.idle-big-kid-overlay { translate:var(--idle-big-kid-shake-x, 0) var(--idle-big-kid-shake-y, 0) }`.
4. **Interactive Detail & Feature Matrix (<article.quick-test__panel> — `定例ミーティング`)**:
   - Landmark `<article class="quick-test__panel is-current">` framing `定例ミーティング` and `課題の整理` (*"保育に集中できない 保育に集中できない 保育に集中できない"*) with `#E2E4EA` surface cards, `#EDEFF4` accents, and `hover { box-shadow:inset 0 -2px 000 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://yoyu.design/`)**:
   - Landmark `<footer class="site-footer">` anchoring `ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サー` footer links (`QUICK TEST · 私たちからの提案 · サポート領域 · 事例紹介 · FAQ`), copy *"園児情報を書き写すまいにち 園児情報を書き写すまいにち 園児情報を書き写すまいにち"*, and `#FFFFFF` structural dividers.
