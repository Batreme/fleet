# UI & UX Architecture: bright-avenue-jp

## Overview & Design Identity
- **Target**: `bright-avenue-jp` (**株式会社ブライトアベニュー · 不動産買取再販事業・リノベーション事業**)
- **Production URL**: [https://bright-avenue.jp/](https://bright-avenue.jp/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#333333` / `#D9D4D4`)
- **Summary**: 株式会社ブライトアベニューは、関東エリアを中心に不動産買取再販サービスを展開しています。
- **Total Clean CSS Variables Extracted**: `159` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Noto Sans JP`
- **Body Font Stack**: `mfw-tbgostd-demibold`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `1.4rem`, `12.5px`, `2.6666666667vw`, `1.2rem`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 3rem`, `line-height: 1.4`)
- **Body Copy**: rule `p` (`font-size: 1.4rem`, `line-height: 1.75`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `1.4rem`, `12.5px`, `2.6666666667vw`, `1.2rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#333333` | `var(--color-text)` in `:root` |
| **Primary Typography Ink** | `#f6f6f6` | `var(--color-background)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Interactive Accent / Highlight** | `#D9D4D4` | `var(--color-beige-1)` in `:root` |
| **Secondary / Muted Copy** | `#e3d3d3` | `var(--color-beige-2)` in `:root` |
| **Structural Hairline Border** | `#afa3a3` | `var(--color-beige-3)` in `:root` |
| **Variable Token (`--color-blue-1`)** | `#609aae` | `var(--color-blue-1)` in `:root` |
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
1. **Brand Header & Navigation Bar (<header.l-header> — `bright-avenue-jp`)**:
   - Landmark `<header class="l-header is-nav-white">` hosting `株式会社ブライトアベニュー · 不動産買取再販事業・リノベーション事業` navigation (`会 会 社 社 情 情 報 報 · 販 販 売 売 実 実 績 績 · 事 事 業 業 内 内 容 容 · お お 知 知 ら ら せ せ · 採 採 用 用 情 情 報 報`), DOM attributes (`data-nav="company"`, `data-header-hover-rotate-bound="true"`, `data-nav="feature"`, `data-header-hover-rotate-bound="true"`), and stylesheet rule `body { margin:0;padding:0;border:none }`.
2. **Hero Stage & Focal Lead (<section.p-top-fv> — `断熱リノベーションで 中古マンションの価値を塗り替える`)**:
   - Landmark `<section class="p-top-fv">` presenting display lead `断熱リノベーションで 中古マンションの価値を塗り替える` and copy excerpt *"私 私 た た ち ち の の 特 特 徴 徴"* over `#333333` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.p-top-message> — `断熱リノベーションで 中古マンションの 価値を塗り替える`)**:
   - Landmark `<section class="p-top-message">` rendering section `断熱リノベーションで 中古マンションの 価値を塗り替える` with copy *"協 協 業 業 の の ご ご 相 相 談 談"*, asset references (`favicon.png`, `top_fv-poster-sp.avif`, `top_fv-poster-blur-frame.webp`, `fonts.googleapis.com`), and grid rule `section { margin:0;padding:0;border:0;list-style-type:none }`.
4. **Interactive Detail & Feature Matrix (<section.p-top-service> — `メッセージ メッセージ`)**:
   - Landmark `<section class="p-top-service">` framing `メッセージ メッセージ` and `事業内容 事業内容` (*"お お 問 問 い い 合 合 わ わ せ せ"*) with `#fff` surface cards, `#D9D4D4` accents, and `table { border:none;border-collapse:collapse;border-spacing:0 }`.
5. **Colophon & Global Directory Footer (<footer.l-footer> — `https://bright-avenue.jp/`)**:
   - Landmark `<footer class="l-footer">` anchoring `株式会社ブライトアベニュー · 不動産買取再販事業・リノベーショ` footer links (`会 会 社 社 情 情 報 報 · 販 販 売 売 実 実 績 績 · 事 事 業 業 内 内 容 容 · お お 知 知 ら ら せ せ · 採 採 用 用 情 情 報 報`), copy *"東京都渋谷区渋谷2丁目9－11 インテリックス青山通ビル 6F"*, and `#afa3a3` structural dividers.
