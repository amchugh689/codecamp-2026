# Lesson 2 Task – Gravity & Flapping

## What You'll Build

A bird that falls under gravity, flaps upward when you press Space, and ends the game if it flies off the top or bottom of the window.

## Task 1: Add Gravity

Add these constants near your bird setup code:

```python
bird_velocity_y = 0
GRAVITY = 0.5
```

Add this inside the game loop, after the event `for` loop but before `window.fill(BLACK)`:

```python
    bird_velocity_y += GRAVITY
    bird_y += bird_velocity_y
```

Run it. The bird should start falling slowly and speed up the longer it falls, matching the concepts page: velocity growing every frame, then applied to position.

## Task 2: Add Flapping

Add this constant near `GRAVITY`:

```python
FLAP_STRENGTH = -8
```

`FLAP_STRENGTH` is negative because upward on screen means a smaller y-value, per the coordinate system from Lesson 1.

Add this inside your event `for` loop, where you check for `pygame.QUIT`:

```python
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_velocity_y = FLAP_STRENGTH
```

Run it. Pressing Space should give the bird a quick upward push, which gravity then pulls back down again, exactly the "rise then fall" pattern from the concepts page.

## Task 3: End the Game at the Edges

Add these near your other setup code, outside the loop:

```python
font = pygame.font.SysFont(None, 36)
game_over = False
```

Add this after the gravity code:

```python
    if bird_y <= 0 or bird_y >= WINDOW_HEIGHT - BIRD_SIZE:
        game_over = True
```

Now wrap the gravity and flap-handling code so it stops running once the game has ended. First, update the flap check from Task 2 to also require the game not being over:

```python
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_over:
            bird_velocity_y = FLAP_STRENGTH
```

Then indent your gravity and boundary-check code (Tasks 1 and 3) under a single check:

```python
    if not game_over:
        bird_velocity_y += GRAVITY
        bird_y += bird_velocity_y

        if bird_y <= 0 or bird_y >= WINDOW_HEIGHT - BIRD_SIZE:
            game_over = True
```

Finally, draw an end message. Add this with your other drawing code, after drawing the bird:

```python
    if game_over:
        message_text = font.render("GAME OVER", True, WHITE)
        window.blit(message_text, (WINDOW_WIDTH // 2 - message_text.get_width() // 2, WINDOW_HEIGHT // 2))
```

Run the full game. Try to keep the bird on screen by flapping. Flying off the top or bottom should freeze the game and show "GAME OVER".

## Self-Check

- The bird falls under gravity, speeding up the longer it falls
- Pressing Space gives the bird a noticeable upward flap
- Flying off the top or bottom of the window ends the game and shows "GAME OVER"
- Once the game ends, pressing Space no longer does anything
