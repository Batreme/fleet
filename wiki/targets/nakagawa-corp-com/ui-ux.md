# UI & UX Architecture: nakagawa-corp-com

## Overview & Design Identity
- **Target**: `nakagawa-corp-com` (**久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホーム）**)
- **Production URL**: [https://nakagawa-corp.com/](https://nakagawa-corp.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#202020` canvas, `#D6B996` ink, `#AD8A72` accent)
- **Summary**: 【1963年創業、久留米・うきはで60年以上】株式会社ナカガワ(本社:福岡県久留米市)は、真っ白な図面から一邸ずつ設計する完全自由設計の工務店です。注文住宅・分譲住宅・土地探しまで、暮らしに合わせてご提案します。
- **Total Clean CSS Variables Extracted**: `131` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cardo`
- **Body Font Stack**: `Jost`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-en-display: "Cardo", serif`, `--display-lg: 160`, `--display-md: 120`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--font-size-heading6)`, `0.875rem`, `1rem`, `1.125rem`, `0.75rem`)
- **Body Copy**: rule `body` (`line-height: 1`)
- **Metadata & Labels**: CSS variables `--leap-project-mono-01: var(--clr-mono-01, #F2F2F2)`, `--leap-project-mono-02: var(--clr-mono-03, #BABDC4)`, `--clr-mono-01: #EEEEEE`; rule `small` (`font-size: max(12px, 0.875rem)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#202020` | `var(--clr-primary-default)` in `:root` |
| **Primary Typography Ink** | `#0F0F0F` | `var(--clr-primary-dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#4A4A4A` | `var(--clr-primary-light)` in `:root` |
| **Interactive Accent / Highlight** | `#AD8A72` | `var(--clr-secondary-default)` in `:root` |
| **Secondary / Muted Copy** | `#5F433E` | `var(--clr-secondary-dark)` in `:root` |
| **Structural Hairline Border** | `#D6B996` | `var(--clr-secondary-light)` in `:root` |
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
| `--fz` | `16` | Design System Custom Token |
| `--rem` | `calc(1 / var(--fz) * 1rem)` | Dimension / Scale Token |
| `--header-hgt` | `96` | Layout / Spatial Grid Token |
| `--header-hgt-fx` | `80` | Layout / Spatial Grid Token |
| `--inner-xs` | `720` | Design System Custom Token |
| `--inner-sm` | `1080` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `nakagawa-corp-com`)**:
   - Landmark `<header class="header header-main">` hosting `久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホーム）` navigation (`ナカガワホームの家づくり · 私たちについて · 快適な住まいづくり · 徹底したこだわり · 家づくりの流れ・アフターサポート`), DOM attributes (`data-js-parallax`, `data-speed="-0.08"`, `data-speed="0.05"`, `data-speed="-0.12"`), and stylesheet rule `.leap_table thead th { background-color: var(--leap-project-main); color: var(--leap-project-wh); }`.
2. **Hero Stage & Focal Lead (<section.home-intro> — `あなたは出会う。 思い描く、その先の暮らしに。`)**:
   - Landmark `<section class="home-intro">` presenting display lead `あなたは出会う。 思い描く、その先の暮らしに。` and copy excerpt *"Tel.0120-168-350 10:00–18:00 CLOSE 火曜日・水曜日"* over `#202020` canvas and `#D6B996` ink.
3. **Primary Showcase & Content Grid (<section.home-works> — `「応える」だけでなく、 「提案する」。`)**:
   - Landmark `<section class="home-works">` rendering section `「応える」だけでなく、 「提案する」。` with copy *"10:00–18:00 CLOSE 火曜日・水曜日"*, asset references (`gtm.js`, `embed`, `front.css`, `style.css`), and grid rule `.box--ttl { font-size: var(--font-size-heading6); font-family: var(--font-jp-heading); }`.
4. **Interactive Detail & Feature Matrix (<section.home-event> — `ご要望の、その先まで。`)**:
   - Landmark `<section class="home-event section_pdg-md-top">` framing `ご要望の、その先まで。` and `提案のための、余白を残す。` (*"あなたは出会う。 思い描く、その先の暮らしに。"*) with `#4A4A4A` surface cards, `#AD8A72` accents, and `.leap_box.leap_box-01 { padding: 1rem 1.5rem; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://nakagawa-corp.com/`)**:
   - Landmark `<footer class="footer">` anchoring `久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホ` footer links (`ナカガワホームの家づくり · 私たちについて · 快適な住まいづくり · 徹底したこだわり · 家づくりの流れ・アフターサポート`), copy *"福岡・佐賀・大分で60年以上。 まだ言葉になっていない理想まで、形にする工務店。"*, and `#D6B996` structural dividers.
