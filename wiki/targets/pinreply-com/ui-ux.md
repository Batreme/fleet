# UI & UX Architecture: pinreply-com

## Overview & Design Identity
- **Target**: `pinreply-com` (**PinReply — Design feedback, in the right place**)
- **Production URL**: [https://pinreply.com/](https://pinreply.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#101828` canvas, `#f8fafc` ink, `#e4e7ec` accent)
- **Summary**: PinReply is a design feedback tool for visual comments on websites. Point to a change, share a review, and keep replies in context.
- **Total Clean CSS Variables Extracted**: `11` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 46px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 36px`)
- **Body Copy**: rule `p` (`font-size: 14px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `clamp(42px,5.5vw,72px)`, `clamp(30px,4vw,44px)`, `22px`, `23px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#101828` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#344054` | `var(--secondary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#667085` | `var(--muted)` in `:root` |
| **Interactive Accent / Highlight** | `#e4e7ec` | `var(--line)` in `:root` |
| **Secondary / Muted Copy** | `#f8fafc` | `var(--canvas)` in `:root` |
| **Structural Hairline Border** | `#5b4cee` | `var(--brand)` in `:root` |
| **Variable Token (`--hover`)** | `#4938d1` | `var(--hover)` in `:root` |
| **Variable Token (`--soft`)** | `#f5f3ff` | `var(--soft)` in `:root` |
| **Variable Token (`--mint`)** | `#087c6f` | `var(--mint)` in `:root` |
| **Variable Token (`--mint-soft`)** | `#f0fdf9` | `var(--mint-soft)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#101828` | Typography Ink Token |
| `--secondary` | `#344054` | Brand / Palette Token |
| `--muted` | `#667085` | Color / Atmospheric Token |
| `--line` | `#e4e7ec` | Color / Atmospheric Token |
| `--canvas` | `#f8fafc` | Canvas / Surface Token |
| `--brand` | `#5b4cee` | Brand / Palette Token |
| `--hover` | `#4938d1` | Color / Atmospheric Token |
| `--soft` | `#f5f3ff` | Color / Atmospheric Token |
| `--mint` | `#087c6f` | Color / Atmospheric Token |
| `--mint-soft` | `#f0fdf9` | Color / Atmospheric Token |
| `--radius` | `18px` | Elevation / Border Token |
| `--pinreply-com-bg` | `#101828` | Canvas Substrate (from `var(--ink)` in `:root`) |
| `--pinreply-com-ink` | `#f8fafc` | Primary Typography Ink (stylesheet-derived) |
| `--pinreply-com-surface` | `#667085` | Surface Substrate (stylesheet-derived) |
| `--pinreply-com-accent` | `#e4e7ec` | Interactive Accent (stylesheet-derived) |
| `--pinreply-com-muted` | `#f8fafc` | Secondary Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `pinreply-com`)**:
   - Landmark `<header class="header">` hosting `PinReply — Design feedback, in the r` navigation (`How it works · For clients · FAQ · Add to Chrome`), DOM attributes (`data-ads-conversion="add-to-chrome"`, `data-ads-conversion="add-to-chrome"`, `data-ads-conversion="add-to-chrome"`, `data-ads-choice="decline"`), and stylesheet rule `html { scroll-behavior:smooth;scroll-padding-top:100px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Website feedback. Without the back`)**:
   - Landmark `<section class="hero">` presenting display lead `Website feedback. Without the back-and-forth.` and copy excerpt *"Point to what needs changing. Add a visual comment. Keep client r"* over `#101828` canvas and `#f8fafc` ink.
3. **Primary Showcase & Content Grid (<section.section> — `1 Spaces for everyday living.`)**:
   - Landmark `<section class="section">` rendering section `1 Spaces for everyday living.` with copy *"For Chrome on desktop. Free at launch. No account or payment card"*, asset references (`favicon.png`, `site.css`, `ads.js`, `pinreply-mark.svg`), and grid rule `textarea { font:inherit }`.
4. **Interactive Detail & Feature Matrix (<article.card> — `Point. Explain. Move forward.`)**:
   - Landmark `<article class="card">` framing `Point. Explain. Move forward.` and `Pin the change` (*"Give the headline more room above the button."*) with `#667085` surface cards, `#e4e7ec` accents, and `summary { -webkit-tap-highlight-color:transparent }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://pinreply.com/`)**:
   - Landmark `<footer class="footer">` anchoring `PinReply — Design feedback, in t` footer links (`How it works · For clients · FAQ · Add to Chrome`), copy *"An example review, with demonstration content."*, and `#5b4cee` structural dividers.
