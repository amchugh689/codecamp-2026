# Lesson 1 – Getting Started

## The Game Loop, Quickly

Every PyGame program is built around a loop that repeats many times per second: check input, update state, draw the screen. A clock caps how many times per second that loop runs (its frame rate), so the game runs at the same speed regardless of how fast the computer is.

If this is new to you: nothing more to it than that for now, it'll make more sense once you see it running in Lesson 1's task.

## Coordinates and Rectangles

PyGame draws using an (x, y) coordinate system where `(0, 0)` is the **top-left** corner, `x` increases to the right, and `y` increases **downward**. A rectangle is drawn from `(x, y, width, height)`: `x` and `y` give its top-left corner, and `width`/`height` give its size from there.

We'll use plain rectangles for the player's ship, the enemies, and the bullets. Simple shapes keep the focus on the logic rather than artwork, and they're easy to swap for images later if you want to.

## Building a Grid with Nested Loops

Space Invaders enemies aren't placed one at a time; they're laid out in **rows and columns**, a grid. The natural way to build a grid in code is a loop inside a loop: the outer loop walks through each row, and the inner loop walks through each column within that row.

For a grid with `ROWS` rows and `COLS` columns, that looks like:

```python
for row in range(ROWS):
    for col in range(COLS):
        # this runs once for every (row, col) combination
```

Each pass through the inner loop can work out an x and y position from `row` and `col` (for example, `col` controls how far across, `row` controls how far down) and add that position to a list. By the time both loops finish, you have a full grid of positions built from just a few lines of code. Storing the enemies as a list of `[x, y]` positions like this is the same idea you'll reuse for the bullets you add in Lesson 2: a list of positions you can loop through, add to, and remove from.

## Check Your Understanding

- If `ROWS = 3` and `COLS = 5`, how many times does the inner loop's body run in total?
- Why is storing enemies as a list more useful here than creating a separate variable for each one?
