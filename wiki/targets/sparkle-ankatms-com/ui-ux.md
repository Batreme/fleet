# UI & UX Architecture: sparkle-ankatms-com

## Overview & Design Identity
- **Target**: `sparkle-ankatms-com` (**Kids Reward Chart & Chore App · Sparkle**)
- **Production URL**: [https://sparkle.ankatms.com](https://sparkle.ankatms.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#1c1736` / `#fbfaf6`)
- **Summary**: Organize tasks, earn stars and choose rewards together. Sparkle is a private reward-chart app for families and groups on iPhone and iPad....
- **Total Clean CSS Variables Extracted**: `31` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Apple Color Emoji`
- **Body Font Stack**: `Hiragino Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(2.3rem,4.5vw,4rem)`, `line-height: 1.15`, `letter-spacing: -.035em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(1.6rem,3vw,2.3rem)`, `line-height: 1.3`, `letter-spacing: -.025em`)
- **Body Copy**: rule `p` (`font-size: .9rem`)
- **Metadata & Labels**: rule `small` (`font-size: 13px`, `font-weight: 650`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#1c1736` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#48425f` | `var(--ink-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#68637d` | `var(--ink-3)` in `:root` |
| **Interactive Accent / Highlight** | `#fbfaf6` | `var(--paper)` in `:root` |
| **Secondary / Muted Copy** | `#6b4ff0` | `var(--violet)` in `:root` |
| **Structural Hairline Border** | `#8d75ff` | `var(--violet-2)` in `:root` |
| **Variable Token (`--gold`)** | `#f5a623` | `var(--gold)` in `:root` |
| **Variable Token (`--gold-2`)** | `#ffcf4a` | `var(--gold-2)` in `:root` |
| **Variable Token (`--amber-ink`)** | `#b85f00` | `var(--amber-ink)` in `:root` |
| **Variable Token (`--rose`)** | `#e2478f` | `var(--rose)` in `:root` |
| **Variable Token (`--mint`)** | `#22c55e` | `var(--mint)` in `:root` |
| **Variable Token (`--night-ink`)** | `#f5f2ff` | `var(--night-ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#1c1736` | Typography Ink Token |
| `--ink-2` | `#48425f` | Typography Ink Token |
| `--ink-3` | `#68637d` | Typography Ink Token |
| `--paper` | `#fbfaf6` | Canvas / Surface Token |
| `--violet` | `#6b4ff0` | Color / Atmospheric Token |
| `--violet-2` | `#8d75ff` | Color / Atmospheric Token |
| `--gold` | `#f5a623` | Color / Atmospheric Token |
| `--gold-2` | `#ffcf4a` | Color / Atmospheric Token |
| `--amber-ink` | `#b85f00` | Typography Ink Token |
| `--rose` | `#e2478f` | Color / Atmospheric Token |
| `--mint` | `#22c55e` | Color / Atmospheric Token |
| `--night-ink` | `#f5f2ff` | Typography Ink Token |
| `--sky-top` | `rgb(255 247 236)` | Color / Atmospheric Token |
| `--sky-bottom` | `rgb(244 238 255)` | Color / Atmospheric Token |
| `--glow-a` | `rgb(255 214 168 / 0.6)` | Color / Atmospheric Token |
| `--glow-b` | `rgb(203 184 255 / 0.6)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `sparkle-ankatms-com`)**:
   - Landmark `<header class="nav">` hosting `Kids Reward Chart & Chore App · Spar` navigation (`English · Deutsch · Español · Français · Türkçe`), DOM attributes (`data-nav`, `data-logo`, `data-hud`, `data-hud-count`), and stylesheet rule `.search-languages a { color:inherit;text-decoration:underline;text-underline-offset:.2em }`.
2. **Hero Stage & Focal Lead (<section.hero> — `S t a r s T o d a y . H a b i t s `)**:
   - Landmark `<section class="hero">` presenting display lead `S t a r s T o d a y . H a b i t s T o m o r r o w .` and copy excerpt *"Scroll to earn your first star"* over `#1c1736` canvas and `#fbfaf6` ink.
3. **Primary Showcase & Content Grid (<section.scene> — `Everyday tasks become achievements`)**:
   - Landmark `<section class="scene scene--tasks">` rendering section `Everyday tasks become achievements.` with copy *"🇧🇷 Português (Brasil)"*, asset references (`favicon-32.png`, `apple-touch-icon.png`, `avatar-luca.jpg`, `sparkle-story.css`), and grid rule `.search-page img { display:block;max-width:100%;height:auto }`.
4. **Interactive Detail & Feature Matrix (<article.tcard> — `Get Moving`)**:
   - Landmark `<article class="tcard">` framing `Get Moving` and `Write something` (*"Português (Brasil)"*) with `#68637d` surface cards, `#fbfaf6` accents, and `.search-page a { color:4c3fba;text-underline-offset:.2em }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://sparkle.ankatms.com`)**:
   - Landmark `<footer class="foot">` anchoring `Kids Reward Chart & Chore App · ` footer links (`English · Deutsch · Español · Français · Türkçe`), copy *"A reward-chart app for families and groups"*, and `#8d75ff` structural dividers.
