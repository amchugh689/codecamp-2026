# Lesson 4 Task – Extension Activities

Builds on: [Lesson 4 – Extension Activities](../Lesson/Lesson-04-Extension-Activities.md)

Start from your finished Lesson 3 code. Pick any extension below; they don't need to be done in order, except that Extension 1 changes code that some of the others build on.

## Extension 1: Turn the Wall into an AI Opponent

Add a second paddle near your existing paddle constants:

```python
opponent_x = WINDOW_WIDTH - 20 - PADDLE_WIDTH
opponent_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
OPPONENT_SPEED = 4
```

Move it toward the ball each frame. Add this near your paddle-movement code:

```python
    if opponent_y + PADDLE_HEIGHT // 2 < ball_y:
        opponent_y += OPPONENT_SPEED
    if opponent_y + PADDLE_HEIGHT // 2 > ball_y:
        opponent_y -= OPPONENT_SPEED
```

Draw it alongside your paddle:

```python
    pygame.draw.rect(window, WHITE, (opponent_x, opponent_y, PADDLE_WIDTH, PADDLE_HEIGHT))
```

Replace your right-wall bounce with a collision check against this paddle instead:

```python
    opponent_rect = pygame.Rect(opponent_x, opponent_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    if opponent_rect.colliderect(ball_rect) and ball_dx > 0:
        ball_dx = -ball_dx
```

Now a miss can happen on **either** side, so you'll need a second "miss" check for `ball_x > WINDOW_WIDTH`, and you may want two scores (yours and the opponent's) instead of one shared score.

Try adjusting `OPPONENT_SPEED`: too fast and it never misses, too slow and it's no challenge at all.

## Extension 2: Two-Player Mode

Give the second paddle its own set of keys instead of AI control (`pygame.K_w` and `pygame.K_s` are a common choice), using the same pattern as your Lesson 2 keyboard code.

## Extension 3: Angle the Bounce

Work out how far from the paddle's centre the ball hit, as a fraction from -1 (top edge) to +1 (bottom edge), and use that to set `ball_dy` when the bounce happens, so hits near the edges leave at a steeper angle than hits near the centre.

## Extension 4: Speed Up Over Time

Increase `ball_dx` and `ball_dy` slightly (keeping their signs) each time the ball bounces off a paddle, and reset them back to their starting values when someone misses.

## Extension 5: Win Condition

Add a target score (e.g. first to 5). When either score reaches it, stop updating the game and display a "You Win" or "Game Over" message instead. You'll need a state variable, similar in spirit to `running`, that switches drawing from the normal game view to an end screen.

## Extension 6: Sound Effects

Wrap sound loading in `try`/`except` so the game keeps working even if audio isn't available:

```python
try:
    pygame.mixer.init()
    hit_sound = pygame.mixer.Sound(buffer=bytearray(100))
    sound_enabled = True
except Exception:
    sound_enabled = False
```

Then only play a sound when `sound_enabled` is `True`, at the moment the ball hits a paddle or a point is scored.

## Make It Your Own

A few more ideas if you want to keep going, with no implementation steps provided; you're on your own for these:

- A ball that gets slightly bigger or changes colour every few hits
- A pause feature (press a key to freeze the game)
- An on-screen instructions or start screen before the rally begins

## Self-Check

- [ ] I picked at least one extension and got it working
- [ ] I tested my extension by actually playing the game, not just reading the code
- [ ] My game still runs without errors after adding it

---

[← Back to Lesson 4 Concepts](../Lesson/Lesson-04-Extension-Activities.md) | [← Back to Series Overview](../README.md)
