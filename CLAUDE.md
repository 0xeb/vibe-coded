# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a collection of educational games and interactive applications demonstrating various programming languages and frameworks. Each project is self-contained within its own directory.

## Project Structure

```
vibe-coded/
├── games/
│   ├── index.html      # Launcher page for all HTML games
│   ├── flappybird/     # Cross-platform Flappy Bird clone (Python/pygame and HTML5/JS)
│   ├── tictactoe/      # Tic Tac Toe implementations (HTML5/JS, Python/pygame, and C#)
│   ├── piano-kids/     # Educational piano game (HTML5 standalone)
│   ├── sliding-puzzle/ # Number sliding puzzle with auto-solver (HTML5 standalone)
│   └── click-trainer/  # Reaction time trainer (HTML5 standalone)
├── music/
│   └── win32_happy_birthday/  # Windows MIDI player (C with WinMM)
└── productivity/
    └── powerpoint-agent/  # Marp-based presentation creator with LLM agent support
```

## Common Development Commands

### All HTML Games (Launcher)
```bash
cd games
python -m http.server 8000
# Open http://localhost:8000 for the games launcher
```

### Flappy Bird (Python)
```bash
cd games/flappybird/python
pip install pygame>=2.0
python -m myflappy
```

### Flappy Bird (Web)
```bash
cd games/flappybird/html
npm install
npm start  # Opens at http://localhost:3000
```

### Tic Tac Toe (Python)
```bash
cd games/tictactoe
pip install pygame
python tictactoe.py
```

### Tic Tac Toe (C#)
```bash
cd games/tictactoe
dotnet build
dotnet run
```

### Tic Tac Toe (Web)
```bash
cd games/tictactoe/html
# Open tic-tac-toe.html directly in browser
# Or serve with: python -m http.server
```

### Piano Kids
```bash
cd games/piano-kids
# Open piano-kids.html directly in browser
# Or serve with: python -m http.server
```

### Sliding Puzzle
```bash
cd games/sliding-puzzle
# Open sliding-puzzle.html directly in browser
# Or serve with: python -m http.server
```

### Click Trainer
```bash
cd games/click-trainer
# Open click-trainer.html directly in browser
# Or serve with: python -m http.server
```

### Win32 Happy Birthday (Windows only)
```bash
cd music/win32_happy_birthday/build
cmake ..
cmake --build .
./wi32_midi_happy_birthday.exe
```

### PowerPoint Agent (Windows recommended)
```bash
cd productivity/powerpoint-agent

# Install prerequisites (run in order, wait for Step 1 to complete)
install-step1.bat  # Installs Node.js, LibreOffice, Python, etc.
install-step2.bat  # Installs npm packages (Marp CLI, etc.)

# Verify installation
node --version
marp --version
where soffice  # LibreOffice (required for editable PPTX)

# Generate a test presentation
marp-pptx.bat hello.md
# or PowerShell: .\marp-pptx.ps1 hello.md

# Use with LLM agents (e.g., GitHub Copilot CLI)
copilot --allow-all-tools
# Then prompt: "Please load the agent-pptx.md file"
```

## Architecture Patterns

### Game Development Patterns

All game projects follow similar architectural principles:

1. **State Management**: Games use state machines (START, PLAYING, PAUSED, GAMEOVER)
2. **Entity Separation**: Game entities (player, obstacles, UI) are typically in separate modules
3. **Configuration**: Constants and tunable parameters are centralized
4. **Game Loop**: Standard update-render loop pattern with fixed timestep where applicable

### Python/Pygame Projects

- Use modular class-based architecture
- Package structure with `__main__.py` for module execution
- Constants separated in dedicated configuration files
- Standard pygame event loop with state management

### Web Projects

- Standalone HTML files or minimal server setup with Express.js
- Canvas-based rendering with requestAnimationFrame
- Vanilla JavaScript (no frameworks) for simplicity
- Mobile-responsive design considerations

