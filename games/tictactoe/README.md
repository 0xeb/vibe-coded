# Tic Tac Toe

Classic Tic Tac Toe game implemented in multiple languages, demonstrating cross-language game development with consistent game logic.

## 📚 Development Prompts

**[View the progressive prompts used to build this game →](PROMPTS/)**

## Features

- **Two-player gameplay** - Take turns as X and O
- **Win detection** - All 8 win conditions checked
- **Draw detection** - Recognizes tied games
- **Visual feedback** - Clear indication of game state
- **Reset functionality** - Play multiple games without restarting

## Implementations

### HTML5 Version (Browser)
```bash
cd html
# Open tic-tac-toe.html directly in browser
# Or serve with: python -m http.server
```

**Features:**
- 2-player local multiplayer
- AI opponent (Easy - random, Hard - minimax)
- Score tracking
- Dark theme with animations

### Python Version (pygame)
```bash
pip install pygame
python tictactoe.py
```

**Controls:**
- Mouse click to place pieces
- R key to reset game
- ESC to quit

### C# Version
```bash
dotnet run
# or
dotnet build
./bin/Debug/net*/TicTacToe.exe
```

**Controls:**
- Enter cell number (1-9) to place piece
- Follow on-screen prompts

## Game Rules

1. Players take turns marking spaces in a 3×3 grid
2. Player 1 (X) always goes first
3. The first player to get 3 marks in a row (horizontally, vertically, or diagonally) wins
4. If all 9 squares are filled without a winner, the game is a draw

## Project Structure

```
tictactoe/
├── html/              # HTML5 browser version
│   ├── tic-tac-toe.html
│   └── PROMPTS/       # HTML version prompts
├── PROMPTS/           # AI development prompts
│   ├── README.md      # Prompts guide
│   └── development.md # Progressive prompts
├── tictactoe.py       # Python/pygame implementation
├── TicTacToe.cs       # C# console implementation
├── TicTacToe.csproj   # C# project file
└── README.md          # This file
```

## Technical Details

### HTML5 Version
- Single-file implementation (HTML/CSS/JS)
- Minimax algorithm for unbeatable AI
- Animated win highlighting
- Score persistence within session
- Dark gradient theme

### Python Version
- Uses pygame for graphics and input
- Object-oriented design with Board class
- 600x600 pixel window
- Color-coded pieces (Blue X, Red O)

### C# Version
- Console-based interface
- ASCII art for board display
- Numbered cell input (1-9)
- Clear console updates

## Learning Objectives

This project teaches:
- Game state management
- Input validation
- Win condition algorithms
- User interface design
- Cross-language implementation of same logic

## Development

See the [PROMPTS folder](PROMPTS/) for step-by-step instructions on building this game from scratch using AI assistance.