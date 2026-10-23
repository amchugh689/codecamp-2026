# Lesson 2 – Movement

## Direction as Two Numbers

Rather than separate logic for "moving up," "moving down," "moving left," and "moving right," it's simpler to store direction as a pair of numbers, `dx` and `dy`, meaning how many cells to move on each axis per step. Moving right is `(1, 0)`, moving down is `(0, 1)`, moving left is `(-1, 0)`, and so on. One set of movement code can then handle every direction, just by using whatever `dx` and `dy` currently are.

## Moving a List-Based Body

A snake doesn't move by shifting every segment individually. Instead: work out where a new head would go (the old head's position, plus the current direction), add that new head to the front of the list, and remove the last segment from the back. The middle segments never move directly, they just end up one position further along because everything shifted by exactly one slot.

This is also exactly how growing will work in Lesson 3: skip removing the tail just once, and the snake is permanently one segment longer.

## Moving on a Timer, Not Every Frame

The game loop runs 60 times a second, but a snake that moved a full cell every single frame would be unplayably fast. Movement needs to happen on its own slower schedule: a counter that increases every frame, and only once it reaches a target does the snake actually take a step (then the counter resets to zero). This decouples how fast the snake moves from how fast the loop runs, so input still gets checked every frame even though the snake itself moves more slowly.

## Changing Direction Safely

Direction changes should happen once per key press, not continuously, so this belongs with single key-press events rather than held-key checks.

There's one rule classic Snake enforces that isn't obvious at first: you can't reverse directly into yourself. If you're moving right, pressing Left shouldn't be allowed, it would send the head straight into the segment right behind it. The usual trick: only allow a turn if it's on the *other* axis to your current direction. If `dy` is currently `0` (you're moving horizontally), you're allowed to start moving vertically, but not to flip `dx` from positive to negative directly.

## Check Your Understanding

- If `dx, dy = -1, 0`, which direction is the snake moving?
- Why does growing the snake later just mean skipping one step, rather than needing new movement code?
- Why can't you turn directly backward in classic Snake?
