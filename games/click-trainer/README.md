# Click Trainer

A reaction time training game built as a single HTML file. Click on randomly appearing targets as fast as possible to improve your aim and reflexes.

## Development Prompts

**[View the prompt used to build this application →](PROMPTS/)**

## Features

- **Configurable targets** - Set number of balls (1-100) per round
- **Adjustable size** - Change target size (10-100px diameter)
- **Reaction timing** - Tracks time to click each target
- **Statistics** - Average time, best time, and progress counter
- **Full-screen canvas** - Targets spawn across the entire screen
- **Glow effects** - Colorful targets with glow for visibility
- **Responsive** - Adapts to window resize

## Quick Start

### Option 1: Direct File Access
Simply open `click-trainer.html` in any modern web browser

### Option 2: Local Server
```bash
# Using Python
python -m http.server 8000
# Open http://localhost:8000/click-trainer.html

# Using Node.js
npx http-server
# Open http://localhost:8080/click-trainer.html
```

## How to Play

1. **Configure** - Set ball count and size (optional)
2. **Start** - Click the green Start button
3. **Click targets** - Click each ball as fast as you can
4. **Track progress** - Watch your stats at the bottom
5. **Complete** - See your final average and best times
6. **Reset** - Click Reset to try again

## Statistics Tracked

| Stat | Description |
|------|-------------|
| Clicked | Progress through current round |
| Avg Time | Average reaction time in milliseconds |
| Best Time | Fastest single click in session |

## Technical Details

- **Single file** - Everything in one HTML file
- **No dependencies** - Pure HTML, CSS, and JavaScript
- **Canvas rendering** - Hardware-accelerated graphics
- **High precision** - Uses `performance.now()` for timing
- **Cross-browser** - Works in Chrome, Firefox, Safari, Edge

## Use Cases

- **Gaming warmup** - Before FPS or competitive games
- **Reaction training** - Improve click speed
- **Hand-eye coordination** - Practice precision clicking
- **Benchmarking** - Compare reaction times

## License

Open source for educational use.
