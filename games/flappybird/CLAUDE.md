# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flappy Bird clone implementation with both Python (pygame) and HTML5/JavaScript versions. The project was created using AI-assisted development with prompts stored in the PROMPTS folder.

## Repository Structure

```
vibe-coded/games/flappybird/
├── python/               # Python/pygame version
│   ├── myflappy/        # Main game package
│   │   ├── __init__.py
│   │   ├── __main__.py  # Entry point for `python -m myflappy`
│   │   ├── main.py      # Game loop and state management
│   │   ├── bird.py      # Bird physics and rendering
│   │   ├── pipes.py     # Pipe obstacles
│   │   ├── cloud.py     # Background clouds
│   │   ├── ground.py    # Ground collision
│   │   └── constants.py # Game configuration
│   └── pyproject.toml   # Package configuration
├── html/                 # Web version
│   ├── index.html       # Game UI
│   ├── game.js          # Game logic
│   ├── server.js        # Express server
│   ├── package.json     # Node dependencies
│   └── README_WEB.md    # Web version documentation
├── PROMPTS/             # AI prompts used to create the game
│   ├── vscode-prompts.md # Python development prompts
│   ├── claude-code-prompt.md # Web conversion prompts
│   ├── prompt-codex-make-tut.md # Tutorial generation prompt
│   └── tuts.md          # Generated tutorial documentation
└── CLAUDE.md            # This file

```

## Python Version

### Commands

#### Run the game
```bash
cd python
python -m myflappy
```

#### Install as package
```bash
cd python
pip install -e .
```

#### Install dependencies only
```bash
pip install pygame>=2.0
```

### Architecture

The game follows a modular architecture with separate classes for each game entity:

- **main.py**: Game loop and state management (START, PLAYING, PAUSED, GAMEOVER)
- **bird.py**: Bird physics, jumping mechanics, and rendering
- **pipes.py**: Pipe obstacle generation and collision detection
- **cloud.py**: Background cloud animation with parallax effect
- **ground.py**: Ground collision boundary
- **constants.py**: Game configuration (dimensions, speeds, colors, physics parameters)
- **myflappy.py**: Convenience wrapper for running main()
- **__main__.py**: Module entry point for `python -m myflappy`

### Key Game Mechanics

- **Lives System**: Player starts with 3 lives, loses one per collision with 1-second invulnerability
- **Physics**: Gravity-based bird movement with jump and hold mechanics
- **Scoring**: Points awarded for passing pipes
- **Parallax**: Clouds move at different speeds for depth perception
- **Debug Features**: 
  - Press 'I' to add 5 lives
  - Press 'G' to toggle god mode (invincibility)
  - Press 'P' to pause/unpause

### State Management

The game uses a state machine with four states controlled in the main game loop:
- STATE_START: Title screen with instructions
- STATE_PLAYING: Active gameplay
- STATE_PAUSED: Game paused (preserves all positions and timing)
- STATE_GAMEOVER: Final score display

All drawing operations happen every frame regardless of state, with updates only occurring during STATE_PLAYING.

## HTML5/JavaScript Version

### Quick Start

#### Using Node.js (Recommended)
```bash
cd html
npm install
npm start
# Opens at http://localhost:3000
```

#### Using Python's HTTP server
```bash
cd html
python -m http.server 3000
# Opens at http://localhost:3000
```

#### Direct file access
Open `html/index.html` directly in a web browser

### Features

The web version maintains feature parity with the Python version:
- Same control scheme (SPACE/Click to jump, P to pause, etc.)
- Identical physics and game mechanics
- Canvas-based rendering with requestAnimationFrame
- Responsive design that works on desktop and mobile

## Controls (Both Versions)

- **SPACE** or **Mouse Click**: Jump (hold for stronger jump)
- **P**: Pause/Resume game
- **G**: Toggle God Mode (no life loss)
- **I**: Add 5 extra lives (debug)
- **ESC**: Quit (Python) / Return to menu (Web)

## Development Notes

### Testing
When testing changes:
1. For Python: Run directly with `python -m myflappy` from the python directory
2. For Web: Use the Node.js server for best compatibility

### Configuration
Game constants can be tuned in:
- Python: `python/myflappy/constants.py` and `python/myflappy/bird.py`
- Web: Top of `html/game.js`

Key tuning parameters:
- `PIPE_SPEED`: Horizontal pipe movement speed
- `PIPE_GAP`: Vertical gap between pipe pairs
- `GRAVITY`: Downward acceleration
- `JUMP_STRENGTH`: Initial upward velocity on jump
- `JUMP_HOLD_BOOST`: Additional boost when holding jump

## AI-Assisted Development

This project was created through iterative development using AI assistance. The prompts used are documented in:
- `PROMPTS/vscode-prompts.md`: Step-by-step Python game development prompts
- `PROMPTS/claude-code-prompt.md`: Prompts for converting to JavaScript and adding server
- `PROMPTS/prompt-codex-make-tut.md`: Prompt for generating the comprehensive tutorial
- `PROMPTS/tuts.md`: Generated tutorial explaining the pygame implementation

The development process showcased:
1. Initial specification and single-file prototype (Python)
2. Modularization into separate components
3. Feature additions (lives, pause, debug modes)
4. Package structure and distribution setup
5. Cross-platform port to web technologies (JavaScript/HTML5)
6. Server implementation with Express.js
7. Documentation generation through AI