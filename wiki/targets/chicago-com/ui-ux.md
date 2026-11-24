---
title: "UI & UX Architecture: chicago-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: chicago-com

## Overview & Design Identity
- **Target**: `chicago-com` (**chicago.com**)
- **Production URL**: [https://chicago.com/](https://chicago.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×5796px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#faf0eb` canvas, `#080808` ink, `#0000ff` accent)
- **Summary**: Local guides, community conversation, and news from every Chicago newsroom, gathered in one place.
- **Total Clean CSS Variables Extracted**: `394` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Tempo`
- **Body Font Stack**: `Tenon`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80px`, `line-height: 88px`, `font-weight: 700`, `letter-spacing: -1.6px`); CSS variables `--osano-display-position: bottom`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 36px`, `line-height: 42.012px`, `font-weight: 700`, `letter-spacing: -0.72px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--loginForm--state-body--font-size: var(--cdc--font-size--14)`, `--guide-body-gutter: 0px`, `--guide-body-pull: 0px`; rule `p` (`font-size: 16px`, `line-height: 22px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: var(--font-dm-mono), ui-monospace, monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#faf0eb` | live computed `section` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#080808` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#a5c4ff` | `var(--osano-dialog-background-color)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ff` | `nButton-module-scss-module__mqy... { background-color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#058a5e` | `var(--osano-gpc-foreground-color)` in `:root` |
| **Structural Hairline Border** | `#058a5e` | `var(--osano-gpc-border-color)` in `:root` |
| **Variable Token (`--osano-button-border-color`)** | `#be189e` | `var(--osano-button-border-color)` in `:root` |
| **Variable Token (`--osano-button-foreground-color`)** | `#ffffff` | `var(--osano-button-foreground-color)` in `:root` |
| **Variable Token (`--osano-dialog-foreground-color`)** | `#000000` | `var(--osano-dialog-foreground-color)` in `:root` |
| **Variable Token (`--osano-toggle-off-track-color`)** | `#a8a7a7` | `var(--osano-toggle-off-track-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--osano-clear-dialog-background` | `rgba(0,0,0,0)` | Canvas / Surface Token |
| `--osano-theme` | `classic` | Brand / Palette Token |
| `--osano-button-border-color` | `#be189e` | Brand / Palette Token |
| `--osano-dialog-type` | `bar` | Typography / Scale Token |
| `--osano-display-position` | `bottom` | Design System Custom Token |
| `--osano-info-dialog-position` | `right` | Design System Custom Token |
| `--osano-widget-position` | `right` | Design System Custom Token |
| `--osano-opt-out-widget-position` | `left` | Design System Custom Token |
| `--osano-button-background-color` | `#be189e` | Canvas / Surface Token |
| `--osano-button-foreground-color` | `#ffffff` | Typography Ink Token |
| `--osano-dialog-background-color` | `#a5c4ff` | Canvas / Surface Token |
| `--osano-dialog-foreground-color` | `#000000` | Typography Ink Token |
| `--osano-info-dialog-overlay-color` | `rgba(0,0,0,0.45)` | Brand / Palette Token |
| `--osano-link-color` | `#000000` | Typography Ink Token |
| `--osano-toggle-off-track-color` | `#a8a7a7` | Brand / Palette Token |
| `--osano-toggle-off-thumb-color` | `#FFFFFF` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.screen-reader-text> — `chicago-com`)**:
   - Landmark `<header class="screen-reader-text">` (`1440x95px`) hosting `chicago.com` navigation (`Guides and how-tos · Communities · Partners · News · Donate`), DOM attributes (`data-headlessui-focus-visible`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `h-module-scss-module__kr7T1a__hom... { padding-block:var(--cdc--spacing--32) }`.
2. **Hero Stage & Focal Lead (<section.fixed> — `Join the conversation on your bloc`)**:
   - Landmark `<section class="fixed">` presenting display lead `Join the conversation on your block` and copy excerpt *"Local guides, community conversation and news from across the Chi"* over `#faf0eb` canvas and `#080808` ink.
3. **Primary Showcase & Content Grid (<section.left-5> — `Birthday Freebies in Edgewater & A`)**:
   - Landmark `<section class="left-5">` rendering section `Birthday Freebies in Edgewater & Andersonville` with copy *"Communities Join the chat."*, asset references (`1k8qyjc-fu7el.css`, `18fnj9qumctti.css`, `1u4ghj5w6l3co.css`, `2u54wdv5bbzks.css`), and grid rule `erch-module-scss-module__kr7T1a__... { margin-block-end:0;padding-block-end:var(--cdc--spacing--8) }`.
4. **Interactive Detail & Feature Matrix (<article.z-50> — `The Out of Towner's guide to Edgew`)**:
   - Landmark `<article class="z-50">` framing `The Out of Towner's guide to Edgewater/Andersonville` and `Logan Square Lunches!` (*"Guides Discover the best spots across town."*) with `#a5c4ff` surface cards, `#0000ff` accents, and `rch-module-scss-module__kr7T1a__c... { gap:var(--cdc--spacing--32);display:grid }`.
5. **Colophon & Global Directory Footer (<footer.flex> — `https://chicago.com/`)**:
   - Landmark `<footer class="flex">` anchoring `chicago.com` footer links (`Guides and how-tos · Communities · Partners · News · Donate`), copy *"Discover the best spots across town."*, and `#058a5e` structural dividers.
