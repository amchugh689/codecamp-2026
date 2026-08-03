# Lesson 1 – Getting Started

## The Game Loop

Every video game runs a **game loop**: a block of code that repeats over and over, many times per second. Each pass through the loop, the game:

1. Checks for input
2. Updates the game state
3. Draws everything

Without a loop like this, a program would draw one frame and stop. The loop is what keeps a game window open, responsive, and animated instead of freezing after a single frame.

Because it runs so many times per second, we also need a way to control *how fast* it runs; otherwise the game would run at wildly different speeds on different computers. PyGame gives us a clock for this, which we ask to "tick" a fixed number of times per second (its **frame rate**, usually written as FPS).

## The Coordinate System

PyGame draws to the screen using an **(x, y) coordinate system**, but it's not quite the one from maths class:

- `(0, 0)` is the **top-left** corner, not the centre
- `x` increases to the right, same as you'd expect
- `y` increases **downward**, the opposite of a maths graph

So a point at `(200, 150)` is 200 pixels from the left edge and 150 pixels down from the top.

## Drawing Shapes

PyGame can draw basic shapes directly onto the window. Two we'll use throughout this game:

- A **rectangle**, defined by an `(x, y, width, height)` box: good for paddles
- An **ellipse**, drawn inside a bounding box the same way: good for a round ball

Both need to know which surface to draw on (our window), what colour to use, and where and how big to draw.

## Check Your Understanding

- Why does a program need a loop to keep a window open and responsive?
- If `y` increases downward, is a shape at `y = 50` nearer the top or bottom of the window than one at `y = 200`?

---

Ready to put this into practice? Head to [Lesson 1 Task – Getting Started](../Tutorial/Lesson-01-Getting-Started-Task.md).
