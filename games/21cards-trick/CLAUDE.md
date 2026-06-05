# CLAUDE.md - 21 Cards Magic Trick

## Overview

Single-file HTML5 game implementing the classic 21-card magic trick with three modes: Play, How It Works (explainer), and Simulator.

## Development

```bash
cd games/21cards-trick
# Open directly in browser
start 21cards-trick.html
# Or serve with:
python -m http.server
```

## Architecture

- **Single file**: `21cards-trick.html` contains all HTML, CSS, and JS inline
- **No dependencies**: Pure vanilla JS, CSS animations only (no libraries)
- **Three modes**: Tab navigation switches between Play, Explain, and Simulator sections

## Key Implementation Details

- Core algorithm preserved from the original: `SHUFFLE_TABLE = [[1,0,2], [0,1,2], [0,2,1]]`
- `shuffleArray(col, arr)` gathers columns with the picked column in the middle
- 21 cards mapped to 3 suits (spades, hearts, diamonds) x 7 ranks (A-7)
- Play mode uses Fisher-Yates shuffle for random initial deck order
- Card flip uses CSS 3D transforms (`rotateY(180deg)`, `backface-visibility: hidden`)
- Staggered deal animation via CSS custom property `--i` per card
- `animBusy` flag prevents double-clicks during animation sequences
- The revealed card is always at index 10 (position 11) after 3 rounds
