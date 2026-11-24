---
title: "UI & UX Architecture: www-mdscollective-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-mdscollective-com

## Overview & Design Identity
- **Target**: `www-mdscollective-com` (**MDS Collective · China Marketing Agency for Hotels & Tourism**)
- **Production URL**: [https://www.mdscollective.com](https://www.mdscollective.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#101010` ink, `#ffa500` accent)
- **Summary**: Award-winning China marketing agency for luxury hotels and tourism brands. RedNote, WeChat, Douyin, KOLs and AI search. Formerly Metric D...
- **Total Clean CSS Variables Extracted**: `15` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Serif`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 141.12px`, `line-height: 143.942px`, `font-weight: 400`, `letter-spacing: -3.528px`); rule `h1` (`font-size: clamp(54px,9.8vw,156px)`, `line-height: 1.02`, `letter-spacing: -.025em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 100.8px`, `line-height: 98.784px`, `font-weight: 400`, `letter-spacing: -3.024px`); rule `h2` (`font-size: clamp(38px,5.6vw,88px)`, `line-height: 1.02`, `letter-spacing: -.025em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 400`); rule `p` (`font-size: 15px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 400`); rule `small` (`font-size: .5em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#101010` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f3f1` | `var(--bg2)` in `:root` |
| **Interactive Accent / Highlight** | `#ffa500` | `.legal-doc a:hover { color: orange }` (`#ffa500`) |
| **Secondary / Muted Copy** | `#8e8e89` | `var(--ink3-lg)` in `:root` |
| **Structural Hairline Border** | `#a3a39e` | `var(--rule)` in `:root` |
| **Variable Token (`--ink2`)** | `#5f5f5b` | `var(--ink2)` in `:root` |
| **Variable Token (`--ink3`)** | `#767671` | `var(--ink3)` in `:root` |
| **Variable Token (`--line`)** | `#e3e3df` | `var(--line)` in `:root` |
| **Variable Token (`--gold`)** | `#1c486d` | `var(--gold)` in `:root` |
| **Variable Token (`--orange`)** | `#e6872d` | `var(--orange)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#fff` | Canvas / Surface Token |
| `--bg2` | `#f3f3f1` | Canvas / Surface Token |
| `--ink` | `#101010` | Typography Ink Token |
| `--ink2` | `#5f5f5b` | Typography Ink Token |
| `--ink3` | `#767671` | Typography Ink Token |
| `--ink3-lg` | `#8e8e89` | Typography Ink Token |
| `--rule` | `#a3a39e` | Color / Atmospheric Token |
| `--line` | `#e3e3df` | Color / Atmospheric Token |
| `--gold` | `#1c486d` | Color / Atmospheric Token |
| `--navy` | `#1c486d` | Layout / Spatial Grid Token |
| `--orange` | `#e6872d` | Color / Atmospheric Token |
| `--serif` | `"Instrument Serif","PS Times","Times New Roman",Georgia,serif` | Typography / Scale Token |
| `--sans` | `"Helvetica Neue",Helvetica,Arial,system-ui,sans-serif` | Typography / Scale Token |
| `--r-lg` | `24px` | Dimension / Scale Token |
| `--hl` | `#e6872d52` | Color / Atmospheric Token |
| `--www-mdscollectiv-bg` | `#ffffff` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.lenis> — `www-mdscollective-com`)**:
   - Landmark `<nav class="lenis">` (`1440x79px`) hosting `MDS Collective · China Marketing Age` navigation (`About · Hotels & Hospitality · Tourism Boards · Airlines & Cruises · Higher Education`), DOM attributes (`data-u="hello"`, `data-d="mdscollective.com"`, `data-src-sm="/video/hero-720.mp4"`, `data-src-lg="/video/hero-1080.mp4"`), and stylesheet rule `selection { color:fff;background:e6872d }`.
2. **Hero Stage & Focal Lead (<section.brand-hero> — `Luxury Marketing targeting Chinese`)**:
   - Landmark `<section class="brand-hero">` presenting display lead `Luxury Marketing targeting Chinese & East Asian T...` and copy excerpt *"ASIA'S TOP HOSPITALITY, TRAVEL AND TOURISM MARKETING COMPANY"* over `#ffffff` canvas and `#101010` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `FIT travelers have evolved. AI is `)**:
   - Landmark `<section class="hero wrap">` rendering section `FIT travelers have evolved. AI is now where their...` with copy *"Asia's top hospitality, travel and tourism marketing company"*, asset references (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `hero-1080.mp4`), and grid rule `body { background:var(--bg);color:var(--ink);font-family:var(--sans);margin:0 }`.
4. **Interactive Detail & Feature Matrix (<section.hero-media> — `We are your long-term East Asia ma`)**:
   - Landmark `<section class="hero-media wrap">` framing `We are your long-term East Asia marketing partner.` and `Mandapa, a Ritz-Carlton Reserve` (*"targeting Chinese &"*) with `#f3f3f1` surface cards, `#ffa500` accents, and `html.lenis { height:auto }`.
5. **Colophon & Global Directory Footer (<footer.wrap> — `https://www.mdscollective.com`)**:
   - Landmark `<footer class="wrap">` anchoring `MDS Collective · China Marketing` footer links (`About · Hotels & Hospitality · Tourism Boards · Airlines & Cruises · Higher Education`), copy *"East Asian Travelers"*, and `#a3a39e` structural dividers.
