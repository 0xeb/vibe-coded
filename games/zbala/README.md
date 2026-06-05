# Zbala (زبالة السرايا)

A satirical trash-tossing arcade game inspired by the 2015 Lebanese garbage crisis. Toss trash bags into the windows of the Grand Serail (the government palace in Beirut) before time runs out.

Modernized from [ZbalaJS](https://github.com/lallousx86/ZbalaJS) (2018).

## Gameplay

- A trash bag slides left and right at the bottom of the screen
- Click or tap to launch it upward — timing matters!
- Click left or right of the bag to angle the shot
- Score a point when the bag goes through a window
- Bags can bounce off window edges (max 3 bounces)
- Only one bag in flight at a time
- You have 60 seconds — go for a high score!

## Usage

Serve from a local server (external assets required):
```bash
python -m http.server
```
Then open `zbala.html` in your browser.

## Controls

- **Click/Tap**: Launch bag (aim by clicking left/right of the bag)

## Credits

Original ZbalaJS by Elias Bachaalany (2018). Modernized with hybrid aiming, requestAnimationFrame, localStorage high scores, and tuned physics.
