import pygame
import sys
import random

from .pipes import Pipe  # import Pipe class only
from .cloud import Cloud, CLOUD_COUNT
from .bird import Bird, BIRD_WIDTH, BIRD_HEIGHT, BIRD_X, GRAVITY, JUMP_STRENGTH, JUMP_HOLD_BOOST, JUMP_HOLD_FRAMES
from .ground import Ground
from .constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, GROUND_HEIGHT,
    PIPE_WIDTH, PIPE_GAP, PIPE_SPEED, PIPE_INTERVAL,
    BG_COLOR, SCORE_COLOR, IMPACT_COLOR,
    FPS,
    STATE_START, STATE_PLAYING, STATE_GAMEOVER, STATE_PAUSED,
)

pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 36, bold=True)
SMALL_FONT = pygame.font.SysFont('Arial', 24)

# Physics rationale:
#   Lower GRAVITY + slightly weaker initial JUMP_STRENGTH smooths arcs.
#   Extended JUMP_HOLD_FRAMES allows gentle feathering without overpowering.
#   Wider PIPE_WIDTH + increased PIPE_GAP reduce precision strain early on.
#   If still hard: options -> reduce PIPE_SPEED to 2.6, raise PIPE_GAP to 200, or GRAVITY to 0.34.


def draw_cross(surface, x, y, size=20, color=IMPACT_COLOR, thickness=3):
    """Draw a simple X (cross) centered at (x, y)."""
    half = size // 2
    pygame.draw.line(surface, color, (x - half, y - half), (x + half, y + half), thickness)
    pygame.draw.line(surface, color, (x - half, y + half), (x + half, y - half), thickness)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Flappy Bird')

"""Modules imported: bird, pipes, cloud, ground, constants."""

