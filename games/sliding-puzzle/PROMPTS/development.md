# Sliding Puzzle Game Prompt

Create a self-contained HTML/CSS/JS sliding puzzle game with these features:

## Core Mechanics
- Grid of numbered, colored tiles with one empty space
- Click a tile adjacent to the empty space to slide it into that space
- Goal: arrange tiles in numerical order (1, 2, 3... with empty space at the end)

## Configurable Grid Size
- Toggle buttons for 3×3, 4×4, and 5×5 grids
- Tile sizes scale appropriately (larger tiles for smaller grids)
- Default to 5×5

## Controls
- **Shuffle**: Randomize the puzzle by making valid moves (not random placement—ensures solvability). Record each move during shuffle.
- **Solve**: Animate the solution by replaying shuffle moves in reverse. No algorithm needed—just reverse the recorded history.
- **Stop**: Cancel solve animation mid-way
- **Reset**: Return to solved state

## Solve Animation
- Speed slider (50ms–500ms per move)
- Status display showing progress ("Solving: 12/100 moves")
- Disable other controls while solving
- If user manually moves a tile, invalidate the stored solution

## UI/UX
- Dark theme with gradient background
- Each tile number has a unique color
- Hover effect on tiles (scale up slightly)
- Highlight effect on tiles during solve animation
- Move counter
- Win detection with celebration modal

## Technical Notes
- Store shuffle history as array of empty-space positions
- Avoid back-and-forth during shuffle (don't undo previous move)
- Scale shuffle intensity with grid size (e.g., gridSize² × 4 moves)
