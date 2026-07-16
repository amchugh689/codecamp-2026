# Lesson 1 – Getting Started with PyGame

## Learning Objectives

By the end of this lesson, you will be able to:

- Explain what PyGame is and why we use it for game development
- Describe how a game loop works
- Create a new Pygame project in CodeHS
- Import the `pygame` library
- Create a game window with a title
- Write a basic game loop that keeps the window open
- Quit the game cleanly

---

## New Concepts

### What Is PyGame?

PyGame is a **Python library** (a collection of pre-written code) that makes it easy to create games. It handles things that would be very difficult to build from scratch:

- Opening a window
- Drawing shapes and images
- Detecting keyboard and mouse input
- Playing sounds
- Controlling timing and speed

Think of PyGame as a **toolbox** — it gives you all the tools you need to build a game without starting from nothing.

### What Is a Game Loop?

Every video game runs a **game loop** — a block of code that repeats over and over, many times per second. Each time through the loop, the game:

1. **Checks for input** (keyboard, mouse)
2. **Updates the game state** (moves objects, checks collisions)
3. **Draws everything** on screen

```
┌──────────────────────────────────────┐
│            GAME LOOP                 │
│                                      │
│   ┌─────────────┐                   │
│   │ Check Input │◄──────────┐       │
│   └──────┬──────┘           │       │
│          ▼                  │       │
│   ┌─────────────┐           │       │
│   │ Update Game │           │       │
│   └──────┬──────┘           │       │
│          ▼                  │       │
│   ┌─────────────┐           │       │
│   │ Draw Screen │───────────┘       │
│   └─────────────┘                   │
│                                      │
│   (Repeats until player quits)      │
└──────────────────────────────────────┘
```

This loop runs so fast (often 30–60 times per second) that it looks like smooth animation — just like a flipbook.

### Why Do We Need a Game Loop?

Without a game loop, your program would:
- Draw something once and then stop
- Never respond to keyboard presses
- Freeze immediately

The game loop keeps everything alive and responsive.

---

## Step-by-Step Instructions

### Step 1: Create Your Pygame Sandbox

