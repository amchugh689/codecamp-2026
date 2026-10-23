# Lesson 3 – Food, Eating & Losing

## Random Positions, Snapped to the Grid

Food needs a random position, but it still has to land exactly on a grid cell, the same rule that applies to everything else in this game. The trick: pick a random **cell**, not a random pixel. Choosing a random whole number of cells across and down, then multiplying each by `CELL_SIZE`, always lands on a valid grid position, the same way the snake's segments do.

## Eating: Skipping the Tail Removal

In Lesson 2, moving worked by adding a new head and removing the tail, keeping the length the same. Eating changes exactly one thing: when the new head's position matches the food's position, skip the tail removal for that one step. The snake ends up one segment longer, permanently, with no other change needed to how it moves.

## Two Ways to Lose

Classic Snake ends the game in two situations, both checked against the snake's new head position before it actually moves there:
- **Hitting a wall**: the new head would land outside the window's boundaries.
- **Hitting itself**: the new head's position already matches somewhere else in the snake's own body.

Checking "does this position already appear in the list" is a single membership check, exactly the same idea as checking whether food's position matches the head, just applied to the whole body instead of one point.

There's a subtlety worth catching before it becomes a confusing bug: on a normal (non-eating) move, the tail is about to be removed this same step, so the new head landing exactly on the *current* tail position isn't really a collision, that cell is vacating as the snake moves. This comes up often once the snake is long enough to loop back on itself. The tail only needs to be excluded from the check when the tail is actually about to move; if the snake is eating instead, the tail stays put that step, so landing on it while growing is still a genuine collision.

## Stopping the Game Cleanly

Once either loss condition is true, everything that changes the game state (movement, direction changes) needs to stop, while drawing keeps running so the final position and a "Game Over" message stay visible. That means every place state could change needs to check the same flag: not just the movement code, but also the key-press handler that changes direction, since that runs in a different part of the loop and won't automatically be covered by wrapping only one of the two.

## Check Your Understanding

- Why multiply a random cell index by `CELL_SIZE` instead of picking a random pixel directly?
- What's the one difference between "moving" and "eating" in terms of what happens to the tail?
- Why should the tail be left out of the self-collision check on a normal move, but not on a move where the snake eats?
- Why does the direction-change key handler need its own check for whether the game has ended, rather than relying on the movement code being gated?
