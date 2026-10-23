# Lesson 3 – Enemies, Collisions & Scoring

## Moving a Group Together

Classic Space Invaders enemies don't move independently. They move as one block: step sideways together, and the instant any one of them touches the edge of the screen, the whole group reverses direction and drops down a row.

That means the direction is a single shared value (one `enemy_dx`, not one per enemy), and each frame needs to answer one question before moving anyone: **has any enemy in the list reached an edge?** Only after checking every enemy do you know whether to flip direction and drop, or carry on moving sideways as normal.

## Rectangle Collision

To know whether a bullet has hit an enemy, you need to check whether two rectangles overlap. PyGame has a built-in way to do this: `pygame.Rect(x, y, width, height)` creates a rectangle, and `rect1.colliderect(rect2)` returns `True` if the two rectangles touch. Build one rectangle for the bullet and one for each enemy, and ask whether they overlap. Much simpler than comparing every edge by hand.

## Checking Many Pairs Safely

A single collision check only ever involves one pair of rectangles. Here, every bullet potentially needs checking against every enemy, a list against a list. The safe way to remove things that get hit is the same list-rebuilding pattern from Lesson 2: rather than deleting a bullet or enemy out of a list while you're still looping over that same list (which can skip items or crash), build a fresh list of survivors and use that.

## Win and Lose Conditions

Right now there's no way for the game to end. Two conditions matter here:
- **Win**: every enemy has been destroyed. Since enemies live in a list, this is simply asking whether that list is now empty.
- **Lose**: an enemy has reached the player's row. This is a check on each enemy's y-position compared to the player's y-position, done every frame alongside everything else.

Once either happens, the usual approach is a single `game_over` flag: while it's `False`, the game updates normally; once it becomes `True`, you stop updating movement and collisions, and instead draw an end-of-game message.

## Check Your Understanding

- Why does the group need one shared direction variable instead of each enemy tracking its own?
- Why is rebuilding a list of survivors safer than removing items from a list while looping over it?
- What's the simplest way to check whether the player has destroyed every enemy?
