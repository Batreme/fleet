---
title: "UI & UX Architecture: www-agencejacquesparis-fr"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-agencejacquesparis-fr

## Overview & Design Identity
- **Target**: `www-agencejacquesparis-fr` (**Jacques Paris - Agence à impact positif**)
- **Production URL**: [https://www.agencejacquesparis.fr/](https://www.agencejacquesparis.fr/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f0f0dc` canvas, `#001847` ink, `#ffffff` accent)
- **Summary**: La créativité au service des marques qui veulent changer les choses et prendre soin de ce qui compte.
- **Total Clean CSS Variables Extracted**: `21` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ClashGrotesk`
- **Body Font Stack**: `ClashGrotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: observed font-size ladder: `16px`, `22.4px`, `14px`, `13.3333px`, `var(--text-xs)`
- **Section Heading (`H2`)**: observed font-size ladder: `16px`, `22.4px`, `14px`, `13.3333px`, `var(--text-xs)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-base: 15px`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-xs: 11px`, `--text-sm: 14px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f0f0dc` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#001847` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.ZoneCard_caseBtn__MWFpY { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#ffffff` | `.ZoneCard_caseBtn__MWFpY { background: #ffffff }` |
| **Secondary / Muted Copy** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#c0c5be` | `.InvitationForm_textarea__Xo0Zw { border-bottom: #c0c5be }` |
| **Variable Token (`--color-cream-light`)** | `#f7f7ed` | `var(--color-cream-light)` in `:root` |
| **Variable Token (`--color-cobalt-light`)** | `#1a3a6b` | `var(--color-cobalt-light)` in `:root` |
| **Variable Token (`--color-teal`)** | `#0e9aa7` | `var(--color-teal)` in `:root` |
| **Variable Token (`--color-coral`)** | `#e8442a` | `var(--color-coral)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-cream` | `#F0F0DC` | Brand / Palette Token |
| `--color-cream-light` | `#F7F7ED` | Canvas / Surface Token |
| `--color-cobalt` | `#001847` | Brand / Palette Token |
| `--color-cobalt-light` | `#1a3a6b` | Canvas / Surface Token |
| `--color-teal` | `#0E9AA7` | Brand / Palette Token |
| `--color-coral` | `#E8442A` | Brand / Palette Token |
| `--space-zero` | `0` | Layout / Spatial Grid Token |
| `--space-xs` | `4px` | Layout / Spatial Grid Token |
| `--space-sm` | `8px` | Layout / Spatial Grid Token |
| `--space-md` | `16px` | Layout / Spatial Grid Token |
| `--space-lg` | `24px` | Layout / Spatial Grid Token |
| `--space-xl` | `40px` | Layout / Spatial Grid Token |
| `--space-2xl` | `64px` | Layout / Spatial Grid Token |
| `--space-3xl` | `96px` | Layout / Spatial Grid Token |
| `--text-xs` | `11px` | Typography Ink Token |
| `--text-sm` | `14px` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.Navbar_navbar__UMdIx> — `www-agencejacquesparis-fr`)**:
   - Landmark `<nav class="Navbar_navbar__UMdIx">` (`1440x50px`) hosting `Jacques Paris - Agence à impact posi` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-nscript="afterInteractive"`), and stylesheet rule `.PosterCanvas_canvas__BduZz { position:absolute;inset:0;overflow:hidden;background-color:var(--color-c... }`.
2. **Hero Stage & Focal Lead (<main.ScrollEngine_scrollSpace__HfjIP> — `Jacques Paris - Agence à impact po`)**:
   - Landmark `<main class="ScrollEngine_scrollSpace__HfjIP">` presenting display lead `Jacques Paris - Agence à impact positif` and copy excerpt *"Assistant Art Director"* over `#f0f0dc` canvas and `#001847` ink.
3. **Primary Showcase & Content Grid (<main.ScrollEngine_viewport__JJVIB> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="ScrollEngine_viewport__JJVIB">` rendering section `Featured Work & Interactive Showcase` with copy *"Junior Business Partner"*, asset references (`jacques-logo.png`, `ad44a6578bd60804.css`, `074517235421c822.css`, `webpack-8fefb68f87553cee.js`), and grid rule `.ZoneLabel_primary__tb_mD { font-size:var(--text-xs);opacity:.35;letter-spacing:.05em }`.
4. **Interactive Detail & Feature Matrix (<main.PosterCanvas_canvas__BduZz> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="PosterCanvas_canvas__BduZz">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Creative Copywriter"*) with `#ffffff` surface cards, `#ffffff` accents, and `.ZoneLabel_secondary__sFo9Q { font-weight:300;color:var(--color-cobalt);line-height:1.4 }`.
5. **Colophon & Global Directory Footer (<footer.PosterCanvas_poster__O791U> — `https://www.agencejacquesparis.fr/`)**:
   - Landmark `<footer class="PosterCanvas_poster__O791U">` anchoring `Jacques Paris - Agence à impact ` footer links (`Overview · Index · Archive · About · Contact`), copy *"Senior Art Director"*, and `#c0c5be` structural dividers.