def draw_text_center(surface, text, font, color, y):
    render = font.render(text, True, color)
    rect = render.get_rect(center=(WINDOW_WIDTH // 2, y))
    surface.blit(render, rect)


"""Cloud logic moved to cloud.Cloud; main orchestrates instances."""

def main():
    state = STATE_START
    bird = Bird(window_height=WINDOW_HEIGHT)
    pipes = []
    ground = Ground()
    score = 0
    last_pipe_time = pygame.time.get_ticks()
    lives = 3
    collision_cooldown = 0  # frames to forgive after a hit
    impact_timer = 0         # frames remaining to show impact marker
    impact_pos = None        # (x, y) center point of impact
    pause_start_time = None  # track when pause began
    god_mode = False         # toggle with 'G' key
    # Clouds (background)
    clouds = [Cloud(WINDOW_WIDTH, WINDOW_HEIGHT, GROUND_HEIGHT) for _ in range(CLOUD_COUNT)]

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_i and state == STATE_PLAYING:
                    # Debug / assist hotkey: grant 5 extra lives
                    lives += 5
                if event.key == pygame.K_g:
                    god_mode = not god_mode
                if event.key == pygame.K_p:
                    if state == STATE_PLAYING:
                        state = STATE_PAUSED
                        pause_start_time = pygame.time.get_ticks()
                    elif state == STATE_PAUSED:
                        # adjust timers so pipe spawn rhythm stays consistent
                        paused_duration = pygame.time.get_ticks() - pause_start_time if pause_start_time else 0
                        last_pipe_time += paused_duration
                        state = STATE_PLAYING
                        pause_start_time = None
                if state == STATE_START and event.key == pygame.K_SPACE:
                    state = STATE_PLAYING
                    bird = Bird(window_height=WINDOW_HEIGHT)
                    pipes = []
                    score = 0
                    lives = 3
                    last_pipe_time = pygame.time.get_ticks()
                    collision_cooldown = 0
                    impact_timer = 0
                    impact_pos = None
                elif state == STATE_PLAYING and event.key == pygame.K_SPACE:
                    bird.jump()
                elif state == STATE_GAMEOVER and event.key == pygame.K_SPACE:
                    state = STATE_START
            if event.type == pygame.KEYUP:
                if state == STATE_PLAYING and event.key == pygame.K_SPACE:
                    bird.jump_release()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if state == STATE_PLAYING:
                    bird.jump()
            if event.type == pygame.MOUSEBUTTONUP:
                if state == STATE_PLAYING:
                    bird.jump_release()

        screen.fill(BG_COLOR)

        # --- Background Clouds --- (animate in START and PLAYING states; static when paused / game over)
        if state in (STATE_START, STATE_PLAYING):
            for c in clouds:
                c.update()
        # Recycle clouds
        for i, c in enumerate(list(clouds)):
            if c.off_screen():
                clouds.remove(c)
                clouds.append(Cloud.spawn_at_right(WINDOW_WIDTH, WINDOW_HEIGHT, GROUND_HEIGHT))
        # Draw clouds first (behind everything)
        for c in clouds:
            c.draw(screen)

        if state == STATE_START:
            draw_text_center(screen, 'Flappy Bird', FONT, SCORE_COLOR, WINDOW_HEIGHT // 3)
            draw_text_center(screen, 'Press SPACE to start', SMALL_FONT, SCORE_COLOR, WINDOW_HEIGHT // 2)
        elif state == STATE_PLAYING:
            # Pipes
            now = pygame.time.get_ticks()
            if now - last_pipe_time > PIPE_INTERVAL:
                pipes.append(Pipe(WINDOW_WIDTH, gap=PIPE_GAP, width=PIPE_WIDTH, speed=PIPE_SPEED,
                                  window_height=WINDOW_HEIGHT, ground_height=GROUND_HEIGHT))
                last_pipe_time = now
            for pipe in pipes:
                pipe.update()
                pipe.draw(screen)
            pipes = [p for p in pipes if not p.off_screen()]

            # Bird
            bird.update()
            bird.draw(screen)

            # Ground
            ground.draw(screen)

            # Collision (with lives)
            hit = False
            if collision_cooldown == 0:
                for pipe in pipes:
                    if pipe.collide(bird.rect):
                        hit = True
                        # Approx impact center: clamp bird center inside pipe rect bounds
                        cx = bird.rect.centerx
                        if bird.rect.centery < pipe.top_rect.bottom:
                            cy = pipe.top_rect.bottom
                        elif bird.rect.centery > pipe.bottom_rect.top:
                            cy = pipe.bottom_rect.top
                        else:
                            cy = bird.rect.centery
                        impact_pos = (cx, cy)
                if ground.collide(bird.rect) or bird.rect.top < 0:
                    hit = True
                    # Ground or ceiling impact
                    cx = bird.rect.centerx
                    cy = bird.rect.bottom if bird.rect.top >= 0 else bird.rect.top
                    impact_pos = (cx, cy)
                if hit:
                    if not god_mode:
                        lives -= 1
                        collision_cooldown = FPS  # 1 second forgiveness
                        impact_timer = int(FPS * 0.6)  # show ~0.6s
                        if lives <= 0:
                            state = STATE_GAMEOVER
                        else:
                            # Reset bird position and velocity, but keep score and pipes
                            bird = Bird(window_height=WINDOW_HEIGHT)
                    else:
                        # In god mode: just brief impact flash
                        impact_timer = int(FPS * 0.3)
            else:
                collision_cooldown = max(0, collision_cooldown - 1)

            # Decrement impact timer every frame (independent of cooldown)
            if impact_timer > 0:
                impact_timer -= 1
                if impact_timer == 0:
                    impact_pos = None

            # Score
            for pipe in pipes:
                if not pipe.passed and pipe.top_rect.right < bird.x:
                    score += 1
                    pipe.passed = True
            draw_text_center(screen, str(score), FONT, SCORE_COLOR, 50)
            # Draw lives at top left
            lives_text = SMALL_FONT.render(f'Lives: {lives}', True, SCORE_COLOR)
            screen.blit(lives_text, (10, 10))
            if god_mode:
                gm_text = SMALL_FONT.render('GOD', True, (255, 215, 0))
                screen.blit(gm_text, (WINDOW_WIDTH - gm_text.get_width() - 10, 10))
        elif state == STATE_PAUSED:
            # Draw current scene without updating positions
            for pipe in pipes:
                pipe.draw(screen)
            bird.draw(screen)
            ground.draw(screen)
            draw_text_center(screen, str(score), FONT, SCORE_COLOR, 50)
            lives_text = SMALL_FONT.render(f'Lives: {lives}', True, SCORE_COLOR)
            screen.blit(lives_text, (10, 10))
            if god_mode:
                gm_text = SMALL_FONT.render('GOD', True, (255, 215, 0))
                screen.blit(gm_text, (WINDOW_WIDTH - gm_text.get_width() - 10, 10))
            draw_text_center(screen, 'Paused', FONT, SCORE_COLOR, WINDOW_HEIGHT // 2 - 20)
            draw_text_center(screen, 'Press P to resume', SMALL_FONT, SCORE_COLOR, WINDOW_HEIGHT // 2 + 30)
        elif state == STATE_GAMEOVER:
            for pipe in pipes:
                pipe.draw(screen)
            bird.draw(screen)
            ground.draw(screen)
            draw_text_center(screen, 'Game Over', FONT, SCORE_COLOR, WINDOW_HEIGHT // 3)
            draw_text_center(screen, f'Score: {score}', SMALL_FONT, SCORE_COLOR, WINDOW_HEIGHT // 2)
            draw_text_center(screen, 'Press SPACE to restart', SMALL_FONT, SCORE_COLOR, WINDOW_HEIGHT // 2 + 40)
            if god_mode:
                gm_text = SMALL_FONT.render('GOD', True, (255, 215, 0))
                screen.blit(gm_text, (WINDOW_WIDTH - gm_text.get_width() - 10, 10))

        # Draw impact indicator (flashing) in PLAYING or GAMEOVER (frozen during pause)
        if impact_timer > 0 and impact_pos and state in (STATE_PLAYING, STATE_GAMEOVER, STATE_PAUSED):
            # Flash every 6 frames
            if (impact_timer // 6) % 2 == 0:
                draw_cross(screen, impact_pos[0], impact_pos[1], size=26)

        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
