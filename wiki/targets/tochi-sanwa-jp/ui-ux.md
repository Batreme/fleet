---
title: "UI & UX Architecture: tochi-sanwa-jp"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: tochi-sanwa-jp

## Overview & Design Identity
- **Target**: `tochi-sanwa-jp` (**岐阜県美濃加茂市でおしゃれな新築一戸建てはサンワ｜ワガママ採用率100%の工務店**)
- **Production URL**: [https://tochi-sanwa.jp/](https://tochi-sanwa.jp/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f2eee9` canvas, `#393533` ink, `#e17738` accent)
- **Summary**: サンワ（SANWA）は岐阜県美濃加茂市で注文住宅・建売分譲・規格住宅を手がけています。自社土地×自社一貫施工を活かしたコストパフォーマンス◎のおしゃれな住まいをご提案。どんな難しいご要望にも「どうすれば実現できるか」を本気で考えます。
- **Total Clean CSS Variables Extracted**: `149` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `TsukuOldGothicStd-B`
- **Body Font Stack**: `TsukuOldGothicStd-B`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 14.1667px`, `line-height: 19.8333px`, `font-weight: 700`, `letter-spacing: 0.425px`); CSS variables `--font-en-display: "Yellowtail", cursive`, `--display-lg: 160`, `--display-lg-sp: 80`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 60px`, `font-weight: 800`, `letter-spacing: 1.8px`)
- **Body Copy**: live computed `body` (`font-size: 14.1667px`, `line-height: 25.5px`, `font-weight: 800`, `letter-spacing: 0.425px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14.1667px`, `line-height: 25.5px`, `font-weight: 800`, `letter-spacing: 0.425px`); rule `.label` (`font-size: 0.875rem`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f2eee9` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#393533` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#5bb2d0` | live computed `hr` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#e17738` | `var(--clr-primary-default)` in `:root` |
| **Secondary / Muted Copy** | `#5bb2d0` | live computed `hr` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#00a0d2` | `.wpcf7 form .wpcf7-response-output { border: #00a0d2 }` |
| **Variable Token (`--leap-project-main`)** | `#0073aa` | `var(--leap-project-main)` in `:root` |
| **Variable Token (`--leap-project-text-primary`)** | `#404044` | `var(--leap-project-text-primary)` in `:root` |
| **Variable Token (`--leap-project-wh`)** | `#ffffff` | `var(--leap-project-wh)` in `:root` |
| **Variable Token (`--leap-project-bg`)** | `#f7f7f4` | `var(--leap-project-bg)` in `:root` |
| **Variable Token (`--leap-project-mono-01`)** | `#f2f2f2` | `var(--leap-project-mono-01)` in `:root` |
| **Variable Token (`--leap-project-mono-02`)** | `#babdc4` | `var(--leap-project-mono-02)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--leap-project-main` | `var(--clr-primary-default, #0073aa)` | Color / Atmospheric Token |
| `--leap-project-text-primary` | `var(--clr-text-primary, #404044)` | Typography Ink Token |
| `--leap-project-wh` | `var(--clr-wht, #fff)` | Color / Atmospheric Token |
| `--leap-project-bg` | `var(--clr-bg-01, #F7F7F4)` | Canvas / Surface Token |
| `--leap-project-mono-01` | `var(--clr-mono-01, #F2F2F2)` | Typography / Scale Token |
| `--leap-project-mono-02` | `var(--clr-mono-03, #BABDC4)` | Typography / Scale Token |
| `--leap-project-bold` | `var(--font-weight-bold, 600)` | Design System Custom Token |
| `--leap-project-radius-none` | `0` | Elevation / Border Token |
| `--leap-project-radius-default` | `var(--border-radius-primary, .5rem)` | Elevation / Border Token |
| `--leap-project-radius-max` | `var(--border-radius-max, 100vmax)` | Elevation / Border Token |
| `--fz-pc` | `16` | Elevation / Border Token |
| `--fz-sp` | `14` | Elevation / Border Token |
| `--rem-pc` | `calc(1 / var(--fz-pc) * 1rem)` | Dimension / Scale Token |
| `--rem-sp` | `calc(1 / var(--fz-sp) * 1rem)` | Dimension / Scale Token |
| `--inner-xs` | `720` | Design System Custom Token |
| `--inner-sm` | `960` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `tochi-sanwa-jp`)**:
   - Landmark `<header class="header">` (`1392x68px`) hosting `岐阜県美濃加茂市でおしゃれな新築一戸建てはサンワ｜ワガママ採用率100%` navigation (`サンワの家づくり · ローコストができる理由 · 家づくりの流れ · コンセプト・約束 · サンワの住宅性能`), DOM attributes (`data-target="tochi-sanwa-jp"`), and stylesheet rule `.wpcf7-back { float:left;margin-top:5px;position:relative;width:70px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `岐阜で注文住宅、規格、分譲を手掛ける工務店`)**:
   - Landmark `<section class="hero scroll_active">` presenting display lead `岐阜で注文住宅、規格、分譲を手掛ける工務店` and copy excerpt *"1,000万円後半〜の家づくり。注文も、規格・セミオーダーも、分譲建売も。"* over `#f2eee9` canvas and `#393533` ink.
3. **Primary Showcase & Content Grid (<section.home_event> — `EVENT LIST イベント情報`)**:
   - Landmark `<section class="home_event section_pdg-sm">` rendering section `EVENT LIST イベント情報` with copy *"1,000万円後半〜 の家づくり。 注文も、規格・セミオーダーも、分譲建売も。"*, asset references (`gtm.js`, `embed`, `styles.css`, `cf7msm.css`), and grid rule `.cf7msm-ro { white-space:pre-wrap }`.
4. **Interactive Detail & Feature Matrix (<article.post> — `THANKS CAMPAIGN 開催！！`)**:
   - Landmark `<article class="post">` framing `THANKS CAMPAIGN 開催！！` and `おうちづくり応援！10000円分ギフトカードがもらえる【予約制】` (*"サンワは背伸びしない価格で、家族のうち色をカタチにします。"*) with `#5bb2d0` surface cards, `#e17738` accents, and `.wpcf7 .hidden-fields-container { display: none; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://tochi-sanwa.jp/`)**:
   - Landmark `<footer class="footer">` anchoring `岐阜県美濃加茂市でおしゃれな新築一戸建てはサンワ｜ワガママ採用率` footer links (`サンワの家づくり · ローコストができる理由 · 家づくりの流れ · コンセプト・約束 · サンワの住宅性能`), copy *"CONCEPT サンワの家づくりのコンセプト"*, and `#00a0d2` structural dividers.
