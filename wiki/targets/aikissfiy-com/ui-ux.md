---
title: "UI & UX Architecture: aikissfiy-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: aikissfiy-com

## Overview & Design Identity
- **Target**: `aikissfiy-com` (**Free AI Kissing Video Generator: Create AI Kiss Videos Online - AIKissfiy**)
- **Production URL**: [https://aikissfiy.com](https://aikissfiy.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#020617` ink, `#6c63ff` accent)
- **Summary**: Description: AIKissfiy creates realistic AI kissing videos from your photos. Choose different kiss styles, keep faces recognizable, and e...
- **Total Clean CSS Variables Extracted**: `251` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Plus Jakarta Sans`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 50px`, `line-height: 54px`, `font-weight: 800`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: 1.11111`, `--text-5xl: 3rem`; rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2 (largest visible desktop heading)` (`font-size: 60px`, `line-height: 1.2`, `font-weight: 900`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.5em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1.33333`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `section` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#020617` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f7f8fb` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#6c63ff` | `var(--gradient-primary)` in `:root` |
| **Secondary / Muted Copy** | `#64748b` | `var(--aikiss-soft-muted)` in `:root` |
| **Structural Hairline Border** | `#d1d5db` | `var(--border-color)` in `:root` |
| **Variable Token (`--aikiss-text`)** | `#0f172a` | `var(--aikiss-text)` in `:root` |
| **Variable Token (`--aikiss-muted`)** | `#475569` | `var(--aikiss-muted)` in `:root` |
| **Variable Token (`--gradient-primary`)** | `#8b81ff` | `var(--gradient-primary)` in `:root` |
| **Variable Token (`--gradient-primary`)** | `#b941ff` | `var(--gradient-primary)` in `:root` |
| **Variable Token (`--gradient-primary`)** | `#ec4899` | `var(--gradient-primary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `Inter,system-ui,sans-serif` | Typography / Scale Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--aikiss-section-bg` | `transparent` | Canvas / Surface Token |
| `--aikiss-surface-solid` | `#fff` | Canvas / Surface Token |
| `--aikiss-surface-muted` | `rgba(248,250,252,.82)` | Canvas / Surface Token |
| `--aikiss-border` | `rgba(99,102,241,.2)` | Elevation / Border Token |
| `--aikiss-border-strong` | `rgba(99,102,241,.34)` | Elevation / Border Token |
| `--aikiss-text` | `#0f172a` | Typography Ink Token |
| `--aikiss-muted` | `#475569` | Color / Atmospheric Token |
| `--aikiss-soft-muted` | `#64748b` | Color / Atmospheric Token |
| `--aikiss-glow-primary` | `rgba(108,99,255,.2)` | Brand / Palette Token |
| `--aikiss-glow-secondary` | `rgba(236,72,153,.14)` | Brand / Palette Token |
| `--gradient-primary` | `linear-gradient(135deg,#6c63ff,#8b81ff 30%,#b941ff 66%,#ec4899)` | Brand / Palette Token |
| `--aikiss-inner-highlight` | `hsla(0,0%,100%,.78)` | Canvas / Surface Token |
| `--aikiss-shadow` | `0 24px 60px rgba(15,23,42,.1)` | Elevation / Border Token |
| `--aikiss-tool-shell` | `hsla(0,0%,100%,.58)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Persistent Left Sidebar Navigation (<nav.app-navigation__nav> — `232×608px` at `x=11`)**:
   - Fixed/sticky left rail `<nav class="app-navigation__nav desktop-only">` (`232px` wide) paired with top bar `<header class="navigate-new top-0">` hosting `Free AI Kissing Video Generato` navigation (`Home · Nano Banana Pro · AI Effects`), DOM attributes (`data-hid="page-structured-data"`, `data-gtag`, `data-v-3c617593`, `data-v-122af031`), and rule `webkit-scrollbar { display:none }`.
2. **Hero Stage & Focal Lead (<section.home-section> — `Free AI Kissing Video Generator`)**:
   - Landmark `<section class="home-section aikiss-ambient-section">` inside `1196px` main stage presenting display lead `Free AI Kissing Video Generator` and copy excerpt *"Upload two photos, choose a kiss style, and create a realistic AI"* over `#ffffff` canvas and `#020617` ink.
3. **Primary Showcase & Content Grid (<article.gap-3> — `Generate AI Kiss Videos in Any Sty`)**:
   - Landmark `<article class="gap-3 px-3">` rendering section `Generate AI Kiss Videos in Any Style` with copy *"AI Kissing Video Generator"*, asset references (`cdn.aikissfiy.com`, `entry.BRsH49Xa.css`, `OverlayScrollbar.CrLIJdLh.css`, `LanguageSwitch.BsPr10ru.css`), and grid rule `.ak-button:focus-visible { outline:2px solid var(--ak-button-outline-color);outline-offset:1px;tran... }`.
4. **Interactive Detail & Feature Matrix (<article.px-3> — `What Else Can You Create with AIKi`)**:
   - Landmark `<article class="gap-3 px-3">` framing `What Else Can You Create with AIKissfiy?` and `Generate Romantic Videos & Love Stories` (*"Start Creating Now"*) with `#f7f8fb` surface cards, `#6c63ff` accents, and `.ak-button>span { align-items:center;display:inline-flex }`.
5. **Colophon & Global Directory Footer (<footer.border-slate-200> — `https://aikissfiy.com`)**:
   - Landmark `<footer class="border-slate-200 pt-8">` anchoring `Free AI Kissing Video Generator:` footer links (`Home · Nano Banana Pro · AI Effects`), copy *"Your Photos Stay Private"*, and `#d1d5db` structural dividers.
