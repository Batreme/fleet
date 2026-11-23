---
title: "UI & UX Architecture: yoloexe-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: yoloexe-com

## Overview & Design Identity
- **Target**: `yoloexe-com` (**YOLO — DxL**)
- **Production URL**: [https://yoloexe.com](https://yoloexe.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0014` / `#00f0ff`)
- **Summary**: A loud, scrolling crash course in YOLO: how computers spot things in pictures, in one look. Then run 27 real YOLO models in your browser.
- **Total Clean CSS Variables Extracted**: `29` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Bungee Shade`
- **Body Font Stack**: `Space Grotesk`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 234px`, `line-height: 257.4px`, `font-weight: 400`); CSS variables `--display: "Bungee", "Impact", system-ui, sans-serif`; rule `.title` (`letter-spacing: -.01em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 73.44px`, `font-weight: 400`, `letter-spacing: -0.72px`); rule `h2` (`font-size: clamp(30px,4.4vw,54px)`, `line-height: 1`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 27.9px`, `font-weight: 400`); CSS variables `--body: "Space Grotesk", ui-sans-serif, system-ui, sans-serif`; rule `p` (`font-size: 19px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 27.9px`, `font-weight: 400`); CSS variables `--mono: "Space Mono", ui-monospace, monospace`; rule `small` (`font-size: 14px`, `letter-spacing: .2em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0014` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fff6fd` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ff2bd6` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#00f0ff` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#ff2bd6` | `var(--pink)` in `:root` |
| **Structural Hairline Border** | `#3b3343` | `code { border: #3b3343 }` |
| **Variable Token (`--muted`)** | `#c9b6dd` | `var(--muted)` in `:root` |
| **Variable Token (`--acid`)** | `#e6ff00` | `var(--acid)` in `:root` |
| **Variable Token (`--orange`)** | `#ff7a1a` | `var(--orange)` in `:root` |
| **Variable Token (`--violet`)** | `#8a2bff` | `var(--violet)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dxl-bg` | `var(--dxlBg)` | Canvas / Surface Token |
| `--dxl-fg` | `var(--dxlFg)` | Typography Ink Token |
| `--dxl-accent` | `var(--dxlAccent)` | Brand / Palette Token |
| `--bg` | `#0a0014` | Canvas / Surface Token |
| `--ink` | `#fff6fd` | Typography Ink Token |
| `--muted` | `#c9b6dd` | Color / Atmospheric Token |
| `--pink` | `#ff2bd6` | Typography Ink Token |
| `--cyan` | `#00f0ff` | Color / Atmospheric Token |
| `--acid` | `#e6ff00` | Color / Atmospheric Token |
| `--orange` | `#ff7a1a` | Color / Atmospheric Token |
| `--violet` | `#8a2bff` | Color / Atmospheric Token |
| `--card` | `rgba(14, 0, 32, .78)` | Color / Atmospheric Token |
| `--display` | `"Bungee", "Impact", system-ui, sans-serif` | Dimension / Scale Token |
| `--shade` | `"Bungee Shade", "Bungee", "Impact", system-ui, sans-serif` | Dimension / Scale Token |
| `--body` | `"Space Grotesk", ui-sans-serif, system-ui, sans-serif` | Dimension / Scale Token |
| `--mono` | `"Space Mono", ui-monospace, monospace` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.dots> — `yoloexe-com`)**:
   - Landmark `<nav class="dots">` (`11x231px`) hosting `YOLO — DxL` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r180"`, `data-yolo="button"`, `data-yolo="button"`, `data-i="0"`), and stylesheet rule `html { scroll-behavior:auto;overflow-x:clip }`.
2. **Hero Stage & Focal Lead (<section.chap> — `YOLO EDITION`)**:
   - Landmark `<section class="chap hero">` presenting display lead `YOLO EDITION` and copy excerpt *"🔊 This one talks. Turn your sound up."* over `#0a0014` canvas and `#fff6fd` ink.
3. **Primary Showcase & Content Grid (<section.chap:nth(2)> — `YOU ONLY LOOK ONCE`)**:
   - Landmark `<section class="chap">` rendering section `YOU ONLY LOOK ONCE` with copy *"How computers spot things in pictures. Then try it on your camera"*, asset references (`favicon.svg`, `apple-touch-icon.png`, `sitemap-index.xml`, `script.js`), and grid rule `body { margin:0;background:var(--bg);color:var(--ink);font-family:var(--body);f... }`.
4. **Interactive Detail & Feature Matrix (<section.chap:nth(3)> — `NOW YOU KNOW YOLO.`)**:
   - Landmark `<section class="chap">` framing `NOW YOU KNOW YOLO.` and `YOUR TURN.` (*"This is how YOLO works"*) with `#ff2bd6` surface cards, `#00f0ff` accents, and `selection { background:var(--acid);color:000 }`.
5. **Colophon & Global Directory Footer (<footer.hud> — `https://yoloexe.com`)**:
   - Landmark `<footer class="hud">` anchoring `YOLO — DxL` footer links (`Overview · Index · Archive · About · Contact`), copy *"Cut the picture into a grid"*, and `#3b3343` structural dividers.
