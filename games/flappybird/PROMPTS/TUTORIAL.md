# Flappy Bird in Pygame — A Practical, Code‑First Tutorial

This tutorial walks through a small Flappy Bird–style game implemented with Pygame. You know Python, so we’ll focus on game‑dev patterns: the game loop, input handling, timing, drawing, scrolling (“moving world”), collisions, and state management — all explained directly from this project’s code.


## Run the Game

- Install: `pip install pygame`
- From the project’s parent directory, run: `python -m myflappy`
  - Entrypoint is `myflappy/__main__.py` which calls `main()` in `myflappy/main.py`.
- Controls:
  - `SPACE` or mouse click: jump (hold briefly for a slightly stronger/longer jump)
  - `SPACE` at title: start
  - `P`: pause/resume
  - `G`: toggle “God mode” (no life loss on hit; useful for practice)
  - `I`: add 5 lives (debug/assist)
  - `ESC` or window close: quit


## Project Layout (What Each File Does)

- `main.py` — Game loop, state machine, high‑level orchestration and UI text.
- `constants.py` — All core tuning constants (window size, pipe speed/gap, colors, FPS, states).
- `bird.py` — Player entity: physics (gravity, jump strength, jump hold boosting) and drawing.
- `pipes.py` — Pipe pair entity (top + bottom) with movement, collision, stylized rendering.
- `ground.py` — Ground strip at the bottom and ground collision check.
- `cloud.py` — Parallax background clouds (slow drift, recycled when off‑screen).
- `__main__.py` — Module entrypoint (`python -m myflappy`).
- `myflappy.py` — Convenience wrapper to run `main()`.


## Pygame Essentials Used Here

- Initialization: `pygame.init()` and `pygame.font.init()`; create a `screen` via `pygame.display.set_mode((w, h))`.
- Clock and FPS: `clock = pygame.time.Clock()` and `clock.tick(FPS)` to cap frame rate.
- Surfaces and Rects: everything draws to the `screen` (a `Surface`). Collisions use `pygame.Rect`.
- Event loop: read `pygame.event.get()` each frame and react to `KEYDOWN`, `KEYUP`, `MOUSEBUTTONDOWN`, etc.
- Timing: `pygame.time.get_ticks()` returns milliseconds since init; used to schedule pipe spawns.
- Drawing: primitives like `pygame.draw.rect`, `ellipse`, `line`, `polygon`, and blitting of pre‑rendered surfaces.
- Display update: `pygame.display.flip()` swaps buffers to show the frame.


## The Core Game Loop and States

This game uses a simple state machine: `START`, `PLAYING`, `PAUSED`, `GAMEOVER`.

High‑level loop (simplified from `main.py`):

```python
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
state = STATE_START

while running:
    clock.tick(FPS)                # cap the frame rate and pace updates
    for event in pygame.event.get():
        handle_input(event, state) # respond to keyboard/mouse

    screen.fill(BG_COLOR)          # clear the frame

    if state == STATE_START:
        draw_title_and_prompt()
    elif state == STATE_PLAYING:
        update_world()             # bird physics, pipes, clouds
        check_collisions_and_score()
        draw_world()
    elif state == STATE_PAUSED:
        draw_world_frozen()
        draw_paused_overlay()
    elif state == STATE_GAMEOVER:
        draw_world_frozen()
        draw_game_over_overlay()

    pygame.display.flip()          # present the frame
```

Key ideas:

- Update vs. Draw: most objects have an `update()` (change their position/state) and `draw()` (render to the screen).
- Pausing: in `STATE_PAUSED`, the scene is drawn but not updated; timing for spawns is adjusted so rhythm resumes correctly on unpause.
- State transitions happen via input (e.g., `SPACE` to start) or game conditions (e.g., running out of lives → `GAMEOVER`).


## How Scrolling Works (Moving World)

There is no camera; instead, the world moves left:

