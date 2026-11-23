---
title: "UI & UX Architecture: ringpopcandy-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: ringpopcandy-com

## Overview & Design Identity
- **Target**: `ringpopcandy-com` (**Ring Pop® — Candy for Every Celebration**)
- **Production URL**: [https://ringpopcandy.com/](https://ringpopcandy.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff7e9` canvas, `#141723` ink, `#ff8300` accent)
- **Summary**: Ring Pop turns any occasion into a celebration: birthdays, weddings, game days, wins. Shop the collections and find Ring Pop at a store n...
- **Total Clean CSS Variables Extracted**: `489` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Ringold`
- **Body Font Stack**: `Greed Standard`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 250px`, `line-height: 213px`, `font-weight: 400`, `letter-spacing: -5px`); CSS variables `--font-heading-h1: 'Ringold', Helvetica, Arial, sans-serif`, `--font-heading-h1-weight: 400`, `--h1-font-case: uppercase`; rule `,h1` (`font-size: var(--font-heading-h1-size-mo...`, `line-height: var(--font-heading-h1...`, `letter-spacing: var(--font-heading-h1...`, `font-weight: var(--font-he...`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 120px`, `line-height: 100px`, `font-weight: 400`, `letter-spacing: -2.4px`); CSS variables `--font-heading-h2: 'Ringold', Helvetica, Arial, sans-serif`, `--font-heading-h2-weight: 400`, `--h2-font-case: uppercase`; rule `,h2` (`font-size: var(--font-heading-h2-size-mo...`, `line-height: var(--font-heading-h2...`, `letter-spacing: var(--font-heading-h2...`, `font-weight: var(--font-he...`)
- **Body Copy**: live computed `body` (`font-size: 20px`, `line-height: 26px`, `font-weight: 400`); CSS variables `--font-body: 'Greed Standard', Helvetica, Arial, sans-serif`, `--font-body-size-xsmall: 14px`, `--font-body-size-small: 18px`; rule `p` (`font-size: inherit`, `line-height: inherit`, `letter-spacing: inherit`, `font-weight: inherit`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 19px`, `line-height: 30px`, `font-weight: 400`); CSS variables `--font-heading-small-title: 'Greed Standard', Helvetica, Arial, sans-serif`, `--font-heading-small-title-weight: 900`, `--small_title-font-case: uppercase`; rule `.label` (`font-size: 1.5rem`, `line-height: 1.083em`, `letter-spacing: -.0225rem`, `font-weight: 600`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fff7e9` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#141723` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fffaf6` | `var(--header-bg-color-sticky)` in `:root` |
| **Interactive Accent / Highlight** | `#ff8300` | `var(--oke-filter-searchHighlightColor)` in `:root` |
| **Secondary / Muted Copy** | `#ff8300` | `var(--oke-text-secondaryColor)` in `:root` |
| **Structural Hairline Border** | `#fcfcfc` | `var(--section-primary-button-border)` in `:root` |
| **Variable Token (`--color-accent`)** | `#b98c40` | `var(--color-accent)` in `:root` |
| **Variable Token (`--color-accent-hover`)** | `#936f33` | `var(--color-accent-hover)` in `:root` |
| **Variable Token (`--color-accent-2`)** | `#ff91b7` | `var(--color-accent-2)` in `:root` |
| **Variable Token (`--color-accent-2-darker`)** | `#ff5e96` | `var(--color-accent-2-darker)` in `:root` |
| **Variable Token (`--color-accent-3`)** | `#ff2b0f` | `var(--color-accent-3)` in `:root` |
| **Variable Token (`--color-accent-3-darker`)** | `#db1a00` | `var(--color-accent-3-darker)` in `:root` |
| **Variable Token (`--color-accent-4`)** | `#3e52ce` | `var(--color-accent-4)` in `:root` |
| **Variable Token (`--color-accent-4-darker`)** | `#2c3ead` | `var(--color-accent-4-darker)` in `:root` |
| **Variable Token (`--color-white`)** | `#ffffff` | `var(--color-white)` in `:root` |
| **Variable Token (`--color-off-white`)** | `#f5f4f3` | `var(--color-off-white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--brand-color` | `#141723` | Brand / Palette Token |
| `--color-accent` | `#B98C40` | Brand / Palette Token |
| `--color-accent-alpha` | `rgba(185, 140, 64, 0.08)` | Brand / Palette Token |
| `--color-accent-hover` | `#936f33` | Brand / Palette Token |
| `--color-accent-2` | `#FF91B7` | Brand / Palette Token |
| `--color-accent-2-darker` | `#ff5e96` | Canvas / Surface Token |
| `--color-accent-3` | `#ff2b0f` | Brand / Palette Token |
| `--color-accent-3-darker` | `#db1a00` | Canvas / Surface Token |
| `--color-accent-4` | `#3e52ce` | Brand / Palette Token |
| `--color-accent-4-darker` | `#2c3ead` | Canvas / Surface Token |
| `--color-body-text` | `#141723` | Typography Ink Token |
| `--color-body-text-alpha` | `rgba(20, 23, 35, 0.5)` | Typography Ink Token |
| `--color-white` | `#ffffff` | Canvas / Surface Token |
| `--color-off-white` | `#f5f4f3` | Canvas / Surface Token |
| `--color-black` | `#141723` | Canvas / Surface Token |
| `--grid-container-padding-mobile` | `25px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `ringpopcandy-com`)**:
   - Landmark `<header class="header is-inview">` (`1440x142px`) hosting `Ring Pop® — Candy for Every Celebrat` navigation (`Products · Explore · About`), DOM attributes (`data-toggler=".is-fixed"`, `data-id="CGMRQMBC77UCKR5263C0"`, `data-ot-ignore`, `data-source-attribution="shopify.exit_intersti..."`), and stylesheet rule `header.header { position:fixed;top:0;left:0;width:100%;z-index:100 }`.
2. **Hero Stage & Focal Lead (<section.mfr-core__hero-section> — `RING POP`)**:
   - Landmark `<section class="mfr-core__hero-section rendered">` presenting display lead `RING POP` and copy excerpt *"Explore Collections"* over `#fff7e9` canvas and `#141723` ink.
3. **Primary Showcase & Content Grid (<section.mfr-core__banner-with-box> — `Ring Pop`)**:
   - Landmark `<section class="mfr-core__banner-with-box grid-gutter-mobile">` rendering section `Ring Pop` with copy *"Made for every moment"*, asset references (`identify_f7846436.js`, `main.MTUyMzg1YjAxOQ.js`, `main.140d4362.js`, `events.js`), and grid rule `o.has-sticky-logo .header-logo__d... { display:none }`.
4. **Interactive Detail & Feature Matrix (<section.mfr-core__scrolling-bar> — `A little Bling to Celebrate Your T`)**:
   - Landmark `<section class="mfr-core__scrolling-bar">` framing `A little Bling to Celebrate Your Thing` and `The Sweetest Way To Say Yes!` (*"Ring Pop x Mindy Weiss"*) with `#fffaf6` surface cards, `#ff8300` accents, and `go.has-sticky-logo .header-logo__... { display:block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://ringpopcandy.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Ring Pop® — Candy for Every Cele` footer links (`Products · Explore · About`), copy *"Perfect for engagements, bridal showers, bachelorettes & wed"*, and `#fcfcfc` structural dividers.
