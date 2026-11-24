---
title: "UI & UX Architecture: legacybridge-software"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: legacybridge-software

## Overview & Design Identity
- **Target**: `legacybridge-software` (**AI Document Entry for AS/400 & Legacy Systems · LegacyBridge**)
- **Production URL**: [https://legacybridge.software/](https://legacybridge.software/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#082a1c` ink, `#cdff8c` accent)
- **Summary**: An AI agent that reads invoices, orders and claims and keys them into AS/400 (IBM i), mainframe and other legacy systems. Human approval,...
- **Total Clean CSS Variables Extracted**: `51` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 68px`, `line-height: 72px`, `font-weight: 500`, `letter-spacing: -3.4px`); rule `.h1` (`letter-spacing: -0.05em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 54px`, `line-height: 58px`, `font-weight: 500`, `letter-spacing: -2.16px`); rule `.h2` (`letter-spacing: -0.04em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: -0.64px`); rule `.body` (`letter-spacing: -0.04em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: -0.64px`); CSS variables `--mono: "Geist Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace`; rule `.caption` (`letter-spacing: -0.04em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#082a1c` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f4f7f9` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#cdff8c` | `var(--brand-accent)` in `:root` |
| **Secondary / Muted Copy** | `#94a3b8` | `var(--text-inverse-muted)` in `:root` |
| **Structural Hairline Border** | `#dde3e7` | `var(--border-divider)` in `:root` |
| **Variable Token (`--text-muted`)** | `#64707a` | `var(--text-muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--text-ink` | `#082a1c` | Typography Ink Token |
| `--text-muted` | `#64707a` | Typography Ink Token |
| `--text-inverse` | `#ffffff` | Typography Ink Token |
| `--text-inverse-muted` | `#94a3b8` | Typography Ink Token |
| `--brand-primary` | `#082a1c` | Brand / Palette Token |
| `--brand-secondary` | `#94a3b8` | Brand / Palette Token |
| `--brand-accent` | `#cdff8c` | Brand / Palette Token |
| `--surface-white` | `#ffffff` | Canvas / Surface Token |
| `--surface-page` | `#ffffff` | Canvas / Surface Token |
| `--surface-card` | `#f4f7f9` | Canvas / Surface Token |
| `--surface-section` | `#f4f7f9` | Canvas / Surface Token |
| `--surface-accent` | `#dde3e7` | Canvas / Surface Token |
| `--surface-subtle` | `#dde3e7` | Canvas / Surface Token |
| `--border-divider` | `#dde3e7` | Elevation / Border Token |
| `--radius-8` | `8px` | Elevation / Border Token |
| `--radius-12` | `12px` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `legacybridge-software`)**:
   - Landmark `<header class="site-header">` (`1440x80px`) hosting `AI Document Entry for AS/400 & Legac` navigation (`How it works · Solutions · Use cases · Blog · Why us`), DOM attributes (`data-lb-cta="header"`, `data-label="Book a demo"`, `data-label="Book"`, `data-contact-open="header"`), and stylesheet rule `.h1 { font: 500 68px/72px var(--font); letter-spacing: -0.05em; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Stop retyping invoices, claims and`)**:
   - Landmark `<section class="hero">` presenting display lead `Stop retyping invoices, claims and orders into AS...` and copy excerpt *"legacy bridge is now part of scandiweb"* over `#ffffff` canvas and `#082a1c` ink.
3. **Primary Showcase & Content Grid (<section.compare-cards> — `Your AS/400 (IBM i) system is not `)**:
   - Landmark `<section class="compare-cards">` rendering section `Your AS/400 (IBM i) system is not the problem. Th...` with copy *"Read the announcement"*, asset references (`favicon.svg`, `favicon-32.png`, `icon-192.png`, `apple-touch-icon.png`), and grid rule `.h2 { font: 500 54px/58px var(--font); letter-spacing: -0.04em; }`.
4. **Interactive Detail & Feature Matrix (<article.compare-cards__card> — `Hours of processing & typing`)**:
   - Landmark `<article class="compare-cards__card compare-cards__card--without">` framing `Hours of processing & typing` and `Seconds to approve` (*"Document entry automation for AS/400 (IBM i)"*) with `#f4f7f9` surface cards, `#cdff8c` accents, and `.h3 { font: 500 38px/42px var(--font); letter-spacing: -0.03em; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://legacybridge.software/`)**:
   - Landmark `<footer class="site-footer is-offscreen">` anchoring `AI Document Entry for AS/400 & L` footer links (`How it works · Solutions · Use cases · Blog · Why us`), copy *"legacy bridge reads incoming documents, checks the informati"*, and `#dde3e7` structural dividers.