- Pipes are spawned just off the right edge and move left each frame by `PIPE_SPEED`.
- Clouds (background) also drift left, but much slower (`0.3–0.9` px/frame) for parallax.
- The ground is static; only the obstacles and background move.

In `pipes.Pipe.update()`:

```python
def update(self):
    self.top_rect.x -= self._speed
    self.bottom_rect.x -= self._speed
```

Clouds similarly update their `x` by a small speed. When a cloud moves off the left edge, a new one is spawned just beyond the right edge to keep the sky filled.


## Bird Physics and Input (Jump Feathering)

The bird’s motion is a simple vertical integrator with gravity, plus a “hold to feather” jump:

- Gravity adds to velocity each frame: `vel += GRAVITY`.
- A jump sets an initial upward velocity (`JUMP_STRENGTH`, a negative number) and starts a short window (`JUMP_HOLD_FRAMES`) during which holding the key applies a small extra boost each frame (`JUMP_HOLD_BOOST`).
- Position is updated from velocity: `y += vel`. Collisions use `pygame.Rect` updated to the integer position.

From `bird.py`:

```python
def update(self):
    if self.jump_held and self.jump_boost_frames > 0:
        self.vel += JUMP_HOLD_BOOST
        self.jump_boost_frames -= 1
    self.vel += GRAVITY
    self.y += self.vel
    self.rect.y = int(self.y)

def jump(self):
    self.vel = JUMP_STRENGTH
    self.jump_boost_frames = JUMP_HOLD_FRAMES
    self.jump_held = True

def jump_release(self):
    self.jump_held = False
    self.jump_boost_frames = 0
```

This makes jumps feel more analog: a quick tap gives a small hop; a brief hold allows a rounder arc without becoming too floaty.


## Pipes: Spawning, Movement, and Collision

- Pipes spawn at a fixed interval (`PIPE_INTERVAL` ms) using `pygame.time.get_ticks()`.
- Each pipe instance is actually a pair of rects: one from the top of the screen down to the gap, and one from just below the gap to just above the ground. Both share the same `x` and move left.
- Collision is a simple `Rect.colliderect` against either rect.

Spawn logic (from `main.py`):

```python
now = pygame.time.get_ticks()
if now - last_pipe_time > PIPE_INTERVAL:
    pipes.append(Pipe(WINDOW_WIDTH, gap=PIPE_GAP, width=PIPE_WIDTH, speed=PIPE_SPEED,
                      window_height=WINDOW_HEIGHT, ground_height=GROUND_HEIGHT))
    last_pipe_time = now
```

Movement and collision (from `pipes.py`):

```python
def update(self):
    self.top_rect.x -= self._speed
    self.bottom_rect.x -= self._speed

def collide(self, bird_rect):
    return self.top_rect.colliderect(bird_rect) or self.bottom_rect.colliderect(bird_rect)
```

Rendering uses `_draw_pipe_body` and `_draw_cap` to add simple shading and a “cap” near the gap for a more polished look.


## Clouds: Simple Parallax Background

`cloud.Cloud` creates a small off‑screen `Surface` with several ellipses to look like a cloud, then blits that each frame at a slowly decreasing `x` (leftward drift). When a cloud goes fully off the left, a new cloud is spawned just beyond the right edge (`spawn_at_right`). Heights and scales are randomized within a sky band (avoiding the ground).


## Ground and World Bounds

The ground is a simple `Rect` spanning the bottom `GROUND_HEIGHT` pixels. Hitting the ground or going above the top counts as a collision during play.

```python
class Ground:
    def __init__(self):
        self.rect = pygame.Rect(0, WINDOW_HEIGHT - GROUND_HEIGHT, WINDOW_WIDTH, GROUND_HEIGHT)

    def collide(self, bird_rect):
        return self.rect.colliderect(bird_rect)
```


## Scoring, Lives, and Feedback

- Score increments when the pipe’s right edge passes the bird’s `x` position (first time only per pipe).
- The player has `lives = 3`. On collision, a short cooldown prevents immediate repeated hits. If lives reach zero, the state switches to `GAMEOVER`.
- A brief red “impact X” is drawn at the approximate collision point for visual feedback.
- God mode (`G`) leaves lives untouched but still flashes impact.

