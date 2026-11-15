# UI & UX Architecture: web-smith-de

## Overview & Design Identity
- **Target**: `web-smith-de` (**Internetagentur Ostwestfalen: Websites & SEO · Web Smith**)
- **Production URL**: [https://web-smith.de](https://web-smith.de)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0a1320` canvas, `#8fb5fa` ink, `#163faf` accent)
- **Summary**: Websites, SEO und individuelle Software: Web Smith ist deine Internetagentur aus Ostwestfalen – mit kostenlosem Website-Check und Konfigu...
- **Total Clean CSS Variables Extracted**: `23` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Plus Jakarta Sans`
- **Body Font Stack**: `Plus Jakarta Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `12.5px`, `clamp(23px,min(2.9vw,5.4vh)`, `15px`, `14px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `12.5px`, `clamp(23px,min(2.9vw,5.4vh)`, `15px`, `14px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `12.5px`, `clamp(23px,min(2.9vw,5.4vh)`, `15px`, `14px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `12.5px`, `clamp(23px,min(2.9vw,5.4vh)`, `15px`, `14px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0a1320` | `var(--navy)` in `:root` |
| **Primary Typography Ink** | `#121e31` | `var(--navy-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1d4fd8` | `var(--blue)` in `:root` |
| **Interactive Accent / Highlight** | `#163faf` | `var(--blue-dark)` in `:root` |
| **Secondary / Muted Copy** | `#3478f6` | `var(--brand)` in `:root` |
| **Structural Hairline Border** | `#8fb5fa` | `var(--blue-soft)` in `:root` |
| **Variable Token (`--text`)** | `#4a5566` | `var(--text)` in `:root` |
| **Variable Token (`--muted`)** | `#aeb8c7` | `var(--muted)` in `:root` |
| **Variable Token (`--line`)** | `#dce2ea` | `var(--line)` in `:root` |
| **Variable Token (`--line-2`)** | `#cbd3df` | `var(--line-2)` in `:root` |
| **Variable Token (`--bg-soft`)** | `#f5f7fa` | `var(--bg-soft)` in `:root` |
| **Variable Token (`--bg-hero`)** | `#f7f8fa` | `var(--bg-hero)` in `:root` |
| **Variable Token (`--chip`)** | `#f2f5f9` | `var(--chip)` in `:root` |
| **Variable Token (`--white`)** | `#fff` | `var(--white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--navy` | `#0a1320` | Layout / Spatial Grid Token |
| `--navy-2` | `#121e31` | Layout / Spatial Grid Token |
| `--blue` | `#1d4fd8` | Color / Atmospheric Token |
| `--blue-dark` | `#163faf` | Canvas / Surface Token |
| `--brand` | `#3478f6` | Brand / Palette Token |
| `--blue-soft` | `#8fb5fa` | Color / Atmospheric Token |
| `--text` | `#4a5566` | Typography Ink Token |
| `--muted` | `#aeb8c7` | Color / Atmospheric Token |
| `--line` | `#dce2ea` | Color / Atmospheric Token |
| `--line-2` | `#cbd3df` | Color / Atmospheric Token |
| `--bg-soft` | `#f5f7fa` | Canvas / Surface Token |
| `--bg-hero` | `#f7f8fa` | Canvas / Surface Token |
| `--chip` | `#f2f5f9` | Color / Atmospheric Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--radius` | `28px` | Elevation / Border Token |
| `--wrap` | `1180px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hd> — `web-smith-de`)**:
   - Landmark `<header class="hd">` hosting `Internetagentur Ostwestfalen: Websit` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-astro-cid-nen7h5rs`, `data-hd`, `data-dd-item`, `data-dd-btn`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Wir entwickeln digitale Lösungen d`)**:
   - Landmark `<section class="hero">` presenting display lead `Wir entwickeln digitale Lösungen die wirken .` and copy excerpt *"Zum Inhalt springen"* over `#0a1320` canvas and `#8fb5fa` ink.
3. **Primary Showcase & Content Grid (<section.mq> — `Alles, was dein Unternehmen online`)**:
   - Landmark `<section class="mq">` rendering section `Alles, was dein Unternehmen online sichtbar macht.` with copy *"Internetagentur aus Ostwestfalen"*, asset references (`favicon.ico`, `favicon.svg`, `favicon-32.png`, `favicon-192.png`), and grid rule `html { -webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:... }`.
4. **Interactive Detail & Feature Matrix (<section.sec> — `Webentwicklung`)**:
   - Landmark `<section class="sec sec--blob">` framing `Webentwicklung` and `Branding` (*"hello@web-smith.de"*) with `#1d4fd8` surface cards, `#163faf` accents, and `svg { max-width:100%;display:block }`.
5. **Colophon & Global Directory Footer (<footer.ft> — `https://web-smith.de`)**:
   - Landmark `<footer class="ft">` anchoring `Internetagentur Ostwestfalen: We` footer links (`Overview · Index · Archive · About · Contact`), copy *"Kostenloser Website-Check"*, and `#8fb5fa` structural dividers.
