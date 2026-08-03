# Lesson 1 Task – Getting Started

Builds on: [Lesson 1 – Getting Started](../Lesson/Lesson-01-Getting-Started.md)

## What You'll Build

A game window with a running game loop, showing a 3-segment snake sitting still on a grid.

## Task 1: Open a Window

In your Pygame sandbox, clear `main.py` and add:

```python
import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")

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

## Task 2: Set Up the Grid

Add this constant above the game loop:

```python
CELL_SIZE = 20
```

Every segment of the snake, and later the food, will be a 20x20 pixel square snapped to this grid, as described in the concepts page.

## Task 3: Draw the Snake

Add the snake's starting position:

```python
snake_list = [[100, 100], [80, 100], [60, 100]]
```

This is a snake with 3 segments: a head at `(100, 100)`, and two body segments trailing to its left, each one cell apart.

Draw every segment. Add this inside the loop, between `window.fill(BLACK)` and `pygame.display.update()`:

```python
    for segment in snake_list:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
```

Run it. You should see 3 green squares in a horizontal line, sitting still.

Try changing one of the coordinates in `snake_list` to something that isn't a multiple of 20 (like `105`) and re-running. The square still draws, just no longer aligned to the grid, which is why every position your code generates from now on will always be a multiple of `CELL_SIZE`.

## Self-Check

- [ ] A window opens and stays open until closed
- [ ] 3 green squares appear in a horizontal line
- [ ] I can explain why the squares are spaced exactly 20 pixels apart

---

[← Back to Lesson 1 Concepts](../Lesson/Lesson-01-Getting-Started.md) | [→ Continue to Lesson 2: Movement](../Lesson/Lesson-02-Movement.md)
