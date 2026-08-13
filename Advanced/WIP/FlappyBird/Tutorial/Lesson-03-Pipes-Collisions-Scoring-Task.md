# Lesson 3 Task – Pipes, Collisions & Scoring

Builds on: [Lesson 3 – Pipes, Collisions & Scoring](../Lesson/Lesson-03-Pipes-Collisions-Scoring.md)

## What You'll Build

Pipes that scroll in from the right with a gap to fly through, collision detection against them, and a score that goes up each time you pass one.

Everything in this lesson's gameplay code goes **inside the `if not game_over:` block** you created in Lesson 2, alongside your gravity and boundary-check code, not outside it. Drawing code stays outside that block, as before.

## Task 1: Spawn and Scroll Pipes

Add these constants near your bird constants:

```python
import random

PIPE_WIDTH = 50
GAP_HEIGHT = 120
PIPE_SPEED = 3
SPAWN_INTERVAL = 90
spawn_timer = 0
pipes = []
```

`import random` needs to go at the very top of your file, with your other imports.

Add this inside your `if not game_over:` block, after the boundary-check code from Lesson 2:

```python
        spawn_timer += 1
        if spawn_timer >= SPAWN_INTERVAL:
            spawn_timer = 0
            gap_y = random.randint(40, WINDOW_HEIGHT - 40 - GAP_HEIGHT)
            pipes.append([WINDOW_WIDTH, gap_y, False])

        for pipe in pipes:
            pipe[0] -= PIPE_SPEED
        pipes = [p for p in pipes if p[0] > -PIPE_WIDTH]
```

Each pipe is `[x, gap_y, scored]`, matching the concepts page: a horizontal position, where its gap starts vertically, and whether it's already been counted for scoring.

## Task 2: Draw the Pipes

Add this with your other drawing code, alongside where you draw the bird:

```python
    for pipe in pipes:
        pipe_x, gap_y, scored = pipe
        pygame.draw.rect(window, GREEN, (pipe_x, 0, PIPE_WIDTH, gap_y))
        pygame.draw.rect(window, GREEN, (pipe_x, gap_y + GAP_HEIGHT, PIPE_WIDTH, WINDOW_HEIGHT - (gap_y + GAP_HEIGHT)))
```

Run it. You should see green pipes scrolling in from the right, each with a gap, while the bird falls and flaps as before.

## Task 3: Collisions and Scoring

Add the score variable near your other setup code, outside the loop:

```python
score = 0
```

Add this inside your `if not game_over:` block, after the pipe-scrolling code from Task 1:

```python
        bird_rect = pygame.Rect(bird_x, bird_y, BIRD_SIZE, BIRD_SIZE)
        for pipe in pipes:
            pipe_x, gap_y, scored = pipe
            top_rect = pygame.Rect(pipe_x, 0, PIPE_WIDTH, gap_y)
            bottom_rect = pygame.Rect(pipe_x, gap_y + GAP_HEIGHT, PIPE_WIDTH, WINDOW_HEIGHT - (gap_y + GAP_HEIGHT))
            if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
                game_over = True

            if not scored and pipe_x + PIPE_WIDTH < bird_x:
                pipe[2] = True
                score += 1
```

This checks the bird against both rectangles built from each pipe's gap, matching the concepts page. The `not scored` check is what stops a single pipe from scoring more than once, per the concepts page.

Draw the score with your other drawing code:

```python
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))
```

Run the full game. Flap through the gaps to score points; flying into a pipe (or off the top or bottom) should end the game and show "GAME OVER".

## Self-Check

- [ ] Pipes scroll in from the right at a steady pace, each with a gap
- [ ] Flying into a pipe ends the game
- [ ] Successfully flying through a gap increases your score by exactly 1, not more
- [ ] Pipes that scroll fully off the left edge disappear rather than piling up

---

[← Back to Lesson 3 Concepts](../Lesson/Lesson-03-Pipes-Collisions-Scoring.md) | [→ Continue to Lesson 4: Extension Activities](../Lesson/Lesson-04-Extension-Activities.md)
