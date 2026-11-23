---
title: "UI & UX Architecture: launch-joinautopilot-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: launch-joinautopilot-com

## Overview & Design Identity
- **Target**: `launch-joinautopilot-com` (**Home**)
- **Production URL**: [https://launch.joinautopilot.com](https://launch.joinautopilot.com)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0d0d0d` / `#0082f3`)
- **Summary**: Instant access to the world's capital. Become a Pilot and launch your first fund in minutes. Join top performers managing $1.2B+ in assets.
- **Total Clean CSS Variables Extracted**: `465` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `FKGrotesk`
- **Body Font Stack**: `FKGrotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 140.001px`, `line-height: 140.001px`, `font-weight: 400`, `letter-spacing: -8.40003px`); CSS variables `--_design-system---font-size--h1: clamp(5.75rem,4.98529rem + 3.13726vw,8.75rem)`, `--_design-system---line-height--h1: 1`, `--_design-system---font-weight--h1: 400`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80.0004px`, `line-height: 81.6004px`, `font-weight: 400`, `letter-spacing: -4.00002px`); CSS variables `--_design-system---font-size--h2: clamp(3.5rem,3.11765rem + 1.56863vw,5rem)`, `--_design-system---line-height--h2: 1.02`, `--_design-system---font-weight--h2: 400`; rule `h2` (`font-size: var(--font-size-h3)`, `line-height: var(--line-height-h3-...`, `letter-spacing: var(--letter-spacing-...`)
- **Body Copy**: live computed `body` (`font-size: 16.0001px`, `line-height: 20.8001px`, `font-weight: 400`, `letter-spacing: -0.160001px`); CSS variables `--_design-system---font-size--body: clamp(.875rem,.843137rem + .130719vw,1rem)`, `--_design-system---line-height--body: 1.3`, `--_design-system---font-weight--body: 400`; rule `,p` (`font-size: var(--font-size-body)`, `line-height: var(--line-height-body)`, `letter-spacing: var(--letter-spacing-...`, `font-weight: var(--font-we...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16.0001px`, `line-height: 20.8001px`, `font-weight: 400`, `letter-spacing: -0.160001px`); CSS variables `--_design-system---letter-spacing--body: -.01em`, `--_design-system---letter-spacing--h1: -.06em`, `--_design-system---letter-spacing--h2: -.05em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0d0d0d` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f1f2f3` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#141414` | `var(--button-on-light-solid-bg-hover)` in `:root` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Structural Hairline Border** | `#0c0c0c` | `var(--_design-system---role--border-subtle)` in `:root` (`00000014`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_design-system---role--bg` | `var(--_design-system---color--surface-background)` | Canvas / Surface Token |
| `--_design-system---font--primary` | `Fkgrotesk,Arial,sans-serif` | Brand / Palette Token |
| `--_design-system---role--fg` | `var(--_design-system---color--primary-dark)` | Typography Ink Token |
| `--_design-system---font-size--body` | `clamp(.875rem,.843137rem + .130719vw,1rem)` | Typography / Scale Token |
| `--_design-system---line-height--body` | `1.3` | Typography / Scale Token |
| `--_design-system---font-weight--body` | `400` | Typography / Scale Token |
| `--_design-system---letter-spacing--body` | `-.01em` | Typography / Scale Token |
| `--_design-system---font-size--h1` | `clamp(5.75rem,4.98529rem + 3.13726vw,8.75rem)` | Typography / Scale Token |
| `--_design-system---line-height--h1` | `1` | Typography / Scale Token |
| `--_design-system---font-weight--h1` | `400` | Typography / Scale Token |
| `--_design-system---letter-spacing--h1` | `-.06em` | Typography / Scale Token |
| `--_design-system---font-size--h2` | `clamp(3.5rem,3.11765rem + 1.56863vw,5rem)` | Typography / Scale Token |
| `--_design-system---line-height--h2` | `1.02` | Typography / Scale Token |
| `--_design-system---font-weight--h2` | `400` | Typography / Scale Token |
| `--_design-system---letter-spacing--h2` | `-.05em` | Typography / Scale Token |
| `--_design-system---font-size--h3` | `clamp(2.375rem,2.08824rem + 1.17647vw,3.5rem)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header_wrap> — `launch-joinautopilot-com`)**:
   - Landmark `<header class="header_wrap">` (`1440x30px`) hosting `Home` navigation (`N e w s News · F A Q FAQ · Careers · Contact · X/Twitter`), DOM attributes (`data-wf-domain="launch.joinautopilot.com"`, `data-wf-page="6a2d51f45ce6148dcfffd71a"`, `data-wf-site="6a07168d6f6cfe1d38b6d627"`, `data-route="home"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.home_hero_wrap> — `Autopilot`)**:
   - Landmark `<section class="home_hero_wrap">` presenting display lead `Autopilot` and copy excerpt *"Become a Pilot and launch your first fund in minutes."* over `#0d0d0d` canvas and `#f1f2f3` ink.
3. **Primary Showcase & Content Grid (<section.steps_wrap> — `A u t o p i l o t`)**:
   - Landmark `<section class="steps_wrap l-section">` rendering section `A u t o p i l o t` with copy *"Instant access to the world’s capital."*, asset references (`cdn.prod.website-files.com`, `ob-autopilot.shared.8ecce8ba9.min...`, `6a316c0692d4727f15940a67_favicon.png`, `6a316c0605a3b4d0e37557a7_favicon.png`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.billackman_wrap> — `T h i s i s w h e r e i t g e t s `)**:
   - Landmark `<section class="billackman_wrap l-section">` framing `T h i s i s w h e r e i t g e t s f u n . This is...` and `P i c k y o u r s t o c k s . Pick your stocks.` (*"Become a Pilot and launch your first fund in minutes. Become a Pi"*) with `#141414` surface cards, `#0082f3` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.home_footer_wrap> — `https://launch.joinautopilot.com`)**:
   - Landmark `<footer class="home_footer_wrap l-section">` anchoring `Home` footer links (`N e w s News · F A Q FAQ · Careers · Contact · X/Twitter`), copy *"Become a Pilot and launch your"*, and `#0c0c0c` structural dividers.
