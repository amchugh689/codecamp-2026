# Lesson 5 – Eating Food

## Learning Objectives

By the end of this lesson, you will be able to:

- Detect when the snake's head is at the same position as the food (collision detection)
- Make the snake grow by one segment when it eats
- Track and display a score
- Render text on screen using PyGame fonts
- Spawn new food after the old food is eaten

---

## New Concepts

### Collision Detection

**Collision detection** means checking whether two objects are overlapping or touching. In many games, this involves complex maths with circles and rectangles. But in our grid-based Snake game, it is beautifully simple:

> The snake eats the food when the **head's position equals the food's position**.

```python
if snake_list[0] == food_position:
    # The snake ate the food!
```

That's it! Because everything is snapped to the grid, we just compare the `[x, y]` lists. If they match, the head is on top of the food.

```
Before eating:               After eating:
┌──┬──┬──┬──┬──┐           ┌──┬──┬──┬──┬──┐
│  │  │■ │■ │■→│◆          │  │  │■ │■ │■ │■■  ← grew!
└──┴──┴──┴──┴──┘           └──┴──┴──┴──┴──┘
         Head hits food              New food spawns elsewhere
```

### Growing the Snake

Remember from Lesson 3: each frame we `insert` a new head and `pop` the tail. This keeps the snake the same length.

To **grow** the snake, we simply **skip the `pop()`** on the frame when it eats food. The new head is inserted but the tail stays — the snake is now one segment longer!

```
Normal frame:  insert head + pop tail    → same length
Eating frame:  insert head (no pop)      → one segment longer
```

### Displaying Text with PyGame Fonts

To show the score on screen, we need to:
1. Create a **font object** (choose size and style)
2. **Render** text into a surface (like a small image of the text)
3. **Blit** (draw) that surface onto the game window

```python
font = pygame.font.SysFont(None, 35)          # Step 1: Create font
text_surface = font.render("Score: 5", True, WHITE)  # Step 2: Render text
window.blit(text_surface, (10, 10))           # Step 3: Draw at position
```

- `SysFont(None, 35)` uses the default system font at size 35
- `render(text, antialias, colour)` creates a surface with the text drawn on it
- `True` turns on **antialiasing** (smooth edges on letters)
- `blit(surface, position)` draws one surface onto another

---

## Step-by-Step Instructions

### Step 1: Add White Colour for Text

Add a white colour constant:

```python
WHITE = (255, 255, 255)
```

### Step 2: Create a Font Object

After your colour definitions and before the game loop, create the font:

```python
# Font for score display
font = pygame.font.SysFont(None, 35)
```

### Step 3: Add a Score Variable

Before the game loop, add:

```python
# Score
score = 0
```

### Step 4: Detect Eating (Collision Check)

In the game loop, after you insert the new head (`snake_list.insert(0, new_head)`), add the eating logic — and **replace** the unconditional `snake_list.pop()` with a conditional one:

**Replace this:**
```python
    snake_list.insert(0, new_head)
    snake_list.pop()
```

**With this:**
```python
    snake_list.insert(0, new_head)

    # Check if snake ate the food
    if snake_list[0] == food_position:
        score = score + 1
        food_position = spawn_food()
        # Don't pop - snake grows!
    else:
        snake_list.pop()
```

When the head is on the food:
- Score goes up by 1
- New food spawns
- We do NOT remove the tail (the snake grows)

When the head is NOT on food:
- Remove the tail as normal (snake stays the same length)

### Step 5: Draw the Score

In the drawing section, after drawing the food and before `pygame.display.update()`, add:

```python
    # Draw the score
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))
```

### Step 6: Run and Test

Click **▶ Run**. Now when the snake's head reaches the food:
- The food disappears and reappears elsewhere
- The snake gets one segment longer
- The score increases by 1

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

# Font for score display
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

    # Check if snake ate the food
    if snake_list[0] == food_position:
        score = score + 1
        food_position = spawn_food()
        # Don't pop - snake grows!
    else:
        snake_list.pop()

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

# Quit PyGame
pygame.quit()
```

---

## Code Walkthrough

### `WHITE = (255, 255, 255)`
Maximum red + maximum green + maximum blue = white. We use this for the score text.

### `font = pygame.font.SysFont(None, 35)`
Creates a font object:
- `None` means "use the default system font" (works on any computer)
- `35` is the font size in pixels

We create this **once**, before the game loop. Creating a font every frame would be wasteful.

### `score = 0`
A simple counter that starts at zero. We add 1 each time the snake eats food.

### The Eating Logic

```python
snake_list.insert(0, new_head)

if snake_list[0] == food_position:
    score = score + 1
    food_position = spawn_food()
else:
    snake_list.pop()
