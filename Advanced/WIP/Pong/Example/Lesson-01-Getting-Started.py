import os
import pygame

os.environ["SDL_AUDIODRIVER"] = "dsp"

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 80
paddle_x = 20
paddle_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2

BALL_SIZE = 15
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BLACK)

    pygame.draw.rect(window, WHITE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(window, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