Score check (from `main.py`):

```python
for pipe in pipes:
    if not pipe.passed and pipe.top_rect.right < bird.x:
        score += 1
        pipe.passed = True
```


## Input Handling Details

- `KEYDOWN`/`KEYUP` for `SPACE` drive `bird.jump()` and `bird.jump_release()`.
- Mouse down/up also jump/release, mirroring spacebar.
- `P` toggles pause. On resume, the code adjusts `last_pipe_time` so pipe spawn timing stays consistent (no “catch‑up burst”).
- `ESC` exits cleanly.


## Drawing Order (Why It Looks Right)

The order of draw calls establishes layers:

1. Clouds (background)
2. Pipes
3. Bird
4. Ground
5. UI text (score, lives, God mode tag)
6. Impact indicator (brief flashing X)

Drawing is immediate; the final `pygame.display.flip()` reveals the composed frame.


## Timing and Pausing Without Glitches

Pipes spawn based on real time (`get_ticks()`), not frame count, which keeps cadence stable across machines. When pausing, the code captures `pause_start_time` and on resume adds the paused duration to `last_pipe_time` so the next spawn happens when it would have if the game had never paused.


## Tuning Difficulty

Open `constants.py` to adjust feel:

- `PIPE_SPEED` — lower to make the game easier (e.g., `2.6`).
- `PIPE_GAP` — increase for easier gaps (e.g., `200+`).
- `GRAVITY`, `JUMP_STRENGTH`, `JUMP_HOLD_BOOST`, `JUMP_HOLD_FRAMES` (in `bird.py`) — tweak arc shape and responsiveness.
- `PIPE_WIDTH` — wider pipes slightly lengthen the “scoring window”.

Make small changes and test; these constants interact to shape the flight arc and rhythm.


## Minimal Patterns to Reuse in Your Own Games

1) Game loop + state machine

```python
running = True
state = STATE_START
while running:
    dt = clock.tick(FPS)  # milliseconds between frames, if you need it
    for event in pygame.event.get():
        handle_input(event, state)
    update_by_state(state)
    draw_by_state(state)
    pygame.display.flip()
```

2) Spawn things on a cadence

```python
now = pygame.time.get_ticks()
if now - last_spawn_ms >= interval_ms:
    spawn_thing()
    last_spawn_ms = now
```

3) Simple physics integrator

```python
vel_y += gravity
y += vel_y
if jumping:
    vel_y = jump_strength
```

4) Rect‑based collision and off‑screen cleanup

```python
if player_rect.colliderect(obstacle_rect):
    handle_hit()
things = [t for t in things if t.rect.right > 0]
```


## Extending This Game

- Add animations (sprite sheets) to the bird or coins to collect.
- Add sound effects for jump, score, and collision (via `pygame.mixer`).
- Add difficulty ramp: slowly increase `PIPE_SPEED` or decrease `PIPE_GAP` over time.
- Add a menu and high‑score persistence (write to a small JSON file).
- Add mobile‑friendly input (single “tap” with repeats/debouncing).


## Troubleshooting

- If the window doesn’t open or crashes on import, ensure Pygame is installed for the same Python interpreter you’re using: `python -m pip show pygame`.
- On high‑DPI displays, window sizes can feel small; increase `WINDOW_WIDTH`/`WINDOW_HEIGHT` in `constants.py` proportionally.
- If frame rate stutters, avoid heavy per‑frame allocations and prefer reusing `Surface`s (like the clouds do) or caching fonts.


## Takeaways

- Pygame’s model is straightforward: a loop that reads input, updates objects, draws them, and flips the screen.
- Scrolling worlds are usually implemented by moving entities leftwards (no camera needed for simple games).
- `Rect` collision + simple physics gets you far; polish comes from timing, feedback, and tuned constants.

