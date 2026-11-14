---
title: "UI & Design System: clipdance-ai"
date: 2026-11-14
target: "[[overview|clipdance-ai]]"
---

# UI Architecture & Design Tokens: clipdance-ai

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
*No CSS custom property tokens extracted.*

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `group/navigation-menu flex max-w-max flex-1 items-center justify-center relative` |
| `<nav>` | `-` | `scrollbar-none flex flex-1 flex-col gap-[3px] overflow-y-auto px-2.5 pt-1 pb-2` |
| `<header>` | `-` | `sticky inset-x-0 top-0 z-40 h-14 border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:` |
| `<aside>` | `-` | `group/rail relative z-10 my-3 ml-3 shrink-0 rounded-2xl border border-border/60 bg-card dark:border-` |
| `<main>` | `main-content` | `home-shell-scroller relative z-10 flex-1 overflow-y-auto [&::-webkit-scrollbar]:hidden` |
| `<footer>` | `-` | `border-t` |
