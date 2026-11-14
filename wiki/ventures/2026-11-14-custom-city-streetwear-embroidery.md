---
title: "Venture: Custom-City Streetwear Embroidery Platform"
date: 2026-11-14
status: completed
tags:
  - venture
  - ecommerce
  - streetwear
  - nextjs
  - canvas
  - embroidery
outcome_summary: "Designed and built custom-city: a dark heavyweight industrial streetwear e-commerce platform featuring an interactive 2D live embroidery simulator, 3D puff relief preview, Tech Pack production sheet generator, city drops, BLIK checkout, and B2B volume pricing calculator."
---

# Venture: Custom-City Streetwear Embroidery Platform

## Context & Desired Outcome
- **Problem / Goal**: Build an authentic, dark industrial streetwear brand & shop ("custom-city") specialized in computer machine embroidery (logos, custom graphics, typography, 3D puff relief) on heavyweight garments (up to 480 GSM).
- **Target Outcome**: A production-ready Next.js application built strictly outside `/fleet` in `/root/projects/custom-city` with:
  1. Interactive 2D live embroidery customizer (garment selector, front/back perspectives, zone bounds, satin stitch texture pattern, 16 Madeira thread colors, 3D puff simulation).
  2. Tech Pack generator (exportable machine specification with dimensions in mm, needle types, stabilizer backing, and stitch counts).
  3. City Drops storefront showcasing 4 limited edition heavy pieces.
  4. Full checkout simulation featuring Polish BLIK 6-digit code validation, timer, and confetti celebration.
  5. Interactive B2B bulk tier calculator for clothing brands and crews.

## Approach Taken
- **Architecture & Isolation**: Created a standalone repository at `/root/projects/custom-city` adhering strictly to workspace boundaries.
- **Tech Stack**: Next.js 15 (App Router, TypeScript), Tailwind CSS, Framer Motion, HTML5 Canvas / SVG hybrid rendering for stitch texture simulation, Web Audio API synthesizer for tactile mechanical UI haptics.
- **Visual Design DNA**: Dark Heavyweight Industrial aesthetic (`#060608` to `#16161c`, raw concrete grey `#6e7075`, acid volt `#ccff00`, safety orange `#ff5500`), heavy grotesk typography, and modular industrial grids.

## Challenges & Obstacles
- **ESLint no-unused-vars during Next.js production build**: Catch clauses and unused variables flagged by Next.js 15 strict linting were resolved by cleaning unused parameters and integrating state variables directly into interactive controls.
- **Realistic Embroidery Simulation**: Rendering thread sheen without heavy external 3D WebGL assets was solved using an SVG filter + patterned diagonal satin stitch lines with anisotropic lighting and ambient occlusion shadows for 3D Puff relief.

## Final Outcome & Artifacts
- **Repository**: Located at `/root/projects/custom-city` with clean git history (`feat: initial release of custom-city streetwear embroidery platform`).
- **Production Server**: Deployed and serving at `http://localhost:3000` with 0 compile errors.
- **Deliverables**:
  - Live Customizer with Realtime Pricing & Canvas Embroidery Simulation.
  - Printable / Downloadable Production Tech Pack Spec Sheet.
  - City Drops #01-#04 limited catalogue.
  - Cart Slide-over & BLIK 6-digit Checkout flow.
  - Interactive B2B Volume Pricing Calculator.

## Reusable Lessons
- **Stitch Texture Simulation**: Combining SVG angled satin lines (`patternTransform="rotate(45)"`) with dual `feDropShadow` filters creates a remarkably convincing thread and 3D puff embroidery effect in pure CSS/SVG without WebGL overhead.
- **Web Audio Haptics**: Generating synthetic oscillator clicks and chimes eliminates the need for external MP3 audio asset dependencies.
- **Links to relevant playbooks**: [[agency-and-ecommerce-patterns]], [[tech-and-experimental-patterns]]
