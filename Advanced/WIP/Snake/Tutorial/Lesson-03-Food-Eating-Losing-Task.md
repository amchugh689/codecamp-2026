# Lesson 3 Task – Food, Eating & Losing

## What You'll Build

Food that makes the snake grow when eaten, a score, and wall/self-collision that ends the game.

Everything in this lesson's gameplay logic needs a `not game_over` check somewhere, since two different parts of the loop (the direction-change handler and the movement code) both change game state and both need to stop once the game ends. Task 3 below covers both explicitly.

## Task 1: Add Food

Add these near your other setup code:

```python
import random

GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

def spawn_food():
    food_x = random.randint(0, GRID_WIDTH - 1) * CELL_SIZE
    food_y = random.randint(0, GRID_HEIGHT - 1) * CELL_SIZE
    return [food_x, food_y]

food_position = spawn_food()
```

`import random` needs to go at the very top of your file, with your other imports. `spawn_food()` picks a random cell (not a random pixel) and converts it to a pixel position, per the concepts page.

Draw the food with your other drawing code:

```python
    pygame.draw.rect(window, RED, (food_position[0], food_position[1], CELL_SIZE, CELL_SIZE))
```

Run it. You should see a red square somewhere on the grid, alongside your moving snake.

## Task 2: Eating and Scoring

Add the score variable near your other setup code:

```python
font = pygame.font.SysFont(None, 36)
score = 0
```

Change your movement code from Lesson 2 so that eating grows the snake instead of always removing the tail:

```python
        snake_list.insert(0, new_head)
        if new_head == food_position:
            score += 1
            food_position = spawn_food()
        else:
            snake_list.pop()
```

This replaces the two lines `snake_list.insert(0, new_head)` and `snake_list.pop()` from Lesson 2 Task 1 with the version above: the insert always happens, but the pop only happens if the new head didn't land on the food.

Draw the score with your other drawing code:

```python
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))
```

Run it. Steer the snake onto the food. It should grow by one segment, your score should go up by 1, and a new piece of food should appear elsewhere.

## Task 3: Wall and Self-Collision

Add this near your score variable:

```python
game_over = False
```

First, update your direction-change handler from Lesson 2 Task 2 to also require the game not being over, since it runs in the event loop and needs its own check:

```python
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, 1
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -1, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = 1, 0
```

Second, update your movement code so it checks for a collision before moving into a new position, and wrap the whole thing (from Lesson 2 Task 1's `move_timer += 1` onward) under a single `if not game_over:`, so it reads:

```python
    if not game_over:
        move_timer += 1
        if move_timer >= MOVE_INTERVAL:
            move_timer = 0
            head = snake_list[0]
            new_head = [head[0] + dx * CELL_SIZE, head[1] + dy * CELL_SIZE]

            if new_head[0] < 0 or new_head[0] >= WINDOW_WIDTH or new_head[1] < 0 or new_head[1] >= WINDOW_HEIGHT:
                game_over = True
            else:
                is_eating = new_head == food_position
                body_to_check = snake_list if is_eating else snake_list[:-1]
                if new_head in body_to_check:
                    game_over = True
                else:
                    snake_list.insert(0, new_head)
                    if is_eating:
                        score += 1
                        food_position = spawn_food()
                    else:
                        snake_list.pop()
```

Notice the collision checks happen *before* the snake actually moves into the new position, per the concepts page: a colliding move never gets applied.

Also notice `body_to_check` leaves the tail segment out unless the snake is eating. That's deliberate, and it matters: if the move isn't an eat, the tail is about to be removed anyway (via `snake_list.pop()`), so the new head landing exactly on the current tail position is a legal move, not a collision, the tail moves out of the way in the same step. Checking against the full list including the tail would wrongly end the game the first time the snake loops back on itself, something that happens often once it's a few segments long. Eating is the one case where this doesn't apply, since the tail *isn't* removed that step, so landing on it while growing is still a real collision.

Drawing should stay outside this check and keep running every frame, so the snake's final position stays visible once the game ends. Add this with your other drawing code:

```python
    if game_over:
        message_text = font.render("GAME OVER", True, WHITE)
        window.blit(message_text, (WINDOW_WIDTH // 2 - message_text.get_width() // 2, WINDOW_HEIGHT // 2))
```

Run the full game. Try to grow as long as possible. Running into a wall or into your own body should freeze the snake in place and show "GAME OVER", and the arrow keys should no longer do anything once that happens.

## Self-Check

- Eating food grows the snake and increases your score
- A new piece of food appears after each one is eaten
- Running into a wall ends the game
- Running into your own body ends the game
- Once the game ends, the arrow keys no longer change direction
