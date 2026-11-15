# UI & UX Architecture: ondocollective-jp

## Overview & Design Identity
- **Target**: `ondocollective-jp` (**Ondo Collective**)
- **Production URL**: [https://ondocollective.jp/](https://ondocollective.jp/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#002c1c`)
- **Summary**: Ondo Collectiveは、ブランドの背景にある文脈を読み解き、理念やコンセプトの言語化からロゴ・キービジュアル・Webまでを一貫して手がけるクリエイティブ・コレクティブです。東京を拠点に、ブランドの世界観づくりを支援します。
- **Total Clean CSS Variables Extracted**: `56` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Gen Interface JP-aa1df9adf44a6d02`
- **Body Font Stack**: `Shippori Mincho-fd992fb70b84b1db`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `.title` (`font-size: var(--title-font-size)`, `line-height: 1.2`, `letter-spacing: -.02em`, `font-weight: 400`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80%`, `75%`, `.0714286vw`, `.266667vw`, `14rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80%`, `75%`, `.0714286vw`, `.266667vw`, `14rem`)
- **Metadata & Labels**: CSS variables `--letter-spacing-base: .03em`; rule `.label` (`font-size: 14rem`, `line-height: 1.2`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-text-white)` in `:root` |
| **Primary Typography Ink** | `#f3e5de` | `var(--color-bg-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#003c26` | `var(--color-green)` in `:root` |
| **Interactive Accent / Highlight** | `#002c1c` | `var(--color-deep-green)` in `:root` |
| **Secondary / Muted Copy** | `#d5cac4` | `var(--color-border-gray)` in `:root` |
| **Structural Hairline Border** | `#a3402c` | `var(--color-error)` in `:root` |
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
   - Landmark `<header class="l-header">` hosting `Ondo Collective` navigation (`Home Home · Projects Projects · Visuals Visuals · Contact Contact`), DOM attributes (`data-color="white"`, `data-visible="false"`, `data-menu="closed"`, `data-hover="fade"`), and stylesheet rule `after { box-sizing:inherit }`.
2. **Hero Stage & Focal Lead (<section.p-home-mv> — `We weave context`)**:
   - Landmark `<section class="p-home-mv">` presenting display lead `We weave context` and copy excerpt *"Founded by Wakako Ishido"* over `#fff` canvas and `#002c1c` ink.
3. **Primary Showcase & Content Grid (<section.p-home-philosophy> — `Philosophy`)**:
   - Landmark `<section class="p-home-philosophy">` rendering section `Philosophy` with copy *"Brand Context Designer"*, asset references (`gtm.js`, `favicon.ico`, `icon-96x96.png`, `icon-32x32.png`), and grid rule `html { -webkit-text-size-adjust:100%;-webkit-tap-highlight-color:transparent;li... }`.
4. **Interactive Detail & Feature Matrix (<section.p-home-introduction> — `Before it becomes words`)**:
   - Landmark `<section class="p-home-introduction">` framing `Before it becomes words` and `Introduction` (*"ishido@ondocollective.jp ishido@ondocollective.jp Copy Copied"*) with `#003c26` surface cards, `#002c1c` accents, and `main { display:block }`.
5. **Colophon & Global Directory Footer (<footer.l-footer> — `https://ondocollective.jp/`)**:
   - Landmark `<footer class="l-footer">` anchoring `Ondo Collective` footer links (`Home Home · Projects Projects · Visuals Visuals · Contact Contact`), copy *"ishido@ondocollective.jp ishido@ondocollective.jp"*, and `#a3402c` structural dividers.
