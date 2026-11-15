# UI & UX Architecture: fighterready-com

## Overview & Design Identity
- **Target**: `fighterready-com` (**Fighter Ready — UK Combat Sports Matchmaking Platform**)
- **Production URL**: [https://fighterready.com/](https://fighterready.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#080808` / `#2b2b2b`)
- **Summary**: Matchmaking that decides whether a bout is safe. One traffic light on weight, age, experience and skill before a bout is agreed — with ha...
- **Total Clean CSS Variables Extracted**: `20` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Barlow Condensed`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--display: "Barlow Condensed", "Arial Narrow", sans-serif`
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(2rem,4vw,3rem)`)
- **Body Copy**: CSS variables `--body: "Inter", system-ui, -apple-system, sans-serif`; rule `p` (`font-size: .9rem`, `line-height: 1.75`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.625rem`, `.95rem`, `.5rem`, `.75rem`, `clamp(3.25rem,9.5vw,9.5rem)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#080808` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#0d0d0d` | `var(--ink-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1a1a1a` | `var(--smoke)` in `:root` |
| **Interactive Accent / Highlight** | `#2b2b2b` | `var(--steel)` in `:root` |
| **Secondary / Muted Copy** | `#6a6a6a` | `var(--ash)` in `:root` |
| **Structural Hairline Border** | `#b8b8b8` | `var(--bone)` in `:root` |
| **Variable Token (`--white`)** | `#f2f2f2` | `var(--white)` in `:root` |
| **Variable Token (`--flame`)** | `#ff6a00` | `var(--flame)` in `:root` |
| **Variable Token (`--amber`)** | `#ffc000` | `var(--amber)` in `:root` |
| **Variable Token (`--gold`)** | `#f5c518` | `var(--gold)` in `:root` |
| **Variable Token (`--ember`)** | `#cc5500` | `var(--ember)` in `:root` |
| **Variable Token (`--green`)** | `#2cc55c` | `var(--green)` in `:root` |
| **Variable Token (`--red`)** | `#ef5350` | `var(--red)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#080808` | Typography Ink Token |
| `--ink-2` | `#0d0d0d` | Typography Ink Token |
| `--smoke` | `#1a1a1a` | Color / Atmospheric Token |
| `--steel` | `#2b2b2b` | Color / Atmospheric Token |
| `--ash` | `#6a6a6a` | Color / Atmospheric Token |
| `--bone` | `#b8b8b8` | Color / Atmospheric Token |
| `--white` | `#f2f2f2` | Canvas / Surface Token |
| `--flame` | `#ff6a00` | Color / Atmospheric Token |
| `--amber` | `#ffc000` | Color / Atmospheric Token |
| `--gold` | `#f5c518` | Color / Atmospheric Token |
| `--ember` | `#cc5500` | Color / Atmospheric Token |
| `--green` | `#2cc55c` | Color / Atmospheric Token |
| `--red` | `#ef5350` | Color / Atmospheric Token |
| `--display` | `"Barlow Condensed", "Arial Narrow", sans-serif` | Design System Custom Token |
| `--body` | `"Inter", system-ui, -apple-system, sans-serif` | Dimension / Scale Token |
| `--gutter` | `clamp(1.25rem, 4vw, 4rem)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.masthead> — `fighterready-com`)**:
   - Landmark `<header class="masthead">` hosting `Fighter Ready — UK Combat Sports Mat` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r170"`, `data-round="doors"`, `data-round="corridor"`, `data-round="ring"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.round> — `FIGHTER READY`)**:
   - Landmark `<section class="round">` presenting display lead `FIGHTER READY` and copy excerpt *"Skip to early access"* over `#080808` canvas and `#b8b8b8` ink.
3. **Primary Showcase & Content Grid (<section.round> — `MATCHMAKING IS BROKEN.`)**:
   - Landmark `<section class="round">` rendering section `MATCHMAKING IS BROKEN.` with copy *"FIGHTER READY COMBAT SPORTS MATCHMAKING"*, asset references (`favicon.ico`, `apple-touch-icon.png`, `site.webmanifest`, `fonts.googleapis.com`), and grid rule `html { background:var(--ink);scroll-behavior:auto }`.
4. **Interactive Detail & Feature Matrix (<section.round> — `Hours lost`)**:
   - Landmark `<section class="round">` framing `Hours lost` and `Mismatches happen` (*"EVENTS & TICKETING"*) with `#1a1a1a` surface cards, `#2b2b2b` accents, and `body.is-locked { overflow:hidden }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://fighterready.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Fighter Ready — UK Combat Sports` footer links (`Overview · Index · Archive · About · Contact`), copy *"ROUND 00 — OVERVIEW"*, and `#b8b8b8` structural dividers.
