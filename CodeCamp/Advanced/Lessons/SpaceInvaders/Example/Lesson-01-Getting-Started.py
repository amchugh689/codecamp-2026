import os
import pygame

os.environ["SDL_AUDIODRIVER"] = "dsp"

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 20
player_x = WINDOW_WIDTH // 2 - PLAYER_WIDTH // 2
player_y = WINDOW_HEIGHT - 40

ENEMY_WIDTH = 40
ENEMY_HEIGHT = 30
ENEMY_ROWS = 3
ENEMY_COLS = 5
ENEMY_SPACING_X = 20
ENEMY_SPACING_Y = 20

enemies = []
for row in range(ENEMY_ROWS):
    for col in range(ENEMY_COLS):
        enemy_x = 60 + col * (ENEMY_WIDTH + ENEMY_SPACING_X)
        enemy_y = 40 + row * (ENEMY_HEIGHT + ENEMY_SPACING_Y)
        enemies.append([enemy_x, enemy_y])

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BLACK)

    pygame.draw.rect(window, GREEN, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    for enemy in enemies:
        pygame.draw.rect(window, RED, (enemy[0], enemy[1], ENEMY_WIDTH, ENEMY_HEIGHT))

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
