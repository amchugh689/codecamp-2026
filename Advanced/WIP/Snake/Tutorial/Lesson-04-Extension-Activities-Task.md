# Lesson 4 Task – Extension Activities

Start from your finished Lesson 3 code. Pick any extension below; they don't need to be done in order.

## Extension 1: Restart Without Re-running

Add a function near your other setup code, outside the loop, that resets every piece of state back to its starting values:

```python
def restart_game():
    global snake_list, dx, dy, score, move_timer, game_over
    snake_list = [[100, 100], [80, 100], [60, 100]]
    dx, dy = 1, 0
    score = 0
    move_timer = 0
    game_over = False
```

`global` is needed here because this function changes variables that were created outside it, rather than creating new local ones.

Add a check inside your event `for` loop that calls it when the game has ended and R is pressed:

```python
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and game_over:
            restart_game()
```

Run it. Let the game end, then press R. Everything should reset and play should continue as if the program had just started.

## Extension 2: Speed Ramp

Instead of a fixed `MOVE_INTERVAL`, tie it to the current score, for example:

```python
    current_interval = max(3, MOVE_INTERVAL - score // 3)
```

Use `current_interval` in place of `MOVE_INTERVAL` in your `if move_timer >= ...` check, so every 3 points makes the snake a little faster. The `max(3, ...)` stops it from becoming impossibly fast.

## Extension 3: Wrap-Around Edges

Replace your wall-collision check with wrap-around instead. Where you currently have:

```python
            if new_head[0] < 0 or new_head[0] >= WINDOW_WIDTH or new_head[1] < 0 or new_head[1] >= WINDOW_HEIGHT:
                game_over = True
```

Replace it with:

```python
            new_head[0] = new_head[0] % WINDOW_WIDTH
            new_head[1] = new_head[1] % WINDOW_HEIGHT
```

Leave your `elif new_head in snake_list:` self-collision check as it is. Run it and drive the snake off one edge of the screen; it should reappear on the opposite side instead of ending the game.

## Extension 4: Obstacles

Add a list of fixed obstacle positions near your other setup code:

```python
obstacle_list = [[300, 200], [320, 200], [340, 200]]
```

Draw them with your other drawing code:

```python
    for obstacle in obstacle_list:
        pygame.draw.rect(window, WHITE, (obstacle[0], obstacle[1], CELL_SIZE, CELL_SIZE))
```

Add a check alongside your self-collision check:

```python
            elif new_head in obstacle_list:
                game_over = True
```

## Extension 5: Sound Effects

Wrap sound loading in `try`/`except` so the game keeps working even if audio isn't available:

```python
try:
    pygame.mixer.init()
    eat_sound = pygame.mixer.Sound(buffer=bytearray(100))
    sound_enabled = True
except Exception:
    sound_enabled = False
```

Then only play a sound when `sound_enabled` is `True`, at the moment food is eaten or the game ends.

## Self-Check

- I picked at least one extension and got it working
- I tested my extension by actually playing the game, not just reading the code
- My game still runs without errors after adding it
