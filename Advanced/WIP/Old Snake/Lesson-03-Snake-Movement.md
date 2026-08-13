# Lesson 3 – Snake Movement

## Learning Objectives

By the end of this lesson, you will be able to:

- Detect keyboard input using PyGame events
- Move the snake continuously in a direction
- Control game speed using `pygame.time.Clock`
- Prevent the snake from reversing into itself
- Explain the difference between event-driven and continuous movement

---

## New Concepts

### Keyboard Input in PyGame

PyGame detects keyboard presses as **events**. When a player presses a key, PyGame creates a `KEYDOWN` event that includes which key was pressed.

```python
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_UP:
        # Player pressed the up arrow
    if event.key == pygame.K_DOWN:
        # Player pressed the down arrow
```

Common key constants:
| Key | PyGame Constant |
|-----|----------------|
| Up Arrow | `pygame.K_UP` |
| Down Arrow | `pygame.K_DOWN` |
| Left Arrow | `pygame.K_LEFT` |
| Right Arrow | `pygame.K_RIGHT` |

### Continuous Movement

In Snake, you press an arrow key to **set a direction**, and the snake keeps moving that way on its own. You don't hold the key down — one press changes the direction.

We achieve this with a **direction variable** that remembers which way the snake is heading:

```python
direction = "RIGHT"  # Snake starts moving right
```

Each frame, we move the snake based on the current direction — even if no key was pressed that frame.

### How Snake Movement Works

Moving a snake is simpler than you might think. We don't move every segment individually. Instead:

1. **Calculate a new head position** (one cell in the current direction)
2. **Insert the new head** at the front of the list
3. **Remove the tail** from the end of the list

```
Before: [Head, Body, Tail]     Direction: RIGHT
         [100,100] [80,100] [60,100]

Step 1 - New head: [120, 100]  (100 + 20 = 120)
Step 2 - Insert:   [120,100] [100,100] [80,100] [60,100]
Step 3 - Remove tail: [120,100] [100,100] [80,100]

After:  [Head, Body, Tail]
         [120,100] [100,100] [80,100]
```

The snake appears to slither forward! The tail disappears and a new head appears.

### Game Timing with Clock

Without timing control, the game loop runs as fast as the computer allows — the snake would be a blur! We use `pygame.time.Clock` to control the speed:

```python
clock = pygame.time.Clock()

while running:
    clock.tick(10)  # Run at 10 frames per second
    # ... rest of game loop
```

`clock.tick(10)` means: "Wait until 1/10th of a second has passed before continuing." This gives us 10 frames per second — the snake moves 10 times per second.

### Preventing Reverse Movement

In Snake, you cannot turn 180° (going right and then suddenly going left). That would make the snake crash into itself immediately. We must **block opposite directions**:

- If going RIGHT, you cannot switch to LEFT
- If going LEFT, you cannot switch to RIGHT
- If going UP, you cannot switch to DOWN
- If going DOWN, you cannot switch to UP

---

## Step-by-Step Instructions

### Step 1: Add the Clock

After `pygame.init()` and before the game loop, create a clock object:

```python
# Game timing
clock = pygame.time.Clock()
GAME_SPEED = 10
```

### Step 2: Add the Direction Variable

Before the game loop, set the starting direction:

```python
# Movement
direction = "RIGHT"
```

### Step 3: Detect Arrow Key Presses

Inside the event loop (where we check for `pygame.QUIT`), add key detection:

```python
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
```

Notice each `if` checks two things:
1. Was this key pressed? (`event.key == pygame.K_UP`)
2. Are we allowed to go that way? (`and direction != "DOWN"`)

### Step 4: Calculate the New Head Position

After the event loop but before drawing, add movement logic:

```python
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
```

**Important**: UP means y **decreases** (because y increases downward in PyGame). DOWN means y **increases**.

### Step 5: Move the Snake (Insert Head, Remove Tail)

Right after calculating the new head, update the list:

```python
    snake_list.insert(0, new_head)
    snake_list.pop()
```

- `insert(0, new_head)` puts the new head at position 0 (the front)
- `pop()` removes the last item (the tail)

### Step 6: Add the Clock Tick

At the very beginning of the game loop (right after `while running:`), add:

```python
    clock.tick(GAME_SPEED)
```

### Step 7: Run and Test

Click **▶ Run**. Your snake should now:
- Start moving to the right automatically
- Change direction when you press arrow keys
- Move at a steady, visible speed

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

# Game timing
clock = pygame.time.Clock()
GAME_SPEED = 10

# Snake starting position
snake_list = [[100, 100], [80, 100], [60, 100]]

# Movement
direction = "RIGHT"

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

    pygame.display.update()

# Quit PyGame
pygame.quit()
```

---

## Code Walkthrough

### `clock = pygame.time.Clock()`
Creates a clock object that we use to control game speed. Think of it as a metronome that keeps the game running at a steady pace.

### `GAME_SPEED = 10`
The number of frames per second. At 10 FPS, the snake moves 10 cells per second. Lower = slower snake. Higher = faster snake. We will use this later to make the game get harder.

### `direction = "RIGHT"`
A string that remembers the snake's current direction. The snake will move this way every frame until the player presses a different arrow key.

### The Key Detection Block

```python
if event.key == pygame.K_UP and direction != "DOWN":
    direction = "UP"
```

This reads as: "If the player pressed UP **and** the snake is NOT currently going DOWN, change direction to UP." The second condition prevents illegal 180° turns.

### Calculating the New Head

```python
head = snake_list[0]
if direction == "RIGHT":
    new_head = [head[0] + CELL_SIZE, head[1]]
