# Lesson 1 Task – Getting Started

Builds on: [Lesson 1 – Getting Started](../Lesson/Lesson-01-Getting-Started.md)

## What You'll Build

A game window with a running game loop, showing a bird sitting still on screen.

## Task 1: Open a Window

Open the Exercise for this lesson. `main.py` starts empty; add:

```python
import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (230, 200, 0)
GREEN = (0, 180, 0)

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

## Task 2: Draw the Bird

Add these constants above the game loop:

```python
BIRD_SIZE = 20
bird_x = 100
bird_y = WINDOW_HEIGHT // 2
```

Then draw it inside the loop, between `window.fill(BLACK)` and `pygame.display.update()`:

```python
    pygame.draw.rect(window, YELLOW, (bird_x, bird_y, BIRD_SIZE, BIRD_SIZE))
```

Run it. You should see a small yellow square sitting still, roughly a sixth of the way across the window and centred vertically.

Try changing `bird_x` and re-running to see it sit at a different horizontal position; then change it back to `100`. As the concepts page explained, this value won't need to change again once the game is running, only `bird_y` will.

## Self-Check

- [ ] A window opens and stays open until closed
- [ ] A yellow square appears near the left side of the window
- [ ] I understand why `bird_x` stays fixed while `bird_y` is the one that will change later

---

[← Back to Lesson 1 Concepts](../Lesson/Lesson-01-Getting-Started.md) | [→ Continue to Lesson 2: Gravity & Flapping](../Lesson/Lesson-02-Gravity-and-Flapping.md)
