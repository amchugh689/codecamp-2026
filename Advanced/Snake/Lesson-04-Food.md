# Lesson 4 – Food

## Learning Objectives

By the end of this lesson, you will be able to:

- Import and use Python's `random` module
- Generate random numbers within a range
- Snap random positions to a grid
- Draw food on the game screen
- Ensure food spawns within the game boundaries

---

## New Concepts

### Random Numbers

Games need randomness — otherwise food would always appear in the same spot and every game would be identical. Python's `random` module gives us tools to generate unpredictable numbers.

```python
import random

# Random integer between 1 and 10 (inclusive)
number = random.randint(1, 10)
```

`random.randint(a, b)` returns a random whole number from `a` to `b`, including both endpoints.

### Grid Alignment

In our Snake game, everything moves on a 20-pixel grid. The food must also land exactly on a grid cell — not between cells. If food appeared at position (37, 82), it would look misaligned:

```
Bad (not on grid):          Good (on grid):
┌──┬──┬──┬──┐              ┌──┬──┬──┬──┐
│  │  │  │  │              │  │  │  │  │
├──┼──┼──┼──┤              ├──┼──┼──┼──┤
│  │ ◆│  │  │  ← offset   │  │◆ │  │  │  ← aligned
├──┼──┼──┼──┤              ├──┼──┼──┼──┤
│  │  │  │  │              │  │  │  │  │
└──┴──┴──┴──┘              └──┴──┴──┴──┘
```

To snap to the grid, food positions must be **multiples of CELL_SIZE** (0, 20, 40, 60, 80, ...).

### Strategy: Generate a Cell Index, Then Multiply

Instead of generating a random pixel position and trying to round it, we:
1. Calculate how many cells fit in the window
2. Pick a random cell number
3. Multiply by CELL_SIZE to get the pixel position

```python
# Window is 600 pixels wide, cells are 20 pixels
# 600 / 20 = 30 cells (numbered 0 to 29)
cell_x = random.randint(0, 29)
food_x = cell_x * CELL_SIZE  # Always a multiple of 20
```

### Keeping Food Inside the Window

The food must not spawn outside the visible area. Since our window is 600×400 and cells are 20px:

