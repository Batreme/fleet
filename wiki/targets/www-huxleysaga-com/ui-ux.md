# UI & UX Architecture: www-huxleysaga-com

## Overview & Design Identity
- **Target**: `www-huxleysaga-com` (**Huxley · Home**)
- **Production URL**: [https://www.huxleysaga.com/](https://www.huxleysaga.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#999`)
- **Summary**: The HUXLEY® saga is an original sci-fi universe created by renowned concept artist Ben Mauro. Explore all the books, products, artwork an...
- **Total Clean CSS Variables Extracted**: `228` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `NB Architekt Light`
- **Body Font Stack**: `NB Architekt Regular`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 48px`)
- **Section Heading (`H2`)**: rule `,h2` (`font-size: clamp(32px,32px + 0vw,32px)`, `line-height: 100%`, `letter-spacing: 1.92px`, `font-weight: 300`)
- **Body Copy**: rule `,p` (`letter-spacing: 12%`, `font-weight: 400`)
- **Metadata & Labels**: CSS variables `--tp-label-foreground-color: hsla(0,0%,100%,.5)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--white)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#9c0703` | `var(--redContact)` in `:root` |
| **Interactive Accent / Highlight** | `#999` | `var(--grey1)` in `:root` |
| **Secondary / Muted Copy** | `#666` | `var(--grey2)` in `:root` |
| **Structural Hairline Border** | `#111` | `var(--grey3)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--white` | `#fff` | Canvas / Surface Token |
| `--white-0` | `hsla(0,0%,100%,0)` | Canvas / Surface Token |
| `--white-5` | `hsla(0,0%,100%,.05)` | Canvas / Surface Token |
| `--white-10` | `hsla(0,0%,100%,.1)` | Canvas / Surface Token |
| `--white-15` | `hsla(0,0%,100%,.15)` | Canvas / Surface Token |
| `--white-20` | `hsla(0,0%,100%,.2)` | Canvas / Surface Token |
| `--white-25` | `hsla(0,0%,100%,.25)` | Canvas / Surface Token |
| `--white-30` | `hsla(0,0%,100%,.3)` | Canvas / Surface Token |
| `--white-35` | `hsla(0,0%,100%,.35)` | Canvas / Surface Token |
| `--white-40` | `hsla(0,0%,100%,.4)` | Canvas / Surface Token |
| `--white-45` | `hsla(0,0%,100%,.45)` | Canvas / Surface Token |
| `--white-50` | `hsla(0,0%,100%,.5)` | Canvas / Surface Token |
| `--white-55` | `hsla(0,0%,100%,.55)` | Canvas / Surface Token |
| `--white-60` | `hsla(0,0%,100%,.6)` | Canvas / Surface Token |
| `--white-65` | `hsla(0,0%,100%,.65)` | Canvas / Surface Token |
| `--white-70` | `hsla(0,0%,100%,.7)` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.e-nav> — `www-huxleysaga-com`)**:
   - Landmark `<header class="e-nav">` hosting `Huxley · Home` navigation (`H o m e · S t o r y · P r o d u c t s · A b o u t · S h o p`), DOM attributes (`data-hid="gtm"`, `data-hid="gtm-noscript"`, `data-hid="no-js-style"`, `data-v-db217464`), and stylesheet rule `before { transform:scale(1);transform-origin:left;transition-delay:var(--delay) }`.
2. **Hero Stage & Focal Lead (<section.s-banner-hero> — `Please enable JavaScript`)**:
   - Landmark `<section class="s-banner-hero">` presenting display lead `Please enable JavaScript` and copy excerpt *"Products HUXLEY: THE ORACLE HUXLEY: GRAPHIC NOVEL"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.s-small-header> — `The HUXLEY® saga`)**:
   - Landmark `<section class="s-small-header">` rendering section `The HUXLEY® saga` with copy *"HUXLEY: THE ORACLE"*, asset references (`gtm.js`, `entry.B21Z6f7r.css`, `SvgMask.Bd2uXaPf.css`, `LabelHighlight.DTuRQ1tQ.css`), and grid rule `.corners>div { opacity:1;transform:translate(0) }`.
4. **Interactive Detail & Feature Matrix (<section.s-featured> — `An original sci-fi universe create`)**:
   - Landmark `<section class="s-featured">` framing `An original sci-fi universe created by renowned c...` and `STORY` (*"HUXLEY: GRAPHIC NOVEL"*) with `#9c0703` surface cards, `#999` accents, and `.a-div { margin-top:auto }`.
5. **Colophon & Global Directory Footer (<footer.e-footer> — `https://www.huxleysaga.com/`)**:
   - Landmark `<footer class="e-footer layout-block">` anchoring `Huxley · Home` footer links (`H o m e · S t o r y · P r o d u c t s · A b o u t · S h o p`), copy *"A post-apocalyptic sci-fi universe"*, and `#111` structural dividers.
