import os
import pygame

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

font = pygame.font.SysFont(None, 36)
game_over = False

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

    window.fill(BLACK)

    pygame.draw.rect(window, YELLOW, (bird_x, bird_y, BIRD_SIZE, BIRD_SIZE))

    if game_over:
        message_text = font.render("GAME OVER", True, WHITE)
        window.blit(message_text, (WINDOW_WIDTH // 2 - message_text.get_width() // 2, WINDOW_HEIGHT // 2))

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
