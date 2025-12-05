# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Sliding Puzzle is a standalone HTML5 number sliding puzzle game that runs entirely in the browser. The entire application is contained in a single HTML file (`sliding-puzzle.html`) with embedded CSS and JavaScript.

## Architecture

The application is a single-page web app with:
- **Grid System**: Configurable 3×3, 4×4, or 5×5 tile grids
- **Game State**: Tracks tile positions, move count, and solve state
- **Solver**: IDA* algorithm with Manhattan distance heuristic for automated solving
- **Shuffle History**: Records moves during shuffle for instant reverse-solve

## Key Components

### State Management
- `tiles[]`: Array representing current tile positions (0 = empty)
- `emptyIndex`: Position of the empty space
- `shuffleHistory[]`: Recorded moves during shuffle for replay
- `hasUserMoved`: Tracks if user invalidated the shuffle history

### Solver System
- **Fast path**: Reverses shuffle history if user hasn't moved
- **IDA* algorithm**: Iterative deepening A* for user-modified puzzles
- **Manhattan distance**: Heuristic for estimating moves to solution
- Max iterations capped at 1,000,000 to prevent browser hang

### UI Components
- Size selector buttons (3×3, 4×4, 5×5)
- Move counter
- Control buttons (Shuffle, Solve, Stop, Reset)
- Speed slider for solve animation (50ms–500ms)
- Win celebration modal

## Development Commands

This is a standalone HTML file with no build process required. To run:
- Open `sliding-puzzle.html` directly in a web browser
- Or serve via any HTTP server (e.g., `python -m http.server`)

## Testing

No automated tests are configured. Manual testing involves:
- Verifying all grid sizes work correctly
- Testing shuffle ensures solvability
- Checking solve animation at various speeds
- Testing win detection
- Verifying controls disable during solve
