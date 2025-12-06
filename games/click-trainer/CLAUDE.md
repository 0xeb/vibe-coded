# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Click Trainer is a standalone HTML5 reaction time training game that runs entirely in the browser. Click randomly spawning targets as fast as possible to improve your aim and reaction speed.

## Architecture

The application is a single-page web app with:
- **Canvas Rendering**: Full-screen canvas for ball drawing with glow effects
- **Timing System**: High-precision timing using `performance.now()`
- **Statistics Tracking**: Average time, best time, and click count

## Key Components

### Game State
- `currentBall`: Current target to click (position, radius, color)
- `times[]`: Array of reaction times for averaging
- `bestTime`: Fastest reaction time in session
- `gameActive`: Whether game is currently running

### Configurable Options
- Ball count (1-100): Number of targets per round
- Ball size (10-100px): Target diameter

### Statistics
- Clicked count / Total
- Average reaction time (ms)
- Best reaction time (ms)

## Development Commands

This is a standalone HTML file with no build process required. To run:
- Open `click-trainer.html` directly in a web browser
- Or serve via any HTTP server (e.g., `python -m http.server`)

## Testing

No automated tests are configured. Manual testing involves:
- Verifying ball spawns within visible area
- Testing various ball counts and sizes
- Checking statistics accuracy
- Testing window resize behavior
