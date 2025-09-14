# Flappy Bird Clone

A feature-complete Flappy Bird clone implemented in both Python (using pygame) and HTML5/JavaScript. This project demonstrates cross-platform game development with identical gameplay mechanics across different technologies.

## 📚 Development Prompts

**[View the progressive prompts used to build this game →](PROMPTS/)**

## Features

- **Classic Flappy Bird gameplay** with smooth physics
- **Lives system** - Start with 3 lives and invulnerability frames
- **Score tracking** - Points for successfully passing pipes
- **Parallax backgrounds** - Moving clouds for depth perception
- **Debug modes** - God mode and extra lives for testing
- **Pause functionality** - Freeze game state anytime
- **Cross-platform** - Play on desktop (Python) or in browser (Web)

## Quick Start

### Python Version

```bash
cd python
pip install pygame>=2.0
python -m myflappy
```

### Web Version

```bash
cd html
npm install
npm start
# Open http://localhost:3000
```

Or use Python's HTTP server:
```bash
cd html
python -m http.server 3000
# Open http://localhost:3000
```

## Game Controls

| Key | Action |
|-----|--------|
| **SPACE** / **Click** | Jump (hold for stronger jump) |
| **P** | Pause/Resume |
| **G** | Toggle God Mode (invincibility) |
| **I** | Add 5 extra lives |
| **ESC** | Quit (Python) / Menu (Web) |

## Project Structure

```
flappybird/
├── python/              # Python/pygame implementation
│   ├── myflappy/       # Game package
│   │   ├── main.py     # Game loop and states
│   │   ├── bird.py     # Player physics
│   │   ├── pipes.py    # Obstacle generation
│   │   ├── cloud.py    # Background elements
│   │   ├── ground.py   # Ground collision
│   │   └── constants.py # Configuration
│   └── pyproject.toml  # Package setup
│
├── html/               # Web implementation
│   ├── index.html     # Game UI
│   ├── game.js        # Game logic
│   ├── server.js      # Express server
│   └── package.json   # Dependencies
│
├── PROMPTS/           # AI development prompts
│   ├── vscode-prompts.md # Step-by-step prompts
│   └── tuts.md        # Implementation tutorial
│
└── CLAUDE.md          # AI assistant guidance
```

## Technical Overview

### Python Version
- Built with **pygame** for cross-platform desktop support
- Modular architecture with separate classes for game entities
- State machine for game flow (START → PLAYING → PAUSED/GAMEOVER)
- Configurable physics and difficulty parameters
- Package-installable with `pip install -e .`

### Web Version
- Pure HTML5 Canvas with vanilla JavaScript
- RequestAnimationFrame for smooth 60 FPS rendering
- Express.js server for local development
- Mobile-responsive with touch controls
- Feature parity with Python version

## Game Mechanics

### Physics
- **Gravity**: Constant downward acceleration
- **Jump**: Instant upward velocity with optional hold boost
- **Collision**: Pixel-perfect rectangle collision detection

### Scoring
- 1 point per pipe passed
- High score tracking per session
- Lives system with collision forgiveness

### Difficulty Tuning
Adjust these parameters in the configuration files:
- `PIPE_SPEED` - Horizontal scroll speed
- `PIPE_GAP` - Vertical space between pipes
- `GRAVITY` - Fall acceleration
- `JUMP_STRENGTH` - Jump power

## Development

This project was created using AI-assisted development, demonstrating:
1. Rapid prototyping from specifications
2. Iterative feature development
3. Code modularization and refactoring
4. Cross-platform porting
5. Documentation generation

The complete development history is preserved in the `PROMPTS/` folder, showing the evolution from a simple single-file prototype to a fully-featured, packaged game.

## Installation for Development

### Python Development
```bash
cd python
pip install -e .  # Editable install
python -m myflappy
```

### Web Development
```bash
cd html
npm install
npm start  # Auto-reloads on changes
```

## Testing

Both versions include debug features for testing:
- Press **G** for God Mode (no collision damage)
- Press **I** to add extra lives
- Modify constants files for gameplay tweaks

## Contributing

Feel free to fork and enhance! Some ideas:
- Add sound effects and music
- Implement sprite animations
- Create difficulty levels
- Add leaderboards
- Mobile app versions

## License

This project is open source and available for educational purposes.

## Credits

Created as a learning project to demonstrate AI-assisted game development using Claude.