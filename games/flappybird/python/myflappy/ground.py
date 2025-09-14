import pygame
from .constants import WINDOW_WIDTH, WINDOW_HEIGHT, GROUND_HEIGHT, GROUND_COLOR

class Ground:
    """Static ground strip at bottom of the screen."""
    def __init__(self):
        self.rect = pygame.Rect(0, WINDOW_HEIGHT - GROUND_HEIGHT, WINDOW_WIDTH, GROUND_HEIGHT)

    def draw(self, surface):
        pygame.draw.rect(surface, GROUND_COLOR, self.rect)

    def collide(self, bird_rect):
        return self.rect.colliderect(bird_rect)
