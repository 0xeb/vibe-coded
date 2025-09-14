import pygame
import random

# Default colors (can be overridden when calling draw_pipe)
PIPE_BODY_COLOR = (34, 139, 34)      # Green body
PIPE_CAP_COLOR = (192, 192, 192)      # Silver cap
PIPE_DARK_SHADE = (20, 90, 20)
PIPE_LIGHT_SHADE = (60, 170, 60)
PIPE_OUTLINE_COLOR = (0, 60, 0)

CAP_HEIGHT = 20
CAP_OVERHANG = 6   # how many pixels the cap extends beyond pipe body on each side
BAND_HEIGHT = 8    # decorative band height


def _draw_pipe_body(surface, rect, body_color):
    # Main body fill
    pygame.draw.rect(surface, body_color, rect)
    # Shading stripes (simple depth illusion)
    left_shade = pygame.Rect(rect.x + 4, rect.y, 6, rect.height)
    right_shade = pygame.Rect(rect.right - 10, rect.y, 6, rect.height)
    pygame.draw.rect(surface, PIPE_DARK_SHADE, left_shade)
    pygame.draw.rect(surface, PIPE_LIGHT_SHADE, right_shade)
    # Decorative horizontal band (near opening edge)
    if rect.height > BAND_HEIGHT * 2:  # avoid tiny artifacts
        # For top pipe, band near bottom; for bottom pipe, band near top.
        if rect.y == 0:  # top pipe heuristic (starts at y=0)
            band_y = rect.bottom - BAND_HEIGHT - CAP_HEIGHT // 2
        else:            # bottom pipe
            band_y = rect.y + CAP_HEIGHT // 2
        band_rect = pygame.Rect(rect.x, band_y, rect.width, BAND_HEIGHT)
        pygame.draw.rect(surface, PIPE_DARK_SHADE, band_rect)


def _draw_cap(surface, body_rect, cap_color, is_top_pipe):
    # Cap spans slightly wider than pipe body
    cap_width = body_rect.width + CAP_OVERHANG * 2
    x = body_rect.x - CAP_OVERHANG
    if is_top_pipe:
        # Cap at lower end of top pipe (opening)
        y = body_rect.bottom - CAP_HEIGHT
    else:
        # Cap at upper end of bottom pipe (opening)
        y = body_rect.y
    cap_rect = pygame.Rect(x, y, cap_width, CAP_HEIGHT)
    pygame.draw.rect(surface, cap_color, cap_rect, border_radius=3)
    # Outline
    pygame.draw.rect(surface, PIPE_OUTLINE_COLOR, cap_rect, 2, border_radius=3)
    # Inner highlight line
    highlight_y = y + 4 if not is_top_pipe else y + CAP_HEIGHT - 6
    pygame.draw.line(surface, (220, 220, 220), (x + 4, highlight_y), (x + cap_width - 4, highlight_y), 2)


def draw_pipe(surface, top_rect, bottom_rect, body_color=PIPE_BODY_COLOR, cap_color=PIPE_CAP_COLOR):
    """Draws a stylized pair of pipes (top & bottom) given their body rects.

    This keeps collision logic unchanged (collisions still use original rects).
    """
    # Draw top pipe body then its cap
    _draw_pipe_body(surface, top_rect, body_color)
    _draw_cap(surface, top_rect, cap_color, is_top_pipe=True)

    # Draw bottom pipe body then its cap
    _draw_pipe_body(surface, bottom_rect, body_color)
    _draw_cap(surface, bottom_rect, cap_color, is_top_pipe=False)

    # Optional outlines for bodies (subtle)
    pygame.draw.rect(surface, PIPE_OUTLINE_COLOR, top_rect, 2)
    pygame.draw.rect(surface, PIPE_OUTLINE_COLOR, bottom_rect, 2)


class Pipe:
    """Game pipe composed of a top and bottom Rect with a gap.

    All numeric tuning parameters are passed in so this module stays decoupled
    from global constants living in main.py.
    """

    def __init__(self, x: int, *, gap: int, width: int, speed: float, window_height: int, ground_height: int):
        gap_y = random.randint(80, window_height - ground_height - 80 - gap)
        self.top_rect = pygame.Rect(x, 0, width, gap_y)
        self.bottom_rect = pygame.Rect(x, gap_y + gap, width, window_height - ground_height - (gap_y + gap))
        self._speed = speed
        self.passed = False

    def update(self):
        self.top_rect.x -= self._speed
        self.bottom_rect.x -= self._speed

    def draw(self, surface):
        # Delegate to stylized drawing
        draw_pipe(surface, self.top_rect, self.bottom_rect)

    def off_screen(self):
        return self.top_rect.right < 0

    def collide(self, bird_rect: pygame.Rect) -> bool:
        return self.top_rect.colliderect(bird_rect) or self.bottom_rect.colliderect(bird_rect)
