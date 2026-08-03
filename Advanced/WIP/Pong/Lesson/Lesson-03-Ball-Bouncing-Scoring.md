# Lesson 3 – Ball, Bouncing & Scoring

## Velocity

To make something move every frame, you give it a **velocity**: how far it moves on the x-axis and y-axis each frame. Add that to its position each time through the loop, and a velocity of `(4, 4)` means "move 4 pixels right and 4 pixels down, every frame."

## Bouncing

A "bounce" off a flat wall just means **reversing the direction** on one axis. Hit the top or bottom wall → flip the y-velocity. Hit a side wall → flip the x-velocity. The ball doesn't need to know anything about angles or physics; reversing a sign is enough to look like a bounce.

## Rectangle Collision

To bounce off a paddle, we first need to know *when* the ball and the paddle are touching. PyGame has a built-in way to check whether two rectangles overlap: `pygame.Rect(x, y, width, height)` creates a rectangle, and `rect1.colliderect(rect2)` returns `True` if the two rectangles touch.

This is much simpler than comparing every edge by hand, and it's the same technique used for collision detection in most simple 2D games.

One subtlety: a collision check on its own can't tell you *which way* the ball should bounce. For a paddle on the left side of the screen, we only want a bounce when the ball is moving toward it (leftward); otherwise a ball that's already moving away could get "caught" flipping direction every frame while it overlaps the paddle.

## Displaying Text

To draw text, you first create a **font** once (outside the loop) with `pygame.font.SysFont(None, size)`. Then, each frame, you render your text to an image with `font.render(text, True, colour)`, and draw that image onto the window with `window.blit(image, (x, y))`. Fonts are the same idea whether you're drawing a score, a title, or a "Game Over" message.

## Handling a Miss

When the ball gets past the paddle entirely, that's a miss: the point where a rally ends. The usual pattern is to check for this as its own condition (the ball's x position going past the edge of the screen) and, when it happens, reset the ball's position, velocity, and score back to their starting values, ready for the next rally.

## Check Your Understanding

- If a ball's velocity is `(3, -2)`, which direction is it moving?
- Why do we check the ball's direction (`ball_dx < 0`) as well as whether it's touching the paddle, before bouncing it?
- What are the three things you'd want to reset when a rally ends?

---

Ready to put this into practice? Head to [Lesson 3 Task – Ball, Bouncing & Scoring](../Tutorial/Lesson-03-Ball-Bouncing-Scoring-Task.md).
