# Lesson 1 – Getting Started

## The Game Loop, Quickly

Every PyGame program is built around a loop that repeats many times per second: check input, update state, draw the screen. A clock caps how many times per second that loop runs, so the game runs at the same speed regardless of how fast the computer is.

## Coordinates and Grids

PyGame draws using an (x, y) coordinate system where `(0, 0)` is the **top-left** corner, `x` increases to the right, and `y` increases **downward**.

Snake doesn't move pixel by pixel: it moves in fixed steps, one **cell** of a grid at a time. If each cell is 20 pixels wide, the snake's position always lands on a multiple of 20, never something like 137. Deciding on a cell size up front, and always moving by whole cells, is what gives Snake its blocky, grid-based feel rather than smooth pixel movement.

## The Snake as a List

The snake's body is a sequence of segments, and a list is the natural way to represent a sequence that needs to grow, shrink, and be looped over: something like `[[x1, y1], [x2, y2], [x3, y3]]`, one `[x, y]` pair per segment, with the **first item as the head** and the rest as the body trailing behind it.

Storing it this way (rather than separate variables for "segment 1," "segment 2," and so on) is what makes it possible to grow the snake by one segment later without changing how the rest of the code works: you're always just adding to or looping over the same list.

## Check Your Understanding

- If every cell is the same fixed width, is a snake segment at an arbitrary pixel position like `x = 137` possible? Why or why not?
- Why is a list a better fit for the snake's body than a separate variable per segment?
