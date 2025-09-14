# Flappy Bird Python Development - Progressive Prompts

Build a Flappy Bird clone step by step using Python and pygame. Each prompt builds on the previous one.

## Prompt 1: Initial Specification and Implementation

```
Let's create a simple Python Flappy Bird 2d platformer game. We don't need artwork, just use rectangles and squares with different colors as needed. We will use the pygame framework which is installed.

Create a single Python file with:
- A bird (yellow rectangle) that falls due to gravity
- Spacebar makes the bird jump
- Green pipes that scroll from right to left
- Collision detection between bird and pipes
- Score that increases when passing pipes
- Game over when hitting pipes or ground
- 800x600 window
```

## Prompt 2: Add Lives System

```
Let's improve the game by implementing lives. Instead of directly losing when hitting a pipe:
- Start with 3 lives
- When hitting a pipe, deduct a life and give 1 second of invulnerability
- Flash the bird during invulnerability
- Display remaining lives in top-left corner
- Only game over when all lives are lost
```

## Prompt 3: Make Physics Tunable

```
Let's expose global variables at the top of the file to control the game physics:
- GRAVITY for falling speed
- JUMP_STRENGTH for jump power  
- PIPE_SPEED for scrolling speed
- PIPE_GAP for the gap between upper and lower pipes
- PIPE_FREQUENCY for how often pipes spawn

Put these constants at the very top of the file with comments explaining each one.
```

## Prompt 4: Add Pause Feature

```
Add a pause feature to the game:
- Press 'P' to pause and unpause
- When paused, stop all movement (bird, pipes, physics)
- Display "PAUSED" text in center of screen
- Game should resume exactly where it left off
```

## Prompt 5: Add Debug Features

```
Add debug features for testing:
- Press 'I' to instantly add 5 extra lives
- Press 'G' to toggle God Mode (invincibility)
- When in God Mode, display "GOD MODE" in top-right corner
- In God Mode, bird can't die but score still works
```

## Prompt 6: Add Background Elements

```
Let's add clouds in the background for visual depth:
- Create 3-4 white clouds that move slowly from right to left
- Clouds should be behind pipes but in front of sky
- Different sizes and speeds for parallax effect
- Clouds should wrap around when they go off screen
- Use simple white circles or rectangles for clouds
```

## Prompt 7: Modularize the Code

```
Let's refactor the code into a cleaner structure:
- Create a Bird class with update() and draw() methods
- Create a Pipe class for pipe management
- Create a Cloud class for background clouds
- Keep all game constants at the top
- Main game loop should be cleaner and easier to read
```

## Prompt 8: Create Package Structure

```
Let's turn this into a proper Python package:
- Create a folder structure: myflappy/ with __init__.py, __main__.py
- Split code into modules: main.py, bird.py, pipes.py, cloud.py, ground.py, constants.py
- Create pyproject.toml for pip installation
- Make it runnable with: python -m myflappy
- Include entry point so it installs as 'myflappy' command
```

## Prompt 9: Add Visual Polish

```
Instead of plain rectangles, let's draw better graphics using pygame shapes:
- Bird: Yellow circle with orange beak triangle
- Pipes: Green rectangles with darker green caps
- Ground: Brown rectangle with grass line on top
- Clouds: Multiple white circles clustered together
Keep it simple but more visually appealing than plain rectangles.
```

## Prompt 10: Add High Score

```
Add a high score feature:
- Track the highest score achieved in the session
- Display "HI: [score]" next to current score
- When beating high score, flash "NEW HIGH SCORE!" message
- High score should persist only during the game session (no file saving needed)
```

## Prompt 11: Add Start Screen

```
Add a proper start screen:
- Show "FLAPPY BIRD" title
- Show "Press SPACE to start" instruction
- Show controls (SPACE: Jump, P: Pause, R: Reset)
- Bird should bob up and down on start screen
- Pressing space transitions to gameplay
```

## Prompt 12: Add Sound Effects (Optional)

```
Add simple sound effects using pygame:
- Jump sound when pressing space
- Score sound when passing pipes
- Hit sound when losing a life
- Game over sound when all lives lost
Use pygame.mixer to generate simple beep sounds programmatically (no external files).
```

## Notes

- Start with Prompt 1 and ensure the game works before moving to the next
- Each prompt adds specific functionality while maintaining what was built before
- The progression goes from basic gameplay → features → polish → packaging
- If any step fails, debug it before continuing to the next prompt
- The final result should be a complete, polished, installable Flappy Bird game