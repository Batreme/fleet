# UI & UX Architecture: actl-me

## Overview & Design Identity
- **Target**: `actl-me` (**ACTL — Arabian Community Tennis League**)
- **Production URL**: [https://actl.me/](https://actl.me/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a2952` / `#f4f4f2`)
- **Summary**: Find your next tennis match in Dubai. Discover the ACTL community, challenge players, follow your ranking and explore ACTL merchandise.
- **Total Clean CSS Variables Extracted**: `5` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `montreal`
- **Body Font Stack**: `montreal Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(60px,14vw,90px)`)
- **Section Heading (`H2`)**: rule `,h2` (`line-height: 1.04`, `letter-spacing: -.035em`, `font-weight: 700`)
- **Body Copy**: CSS variables `--font-body: "montreal", "montreal Fallback"`; rule `p` (`font-size: 15px`)
- **Metadata & Labels**: rule `small` (`font-size: 16px`, `letter-spacing: 0`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0a2952` | `var(--navy)` in `:root` |
| **Primary Typography Ink** | `#aaf136` | `var(--lime)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ede6c4` | `var(--cream)` in `:root` |
| **Interactive Accent / Highlight** | `#f4f4f2` | `var(--paper)` in `:root` |
| **Secondary / Muted Copy** | `#000080` | `body { background: navy }` (`#000080`) |
| **Structural Hairline Border** | `#162131` | `.phone { border: #162131 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-body` | `"montreal", "montreal Fallback"` | Typography / Scale Token |
| `--navy` | `#0a2952` | Layout / Spatial Grid Token |
| `--lime` | `#aaf136` | Color / Atmospheric Token |
| `--cream` | `#ede6c4` | Color / Atmospheric Token |
| `--paper` | `#f4f4f2` | Canvas / Surface Token |
| `--actl-me-bg` | `#0a2952` | Canvas Substrate (from `var(--navy)` in `:root`) |
| `--actl-me-ink` | `#f4f4f2` | Primary Typography Ink (stylesheet-derived) |
| `--actl-me-surface` | `#ede6c4` | Surface Substrate (stylesheet-derived) |
| `--actl-me-accent` | `#f4f4f2` | Interactive Accent (stylesheet-derived) |
| `--actl-me-muted` | `#000080` | Secondary Ink (stylesheet-derived) |
| `--actl-me-border` | `#162131` | Structural Border (stylesheet-derived) |
| `--actl-me-container` | `720px` | Container Bound (stylesheet-derived) |
| `--actl-me-gap` | `28px` | Grid Gutter (stylesheet-derived) |
| `--actl-me-pad` | `8px` | Lateral Padding (stylesheet-derived) |
| `--actl-me-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--actl-me-radius` | `40px` | Corner Radius (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `actl-me`)**:
   - Landmark `<header class="header">` hosting `ACTL — Arabian Community Tennis Leag` navigation (`The league · The app · The shop · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r185"`, `data-reveal="true"`, `data-reveal="true"`), and stylesheet rule `real_ae148c7a-module__pSTb6W__cla... { font-family:montreal,montreal Fallback }`.
2. **Hero Stage & Focal Lead (<section.league> — `Find your people.`)**:
   - Landmark `<section class="league section">` presenting display lead `Find your people.` and copy excerpt *"Arabian Community Tennis League · Dubai"* over `#0a2952` canvas and `#f4f4f2` ink.
3. **Primary Showcase & Content Grid (<section.app> — `Your kind of tennis.`)**:
   - Landmark `<section class="app section">` rendering section `Your kind of tennis.` with copy *"A shared court. A new rival. A reason to play again. Welcome to A"*, asset references (`NeueMontreal_Bold-s.p.1cs3sgkx_vm...`, `NeueMontreal_Regular-s.p.3qaxr7gv...`, `actl-logo.png`, `0xt1j8hd4-iqd.css`), and grid rule `treal_ae148c7a-module__pSTb6W__va... { --font-body:"montreal", "montreal Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.match-section> — `Less organising. More playing.`)**:
   - Landmark `<section class="match-section section">` framing `Less organising. More playing.` and `One more set? Always.` (*"Join via WhatsApp ↗"*) with `#ede6c4` surface cards, `#f4f4f2` accents, and `root { --navy:0a2952;--lime:aaf136;--cream:ede6c4;--paper:f4f4f2 }`.
5. **Colophon & Global Directory Footer (<footer.header-cta> — `https://actl.me/`)**:
   - Landmark `<footer class="header-cta">` anchoring `ACTL — Arabian Community Tennis ` footer links (`The league · The app · The shop · Contact`), copy *"More than the match"*, and `#162131` structural dividers.
