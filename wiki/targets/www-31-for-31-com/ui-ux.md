---
title: "UI & UX Architecture: www-31-for-31-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-31-for-31-com

## Overview & Design Identity
- **Target**: `www-31-for-31-com` (**31 for 31 · One scary movie for every night of October**)
- **Production URL**: [https://www.31-for-31.com/](https://www.31-for-31.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#07090c` / `#ff0000`)
- **Summary**: Thirty one horror movies, one for each night of October. Rate them, find where to stream them, and scroll through the whole tape.
- **Total Clean CSS Variables Extracted**: `18` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Saans`
- **Body Font Stack**: `Saans`
- **Monospace / Technical Font Stack**: `Saans Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 34px`, `line-height: 0px`, `font-weight: 700`); rule `.title` (`line-height: 0`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 60px`, `font-weight: 400`); rule `h2` (`font-size: clamp(28px, 3.4vw, 52px)`, `line-height: 1`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 27.2px`, `font-weight: 400`); CSS variables `--font-body: "Saans", system-ui, -apple-system, "Helvetica Neue", sans-serif`; rule `body` (`font-size: 17px`, `line-height: 1.6`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 27.2px`, `font-weight: 400`); rule `small` (`font-size: 15px`, `letter-spacing: .3em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#07090c` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | live computed `nav` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff0000` | `.rate button.dislike.is-mine { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#8d8a80` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#313335` | `.film-day { stroke: #313335 }` |
| **Variable Token (`--bg-2`)** | `#0d1218` | `var(--bg-2)` in `:root` |
| **Variable Token (`--ink`)** | `#e8e4d8` | `var(--ink)` in `:root` |
| **Variable Token (`--green`)** | `#4dff8c` | `var(--green)` in `:root` |
| **Variable Token (`--green-dim`)** | `#1f8f4e` | `var(--green-dim)` in `:root` |
| **Variable Token (`--orange`)** | `#ff6a1a` | `var(--orange)` in `:root` |
| **Variable Token (`--red`)** | `#ff2d55` | `var(--red)` in `:root` |
| **Variable Token (`--cyan`)** | `#2ee6ff` | `var(--cyan)` in `:root` |
| **Variable Token (`--block-a`)** | `#b8321f` | `var(--block-a)` in `:root` |
| **Variable Token (`--block-b`)** | `#1f3d2b` | `var(--block-b)` in `:root` |
| **Variable Token (`--block-c`)** | `#2a1f45` | `var(--block-c)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#07090c` | Canvas / Surface Token |
| `--bg-2` | `#0d1218` | Canvas / Surface Token |
| `--ink` | `#e8e4d8` | Typography Ink Token |
| `--muted` | `#8d8a80` | Color / Atmospheric Token |
| `--green` | `#4dff8c` | Color / Atmospheric Token |
| `--green-dim` | `#1f8f4e` | Color / Atmospheric Token |
| `--orange` | `#ff6a1a` | Color / Atmospheric Token |
| `--red` | `#ff2d55` | Color / Atmospheric Token |
| `--cyan` | `#2ee6ff` | Color / Atmospheric Token |
| `--block-a` | `#b8321f` | Color / Atmospheric Token |
| `--block-b` | `#1f3d2b` | Color / Atmospheric Token |
| `--block-c` | `#2a1f45` | Color / Atmospheric Token |
| `--font-spooky` | `"Creepster", "Impact", cursive` | Typography / Scale Token |
| `--font-blimp` | `"OC Blimp", "Creepster", "Impact", cursive` | Typography / Scale Token |
| `--font-osd` | `"Saans Mono", ui-monospace, "SF Mono", Menlo, "Courier New", monospace` | Typography / Scale Token |
| `--font-body` | `"Saans", system-ui, -apple-system, "Helvetica Neue", sans-serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.topbar> — `www-31-for-31-com`)**:
   - Landmark `<header class="topbar">` (`1440x98px`) hosting `31 for 31 · One scary movie for ever` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sound-toggle`, `data-view="scroll"`, `data-label="Scroll"`, `data-view="gallery"`), and stylesheet rule `focus { outline: none; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Wes Craven's New Nightmare`)**:
   - Landmark `<section class="hero">` presenting display lead `Wes Craven's New Nightmare` and copy excerpt *"One scary movie for every night of October. Thirty one tapes, rew"* over `#07090c` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.film> — `Friday the 13th`)**:
   - Landmark `<section class="film">` rendering section `Friday the 13th` with copy *"1948 DIR. ALFRED HITCHCOCK"*, asset references (`apple-touch-icon.png`, `Saans-Regular.woff`, `SaansMono-Regular.woff`, `style.css`), and grid rule `focus-visible { outline: 2px solid var(--green); outline-offset: 3px; box-shadow: 0 0 0... }`.
4. **Interactive Detail & Feature Matrix (<section.film:nth(2)> — `Sleepy Hollow`)**:
   - Landmark `<section class="film">` framing `Sleepy Hollow` and `The House of the Devil` (*"DIR. ALFRED HITCHCOCK"*) with `#000000` surface cards, `#ff0000` accents, and `.stream a:focus-visible { outline-offset: 2px; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.31-for-31.com/`)**:
   - Landmark `<footer class="footer">` anchoring `31 for 31 · One scary movie for ` footer links (`Overview · Index · Archive · About · Contact`), copy *"Two college friends strangle a classmate, hide the body in a"*, and `#313335` structural dividers.
