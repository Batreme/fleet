---
title: "UI & UX Architecture: members-play-lacoste-com_ace-breaker-rg"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: members-play-lacoste-com_ace-breaker-rg

## Overview & Design Identity
- **Target**: `members-play-lacoste-com_ace-breaker-rg` (**Lacoste - Ace breaker**)
- **Production URL**: [https://members-play.lacoste.com/ace-breaker-rg](https://members-play.lacoste.com/ace-breaker-rg)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#fcd757`)
- **Summary**: Play and break as many bricks as you can
- **Total Clean CSS Variables Extracted**: `51` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `MonaSans`
- **Body Font Stack**: `MonaSans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: var(--title)`, `line-height: 1.1`, `letter-spacing: -.06em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.5em`, `font-weight: bold`)
- **Body Copy**: live computed `body` (`font-size: 50px`, `line-height: 52.5px`, `font-weight: 500`); rule `p` (`font-size: 20px`)
- **Metadata & Labels**: observed font-size ladder: `50px`, `var(--cta-text)`, `1em`, `14px`, `var(--home-title)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f3f2e1` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#00503c` | `:after { background: #00503c }` |
| **Interactive Accent / Highlight** | `#fcd757` | `var(--color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#3f8964` | `domi-gpc-label .right-container... { color: #3f8964 }` |
| **Structural Hairline Border** | `#7a7a2c` | `var(--border-color)` in `:root` (`rgba(245, 245, 88, .5)`) |
| **Variable Token (`--color-green`)** | `#008a20` | `var(--color-green)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--base-text` | `calc((22px) * var(--h-demult, 1))` | Typography Ink Token |
| `--color-main` | `#00503c` | Brand / Palette Token |
| `--color-accent` | `#fcd757` | Brand / Palette Token |
| `--color-green` | `#008A20` | Brand / Palette Token |
| `--padding` | `calc(var(--base-text))` | Layout / Spatial Grid Token |
| `--font-btn` | `MonaSans, Arial, Helvetica, sans-serif` | Typography / Scale Token |
| `--font-title` | `MonaSans, Arial, Helvetica, sans-serif` | Typography / Scale Token |
| `--font-text` | `MonaSans, Arial, Helvetica, sans-serif` | Typography Ink Token |
| `--logo-size` | `calc((50px) * var(--h-demult, 1))` | Layout / Spatial Grid Token |
| `--cta-text` | `calc((22.5px) * var(--h-demult, 1))` | Typography Ink Token |
| `--home-title` | `calc((45px) * var(--h-demult, 1))` | Dimension / Scale Token |
| `--prize-title` | `calc((45px) * var(--h-demult, 1))` | Dimension / Scale Token |
| `--prize-text` | `calc((22px) * var(--h-demult, 1))` | Typography Ink Token |
| `--padding-header` | `calc((10px) * var(--h-demult, 1))` | Layout / Spatial Grid Token |
| `--size` | `calc((400px) * var(--h-demult, 1))` | Layout / Spatial Grid Token |
| `--prize-mult` | `calc((24px) * var(--h-demult, 1))` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.desktop> — `members-play-lacoste-com_ace-breaker-rg`)**:
   - Landmark `<header class="desktop">` (`1440px`) hosting `Lacoste - Ace breaker` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-nosnippet="true"`, `data-lang-dir="ltr"`, `data-v-app`, `data-v-1c0d994a`), and stylesheet rule `path { fill:fcd757 }`.
2. **Hero Stage & Focal Lead (<main.ui> — `Lacoste - Ace breaker`)**:
   - Landmark `<main class="ui">` presenting display lead `Lacoste - Ace breaker` and copy excerpt *"Play and break as many bricks as you can"* over `#000000` canvas and `#f3f2e1` ink.
3. **Primary Showcase & Content Grid (<main.ui:nth(2)> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="ui">` rendering section `Featured Work & Interactive Showcase` with copy *"Lacoste - Ace breaker"*, asset references (`gtm.js`, `loader.js`, `favicon.ico`, `favicon_dark.svg`), and grid rule `disabled { pointer-events:none;opacity:.5 }`.
4. **Interactive Detail & Feature Matrix (<main.ui:nth(3)> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="ui">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#00503c` surface cards, `#fcd757` accents, and `hover { background:fff;transform:scale(1.05) }`.
5. **Colophon & Global Directory Footer (<footer.didomi-host> — `https://members-play.lacoste.com/ace-breaker-rg`)**:
   - Landmark `<footer class="didomi-host">` anchoring `Lacoste - Ace breaker` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#7a7a2c` structural dividers.
