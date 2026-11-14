---
title: "UI & Design System: manifesto-blandina-org"
date: 2026-11-14
target: "[[overview|manifesto-blandina-org]]"
---

# UI Architecture & Design Tokens: manifesto-blandina-org

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--btn-color` | `var(--color-white)` |
| `--btn-fill` | `var(--color-white-10)` |
| `--btn-color` | `var(--color-sand)` |
| `--font-serif` | `"Libertinus Sans", "Libertinus Sans Fallback: BlinkMacSystem` |
| `--font-sans` | `"Host Grotesk", "Host Grotesk Fallback: BlinkMacSystemFont",` |
| `--font-base` | `var(--font-sans)` |
| `--color-white` | `#fff` |
| `--color-white-10` | `#ffffff1a` |
| `--color-bark-green` | `#4a4f32` |
| `--color-field-green` | `#9c9873` |
| `--color-ivory` | `#edece8` |
| `--color-sand` | `#b59972` |
| `--color-terracotta` | `#a54d25` |
| `--color-black` | `#0f0f0f` |
| `--color-soft-black` | `#1d150c` |
| `--color-orange` | `#fa712a` |
| `--color-orange-30` | `#fa712a4d` |
| `--color-ivory-10` | `#edece81a` |
| `--color-ivory-30` | `#edece84d` |
| `--color-soft-black-10` | `#1d150c1a` |
| `--color-soft-black-70` | `#1d150cb3` |
| `--color-soft-black-50` | `#1d150c80` |
| `--color-soft-black-30` | `#1d150c4d` |
| `--color-primary` | `var(--color-soft-black)` |
| `--color-bg` | `var(--color-ivory)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<header>` | `-` | `inspirational-gallery__head` |
| `<main>` | `main-content` | `main-content` |
| `<footer>` | `-` | `the-footer -is-away` |
