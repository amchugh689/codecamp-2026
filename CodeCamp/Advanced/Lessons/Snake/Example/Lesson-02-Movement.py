import os
import pygame

os.environ["SDL_AUDIODRIVER"] = "dsp"

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

CELL_SIZE = 20

snake_list = [[100, 100], [80, 100], [60, 100]]
dx, dy = 1, 0
next_dx, next_dy = dx, dy

move_timer = 0
MOVE_INTERVAL = 8

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                next_dx, next_dy = 0, -1
            elif event.key == pygame.K_DOWN and dy == 0:
                next_dx, next_dy = 0, 1
            elif event.key == pygame.K_LEFT and dx == 0:
                next_dx, next_dy = -1, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                next_dx, next_dy = 1, 0

    move_timer += 1
    if move_timer >= MOVE_INTERVAL:
        move_timer = 0
        dx, dy = next_dx, next_dy
        head = snake_list[0]
        new_head = [head[0] + dx * CELL_SIZE, head[1] + dy * CELL_SIZE]
        snake_list.insert(0, new_head)
        snake_list.pop()

    window.fill(BLACK)

    for segment in snake_list:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
