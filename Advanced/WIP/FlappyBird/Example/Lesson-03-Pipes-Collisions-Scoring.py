import os
import pygame
import random

os.environ["SDL_AUDIODRIVER"] = "dsp"

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (230, 200, 0)
GREEN = (0, 180, 0)

BIRD_SIZE = 20
bird_x = 100
bird_y = WINDOW_HEIGHT // 2
bird_velocity_y = 0
GRAVITY = 0.5
FLAP_STRENGTH = -8

PIPE_WIDTH = 50
GAP_HEIGHT = 120
PIPE_SPEED = 3
SPAWN_INTERVAL = 90
spawn_timer = 0
pipes = []

font = pygame.font.SysFont(None, 36)
game_over = False
score = 0

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_over:
            bird_velocity_y = FLAP_STRENGTH

    if not game_over:
        bird_velocity_y += GRAVITY
        bird_y += bird_velocity_y

        if bird_y <= 0 or bird_y >= WINDOW_HEIGHT - BIRD_SIZE:
            game_over = True

        spawn_timer += 1
        if spawn_timer >= SPAWN_INTERVAL:
            spawn_timer = 0
            gap_y = random.randint(40, WINDOW_HEIGHT - 40 - GAP_HEIGHT)
            pipes.append([WINDOW_WIDTH, gap_y, False])

        for pipe in pipes:
            pipe[0] -= PIPE_SPEED
        pipes = [p for p in pipes if p[0] > -PIPE_WIDTH]

        bird_rect = pygame.Rect(bird_x, bird_y, BIRD_SIZE, BIRD_SIZE)
        for pipe in pipes:
            pipe_x, gap_y, scored = pipe
            top_rect = pygame.Rect(pipe_x, 0, PIPE_WIDTH, gap_y)
            bottom_rect = pygame.Rect(pipe_x, gap_y + GAP_HEIGHT, PIPE_WIDTH, WINDOW_HEIGHT - (gap_y + GAP_HEIGHT))
            if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
                game_over = True

            if not scored and pipe_x + PIPE_WIDTH < bird_x:
                pipe[2] = True
                score += 1

    window.fill(BLACK)

    pygame.draw.rect(window, YELLOW, (bird_x, bird_y, BIRD_SIZE, BIRD_SIZE))

    for pipe in pipes:
        pipe_x, gap_y, scored = pipe
        pygame.draw.rect(window, GREEN, (pipe_x, 0, PIPE_WIDTH, gap_y))
        pygame.draw.rect(window, GREEN, (pipe_x, gap_y + GAP_HEIGHT, PIPE_WIDTH, WINDOW_HEIGHT - (gap_y + GAP_HEIGHT)))

    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

    if game_over:
        message_text = font.render("GAME OVER", True, WHITE)
        window.blit(message_text, (WINDOW_WIDTH // 2 - message_text.get_width() // 2, WINDOW_HEIGHT // 2))

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
