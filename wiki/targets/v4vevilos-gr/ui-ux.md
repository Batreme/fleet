---
title: "UI & UX Architecture: v4vevilos-gr"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: v4vevilos-gr

## Overview & Design Identity
- **Target**: `v4vevilos-gr` (**Βέβηλος • Once dead twice alive**)
- **Production URL**: [https://v4vevilos.gr](https://v4vevilos.gr)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×3312px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#050507` / `#ff6a00`)
- **Summary**: Επίσημο hub του Βέβηλου • μουσική, live, δισκογραφία & σύνδεσμοι σε ένα σημείο.
- **Total Clean CSS Variables Extracted**: `26` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Advent Pro`
- **Body Font Stack**: `Advent Pro`
- **Monospace / Technical Font Stack**: `Fira Sans Extra Condensed`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 168px`, `line-height: 154.56px`, `font-weight: 300`, `letter-spacing: 3.36px`); CSS variables `--font-display: "Bebas Neue", "Fira Sans Extra Condensed", "Arial Narrow", sans-serif`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 95.04px`, `line-height: 83.6352px`, `font-weight: 800`, `letter-spacing: -1.4256px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--font-body: "Advent Pro", sans-serif`; rule `p` (`font-size: .98rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); rule `small` (`font-size: .55em`, `font-weight: 500`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#050507` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#050506` | `var(--pl-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#ff6a00` | `var(--accent-fire)` in `:root` |
| **Secondary / Muted Copy** | `#f4efe6` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#1c1c1d` | `var(--border)` in `:root` (`rgba(255,255,255,.09)`) |
| **Variable Token (`--accent`)** | `#ff3e3e` | `var(--accent)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#050507` | Canvas / Surface Token |
| `--bg-soft` | `rgba(255,255,255,.02)` | Canvas / Surface Token |
| `--card-bg` | `rgba(255,255,255,.035)` | Canvas / Surface Token |
| `--card-bg-strong` | `rgba(255,255,255,.05)` | Canvas / Surface Token |
| `--border` | `rgba(255,255,255,.09)` | Elevation / Border Token |
| `--border-strong` | `rgba(255,62,62,.22)` | Elevation / Border Token |
| `--accent` | `#ff3e3e` | Brand / Palette Token |
| `--accent-fire` | `#ff6a00` | Brand / Palette Token |
| `--text` | `#ffffff` | Typography Ink Token |
| `--text-muted` | `rgba(255,255,255,.68)` | Typography Ink Token |
| `--text-soft` | `rgba(255,255,255,.45)` | Typography Ink Token |
| `--glass` | `blur(18px) saturate(155%)` | Dimension / Scale Token |
| `--radius-xl` | `32px` | Elevation / Border Token |
| `--radius-lg` | `22px` | Elevation / Border Token |
| `--radius-md` | `16px` | Elevation / Border Token |
| `--font-display` | `"Bebas Neue", "Fira Sans Extra Condensed", "Arial Narrow", sans-serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.topbar> — `v4vevilos-gr`)**:
   - Landmark `<header class="topbar reveal">` (`1192x126px`) hosting `Βέβηλος • Once dead twice alive` navigation (`EL · EN`), DOM attributes (`data-state="off"`, `data-engine="assets/sound-engine.m..."`, `data-zap="Βέβηλος·Vevilos·V4"`, `data-split`), and stylesheet rule `html { scroll-behavior:smooth }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Βέβηλος Βέβηλος`)**:
   - Landmark `<section class="hero">` presenting display lead `Βέβηλος Βέβηλος` and copy excerpt *"Rap • Hip-hop • Αθήνα"* over `#050507` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.gig-banner> — `Βέβηλος Β έ β η λ ο ς`)**:
   - Landmark `<section class="gig-banner hero-gig">` rendering section `Βέβηλος Β έ β η λ ο ς` with copy *"Ιδρυτικό μέλος των Βαβυλώνα και Omerta. Rap και hip-hop με βάθος,"*, asset references (`favicon.ico`, `apple-touch-icon.png`, `advent-pro-100-700-greek.woff2`, `advent-pro-100-700-latin.woff2`), and grid rule `body { overflow-x:clip }`.
4. **Interactive Detail & Feature Matrix (<section.vv-consent> — `Νεκρή Ζώνη V`)**:
   - Landmark `<section class="vv-consent">` framing `Νεκρή Ζώνη V` and `Η επόμενη σελίδα γράφεται και από σένα.` (*"Δεν χρειάζεται πια να ψάξεις τη Νεκρή Ζώνη.. Αυτή τη φορά, θα σε "*) with `#050506` surface cards, `#ff6a00` accents, and `img { max-width:100%;display:block }`.
5. **Colophon & Global Directory Footer (<footer.pl-open> — `https://v4vevilos.gr`)**:
   - Landmark `<footer class="pl-open">` anchoring `Βέβηλος • Once dead twice alive` footer links (`EL · EN`), copy *"Δεν χρειάζεται πια να ψάξεις τη Νεκρή Ζώνη.."*, and `#1c1c1d` structural dividers.
