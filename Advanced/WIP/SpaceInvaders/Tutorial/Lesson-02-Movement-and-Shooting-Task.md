## What You'll Build

A ship you can move left and right, and bullets you can fire with the spacebar that travel up the screen and disappear once they leave it.

## Task 1: Move the Ship

Add a speed constant near your player constants:

```python
PLAYER_SPEED = 6
```

Then, inside the game loop, after the event `for` loop but before `window.fill(BLACK)`, add:

```python
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - PLAYER_WIDTH:
        player_x += PLAYER_SPEED
```

Run it. Holding Left or Right should move the ship smoothly, stopping at the edges of the window instead of sliding off.

## Task 2: Fire Bullets

Add bullet constants and an empty list to hold them, near your other setup code:

```python
BULLET_WIDTH = 4
BULLET_HEIGHT = 10
BULLET_SPEED = 8
bullets = []
```

Now add firing. Inside your event `for` loop (where you check for `pygame.QUIT`), add a check for the spacebar going down:

```python
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append([player_x + PLAYER_WIDTH // 2 - BULLET_WIDTH // 2, player_y])
```

This adds a new `[x, y]` bullet, centred on the ship's current position, every time Space is pressed (once per press, per the concepts page).

## Task 3: Move and Clean Up Bullets

Add this after your ship-movement code:

```python
    for bullet in bullets:
        bullet[1] -= BULLET_SPEED
    bullets = [b for b in bullets if b[1] > 0]
```

The first part moves every bullet upward. The second part keeps only the bullets still on screen, using the pattern from the concepts page.

## Task 4: Draw the Bullets

Add this with your other drawing code:

```python
    for bullet in bullets:
        pygame.draw.rect(window, WHITE, (bullet[0], bullet[1], BULLET_WIDTH, BULLET_HEIGHT))
```

Run the full game. Move your ship with the arrow keys and press Space to fire. You should see white bullets travel up the screen and vanish once they pass the top edge.

## Self-Check

- Holding Left or Right moves the ship, stopping at the window edges
- Pressing Space fires one bullet per press, not a continuous stream
- Bullets travel upward and disappear once they leave the screen
- Mashing Space repeatedly fires lots of bullets, and the game keeps running smoothly (a sign old bullets are actually being removed from the list, not just piling up off-screen)