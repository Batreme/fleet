# UI & UX Architecture: www-glowingcheetah-com

## Overview & Design Identity
- **Target**: `www-glowingcheetah-com` (**Glowing Cheetah Studios · Father & Son Indie Game Studio**)
- **Production URL**: [https://www.glowingcheetah.com/](https://www.glowingcheetah.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#131313` canvas, `#FFFDB8` ink, `#FFFDB8` accent)
- **Summary**: Glowing Cheetah is a father and son indie studio making games, books and animation. Creators of Pigeon’s Mission, a pixel platformer on S...
- **Total Clean CSS Variables Extracted**: `84` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Thanks`
- **Body Font Stack**: `Circular Std`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: CSS variables `--font-display: "Thanks",Impact,"Arial Narrow",sans-serif`, `--text-display: clamp(56px,6.5vw,96px)`, `--text-h1: 56px`
- **Section Heading (`H2`)**: CSS variables `--text-h2: 40px`
- **Body Copy**: CSS variables `--text-body: var(--fg-2)`, `--font-body: "Circular Std",system-ui,sans-serif`, `--leading-body: 1.5`; rule `body` (`font-size: var(--text-body)`, `line-height: var(--leading-body)`)
- **Metadata & Labels**: CSS variables `--font-mono: "SF Mono",Menlo,Consolas,monospace`, `--text-small: 14px`, `--text-caption: 12px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#131313` | `var(--night-deep)` in `:root` |
| **Primary Typography Ink** | `#1F1F1F` | `var(--night)` in `:root` |
| **Elevated Surface / Card Substrate** | `#2A2A2A` | `var(--night-2)` in `:root` |
| **Interactive Accent / Highlight** | `#FFFDB8` | `var(--yellow)` in `:root` |
| **Secondary / Muted Copy** | `#D5B123` | `var(--yellow-glow)` in `:root` |
| **Structural Hairline Border** | `#B8981C` | `var(--yellow-deep)` in `:root` |
| **Variable Token (`--ember`)** | `#DF7042` | `var(--ember)` in `:root` |
| **Variable Token (`--white`)** | `#FFFFFF` | `var(--white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--night-deep` | `#131313` | Color / Atmospheric Token |
| `--night` | `#1F1F1F` | Color / Atmospheric Token |
| `--night-2` | `#2A2A2A` | Color / Atmospheric Token |
| `--yellow` | `#FFFDB8` | Color / Atmospheric Token |
| `--yellow-glow` | `#D5B123` | Color / Atmospheric Token |
| `--yellow-deep` | `#B8981C` | Color / Atmospheric Token |
| `--ember` | `#DF7042` | Color / Atmospheric Token |
| `--white` | `#FFFFFF` | Canvas / Surface Token |
| `--ink` | `#1F1F1F` | Typography Ink Token |
| `--fg-1` | `#FFFFFF` | Typography Ink Token |
| `--fg-2` | `rgba(255,255,255,.72)` | Typography Ink Token |
| `--fg-3` | `rgba(255,255,255,.48)` | Typography Ink Token |
| `--line-1` | `rgba(255,255,255,.12)` | Color / Atmospheric Token |
| `--line-2` | `rgba(255,255,255,.24)` | Color / Atmospheric Token |
| `--ink-1` | `#1F1F1F` | Typography Ink Token |
| `--ink-2` | `rgba(31,31,31,.72)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.gc-rv> — `www-glowingcheetah-com`)**:
   - Landmark `<nav class="gc-rv">` hosting `Glowing Cheetah Studios · Father & S` navigation (`Projects · Team · Contact`), DOM attributes (`data-dc-tpl="1"`, `data-sc-name="Root"`, `data-dc-tpl="2"`, `data-dc-tpl="3"`), and stylesheet rule `l.sc-dc-streaming .sc-interp.sc-m... { position:relative; background:color-mix(in srgb,currentColor 5%,transpar... }`.
2. **Hero Stage & Focal Lead (<section.sc-host> — `We craft stories`)**:
   - Landmark `<section class="sc-host">` presenting display lead `We craft stories` and copy excerpt *"We're a father and son creative studio bringing stories to life t"* over `#131313` canvas and `#FFFDB8` ink.
3. **Primary Showcase & Content Grid (<section.gc-skip> — `An indie studio`)**:
   - Landmark `<section class="gc-skip">` rendering section `An indie studio` with copy *"Fly into a world of excitement as Archie embarks on a mission to "*, asset references (`clarity.js`, `ylwyja15eg`, `icon.svg`, `favicon-32.png`), and grid rule `before { animation:none; background:color-mix(in srgb,currentColor 8%,transparent) }`.
4. **Interactive Detail & Feature Matrix (<section.gc-intro__panel> — `Pigeon's Mission`)**:
   - Landmark `<section class="gc-intro__panel">` framing `Pigeon's Mission` and `The Known Sector` (*"A sci-fi epic rooted in Afrofuturism about three interconnected i"*) with `#2A2A2A` surface cards, `#FFFDB8` accents, and `.sc-host.sc-has-error { position:relative }`.
5. **Colophon & Global Directory Footer (<footer.gc-sr> — `https://www.glowingcheetah.com/`)**:
   - Landmark `<footer class="gc-sr">` anchoring `Glowing Cheetah Studios · Father` footer links (`Projects · Team · Contact`), copy *"When Logan was five, he beat Mario Odyssey for the first tim"*, and `#B8981C` structural dividers.
