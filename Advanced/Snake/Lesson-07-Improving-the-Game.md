# Lesson 7 – Improving the Game

## Learning Objectives

By the end of this lesson, you will be able to:

- Organise code into functions for readability and reuse
- Use colour constants effectively for visual polish
- Implement a pause feature
- Make the game speed increase as the score grows
- Draw a distinct snake head
- Prevent food from spawning on the snake

---

## New Concepts

### Refactoring with Functions

**Refactoring** means reorganising code without changing what it does. Right now, all our logic is crammed into one long game loop. By moving code into **functions**, we:

- Make the code **easier to read** (each function has a clear purpose)
- Make it **easier to fix bugs** (you know where to look)
- **Reduce repetition** (call a function instead of copying code)

Example:
```python
# Before: everything in the loop
window.fill(BLACK)
for segment in snake_list:
    pygame.draw.rect(...)
pygame.draw.rect(...)  # food
score_text = font.render(...)
window.blit(...)

# After: one clear function call
draw_everything()
```

### Pause Feature

A pause feature freezes the game when the player presses P, and resumes when they press P again. We use a boolean toggle:

```python
if event.key == pygame.K_p:
    paused = not paused  # Flip True to False, or False to True
```

When `paused` is `True`, we skip the update step (snake doesn't move) but still draw the current state.

### Dynamic Speed

To make the game harder over time, we increase the speed as the score grows:

```python
current_speed = GAME_SPEED + (score // 3)
```

This means:
- Score 0–2: speed 10
- Score 3–5: speed 11
- Score 6–8: speed 12
- And so on...

The game gradually gets faster, making it more challenging.

---

## Step-by-Step Instructions

### Step 1: Define Better Colours

Replace and expand your colour definitions:

```python
# Colours (Red, Green, Blue)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
RED = (220, 50, 50)
GREY = (40, 40, 40)
```

We now have:
- `GREEN` for the snake head (slightly adjusted)
- `DARK_GREEN` for the snake body (darker, creates contrast)
- `RED` softened slightly (less harsh on the eyes)
- `GREY` for optional grid lines

### Step 2: Add the Paused Variable

Before the game loop, add:

```python
# Game state
game_over = False
paused = False
```

### Step 3: Create Helper Functions

Before the game loop (after `spawn_food` and before variable initializations), add these functions:

```python
def draw_snake(snake):
    """Draw the snake with a distinct head colour."""
    for i, segment in enumerate(snake):
        if i == 0:
            # Head is brighter
            colour = GREEN
        else:
            # Body is darker
            colour = DARK_GREEN
        pygame.draw.rect(window, colour, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))


def draw_food(position):
    """Draw the food item."""
    pygame.draw.rect(window, RED, (position[0], position[1], CELL_SIZE, CELL_SIZE))


def draw_score(current_score):
    """Draw the score in the top-left corner."""
    score_text = font.render("Score: " + str(current_score), True, WHITE)
    window.blit(score_text, (10, 10))


def draw_pause_message():
    """Draw PAUSED text in the centre of the screen."""
    pause_text = font.render("PAUSED - Press P to Resume", True, WHITE)
    x = WINDOW_WIDTH // 2 - pause_text.get_width() // 2
    y = WINDOW_HEIGHT // 2 - pause_text.get_height() // 2
    window.blit(pause_text, (x, y))


def move_snake(snake, direction):
    """Calculate new head and move the snake. Returns the new head position."""
    head = snake[0]
    if direction == "RIGHT":
        new_head = [head[0] + CELL_SIZE, head[1]]
    elif direction == "LEFT":
        new_head = [head[0] - CELL_SIZE, head[1]]
    elif direction == "UP":
        new_head = [head[0], head[1] - CELL_SIZE]
    elif direction == "DOWN":
        new_head = [head[0], head[1] + CELL_SIZE]
    snake.insert(0, new_head)
    return new_head


def check_wall_collision(head):
    """Return True if the head is outside the window."""
    if head[0] < 0 or head[0] >= WINDOW_WIDTH:
        return True
    if head[1] < 0 or head[1] >= WINDOW_HEIGHT:
        return True
    return False


def check_self_collision(snake):
    """Return True if the head overlaps any body segment."""
    return snake[0] in snake[1:]


def spawn_food_safe(snake):
    """Spawn food that is not on the snake."""
    while True:
        position = spawn_food()
        if position not in snake:
            return position
```

### Step 4: Add Pause Key Detection

Update the event handling to include the P key:

```python
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                # Reset everything
                snake_list = [[100, 100], [80, 100], [60, 100]]
                direction = "RIGHT"
                score = 0
                food_position = spawn_food_safe(snake_list)
                game_over = False
                paused = False
            elif not game_over:
                if event.key == pygame.K_p:
                    paused = not paused
                elif not paused:
                    if event.key == pygame.K_UP and direction != "DOWN":
                        direction = "UP"
                    elif event.key == pygame.K_DOWN and direction != "UP":
                        direction = "DOWN"
                    elif event.key == pygame.K_LEFT and direction != "RIGHT":
                        direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and direction != "LEFT":
                        direction = "RIGHT"
```

### Step 5: Add Dynamic Speed

Replace the fixed `clock.tick(GAME_SPEED)` with dynamic speed:

```python
    # Dynamic speed - gets faster as score increases
    current_speed = GAME_SPEED + (score // 3)
    clock.tick(current_speed)
```

### Step 6: Restructure the Game Loop

Update the game loop to use the new functions and pause logic:

```python
    if not game_over and not paused:
        # Move the snake
        new_head = move_snake(snake_list, direction)

        # Check if snake ate the food
        if snake_list[0] == food_position:
            score = score + 1
            food_position = spawn_food_safe(snake_list)
        else:
            snake_list.pop()

        # Check collisions
        if check_wall_collision(snake_list[0]):
            game_over = True
        if check_self_collision(snake_list):
            game_over = True
```

### Step 7: Update Drawing Section

```python
    # Draw everything (always draw, even when paused)
    if not game_over:
        window.fill(BLACK)
        draw_snake(snake_list)
        draw_food(food_position)
        draw_score(score)
        if paused:
            draw_pause_message()
        pygame.display.update()
    else:
        # Game Over screen (same as Lesson 6)
        window.fill(BLACK)
        game_over_text = font.render("GAME OVER", True, RED)
        score_final = font.render("Final Score: " + str(score), True, WHITE)
        restart_text = font.render("Press R to Restart", True, WHITE)
        window.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, 120))
        window.blit(score_final, (WINDOW_WIDTH // 2 - score_final.get_width() // 2, 180))
        window.blit(restart_text, (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, 240))
        pygame.display.update()
```

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
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
RED = (220, 50, 50)

# Game timing
clock = pygame.time.Clock()
GAME_SPEED = 10

# Font for text display
font = pygame.font.SysFont(None, 35)


def spawn_food():
    """Generate a random grid-aligned position."""
    x = random.randint(0, (WINDOW_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    y = random.randint(0, (WINDOW_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    return [x, y]


def spawn_food_safe(snake):
    """Spawn food that is not on the snake."""
    while True:
        position = spawn_food()
        if position not in snake:
            return position


def draw_snake(snake):
    """Draw the snake with a distinct head colour."""
    for i, segment in enumerate(snake):
        if i == 0:
            colour = GREEN
        else:
            colour = DARK_GREEN
        pygame.draw.rect(window, colour, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))


def draw_food(position):
    """Draw the food item."""
    pygame.draw.rect(window, RED, (position[0], position[1], CELL_SIZE, CELL_SIZE))


def draw_score(current_score):
    """Draw the score in the top-left corner."""
    score_text = font.render("Score: " + str(current_score), True, WHITE)
    window.blit(score_text, (10, 10))


def draw_pause_message():
    """Draw PAUSED text in the centre of the screen."""
    pause_text = font.render("PAUSED - Press P to Resume", True, WHITE)
    x = WINDOW_WIDTH // 2 - pause_text.get_width() // 2
    y = WINDOW_HEIGHT // 2 - pause_text.get_height() // 2
    window.blit(pause_text, (x, y))


def move_snake(snake, current_direction):
    """Calculate new head and move the snake. Returns the new head position."""
    head = snake[0]
    if current_direction == "RIGHT":
        new_head = [head[0] + CELL_SIZE, head[1]]
    elif current_direction == "LEFT":
        new_head = [head[0] - CELL_SIZE, head[1]]
    elif current_direction == "UP":
        new_head = [head[0], head[1] - CELL_SIZE]
    elif current_direction == "DOWN":
        new_head = [head[0], head[1] + CELL_SIZE]
    snake.insert(0, new_head)
    return new_head


def check_wall_collision(head):
    """Return True if the head is outside the window."""
    if head[0] < 0 or head[0] >= WINDOW_WIDTH:
        return True
    if head[1] < 0 or head[1] >= WINDOW_HEIGHT:
        return True
    return False


def check_self_collision(snake):
    """Return True if the head overlaps any body segment."""
    return snake[0] in snake[1:]


# Snake starting position
snake_list = [[100, 100], [80, 100], [60, 100]]

# Movement
direction = "RIGHT"

# Food
food_position = spawn_food_safe(snake_list)

# Score
score = 0

# Game state
game_over = False
paused = False

# Game loop
running = True
while running:
    # Dynamic speed - gets faster as score increases
    current_speed = GAME_SPEED + (score // 3)
    clock.tick(current_speed)

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
                food_position = spawn_food_safe(snake_list)
                game_over = False
                paused = False
            elif not game_over:
                if event.key == pygame.K_p:
                    paused = not paused
                elif not paused:
                    if event.key == pygame.K_UP and direction != "DOWN":
                        direction = "UP"
                    elif event.key == pygame.K_DOWN and direction != "UP":
                        direction = "DOWN"
                    elif event.key == pygame.K_LEFT and direction != "RIGHT":
                        direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and direction != "LEFT":
                        direction = "RIGHT"

    # 2. Update game state
    if not game_over and not paused:
        # Move the snake
        new_head = move_snake(snake_list, direction)

        # Check if snake ate the food
        if snake_list[0] == food_position:
            score = score + 1
            food_position = spawn_food_safe(snake_list)
        else:
            snake_list.pop()

        # Check collisions
        if check_wall_collision(snake_list[0]):
            game_over = True
        if check_self_collision(snake_list):
            game_over = True

    # 3. Draw everything
    if not game_over:
        window.fill(BLACK)
        draw_snake(snake_list)
        draw_food(food_position)
        draw_score(score)
        if paused:
            draw_pause_message()
        pygame.display.update()
    else:
        # Game Over screen
        window.fill(BLACK)

        game_over_text = font.render("GAME OVER", True, RED)
        score_final = font.render("Final Score: " + str(score), True, WHITE)
        restart_text = font.render("Press R to Restart", True, WHITE)
        speed_text = font.render("Final Speed: " + str(current_speed) + " FPS", True, WHITE)

        window.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, 100))
        window.blit(score_final, (WINDOW_WIDTH // 2 - score_final.get_width() // 2, 160))
        window.blit(speed_text, (WINDOW_WIDTH // 2 - speed_text.get_width() // 2, 210))
        window.blit(restart_text, (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, 270))

        pygame.display.update()

# Quit PyGame
pygame.quit()
```

---

## Code Walkthrough

### Helper Functions

Each function has one job:

| Function | Job |
|----------|-----|
| `spawn_food()` | Generate a random grid-aligned position |
| `spawn_food_safe(snake)` | Generate food that is NOT on the snake |
| `draw_snake(snake)` | Draw all segments with head/body colours |
| `draw_food(position)` | Draw the food rectangle |
| `draw_score(score)` | Render and display the score text |
| `draw_pause_message()` | Show "PAUSED" centred on screen |
| `move_snake(snake, direction)` | Calculate and insert new head |
| `check_wall_collision(head)` | Return True if head is out of bounds |
| `check_self_collision(snake)` | Return True if head overlaps body |

### `enumerate(snake)`

```python
for i, segment in enumerate(snake):
```

`enumerate` gives us both the **index** (`i`) and the **value** (`segment`) as we loop. We use the index to check if we're drawing the head (index 0) or a body segment (any other index).

### `spawn_food_safe(snake)`

```python
def spawn_food_safe(snake):
    while True:
        position = spawn_food()
        if position not in snake:
            return position
```

This keeps generating random positions until it finds one that is NOT occupied by the snake. The `while True` loop runs until `return` exits it. This prevents the frustrating situation where food appears under the snake.

### `paused = not paused`

This is a **toggle**. If `paused` is `True`, `not True` is `False`. If `paused` is `False`, `not False` is `True`. One line flips the value.

### Dynamic Speed

```python
current_speed = GAME_SPEED + (score // 3)
```

- `score // 3` uses integer division: score 0–2 gives 0, score 3–5 gives 1, etc.
- The base speed (10) increases by 1 for every 3 points scored
- At score 15, speed is 15 FPS — noticeably faster!
- At score 30, speed is 20 FPS — very challenging!

---

## Expected Output

### Normal Gameplay
- Snake head is **bright green**, body is **darker green**
- Score displayed in white at top-left
- Game gets slightly faster every 3 points

### When Paused
- Snake, food, and score remain visible (frozen)
- "PAUSED - Press P to Resume" appears in the centre
- Press P again to continue

### Game Over
- Shows "GAME OVER" in red
- Shows final score
- Shows final speed
- Shows "Press R to Restart"

---

## Common Mistakes

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Forgetting `not paused` in direction check | Can change direction while paused | Add `elif not paused:` before arrow key checks |
| `spawn_food_safe` infinite loop | Game freezes when snake fills screen | Rare in practice; for extra safety, add a max attempts counter |
| Functions defined inside the game loop | Functions recreated every frame (slow) | Define functions BEFORE the game loop |
| `enumerate` not available (very old Python) | Error | CodeHS supports Python 3, so this always works |
| Passing wrong arguments to functions | `TypeError` | Check function signatures match call sites |

---

## Debugging Tips

1. **Pause doesn't work**: Make sure `pygame.K_p` is lowercase p. Also check that the pause check is outside the `elif not paused` block (it needs to work even when already paused).
2. **Speed not increasing**: Print `current_speed` each frame. It should grow as `score` increases. Make sure `score // 3` is correct (not `score / 3`).
3. **Functions not called**: If you defined a function but the game behaves like before, check that you're actually calling the new functions in the game loop.
4. **Food spawns on snake**: Make sure you're calling `spawn_food_safe(snake_list)` (not `spawn_food()`).
5. **Two-tone snake looks wrong**: Check that `i == 0` catches only the head. If the colours are reversed, swap `GREEN` and `DARK_GREEN`.

---

## Review Questions

1. What is "refactoring" and why is it useful?
2. How does `enumerate()` differ from a regular `for` loop?
3. Why does `spawn_food_safe` use a `while True` loop? What stops it from running forever?
4. How does the formula `GAME_SPEED + (score // 3)` create gradual difficulty?
5. What does `paused = not paused` do?

---

## Practice Exercises

### Exercise 1: Add Grid Lines
Draw subtle grid lines on the background to help visualise the cells:

```python
def draw_grid():
    """Draw light grid lines."""
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(window, (30, 30, 30), (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(window, (30, 30, 30), (0, y), (WINDOW_WIDTH, y))
```

Call this after `window.fill(BLACK)` and before `draw_snake()`.

### Exercise 2: Show Speed on Screen
Display the current speed alongside the score during gameplay. Add a second line of text showing "Speed: X" at position `(10, 40)`.

### Exercise 3: Maximum Speed Cap
The game shouldn't get infinitely fast. Add a cap:
```python
current_speed = min(GAME_SPEED + (score // 3), 25)
```

What does `min()` do here? Test it by getting a high score.

---

## Extension Challenge

Add a **start screen** that shows before the game begins. The start screen should display:
- "SNAKE" in large text
- "Press ENTER to Start" below it
- "Use arrow keys to move"

The game should only begin when the player presses Enter. You will need a third game state (e.g., `game_started = False`).

---

## Teacher Notes

**Time Estimate**: 40–50 minutes

**Key Misconceptions**:
- Students may think refactoring changes the game's behaviour. Emphasize: "The game does exactly the same thing — we're just organising the code better."
- The `enumerate` function may be new. If students struggle, they can use a counter variable instead: `i = 0` before the loop, `i = i + 1` inside it.
- Dynamic speed can make debugging harder because the game speeds up. Suggest students temporarily set `current_speed = 10` (constant) while testing other features.

**Assessment Checklist**:
- [ ] Code uses at least 4 functions
- [ ] Snake head is visually distinct from body
- [ ] Pause works correctly (P toggles)
- [ ] Game speed increases with score
- [ ] Food never spawns on the snake
- [ ] Student can explain what each function does

**Code Quality Discussion**:
This is a good lesson to discuss code quality. Ask students: "Is it easier to find a bug in the Lesson 6 code or the Lesson 7 code? Why?" The function names serve as documentation — `check_wall_collision()` tells you exactly what that code does without reading the implementation.

---

## What's Next?

Your Snake game is polished and well-organised! In **Lesson 8**, we explore extension activities — bonus features you can add to make your game unique: difficulty settings, high scores, obstacles, animated food, sound effects, themes, and power-ups.

[← Back to Lesson 6](Lesson-06-Losing-the-Game.md) | [→ Continue to Lesson 8: Extension Activities](Lesson-08-Extension-Activities.md)