1. Go to [codehs.com/sandbox](https://codehs.com/sandbox)
2. Scroll to the **Python** section
3. Click **Pygame** → **Create New**
4. You should see `main.py` open in the editor on the left

### Step 2: Clear the Default Code

CodeHS may put some starter code in `main.py`. **Select all** (Ctrl+A or Cmd+A) and **delete it**. We are starting fresh.

### Step 3: Import PyGame

Type this at the very top of your file:

```python
import pygame
```

This line tells Python: "I want to use the PyGame toolbox."

### Step 4: Initialize PyGame

Add this line below the import:

```python
pygame.init()
```

`pygame.init()` starts up all the PyGame systems (graphics, sound, etc.). You must call this before using any other PyGame feature.

### Step 5: Create the Game Window

Add these lines:

```python
# Game window settings
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")
```

This creates a window that is 600 pixels wide and 400 pixels tall, with "Snake Game" in the title bar.

### Step 6: Set Up a Colour

Add this line:

```python
# Colours (Red, Green, Blue)
BLACK = (0, 0, 0)
```

Colours in PyGame are written as **(Red, Green, Blue)** values from 0 to 255. `(0, 0, 0)` means no red, no green, no blue — that makes **black**.

### Step 7: Write the Game Loop

Now add the game loop:

```python
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
    pygame.display.update()

# Quit PyGame
pygame.quit()
```

### Step 8: Run Your Program

Click the green **▶ Run** button at the top of CodeHS. You should see a **black window** appear in the output panel with "Snake Game" as the title.

To close it, click the **■ Stop** button or close the output window.

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

# Colours (Red, Green, Blue)
BLACK = (0, 0, 0)

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
    pygame.display.update()

# Quit PyGame
pygame.quit()
```

---

## Code Walkthrough

### `import pygame`
Loads the PyGame library so we can use its functions.

### `pygame.init()`
Starts all PyGame modules. Always call this first.

### `WINDOW_WIDTH = 600` and `WINDOW_HEIGHT = 400`
Constants that define the size of our game window in pixels. We use ALL_CAPS names for values that never change (this is a Python convention called a "constant").

### `window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))`
Creates the game window. Notice the **double parentheses** — `set_mode()` takes a **tuple** `(width, height)` as its argument.

### `pygame.display.set_caption("Snake Game")`
Sets the text shown in the window's title bar.

### `BLACK = (0, 0, 0)`
Defines a colour. PyGame uses RGB (Red, Green, Blue) tuples. Each value ranges from 0 (none) to 255 (maximum).

| Colour | RGB Value |
|--------|-----------|
| Black | (0, 0, 0) |
| White | (255, 255, 255) |
| Red | (255, 0, 0) |
| Green | (0, 255, 0) |
| Blue | (0, 0, 255) |

### `running = True`
A **flag variable** that controls whether the game loop continues. When we set it to `False`, the loop ends and the game closes.

### `while running:`
The game loop! This block repeats until `running` becomes `False`.

### `for event in pygame.event.get():`
Every frame, PyGame collects a list of **events** — things that happened (keyboard press, mouse click, window close, etc.). This `for` loop checks each one.

### `if event.type == pygame.QUIT:`
`pygame.QUIT` is the event generated when the player clicks the window's close button. When we detect it, we set `running = False` to exit the loop.

### `window.fill(BLACK)`
Fills the entire window with black. We do this every frame to "erase" the previous frame before drawing the new one.

### `pygame.display.update()`
Shows everything we have drawn. Without this line, nothing would appear on screen. Think of it as "flipping the page" to reveal what you just drew.

### `pygame.quit()`
Cleanly shuts down PyGame after the loop ends. Always include this at the end.

---

## Expected Output

When you run the program, you should see:
- A **600×400 pixel black window** in the CodeHS output panel
- The title "Snake Game" in the window bar (may not be visible depending on CodeHS display)
- The window stays open until you click Stop

If nothing appears, make sure you selected the **Pygame** sandbox type (not Python 3).

---

## Common Mistakes

| Mistake | Error You See | Fix |
|---------|--------------|-----|
| Forgot `pygame.init()` | `pygame.error: video system not initialized` | Add `pygame.init()` before creating the window |
| Single parentheses in `set_mode` | `TypeError: argument 1 must be 2-item sequence` | Use double parentheses: `set_mode((600, 400))` |
| Misspelled `pygame` | `ModuleNotFoundError: No module named 'pygam'` | Check your spelling |
| Missing `pygame.display.update()` | Black screen, nothing visible | Add `pygame.display.update()` inside the loop |
| No event loop | Window freezes and becomes unresponsive | Add the `for event in pygame.event.get()` loop |
| Used Python 3 sandbox instead of Pygame | `ModuleNotFoundError: No module named 'pygame'` | Create a new sandbox using the **Pygame** tile |

---

## Debugging Tips

1. **Read error messages from the bottom up** — the last line tells you what went wrong, and the lines above show where.
2. **Check your indentation** — Python cares about whitespace. Code inside the `while` loop must be indented one level (4 spaces).
3. **Run after every small change** — if you write 20 lines and then run, it is harder to find which line caused the error.
4. **Compare to the complete code** — look character by character for differences.

---

## Review Questions

1. What does `pygame.init()` do, and why must it come before other PyGame code?
2. Why do we use a `while` loop for the game loop instead of an `if` statement?
3. What would happen if you removed `window.fill(BLACK)` from the loop?
4. What is the purpose of `pygame.display.update()`?
5. What event type do we check to know when the player wants to close the window?

---

## Practice Exercises

### Exercise 1: Change the Window Size
Modify `WINDOW_WIDTH` and `WINDOW_HEIGHT` to make the window:
- a) 800×600 pixels (larger)
- b) 400×400 pixels (square)

Run the program after each change and observe the difference.

### Exercise 2: Change the Background Colour
Create a new colour constant and use it in `window.fill()`:
- Try `DARK_GREEN = (0, 100, 0)` for a classic Snake background
- Try `NAVY = (0, 0, 128)` for a dark blue background

### Exercise 3: Add a Print Statement
Add `print("Game loop running")` inside the `while` loop (before `window.fill`). Run the program and look at the console output. How many times does it print? Why?

---

## Extension Challenge

Create a program that **changes the background colour every second**, cycling between 3 different colours. Hint: You'll need `pygame.time.get_ticks()` which returns the number of milliseconds since PyGame started.

---

## Teacher Notes

**Time Estimate**: 20–30 minutes

**Key Misconceptions**:
- Students often forget the double parentheses in `set_mode((width, height))`. Emphasize that `set_mode` expects a single tuple argument.
- Some students will not understand why we need `window.fill()` every frame. Demonstrate by commenting it out in a later lesson when there are moving objects — they will see "trails."
- The concept of a game loop running continuously may be confusing for students used to programs that run top-to-bottom and stop. Relate it to animation: "It's like drawing a new picture 60 times per second."

**Assessment Checklist**:
- [ ] Student can create a Pygame sandbox in CodeHS
- [ ] Student can explain the three parts of a game loop
- [ ] Student's program runs without errors
- [ ] Student can modify the window size and background colour

**Common Support Needed**:
- Students selecting the wrong sandbox type (Python 3 instead of Pygame)
- Indentation errors inside the while loop
- Forgetting to call `pygame.quit()` (program may not terminate cleanly)

---

## What's Next?

In **Lesson 2**, we will learn how to draw shapes on screen and create the snake! You will learn about coordinates, rectangles, and how to represent the snake as a Python list.

[→ Continue to Lesson 2: Drawing the Snake](Lesson-02-Drawing-the-Snake.md)
