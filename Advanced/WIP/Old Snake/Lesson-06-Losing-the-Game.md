# Lesson 6 – Losing the Game

## Learning Objectives

By the end of this lesson, you will be able to:

- Detect when the snake hits a wall (boundary collision)
- Detect when the snake hits itself (self-collision)
- Display a Game Over screen with the final score
- Restart the game when the player presses a key
- Manage game states (playing vs. game over)

---

## New Concepts

### Wall Collision

The snake should not be able to leave the screen. When the head moves past any edge, the game is over.

```
Wall collision conditions:
┌────────────────────────────────┐
│         x < 0 (left wall)      │
│         x >= 600 (right wall)  │
│         y < 0 (top wall)       │
│         y >= 400 (bottom wall) │
└────────────────────────────────┘
```

We check the head's position after it moves. If x or y is outside the window, the snake has hit a wall.

```python
head = snake_list[0]
if head[0] < 0 or head[0] >= WINDOW_WIDTH:
    # Hit left or right wall
if head[1] < 0 or head[1] >= WINDOW_HEIGHT:
    # Hit top or bottom wall
```

**Why `>=` instead of `>`?** Because positions go from 0 to 580 (for x). A position of 600 means the square would start at the right edge and extend beyond it — so 600 is already off-screen.

### Self-Collision

As the snake grows longer, it can crash into its own body. Self-collision happens when the head's position matches any body segment's position.

```
Self-collision example:
    ■ ■ ■ ■
    ■       ■
    ■   ←── ■  ← Head turns into body!
    ■ ■ ■ ■
```

We check if the head's position exists anywhere else in the snake list:

```python
if snake_list[0] in snake_list[1:]:
    # Head is on top of a body segment!
```

