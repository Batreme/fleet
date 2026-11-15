# UI & UX Architecture: useguidely-co

## Overview & Design Identity
- **Target**: `useguidely-co` (**guidely - the hospitality of the future**)
- **Production URL**: [https://useguidely.co/](https://useguidely.co/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#1f1d1a` canvas, `#fff` ink, `#222` accent)
- **Summary**: A smart guest app that answers questions any hour, recommends what is good right now, plans the day and takes room orders, all from one l...
- **Total Clean CSS Variables Extracted**: `14` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Satoshi`
- **Body Font Stack**: `PP Mori`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-display: Georgia,"Times New Roman",serif`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)
- **Body Copy**: CSS variables `--font-body: system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif`
- **Metadata & Labels**: CSS variables `--font-mono: ui-monospace,SFMono-Regular,Menlo,monospace`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#1f1d1a` | `var(--brand)` in `:root` |
| **Primary Typography Ink** | `#9b7b4d` | `var(--accent)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--surface)` in `:root` |
| **Interactive Accent / Highlight** | `#222` | `var(--ink)` in `:root` |
| **Secondary / Muted Copy** | `#6f6f6f` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#e5e7eb` | `:before { border: #e5e7eb }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--brand` | `#1f1d1a` | Brand / Palette Token |
| `--accent` | `#9b7b4d` | Brand / Palette Token |
| `--surface` | `#fff` | Canvas / Surface Token |
| `--ink` | `#222` | Typography Ink Token |
| `--muted` | `#6f6f6f` | Color / Atmospheric Token |
| `--line` | `rgba(0,0,0,.08)` | Color / Atmospheric Token |
| `--font-display` | `Georgia,"Times New Roman",serif` | Typography / Scale Token |
| `--vintage-filter` | `sepia(0.24) saturate(1.1) contrast(1.04) brightness(1.02)` | Design System Custom Token |
| `--hop` | `center 42%` | Dimension / Scale Token |
| `--font-name` | `system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif` | Typography / Scale Token |
| `--font-body` | `system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif` | Typography / Scale Token |
| `--font-mono` | `ui-monospace,SFMono-Regular,Menlo,monospace` | Typography / Scale Token |
| `--hero-ready` | `1` | Design System Custom Token |
| `--reveal-delay` | `0ms` | Motion / Easing Token |
| `--useguidely-co-bg` | `#1f1d1a` | Canvas Substrate (from `var(--brand)` in `:root`) |
| `--useguidely-co-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.relative> — `useguidely-co`)**:
   - Landmark `<header class="relative mx-auto">` hosting `guidely - the hospitality of the fut` navigation (`Home · About · Hotels & lodges · Features · Pricing`), DOM attributes (`data-precedence="next"`, `data-foldout-prefetch`, `data-spark="true"`, `data-reveal="stagger"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.hero-sec> — `The smart app for your guests.`)**:
   - Landmark `<section class="hero-sec mx-auto">` presenting display lead `The smart app for your guests.` and copy excerpt *"Check-in, Wi-Fi, house details, local recommendations, guest ques"* over `#1f1d1a` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.mt-12> — `What is a smart app?`)**:
   - Landmark `<section class="mt-12">` rendering section `What is a smart app?` with copy *"Smart picks for right now"*, asset references (`logo.png`, `hero-cover-19.jpg`, `001c094435c96c6a.css`, `webpack-61e7ac9f112b97ad.js`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.mx-auto> — `B&Bs & guest houses`)**:
   - Landmark `<section class="mx-auto px-6">` framing `B&Bs & guest houses` and `Boutique hotels` (*"Experiences & activities"*) with `#fff` surface cards, `#222` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.mt-16> — `https://useguidely.co/`)**:
   - Landmark `<footer class="mt-16">` anchoring `guidely - the hospitality of the` footer links (`Home · About · Hotels & lodges · Features · Pricing`), copy *"Room service ordering"*, and `#e5e7eb` structural dividers.
