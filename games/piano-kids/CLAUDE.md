# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Piano Kids is a standalone HTML5 educational piano game for children that runs entirely in the browser. The entire application is contained in a single HTML file (`piano-kids.html`) with embedded CSS and JavaScript.

## Architecture

The application is a single-page web app with:
- **Piano Interface**: 6 numbered keys (1-6) that play musical notes (C4-A4)
- **Song Library**: Pre-defined children's songs stored in `SONGS_TABLE` array
- **Playback System**: Demo mode that plays songs automatically with adjustable speed
- **Print Mode**: Alternative view for printing song sheets

## Key Components

### Data Structure
Songs are defined in the `SONGS_TABLE` array (line 337) with:
- `id`: Unique identifier
- `name`: Display name
- `notes`: Space-separated numbers (1-6) with commas for phrase breaks

### Audio System
- Uses Web Audio API with oscillators for sound generation
- Frequencies defined for notes 1-6 (C4 through A4)
- Volume control and playback speed controls (1x, 1.5x, 2x)

### Interaction Modes
1. **Play Mode**: Click piano keys or use keyboard numbers 1-6
2. **Demo Mode**: Automatic playback of selected songs
3. **Print Mode**: Printable song sheets with note numbers

## Development Commands

This is a standalone HTML file with no build process required. To run:
- Open `piano-kids.html` directly in a web browser
- Or serve via any HTTP server (e.g., `python -m http.server`)

## Testing

No automated tests are configured. Manual testing involves:
- Verifying all piano keys produce correct sounds
- Testing song playback at different speeds
- Checking print view formatting
- Testing keyboard input (numbers 1-6)