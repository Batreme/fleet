---
title: "UI & UX Architecture: nakagawa-corp-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: nakagawa-corp-com

## Overview & Design Identity
- **Target**: `nakagawa-corp-com` (**久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホーム）**)
- **Production URL**: [https://nakagawa-corp.com/](https://nakagawa-corp.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#202020` ink, `#333333` accent)
- **Summary**: 【1963年創業、久留米・うきはで60年以上】株式会社ナカガワ(本社:福岡県久留米市)は、真っ白な図面から一邸ずつ設計する完全自由設計の工務店です。注文住宅・分譲住宅・土地探しまで、暮らしに合わせてご提案します。
- **Total Clean CSS Variables Extracted**: `131` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Shuei KakuGo Gin M`
- **Body Font Stack**: `Shuei KakuGo Gin M`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 14.1667px`, `line-height: 19.8333px`, `font-weight: 700`, `letter-spacing: 1.13333px`); CSS variables `--font-en-display: "Cardo", serif`, `--display-lg: 160`, `--display-md: 120`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 30px`, `line-height: 48px`, `font-weight: 400`, `letter-spacing: 4.5px`)
- **Body Copy**: live computed `body` (`font-size: 14.1667px`, `line-height: 28.3333px`, `font-weight: 400`, `letter-spacing: 1.13333px`); rule `body` (`line-height: 1`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14.1667px`, `line-height: 28.3333px`, `font-weight: 400`, `letter-spacing: 1.13333px`); rule `small` (`font-size: max(12px, 0.875rem)`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#202020` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f7f7f4` | `var(--leap-project-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#333333` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#ad8a72` | `var(--clr-secondary-default)` in `:root` |
| **Structural Hairline Border** | `#cccccc` | `hr { border-top: #cccccc }` |
| **Variable Token (`--leap-project-main`)** | `#0073aa` | `var(--leap-project-main)` in `:root` |
| **Variable Token (`--leap-project-text-primary`)** | `#404044` | `var(--leap-project-text-primary)` in `:root` |
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
| `--fz` | `16` | Design System Custom Token |
| `--rem` | `calc(1 / var(--fz) * 1rem)` | Dimension / Scale Token |
| `--header-hgt` | `96` | Layout / Spatial Grid Token |
| `--header-hgt-fx` | `80` | Layout / Spatial Grid Token |
| `--inner-xs` | `720` | Design System Custom Token |
| `--inner-sm` | `1080` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `nakagawa-corp-com`)**:
   - Landmark `<header class="header header-main">` (`1425x80px`) hosting `久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホーム）` navigation (`ナカガワホームの家づくり · 私たちについて · 快適な住まいづくり · 徹底したこだわり · 家づくりの流れ・アフターサポート`), DOM attributes (`data-js-parallax`, `data-speed="-0.08"`, `data-speed="0.05"`, `data-speed="-0.12"`), and stylesheet rule `.leap_table thead th { background-color: var(--leap-project-main); color: var(--leap-project-wh); }`.
2. **Hero Stage & Focal Lead (<section.home-intro> — `あなたは出会う。 思い描く、その先の暮らしに。`)**:
   - Landmark `<section class="home-intro">` presenting display lead `あなたは出会う。 思い描く、その先の暮らしに。` and copy excerpt *"あなたは出会う。 思い描く、その先の暮らしに。"* over `#ffffff` canvas and `#202020` ink.
3. **Primary Showcase & Content Grid (<section.home-works> — `「応える」だけでなく、 「提案する」。`)**:
   - Landmark `<section class="home-works">` rendering section `「応える」だけでなく、 「提案する」。` with copy *"福岡・佐賀・大分で60年以上。 まだ言葉になっていない理想まで、形にする工務店。"*, asset references (`gtm.js`, `embed`, `front.css`, `style.css`), and grid rule `.box--ttl { font-size: var(--font-size-heading6); font-family: var(--font-jp-heading); }`.
4. **Interactive Detail & Feature Matrix (<section.home-event> — `提案のための、余白を残す。`)**:
   - Landmark `<section class="home-event section_pdg-md-top">` framing `提案のための、余白を残す。` and `いつも、真っ白な図面から。` (*"ご要望にお応えするだけでは、本当に心地よい住まいにはなりません。 ご家族の想いに、プロである私たちの提案を重ねていく。その先に、想"*) with `#f7f7f4` surface cards, `#333333` accents, and `.leap_box.leap_box-01 { padding: 1rem 1.5rem; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://nakagawa-corp.com/`)**:
   - Landmark `<footer class="footer">` anchoring `久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホ` footer links (`ナカガワホームの家づくり · 私たちについて · 快適な住まいづくり · 徹底したこだわり · 家づくりの流れ・アフターサポート`), copy *"ご要望として語られるのは、理想のほんの一部。 言葉の奥にある暮らし方まで読み解き、ご提案します。"*, and `#cccccc` structural dividers.
