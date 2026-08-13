# Lesson 4 Task – Extension Activities

Builds on: [Lesson 4 – Extension Activities](../Lesson/Lesson-04-Extension-Activities.md)

Start from your finished Lesson 3 code. Pick any extension below; they don't need to be done in order, except that Extension 2 (High Score) assumes Extension 1 (Restart) is done first.

## Extension 1: Restart Without Re-running

Add a function near your other setup code, outside the loop, that resets every piece of state back to its starting values:

```python
def restart_game():
    global bird_y, bird_velocity_y, pipes, score, spawn_timer, game_over
    bird_y = WINDOW_HEIGHT // 2
    bird_velocity_y = 0
    pipes = []
    score = 0
    spawn_timer = 0
    game_over = False
```

`global` is needed here because this function changes variables that were created outside it, rather than creating new local ones.

Add a check inside your event `for` loop that calls it when the game has ended and R is pressed:

```python
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and game_over:
            restart_game()
```

Run it. Let the game end, then press R. Everything should reset and play should continue as if the program had just started.

## Extension 2: A High Score

Add this near your other setup code, outside the loop, and outside `restart_game()` (it should NOT be reset when the game restarts):

```python
high_score = 0
```

Update it the moment the game ends. Wherever your code sets `game_over = True` (there are a few places: hitting a pipe, flying off the top or bottom), add:

```python
high_score = max(high_score, score)
```

Draw it alongside your score:

```python
    high_score_text = font.render("Best: " + str(high_score), True, WHITE)
    window.blit(high_score_text, (WINDOW_WIDTH - high_score_text.get_width() - 10, 10))
```

## Extension 3: Difficulty Ramp

Instead of a fixed `PIPE_SPEED`, tie the pipes' speed to the current score, for example:

```python
    current_pipe_speed = PIPE_SPEED + score // 5
```

Use `current_pipe_speed` in place of `PIPE_SPEED` wherever pipes move, so every 5 points makes the pipes a little faster.

## Extension 4: A Second Way to Fly

Instead of (or alongside) the tap-to-flap control, try a hold-to-rise control using held keys:

```python
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird_velocity_y -= 1
```

Placed alongside your gravity code, this pulls the velocity upward a little every frame Space is held, while gravity keeps pulling it back down, giving a floatier feel than the instant flap. You'll likely want to cap how negative `bird_velocity_y` can get, so it doesn't rise forever.

## Extension 5: Sound Effects

Wrap sound loading in `try`/`except` so the game keeps working even if audio isn't available:

```python
try:
    pygame.mixer.init()
    flap_sound = pygame.mixer.Sound(buffer=bytearray(100))
    sound_enabled = True
except Exception:
    sound_enabled = False
```

Then only play a sound when `sound_enabled` is `True`, at the moment the bird flaps or hits something.

## Self-Check

- [ ] I picked at least one extension and got it working
- [ ] I tested my extension by actually playing the game, not just reading the code
- [ ] My game still runs without errors after adding it

---

[← Back to Lesson 4 Concepts](../Lesson/Lesson-04-Extension-Activities.md) | [← Back to Series Overview](../README.md)