- x can be 0, 20, 40, ... up to 580 (that's cell 0 to cell 29)
- y can be 0, 20, 40, ... up to 380 (that's cell 0 to cell 19)

Why 580 and not 600? Because the food square starts at that position and extends 20 pixels to the right — so starting at 580 means it ends at 600 (the right edge). Starting at 600 would put it off-screen.

---

## Step-by-Step Instructions

### Step 1: Import the Random Module

At the top of your file, add `random` to your imports:

```python
import pygame
import random
```

### Step 2: Add a Food Colour

Add a red colour for the food, with your other colour definitions:

```python
RED = (255, 0, 0)
```

### Step 3: Create a Function to Generate Food Position

Before the game loop, add this function:

```python
def spawn_food():
    x = random.randint(0, (WINDOW_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    y = random.randint(0, (WINDOW_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    return [x, y]
```

Let's break this down:
- `(WINDOW_WIDTH - CELL_SIZE) // CELL_SIZE` calculates the maximum cell index
  - (600 - 20) // 20 = 580 // 20 = 29
- `random.randint(0, 29)` picks a random cell number (0 to 29)
- Multiplying by `CELL_SIZE` converts back to pixel position

### Step 4: Spawn the First Food

Before the game loop, call the function to create the initial food:

```python
food_position = spawn_food()
```

### Step 5: Draw the Food

Inside the game loop, after drawing the snake and before `pygame.display.update()`, add:

```python
    # Draw the food
    pygame.draw.rect(window, RED, (food_position[0], food_position[1], CELL_SIZE, CELL_SIZE))
```

### Step 6: Run and Test

Click **▶ Run**. You should see:
- Your green snake moving as before
- A **red square** somewhere on the screen

Each time you run the program, the food should appear in a **different** position (because it's random).

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

# Game timing
clock = pygame.time.Clock()
GAME_SPEED = 10


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

# Game loop
running = True
while running:
    clock.tick(GAME_SPEED)

    # 1. Check for input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

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
    snake_list.pop()

    # 3. Draw everything
    window.fill(BLACK)

    # Draw the snake
    for segment in snake_list:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # Draw the food
    pygame.draw.rect(window, RED, (food_position[0], food_position[1], CELL_SIZE, CELL_SIZE))

    pygame.display.update()

# Quit PyGame
pygame.quit()
```

---

## Code Walkthrough

### `import random`
Loads Python's random number module. We need this for `random.randint()`.

### `RED = (255, 0, 0)`
Maximum red, no green, no blue — pure red. This is our food colour.

### The `spawn_food()` Function

```python
def spawn_food():
    x = random.randint(0, (WINDOW_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    y = random.randint(0, (WINDOW_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    return [x, y]
```

Let's trace through the x calculation with our values:
1. `WINDOW_WIDTH - CELL_SIZE` = 600 - 20 = 580
2. `580 // CELL_SIZE` = 580 // 20 = 29
3. `random.randint(0, 29)` picks a number, say 15
4. `15 * CELL_SIZE` = 15 * 20 = 300

So food_x = 300, which is a valid grid-aligned position.

**Why a function?** We will call `spawn_food()` again in Lesson 5 every time the snake eats — having it as a function means we don't duplicate code.

### `food_position = spawn_food()`
Calls our function once to create the first food item. `food_position` will be something like `[300, 160]`.

### Drawing the Food

```python
pygame.draw.rect(window, RED, (food_position[0], food_position[1], CELL_SIZE, CELL_SIZE))
```

Same pattern as drawing snake segments — a 20×20 rectangle at the food's position, but in red.

---

## Expected Output

When you run the program:
- The green snake moves as before (arrow keys work)
- A **red square** appears at a random position on screen
- The food doesn't move
- The snake can pass through/over the food (eating isn't implemented yet — that's Lesson 5!)
- If you run the program again, the food will likely be in a different spot

```
┌────────────────────────────────────────────────┐
│                                                │
│      ■ ■ ■ →                                   │
│                                                │
│                                                │
│                        ◆ ← Red food            │
│                                                │
│                                                │
└────────────────────────────────────────────────┘
```

---

## Common Mistakes

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Forgot `import random` | `NameError: name 'random' is not defined` | Add `import random` at the top |
| Food at position 600 or 400 | Food partially or fully off-screen | Use `WINDOW_WIDTH - CELL_SIZE` as the max |
| Not multiplying by CELL_SIZE | Food not aligned to grid (between cells) | Multiply the random result by `CELL_SIZE` |
| Calling `spawn_food()` inside the loop | Food moves every frame (teleports) | Call it once before the loop (we'll call it again in Lesson 5 only when eaten) |
| Drawing food before `window.fill()` | Food is invisible (covered by black) | Draw after `window.fill(BLACK)` |

---

## Debugging Tips

1. **Food not visible**: Add `print(food_position)` after `spawn_food()` to see the coordinates. Check that they are within 0–580 for x and 0–380 for y.
2. **Food always in same spot**: Make sure you have `import random` (not `import Random` — Python is case-sensitive).
3. **Food appears between grid lines**: Print the x and y values — they should be multiples of 20. If not, check your multiplication.
4. **Test the function**: Add these temporary lines before the game loop to verify:
   ```python
   for i in range(5):
       print(spawn_food())
   ```
   All printed positions should be multiples of 20.

---

## Review Questions

1. Why do we need the `random` module? What would happen without it?
2. What does `//` mean in Python? How is it different from `/`?
3. Why do we multiply the random number by `CELL_SIZE`?
4. Why is the maximum x position 580 instead of 600?
5. Why did we write `spawn_food()` as a function instead of putting the code directly?

---

## Practice Exercises

### Exercise 1: Different Food Colour
Change the food colour to orange `(255, 165, 0)` or yellow `(255, 255, 0)`.

### Exercise 2: Verify Grid Alignment
Add this code before the game loop to test that food always lands on the grid:

```python
# Test: generate 20 food positions and check alignment
for i in range(20):
    test_food = spawn_food()
    if test_food[0] % CELL_SIZE != 0 or test_food[1] % CELL_SIZE != 0:
        print("ERROR: Food not aligned!", test_food)
    else:
        print("OK:", test_food)
```

Run it and verify all positions print "OK". Then remove this test code.

### Exercise 3: Two Food Items
Modify the code to display **two** food items at the same time:
1. Create `food_position_2 = spawn_food()`
2. Draw both food items in the game loop

(This is just for practice — we'll go back to one food item in Lesson 5.)

---

## Extension Challenge

Make the food a **different shape** — draw it as a circle instead of a square:

```python
# Draw circular food
pygame.draw.circle(window, RED, (food_position[0] + CELL_SIZE // 2, food_position[1] + CELL_SIZE // 2), CELL_SIZE // 2)
```

The circle needs a **centre point** and a **radius**, unlike the rectangle which needs a top-left corner. We add `CELL_SIZE // 2` to the food position to centre the circle in the grid cell.

---

## Teacher Notes

**Time Estimate**: 20–30 minutes

**Key Misconceptions**:
- Students may not understand why `//` (integer division) is needed instead of `/` (which returns a float). Explain: "We need a whole number for `randint`, and pixel positions should be whole numbers."
- The concept of snapping to a grid by multiplying an index takes some explanation. Use an analogy: "It's like having numbered parking spots. You pick a random spot number (3), then calculate the position (spot 3 × 2 metres per spot = 6 metres from the start)."
- Some students will put `spawn_food()` inside the game loop, making food jump every frame. Emphasize it should be called once to create, and again only when eaten (Lesson 5).

**Assessment Checklist**:
- [ ] Student can explain why random numbers are needed in games
- [ ] Food appears at a random, grid-aligned position
- [ ] Food stays within the window boundaries
- [ ] Student understands the grid alignment technique
- [ ] Student can explain why `spawn_food()` is a function

**Extension**: If a student finishes early, have them add a border to the food rectangle by drawing a slightly larger yellow rectangle behind the red one.

---

## What's Next?

The food is there, but nothing happens when the snake reaches it! In **Lesson 5**, we will make the snake **eat** the food, grow longer, and keep score.

[← Back to Lesson 3](Lesson-03-Snake-Movement.md) | [→ Continue to Lesson 5: Eating Food](Lesson-05-Eating-Food.md)
