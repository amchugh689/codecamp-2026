# Lesson 2 Task – Movement

Builds on: [Lesson 2 – Movement](../Lesson/Lesson-02-Movement.md)

## What You'll Build

A snake that moves on its own, one grid cell at a time, and turns with the arrow keys, without being able to reverse directly into itself.

## Task 1: Move the Snake

Add these near your `snake_list`:

```python
dx, dy = 1, 0

move_timer = 0
MOVE_INTERVAL = 8
```

The snake starts moving right (`dx = 1, dy = 0`). `MOVE_INTERVAL` is how many frames pass between each step, per the concepts page.

Add this inside the game loop, after the event `for` loop but before `window.fill(BLACK)`:

```python
    move_timer += 1
    if move_timer >= MOVE_INTERVAL:
        move_timer = 0
        head = snake_list[0]
        new_head = [head[0] + dx * CELL_SIZE, head[1] + dy * CELL_SIZE]
        snake_list.insert(0, new_head)
        snake_list.pop()
```

Run it. The snake should glide steadily to the right, one cell at a time, at a readable speed rather than instantly.

Try changing `MOVE_INTERVAL` to `2` and then to `20`, re-running each time, to see how it controls speed.

## Task 2: Turn with the Arrow Keys

Add this inside your event `for` loop, where you check for `pygame.QUIT`:

```python
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, 1
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -1, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = 1, 0
```

Each direction only takes effect if the *other* axis is currently zero, exactly the reversal-prevention rule from the concepts page.

Run it. Steer the snake around with the arrow keys. Try pressing the key for the direction directly behind you (Left, while moving right) and confirm nothing happens, then try turning up or down instead.

## Self-Check

- [ ] The snake moves on its own, one cell at a time, at a steady readable pace
- [ ] The arrow keys change direction
- [ ] Pressing the direction directly behind the snake's current movement does nothing
- [ ] Changing `MOVE_INTERVAL` makes the snake visibly faster or slower

---

[← Back to Lesson 2 Concepts](../Lesson/Lesson-02-Movement.md) | [→ Continue to Lesson 3: Food, Eating & Losing](../Lesson/Lesson-03-Food-Eating-Losing.md)
