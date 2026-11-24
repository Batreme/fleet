---
title: "UI & UX Architecture: www-stellarmanagement-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-stellarmanagement-com

## Overview & Design Identity
- **Target**: `www-stellarmanagement-com` (**Stellar Management · NYC Real Estate Developer & No Fee Rentals**)
- **Production URL**: [https://www.stellarmanagement.com](https://www.stellarmanagement.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#181513` ink, `#0000ff` accent)
- **Summary**: Stellar is a leading New York real estate developer and manager providing a wide range of apartments and commercial properties. Browse no...
- **Total Clean CSS Variables Extracted**: `94` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `General Sans Variable`
- **Body Font Stack**: `General Sans Variable`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 81px`, `line-height: 72.9px`, `font-weight: 500`, `letter-spacing: -3.24px`); CSS variables `--title-xl-size: max(28px,4.4rem)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 70.2px`, `line-height: 77.22px`, `font-weight: 500`, `letter-spacing: -2.106px`)
- **Body Copy**: live computed `body` (`font-size: 9px`, `line-height: normal`, `font-weight: 500`); rule `p` (`font-size: var(--desc-l-size)`, `line-height: 150%`, `letter-spacing: 0`, `font-weight: 500`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 9px`, `line-height: normal`, `font-weight: 500`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#181513` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#808080` | `:before { background: grey }` (`#808080`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.header-bottom .app-button { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#808080` | `.app-input .app-input-desc { color: grey }` (`#808080`) |
| **Structural Hairline Border** | `#0000ff` | `:hover { border-color: #0000ff }` |
| **Variable Token (`--grey`)** | `#cdcdcd` | `var(--grey)` in `:root` |
| **Variable Token (`--grey-light`)** | `#f5f5f5` | `var(--grey-light)` in `:root` |
| **Variable Token (`--grey-medium`)** | `#9e9e9e` | `var(--grey-medium)` in `:root` |
| **Variable Token (`--grey-dark`)** | `#727272` | `var(--grey-dark)` in `:root` |
| **Variable Token (`--grey-skeleton`)** | `#ebebeb` | `var(--grey-skeleton)` in `:root` |
| **Variable Token (`--grey-hover`)** | `#f0f0f0` | `var(--grey-hover)` in `:root` |
| **Variable Token (`--dark-blue`)** | `#06184f` | `var(--dark-blue)` in `:root` |
| **Variable Token (`--sky-blue`)** | `#dee9ff` | `var(--sky-blue)` in `:root` |
| **Variable Token (`--sky-blue-60`)** | `#ebf2ff` | `var(--sky-blue-60)` in `:root` |
| **Variable Token (`--sky-blue-25`)** | `#f7faff` | `var(--sky-blue-25)` in `:root` |
| **Variable Token (`--red`)** | `#e90000` | `var(--red)` in `:root` |
| **Variable Token (`--green`)** | `#0d4f06` | `var(--green)` in `:root` |
| **Variable Token (`--green-light`)** | `#def2df` | `var(--green-light)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--white` | `#fff` | Canvas / Surface Token |
| `--black` | `#181513` | Canvas / Surface Token |
| `--grey` | `#cdcdcd` | Color / Atmospheric Token |
| `--grey-light` | `#f5f5f5` | Canvas / Surface Token |
| `--grey-medium` | `#9e9e9e` | Color / Atmospheric Token |
| `--grey-dark` | `#727272` | Canvas / Surface Token |
| `--grey-skeleton` | `#ebebeb` | Color / Atmospheric Token |
| `--grey-hover` | `#f0f0f0` | Color / Atmospheric Token |
| `--dark-blue` | `#06184f` | Canvas / Surface Token |
| `--sky-blue` | `#dee9ff` | Color / Atmospheric Token |
| `--sky-blue-60` | `#ebf2ff` | Color / Atmospheric Token |
| `--sky-blue-25` | `#f7faff` | Color / Atmospheric Token |
| `--red` | `#e90000` | Color / Atmospheric Token |
| `--green` | `#0d4f06` | Color / Atmospheric Token |
| `--green-light` | `#def2df` | Canvas / Surface Token |
| `--black-opacity-l` | `rgba(0,0,0,.8)` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `www-stellarmanagement-com`)**:
   - Landmark `<header class="header">` (`1440x63px`) hosting `Stellar Management · NYC Real Estate` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-hid="page-vw"`, `data-gtag`, `data-v-d3185d1d`, `data-path="/"`), and stylesheet rule `root { --block-width-m:84rem;--search-sidebar-width:30rem }`.
2. **Hero Stage & Focal Lead (<section.first> — `We help New Yorkers find home`)**:
   - Landmark `<section class="first scroll-locked-fullscreen">` presenting display lead `We help New Yorkers find home` and copy excerpt *"Since 1985, creating, investing, developing & living NYC real est"* over `#ffffff` canvas and `#181513` ink.
3. **Primary Showcase & Content Grid (<section.block> — `We help New Yorkers find h o m e`)**:
   - Landmark `<section class="block">` rendering section `We help New Yorkers find h o m e` with copy *"R e n t w i t h u s R e n t w i t h u s"*, asset references (`entry.BO5l_mVZ.css`, `default.D_u9mJpK.css`, `filterMain.Dy3QUOs1.css`, `appInput.BLk3pTmz.css`), and grid rule `before { background:var(--white)!important }`.
4. **Interactive Detail & Feature Matrix (<section.neighborhoods> — `From h i s t o r i c blocks to n e`)**:
   - Landmark `<section class="neighborhoods neighborhoods-section">` framing `From h i s t o r i c blocks to n e w developments...` and `Explore our b a c k y a r d` (*"R e n t w i t h u s"*) with `#808080` surface cards, `#0000ff` accents, and `hover { border-color:var(--dark-blue);color:var(--dark-blue) }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.stellarmanagement.com`)**:
   - Landmark `<footer class="footer">` anchoring `Stellar Management · NYC Real Es` footer links (`Overview · Index · Archive · About · Contact`), copy *"The Way We Work, Defines Who We Are"*, and `#0000ff` structural dividers.
