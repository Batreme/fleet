---
title: "UI & UX Architecture: yoyu-design"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: yoyu-design

## Overview & Design Identity
- **Target**: `yoyu-design` (**ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サービス**)
- **Production URL**: [https://yoyu.design/](https://yoyu.design/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f6f8fb` / `#007aff`)
- **Summary**: 園の業務としくみを整え、まず余裕をつくる。その余裕を、園が大切にする保育の実現へつなげる技術支援サービスです。
- **Total Clean CSS Variables Extracted**: `95` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `IBM Plex Sans JP`
- **Body Font Stack**: `IBM Plex Sans JP`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 24px`, `line-height: 34.56px`, `font-weight: 500`, `letter-spacing: 0.48px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--pixel-small: 4px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f6f8fb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | live computed `header` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#007aff` | `:root { color: #007aff }` |
| **Secondary / Muted Copy** | `#007aff` | `:root { color: #007aff }` |
| **Structural Hairline Border** | `#ffffff` | `:disabled { border-color: #ffffff }` |
| **Variable Token (`--color-gray-dark`)** | `#858890` | `var(--color-gray-dark)` in `:root` |
| **Variable Token (`--color-gray-heavy`)** | `#e2e4ea` | `var(--color-gray-heavy)` in `:root` |
| **Variable Token (`--color-gray-middle`)** | `#edeff4` | `var(--color-gray-middle)` in `:root` |
| **Variable Token (`--color-red`)** | `#ff4130` | `var(--color-red)` in `:root` |
| **Variable Token (`--color-yellow`)** | `#eeff5a` | `var(--color-yellow)` in `:root` |
| **Variable Token (`--color-green`)** | `#00b995` | `var(--color-green)` in `:root` |
| **Variable Token (`--color-pale-blue`)** | `#99e1ff` | `var(--color-pale-blue)` in `:root` |
| **Variable Token (`--color-blue`)** | `#004261` | `var(--color-blue)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#000000` | Canvas / Surface Token |
| `--color-gray-dark` | `#858890` | Canvas / Surface Token |
| `--color-gray-heavy` | `#E2E4EA` | Brand / Palette Token |
| `--color-gray-middle` | `#EDEFF4` | Brand / Palette Token |
| `--color-gray-light` | `#F6F8FB` | Canvas / Surface Token |
| `--color-white` | `#FFFFFF` | Canvas / Surface Token |
| `--color-red` | `#FF4130` | Brand / Palette Token |
| `--color-yellow` | `#EEFF5A` | Brand / Palette Token |
| `--color-green` | `#00B995` | Brand / Palette Token |
| `--color-pale-blue` | `#99E1FF` | Brand / Palette Token |
| `--color-blue` | `#004261` | Brand / Palette Token |
| `--pixel-min` | `2px` | Dimension / Scale Token |
| `--pixel-small` | `4px` | Dimension / Scale Token |
| `--grid-unit` | `8px` | Layout / Spatial Grid Token |
| `--menu-bar-delay` | `0ms` | Motion / Easing Token |
| `--idle-big-kid-base-size` | `540px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `yoyu-design`)**:
   - Landmark `<header class="site-header is-visible">` (`1440x80px`) hosting `ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サービス` navigation (`QUICK TEST · 私たちからの提案 · サポート領域 · 事例紹介 · FAQ`), DOM attributes (`data-question-invasion-reveal-active="false"`, `data-question-invasion-reveal-start-scroll-y="2885"`, `data-question-invasion-covered="false"`, `data-question-content-visible="false"`), and stylesheet rule `.main-content { min-height:100svh }`.
2. **Hero Stage & Focal Lead (<section.first-view> — `増えすぎたツール を、ひとつに`)**:
   - Landmark `<section class="first-view">` presenting display lead `増えすぎたツール を、ひとつに` and copy excerpt *"園の余裕創出から理念実現まで、園づくりを支える技術支援サービス"* over `#f6f8fb` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.quick-test> — `\ ご利用までの流れ /`)**:
   - Landmark `<section class="quick-test is-idle">` rendering section `\ ご利用までの流れ /` with copy *"システムを導入したのになぜか時間に追われていませんか？"*, asset references (`gtm.js`, `favicon-32.png`, `favicon.svg`, `apple-touch-icon.png`), and grid rule `.idle-big-kid-overlay { translate:var(--idle-big-kid-shake-x, 0) var(--idle-big-kid-shake-y, 0) }`.
4. **Interactive Detail & Feature Matrix (<article.quick-test__panel> — `ITに詳しくない職員でも大丈夫ですか？`)**:
   - Landmark `<article class="quick-test__panel is-current">` framing `ITに詳しくない職員でも大丈夫ですか？` and `費用はどれくらいかかりますか？` (*"保育に集中できない 保育に集中できない 保育に集中できない"*) with `#ffffff` surface cards, `#007aff` accents, and `hover { box-shadow:inset 0 -2px 000 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://yoyu.design/`)**:
   - Landmark `<footer class="site-footer">` anchoring `ヨユデザ（よゆでざ）｜幼稚園・保育園・認定こども園の技術支援サー` footer links (`QUICK TEST · 私たちからの提案 · サポート領域 · 事例紹介 · FAQ`), copy *"園児情報を書き写すまいにち 園児情報を書き写すまいにち 園児情報を書き写すまいにち"*, and `#ffffff` structural dividers.
