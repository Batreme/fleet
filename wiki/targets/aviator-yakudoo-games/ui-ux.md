---
title: "UI & Design System: aviator-yakudoo-games"
date: 2026-11-14
target: "[[overview|aviator-yakudoo-games]]"
---

# UI Architecture & Design Tokens: aviator-yakudoo-games

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--start-top` | `59.5%` |
| `--hud-icon` | `42}@media (pointer:coarse){.hud{--hud-icon:calc(42 * var(--h` |
| `--t` | `1.5` |
| `--d` | `1` |
| `--t` | `3` |
| `--d` | `1.25` |
| `--t` | `1` |
| `--d` | `.8` |
| `--t` | `2` |
| `--d` | `1.4` |
| `--t` | `4` |
| `--d` | `.9` |
| `--t` | `1.5` |
| `--d` | `1.1` |
| `--t` | `2.5` |
| `--d` | `.75` |
| `--t` | `1` |
| `--d` | `1.3` |
| `--t` | `3` |
| `--d` | `1` |
| `--lu` | `clamp(.6px, calc(var(--app-w,100vw) / 2000), 1px)` |
| `--start` | `before,.screen--menu .screen__button--start:after{width:calc` |
| `--menu-gap-scale` | `.7}}.app--menu-open .links{opacity:1` |
| `--links-in` | `not(.is-board) .menu-toggle{opacity:1` |
| `--board-delay` | `0s}.board__list{width:min(100%, calc(600 * var(--u)), 34em)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `links` |
