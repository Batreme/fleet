---
title: "UI & UX Architecture: www-hollywoodexhibit2026-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-hollywoodexhibit2026-com

## Overview & Design Identity
- **Target**: `www-hollywoodexhibit2026-com` (**ELLE & Esquire, The New Hollywood Photography Exhibition**)
- **Production URL**: [https://www.hollywoodexhibit2026.com](https://www.hollywoodexhibit2026.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ffffff`)
- **Summary**: Hearst Galleries presented a joint photography exhibition for ELLE and Esquire, ELLE: The New Hollywood and Esquire Goes to Hollywood, fe...
- **Total Clean CSS Variables Extracted**: `44` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Apple Color Emoji`
- **Body Font Stack**: `Apple Color Emoji`
- **Monospace / Technical Font Stack**: `safiraMarch`
- **Hero Display (`H1`)**: observed font-size ladder: `18.7573px`, `1em`, `80%`, `75%`, `var(--text-headline-10)`
- **Section Heading (`H2`)**: observed font-size ladder: `18.7573px`, `1em`, `80%`, `75%`, `var(--text-headline-10)`
- **Body Copy**: live computed `body` (`font-size: 18.7573px`, `line-height: 23.4466px`, `font-weight: 400`, `letter-spacing: -2%`); CSS variables `--text-body-10--font-weight: 400`, `--text-body-10--line-height: 1.25`, `--text-body-10--letter-spacing: -2%`
- **Metadata & Labels**: CSS variables `--text-label--font-weight: 400`, `--text-label--line-height: 1`, `--text-label--letter-spacing: .03em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | `.text-white { color: white }` (`#ffffff`) |
| **Elevated Surface / Card Substrate** | `#e7e7e7` | `:disabled { background-color: #e7e7e7 }` |
| **Interactive Accent / Highlight** | `#ffffff` | `.text-white { color: white }` (`#ffffff`) |
| **Secondary / Muted Copy** | `#909090` | `:disabled { color: #909090 }` |
| **Structural Hairline Border** | `#808080` | `50 { border-color: #808080 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--spacing` | `.0625rem` | Layout / Spatial Grid Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--animate-spin` | `spin 1s linear infinite` | Motion / Easing Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--fluid-min-w` | `var(--layout-min-w,375)` | Design System Custom Token |
| `--fluid-max-w` | `var(--layout-max-w,1920)` | Layout / Spatial Grid Token |
| `--text-label--font-weight` | `400` | Typography Ink Token |
| `--text-label--line-height` | `1` | Typography Ink Token |
| `--text-label--letter-spacing` | `.03em` | Typography Ink Token |
| `--text-body-10--font-weight` | `400` | Typography Ink Token |
| `--text-body-10--line-height` | `1.25` | Typography Ink Token |
| `--text-body-10--letter-spacing` | `-2%` | Typography Ink Token |
| `--text-headline-10--font-weight` | `400` | Typography Ink Token |
| `--text-headline-10--line-height` | `1` | Typography Ink Token |
| `--text-headline-10--letter-spacing` | `normal` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.wf-helveticaltpro-n4-active> — `www-hollywoodexhibit2026-com`)**:
   - Landmark `<header class="wf-helveticaltpro-n4-active">` (`1440px`) hosting `ELLE & Esquire, The New Hollywood Ph` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r182"`, `data-nscript="afterInteractive"`, `data-nscript="afterInteractive"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.wf-helveticaltpro-n7-active> — `ELLE & Esquire, The New Hollywood `)**:
   - Landmark `<main class="wf-helveticaltpro-n7-active">` presenting display lead `ELLE & Esquire, The New Hollywood Photography Ex` and copy excerpt *"Hearst Galleries presented a joint photography exhibition for ELL"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.wf-helveticaltpro-i7-active> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="wf-helveticaltpro-i7-active">` rendering section `Featured Work & Interactive Showcase` with copy *"ELLE & Esquire, The New Hollywood Photography Ex"*, asset references (`ABCArizonaVariable-s.p.6844b0f6.w...`, `Haigrast-s.p.42f2de84.woff2`, `IvyPrestoHeadline_Thin-s.p.830ff3...`, `IvyPrestoText_Thin-s.p.3ba47ad4.w...`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.wf-helveticaltpro-i4-active> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="wf-helveticaltpro-i4-active">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#e7e7e7` surface cards, `#ffffff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.wf-ivyprestodisplay-n4-active> — `https://www.hollywoodexhibit2026.com`)**:
   - Landmark `<footer class="wf-ivyprestodisplay-n4-active">` anchoring `ELLE & Esquire, The New Hollywoo` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#808080` structural dividers.