### C/C++ Projects

- CMake-based build system
- Platform-specific APIs (WinMM for Windows MIDI)
- Minimal external dependencies

### Productivity Tools

- **Marp-based workflow**: Markdown → HTML/PDF/PPTX conversion
- **LLM agent integration**: agent-pptx.md provides structured prompts for AI assistants
- **Helper scripts**: Batch (.bat) and PowerShell (.ps1) wrappers for cross-shell compatibility
- **Editable output**: LibreOffice enables `--pptx-editable` flag for fully editable PowerPoint files
- **Folder structure**: Each presentation in its own subfolder with `images/`, `plan.md`, and source `.md` files

## Testing Approach

- **Python Games**: Run directly with `python -m <module>` or `python <file>.py`
- **Web Games**: Test in browser with local server to avoid CORS issues
- **Debug Features**: Most games include debug modes (god mode, extra lives) accessible via keyboard shortcuts

## Key Implementation Details

### Flappy Bird
- Modular architecture with separate physics, rendering, and game state
- Configurable difficulty through constants (pipe gap, speed, gravity)
- Lives system with invulnerability frames
- Both Python and JavaScript versions maintain feature parity

### Tic Tac Toe
- Simple 3x3 grid with win detection
- Multiple implementations (HTML5/JS, Python/pygame, C#)
- HTML5 version includes AI opponents (easy/hard with minimax)
- Score tracking and animated win highlighting
- Mouse-based input with visual feedback

### Piano Kids
- Web Audio API for sound generation
- Educational focus with numbered keys (1-6)
- Song library with playback at variable speeds
- Print mode for song sheets

### Sliding Puzzle
- Configurable grid sizes (3×3, 4×4, 5×5)
- Shuffle history recording for instant reverse-solve
- IDA* algorithm with Manhattan distance heuristic for user-modified puzzles
- Speed-adjustable solve animation
- Win detection with celebration modal

### Click Trainer
- Full-screen canvas with crosshair cursor
- Configurable target count and size
- High-precision timing with `performance.now()`
- Statistics tracking (average time, best time)
- Colorful targets with glow effects

### Win32 Happy Birthday
- Windows-specific MIDI implementation
- Demonstrates low-level audio programming
- CMake build configuration for cross-compiler support

### PowerPoint Agent
- Automates presentation creation using Marp (Markdown Presentation Ecosystem)
- `agent-pptx.md` defines a 4-step workflow: Define → Research & Plan → Create → Generate PPTX
- Helper scripts (`marp-pptx.bat`/`.ps1`) wrap Marp CLI with proper flags and LibreOffice PATH setup
- Requires LibreOffice for `--pptx-editable` flag (creates fully editable PowerPoint files vs. image-only slides)
- Critical flags: `--allow-local-files` (for images), `--pptx-editable` (for text editing in PowerPoint)
- Designed for LLM agent automation (GitHub Copilot CLI, Claude Code, etc.)

## Development Guidelines

When modifying existing games:
1. Maintain the existing code style and patterns
2. Keep configuration values in their designated locations
3. Preserve debug features for testing
4. Update relevant CLAUDE.md files in subdirectories

When adding new features:
1. Follow the established state management patterns
2. Keep entity logic separated
3. Add keyboard shortcuts for debug features
4. Document any new dependencies or build steps

When creating presentations with powerpoint-agent:
1. Always use the helper scripts (`marp-pptx.bat` or `.ps1`) instead of calling `marp` directly
2. Organize each presentation in its own subfolder under `example/` or custom location
3. Create a `plan.md` before writing the presentation markdown
4. Store images in logical subfolders (e.g., `images/logos/`, `images/screenshots/`)
5. Verify LibreOffice is installed and accessible via `soffice` command before generating PPTX
6. Use Marp front matter: `marp: true`, `theme: default`, `paginate: true`, `header: ''`, `footer: ''`