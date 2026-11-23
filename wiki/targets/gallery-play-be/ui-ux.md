---
title: "UI & UX Architecture: gallery-play-be"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: gallery-play-be

## Overview & Design Identity
- **Target**: `gallery-play-be` (**Home - Gallery Play**)
- **Production URL**: [https://gallery-play.be/](https://gallery-play.be/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#1e1e1e` / `#ff3700`)
- **Summary**: We craft bold campaigns, authentic stories and premium collaborations that move sport and culture forward.
- **Total Clean CSS Variables Extracted**: `182` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Telegraf`
- **Body Font Stack**: `PP Telegraf`
- **Monospace / Technical Font Stack**: `Inconsolata`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 64px`, `line-height: 57.6px`, `font-weight: 700`); CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: var( --e-global-typography-pr...`, `line-height: var( --e-global-typog...`, `font-weight: var( --e-glob...`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 32px`, `line-height: 28.8px`, `font-weight: 700`); rule `h2` (`font-size: 32px`, `line-height: 0.9em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20px`, `font-weight: 300`); CSS variables `--cmplz_category_body_font_size: 12px`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20px`, `font-weight: 300`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#1e1e1e` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#55595c` | `on-dropdown ul.menu li.current-... { background: #55595c }` |
| **Interactive Accent / Highlight** | `#ff3700` | `var(--gradient-5)` in `:root` |
| **Secondary / Muted Copy** | `#cc3366` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#f2f2f2` | `var(--cmplz_banner_border_color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--direction-multiplier` | `1` | Design System Custom Token |
| `--page-title-display` | `block` | Design System Custom Token |
| `--cmplz_banner_width` | `526px` | Layout / Spatial Grid Token |
| `--cmplz_banner_background_color` | `#ffffff` | Canvas / Surface Token |
| `--cmplz_banner_border_color` | `#f2f2f2` | Brand / Palette Token |
| `--cmplz_banner_border_width` | `0px 0px 0px 0px` | Layout / Spatial Grid Token |
| `--cmplz_banner_border_radius` | `0px 0px 0px 0px` | Elevation / Border Token |
| `--cmplz_banner_margin` | `10px` | Layout / Spatial Grid Token |
| `--cmplz_categories-height` | `163px` | Layout / Spatial Grid Token |
| `--cmplz_title_font_size` | `15px` | Typography / Scale Token |
| `--cmplz_text_line_height` | `calc(var(--cmplz_text_font_size) * 1.5)` | Typography Ink Token |
| `--cmplz_text_color` | `#1e1e1e` | Typography Ink Token |
| `--cmplz_hyperlink_color` | `#1e1e1e` | Typography Ink Token |
| `--cmplz_text_font_size` | `12px` | Typography Ink Token |
| `--cmplz_link_font_size` | `12px` | Typography Ink Token |
| `--cmplz_category_body_font_size` | `12px` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.elementor> — `gallery-play-be`)**:
   - Landmark `<header class="elementor elementor-100">` (`1440x0px`) hosting `Home - Gallery Play` navigation (`Projects · Services · Athletes · Team · Contact`), DOM attributes (`data-mp="true"`, `data-cfasync="false"`, `data-mp="true"`, `data-cfasync="false"`), and stylesheet rule `.elementor-kit-5 e-page-transition { background-color:FFBC7D; }`.
2. **Hero Stage & Focal Lead (<main.site-main> — `CULTURE-SHIFTING CREATIVITY FOR TH`)**:
   - Landmark `<main class="site-main post-15">` presenting display lead `CULTURE-SHIFTING CREATIVITY FOR THE WORLD OF SPORTS` and copy excerpt *"We craft bold campaigns, authentic stories and premium collaborat"* over `#1e1e1e` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.post-15> — `Culture-shifting creativity for th`)**:
   - Landmark `<main class="site-main post-15">` rendering section `Culture-shifting creativity for the world of sports` with copy *"Start the conversation"*, asset references (`player.js`, `recaptcha__en.js`, `embed`, `cookieblocker.min.css`), and grid rule `or-section-boxed > .elementor-con... { max-width:1800px; }`.
4. **Interactive Detail & Feature Matrix (<main.page> — `Rooted in top-level football, flue`)**:
   - Landmark `<main class="site-main post-15">` framing `Rooted in top-level football, fluent in branding,...` and `Work that speaks louder than words.` (*"From shirt launches and transfer announcements to player branding"*) with `#55595c` surface cards, `#ff3700` accents, and `.elementor-element { --widgets-spacing:0px 0px;--widgets-spacing-row:0px;--widgets-spacing-co... }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://gallery-play.be/`)**:
   - Landmark `<footer class="elementor elementor-102">` anchoring `Home - Gallery Play` footer links (`Projects · Services · Athletes · Team · Contact`), copy *"We tailor every collaboration to the client. Brands, athlete"*, and `#f2f2f2` structural dividers.
