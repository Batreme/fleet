---
title: "UI & UX Architecture: pinreply-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: pinreply-com

## Overview & Design Identity
- **Target**: `pinreply-com` (**Website Feedback Tool for Chrome · PinReply**)
- **Production URL**: [https://pinreply.com/](https://pinreply.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4968px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#101828` ink, `#5b4cee` accent)
- **Summary**: Pin visual comments on websites, share screenshot reviews, and collect client replies without accounts. A free-at-launch website feedback...
- **Total Clean CSS Variables Extracted**: `11` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 82.8px`, `font-weight: 700`, `letter-spacing: -3.24px`); rule `h1` (`font-size: 46px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 44px`, `line-height: 50.6px`, `font-weight: 700`, `letter-spacing: -1.98px`); rule `h2` (`font-size: 36px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); rule `p` (`font-size: 14px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 22.4px`, `font-weight: 600`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#101828` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f8fafc` | `var(--canvas)` in `:root` |
| **Interactive Accent / Highlight** | `#5b4cee` | `var(--brand)` in `:root` |
| **Secondary / Muted Copy** | `#667085` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#e4e7ec` | `var(--line)` in `:root` |
| **Variable Token (`--secondary`)** | `#344054` | `var(--secondary)` in `:root` |
| **Variable Token (`--hover`)** | `#4938d1` | `var(--hover)` in `:root` |
| **Variable Token (`--soft`)** | `#f5f3ff` | `var(--soft)` in `:root` |
| **Variable Token (`--mint`)** | `#087c6f` | `var(--mint)` in `:root` |
| **Variable Token (`--mint-soft`)** | `#f0fdf9` | `var(--mint-soft)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#101828` | Typography Ink Token |
| `--secondary` | `#344054` | Brand / Palette Token |
| `--muted` | `#667085` | Color / Atmospheric Token |
| `--line` | `#e4e7ec` | Color / Atmospheric Token |
| `--canvas` | `#f8fafc` | Canvas / Surface Token |
| `--brand` | `#5b4cee` | Brand / Palette Token |
| `--hover` | `#4938d1` | Color / Atmospheric Token |
| `--soft` | `#f5f3ff` | Color / Atmospheric Token |
| `--mint` | `#087c6f` | Color / Atmospheric Token |
| `--mint-soft` | `#f0fdf9` | Color / Atmospheric Token |
| `--radius` | `18px` | Elevation / Border Token |
| `--pinreply-com-bg` | `#ffffff` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--pinreply-com-ink` | `#101828` | Primary Typography Ink (computed-derived) |
| `--pinreply-com-surface` | `#f8fafc` | Surface Substrate (computed-derived) |
| `--pinreply-com-accent` | `#5b4cee` | Interactive Accent (computed-derived) |
| `--pinreply-com-muted` | `#667085` | Secondary Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `pinreply-com`)**:
   - Landmark `<header class="header">` (`1440x81px`) hosting `Website Feedback Tool for Chrome · P` navigation (`How it works · For clients · FAQ · Guides · Add to Chrome`), DOM attributes (`data-ads-conversion="add-to-chrome"`, `data-ads-conversion="add-to-chrome"`, `data-ads-conversion="add-to-chrome"`, `data-ads-choice="decline"`), and stylesheet rule `html { scroll-behavior:smooth;scroll-padding-top:100px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Website feedback. Without the back`)**:
   - Landmark `<section class="hero">` presenting display lead `Website feedback. Without the back-and-forth.` and copy excerpt *"A website feedback tool for Chrome. Pin a visual comment, share a"* over `#ffffff` canvas and `#101828` ink.
3. **Primary Showcase & Content Grid (<section.section> — `1 Spaces for everyday living.`)**:
   - Landmark `<section class="section">` rendering section `1 Spaces for everyday living.` with copy *"For Chrome on desktop. Free at launch. No account or payment card"*, asset references (`favicon.png`, `site.css`, `ads.js`, `pinreply-mark.svg`), and grid rule `textarea { font:inherit }`.
4. **Interactive Detail & Feature Matrix (<article.card> — `Point. Explain. Move forward.`)**:
   - Landmark `<article class="card">` framing `Point. Explain. Move forward.` and `Pin the change` (*"Give the headline more room above the button."*) with `#f8fafc` surface cards, `#5b4cee` accents, and `summary { -webkit-tap-highlight-color:transparent }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://pinreply.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Website Feedback Tool for Chrome` footer links (`How it works · For clients · FAQ · Guides · Add to Chrome`), copy *"An example review, with demonstration content."*, and `#e4e7ec` structural dividers.
