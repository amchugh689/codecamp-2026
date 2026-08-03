# Lesson 1 Task – Getting Started

Builds on: [Lesson 1 – Getting Started](../Lesson/Lesson-01-Getting-Started.md)

## What You'll Build

A game window with a running game loop, showing a paddle and a ball sitting still on screen.

## Task 1: Open a Window

In your Pygame sandbox, clear `main.py` and add:

```python
import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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

Run it. You should see a black 600×400 window that stays open until you close it.

`clock.tick(FPS)` is what caps the loop at 60 times per second. `pygame.QUIT` is the event fired when you click the window's close button.

## Task 2: Draw a Paddle and Ball

Add these constants above the game loop:

```python
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 80
paddle_x = 20
paddle_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2

BALL_SIZE = 15
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
```

Then draw both inside the loop, between `window.fill(BLACK)` and `pygame.display.update()`:

```python
    pygame.draw.rect(window, WHITE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(window, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
```

Run it. You should see a white paddle near the left edge and a white ball near the centre of the screen, both sitting still.

Try changing `PADDLE_HEIGHT` or `BALL_SIZE` and re-running: you should see their size on screen change to match.

## Self-Check

- [ ] A window opens and stays open until closed
- [ ] A paddle-shaped rectangle appears near the left edge
- [ ] A round ball appears near the centre
- [ ] Changing `PADDLE_HEIGHT` or `BALL_SIZE` changes their on-screen size

---

[← Back to Lesson 1 Concepts](../Lesson/Lesson-01-Getting-Started.md) | [→ Continue to Lesson 2: Paddle Movement](../Lesson/Lesson-02-Paddle-Movement.md)
