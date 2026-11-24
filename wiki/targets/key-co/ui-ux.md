---
title: "UI & UX Architecture: key-co"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: key-co

## Overview & Design Identity
- **Target**: `key-co` (**KEY.co · Luxury Vacation Home Rentals + Concierge Services**)
- **Production URL**: [https://key.co/](https://key.co/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#020817` ink, `#0b142b` accent)
- **Summary**: Find your perfect getaway with KEY.co. Explore curated vacation homes with in-home services like pre-arrival groceries and private chefs.
- **Total Clean CSS Variables Extracted**: `118` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `adobe-caslon-pro`
- **Body Font Stack**: `proxima-nova`
- **Monospace / Technical Font Stack**: `GeistMono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 92px`, `font-weight: 400`, `letter-spacing: -1.44px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 32px`, `line-height: 40px`, `font-weight: 400`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `,h2` (`font-weight: var(--font-we...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: .28px`, `font-weight: var(--font-we...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#020817` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fbf9f2` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0b142b` | `.accent-brand-navy { color: #0b142b }` |
| **Secondary / Muted Copy** | `#b47f00` | `.text-brand-gold { color: #b47f00 }` |
| **Structural Hairline Border** | `#b47f00` | `.border-brand-gold { border-color: #b47f00 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-geist-sans` | `"GeistSans","GeistSans Fallback"` | Typography / Scale Token |
| `--color-red-50` | `oklch(97.1% .013 17.38)` | Brand / Palette Token |
| `--color-red-100` | `oklch(93.6% .032 17.717)` | Brand / Palette Token |
| `--color-red-200` | `oklch(88.5% .062 18.334)` | Brand / Palette Token |
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-600` | `oklch(57.7% .245 27.325)` | Brand / Palette Token |
| `--color-red-700` | `oklch(50.5% .213 27.518)` | Brand / Palette Token |
| `--color-red-800` | `oklch(44.4% .177 26.899)` | Brand / Palette Token |
| `--color-orange-100` | `oklch(95.4% .038 75.164)` | Brand / Palette Token |
| `--color-orange-600` | `oklch(64.6% .222 41.116)` | Brand / Palette Token |
| `--color-green-100` | `oklch(96.2% .044 156.743)` | Brand / Palette Token |
| `--color-green-600` | `oklch(62.7% .194 149.214)` | Brand / Palette Token |
| `--color-blue-50` | `oklch(97% .014 254.604)` | Brand / Palette Token |
| `--color-blue-100` | `oklch(93.2% .032 255.585)` | Brand / Palette Token |
| `--color-blue-500` | `oklch(62.3% .214 259.815)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.max-w-max> — `key-co`)**:
   - Landmark `<nav class="max-w-max flex-1">` (`1120x68px`) hosting `KEY.co · Luxury Vacation Home Rental` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-rspack="@klaviyo/onsite-modul..."`), and stylesheet rule `.__className_fb8f2c { font-family:GeistSans,GeistSans Fallback }`.
2. **Hero Stage & Focal Lead (<section.navbar-section> — `Pack your bags, we’ll do the rest`)**:
   - Landmark `<section class="navbar-section">` presenting display lead `Pack your bags, we’ll do the rest` and copy excerpt *"$500 off $10k+ stays w/ HOLIDAYSAREHERE - ends 12/31"* over `#ffffff` canvas and `#020817` ink.
3. **Primary Showcase & Content Grid (<article.wf-proximanova-n5-active> — `$500 off $10k+ stays w/ HOLIDAYSAR`)**:
   - Landmark `<article class="wf-proximanova-n5-active">` rendering section `$500 off $10k+ stays w/ HOLIDAYSAREHERE - ends 1` with copy *"Curated Vacation Homes + Luxury Services"*, asset references (`oaiq.min.js`, `283498678855975`, `fbevents.js`, `gtm.js`), and grid rule `.__variable_fb8f2c { --font-geist-sans:"GeistSans","GeistSans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.video-fit> — `Curated Vacation Homes + Luxury Se`)**:
   - Landmark `<section class="video-fit no-gsap-animation">` framing `Curated Vacation Homes + Luxury Services` and `Explore our selection of premium homes—each chos` (*"Explore our selection of premium homes—each chosen for style, com"*) with `#fbf9f2` surface cards, `#0b142b` accents, and `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.bg-brand-beige> — `https://key.co/`)**:
   - Landmark `<footer class="bg-brand-beige">` anchoring `KEY.co · Luxury Vacation Home Re` footer links (`Overview · Index · Archive · About · Contact`), copy *"Professionally managed and vetted for comfort and style, our"*, and `#b47f00` structural dividers.
