## What You'll Build

A game window with a running game loop, showing a player ship and a grid of enemies, all sitting still on screen.

## Task 1: Open a Window

Open the Exercise for this lesson. `main.py` starts empty; add:

```python
import pygame
import os

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

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BLACK)
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
```

Run it. You should see a black 600x400 window that stays open until you close it.

## Task 2: Draw the Player Ship

Add these constants above the game loop:

```python
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 20
player_x = WINDOW_WIDTH // 2 - PLAYER_WIDTH // 2
player_y = WINDOW_HEIGHT - 40
```

Then draw it inside the loop, between `window.fill(BLACK)` and `pygame.display.update()`:

```python
    pygame.draw.rect(window, GREEN, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))
```

Run it. You should see a green rectangle near the bottom-centre of the window.

## Task 3: Build and Draw the Enemy Grid

Add these constants near your other setup code:

```python
ENEMY_WIDTH = 40
ENEMY_HEIGHT = 30
ENEMY_ROWS = 3
ENEMY_COLS = 5
ENEMY_SPACING_X = 20
ENEMY_SPACING_Y = 20
```

Now build the grid using the nested loop from the concepts page:

```python
enemies = []
for row in range(ENEMY_ROWS):
    for col in range(ENEMY_COLS):
        enemy_x = 60 + col * (ENEMY_WIDTH + ENEMY_SPACING_X)
        enemy_y = 40 + row * (ENEMY_HEIGHT + ENEMY_SPACING_Y)
        enemies.append([enemy_x, enemy_y])
```

Each entry in `enemies` is an `[x, y]` position, the same kind of list you'll use for bullets in the next lesson.

Draw every enemy in the loop, alongside your player:

```python
    for enemy in enemies:
        pygame.draw.rect(window, RED, (enemy[0], enemy[1], ENEMY_WIDTH, ENEMY_HEIGHT))
```

Run it. You should see 3 rows of 5 red rectangles arranged in a grid above your green ship.

Try changing `ENEMY_ROWS` or `ENEMY_COLS` and re-running to see the grid resize.

## Self-Check

- A window opens and stays open until closed
- A green ship rectangle appears near the bottom-centre
- A grid of red enemy rectangles appears, arranged in rows and columns
- Changing `ENEMY_ROWS` or `ENEMY_COLS` changes the size of the grid
