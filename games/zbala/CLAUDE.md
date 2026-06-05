# CLAUDE.md - Zbala (زبالة السرايا)

## Overview

Single-file HTML5 canvas game — a satirical trash-tossing arcade game from 2018 about the Lebanese garbage crisis. Toss trash bags into the windows of the Grand Serail (government palace) before time runs out. Modernized from [ZbalaJS](https://github.com/lallousx86/ZbalaJS).

## Development

Requires a local server (assets are external PNGs/WAV):
```bash
cd games/zbala
python -m http.server
```

## Architecture

- **Single HTML file** with inline JS, references external assets in `res/`
- **Original code structure preserved**: `BasketZbala` (controller), `Ball` (physics), `Hoop` (target), `PopText` (floating score)
- **Assets**: `res/background*.png` (start/play/over screens), `res/ball.png` (trash bag), `res/hoop.png` (window/bin), `res/bounce_1.wav`

## Key Implementation Details

- **Hybrid aiming**: Bag oscillates left-right at bottom (timing skill). Click/tap position offsets launch angle ±30° from vertical (aiming skill). Sensitivity: `dx * 0.12`.
- **Physics**: Gravity 1500 px/s², launch speed ~1480, max 3 bounces per bag. Rim collision uses angle-based deflection with ±5° randomness.
- **One bag at a time**: New bag cannot launch until current one falls off screen.
- **Game loop**: `requestAnimationFrame` with delta time capped at 50ms.
- **Sound**: Enabled by default, uses `res/bounce_1.wav` for rim hits.
- **High score**: localStorage key `'zbala-best'`, displayed on game-over screen.
- **Bag oscillation speed**: 650 px/s (slowed from original 1200).
- **State machine**: `'menu'` → `'play'` → `'over'` → `'menu'`
- **Hoop positions**: Three fixed positions — two at y=520 (lower windows), one at y=290 (upper window).
