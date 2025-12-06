# Tic Tac Toe Game Prompt

Create a self-contained HTML/CSS/JS Tic Tac Toe game with these features:

## Core Mechanics
- 3x3 grid for placing X and O marks
- Two players take turns (X goes first)
- Win detection for rows, columns, and diagonals
- Draw detection when board is full

## Game Modes
- **2 Players**: Local multiplayer, players alternate turns
- **vs AI (Easy)**: AI makes random valid moves
- **vs AI (Hard)**: AI uses minimax algorithm for optimal play

## Controls
- Click any empty cell to place your mark
- Mode selector buttons to switch between game modes
- New Game button to reset the board
- Reset Scores button to clear the scoreboard

## Scoreboard
- Track wins for Player X
- Track wins for Player O
- Track draws
- Persist scores across games (until page refresh or manual reset)

## UI/UX
- Dark theme with gradient background
- X marks in red color with glow effect
- O marks in blue color with glow effect
- Hover effect on empty cells
- Winning cells highlighted with green background and pulse animation
- Turn indicator showing current player

## AI Implementation
- Easy mode: Random move selection from available cells
- Hard mode: Minimax algorithm
  - Maximizing player (O) seeks highest score
  - Minimizing player (X) seeks lowest score
  - Depth-aware scoring to prefer faster wins
  - Returns optimal move for unbeatable AI

## Technical Notes
- Single HTML file with embedded CSS and JavaScript
- No external dependencies
- Responsive design
- AI moves delayed slightly (400ms) for better UX
