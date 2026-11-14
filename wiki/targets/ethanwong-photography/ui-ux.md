---
title: "UI & Design System: ethanwong-photography"
date: 2026-11-14
target: "[[overview|ethanwong-photography]]"
---

# UI Architecture & Design Tokens: ethanwong-photography

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--fit-lh` | `1` |
| `--fit-reserve` | `0px` |
| `--red` | `#9b1120` |
| `--red-hover` | `#b3162a` |
| `--red-lift` | `#ab182c` |
| `--red-lift-hover` | `#c01f34` |
| `--red-deep` | `#8a0f1e` |
| `--lab-nav` | `13px` |
| `--lab` | `12px` |
| `--lab-sm` | `11px` |
| `--lab-dock` | `9.5px` |
| `--lab-quiet` | `10px` |
| `--lab-w` | `400` |
| `--lab-w-nav` | `400` |
| `--lab-w-dock` | `500` |
| `--head-band` | `74px` |
| `--foot-band` | `58px` |
| `--lap-vh` | `100vw}@media(max-width:640px),(pointer:coarse)and (max-heigh` |
| `--red-hover` | `var(--red-lift-hover)}.mo .lab,.mo button{font-weight:var(--` |
| `--mark-dot` | `max(3px, .115em)` |
| `--mark-dot-ink` | `var(--red)}header.site.nav-on-dark .logo,.mo #menuLogo{--mar` |
| `--red` | `var(--red-lift)` |
| `--red-hover` | `var(--red-lift-hover)}html.menu-open header.site .h-left,htm` |
| `--dock-span` | `min( calc(100% - 22px) , 434px)` |
| `--dock-indent` | `49px}.dock-cat--sub{position:relative` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `stag-left idx-cycling` |
| `<nav>` | `dock-sheet` | `dock-sheet` |
| `<nav>` | `-` | `dock dock-in` |
| `<header>` | `-` | `site nav-on-dark` |
| `<main>` | `-` | `idx-main` |
| `<footer>` | `-` | `sf sf--fixed sf--dark` |
