---
title: "UI & Design System: wiro-ae"
date: 2026-11-15
target: "wiro-ae"
---

# UI Architecture & Design Tokens: wiro-ae

> Ground-truth CSS custom properties and DOM layout primitives extracted from `wiro-ae` (`Wiro · Operating System for All Agencies`). All values are sanitized, deduplicated, and mapped to their semantic UI roles. Also see [UI Prompt Blueprint](prompt-blueprint.md).

## 🎨 Design Tokens (CSS Variables)

| Token Name | Extracted Value | Semantic UI Role |
|---|---|---|
| `--font-heading` | `var(--font-bricolage),"Bricolage Grotesque",sans-serif` | Primary display heading font stack |
| `--font-ui` | `var(--font-dmsans),"DM Sans",Arial,Helvetica,sans-serif` | UI controls & body copy font stack |
| `--solar-stroke-width` | `2.5` | Custom stroke weight for vector UI icons |
| `--wiro-ink` | `#10100f` | Primary deep charcoal ink |
| `--wiro-muted` | `rgba(16,16,15,.52)` | Muted label & description ink |
| `--wiro-canvas` | `#f6efe3` | Warm paper viewport canvas |
| `--wiro-surface` | `#f6efe3` | Primary container surface |
| `--wiro-surface-2` | `#ece5da` | Secondary recessed bento card surface |
| `--wiro-border` | `rgba(16,16,15,.12)` | 1px structural card & table border |
| `--wiro-pink` | `#efacd4` | Pastel pink accent for Projects module |
| `--wiro-yellow` | `#f6d94e` | Warm yellow accent for Finance module |
| `--wiro-sage` | `#9caf63` | Sage green accent for Clients module |
| `--wiro-blue` | `#a9c5e9` | Sky blue accent for Team/Docs module |
| `--wiro-radius-lg` | `18px` | Outer OS window & section border radius |
| `--wiro-radius-md` | `12px` | Inner card & button border radius |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `lj-bar-links` |
| `<nav>` | `-` | `lp-scatter` |
| `<main>` | `-` | `lp-page` |
| `<section>` | `-` | `wi` |
| `<section>` | `-` | `lp-hero` |
| `<section>` | `pages` | `lp-section lp-pages` |
| `<section>` | `waitlist` | `lp-section lp-waitlist` |
| `<footer>` | `-` | `lp-footer lp-footer-scatter` |
