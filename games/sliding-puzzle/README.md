# Sliding Puzzle

A classic number sliding puzzle game built as a single HTML file with no external dependencies. Features multiple grid sizes and an automated solver.

## Development Prompts

**[View the prompt used to build this application →](PROMPTS/)**

## Features

- **Multiple grid sizes** - Choose between 3×3, 4×4, or 5×5 puzzles
- **Colorful tiles** - Each number has a unique color for easy identification
- **Move counter** - Track your progress
- **Auto-solver** - Watch the puzzle solve itself with IDA* algorithm
- **Speed control** - Adjust solve animation speed (50ms–500ms per move)
- **Shuffle history** - Instant solve by reversing shuffle moves
- **Win detection** - Celebration modal when puzzle is completed
- **Dark theme** - Easy on the eyes with gradient background
- **Responsive design** - Works on desktop and mobile

## Quick Start

### Option 1: Direct File Access
Simply open `sliding-puzzle.html` in any modern web browser

### Option 2: Local Server
```bash
# Using Python
python -m http.server 8000
# Open http://localhost:8000/sliding-puzzle.html

# Using Node.js
npx http-server
# Open http://localhost:8080/sliding-puzzle.html
```

## How to Play

1. **Select grid size** - Click 3×3, 4×4, or 5×5 button
2. **Shuffle** - Click Shuffle to randomize the puzzle
3. **Slide tiles** - Click any tile adjacent to the empty space
4. **Goal** - Arrange tiles in numerical order (1, 2, 3... with empty at bottom-right)
5. **Auto-solve** - Click Solve to watch the solution animate
6. **Adjust speed** - Use the slider to control solve animation speed

## Controls

| Button | Action |
|--------|--------|
| Shuffle | Randomize the puzzle (ensures solvability) |
| Solve | Animate the solution |
| Stop | Cancel solve animation |
| Reset | Return to solved state |

## Technical Details

- **Single file** - Everything in one HTML file for easy sharing
- **No dependencies** - Pure HTML, CSS, and JavaScript
- **IDA* solver** - Iterative deepening A* with Manhattan distance heuristic
- **Shuffle optimization** - Records moves for instant reverse-solve
- **Cross-browser** - Works in Chrome, Firefox, Safari, Edge

## Solver Algorithm

The game uses two solving strategies:

1. **Fast path**: If the user hasn't manually moved any tiles, the solver simply reverses the recorded shuffle history for an instant solution.

2. **IDA* algorithm**: If the user has moved tiles, the solver computes an optimal solution using:
   - Iterative deepening A* search
   - Manhattan distance heuristic
   - Best-first neighbor ordering
   - Max 1,000,000 iterations to prevent hangs

## Customization

The single-file design makes it easy to:
- Add new grid sizes (modify `tileSizes` object)
- Change color scheme (modify `colors` array)
- Adjust shuffle intensity (modify `shuffleMoves` calculation)
- Customize styling (modify CSS)

## License

Open source for educational use.