```

- `snake_list[0]` gets the current head position
- `head[0]` is the head's x coordinate
- `head[0] + CELL_SIZE` moves one cell to the right
- `head[1]` stays the same (y doesn't change when moving horizontally)

Direction → coordinate change:
| Direction | x change | y change | Why |
|-----------|----------|----------|-----|
| RIGHT | + CELL_SIZE | 0 | Moving right = larger x |
| LEFT | - CELL_SIZE | 0 | Moving left = smaller x |
| UP | 0 | - CELL_SIZE | Moving up = smaller y (y is flipped!) |
| DOWN | 0 | + CELL_SIZE | Moving down = larger y |

### `snake_list.insert(0, new_head)`
Inserts `new_head` at index 0 — the very front of the list. The snake now has one extra segment at the front.

### `snake_list.pop()`
Removes the last item from the list (the tail). Combined with `insert`, this creates the illusion of movement: new head appears, old tail disappears.

### `clock.tick(GAME_SPEED)`
Pauses just long enough to maintain 10 FPS. If the computer is fast, it waits longer. If it is slow, it waits less. This keeps the game speed consistent.

---

## Expected Output

When you run the program:
- The snake starts moving **to the right** automatically
- Pressing **↑** makes it go up, **↓** goes down, **←** goes left, **→** goes right
- The snake moves at a steady pace (10 cells per second)
- You **cannot** reverse direction (pressing left while going right does nothing)
- The snake moves off-screen and disappears (we'll fix this in Lesson 6!)

---

## Common Mistakes

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Forgot `clock.tick(GAME_SPEED)` | Snake moves extremely fast (invisible) | Add `clock.tick(GAME_SPEED)` at the start of the loop |
| Using `elif` after `pygame.QUIT` check | Key events not detected | Use a separate `if` (not `elif`) for `KEYDOWN` |
| Swapping + and - for UP/DOWN | Snake goes opposite direction | Remember: UP = y minus, DOWN = y plus |
| Putting movement code outside the loop | Snake moves once and stops | Make sure all movement code is inside `while running:` |
| Forgetting `snake_list.pop()` | Snake grows forever | Add `pop()` after `insert()` |
| Using `append` instead of `insert(0, ...)` | New head goes to the end (tail) | Use `insert(0, new_head)` to add at the front |

---

## Debugging Tips

1. **Snake doesn't move**: Make sure `clock.tick()` and the movement code are INSIDE the `while` loop, properly indented.
2. **Snake moves but keys don't work**: Check that the `KEYDOWN` block is inside the `for event` loop and uses `event.key` (not `event.type`).
3. **Snake goes the wrong way when pressing UP**: Remember that UP = `y - CELL_SIZE` in PyGame (y decreases going up).
4. **Snake leaves a trail**: Make sure `window.fill(BLACK)` is still in your loop, BEFORE drawing the snake.
5. **Add a debug print**: Put `print(direction, snake_list[0])` in the loop to see the current direction and head position each frame.

---

## Review Questions

1. What is the difference between detecting a key press in the event loop vs. checking if a key is held down?
2. Why do we use `insert(0, new_head)` instead of `append(new_head)`?
3. What would happen if we removed `snake_list.pop()` from the code?
4. Why does moving UP require subtracting from the y coordinate?
5. What does `clock.tick(10)` do, and what would happen if we changed 10 to 5?

---

## Practice Exercises

### Exercise 1: Change the Speed
1. Change `GAME_SPEED` to 5. How does the snake feel?
2. Change it to 20. How does it feel now?
3. What value feels best to you for playing?

### Exercise 2: Start in a Different Direction
Change the starting direction to `"DOWN"` and the starting position to `[[300, 0], [300, 0], [300, 0]]`. Run the program — what happens?

Now fix the starting position so the snake starts at the top and moves down with proper spacing between segments.

### Exercise 3: Add WASD Controls
In addition to arrow keys, let players use W (up), A (left), S (down), D (right):
- `pygame.K_w` for W
- `pygame.K_a` for A
- `pygame.K_s` for S
- `pygame.K_d` for D

Add these as additional conditions in your key detection block.

---

## Extension Challenge

Add a **speed boost**: When the player holds the **Space** key, the snake moves twice as fast. When they release it, it returns to normal speed.

Hint: Use `pygame.key.get_pressed()` (which checks if a key is currently held down) instead of the event system. Check it each frame:

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_SPACE]:
    clock.tick(GAME_SPEED * 2)
else:
    clock.tick(GAME_SPEED)
```

---

## Teacher Notes

**Time Estimate**: 30–40 minutes

**Key Misconceptions**:
- Students often confuse `KEYDOWN` (event: key was just pressed this frame) with `get_pressed()` (state: key is currently held down). For Snake, we use `KEYDOWN` because one press = direction change.
- The y-axis being inverted is a major source of bugs. Draw it on a whiteboard if possible.
- Some students will try to move each segment individually. Emphasize the elegant insert/pop pattern: "You only calculate one new position — the head. Everything else shifts automatically."

**Assessment Checklist**:
- [ ] Snake moves continuously without the player holding a key
- [ ] All four arrow keys change direction correctly
- [ ] Snake cannot reverse (180° turn is blocked)
- [ ] Game runs at a consistent, playable speed
- [ ] Student can explain the insert/pop movement pattern

**Classroom Demonstration Idea**:
Have students stand in a line (they are the snake). The "head" student steps in a new direction, everyone else steps to where the person in front of them was. Then the "tail" student sits down. This physically demonstrates the insert/pop pattern.

---

## What's Next?

The snake can move — but there's nothing to eat! In **Lesson 4**, we will add food that appears at random positions on the grid.

[← Back to Lesson 2](Lesson-02-Drawing-the-Snake.md) | [→ Continue to Lesson 4: Food](Lesson-04-Food.md)
