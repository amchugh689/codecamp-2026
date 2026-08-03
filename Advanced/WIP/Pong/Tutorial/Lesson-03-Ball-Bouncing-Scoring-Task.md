# Lesson 3 Task – Ball, Bouncing & Scoring

Builds on: [Lesson 3 – Ball, Bouncing & Scoring](../Lesson/Lesson-03-Ball-Bouncing-Scoring.md)

## What You'll Build

A ball that moves on its own, bounces off the top, bottom and right walls and off your paddle, plus a score that resets when you miss.

## Task 1: Set the Ball Moving

Add these below your ball's starting position:

```python
ball_dx = 4
ball_dy = 4
```

Then, inside the loop (after the keyboard-reading code from Lesson 2), add:

```python
    ball_x += ball_dx
    ball_y += ball_dy
```

Run it. The ball should drift off the bottom-right of the screen and keep going forever (PyGame just won't draw it once it's off-screen).

## Task 2: Bounce Off Top, Bottom and Right

Add this straight after the two lines that move the ball:

```python
    if ball_y <= 0 or ball_y >= WINDOW_HEIGHT - BALL_SIZE:
        ball_dy = -ball_dy

    if ball_x >= WINDOW_WIDTH - BALL_SIZE:
        ball_dx = -ball_dx
```

Run it. The ball should now bounce off the top, bottom and right edges, like it's in a box that's open on the left.

## Task 3: Bounce Off the Paddle and Score

Add this after the wall-bounce code:

```python
    paddle_rect = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball_rect = pygame.Rect(ball_x, ball_y, BALL_SIZE, BALL_SIZE)

    if paddle_rect.colliderect(ball_rect) and ball_dx < 0:
        ball_dx = -ball_dx
```

Run it. Move your paddle in front of the ball; it should bounce back to the right. (Remember the `and ball_dx < 0` check from the concepts page: that's what's preventing the ball from getting stuck.)

Now let's track a score. Add this near your other setup code, outside the loop:

```python
font = pygame.font.SysFont(None, 36)
score = 0
```

Then increase the score inside the paddle-bounce check, so it reads:

```python
    if paddle_rect.colliderect(ball_rect) and ball_dx < 0:
        ball_dx = -ball_dx
        score += 1
```

## Task 4: Display the Score

Add this with your other drawing code, after `window.fill(BLACK)`:

```python
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))
```

Run it. Your score should go up by 1 each time you hit the ball.

## Task 5: Detect a Miss and Reset

Add this after the paddle-bounce code:

```python
    if ball_x < 0:
        ball_x = WINDOW_WIDTH // 2
        ball_y = WINDOW_HEIGHT // 2
        ball_dx = 4
        ball_dy = 4
        score = 0
```

Run the full game. Try to keep the rally going as long as possible. Missing should snap the ball back to the centre and reset your score to 0.

## Self-Check

- [ ] The ball moves on its own and bounces off the top, bottom and right walls
- [ ] The ball bounces off your paddle when you're in the way
- [ ] Your score increases by 1 each time you hit the ball
- [ ] Missing the ball resets its position and your score

---

[← Back to Lesson 3 Concepts](../Lesson/Lesson-03-Ball-Bouncing-Scoring.md) | [→ Continue to Lesson 4: Extension Activities](../Lesson/Lesson-04-Extension-Activities.md)
