---
title: "UI & UX Architecture: dennypratama-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: dennypratama-com

## Overview & Design Identity
- **Target**: `dennypratama-com` (**Denny Pratama · Product designer who now builds what he designs**)
- **Production URL**: [https://dennypratama.com](https://dennypratama.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0c0c0b` / `#ff0000`)
- **Summary**: Eight years designing SaaS products and dashboards, now building them too. I design it. I build it.
- **Total Clean CSS Variables Extracted**: `94` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Archivo Fallback`
- **Monospace / Technical Font Stack**: `ui-monospace)`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: 24px`, `font-weight: 700`); CSS variables `--fs-h1: 64px`, `--lh-h1: 64px`; rule `h1` (`font-size: var(--fs-mega)`, `line-height: var(--lh-mega)`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 96px`, `line-height: 88px`, `font-weight: 300`, `letter-spacing: -4.8px`); CSS variables `--fs-h2: 48px`, `--lh-h2: 52px`; rule `h2` (`font-size: var(--fs-h3)`, `line-height: var(--lh-h3)`, `letter-spacing: -.025em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--fs-body: 16px`, `--lh-body: 24px`; rule `p` (`font-size: var(--fs-lead)`, `line-height: var(--lh-lead)`, `letter-spacing: -.01em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: -0.16px`); CSS variables `--fs-label: 14px`, `--lh-label: 20px`, `--fs-sm: 12px`; rule `small` (`font-size: 11px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0c0c0b` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ff0000` | `.site ::selection { background: red }` (`#ff0000`) |
| **Interactive Accent / Highlight** | `#ff0000` | `.btn:before { background: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#c9c6be` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#2c2b2a` | `var(--line)` in `:root` (`eceae424`) |
| **Variable Token (`--ink-2`)** | `#151514` | `var(--ink-2)` in `:root` |
| **Variable Token (`--ink-3`)** | `#1f1f1d` | `var(--ink-3)` in `:root` |
| **Variable Token (`--bone`)** | `#eceae4` | `var(--bone)` in `:root` |
| **Variable Token (`--bone-3`)** | `#e2dfd8` | `var(--bone-3)` in `:root` |
| **Variable Token (`--mute`)** | `#8c8a84` | `var(--mute)` in `:root` |
| **Variable Token (`--dim`)** | `#3b3a36` | `var(--dim)` in `:root` |
| **Variable Token (`--pm`)** | `#5f5d57` | `var(--pm)` in `:root` |
| **Variable Token (`--red`)** | `#ff4f2b` | `var(--red)` in `:root` |
| **Variable Token (`--ok`)** | `#3ccf7d` | `var(--ok)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#0c0c0b` | Typography Ink Token |
| `--ink-2` | `#151514` | Typography Ink Token |
| `--ink-3` | `#1f1f1d` | Typography Ink Token |
| `--bone` | `#eceae4` | Color / Atmospheric Token |
| `--bone-2` | `#c9c6be` | Color / Atmospheric Token |
| `--bone-3` | `#e2dfd8` | Color / Atmospheric Token |
| `--mute` | `#8c8a84` | Color / Atmospheric Token |
| `--dim` | `#3b3a36` | Color / Atmospheric Token |
| `--line` | `#eceae424` | Color / Atmospheric Token |
| `--line-2` | `#eceae447` | Color / Atmospheric Token |
| `--lp` | `#0c0c0b24` | Color / Atmospheric Token |
| `--lp2` | `#0c0c0b52` | Color / Atmospheric Token |
| `--pm` | `#5f5d57` | Color / Atmospheric Token |
| `--red` | `#ff4f2b` | Color / Atmospheric Token |
| `--ok` | `#3ccf7d` | Color / Atmospheric Token |
| `--e-out` | `cubic-bezier(.16,1,.3,1)` | Motion / Timing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `dennypratama-com`)**:
   - Landmark `<header class="nav">` (`1440x80px`) hosting `Denny Pratama · Product designer who` navigation (`Work · About · Blog · Contact`), DOM attributes (`data-precedence="next"`, `data-mode`, `data-cursor="link"`, `data-cursor="link"`), and stylesheet rule `.iX1fDW_className { font-family:Archivo,Archivo Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Denny Pratama, product designer. I`)**:
   - Landmark `<section class="hero">` presenting display lead `Denny Pratama, product designer. I design it. I b...` and copy excerpt *"Indonesia · 07:45 GMT+7"* over `#0c0c0b` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.work> — `Drawn, then shipped.`)**:
   - Landmark `<section class="work on-bone">` rendering section `Drawn, then shipped.` with copy *"01 · d · drawings Every product starts as a drawing."*, asset references (`21ca8f3f56c22ca2-s.p.14a9xpaqsbpp...`, `38ornfmwrfpoc.css`, `3rqd4qnakn6f7.js`, `3j77l_h18tv3f.js`), and grid rule `.iX1fDW_variable { --font-archivo:"Archivo", "Archivo Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.con> — `The mark, constructed: a pivot, on`)**:
   - Landmark `<section class="con">` framing `The mark, constructed: a pivot, one angle, eleven...` and `One angle, eleven points` (*"02 · the handoff Most get handed to someone else to build."*) with `#ff0000` surface cards, `#ff0000` accents, and `property --w { syntax:"<percentage>";inherits:false;initial-value:100% }`.
5. **Colophon & Global Directory Footer (<footer.ct> — `https://dennypratama.com`)**:
   - Landmark `<footer class="ct">` anchoring `Denny Pratama · Product designer` footer links (`Work · About · Blog · Contact`), copy *"03 · the gap That handoff is where they lose their shape."*, and `#2c2b2a` structural dividers.
