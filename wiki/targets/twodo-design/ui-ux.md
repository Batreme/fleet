# UI & UX Architecture: twodo-design

## Overview & Design Identity
- **Target**: `twodo-design` (**Two-Do**)
- **Production URL**: [https://twodo.design](https://twodo.design)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f6f2e9` canvas, `#211d18` ink, `#57524a` accent)
- **Summary**: Two-Do case study: a voice-first, shared to-do app for couples, where an AI agent does the legwork and nothing happens until you both agree.
- **Total Clean CSS Variables Extracted**: `19` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Caveat`
- **Body Font Stack**: `Fraunces`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(3.2rem, 7.4vw, 6.6rem)`, `line-height: 0.95`, `letter-spacing: -0.035em`, `font-weight: 300`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(2.2rem, 4vw, 3.6rem)`)
- **Body Copy**: rule `body` (`font-size: 17px`, `line-height: 1.6`)
- **Metadata & Labels**: rule `.mono` (`font-size: 0.72rem`, `letter-spacing: 0.12em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f6f2e9` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#efe9dc` | `var(--bg-deep)` in `:root` |
| **Elevated Surface / Card Substrate** | `#211d18` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#57524a` | `var(--ink-soft)` in `:root` |
| **Secondary / Muted Copy** | `#6e685a` | `var(--ink-faint)` in `:root` |
| **Structural Hairline Border** | `#5c6e4e` | `var(--sage)` in `:root` |
| **Variable Token (`--peach`)** | `#c97a4a` | `var(--peach)` in `:root` |
| **Variable Token (`--glow`)** | `#b8842a` | `var(--glow)` in `:root` |
| **Variable Token (`--sage-text`)** | `#4e6042` | `var(--sage-text)` in `:root` |
| **Variable Token (`--peach-text`)** | `#98552c` | `var(--peach-text)` in `:root` |
| **Variable Token (`--glow-text`)** | `#7f590f` | `var(--glow-text)` in `:root` |
| **Variable Token (`--heart`)** | `#c1633c` | `var(--heart)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#f6f2e9` | Canvas / Surface Token |
| `--bg-deep` | `#efe9dc` | Canvas / Surface Token |
| `--surface` | `rgba(33, 29, 24, 0.04)` | Canvas / Surface Token |
| `--border` | `rgba(33, 29, 24, 0.12)` | Elevation / Border Token |
| `--border-soft` | `rgba(33, 29, 24, 0.07)` | Elevation / Border Token |
| `--ink` | `#211d18` | Typography Ink Token |
| `--ink-soft` | `#57524a` | Typography Ink Token |
| `--ink-faint` | `#6e685a` | Typography Ink Token |
| `--sage` | `#5c6e4e` | Color / Atmospheric Token |
| `--peach` | `#c97a4a` | Color / Atmospheric Token |
| `--glow` | `#b8842a` | Color / Atmospheric Token |
| `--sage-text` | `#4e6042` | Typography Ink Token |
| `--peach-text` | `#98552c` | Typography Ink Token |
| `--glow-text` | `#7f590f` | Typography Ink Token |
| `--heart` | `#c1633c` | Color / Atmospheric Token |
| `--orb-a` | `rgba(140, 171, 123, 0.34)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bar> — `twodo-design`)**:
   - Landmark `<header class="bar">` hosting `Two-Do` navigation (`The idea · Moments · System`), DOM attributes (`data-theme="dark"`, `data-action="capture"`, `data-arg="checkup"`, `data-title="Say it out loud"`), and stylesheet rule `html { scroll-behavior: smooth; overflow-x: clip; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `The to- do list built for two.`)**:
   - Landmark `<section class="hero">` presenting display lead `The to- do list built for two.` and copy excerpt *"Open the app Open app ↗"* over `#f6f2e9` canvas and `#211d18` ink.
3. **Primary Showcase & Content Grid (<section.idea> — `Half of running a home is the thin`)**:
   - Landmark `<section class="idea">` rendering section `Half of running a home is the thinking about it.` with copy *"A product concept · 2026"*, asset references (`favicon.svg`, `apple-touch-icon.png`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `h3 { font-family: "Fraunces", Georgia, serif; font-weight: 380; letter-spacin... }`.
4. **Interactive Detail & Feature Matrix (<section.grain> — `Say it, don't type it.`)**:
   - Landmark `<section class="grain">` framing `Say it, don't type it.` and `Nothing happens without both of you.` (*"Two-Do is a shared home for a couple's projects. Say what needs d"*) with `#211d18` surface cards, `#57524a` accents, and `button { font-family: inherit; }`.
5. **Colophon & Global Directory Footer (<footer.credits> — `https://twodo.design`)**:
   - Landmark `<footer class="credits">` anchoring `Two-Do` footer links (`The idea · Moments · System`), copy *"The phone on the right is live — tap anything"*, and `#5c6e4e` structural dividers.
