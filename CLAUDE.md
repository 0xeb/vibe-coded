# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

A collection of educational games and interactive applications across multiple languages (Python, JavaScript, C#, C). Each project is self-contained with its own `CLAUDE.md` containing implementation-specific details — consult those for per-project architecture, algorithms, and state management.

## Project Structure

```
vibe-coded/
├── games/
│   ├── index.html          # Launcher page for all HTML games (MUST update when adding games)
│   ├── flappybird/         # Python/pygame + HTML5/JS (dual implementation)
│   ├── tictactoe/          # HTML5/JS + Python/pygame + C# (triple implementation)
│   ├── piano-kids/         # HTML5 standalone
│   ├── sliding-puzzle/     # HTML5 standalone
│   ├── click-trainer/      # HTML5 standalone
│   └── 21cards-trick/      # HTML5 standalone
├── music/
│   └── win32_happy_birthday/  # C with WinMM (Windows only)
└── productivity/
    └── powerpoint-agent/      # Marp + LLM agent workflow
```

## Common Development Commands

### HTML Games Launcher
```bash
cd games && python -m http.server 8000
# Open http://localhost:8000
```

### Standalone HTML Games (piano-kids, sliding-puzzle, click-trainer, 21cards-trick)
Open the HTML file directly in a browser, or serve via `python -m http.server` from the game directory.

### Flappy Bird
```bash
# Python
cd games/flappybird/python && pip install pygame>=2.0 && python -m myflappy

# Web
cd games/flappybird/html && npm install && npm start  # http://localhost:3000
```

### Tic Tac Toe
```bash
# Python
cd games/tictactoe && pip install pygame && python tictactoe.py

# C#
cd games/tictactoe && dotnet build && dotnet run

# Web: open games/tictactoe/html/tic-tac-toe.html in browser
```

### Win32 Happy Birthday (Windows only)
```bash
cd music/win32_happy_birthday/build && cmake .. && cmake --build .
./wi32_midi_happy_birthday.exe
```

### PowerPoint Agent
```bash
cd productivity/powerpoint-agent
install-step1.bat   # Node.js, LibreOffice, Python, etc.
install-step2.bat   # npm packages (Marp CLI)
marp-pptx.bat hello.md  # or: .\marp-pptx.ps1 hello.md
```

## Architecture Patterns

### Cross-Cutting Patterns
- **State machines**: Games use states (START, PLAYING, PAUSED, GAMEOVER) with a main update-render loop
- **Entity separation**: Game objects (player, obstacles, UI) in separate modules/classes
- **Centralized config**: Tunable constants in dedicated locations (e.g., `constants.py`, top of `game.js`)
- **PROMPTS/ directories**: Most projects include a `PROMPTS/` folder documenting the AI prompts used during development

### Technology Stack Details
- **Python/Pygame**: Package structure with `__main__.py` entry points, modular classes
- **Web games**: Vanilla JS (no frameworks), Canvas + `requestAnimationFrame`, mobile-responsive
- **C/C++**: CMake build system, platform-specific APIs
- **PowerPoint Agent**: Marp (Markdown → PPTX), requires LibreOffice for `--pptx-editable` flag; use helper scripts (`marp-pptx.bat`/`.ps1`) instead of calling `marp` directly

## Testing

- No automated test framework across the repo; `games/tictactoe/test.cs` is the only unit test file
- **Manual testing**: Run games directly and exercise features
- **Debug shortcuts**: Most games have debug modes (e.g., Flappy Bird: I for +5 lives, G for god mode, P to pause)
- **Web games**: Use a local HTTP server to avoid CORS issues

## Development Guidelines

When adding a new HTML game:
1. Create a self-contained directory under `games/` with the game HTML file
2. **Add a card to `games/index.html`** — this is the launcher and must list all games
3. Add a `CLAUDE.md` in the game directory with implementation details
4. Add a `README.md` with usage instructions

When modifying existing projects:
1. Read the project's own `CLAUDE.md` first for architecture and implementation details
2. Keep configuration values in their designated locations
3. Preserve debug features and keyboard shortcuts

When creating presentations with powerpoint-agent:
1. Use helper scripts (`marp-pptx.bat`/`.ps1`), not `marp` directly
2. Each presentation in its own subfolder with `images/` and `plan.md`
3. Use Marp front matter: `marp: true`, `theme: default`, `paginate: true`