# Lesson 2 Task – Paddle Movement

Builds on: [Lesson 2 – Paddle Movement](../Lesson/Lesson-02-Paddle-Movement.md)

## What You'll Build

A paddle that moves up and down with the keyboard, and stays inside the window.

## Task: Move the Paddle

Add a speed constant near your other paddle constants:

```python
PADDLE_SPEED = 6
```

Then, inside the game loop, after the event `for` loop but before `window.fill(BLACK)`, add:

```python
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle_y > 0:
        paddle_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        paddle_y += PADDLE_SPEED
```

Run it. Holding Up or Down should smoothly move the paddle, and it should stop exactly at the top and bottom edges instead of sliding off screen.

The `and` conditions are what stop the paddle at the edges: that's the boundary check from the concepts page. Try temporarily removing one and see what happens, then put it back.

## Self-Check

- [ ] Holding Up moves the paddle up; holding Down moves it down
- [ ] The paddle stops at the top and bottom of the window instead of disappearing off the edge
- [ ] Changing `PADDLE_SPEED` makes the paddle feel faster or slower

---

[← Back to Lesson 2 Concepts](../Lesson/Lesson-02-Paddle-Movement.md) | [→ Continue to Lesson 3: Ball, Bouncing & Scoring](../Lesson/Lesson-03-Ball-Bouncing-Scoring.md)
