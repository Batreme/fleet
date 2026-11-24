---
title: "UI & UX Architecture: vadimcarazan-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: vadimcarazan-com

## Overview & Design Identity
- **Target**: `vadimcarazan-com` (**Vadim Carazan, Creative Director**)
- **Production URL**: [https://vadimcarazan.com/](https://vadimcarazan.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0b` / `#f2f2f2`)
- **Summary**: Vadim Carazan, creative director and founder of WeGrow. Fourteen years of brand identities, websites and products for founders.
- **Total Clean CSS Variables Extracted**: `9` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Editorial Old Italic`
- **Body Font Stack**: `Inter Tight`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 0px`, `line-height: 0px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 33.12px`, `line-height: 35.7696px`, `font-weight: 400`, `letter-spacing: -0.4968px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0a0b` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f2f2f2` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0a0a0b` | transparent/inherited card surface over live computed `body` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#f2f2f2` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#f2f2f2` | secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#272728` | `var(--line)` in `:root` (`rgba(255, 255, 255, 0.12)`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#0a0a0b` | Canvas / Surface Token |
| `--ink` | `#f2f2f2` | Typography Ink Token |
| `--mute` | `rgba(242, 242, 242, 0.55)` | Color / Atmospheric Token |
| `--line` | `rgba(255, 255, 255, 0.12)` | Color / Atmospheric Token |
| `--serif` | `"Editorial Old Italic", "Instrument Serif", "Times New Roman", serif` | Typography / Scale Token |
| `--sans` | `"Inter Tight", "Inter", -apple-system, "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--pad` | `clamp(16px, 2vw, 32px)` | Layout / Spatial Grid Token |
| `--box-open` | `clamp(460px, 42vw, 780px)` | Dimension / Scale Token |
| `--ease` | `cubic-bezier(0.22, 1, 0.36, 1)` | Motion / Easing Token |
| `--vadimcarazan-com-bg` | `#0a0a0b` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--vadimcarazan-com-ink` | `#f2f2f2` | Primary Typography Ink (computed-derived) |
| `--vadimcarazan-com-surface` | `#0a0a0b` | Surface Substrate (computed-derived) |
| `--vadimcarazan-com-accent` | `#f2f2f2` | Interactive Accent (computed-derived) |
| `--vadimcarazan-com-muted` | `#f2f2f2` | Secondary Ink (computed-derived) |
| `--vadimcarazan-com-border` | `#272728` | Structural Border (computed-derived) |
| `--vadimcarazan-com-container` | `1382px` | Container Bound (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.topbar> — `vadimcarazan-com`)**:
   - Landmark `<header class="topbar">` (`1382x41px`) hosting `Vadim Carazan, Creative Director` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r169"`, `data-go="about"`, `data-go="about"`, `data-go="selected"`), and stylesheet rule `vc-consent.in { opacity:1;transform:none }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Vadim Carazan, Creative Director`)**:
   - Landmark `<section class="hero">` presenting display lead `Vadim Carazan, Creative Director` and copy excerpt *"Fourteen years of brand identities, websites and products for fou"* over `#0a0a0b` canvas and `#f2f2f2` ink.
3. **Primary Showcase & Content Grid (<section.view> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="view v-project">` rendering section `Featured Work & Interactive Showcase` with copy *"Creative Director, WeGrow"*, asset references (`clarity.js`, `ywzmdkawk4`, `track.js`, `favicon.ico`), and grid rule `vc-consent.out { opacity:0;transform:translateY(14px) }`.
4. **Interactive Detail & Feature Matrix (<section.v-selected> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="view v-selected">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Cluj-Napoca, Romania ( 19:06 )"*) with `#0a0a0b` surface cards, `#f2f2f2` accents, and `vc-consent p { margin:0 0 12px;color:rgba(242,242,242,.82) }`.
5. **Colophon & Global Directory Footer (<footer.logo> — `https://vadimcarazan.com/`)**:
   - Landmark `<footer class="logo">` anchoring `Vadim Carazan, Creative Director` footer links (`Overview · Index · Archive · About · Contact`), copy *"Selected , Work , About , Contact"*, and `#272728` structural dividers.
