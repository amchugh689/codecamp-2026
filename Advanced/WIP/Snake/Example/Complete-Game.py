# Finished base game (Lessons 1-3). Extensions in Lesson 4 are optional and not included here.
import os
import pygame
import random

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
GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

snake_list = [[100, 100], [80, 100], [60, 100]]
dx, dy = 1, 0
next_dx, next_dy = dx, dy

move_timer = 0
MOVE_INTERVAL = 8


def spawn_food():
    food_x = random.randint(0, GRID_WIDTH - 1) * CELL_SIZE
    food_y = random.randint(0, GRID_HEIGHT - 1) * CELL_SIZE
    return [food_x, food_y]


food_position = spawn_food()

font = pygame.font.SysFont(None, 36)
score = 0
game_over = False

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_UP and dy == 0:
                next_dx, next_dy = 0, -1
            elif event.key == pygame.K_DOWN and dy == 0:
                next_dx, next_dy = 0, 1
            elif event.key == pygame.K_LEFT and dx == 0:
                next_dx, next_dy = -1, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                next_dx, next_dy = 1, 0

    if not game_over:
        move_timer += 1
        if move_timer >= MOVE_INTERVAL:
            move_timer = 0
            dx, dy = next_dx, next_dy
            head = snake_list[0]
            new_head = [head[0] + dx * CELL_SIZE, head[1] + dy * CELL_SIZE]

            if new_head[0] < 0 or new_head[0] >= WINDOW_WIDTH or new_head[1] < 0 or new_head[1] >= WINDOW_HEIGHT:
                game_over = True
            else:
                is_eating = new_head == food_position
                body_to_check = snake_list if is_eating else snake_list[:-1]
                if new_head in body_to_check:
                    game_over = True
                else:
                    snake_list.insert(0, new_head)
                    if is_eating:
                        score += 1
                        food_position = spawn_food()
                    else:
                        snake_list.pop()

    window.fill(BLACK)

    for segment in snake_list:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(window, RED, (food_position[0], food_position[1], CELL_SIZE, CELL_SIZE))

    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

    if game_over:
        message_text = font.render("GAME OVER", True, WHITE)
        window.blit(message_text, (WINDOW_WIDTH // 2 - message_text.get_width() // 2, WINDOW_HEIGHT // 2))

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
