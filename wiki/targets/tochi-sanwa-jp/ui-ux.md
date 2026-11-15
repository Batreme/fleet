# UI & UX Architecture: tochi-sanwa-jp

## Overview & Design Identity
- **Target**: `tochi-sanwa-jp` (**岐阜県美濃加茂市でおしゃれな新築一戸建てはサンワ｜ワガママ採用率100%の工務店**)
- **Production URL**: [https://tochi-sanwa.jp/](https://tochi-sanwa.jp/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#E17738` canvas, `#D03030` ink, `#EB3535` accent)
- **Summary**: サンワ（SANWA）は岐阜県美濃加茂市で注文住宅・建売分譲・規格住宅を手がけています。自社土地×自社一貫施工を活かしたコストパフォーマンス◎のおしゃれな住まいをご提案。どんな難しいご要望にも「どうすれば実現できるか」を本気で考えます。
- **Total Clean CSS Variables Extracted**: `149` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Lato`
- **Body Font Stack**: `Oswald`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-en-display: "Yellowtail", cursive`, `--display-lg: 160`, `--display-lg-sp: 80`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(12px, 1rem, 14px)`, `clamp(10px, 0.875rem, 12px)`, `0.875rem`, `1rem`, `1.125rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(12px, 1rem, 14px)`, `clamp(10px, 0.875rem, 12px)`, `0.875rem`, `1rem`, `1.125rem`)
- **Metadata & Labels**: CSS variables `--leap-project-mono-01: var(--clr-mono-01, #F2F2F2)`, `--leap-project-mono-02: var(--clr-mono-03, #BABDC4)`, `--clr-mono-01: #EEEEEE`; rule `.label` (`font-size: 0.875rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#E17738` | `var(--clr-primary-default)` in `:root` |
| **Primary Typography Ink** | `#B25722` | `var(--clr-primary-dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#E88E58` | `var(--clr-primary-light)` in `:root` |
| **Interactive Accent / Highlight** | `#EB3535` | `var(--clr-secondary-default)` in `:root` |
| **Secondary / Muted Copy** | `#D03030` | `var(--clr-secondary-dark)` in `:root` |
| **Structural Hairline Border** | `#F25353` | `var(--clr-secondary-light)` in `:root` |
| **Variable Token (`--leap-project-main`)** | `#0073aa` | `var(--leap-project-main)` in `:root` |
| **Variable Token (`--leap-project-text-primary`)** | `#404044` | `var(--leap-project-text-primary)` in `:root` |
| **Variable Token (`--leap-project-wh`)** | `#fff` | `var(--leap-project-wh)` in `:root` |
| **Variable Token (`--leap-project-bg`)** | `#F7F7F4` | `var(--leap-project-bg)` in `:root` |
| **Variable Token (`--leap-project-mono-01`)** | `#F2F2F2` | `var(--leap-project-mono-01)` in `:root` |
| **Variable Token (`--leap-project-mono-02`)** | `#BABDC4` | `var(--leap-project-mono-02)` in `:root` |

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
   - Landmark `<header class="header">` hosting `岐阜県美濃加茂市でおしゃれな新築一戸建てはサンワ｜ワガママ採用率100%` navigation (`サンワの家づくり · ローコストができる理由 · 家づくりの流れ · コンセプト・約束 · サンワの住宅性能`), DOM attributes (`data-target="tochi-sanwa-jp"`), and stylesheet rule `.wpcf7-back { float:left;margin-top:5px;position:relative;width:70px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `岐阜で注文住宅、規格、分譲を手掛ける工務店`)**:
   - Landmark `<section class="hero scroll_active">` presenting display lead `岐阜で注文住宅、規格、分譲を手掛ける工務店` and copy excerpt *"岐阜で注文住宅、規格、分譲を手掛ける工務店"* over `#E17738` canvas and `#D03030` ink.
3. **Primary Showcase & Content Grid (<section.home_event> — `EVENT LIST イベント情報`)**:
   - Landmark `<section class="home_event section_pdg-sm">` rendering section `EVENT LIST イベント情報` with copy *"サンワの家づくり CONCEPT サンワの家づくり ローコストができる理由 家づくりの流れ コンセプト・約束 サンワの住宅性能"*, asset references (`gtm.js`, `embed`, `styles.css`, `cf7msm.css`), and grid rule `.cf7msm-ro { white-space:pre-wrap }`.
4. **Interactive Detail & Feature Matrix (<article.post> — `THANKS CAMPAIGN 開催！！`)**:
   - Landmark `<article class="post">` framing `THANKS CAMPAIGN 開催！！` and `おうちづくり応援！10000円分ギフトカードがもらえる【予約制】` (*"ラインナップ LINE UP ラインナップ 注文住宅 規格・セミオーダー住宅 建売分譲"*) with `#E88E58` surface cards, `#EB3535` accents, and `.leap_table thead th { background-color: var(--leap-project-main); color: var(--leap-project-wh); }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://tochi-sanwa.jp/`)**:
   - Landmark `<footer class="footer">` anchoring `岐阜県美濃加茂市でおしゃれな新築一戸建てはサンワ｜ワガママ採用率` footer links (`サンワの家づくり · ローコストができる理由 · 家づくりの流れ · コンセプト・約束 · サンワの住宅性能`), copy *"物件・土地を探す HOME & LAND 物件・土地を探す 建売分譲を探す 土地を探す 見つける間取り"*, and `#F25353` structural dividers.
