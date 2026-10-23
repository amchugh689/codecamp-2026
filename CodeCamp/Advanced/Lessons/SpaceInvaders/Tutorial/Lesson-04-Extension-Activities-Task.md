# Lesson 4 Task – Extension Activities

Start from your finished Lesson 3 code. Pick any extension below; they don't need to be done in order, except that Extension 2 (Lives) assumes Extension 1 (Return Fire) is done first.

## Extension 1: Enemy Return Fire

Add these near your other bullet constants:

```python
ENEMY_BULLET_WIDTH = 4
ENEMY_BULLET_HEIGHT = 10
ENEMY_BULLET_SPEED = 5
enemy_bullets = []
```

Add this inside your `if not game_over:` block, after the enemy-movement code. It gives a roughly 1-in-60 chance each frame (about once a second at 60 FPS) that a random enemy fires:

```python
    if enemies and random.randint(1, 60) == 1:
        shooter = random.choice(enemies)
        enemy_bullets.append([shooter[0] + ENEMY_WIDTH // 2, shooter[1] + ENEMY_HEIGHT])
```

You'll need `import random` at the top of your file if you don't already have it.

Move and clean up enemy bullets the same way you did for the player's:

```python
    for bullet in enemy_bullets:
        bullet[1] += ENEMY_BULLET_SPEED
    enemy_bullets = [b for b in enemy_bullets if b[1] < WINDOW_HEIGHT]
```

Check whether an enemy bullet has hit the player, using the same rectangle-collision pattern from Lesson 3:

```python
    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    surviving_enemy_bullets = []
    for bullet in enemy_bullets:
        bullet_rect = pygame.Rect(bullet[0], bullet[1], ENEMY_BULLET_WIDTH, ENEMY_BULLET_HEIGHT)
        if bullet_rect.colliderect(player_rect):
            game_over = True
            game_message = "GAME OVER"
        else:
            surviving_enemy_bullets.append(bullet)
    enemy_bullets = surviving_enemy_bullets
```

Draw the enemy bullets with your other drawing code:

```python
    for bullet in enemy_bullets:
        pygame.draw.rect(window, WHITE, (bullet[0], bullet[1], ENEMY_BULLET_WIDTH, ENEMY_BULLET_HEIGHT))
```

## Extension 2: Lives Instead of One Hit

Instead of ending the game on the first enemy bullet, give the player a few chances. Add near your score variable:

```python
lives = 3
```

Change the enemy-bullet-hits-player check from Extension 1 so it reads:

```python
        if bullet_rect.colliderect(player_rect):
            lives -= 1
            if lives <= 0:
                game_over = True
                game_message = "GAME OVER"
        else:
            surviving_enemy_bullets.append(bullet)
```

Draw the remaining lives alongside your score:

```python
    lives_text = font.render("Lives: " + str(lives), True, WHITE)
    window.blit(lives_text, (WINDOW_WIDTH - lives_text.get_width() - 10, 10))
```

## Extension 3: Difficulty Ramp

Base the enemies' speed on how many are left, instead of a fixed number. Where you currently set `enemy_dx = 2` at the start, leave that as the starting speed, then adjust the *size* of the move each frame based on the enemy count, for example:

```python
    speed_multiplier = 1 + (ENEMY_ROWS * ENEMY_COLS - len(enemies)) // 5
```

Multiply your enemy movement by `speed_multiplier` instead of moving by a fixed amount, so the fewer enemies remain, the faster they move.

## Extension 4: A Bonus UFO

Add a separate enemy that isn't part of the main grid: its own position, its own speed, and a random chance each frame (or every few hundred frames) that it appears at one edge of the screen and crosses to the other. Give it its own collision check against bullets, worth more points than a regular enemy.

## Extension 5: Barriers

Build a small grid of destructible blocks (the same nested-loop technique from Lesson 1) positioned between the player and the enemies. Give bullets from either side a collision check against these blocks, and remove a block once it's hit instead of removing an enemy or ending the game.

## Extension 6: Sound Effects

Wrap sound loading in `try`/`except` so the game keeps working even if audio isn't available:

```python
try:
    pygame.mixer.init()
    fire_sound = pygame.mixer.Sound(buffer=bytearray(100))
    sound_enabled = True
except Exception:
    sound_enabled = False
```

Then only play a sound when `sound_enabled` is `True`, at the moment a bullet is fired or an enemy is destroyed.

## Self-Check

- I picked at least one extension and got it working
- I tested my extension by actually playing the game, not just reading the code
- My game still runs without errors after adding it
