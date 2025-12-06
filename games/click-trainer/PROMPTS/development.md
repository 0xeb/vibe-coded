# Click Trainer Game Prompt

Create a self-contained HTML/CSS/JS click training game with these features:

## Core Mechanics
- Full-screen canvas with crosshair cursor
- One ball appears at a time at random position
- Click the ball to score and spawn next ball
- Track reaction time for each click

## Configurable Options
- **Ball count**: Number of targets per round (1-100)
- **Ball size**: Diameter of targets (10-100px)

## Controls
- Number inputs for ball count and size
- Start button to begin a round
- Reset button to clear and start over

## Statistics Display
- Clicked count / Total count
- Average reaction time (milliseconds)
- Best reaction time in session

## UI/UX
- Dark theme with gradient background
- Colorful balls with glow/shadow effects
- Controls bar at top of screen
- Stats bar at bottom of screen
- Center message for game state (start, complete)

## Technical Notes
- Use canvas for rendering balls
- Use `performance.now()` for precise timing
- Spawn balls avoiding top (controls) and bottom (stats) areas
- Handle window resize to update canvas dimensions
- Store times in array for average calculation
