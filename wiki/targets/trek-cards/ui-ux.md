---
title: "UI & UX Architecture: trek-cards"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: trek-cards

## Overview & Design Identity
- **Target**: `trek-cards` (**Trek Cards - The AI-Powered TCG Where Every Card Has a Story**)
- **Production URL**: [https://trek.cards/](https://trek.cards/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#18001a` / `#ff00ee`)
- **Summary**: Trek Cards is the AI-powered trading card game (TCG). Craft UNIQUE character cards, battle players worldwide and track your cards around...
- **Total Clean CSS Variables Extracted**: `38` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Rubik One`
- **Body Font Stack**: `Rubik`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 70.56px`, `font-weight: 400`, `letter-spacing: -2.16px`); rule `.title` (`line-height: .98`, `letter-spacing: -0.03em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 150px`, `line-height: 147px`, `font-weight: 400`, `letter-spacing: -4.5px`); rule `h2` (`font-size: clamp(38px, 6vw, 92px)`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 27.2px`, `font-weight: 400`); CSS variables `--body: 'Rubik', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`; rule `body` (`font-size: 17px`, `line-height: 1.6`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14.5px`, `line-height: 23.2px`, `font-weight: 500`); rule `small` (`font-size: 11px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#18001a` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1a0a2e` | `var(--bg)` in `:root` |
| **Interactive Accent / Highlight** | `#ff00ee` | `.btn--play { background: #ff00ee }` |
| **Secondary / Muted Copy** | `#b6a6d6` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#2a142c` | `var(--stroke)` in `:root` (`rgba(255, 255, 255, 0.08)`) |
| **Variable Token (`--surface`)** | `#221041` | `var(--surface)` in `:root` |
| **Variable Token (`--surface-2`)** | `#2e1650` | `var(--surface-2)` in `:root` |
| **Variable Token (`--purple`)** | `#6a00ff` | `var(--purple)` in `:root` |
| **Variable Token (`--lilac`)** | `#b176ff` | `var(--lilac)` in `:root` |
| **Variable Token (`--green`)** | `#68ff8e` | `var(--green)` in `:root` |
| **Variable Token (`--brand`)** | `#7b22ff` | `var(--brand)` in `:root` |
| **Variable Token (`--brand`)** | `#c215f6` | `var(--brand)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ground` | `#18001A` | Color / Atmospheric Token |
| `--bg` | `#1A0A2E` | Canvas / Surface Token |
| `--surface` | `#221041` | Canvas / Surface Token |
| `--surface-2` | `#2E1650` | Canvas / Surface Token |
| `--purple` | `#6A00FF` | Color / Atmospheric Token |
| `--pink` | `#FF00EE` | Typography Ink Token |
| `--lilac` | `#B176FF` | Color / Atmospheric Token |
| `--ink` | `#FFFFFF` | Typography Ink Token |
| `--muted` | `#B6A6D6` | Color / Atmospheric Token |
| `--soft` | `rgba(255, 255, 255, 0.72)` | Color / Atmospheric Token |
| `--stroke` | `rgba(255, 255, 255, 0.08)` | Elevation / Border Token |
| `--green` | `#68FF8E` | Color / Atmospheric Token |
| `--title` | `'Rubik One', 'Rubik', sans-serif` | Design System Custom Token |
| `--body` | `'Rubik', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif` | Dimension / Scale Token |
| `--brand` | `linear-gradient(55deg, #7B22FF 0%, #C215F6 38%, #FF00EE 82%)` | Brand / Palette Token |
| `--ease` | `cubic-bezier(.2, .8, .2, 1)` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `trek-cards`)**:
   - Landmark `<header class="nav">` (`1120x68px`) hosting `Trek Cards - The AI-Powered TCG Wher` navigation (`Craft · Battle · Journey · Legacy · Collect`), DOM attributes (`data-notify`, `data-when="prelaunch"`, `data-when="launch"`, `data-key="kravix"`), and stylesheet rule `font-face { font-family: 'Rubik One'; src: url('../fonts/rubik-one.woff') format('wo... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `EVERY CARD HAS A STORY.`)**:
   - Landmark `<section class="hero">` presenting display lead `EVERY CARD HAS A STORY.` and copy excerpt *"Trek Cards™ is the AI-powered TCG where you craft UNIQUE cards to"* over `#18001a` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.prologue> — `Every card has a story.`)**:
   - Landmark `<section class="prologue">` rendering section `Every card has a story.` with copy *"Where losing is only the beginning"*, asset references (`favicon-32x32.png`, `apple-touch-icon.png`, `site.css`, `trek-logo.webp (Trek Cards)`), and grid rule `after { box-sizing: border-box; margin: 0; padding: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.chapter> — `Craft your Unique`)**:
   - Landmark `<section class="chapter ch-craft">` framing `Craft your Unique` and `1 Describe your character` (*"Trek Cards™ is the AI-powered TCG where you craft Unique cards to"*) with `#1a0a2e` surface cards, `#ff00ee` accents, and `html { -webkit-text-size-adjust: 100%; overflow-x: hidden; overflow-x: clip; }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://trek.cards/`)**:
   - Landmark `<footer class="foot">` anchoring `Trek Cards - The AI-Powered TCG ` footer links (`Craft · Battle · Journey · Legacy · Collect`), copy *"Download on the App Store"*, and `#2a142c` structural dividers.
