# Core game constants centralized here

# Window / layout
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
GROUND_HEIGHT = 100

# Pipe tuning
PIPE_WIDTH = 80          # Widened pipes (visual + scoring pacing)
PIPE_GAP = 190           # Larger gap for easier play
PIPE_SPEED = 3           # Keep speed for now (can lower later if still hard)
PIPE_INTERVAL = 1500     # milliseconds between spawns

# Colors
BG_COLOR = (135, 206, 250)   # Light blue
BIRD_COLOR = (255, 215, 0)   # Yellow (not currently used directly; bird draws itself)
PIPE_COLOR = (34, 139, 34)   # Green (stylized pipe module may override)
GROUND_COLOR = (139, 69, 19) # Brown
SCORE_COLOR = (255, 255, 255)  # White
IMPACT_COLOR = (255, 0, 0)     # Red for impact markers

# Timing / performance
FPS = 60

# Game States
STATE_START = 0
STATE_PLAYING = 1
STATE_GAMEOVER = 2
STATE_PAUSED = 3
