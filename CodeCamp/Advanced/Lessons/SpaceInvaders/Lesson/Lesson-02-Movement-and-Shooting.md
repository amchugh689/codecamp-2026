# Lesson 2 – Movement & Shooting

## Held Keys vs. Single Presses

Not all input should be treated the same way. Moving the ship should happen continuously while a key is held, which is what `pygame.key.get_pressed()` is for: it tells you what's held down right now, checked fresh every frame.

Firing a bullet is different. You want **one** bullet per press, not a stream of bullets for as long as the key is down. For that, you need to know the moment a key goes down, which is exactly what the event loop already gives you: `pygame.event.get()` reports an event with `event.type == pygame.KEYDOWN` the instant a key is pressed, once, no matter how long it's held afterward.

So: held keys for movement, a single event for firing. Same input system, two different tools depending on what you need.

## A List That Grows and Shrinks

The enemy grid from Lesson 1 is a list that's mostly static once built. Bullets are different: new ones get added while the game is running (every time you fire), and old ones need to be removed once they're no longer useful (once they fly off the top of the screen).

The pattern for "remove things that no longer qualify" is usually a fresh list built with a condition, rather than deleting items out of the list you're currently using:

```python
bullets = [bullet for bullet in bullets if bullet[1] > 0]
```

This keeps every bullet whose y-position is still greater than 0 (still on screen) and drops the rest. It reads as "bullets is now every bullet from the old bullets list, but only the ones where this condition is true."

## Check Your Understanding

- Why does movement use `pygame.key.get_pressed()` while firing uses an event instead?
- What would happen to the game over time if old bullets were never removed from the list?