```

**Important**: We insert the new head FIRST, then check if it's on the food. This is the order because:
1. `insert(0, new_head)` — the head moves to its new position
2. `if snake_list[0] == food_position` — is the head now on the food?
   - YES: Score up, new food, keep the tail (grow)
   - NO: Remove tail (normal movement)

### `snake_list[0] == food_position`
This compares two lists: `[x, y] == [x, y]`. Python checks if both values match. If the head's x equals food's x AND head's y equals food's y, this is `True`.

### `food_position = spawn_food()`
When the snake eats, we call `spawn_food()` again to place new food at a random location. The old `food_position` is overwritten.

### Drawing the Score

```python
score_text = font.render("Score: " + str(score), True, WHITE)
window.blit(score_text, (10, 10))
```

- `"Score: " + str(score)` creates a string like "Score: 3"
- `str(score)` converts the number to a string (you can't add a number to a string directly)
- `font.render(...)` turns that string into a drawable image
- `window.blit(score_text, (10, 10))` draws it 10 pixels from the top-left corner

---

## Expected Output

When you run the program:
- Snake moves with arrow keys (as before)
- "Score: 0" appears in the top-left corner in white text
- When the snake's head reaches the red food:
  - The food vanishes and appears somewhere new
  - The snake becomes one segment longer
  - The score increases: "Score: 1", "Score: 2", etc.
- The snake can still go off-screen (we fix that in Lesson 6)

```
┌────────────────────────────────────────────────┐
│ Score: 3                                       │
│                                                │
│            ■ ■ ■ ■ ■ ■  ← Snake (grew!)       │
│                                                │
│                                                │
│                   ◆  ← New food                │
│                                                │
└────────────────────────────────────────────────┘
```

---

## Common Mistakes

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Comparing with `==` before inserting head | Checks old head position, not new | Insert head FIRST, then compare |
| Forgot `str(score)` in render | `TypeError: can only concatenate str to str` | Convert score to string: `str(score)` |
| Always popping (didn't add the if/else) | Snake never grows | Replace unconditional `pop()` with the if/else block |
| Never popping (removed pop entirely) | Snake grows every frame | Only skip pop when food is eaten (use the else) |
| Created font inside the game loop | Game runs slowly | Create `font` once, before the loop |
| Forgot `window.blit()` | Score text renders but never appears | Add `window.blit(score_text, (10, 10))` |

---

## Debugging Tips

1. **Snake doesn't grow when it hits food**: Add `print(snake_list[0], food_position)` to see if the values actually match. If they don't match exactly, food might not be aligned to the grid.
2. **Score doesn't update**: Make sure `score = score + 1` is inside the `if` block (indented correctly).
3. **Food spawns on the snake**: This can happen! We will fix it in Lesson 7. For now, it is a minor issue.
4. **Text looks blurry or wrong**: Try changing the font size. `SysFont(None, 35)` should work, but you can try sizes from 20 to 50.
5. **Helpful test**: Temporarily set `snake_list = [[80, 100]]` and `food_position = [100, 100]` with `direction = "RIGHT"`. The snake will hit the food on the very first frame — instant test!

---

## Review Questions

1. How does our collision detection work? Why is it so simple in a grid-based game?
2. What is the difference between what happens on a frame when the snake eats vs. when it doesn't?
3. Why do we need `str(score)` when building the score text?
4. What is the difference between `font.render()` and `window.blit()`?
5. Why do we call `spawn_food()` inside the eating condition, not just once at the start?

---

## Practice Exercises

### Exercise 1: Points Worth More
Modify the code so each food item is worth **10 points** instead of 1. Change the line:
```python
score = score + 1
```
What would you change it to?

### Exercise 2: Longer Starting Snake
Change the starting `snake_list` to have **5 segments**. Verify the game still works — the snake should still grow when eating food.

### Exercise 3: Score Position
Move the score display to the **top-right corner** of the screen. Hint: You will need to calculate the x position based on the text width. Try:
```python
text_width = score_text.get_width()
window.blit(score_text, (WINDOW_WIDTH - text_width - 10, 10))
```

---

## Extension Challenge

Add a **food counter** that shows how many food items the snake has eaten (separate from the score). Display it below the score:

```python
food_eaten = 0
```

Increment `food_eaten` when the snake eats, and render it as a second line of text at position `(10, 45)`.

Bonus: Make the score worth different amounts — the first food is worth 1 point, the second 2 points, the third 3 points, and so on. (Hint: use `food_eaten + 1` as the point value.)

---

## Teacher Notes

**Time Estimate**: 25–35 minutes

**Key Misconceptions**:
- Students may think collision detection is always complex. Emphasize that grid alignment makes it trivially simple — exact equality check. In other types of games, you would need distance calculations or bounding-box overlap checks.
- The if/else pattern around `pop()` is the trickiest part. Students sometimes put `pop()` both inside and outside the if/else. Walk through both cases on the board: "eating frame" vs. "normal frame."
- `font.render()` doesn't draw anything on screen — it creates a surface. `blit()` draws that surface. Students often forget the `blit()` step.

**Assessment Checklist**:
- [ ] Snake grows by exactly one segment when eating food
- [ ] Score updates correctly
- [ ] New food appears after eating
- [ ] Student can explain the if/else pattern around `pop()`
- [ ] Score is displayed on screen

**Classroom Activity**:
Challenge students to a "highest score" competition — who can eat the most food in 60 seconds? (The snake will still go off-screen since there are no boundaries yet.) This motivates Lesson 6.

---

## What's Next?

Our snake eats and grows — great! But there's a problem: **it can never lose**. The snake goes off-screen and the game runs forever. In **Lesson 6**, we add wall collisions, self-collision, Game Over, and restart.

[← Back to Lesson 4](Lesson-04-Food.md) | [→ Continue to Lesson 6: Losing the Game](Lesson-06-Losing-the-Game.md)
