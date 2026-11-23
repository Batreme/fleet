---
title: "UI & UX Architecture: www-selkirk-com_pages-omni-pickleball-paddle"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-selkirk-com_pages-omni-pickleball-paddle

## Overview & Design Identity
- **Target**: `www-selkirk-com_pages-omni-pickleball-paddle` (**Selkirk OMNI™ Pickleball Paddle · Selkirk Sport - We Are Pickleball**)
- **Production URL**: [https://www.selkirk.com/pages/omni-pickleball-paddle](https://www.selkirk.com/pages/omni-pickleball-paddle)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#00c6fd` accent)
- **Summary**: The Selkirk OMNI™ pickleball paddle redefines all-court performance for the modern fast-paced pickleball game. Featuring ReactCore™ techn...
- **Total Clean CSS Variables Extracted**: `232` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `akira expanded`
- **Body Font Stack**: `owners-xwide`
- **Monospace / Technical Font Stack**: `Kode Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40px`, `line-height: normal`, `font-weight: 700`); rule `.title` (`font-size: 2.5rem`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 36px`, `line-height: 36px`, `font-weight: 700`, `letter-spacing: -0.5px`); rule `h2` (`line-height: 1.4em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 400`); CSS variables `--oke-bodyText-fontWeight: 400`, `--oke-bodyText-fontSize: var(--oke-text-regular,14px)`, `--oke-bodyText-fontFamily: inherit`; rule `p` (`line-height: var(--font_size_plus12)`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--oke-text-small: 12px`, `--onstore-label-size: 10px`; rule `.label` (`font-size: 9px`, `line-height: 24px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f9fafb` | `var(--loop-badge-background)` in `:root` |
| **Interactive Accent / Highlight** | `#00c6fd` | `.moi-explore-btn:hover { background: #00c6fd }` |
| **Secondary / Muted Copy** | `#333333` | `var(--shop-ai-reply-text)` in `:root` |
| **Structural Hairline Border** | `#f6f6f6` | `var(--new_label_border)` in `:root` |
| **Variable Token (`--loop-primary-color`)** | `#030712` | `var(--loop-primary-color)` in `:root` |
| **Variable Token (`--loop-badge-text`)** | `#374151` | `var(--loop-badge-text)` in `:root` |
| **Variable Token (`--loop-button-background`)** | `#d1d5db` | `var(--loop-button-background)` in `:root` |
| **Variable Token (`--loop-button-text`)** | `#1f2937` | `var(--loop-button-text)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--loop-primary-color` | `#030712` | Brand / Palette Token |
| `--loop-text-color` | `white` | Typography Ink Token |
| `--loop-badge-background` | `#F9FAFB` | Canvas / Surface Token |
| `--loop-badge-text` | `#374151` | Typography Ink Token |
| `--loop-button-background` | `#D1D5DB` | Canvas / Surface Token |
| `--loop-button-text` | `#1F2937` | Typography Ink Token |
| `--loop-onstore-button-padding` | `14px 16px` | Layout / Spatial Grid Token |
| `--loop-onstore-checkout-background` | `#030712` | Canvas / Surface Token |
| `--loop-onstore-checkout-text-color` | `white` | Typography Ink Token |
| `--loop-onstore-button-radius` | `0` | Elevation / Border Token |
| `--loop-onstore-button-gap` | `0.25rem` | Layout / Spatial Grid Token |
| `--loop-onstore-add-more-background` | `white` | Canvas / Surface Token |
| `--loop-onstore-add-more-text-color` | `black` | Typography Ink Token |
| `--loop-onstore-add-more-border` | `black` | Elevation / Border Token |
| `--loop-onstore-casing` | `uppercase` | Design System Custom Token |
| `--font_size` | `14px` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.no-js> — `www-selkirk-com_pages-omni-pickleball-paddle`)**:
   - Landmark `<header class="no-js">` (`1440px`) hosting `Selkirk OMNI™ Pickleball Paddle · Se` navigation (`Paddles · Clothing · Shoes · Gear · Blog`), DOM attributes (`data-gif-toggle-ready="true"`, `data-src="https://static.ads-tw..."`, `data-cookiecategory="4"`, `data-source-attribution="shopify.exit_intersti..."`), and stylesheet rule `.patrol-unstyled-list { list-style:inherit;padding:0;margin:0 }`.
2. **Hero Stage & Focal Lead (<section.template-page> — `ALL-COURT PERFORMANCE, REDEFINED`)**:
   - Landmark `<section class="template-page">` presenting display lead `ALL-COURT PERFORMANCE, REDEFINED` and copy excerpt *"BOOMSTIK ST IS HERE: More power. Now more spin."* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.shopify-section> — `referred you!`)**:
   - Landmark `<section class="shopify-section section-omni-landing">` rendering section `referred you!` with copy *"Shop and spend $50+ to get your free gift. Free gift will be adde"*, asset references (`uwt.js`, `patrol-styles.css`, `pandectes-rules.js`, `favicon.ico`), and grid rule `span.patrol-blank-target { display:none }`.
4. **Interactive Detail & Feature Matrix (<section.omni-hero> — `We're sorry, self-referrals are no`)**:
   - Landmark `<section class="omni-hero">` framing `We're sorry, self-referrals are not allowed.` and `We're sorry, but the referral link you used is no...` (*"A dark-toned, overhead action shot of a male pickleball player lu"*) with `#f9fafb` surface cards, `#00c6fd` accents, and `strong.patrol-semantic-bold { font-weight:inherit }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.selkirk.com/pages/omni-pickleball-paddle`)**:
   - Landmark `<footer class="site-footer footer-default">` anchoring `Selkirk OMNI™ Pickleball Paddle ` footer links (`Paddles · Clothing · Shoes · Gear · Blog`), copy *"OMNI [definition: “of all things”]"*, and `#f6f6f6` structural dividers.
