# Flappy Bird Web Version

## Quick Start

### Option 1: Using Node.js Server (Recommended)

1. Install dependencies:
```bash
npm install
```

2. Start the server:
```bash
npm start
```

3. Open your browser and navigate to:
```
http://localhost:3000
```

### Option 2: Using Python's built-in server

If you don't have Node.js installed, you can use Python:

```bash
# Python 3
python -m http.server 3000

# Python 2
python -m SimpleHTTPServer 3000
```

Then open http://localhost:3000 in your browser.

### Option 3: Direct file opening

Simply open `index.html` directly in your web browser (though some features may be limited due to CORS policies).

## Changing the Port

To use a different port, you can:

1. **For Node.js server**: Set the PORT environment variable
```bash
# Windows
set PORT=8080 && npm start

# Mac/Linux
PORT=8080 npm start
```

2. **For Python server**: Change the port number in the command
```bash
python -m http.server 8080
```

## Game Controls

- **SPACE** or **Click**: Jump/Fly
- **P**: Pause/Resume
- **G**: Toggle God Mode
- **I**: Add 5 extra lives
- **ESC**: Return to main menu

## Features

- Lives system (start with 3 lives)
- Score tracking
- Parallax cloud backgrounds
- Collision detection with visual feedback
- Pause functionality
- Debug mode for testing