`snake_list[1:]` is "everything except the head" (because the head is always at index 0, and we don't want to compare the head to itself).

### Game States

Our game now has two states:
1. **Playing** — snake moves, food spawns, score increases
2. **Game Over** — game is frozen, message displayed, waiting for restart

We use a simple variable to track which state we're in:

```python
game_over = False
```

When `game_over` is `True`, we stop updating the snake and show the Game Over screen. When the player presses a key, we reset everything and start again.

### Restarting the Game

To restart, we reset all game variables to their starting values:
- Snake goes back to its starting position and length
- Direction resets to "RIGHT"
- Score resets to 0
- New food is spawned
- `game_over` becomes `False`

---

## Step-by-Step Instructions

### Step 1: Add the Game Over Variable

Before the game loop, add:

```python
# Game state
game_over = False
```

### Step 2: Add Collision Detection

In the game loop, after moving the snake (after the eating/pop logic), add collision checks:

```python
    # Check for wall collision
    head = snake_list[0]
    if head[0] < 0 or head[0] >= WINDOW_WIDTH:
        game_over = True
    if head[1] < 0 or head[1] >= WINDOW_HEIGHT:
        game_over = True

    # Check for self-collision
    if head in snake_list[1:]:
        game_over = True
```

### Step 3: Only Update When Not Game Over

Wrap the movement and collision code so it only runs when `game_over` is `False`. The structure becomes:

```python
    if not game_over:
        # Movement code
        # Eating code
        # Collision checks
    else:
        # Game Over screen (Step 4)
```

### Step 4: Display Game Over Screen

In the `else` block (when game is over), draw the Game Over message:

```python
    else:
        # Game Over screen
        game_over_text = font.render("GAME OVER", True, RED)
        score_final = font.render("Final Score: " + str(score), True, WHITE)
        restart_text = font.render("Press R to Restart", True, WHITE)

        # Centre the text on screen
        window.fill(BLACK)
        window.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, 120))
        window.blit(score_final, (WINDOW_WIDTH // 2 - score_final.get_width() // 2, 180))
        window.blit(restart_text, (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, 240))
        pygame.display.update()
```

### Step 5: Handle Restart Input

In the event loop, add a check for the R key when the game is over:

```python
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                # Reset everything
                snake_list = [[100, 100], [80, 100], [60, 100]]
                direction = "RIGHT"
                score = 0
                food_position = spawn_food()
                game_over = False
```

### Step 6: Run and Test

Click **▶ Run**. Test these scenarios:
1. Move the snake into a wall — you should see "GAME OVER"
2. Press R — the game should restart
3. Grow the snake long enough to crash into yourself — Game Over should trigger

---

## Complete Code

```python
import pygame
import random

# Initialize PyGame
pygame.init()

# Game window settings
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# Grid settings
CELL_SIZE = 20

# Colours (Red, Green, Blue)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Game timing
clock = pygame.time.Clock()
GAME_SPEED = 10

# Font for text display
font = pygame.font.SysFont(None, 35)


def spawn_food():
    x = random.randint(0, (WINDOW_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    y = random.randint(0, (WINDOW_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    return [x, y]


# Snake starting position
snake_list = [[100, 100], [80, 100], [60, 100]]

# Movement
direction = "RIGHT"

# Food
food_position = spawn_food()

# Score
score = 0

# Game state
game_over = False

# Game loop
running = True
while running:
    clock.tick(GAME_SPEED)

    # 1. Check for input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                # Reset everything
                snake_list = [[100, 100], [80, 100], [60, 100]]
                direction = "RIGHT"
                score = 0
                food_position = spawn_food()
                game_over = False
            elif not game_over:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

    if not game_over:
        # 2. Update game state - move the snake
        head = snake_list[0]
        if direction == "RIGHT":
            new_head = [head[0] + CELL_SIZE, head[1]]
        elif direction == "LEFT":
            new_head = [head[0] - CELL_SIZE, head[1]]
        elif direction == "UP":
            new_head = [head[0], head[1] - CELL_SIZE]
        elif direction == "DOWN":
            new_head = [head[0], head[1] + CELL_SIZE]

        snake_list.insert(0, new_head)

        # Check if snake ate the food
        if snake_list[0] == food_position:
            score = score + 1
            food_position = spawn_food()
        else:
            snake_list.pop()

        # Check for wall collision
        head = snake_list[0]
        if head[0] < 0 or head[0] >= WINDOW_WIDTH:
            game_over = True
        if head[1] < 0 or head[1] >= WINDOW_HEIGHT:
            game_over = True

        # Check for self-collision
        if head in snake_list[1:]:
            game_over = True

        # 3. Draw everything
        window.fill(BLACK)

        # Draw the snake
        for segment in snake_list:
            pygame.draw.rect(window, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

        # Draw the food
        pygame.draw.rect(window, RED, (food_position[0], food_position[1], CELL_SIZE, CELL_SIZE))

        # Draw the score
        score_text = font.render("Score: " + str(score), True, WHITE)
        window.blit(score_text, (10, 10))

        pygame.display.update()

    else:
        # Game Over screen
        window.fill(BLACK)

        game_over_text = font.render("GAME OVER", True, RED)
        score_final = font.render("Final Score: " + str(score), True, WHITE)
        restart_text = font.render("Press R to Restart", True, WHITE)

        # Centre text on screen
        window.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, 120))
        window.blit(score_final, (WINDOW_WIDTH // 2 - score_final.get_width() // 2, 180))
        window.blit(restart_text, (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, 240))

        pygame.display.update()

# Quit PyGame
pygame.quit()
```

---

## Code Walkthrough

### `game_over = False`
A boolean flag that tracks the game state. `False` = playing, `True` = game over.

### Restructured Event Handling

```python
if event.type == pygame.KEYDOWN:
    if game_over and event.key == pygame.K_r:
        # Restart logic
    elif not game_over:
        # Direction change logic
```

We now check **which state we're in** before processing key presses:
- If game is over: only the R key does anything (restart)
- If game is active: arrow keys change direction (as before)

### `if not game_over:` Block
All movement, eating, collision checking, and normal drawing is wrapped inside this condition. When the game is over, none of this code runs — the snake stops moving.

### Wall Collision

```python
head = snake_list[0]
if head[0] < 0 or head[0] >= WINDOW_WIDTH:
    game_over = True
if head[1] < 0 or head[1] >= WINDOW_HEIGHT:
    game_over = True
```

Four possible wall hits:
| Condition | Meaning |
|-----------|---------|
| `head[0] < 0` | Head went past the left edge |
| `head[0] >= WINDOW_WIDTH` | Head went past the right edge |
| `head[1] < 0` | Head went past the top edge |
| `head[1] >= WINDOW_HEIGHT` | Head went past the bottom edge |

### Self-Collision

```python
if head in snake_list[1:]:
    game_over = True
```

- `snake_list[1:]` is a slice containing everything except index 0 (the head)
- `head in snake_list[1:]` checks: "Is the head's `[x, y]` position found anywhere in the body?"
- If yes, the snake ran into itself

**Why `[1:]` and not the full list?** Because `snake_list[0]` IS the head — it would always match itself!

### Centering Text

```python
window.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, 120))
```

To centre text horizontally:
1. `WINDOW_WIDTH // 2` = centre of the screen (300)
2. `game_over_text.get_width() // 2` = half the text's width
3. Subtracting half the text width from the centre gives the starting x position

### Restart Logic

```python
snake_list = [[100, 100], [80, 100], [60, 100]]
direction = "RIGHT"
score = 0
food_position = spawn_food()
game_over = False
```

We reset every game variable to its original value. The game loop continues running — it was never stopped — so the game immediately resumes.

---

## Expected Output

### During Gameplay
Same as before — snake moves, eats food, score updates.

### When Snake Hits a Wall or Itself

```
┌────────────────────────────────────────────────┐
│                                                │
│                                                │
│                                                │
│              GAME OVER                         │
│                                                │
│           Final Score: 7                       │
│                                                │
│         Press R to Restart                     │
│                                                │
│                                                │
└────────────────────────────────────────────────┘
```

### After Pressing R
The game restarts — snake is back to 3 segments at the starting position, score is 0, new food appears.

---

## Common Mistakes

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Checking collision before moving | Collision detected at old position | Check after `insert(0, new_head)` |
| Using `snake_list` instead of `snake_list[1:]` | Game Over triggers immediately (head matches itself) | Always use `[1:]` for self-collision |
| Forgetting to reset `game_over = False` on restart | Game stays frozen after pressing R | Include `game_over = False` in reset |
| Not wrapping movement in `if not game_over:` | Snake keeps moving during Game Over | Wrap ALL game logic in the condition |
| Drawing during game over AND during play without separate logic | Mixed/overlapping screens | Use if/else for the two states |
| Using `>` instead of `>=` for right/bottom walls | Snake goes 1 cell off-screen before dying | Use `>=` for right and bottom edges |

---

## Debugging Tips

1. **Game Over triggers immediately on start**: Check your starting position — make sure the snake doesn't start outside the window or overlapping itself.
2. **Can't restart**: Make sure the R key check comes BEFORE the direction change checks, and that it checks `if game_over`.
3. **Self-collision doesn't work**: The snake needs to be at least 5 segments long to collide with itself (it takes 4 turns to create a loop). Grow it by eating food first.
4. **Wall collision doesn't trigger**: Add `print(head)` before the collision checks to see the head position. It should go past 0 or past 580/380.
5. **Quick test**: Temporarily set `snake_list = [[580, 100], [560, 100], [540, 100]]` with direction `"RIGHT"`. The snake should hit the right wall in 1 frame.

---

## Review Questions

1. Why do we check `head[0] >= WINDOW_WIDTH` instead of `head[0] > WINDOW_WIDTH`?
2. What does `snake_list[1:]` mean, and why don't we use `snake_list` for self-collision?
3. What is the purpose of the `game_over` variable? Why not just use `running = False`?
4. List all the variables that need to be reset when the game restarts.
5. Could the snake collide with itself if it has only 3 segments? Why or why not?

---

## Practice Exercises

### Exercise 1: Different Restart Key
Change the restart key from R to **Space** (`pygame.K_SPACE`). Test it works.

### Exercise 2: Death Message
Change the Game Over screen to show different messages based on how the player died:
- "You hit a wall!" for wall collision
- "You hit yourself!" for self-collision

Hint: Create a `death_reason` variable and set it to different strings depending on which collision triggered.

### Exercise 3: Confirm Before Restart
Instead of immediately restarting when R is pressed, first show "Press R again to confirm restart" after the first R press. Only restart on the second R press.

Hint: Add a `restart_confirm` variable.

---

## Extension Challenge

Add a **death animation**: When the snake dies, don't immediately show Game Over. Instead, flash the snake red 3 times before showing the Game Over screen.

Hint approach:
1. When collision is detected, set `death_animation = True` and `flash_count = 0`
2. Each frame during death animation, alternate the snake colour between RED and GREEN
3. After 6 frames (3 full flashes), set `game_over = True`

---

## Teacher Notes

**Time Estimate**: 35–45 minutes

**Key Misconceptions**:
- The difference between `running` and `game_over`: `running = False` exits the entire program. `game_over = True` stops the game but keeps the program running so the player can restart. Students may confuse these.
- Self-collision with a short snake: Students may test self-collision immediately and think it is broken because the 3-segment snake can't reach itself. Explain that they need to grow first.
- The `>=` vs `>` boundary check trips up students who think "the window is 600 wide so anything above 600 is out." Remind them that position 600 means the left edge of the square is at 600, which is already past the right side of the window.

**Assessment Checklist**:
- [ ] Wall collision works on all four sides
- [ ] Self-collision works when the snake is long enough
- [ ] Game Over screen displays with final score
- [ ] Game restarts correctly when R is pressed
- [ ] All variables are properly reset on restart
- [ ] Arrow keys don't work during Game Over
- [ ] Student can explain the difference between `game_over` and `running`

**Milestone**: At this point, students have a **fully playable game**! Take a moment to celebrate — the core game is complete. Lessons 7 and 8 add polish and extensions.

---

## What's Next?

Congratulations — you have a **complete, playable Snake game**! 🎉

But there is room to make it better. In **Lesson 7**, we will clean up the code, add a pause feature, make the game speed up as you score, and improve the visual style.

[← Back to Lesson 5](Lesson-05-Eating-Food.md) | [→ Continue to Lesson 7: Improving the Game](Lesson-07-Improving-the-Game.md)
