---
title: "UI & UX Architecture: mms-inherited-band"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: mms-inherited-band

## Overview & Design Identity
- **Target**: `mms-inherited-band` (**INHERITED – ME, MYSELF & SAM (EP DEBUT)**)
- **Production URL**: [https://mms.inherited.band/](https://mms.inherited.band/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#262424` / `#fffdf6`)
- **Summary**: A cinematic deathcore EP built around three stories, three characters, and a world of evidence. Me, Myself and Sam turns music into an in...
- **Total Clean CSS Variables Extracted**: `13` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Segoe UI`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `Founder Grotesk Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`); rule `,body` (`font-size: 16px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`); CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#262424` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fffdf6` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0a0909` | `.loader__background.svelte-1ojmd8e { background: #0a0909 }` |
| **Interactive Accent / Highlight** | `#fffdf6` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#b4b4b4` | `.tc--light-grey { color: #b4b4b4 }` |
| **Structural Hairline Border** | `#464443` | `.grid-helper__col-inner.svelte-... { border: #464443 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bw` | `100vw` | Dimension / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--max-container` | `100vw` | Layout / Spatial Grid Token |
| `--outer-margin` | `24px` | Layout / Spatial Grid Token |
| `--grid-gap` | `0px` | Layout / Spatial Grid Token |
| `--grid-size` | `calc(var(--bw) - (var(--outer-margin) * 2))` | Layout / Spatial Grid Token |
| `--grid-max-size` | `calc(var(--max-container) - (var(--outer-margin) * 2))` | Layout / Spatial Grid Token |
| `--image-height` | `min(80vw / var(--image-ratio), 60lvh)` | Layout / Spatial Grid Token |
| `--progress` | `50%` | Dimension / Scale Token |
| `--tw-rotate-x` | `initial` | Design System Custom Token |
| `--mms-inherited-ba-bg` | `#262424` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--mms-inherited-ba-ink` | `#fffdf6` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.app> — `mms-inherited-band`)**:
   - Landmark `<header class="app">` (`1440px`) hosting `INHERITED – ME, MYSELF & SAM (EP DEB` navigation (`IG · TIKTOK · inherited.band · INHERITED.BAND`), DOM attributes (`data-sveltekit-preload-data="hover"`, `data-engine="three.js r180"`, `data-cta-audio`), and stylesheet rule `.webgl-container.svelte-hy9597 { z-index:1;width:100vw;height:100lvh;position:fixed;top:0;left:0 }`.
2. **Hero Stage & Focal Lead (<section.sr-only> — `INHERITED – ME, MYSELF & SAM (EP D`)**:
   - Landmark `<section class="sr-only">` presenting display lead `INHERITED – ME, MYSELF & SAM (EP DEBUT)` and copy excerpt *"THE INDIVIDUAL MAY APPEAR CALM AND APPROACHABLE, OFTEN USING A VE"* over `#262424` canvas and `#fffdf6` ink.
3. **Primary Showcase & Content Grid (<section.sr-only:nth(2)> — `THE UNIDENTIFIED SUBJECT`)**:
   - Landmark `<section class="sr-only">` rendering section `THE UNIDENTIFIED SUBJECT` with copy *"The individual may appear calm and approachable, often using a ve"*, asset references (`FoundersGrotesk-Medium.woff2`, `FoundersGroteskMono-Regular.woff2`, `favicon.ico`, `favicon.svg`), and grid rule `.webgl-container__canvas.svelte-h... { width:100%;height:100% }`.
4. **Interactive Detail & Feature Matrix (<section.sr-only:nth(3)> — `THE MODEL CITIZEN`)**:
   - Landmark `<section class="sr-only">` framing `THE MODEL CITIZEN` and `Diego Castro` (*"Do not approach. If you recognize this individual, contact inheri"*) with `#0a0909` surface cards, `#fffdf6` accents, and `.audio-ctas.svelte-186a61h { align-items:center;gap:1.5rem;margin-top:2rem;display:flex }`.
5. **Colophon & Global Directory Footer (<footer.svelte-hy9597> — `https://mms.inherited.band/`)**:
   - Landmark `<footer class="svelte-hy9597">` anchoring `INHERITED – ME, MYSELF & SAM (EP` footer links (`IG · TIKTOK · inherited.band · INHERITED.BAND`), copy *"The individual may not appear to be the primary threat. He i"*, and `#464443` structural dividers.
