import pygame
import random

# Cloud settings (exported)
CLOUD_COLOR = (255, 255, 255)
CLOUD_MIN_SPEED = 0.3
CLOUD_MAX_SPEED = 0.9
CLOUD_MIN_SCALE = 0.6
CLOUD_MAX_SCALE = 1.3
CLOUD_COUNT = 6
CLOUD_SPAWN_BUFFER = 120  # how far beyond right edge to spawn

class Cloud:
    """Simple multi-ellipse cloud for parallax background.

    Refactored to be independent of main.py globals. Provide window dimensions
    and ground height at construction/spawn time so we avoid circular deps.
    """
    def __init__(self, window_width: int, window_height: int, ground_height: int, x: int | None = None):
        self._window_width = window_width
        self._window_height = window_height
        self._ground_height = ground_height
        self.scale = random.uniform(CLOUD_MIN_SCALE, CLOUD_MAX_SCALE)
        base_w = int(100 * self.scale)
        base_h = int(60 * self.scale)
        self.width = base_w
        self.height = base_h
        if x is None:
            max_start_x = max(0, window_width - base_w)
            self.x = random.randint(0, max_start_x)
        else:
            self.x = x
        sky_top = 10
        sky_bottom = window_height - ground_height - 200
        if sky_bottom < sky_top + 20:
            sky_bottom = sky_top + 20
        self.y = random.randint(sky_top, sky_bottom)
        self.speed = random.uniform(CLOUD_MIN_SPEED, CLOUD_MAX_SPEED)
        # Pre-render shape
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self._render_shape()

    def _render_shape(self):
        w, h = self.width, self.height
        ellipses = [
            (0.05, 0.45, 0.42, 0.5),
            (0.25, 0.25, 0.5, 0.6),
            (0.50, 0.40, 0.45, 0.5),
            (0.35, 0.10, 0.40, 0.55),
        ]
        for (ex, ey, ew, eh) in ellipses:
            rect = (int(ex * w), int(ey * h), int(ew * w), int(eh * h))
            pygame.draw.ellipse(self.surface, (*CLOUD_COLOR, 210), rect)

    def update(self):
        self.x -= self.speed

    def draw(self, target):
        target.blit(self.surface, (int(self.x), int(self.y)))

    def off_screen(self):
        return self.x + self.width < 0

    @staticmethod
    def spawn_at_right(window_width: int, window_height: int, ground_height: int):
        return Cloud(window_width, window_height, ground_height, x=window_width + random.randint(0, CLOUD_SPAWN_BUFFER))
