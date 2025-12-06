# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Tic Tac Toe implemented in multiple languages: HTML5/JavaScript, Python/Pygame, and C#. Each version features a 3x3 grid where two players take turns marking X's and O's.

## Development Commands

### HTML5 Version (Browser)
```bash
cd html
# Open tic-tac-toe.html directly in browser
# Or serve with: python -m http.server
```

### Python Version
```bash
python tictactoe.py
# or
python3 tictactoe.py
```

### C# Version
```bash
dotnet run
```

### Dependencies
- **HTML5**: No dependencies (runs in browser)
- **Python**: pygame library (`pip install pygame`)
- **C#**: .NET SDK

## Architecture

The codebase follows a simple object-oriented design with two main components:

1. **Board Class** (`tictactoe.py:23-73`)
   - Manages game state (3x3 grid)
   - Handles move validation
   - Checks for win conditions and draws
   - Tracks current player and game status

2. **Main Game Loop** (`tictactoe.py:119-158`)
   - Handles Pygame event processing
   - Manages drawing functions (grid, symbols, status)
   - Coordinates game flow

## Key Implementation Details

- **Screen**: 600x600 pixels, divided into 3x3 cells
- **Players**: X (blue) and O (red)
- **Controls**: Mouse click to place moves, 'R' key to restart
- **Win Detection**: Checks rows, columns, and diagonals after each move

## Development Phases

The project was developed following the phases outlined in `phases.md`, with each phase building on the previous:
1. Basic setup and window creation
2. Game board implementation
3. Game logic (validation, win checking)
4. UI polish (turn indicators, messages, reset)