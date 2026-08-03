# Lesson 2 – Drawing the Snake

## Learning Objectives

By the end of this lesson, you will be able to:

- Explain how the PyGame coordinate system works
- Draw rectangles on screen using `pygame.draw.rect()`
- Define a grid system for the game
- Represent the snake as a Python list
- Display a multi-segment snake on screen

---

## New Concepts

### The Coordinate System

In PyGame, the screen uses an **(x, y) coordinate system**, but it works differently from what you may have learned in maths class:

```
(0,0) ───────────────────────► x increases
  │
  │
  │         (200, 150) ●
  │
  │
  ▼
  y increases
```

**Key differences from maths coordinates:**
- **(0, 0) is the top-left corner** (not the centre)
- **x increases to the right** (same as maths)
- **y increases downward** (opposite of maths!)

So a point at `(200, 150)` is 200 pixels from the left edge and 150 pixels down from the top.

### Drawing Rectangles

PyGame draws rectangles with `pygame.draw.rect()`. A rectangle needs:
- Which **surface** to draw on (our window)
- What **colour** to use
- A **rectangle** defined by `(x, y, width, height)`

```python
pygame.draw.rect(window, GREEN, (100, 50, 20, 20))
#                surface  colour  x    y   w    h
```

This draws a 20×20 green square at position (100, 50).

### The Grid System

In Snake, the snake and food don't move pixel by pixel — they move in **cells** (grid squares). We define a cell size and snap everything to that grid.

```
┌──┬──┬──┬──┬──┬──┬──┬──┬──┬──┐
│  │  │  │  │  │  │  │  │  │  │  ← Each cell is 20×20 pixels
├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤
│  │  │■■│■■│■■│  │  │  │  │  │  ← Snake occupies 3 cells
├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤
│  │  │  │  │  │  │  │  │  │  │
├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤
│  │  │  │  │  │  │  │  │  │  │
└──┴──┴──┴──┴──┴──┴──┴──┴──┴──┘
```

With a 600×400 window and 20-pixel cells:
- The grid is **30 cells wide** (600 ÷ 20 = 30)
- The grid is **20 cells tall** (400 ÷ 20 = 20)

### Representing the Snake as a List

A snake is made of body segments. Each segment sits in one grid cell. We store the snake as a **list of positions**:

```python
snake_list = [[100, 100], [80, 100], [60, 100]]
#              ↑ head      ↑ body     ↑ tail
```

Each item `[x, y]` is one segment's position. The **first item is the head**, and the **last item is the tail**.

Why a list? Because:
- Lists can **grow** (when the snake eats food)
- We can easily **add** or **remove** segments
- We can **loop through** all segments to draw them

---

## Step-by-Step Instructions

### Step 1: Start with Your Lesson 1 Code

Open your Snake Game sandbox in CodeHS. You should have the code from Lesson 1. We will add to it.

### Step 2: Add More Colours

Find your colour definition section and add a green colour for the snake:

```python
# Colours (Red, Green, Blue)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
```

### Step 3: Define the Cell Size

Add a constant for the grid cell size, near your window settings:

```python
# Grid settings
CELL_SIZE = 20
```

Every segment of the snake will be a 20×20 pixel square.

### Step 4: Create the Snake

Before the game loop, define the snake's starting position:

```python
# Snake starting position
snake_list = [[100, 100], [80, 100], [60, 100]]
```

This creates a snake with 3 segments:
- Head at (100, 100)
- Body at (80, 100)
- Tail at (60, 100)

All three segments are on the same row (y=100) but at different x positions, spaced 20 pixels apart (one cell each).

### Step 5: Draw the Snake in the Game Loop

Inside your game loop, after `window.fill(BLACK)` and before `pygame.display.update()`, add code to draw each segment:

```python
    # Draw the snake
    for segment in snake_list:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
```

This loops through every `[x, y]` position in `snake_list` and draws a green square at that location.

### Step 6: Run and Check

Click **▶ Run**. You should see three green squares in a horizontal line on the black background.

---

## Complete Code

```python
import pygame

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

# Snake starting position
snake_list = [[100, 100], [80, 100], [60, 100]]

# Game loop
running = True
while running:
    # 1. Check for input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update game state (nothing yet)

    # 3. Draw everything
    window.fill(BLACK)

    # Draw the snake
    for segment in snake_list:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    pygame.display.update()

# Quit PyGame
pygame.quit()
```

---

## Code Walkthrough

### `GREEN = (0, 255, 0)`
A colour with no red, maximum green, and no blue — pure green. This is our snake's colour.

### `CELL_SIZE = 20`
Each grid cell (and each snake segment) is 20×20 pixels. This constant makes our code flexible — if we later want bigger or smaller cells, we change one number.

### `snake_list = [[100, 100], [80, 100], [60, 100]]`

A list containing three lists. Each inner list `[x, y]` represents one segment:

```
Position:   [100, 100]    [80, 100]    [60, 100]
Role:        Head          Body          Tail
Grid cell:   Column 5      Column 4     Column 3
             Row 5         Row 5        Row 5
```

(Column = x ÷ 20, Row = y ÷ 20)

### The Drawing Loop

```python
for segment in snake_list:
    pygame.draw.rect(window, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
```

Let's break down what happens each time through the loop:

| Iteration | `segment` | `segment[0]` (x) | `segment[1]` (y) | What's drawn |
|-----------|-----------|-------------------|-------------------|--------------|
| 1st | [100, 100] | 100 | 100 | Square at (100, 100) |
| 2nd | [80, 100] | 80 | 100 | Square at (80, 100) |
| 3rd | [60, 100] | 60 | 100 | Square at (60, 100) |

