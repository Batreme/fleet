# UI & UX Architecture: tej-as_story

## Overview & Design Identity
- **Target**: `tej-as_story` (**The testimony and autobiography of Tejas Kumar**)
- **Production URL**: [https://tej.as/story](https://tej.as/story)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0708` / `#4a4441`)
- **Summary**: Tejas Kumar died at 4 and was revived, got about 19 days of school a year, and is now an AI engineer at IBM. His full testimony, in 39 ch...
- **Total Clean CSS Variables Extracted**: `148` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Jost`
- **Body Font Stack**: `Switzer`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: CSS variables `--font-display: "Jost", "Futura", "Century Gothic", "Trebuchet MS", system-ui, sans-serif`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)
- **Body Copy**: CSS variables `--font-body: "Switzer", "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif`, `--t-body: clamp(1.125rem, 1.3vw, 1.3125rem)`, `--lh-body: 1.62`
- **Metadata & Labels**: CSS variables `--fg-label: color-mix(in srgb, var(--fg-2) 72%, var(--fg))`, `--font-mono: "Geist Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`, `--t-small: clamp(.9375rem, 1vw, 1rem)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0708` | `var(--void)` in `:root` |
| **Primary Typography Ink** | `#161012` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#2a2426` | `var(--rule-dark)` in `:root` |
| **Interactive Accent / Highlight** | `#4a4441` | `var(--rule-dark-lit)` in `:root` |
| **Secondary / Muted Copy** | `#f2efe9` | `var(--bone)` in `:root` |
| **Structural Hairline Border** | `#a39b98` | `var(--ash)` in `:root` |
| **Variable Token (`--ash-dim`)** | `#8c8481` | `var(--ash-dim)` in `:root` |
| **Variable Token (`--paper`)** | `#f4f1ea` | `var(--paper)` in `:root` |
| **Variable Token (`--paper-2`)** | `#e8e4da` | `var(--paper-2)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--accent` | `var(--on-red)` | Brand / Palette Token |
| `--fg-2` | `var(--on-red-2)` | Typography Ink Token |
| `--fg-3` | `var(--on-red-2)` | Typography Ink Token |
| `--fg` | `var(--on-red)` | Typography Ink Token |
| `--focus` | `var(--on-red)` | Design System Custom Token |
| `--gold-fg` | `var(--gold)` | Typography Ink Token |
| `--mark` | `var(--gold)` | Design System Custom Token |
| `--void` | `#0a0708` | Color / Atmospheric Token |
| `--ink` | `#161012` | Typography Ink Token |
| `--rule-dark` | `#2a2426` | Canvas / Surface Token |
| `--rule-dark-lit` | `#4a4441` | Canvas / Surface Token |
| `--bone` | `#f2efe9` | Color / Atmospheric Token |
| `--ash` | `#a39b98` | Color / Atmospheric Token |
| `--ash-dim` | `#8c8481` | Color / Atmospheric Token |
| `--paper` | `#f4f1ea` | Canvas / Surface Token |
| `--paper-2` | `#e8e4da` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.topbar> — `tej-as_story`)**:
   - Landmark `<header class="topbar">` hosting `The testimony and autobiography of T` navigation (`Speaking · Story · Podcast · Blog · Book Fluent React`), DOM attributes (`data-theme="light"`, `data-track="Nav Click"`, `data-track-label="Wordmark"`, `data-track-href="/"`), and stylesheet rule `after { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.relative> — `The thread .`)**:
   - Landmark `<section class="relative isolate">` presenting display lead `The thread .` and copy excerpt *"More Speaking Talks, topics and fees Calendar Where I'll be next "* over `#0a0708` canvas and `#f2efe9` ink.
3. **Primary Showcase & Content Grid (<section.summary> — `The short version.`)**:
   - Landmark `<section class="summary">` rendering section `The short version.` with copy *"Speaking Talks, topics and fees"*, asset references (`favicon.svg`, `story`, `array.js`, `jost-var.woff2`), and grid rule `body { line-height:inherit;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<section.border-t> — `Contents`)**:
   - Landmark `<section class="border-t border-hairline">` framing `Contents` and `Before` (*"Talks, topics and fees"*) with `#2a2426` surface cards, `#4a4441` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://tej.as/story`)**:
   - Landmark `<footer class="border-t border-hairline">` anchoring `The testimony and autobiography ` footer links (`Speaking · Story · Podcast · Blog · Book Fluent React`), copy *"Calendar Where I'll be next"*, and `#a39b98` structural dividers.
