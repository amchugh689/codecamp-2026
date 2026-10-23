# Lesson 3 Task – Enemies, Collisions & Scoring

## What You'll Build

Enemies that march side to side and drop closer each time they hit an edge, bullets that destroy them, a score, and a message when you win or lose.

## Task 1: Move the Enemy Group

Add these near your enemy setup code:

```python
enemy_dx = 2
ENEMY_DROP = 20
```

Add this inside the game loop, after your bullet-movement code:

```python
    hit_edge = False
    for enemy in enemies:
        if (enemy_dx > 0 and enemy[0] >= WINDOW_WIDTH - ENEMY_WIDTH) or (enemy_dx < 0 and enemy[0] <= 0):
            hit_edge = True

    if hit_edge:
        enemy_dx = -enemy_dx
        for enemy in enemies:
            enemy[1] += ENEMY_DROP
    else:
        for enemy in enemies:
            enemy[0] += enemy_dx
```

The first loop checks every enemy before deciding anything, matching the concepts page: one shared decision, made after looking at the whole group.

Run it. The enemy grid should march sideways and step down each time it reaches an edge.

## Task 2: Bullets Destroy Enemies

Add the score variable near your other setup code, outside the loop, before you use it:

```python
font = pygame.font.SysFont(None, 36)
score = 0
```

Now add this after the enemy-movement code:

```python
    surviving_bullets = []
    for bullet in bullets:
        bullet_rect = pygame.Rect(bullet[0], bullet[1], BULLET_WIDTH, BULLET_HEIGHT)
        hit_enemy = None
        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy[0], enemy[1], ENEMY_WIDTH, ENEMY_HEIGHT)
            if bullet_rect.colliderect(enemy_rect):
                hit_enemy = enemy
                break
        if hit_enemy is not None:
            enemies.remove(hit_enemy)
            score += 1
        else:
            surviving_bullets.append(bullet)
    bullets = surviving_bullets
```

This builds a fresh `surviving_bullets` list, exactly as described in the concepts page: a bullet that hit something removes that enemy and isn't added to the survivors; a bullet that hit nothing carries on.

Draw the score with your other drawing code:

```python
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))
```

Run it. Shooting an enemy should remove it and increase your score by 1.

## Task 3: Win and Lose Conditions

Add these near your score variable:

```python
game_over = False
game_message = ""
```

Add this after the bullet-collision code:

```python
    for enemy in enemies:
        if enemy[1] + ENEMY_HEIGHT >= player_y:
            game_over = True
            game_message = "GAME OVER"

    if len(enemies) == 0:
        game_over = True
        game_message = "YOU WIN"
```

There are two places gameplay can still change after the game has ended, and both need to stop.

First, your Space-fire check from Lesson 2 lives inside the event loop, which runs every frame regardless of what else is gated. Update it to also require the game not being over, so it reads:

```python
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_over:
            bullets.append([player_x + PLAYER_WIDTH // 2 - BULLET_WIDTH // 2, player_y])
```

Second, everything else that updates the game each frame (ship movement, bullet movement and cleanup, enemy movement, collisions, and the win/lose checks you just added) needs wrapping in the same check. Starting from your ship-movement code (Task 1 of Lesson 2) through to the win/lose checks above, indent that whole block one level further, under:

```python
    if not game_over:
        # ...ship movement, bullet movement and cleanup, enemy movement,
        # collisions, and the win/lose checks, all indented under here...
```

Drawing should stay outside this check and keep running every frame, so the final state of the game (and the win/lose message) stays visible on screen once it ends.

Finally, draw the end message. Add this with your other drawing code, after drawing the score:

```python
    if game_over:
        message_text = font.render(game_message, True, WHITE)
        window.blit(message_text, (WINDOW_WIDTH // 2 - message_text.get_width() // 2, WINDOW_HEIGHT // 2))
```

Run the full game. Destroy every enemy to see "YOU WIN", or let the grid drop down far enough to see "GAME OVER". Either way, the game should freeze on that message instead of continuing.

## Self-Check

- The enemy grid marches side to side and drops down when it hits an edge
- Shooting an enemy removes it and increases your score
- Destroying every enemy shows "YOU WIN"
- Letting the enemies reach your ship's row shows "GAME OVER"
- Once the game ends, the ship, bullets and enemies stop responding or moving
