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

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BLACK)

    pygame.draw.rect(window, YELLOW, (bird_x, bird_y, BIRD_SIZE, BIRD_SIZE))

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
