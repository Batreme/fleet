# UI & UX Architecture: dark-moon-org

## Overview & Design Identity
- **Target**: `dark-moon-org` (**Darkmoon: Autonomous AI Penetration Testing Platform**)
- **Production URL**: [https://dark-moon.org/](https://dark-moon.org/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#dceaf4` ink, `#b9c7d6` accent)
- **Summary**: Darkmoon is an open-source, AI-powered autonomous penetration testing platform. 50 specialized AI agents covering web, cloud, identity, C...
- **Total Clean CSS Variables Extracted**: `384` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `DM Title Fallback`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: `Google Sans Code`
- **Hero Display (`H1`)**: CSS variables `--m-display: clamp(3.5rem,calc(2rem + 8.2vw),4.5rem)`, `--m-h1: clamp(2.25rem,calc(1.25rem + 5.13vw),2.75rem)`, `--dm-display: var(--m-display)`; rule `.h1` (`font-size: var(--m-h1)`, `line-height: .95`, `letter-spacing: -.02em`, `font-weight: 500`)
- **Section Heading (`H2`)**: CSS variables `--nb-sh2: #e4e8ec`; rule `h2` (`letter-spacing: -.01em!important`)
- **Body Copy**: CSS variables `--m-body: 1.0625rem`, `--dm-body: var(--m-body)`, `--text-base: 1rem`; rule `p` (`font-size: 12px!important`)
- **Metadata & Labels**: CSS variables `--cv-mono: var(--font-code),"Google Sans Code",monospace`, `--m-caption: 0.8125rem`, `--m-mono: 0.75rem`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--ed-bg)` in `:root` |
| **Primary Typography Ink** | `#0b0d13` | `var(--ed-pale)` in `:root` |
| **Elevated Surface / Card Substrate** | `#dceaf4` | `var(--ed-fg)` in `:root` |
| **Interactive Accent / Highlight** | `#b9c7d6` | `var(--ed-soft)` in `:root` |
| **Secondary / Muted Copy** | `#8e9baa` | `var(--ed-mute)` in `:root` |
| **Structural Hairline Border** | `#87bfff` | `var(--ed-acc)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--nb-glow` | `59,38,204` | Design System Custom Token |
| `--nb-gx` | `10%` | Dimension / Scale Token |
| `--m-ink` | `var(--dm-offwhite)` | Typography Ink Token |
| `--m-moon-bg` | `transparent` | Canvas / Surface Token |
| `--m-moon` | `transparent` | Design System Custom Token |
| `--m-line-light` | `rgba(220,234,244,0.22)` | Canvas / Surface Token |
| `--m-rule-light` | `rgba(220,234,244,0.45)` | Canvas / Surface Token |
| `--gl-liquidgl` | `0` | Design System Custom Token |
| `--ed-bg` | `#000` | Canvas / Surface Token |
| `--ed-pale` | `#0b0d13` | Color / Atmospheric Token |
| `--ed-fg` | `#dceaf4` | Typography Ink Token |
| `--ed-soft` | `#b9c7d6` | Color / Atmospheric Token |
| `--ed-mute` | `#8e9baa` | Color / Atmospheric Token |
| `--ed-line` | `rgba(220,234,244,0.16)` | Color / Atmospheric Token |
| `--ed-acc` | `#87bfff` | Color / Atmospheric Token |
| `--ed-title` | `var(--font-display),"Space Mono",monospace` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `dark-moon-org`)**:
   - Landmark `<header class="fixed inset-x-0">` hosting `Darkmoon: Autonomous AI Penetration ` navigation (`Product · Pricing · Docs · Blog`), DOM attributes (`data-route-lang="en"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.dm-pill:hover { transform:translate(-2px,-2px);box-shadow:5.1px 5.1px 0 var(--nb-sh-btn) }`.
2. **Hero Stage & Focal Lead (<section.dm-hero> — `Darkmoon, Autonomous AI Penetratio`)**:
   - Landmark `<section class="dm-hero w6">` presenting display lead `Darkmoon, Autonomous AI Penetration Testing Platform` and copy excerpt *"D D A A R R K K M M O O O O N N"* over `#000` canvas and `#dceaf4` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Attack surface camp_20260426_3d2f `)**:
   - Landmark `<section class="relative scroll-mt-24">` rendering section `Attack surface camp_20260426_3d2f · 26 Apr 2026` with copy *"Autonomous, continuous penetration testing"*, asset references (`eafabf029ad39a43-s.p.woff2`, `c15382663895c1a1.css`, `6e008cfa72251405.css`, `e824d722814de74c.css`), and grid rule `hover { box-shadow:5.1px 5.1px 0 rgba(0,0,0,.75) }`.
4. **Interactive Detail & Feature Matrix (<section.dc> — `Not a scanner. An autonomous secur`)**:
   - Landmark `<section class="dc dc--default">` framing `Not a scanner. An autonomous security conductor.` and `Darkmoon + Splunk: Send AI Pentest Findings to Yo...` (*"Autonomous, continuous"*) with `#dceaf4` surface cards, `#b9c7d6` accents, and `.dm-pill:active { transform:translate(4px,4px);box-shadow:0 0 0 var(--nb-sh-btn) }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://dark-moon.org/`)**:
   - Landmark `<footer class="relative bg-white">` anchoring `Darkmoon: Autonomous AI Penetrat` footer links (`Product · Pricing · Docs · Blog`), copy *"penetration testing"*, and `#87bfff` structural dividers.
