# Tic Tac Toe Development - Progressive Prompts

Build a Tic Tac Toe game step by step using Python and pygame.

## Prompt 1: Basic Game Window

```
Create a Tic Tac Toe game using pygame:
- 600x600 pixel window with white background
- Draw a 3x3 grid with black lines (5 pixels thick)
- Grid should evenly divide the window into 9 cells
- Basic game loop that handles quit events
```

## Prompt 2: Add Click Detection and Board State

```
Add game logic to track the board:
- Create a 3x3 array to store board state (0=empty, 1=X, 2=O)
- Detect which cell was clicked with the mouse
- Alternate between X and O players
- Don't allow clicking on already occupied cells
- Print board state to console for debugging
```

## Prompt 3: Draw X's and O's

```
Draw the game pieces on the board:
- Draw X as two blue crossed lines (thick)
- Draw O as a red circle outline (thick)
- Center them in their cells with padding
- Draw all pieces based on board state
```

## Prompt 4: Add Win Detection

```
Implement win detection:
- Check all 8 possible win conditions (3 rows, 3 columns, 2 diagonals)
- Detect winner after each move
- Stop accepting moves after someone wins
- Display "Player X Wins!" or "Player O Wins!" at the bottom
```

## Prompt 5: Add Draw Detection and Reset

```
Complete the game logic:
- Detect when the game is a draw (board full, no winner)
- Display "It's a Draw!" when appropriate
- Add 'R' key to reset the game at any time
- Show whose turn it is during gameplay
```

## Prompt 6: Visual Polish

```
Improve the appearance:
- Use better colors (light gray grid lines, darker blue/red for pieces)
- Add hover effect - highlight cell under mouse with light background
- Make X and O thicker and add margins from cell edges
- Use a nice font for text display
- Center all text properly
```

## Prompt 7: Add Game States

```
Implement proper game state management:
- Create START, PLAYING, and GAME_OVER states
- Start screen shows "Press SPACE to start"
- Game over screen shows result and "Press R to play again"
- ESC key returns to start screen
```

## Prompt 8: Create C# Version (Optional)

```
Create a C# console version of Tic Tac Toe:
- Use the same game logic
- Display board using ASCII characters
- Number cells 1-9 for input
- Clear console and redraw after each move
- Include win/draw detection
```

## Notes

- Each prompt builds on the previous implementation
- Test thoroughly after each step
- The progression goes from visual → interaction → logic → polish
- Final result should be a complete, polished game