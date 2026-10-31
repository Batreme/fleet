---
title: "Venture: Cinematic 35mm Photography Portfolio & Interactive Viewfinder"
date: 2026-10-31
status: completed
tags:
  - venture
  - photography
  - nextjs15
  - framer-motion
  - reverse-engineered
outcome_summary: "Scaffolded and built a bespoke cinematic-studio photography portfolio application outside /fleet with an interactive 24mm-85mm optical scroll-scrub lens hero, Web Audio shutter synthesis, and an EXIF inspector."
---

# Venture: Cinematic 35mm Photography Portfolio & Interactive Viewfinder

## Context & Desired Outcome
- **Problem / Goal**: The user requested a cinematic-studio photography portfolio application based on Fleet's reverse-engineering knowledge base and setup. The hero section required framing a user-uploaded 35mm monochrome photograph inside a camera lens that dynamically zooms in and out driven by mouse scroll.
- **Target Outcome**: An isolated, production-grade Next.js 15 application adhering strictly to `AGENTS.md` (no application code in `/fleet`), incorporating reverse-engineered design DNA from `velourproductions-com` and `untitledfilm-framer-website`, tactile audio feedback, and technical EXIF metadata inspection.

## Approach Taken
- **Boundary Compliance**: Initialized the project at `../cinematic-studio-portfolio` as a dedicated standalone Git repository using `reverse-harness scaffold --style cinematic-studio`.
- **Interactive Optical Viewfinder**: Built `HeroViewfinder` utilizing Framer Motion's `useScroll` and `useSpring` across a pinned ~250vh track. The lens smoothly scrubs focal length from 24mm (`f/2.8`) to 85mm (`f/1.4`), anchored directly on the subject (`50% X, 72% Y`) with subtle 3D cursor-tracking parallax.
- **Web Audio API Mechanical Synthesizer**: Implemented zero-dependency procedural audio in `lib/sound.ts` to synthesize realistic focal plane shutter clicks (mirror slap, curtain transit, latch detent) and aperture dial notches without external audio files.
- **Technical EXIF Inspector**: Created an interactive camera telemetry modal (`ExifInspectorModal`) with full camera specifications (Leica M6, Hasselblad 500 C/M, Linhof 4x5), film emulsions (Ilford HP5+, Kodak Tri-X, T-Max), and GPS coordinates.
- **Print Acquisition Drawer**: Engineered a slide-over inquiry drawer with live studio availability badges and archival baryta paper specifications.

## Challenges & Obstacles
- **Scroll Hijacking vs Pinned Scrubbing**: Traditional wheel event interceptors can feel jittery or break standard browser navigation. By using a standard pinned sticky container with `useScroll({ offset: ["start start", "end end"] })`, native smooth scrolling works bidirectionally without trapping or breaking user scroll expectations.
- **Subject Anchor Offset**: Centered zoom scales from the dead center of the photo (`50% 50%`), which would crop out the reposing human subject located in the lower-center lawn. Anchoring `transformOrigin` to `50% 72%` ensures the 85mm telephoto crop focuses with razor precision on the subject.

## Final Outcome & Artifacts
- **Repository Location**: `/Users/jakubszkop/Desktop/Projects/Github/cinematic-studio-portfolio`
- **Initial Commit**: `406a5b3` (`main`)
- **Key Deliverables**:
  - `HeroViewfinder.tsx`: Pinned 24mm-85mm zoom viewfinder with dynamic HUD telemetry, corner anamorphic framelines, rule-of-thirds grid, and flash burst.
  - `lib/sound.ts`: Procedural Web Audio API mechanical shutter and aperture sound engine.
  - `data/photography.ts`: Flagship Study No. 01 featuring the uploaded photo + 7 curated monochrome studies.
  - `ExifInspectorModal.tsx`: Keyboard-navigable camera telemetry inspector.
  - `InquiryDrawer.tsx`: Commission and archival print booking interface.

## Reusable Lessons
- When implementing scroll-driven zoom in Next.js/React, stick to sticky container tracks (`h-[200vh-300vh]`) with `useScroll` rather than intercepting raw wheel events.
- Synthesizing tactile camera mechanics via Web Audio API oscillators and noise buffers avoids CORS, asset 404s, and autoplay policy blockers.
