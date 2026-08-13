# Lesson 3 – Pipes, Collisions & Scoring

## Spawning Things Over Time

Pipes need to appear at a steady interval, not all at once and not only on the first frame. The usual pattern for "do this every so often" is a counter that increases every frame, checked against a target: once the counter reaches the target, do the thing and reset the counter back to zero.

```python
timer += 1
if timer >= interval:
    timer = 0
    # spawn something here
```

At 60 frames per second, a `SPAWN_INTERVAL` of 90 means a new pipe roughly every 1.5 seconds. This same pattern works for anything that needs to happen periodically rather than once.

## One Gap, Two Rectangles

A pipe isn't really one shape, it's a gap in a wall: a solid block above the gap, and a solid block below it. Rather than storing both blocks separately, it's simpler to store a **single number**, the y-position where the gap starts, and work out both rectangles from it whenever you need them:
- The top block runs from `y = 0` down to the gap's start
- The bottom block runs from the gap's end down to the bottom of the window

Store each pipe as `[x, gap_y]`: the gap's horizontal position and where its vertical gap begins. Everything else about its shape can be calculated from those two numbers plus some fixed constants (pipe width, gap height).

## Rectangle Collision

To check whether the bird has hit a pipe, build a rectangle for the bird and rectangles for both the top and bottom blocks of each pipe, then ask whether the bird's rectangle overlaps either one. `pygame.Rect(x, y, width, height)` creates a rectangle, and `rect1.colliderect(rect2)` returns `True` if two rectangles touch.

## Scoring by Passing, Not Hitting

Unlike destroying an enemy, scoring here isn't about a collision at all, it's about **successfully avoiding** one. A pipe should award a point the moment it's fully behind the bird (its right edge has scrolled past the bird's position), regardless of whether the bird is near the top or bottom of the gap.

The tricky part: without tracking whether a pipe has already been scored, it would keep being "behind the bird" every single frame after that point, awarding a point 60 times a second forever. The fix is to store a third value per pipe, a flag for whether it's already been counted, so each pipe only ever scores once: `[x, gap_y, scored]`.

## Cleaning Up Off-Screen Pipes

Once a pipe has scrolled fully off the left edge of the screen, it's no longer useful and should be removed from the list, the same list-rebuilding pattern as anywhere else you've removed items based on a condition: build a fresh list containing only the pipes that are still on screen.

## Check Your Understanding

- Why store one gap position per pipe instead of two separate rectangles?
- Without the "already scored" flag, what would go wrong with the score?

---

Ready to put this into practice? Head to [Lesson 3 Task – Pipes, Collisions & Scoring](../Tutorial/Lesson-03-Pipes-Collisions-Scoring-Task.md).
