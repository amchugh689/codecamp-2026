# Lesson 1 – Getting Started

## The Game Loop, Quickly

Every PyGame program is built around a loop that repeats many times per second: check input, update state, draw the screen. A clock caps how many times per second that loop runs, so the game runs at the same speed regardless of how fast the computer is.

## Coordinates and Rectangles

PyGame draws using an (x, y) coordinate system where `(0, 0)` is the **top-left** corner, `x` increases to the right, and `y` increases **downward**. A rectangle is drawn from `(x, y, width, height)`: `x` and `y` give its top-left corner, and `width`/`height` give its size from there.

We'll use a plain rectangle for the bird. Simple shapes keep the focus on the logic rather than artwork, and they're easy to swap for an image later if you want to.

## A Fixed Horizontal Position

In this style of game, the bird doesn't actually move left or right at all: its x position stays fixed for the whole game. What looks like the bird "flying forward" is really everything else (the pipes, in Lesson 3) scrolling past it in the opposite direction. Only the bird's y position ever changes, which is what Lesson 2 is about.

## Check Your Understanding

- If the bird's x position never changes, what has to move instead to create the illusion of forward flight?
- Which coordinate, x or y, will Lesson 2 be concerned with changing?
