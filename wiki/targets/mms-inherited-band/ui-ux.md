# UI & UX Architecture: mms-inherited-band

## Overview & Design Identity
- **Target**: `mms-inherited-band` (**INHERITED – ME, MYSELF & SAM (EP DEBUT)**)
- **Production URL**: [https://mms.inherited.band/](https://mms.inherited.band/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0909` / `#0000`)
- **Summary**: A cinematic deathcore EP built around three stories, three characters, and a world of evidence. Me, Myself and Sam turns music into an in...
- **Total Clean CSS Variables Extracted**: `13` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Founder Grotesk`
- **Body Font Stack**: `Founder Grotesk Mono`
- **Monospace / Technical Font Stack**: `Founder Grotesk Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `2rem`, `2.5rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `2rem`, `2.5rem`)
- **Body Copy**: rule `,body` (`font-size: 16px`)
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0909` | `.loader__background.svelte-1ojmd8e { background: #0a0909 }` |
| **Primary Typography Ink** | `#fffdf6` | `.icon-play.svelte-1kqkx9o { fill: #fffdf6 }` |
| **Elevated Surface / Card Substrate** | `#000` | `.video-modal.svelte-1rnt8or { background-color: #000 }` |
| **Interactive Accent / Highlight** | `#0000` | `textarea { background-color: #0000 }` |
| **Secondary / Muted Copy** | `#262424` | `.tc--dark-grey { color: #262424 }` |
| **Structural Hairline Border** | `#323030` | `.tc--grey { color: #323030 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--bw` | `100vw` | Dimension / Scale Token |
| `--max-container` | `100vw` | Layout / Spatial Grid Token |
| `--outer-margin` | `24px` | Layout / Spatial Grid Token |
| `--grid-gap` | `0px` | Layout / Spatial Grid Token |
| `--grid-size` | `calc(var(--bw) - (var(--outer-margin) * 2))` | Layout / Spatial Grid Token |
| `--grid-max-size` | `calc(var(--max-container) - (var(--outer-margin) * 2))` | Layout / Spatial Grid Token |
| `--image-height` | `min(80vw / var(--image-ratio), 60lvh)` | Layout / Spatial Grid Token |
| `--progress` | `50%` | Dimension / Scale Token |
| `--tw-rotate-x` | `initial` | Design System Custom Token |
| `--mms-inherited-ba-bg` | `#0a0909` | Canvas Substrate (from `.loader__background.svelte-1ojmd8e { background: #0a0909 }`) |
| `--mms-inherited-ba-ink` | `#fffdf6` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.app> — `mms-inherited-band`)**:
   - Landmark `<header class="app">` hosting `INHERITED – ME, MYSELF & SAM (EP DEB` navigation (`IG · TIKTOK · inherited.band · INHERITED.BAND`), DOM attributes (`data-sveltekit-preload-data="hover"`, `data-engine="three.js r180"`, `data-cta-audio`), and stylesheet rule `.webgl-container.svelte-hy9597 { z-index:1;width:100vw;height:100lvh;position:fixed;top:0;left:0 }`.
2. **Hero Stage & Focal Lead (<section.sr-only> — `INHERITED – ME, MYSELF & SAM (EP D`)**:
   - Landmark `<section class="sr-only">` presenting display lead `INHERITED – ME, MYSELF & SAM (EP DEBUT)` and copy excerpt *"This experience requires JavaScript and WebGL. Please enable Java"* over `#0a0909` canvas and `#fffdf6` ink.
3. **Primary Showcase & Content Grid (<section.sr-only> — `THE UNIDENTIFIED SUBJECT`)**:
   - Landmark `<section class="sr-only">` rendering section `THE UNIDENTIFIED SUBJECT` with copy *"For adults (18+) only. Inspired by true crime, this fictional exp"*, asset references (`FoundersGrotesk-Medium.woff2`, `FoundersGroteskMono-Regular.woff2`, `favicon.ico`, `favicon.svg`), and grid rule `.webgl-container__canvas.svelte-h... { width:100%;height:100% }`.
4. **Interactive Detail & Feature Matrix (<section.sr-only> — `OPEN CALL`)**:
   - Landmark `<section class="sr-only">` framing `OPEN CALL` and `THE MODEL CITIZEN` (*"The individual may appear calm and approachable, often using a ve"*) with `#000` surface cards, `#0000` accents, and `.audio-ctas.svelte-186a61h { align-items:center;gap:1.5rem;margin-top:2rem;display:flex }`.
5. **Colophon & Global Directory Footer (<footer.svelte-hy9597> — `https://mms.inherited.band/`)**:
   - Landmark `<footer class="svelte-hy9597">` anchoring `INHERITED – ME, MYSELF & SAM (EP` footer links (`IG · TIKTOK · inherited.band · INHERITED.BAND`), copy *"Do not approach. If you recognize this individual, contact i"*, and `#323030` structural dividers.
