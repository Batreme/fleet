---
title: "UI & UX Architecture: www-politico-eu_sponsored-content-saving-costs-and-improving-lives"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-politico-eu_sponsored-content-saving-costs-and-improving-lives

## Overview & Design Identity
- **Target**: `www-politico-eu_sponsored-content-saving-costs-and-improving-lives` (**Saving costs and improving lives – POLITICO**)
- **Production URL**: [https://www.politico.eu/sponsored-content/saving-costs-and-improving-lives/](https://www.politico.eu/sponsored-content/saving-costs-and-improving-lives/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0d0f16` ink, `#ff0000` accent)
- **Summary**: Visit the post for more.
- **Total Clean CSS Variables Extracted**: `324` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Sohne`
- **Body Font Stack**: `Martina Plantijn`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-weight: var(--font-we...`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 20px`, `line-height: 30px`, `font-weight: 500`); rule `h2` (`font-weight: var(--font-we...`)
- **Body Copy**: live computed `body` (`font-size: 20px`, `line-height: 30px`, `font-weight: 400`); rule `p` (`font-size: var(--wp--custom--type-scale-...`, `line-height: var(--wp--custom--typ...`, `font-weight: var(--font-we...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 20px`, `line-height: 30px`, `font-weight: 400`); CSS variables `--wp--custom--animation--duration--small: 100ms`, `--wp--custom--animation--duration--extra-small: 50ms`, `--wp--custom--stroke--small: 1px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0d0f16` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0000` | `ant--primary .tags__tags .tags_... { background-color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#1ea0c3` | `.wp-social-link-bandcamp { color: #1ea0c3 }` |
| **Structural Hairline Border** | `#dadada` | `.sponsored-content-banner__bott... { border-top: #dadada }` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Variable Token (`--wp--custom--color--blue--100`)** | `#cce5f4` | `var(--wp--custom--color--blue--100)` in `:root` |
| **Variable Token (`--wp--custom--color--blue--300`)** | `#66b0dd` | `var(--wp--custom--color--blue--300)` in `:root` |
| **Variable Token (`--wp--custom--color--blue--500`)** | `#007bc7` | `var(--wp--custom--color--blue--500)` in `:root` |
| **Variable Token (`--wp--custom--color--blue--600`)** | `#00629f` | `var(--wp--custom--color--blue--600)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |
| `--wp-admin-theme-color--rgb` | `0,124,186` | Brand / Palette Token |
| `--wp-admin-theme-color-darker-10` | `#006ba1` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-10--rgb` | `0,107,160.5` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20` | `#005a87` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20--rgb` | `0,90,135` | Canvas / Surface Token |
| `--wp-admin-border-width-focus` | `2px` | Layout / Spatial Grid Token |
| `--wp-admin--admin-bar--position-offset` | `var(--wp-admin--admin-bar--height,0px)` | Dimension / Scale Token |
| `--wp--custom--color--blue--100` | `#CCE5F4` | Brand / Palette Token |
| `--wp--custom--color--blue--300` | `#66B0DD` | Brand / Palette Token |
| `--wp--custom--color--blue--500` | `#007BC7` | Brand / Palette Token |
| `--wp--custom--color--blue--600` | `#00629F` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Persistent Left Sidebar Navigation (<nav.navigation-mini> — `200×700px` at `x=40`)**:
   - Fixed/sticky left rail `<nav class="navigation-mini header__edition-nav-alt">` (`200px` wide) paired with top bar `<header class="header">` hosting `Saving costs and improving liv` navigation (`Europe · UK · France · Germany · Spain`), DOM attributes (`data-previous-scroll-y="null"`, `data-wp-strategy="async"`, `data-id="adlibScripts"`, `data-marketo-munchkin="true"`), and rule `k-polylang-navigation-language-sw... { align-self:center }`.
2. **Hero Stage & Focal Lead (<article.article> — `Our readers read next`)**:
   - Landmark `<article class="article article--no-top-margin">` inside `1440px` main stage presenting display lead `Our readers read next` and copy excerpt *"The above column is sponsor-generated content. To learn more abou"* over `#ffffff` canvas and `#0d0f16` ink.
3. **Primary Showcase & Content Grid (<article.article--no-top-margin> — `Lucy Powell promotes UK education `)**:
   - Landmark `<article class="article article--no-top-margin">` rendering section `Lucy Powell promotes UK education in China despit...` with copy *"is sponsor-generated"*, asset references (`wrap.js`, `munchkin.js`, `insight.min.js`, `uwt.js`), and grid rule `itcher .wp-block-navigation-item_... { align-items:center;display:inline-flex;line-height:normal;width:auto }`.
4. **Interactive Detail & Feature Matrix (<article.article:nth(2)> — `Global climate talks have collapse`)**:
   - Landmark `<article class="article article--no-top-margin">` framing `Global climate talks have collapsed. Here’s what...` and `Global left rallies in Paris to make ‘not so radi...` (*"Our readers read next"*) with `#dddddd` surface cards, `#ff0000` accents, and `on-language-switcher .pll-switche... { align-items:center;display:flex }`.
5. **Colophon & Global Directory Footer (<footer.article__footer-inline> — `https://www.politico.eu/sponsored-content/saving-costs-and-improving-lives/`)**:
   - Landmark `<footer class="article__footer-inline">` anchoring `Saving costs and improving lives` footer links (`Europe · UK · France · Germany · Spain`), copy *"Policy areas Agriculture and Food Central Banker Competition"*, and `#dadada` structural dividers.
