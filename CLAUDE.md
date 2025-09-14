# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a collection of educational games and interactive applications demonstrating various programming languages and frameworks. Each project is self-contained within its own directory.

## Project Structure

```
vibe-coded/
├── games/
│   ├── flappybird/     # Cross-platform Flappy Bird clone (Python/pygame and HTML5/JS)
│   ├── tictactoe/      # Tic Tac Toe implementations (Python/pygame and C#)
│   └── piano-kids/     # Educational piano game (HTML5 standalone)
└── music/
    └── win32_happy_birthday/  # Windows MIDI player (C with WinMM)
```

## Common Development Commands

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

### Piano Kids
```bash
cd games/piano-kids
# Open piano-kids.html directly in browser
# Or serve with: python -m http.server
```

### Win32 Happy Birthday (Windows only)
```bash
cd music/win32_happy_birthday/build
cmake ..
cmake --build .
./wi32_midi_happy_birthday.exe
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
- Multiple implementations demonstrating different languages
- Mouse-based input with visual feedback
- Restart functionality

### Piano Kids
- Web Audio API for sound generation
- Educational focus with numbered keys (1-6)
- Song library with playback at variable speeds
- Print mode for song sheets

### Win32 Happy Birthday
- Windows-specific MIDI implementation
- Demonstrates low-level audio programming
- CMake build configuration for cross-compiler support

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