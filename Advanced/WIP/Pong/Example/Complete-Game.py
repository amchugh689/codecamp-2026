# Finished base game (Lessons 1-3). Extensions in Lesson 4 are optional and not included here.
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
PADDLE_SPEED = 6

BALL_SIZE = 15
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_dx = 4
ball_dy = 4

font = pygame.font.SysFont(None, 36)
score = 0

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle_y > 0:
        paddle_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        paddle_y += PADDLE_SPEED

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_y <= 0 or ball_y >= WINDOW_HEIGHT - BALL_SIZE:
        ball_dy = -ball_dy

    if ball_x >= WINDOW_WIDTH - BALL_SIZE:
        ball_dx = -ball_dx

    paddle_rect = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball_rect = pygame.Rect(ball_x, ball_y, BALL_SIZE, BALL_SIZE)

    if paddle_rect.colliderect(ball_rect) and ball_dx < 0:
        ball_dx = -ball_dx
        score += 1

    if ball_x < 0:
        ball_x = WINDOW_WIDTH // 2
        ball_y = WINDOW_HEIGHT // 2
        ball_dx = 4
        ball_dy = 4
        score = 0

    window.fill(BLACK)

    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

    pygame.draw.rect(window, WHITE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(window, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
