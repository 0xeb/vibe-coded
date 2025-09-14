import pygame

# Bird physics & sizing constants (centralized)
BIRD_WIDTH = 40
BIRD_HEIGHT = 30
BIRD_X = 50
GRAVITY = 0.38
JUMP_STRENGTH = -7
JUMP_HOLD_BOOST = -0.35
JUMP_HOLD_FRAMES = 14

YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)

def draw_bird(surface, x: int, y: int):
    """Draw the bird at top-left (x,y)."""
    pygame.draw.ellipse(surface, YELLOW, (x, y, 40, 30))           # body
    pygame.draw.ellipse(surface, ORANGE, (x+10, y+10, 20, 10))     # wing
    pygame.draw.polygon(surface, ORANGE, [(x+40, y+15), (x+50, y+20), (x+40, y+20)])  # beak
    pygame.draw.circle(surface, BLACK, (x+30, y+10), 3)            # eye

class Bird:
    """Player-controlled bird entity.

    Handles position, velocity, jump buffering / feathering; drawing now inlined.
    Coordinates are kept as floats for smoother physics
    while the rect used for collision is integer-aligned.
    """
    def __init__(self, start_y: int | None = None, window_height: int | None = None):
        if start_y is not None:
            self.y = float(start_y)
        else:
            if window_height is None:
                raise ValueError("Either start_y or window_height must be provided")
            self.y = window_height // 2 - BIRD_HEIGHT // 2
        self.x = BIRD_X
        self.vel = 0.0
        self.rect = pygame.Rect(self.x, int(self.y), BIRD_WIDTH, BIRD_HEIGHT)
        self.jump_held = False
        self.jump_boost_frames = 0

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

    def draw(self, surface):
        draw_bird(surface, self.rect.x, self.rect.y)

    def reset(self, window_height: int):
        self.__init__(window_height=window_height)
