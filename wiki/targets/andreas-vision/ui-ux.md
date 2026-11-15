# UI & UX Architecture: andreas-vision

## Overview & Design Identity
- **Target**: `andreas-vision` (**Andreas Kruszakin, growth-focused design engineer in Europe**)
- **Production URL**: [https://andreas.vision](https://andreas.vision)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#000000`)
- **Summary**: I'm Andreas, a growth-focused design engineer who is design first and builds the system underneath. I make founders' products easy to get...
- **Total Clean CSS Variables Extracted**: `39` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist Variable`
- **Body Font Stack**: `Geist Mono Variable`
- **Monospace / Technical Font Stack**: `Geist Mono Variable`
- **Hero Display (`H1`)**: not extracted from static CSS (sized via runtime/utility classes)
- **Section Heading (`H2`)**: not extracted from static CSS (sized via runtime/utility classes)
- **Body Copy**: not extracted from static CSS (sized via runtime/utility classes)
- **Metadata & Labels**: CSS variables `--font-brand-mono: "Geist Mono Variable", ui-monospace, monospace`, `--label-color: var(--palette-b60)`, `--labels: 0`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `html { background: #fff }` |
| **Primary Typography Ink** | `#000000` | `body` default contrast ink (`#000000`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Geist Variable", -apple-system, system-ui, sans-serif` | Typography / Scale Token |
| `--font-brand` | `"Geist Variable", -apple-system, system-ui, sans-serif` | Brand / Palette Token |
| `--font-brand-serif` | `"Newsreader Variable", Georgia, serif` | Brand / Palette Token |
| `--font-brand-mono` | `"Geist Mono Variable", ui-monospace, monospace` | Brand / Palette Token |
| `--font-site` | `"Geist Variable", -apple-system, system-ui, sans-serif` | Typography / Scale Token |
| `--font-site-highlight` | `"TRJN DaVinci", "Newsreader Variable", Georgia, serif` | Canvas / Surface Token |
| `--screens` | `1.8` | Design System Custom Token |
| `--peek` | `80px` | Dimension / Scale Token |
| `--word` | `500ms` | Motion / Timing Token |
| `--stagger` | `70ms` | Motion / Timing Token |
| `--delay` | `120ms` | Motion / Easing Token |
| `--out` | `0` | Design System Custom Token |
| `--bio` | `1` | Design System Custom Token |
| `--radius` | `28px` | Elevation / Border Token |
| `--tile-radius` | `16px` | Elevation / Border Token |
| `--tile-aspect` | `1.5` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top> — `andreas-vision`)**:
   - Landmark `<header class="top">` hosting `Andreas Kruszakin, growth-focused de` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-selection-ink`, `data-emotion="css-global"`, `data-s`, `data-emotion="css-global"`), and stylesheet rule `root { height: 100%; margin: 0; }`.
2. **Hero Stage & Focal Lead (<section.e5sioty0> — `Designer who ships with vision Des`)**:
   - Landmark `<section class="e5sioty0 css-8jf4oe">` presenting display lead `Designer who ships with vision Design Engineer wh...` and copy excerpt *"Designer who ships with vision"* over `#fff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.swap> — `Work`)**:
   - Landmark `<section class="swap css-1eowax1">` rendering section `Work` with copy *"Design Engineer who ships growth"*, asset references (`llms.txt`, `icon-192.png`, `favicon.ico`, `favicon.svg`), and grid rule `html { background: fff; }`.
4. **Interactive Detail & Feature Matrix (<section.swap> — `Built to move`)**:
   - Landmark `<section class="swap css-1yyyvev">` framing `Built to move` and `Beyond work` (*"I'm Andreas, making precise, joyful interfaces and the tools to b"*) with `#fff` surface cards, `#000000` accents, and `header { border-color: #000000; }`.
5. **Colophon & Global Directory Footer (<footer.css-za9d9j> — `https://andreas.vision`)**:
   - Landmark `<footer class="css-za9d9j e154gxt60">` anchoring `Andreas Kruszakin, growth-focuse` footer links (`Overview · Index · Archive · About · Contact`), copy *"Cheval Inbox Canvas Arrange Share 2. Inbox: crit and variant"*, and `#000000` structural dividers.