The result: three green squares in a row — our snake!

### `pygame.draw.rect(window, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))`

The four numbers in the rectangle tuple are:
- `segment[0]` — x position (left edge of the square)
- `segment[1]` — y position (top edge of the square)
- `CELL_SIZE` — width (20 pixels)
- `CELL_SIZE` — height (20 pixels)

---

## Expected Output

You should see:
- A **black background** filling the window
- **Three green squares** arranged horizontally near the top-left area
- The squares are touching (no gaps between them)
- The snake does not move yet (that's Lesson 3!)

```
Approximate appearance:

  ┌────────────────────────────────────────────┐
  │                                            │
  │                                            │
  │                                            │
  │                                            │
  │      ■ ■ ■   ← Three green squares        │
  │                                            │
  │                                            │
  │                                            │
  │                                            │
  │                                            │
  └────────────────────────────────────────────┘
```

---

## Common Mistakes

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Drawing AFTER `pygame.display.update()` | Snake is invisible | Move drawing code BEFORE `pygame.display.update()` |
| Using `()` instead of `[]` for segments | Can't modify positions later | Use square brackets: `[100, 100]` |
| Forgetting `CELL_SIZE` in the rect | Tiny 1-pixel dots or errors | Include all 4 values: `(x, y, CELL_SIZE, CELL_SIZE)` |
| Drawing BEFORE `window.fill(BLACK)` | Snake is covered by black fill | Draw AFTER the fill |
| Indentation not inside the `while` loop | Snake draws once or not at all | Make sure drawing code is indented inside `while running:` |

### Order Matters!

The drawing order inside the game loop must be:
1. `window.fill(BLACK)` — erase everything
2. Draw the snake — put new shapes on screen
3. `pygame.display.update()` — show the result

If you swap steps 1 and 2, the fill covers your snake. If you forget step 3, nothing appears.

---

## Debugging Tips

1. **If you see nothing on the black screen** — check that your drawing code comes AFTER `window.fill()` and BEFORE `pygame.display.update()`.
2. **If only one square appears** — make sure `snake_list` has three items and your `for` loop uses `snake_list` (not just one position).
3. **If squares are in weird positions** — print `snake_list` before the loop to check the values.
4. **Add a temporary test**: Replace your snake_list with `[[0, 0]]` to draw one square in the top-left corner. If it appears, your drawing code works and the issue is with positions.

---

## Review Questions

1. In PyGame's coordinate system, which direction does the y-axis increase — up or down?
2. What are the four values needed to define a rectangle in `pygame.draw.rect()`?
3. Why do we use a list to store the snake instead of separate variables for each segment?
4. If `CELL_SIZE = 20` and the window is 600 pixels wide, how many cells fit across the screen?
5. In our `snake_list`, which position is the head — the first item or the last item?

---

## Practice Exercises

### Exercise 1: Make a Longer Snake
Change `snake_list` to have **5 segments** instead of 3. Make sure they are all spaced correctly (each one 20 pixels apart on the x-axis).

### Exercise 2: Move the Snake's Position
Change the starting position so the snake appears in the **centre of the screen**. Remember: the centre is at approximately (300, 200).

### Exercise 3: Change the Snake's Colour
1. Create a `DARK_GREEN = (0, 200, 0)` colour
2. Draw the **head** (first segment) in bright `GREEN` and the **body** (remaining segments) in `DARK_GREEN`

Hint: You can use `snake_list[0]` for the head and `snake_list[1:]` for the rest.

---

## Extension Challenge

Draw a **grid of lines** on the background so you can see the cells. Use `pygame.draw.line()` to draw light grey lines:

```python
GREY = (40, 40, 40)
# Draw vertical lines
for x in range(0, WINDOW_WIDTH, CELL_SIZE):
    pygame.draw.line(window, GREY, (x, 0), (x, WINDOW_HEIGHT))
# Draw horizontal lines
for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
    pygame.draw.line(window, GREY, (0, y), (WINDOW_WIDTH, y))
```

Place this AFTER `window.fill(BLACK)` but BEFORE drawing the snake. This helps you visualise the grid!

---

## Teacher Notes

**Time Estimate**: 25–35 minutes

**Key Misconceptions**:
- Students confuse the maths coordinate system (y-up) with the screen coordinate system (y-down). Use the ASCII diagram to emphasize this.
- Some students will try to create separate variables like `head_x`, `head_y`, `body1_x`, etc. Explain why a list is better: "What if the snake grows to 50 segments? Would you want 100 variables?"
- The difference between `(tuples)` and `[lists]` may confuse students. Emphasize: we use lists because the snake changes (grows/moves), and lists can be changed.

**Assessment Checklist**:
- [ ] Student can explain why (0,0) is top-left
- [ ] Student can draw a rectangle at a specified position
- [ ] Student's snake appears on screen with correct number of segments
- [ ] Student can modify snake length and position

**Preparation for Next Lesson**:
In Lesson 3, students will make the snake move. The key concept is: to move the snake, we add a new head to the front of the list and remove the tail from the end. Make sure students understand the list structure before moving on.

---

## What's Next?

Your snake looks great, but it just sits there! In **Lesson 3**, we will make the snake move using the arrow keys and learn how to control the game's speed.

[← Back to Lesson 1](Advanced/WIP/Snake/Lesson-01-Getting-Started.md) | [→ Continue to Lesson 3: Snake Movement](Lesson-03-Snake-Movement.md)
