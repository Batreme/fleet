# UI & UX Architecture: trek-cards

## Overview & Design Identity
- **Target**: `trek-cards` (**Trek Cards - The AI-Powered TCG Where Every Card Has a Story**)
- **Production URL**: [https://trek.cards/](https://trek.cards/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#18001A` / `#2E1650`)
- **Summary**: Trek Cards is the AI-powered trading card game (TCG). Craft UNIQUE character cards, battle players worldwide and track your cards around...
- **Total Clean CSS Variables Extracted**: `38` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Rubik One`
- **Body Font Stack**: `Rubik`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `.title` (`line-height: .98`, `letter-spacing: -0.03em`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(38px, 6vw, 92px)`)
- **Body Copy**: CSS variables `--body: 'Rubik', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`; rule `body` (`font-size: 17px`, `line-height: 1.6`)
- **Metadata & Labels**: rule `small` (`font-size: 11px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#18001A` | `var(--ground)` in `:root` |
| **Primary Typography Ink** | `#1A0A2E` | `var(--bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#221041` | `var(--surface)` in `:root` |
| **Interactive Accent / Highlight** | `#2E1650` | `var(--surface-2)` in `:root` |
| **Secondary / Muted Copy** | `#6A00FF` | `var(--purple)` in `:root` |
| **Structural Hairline Border** | `#FF00EE` | `var(--pink)` in `:root` |
| **Variable Token (`--lilac`)** | `#B176FF` | `var(--lilac)` in `:root` |
| **Variable Token (`--ink`)** | `#FFFFFF` | `var(--ink)` in `:root` |
| **Variable Token (`--muted`)** | `#B6A6D6` | `var(--muted)` in `:root` |
| **Variable Token (`--green`)** | `#68FF8E` | `var(--green)` in `:root` |
| **Variable Token (`--brand`)** | `#7B22FF` | `var(--brand)` in `:root` |
| **Variable Token (`--brand`)** | `#C215F6` | `var(--brand)` in `:root` |

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
   - Landmark `<header class="nav">` hosting `Trek Cards - The AI-Powered TCG Wher` navigation (`Craft · Battle · Journey · Legacy · Collect`), DOM attributes (`data-notify`, `data-when="prelaunch"`, `data-when="launch"`, `data-key="kravix"`), and stylesheet rule `font-face { font-family: 'Rubik One'; src: url('../fonts/rubik-one.woff') format('wo... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Every card has a story.`)**:
   - Landmark `<section class="hero">` presenting display lead `Every card has a story.` and copy excerpt *"Download on the App Store"* over `#18001A` canvas and `#FF00EE` ink.
3. **Primary Showcase & Content Grid (<section.prologue> — `Craft your Unique`)**:
   - Landmark `<section class="prologue">` rendering section `Craft your Unique` with copy *"For iPhone iOS 17 or later"*, asset references (`favicon-32x32.png`, `apple-touch-icon.png`, `site.css`, `trek-logo.webp (Trek Cards)`), and grid rule `after { box-sizing: border-box; margin: 0; padding: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.chapter> — `1 Describe your character`)**:
   - Landmark `<section class="chapter ch-craft">` framing `1 Describe your character` and `2 Choose a frame` (*"Get it on Google Play"*) with `#221041` surface cards, `#2E1650` accents, and `html { -webkit-text-size-adjust: 100%; overflow-x: hidden; overflow-x: clip; }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://trek.cards/`)**:
   - Landmark `<footer class="foot">` anchoring `Trek Cards - The AI-Powered TCG ` footer links (`Craft · Battle · Journey · Legacy · Collect`), copy *"For Android On Google Play"*, and `#FF00EE` structural dividers.
