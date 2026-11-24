---
title: "UI & UX Architecture: www-offforum-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-offforum-com

## Overview & Design Identity
- **Target**: `www-offforum-com` (**A WEEK OF DESIGN, ART & DIGITAL CULTURE · FORUM · SEPT 15, 2027 · OFFF S...**)
- **Production URL**: [https://www.offforum.com/](https://www.offforum.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×1656px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#808080` accent)
- **Summary**: A one-week festival convening designers, artists, and digital culture practitioners.
- **Total Clean CSS Variables Extracted**: `149` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Forvm`
- **Body Font Stack**: `Baikal`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 45px`, `line-height: 43px`, `font-weight: 400`, `letter-spacing: -0.9px`); CSS variables `--text-h1-mobile-offf: 3.2rem`, `--text-h1-mobile-offf--line-height: 3.1rem`, `--text-h1-mobile-offf--font-weight: 600`
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 32px`, `line-height: 31px`, `font-weight: 600`, `letter-spacing: -1.28px`); CSS variables `--text-h2-mobile-offf: 3.2rem`, `--text-h2-mobile-offf--line-height: 3.1rem`, `--text-h2-mobile-offf--font-weight: 600`; rule `h2` (`font-size: var(--text-body-mobile)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`, `font-weight: var(--tw-font...`)
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: 15px`, `font-weight: 400`); CSS variables `--text-body-mobile: 1.8rem`, `--text-body-mobile--line-height: 2rem`, `--text-body-mobile--font-weight: 600`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10px`, `line-height: 15px`, `font-weight: 400`); CSS variables `--text-body-mobile--letter-spacing: -.04em`, `--text-body-desktop--letter-spacing: -.04em`, `--text-body-2-mobile--letter-spacing: -.02em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ff0000` | `.bg-red { background-color: red }` (`#ff0000`) |
| **Interactive Accent / Highlight** | `#808080` | `.button-basic-primary:disabled { background-color: grey }` (`#808080`) |
| **Secondary / Muted Copy** | `#808080` | `.button-basic-secondary:disabled { color: grey }` (`#808080`) |
| **Structural Hairline Border** | `#808080` | `.button-basic-primary:disabled { border-color: #808080 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--spacing` | `.1rem` | Layout / Spatial Grid Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--ease-in-out` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--aspect-video` | `16 / 9` | Design System Custom Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--font-baikal` | `"Baikal", sans-serif` | Typography / Scale Token |
| `--font-forvm` | `"Forvm", serif` | Typography / Scale Token |
| `--text-body-mobile` | `1.8rem` | Typography Ink Token |
| `--text-body-mobile--line-height` | `2rem` | Typography Ink Token |
| `--text-body-mobile--font-weight` | `600` | Typography Ink Token |
| `--text-body-mobile--letter-spacing` | `-.04em` | Typography Ink Token |
| `--text-body-desktop` | `2.4rem` | Typography Ink Token |
| `--text-body-desktop--line-height` | `2.6rem` | Typography Ink Token |
| `--text-body-desktop--font-weight` | `600` | Typography Ink Token |
| `--text-body-desktop--letter-spacing` | `-.04em` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `www-offforum-com`)**:
   - Landmark `<header class="header h-header-height">` (`1440x120px`) hosting `A WEEK OF DESIGN, ART & DIGITAL CULT` navigation (`About`), DOM attributes (`data-svg-origin="609.3610229492188 0"`, `data-svg-origin="-0.09765620529651642..."`, `data-nuxt-data="nuxt-app"`, `data-ssr="true"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.min-h-screen> — `A WEEK OF DESIGN, ART & DIGITAL CU`)**:
   - Landmark `<main class="min-h-screen">` presenting display lead `A WEEK OF DESIGN, ART & DIGITAL CULTURE · FORUM ·...` and copy excerpt *"©OFFFORUM 2026. All rights reserved."* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.min-h-screen:nth(2)> — `Join our community and get updates`)**:
   - Landmark `<main class="min-h-screen">` rendering section `Join our community and get updates, offers, and e...` with copy *"GET YOUR FORUM TICKET"*, asset references (`gtm.js`, `entry.CI2s3_W4.css`, `_payload.json`, `f8tcD554.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.min-h-screen:nth(3)> — `GET YOUR FORUM TICKET`)**:
   - Landmark `<main class="min-h-screen">` framing `GET YOUR FORUM TICKET` and `www-offforum-com Archive & Directory` (*"Join our community and get updates, offers, and e..."*) with `#ff0000` surface cards, `#808080` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.container-main> — `https://www.offforum.com/`)**:
   - Landmark `<footer class="container-main">` anchoring `A WEEK OF DESIGN, ART & DIGITAL ` footer links (`About`), copy *"GET YOUR FORUM TICKET"*, and `#808080` structural dividers.
