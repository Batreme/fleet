---
title: "UI & Design System: crun-ai"
date: 2026-11-14
target: "[[overview|crun-ai]]"
---

# UI Architecture & Design Tokens: crun-ai

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--crisp-color-base-white-normal` | `255, 255, 255` |
| `--crisp-color-base-white-dark` | `255, 255, 255` |
| `--crisp-color-base-black-light` | `28, 41, 59` |
| `--crisp-color-base-black-normal` | `0, 0, 0` |
| `--crisp-color-base-blue-ultra-light` | `224, 237, 255` |
| `--crisp-color-base-blue-light` | `89, 144, 226` |
| `--crisp-color-base-grey-ultra-light` | `240, 242, 245` |
| `--crisp-color-base-grey-light` | `211, 221, 230` |
| `--crisp-color-base-grey-normal` | `102, 120, 138` |
| `--crisp-color-base-grey-dark` | `55, 81, 108` |
| `--crisp-color-base-grey-ultra-dark` | `40, 64, 89` |
| `--crisp-color-base-red-ultra-light` | `255, 242, 243` |
| `--crisp-color-base-red-light` | `255, 220, 224` |
| `--crisp-color-base-red-normal` | `238, 51, 75` |
| `--crisp-color-base-red-dark` | `199, 10, 34` |
| `--crisp-color-base-red-ultra-dark` | `107, 12, 0` |
| `--crisp-color-base-green-light` | `78, 206, 61` |
| `--crisp-color-base-green-normal` | `34, 178, 15` |
| `--crisp-color-base-green-dark` | `15, 128, 4` |
| `--crisp-color-base-green-ultra-dark` | `7, 58, 0` |
| `--crisp-color-base-orange-dark` | `225, 105, 0` |
| `--crisp-color-base-yellow-ultra-light` | `255, 246, 208` |
| `--crisp-color-base-yellow-light` | `255, 244, 127` |
| `--crisp-color-base-yellow-normal` | `245, 201, 12` |
| `--crisp-color-base-white-normal-fixed` | `255, 255, 255` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `h-full ml-16px color-zinc-800 dark:color-zinc-100 custom_nav` |
| `<nav>` | `-` | `custom_nav dark:bg-[#050B14] dark:text-slate-200` |
| `<header>` | `-` | `fixed left-0 right-0 top-0 z-999 transition-all duration-300 backdrop-blur-2xl border-b border-slate` |
