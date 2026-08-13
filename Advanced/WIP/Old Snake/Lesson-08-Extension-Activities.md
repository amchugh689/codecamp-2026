# Lesson 8 – Extension Activities

## Learning Objectives

By the end of this lesson, you will be able to:

- Add a difficulty selection menu to your game
- Track and display a high score
- Place obstacles on the game board
- Create animated food effects
- Add sound effects (where supported)
- Implement visual themes
- Create power-up items with timed effects

---

## Overview

This lesson is different from the others. Instead of building one feature together, you have **seven independent extension activities** to choose from. Each one adds a new feature to your Lesson 7 game.

Pick the ones that interest you most! You can do them in any order, and you can combine multiple extensions into one game.

**Start with your complete code from Lesson 7.** Each extension below explains what to add and where to add it.

---

## Extension 1: Difficulty Settings

### What You'll Build
A start screen that lets the player choose Easy, Medium, or Hard before playing. Each difficulty changes the starting speed.

### New Concepts
- **Menu state**: A new game state before playing starts
- **Multiple options**: Using number keys to select

### Implementation

Add a new game state and difficulty variable before the game loop:

```python
# Difficulty settings
EASY_SPEED = 8
MEDIUM_SPEED = 12
HARD_SPEED = 18

# Game states: "menu", "playing", "game_over"
game_state = "menu"
base_speed = MEDIUM_SPEED
```

Add the menu drawing function:

```python
def draw_menu():
    """Draw the difficulty selection menu."""
    window.fill(BLACK)

    title = font.render("SNAKE", True, GREEN)
    easy = font.render("1 - Easy", True, WHITE)
    medium = font.render("2 - Medium", True, WHITE)
    hard = font.render("3 - Hard", True, WHITE)

    window.blit(title, (WINDOW_WIDTH // 2 - title.get_width() // 2, 80))
    window.blit(easy, (WINDOW_WIDTH // 2 - easy.get_width() // 2, 180))
    window.blit(medium, (WINDOW_WIDTH // 2 - medium.get_width() // 2, 230))
    window.blit(hard, (WINDOW_WIDTH // 2 - hard.get_width() // 2, 280))

    pygame.display.update()
```

Add key handling for the menu in your event loop:

```python
            if game_state == "menu":
                if event.key == pygame.K_1:
                    base_speed = EASY_SPEED
                    game_state = "playing"
                elif event.key == pygame.K_2:
                    base_speed = MEDIUM_SPEED
                    game_state = "playing"
                elif event.key == pygame.K_3:
                    base_speed = HARD_SPEED
                    game_state = "playing"
```

Update your speed calculation:

```python
    current_speed = base_speed + (score // 3)
    clock.tick(current_speed)
```

Update your main game loop structure to include the menu state:

```python
    if game_state == "menu":
        draw_menu()
    elif game_state == "playing":
        # ... existing playing code ...
    elif game_state == "game_over":
        # ... existing game over code ...
```

When restarting, go back to the menu:

```python
    game_state = "menu"
```

### Expected Result
- Game starts with a menu showing Easy/Medium/Hard
- Pressing 1, 2, or 3 starts the game at different speeds
- After Game Over and restart, the menu appears again

---

## Extension 2: High Score

### What You'll Build
Track the highest score achieved during the current session. Display it on the Game Over screen and during gameplay.

### New Concepts
- **Persistent variable**: A value that survives game restarts (within the same session)
- **`max()` function**: Finds the larger of two values

### Implementation

Add a high score variable before the game loop (this is NOT reset on restart):

```python
# High score (persists across restarts)
high_score = 0
```

Update the high score when the game ends. Add this where `game_over = True` is set:

```python
        if check_wall_collision(snake_list[0]):
            game_over = True
            high_score = max(high_score, score)
        if check_self_collision(snake_list):
            game_over = True
            high_score = max(high_score, score)
```

Display during gameplay (add after drawing the score):

```python
def draw_high_score(current_high):
    """Draw the high score in the top-right corner."""
    high_text = font.render("Best: " + str(current_high), True, WHITE)
    window.blit(high_text, (WINDOW_WIDTH - high_text.get_width() - 10, 10))
```

Display on the Game Over screen:

```python
        high_text = font.render("High Score: " + str(high_score), True, WHITE)
        window.blit(high_text, (WINDOW_WIDTH // 2 - high_text.get_width() // 2, 210))
```

**Important**: Do NOT reset `high_score` in the restart logic. It should persist.

### Expected Result
- "Best: X" shows in the top-right during gameplay
- Game Over screen shows the all-time high score
- High score persists across multiple games (but resets when you stop the program)

### Limitations in CodeHS
The high score cannot be saved between program runs (no file I/O in Pygame sandbox for persistence). It resets when you click Stop and Run again. This is normal for browser-based environments.

---

## Extension 3: Obstacles

### What You'll Build
Walls or blocks placed on the game board that the snake must avoid. Obstacles increase as the score grows.

### New Concepts
- **List of obstacles**: A list of `[x, y]` positions that kill the snake
- **Dynamic difficulty**: More obstacles appear as you score

### Implementation

Add obstacle colour and list:

```python
BLUE = (50, 50, 200)
obstacle_list = []
```

Create a function to add obstacles:

```python
def add_obstacle(snake, food, obstacles):
    """Add a new obstacle that doesn't overlap snake, food, or other obstacles."""
    attempts = 0
    while attempts < 100:
        position = spawn_food()
        if (position not in snake and
                position != food and
                position not in obstacles):
            return position
        attempts = attempts + 1
    return None  # Could not find a valid position
```

Every 5 points, add a new obstacle. In your eating logic:

```python
        if snake_list[0] == food_position:
            score = score + 1
            food_position = spawn_food_safe(snake_list)
            # Add obstacle every 5 points
            if score % 5 == 0:
                new_obstacle = add_obstacle(snake_list, food_position, obstacle_list)
                if new_obstacle is not None:
                    obstacle_list.append(new_obstacle)
```

Draw obstacles:

```python
def draw_obstacles(obstacles):
    """Draw all obstacles as blue squares."""
    for obs in obstacles:
        pygame.draw.rect(window, BLUE, (obs[0], obs[1], CELL_SIZE, CELL_SIZE))
```

Check obstacle collision (add after wall/self-collision checks):

```python
        if snake_list[0] in obstacle_list:
            game_over = True
```

Reset obstacles on restart:

```python
    obstacle_list = []
```

### Expected Result
- Every 5 points, a blue block appears on the board
- Hitting a blue block ends the game
- The board gets more dangerous over time

---

## Extension 4: Animated Food

### What You'll Build
Food that pulses (grows and shrinks) or changes colour to draw the player's attention.

### New Concepts
- **Animation frames**: Changing appearance over time
- **Sine wave or counter**: Creating smooth pulsing effects
- **`pygame.time.get_ticks()`**: Getting the current time for animation

### Implementation — Colour Cycling

Make food cycle through colours using time:

```python
def draw_food_animated(position):
    """Draw food with colour cycling animation."""
    # Get time in milliseconds
    ticks = pygame.time.get_ticks()

    # Cycle through colours (changes every 200ms)
    cycle = (ticks // 200) % 3
    if cycle == 0:
        colour = (255, 50, 50)   # Red
    elif cycle == 1:
        colour = (255, 150, 50)  # Orange
    else:
        colour = (255, 255, 50)  # Yellow

    pygame.draw.rect(window, colour, (position[0], position[1], CELL_SIZE, CELL_SIZE))
```

### Implementation — Pulsing Size

Make food grow and shrink:

```python
def draw_food_pulsing(position):
    """Draw food that pulses in size."""
    ticks = pygame.time.get_ticks()

    # Calculate size offset (oscillates between -4 and +4)
    import math
    offset = int(math.sin(ticks / 200) * 4)
    size = CELL_SIZE + offset

    # Centre the food in its cell
    x = position[0] + (CELL_SIZE - size) // 2
    y = position[1] + (CELL_SIZE - size) // 2

    pygame.draw.rect(window, RED, (x, y, size, size))
```

Replace `draw_food(food_position)` with either animated version in your drawing code.

### Expected Result
- Food visually pulses or changes colour, making it more engaging
- No gameplay change — just visual polish

---

## Extension 5: Sound Effects

### What You'll Build
Sound effects for eating food, dying, and (optionally) background music.

### Important Note for CodeHS
Sound support in the CodeHS Pygame sandbox may be limited due to browser restrictions. This extension uses `try/except` to gracefully handle cases where sound doesn't work. If sounds don't play, the game will still function normally.

### Implementation

Initialize the mixer and load sounds:

```python
# Sound effects (may not work in all environments)
try:
    pygame.mixer.init()
    sound_enabled = True
except Exception:
    sound_enabled = False
```

Since we cannot use external sound files in CodeHS, we can generate simple beep sounds programmatically:

```python
import array

def create_beep(frequency, duration_ms):
    """Create a simple beep sound. Returns None if audio unavailable."""
    if not sound_enabled:
        return None
    try:
        sample_rate = 22050
        num_samples = int(sample_rate * duration_ms / 1000)
        buf = array.array('h', [0] * num_samples)
        import math
        for i in range(num_samples):
            buf[i] = int(4000 * math.sin(2 * math.pi * frequency * i / sample_rate))
        sound = pygame.mixer.Sound(buffer=buf)
        return sound
    except Exception:
        return None

# Create sounds
eat_sound = create_beep(800, 100)    # High short beep for eating
die_sound = create_beep(200, 500)    # Low long beep for dying
```

Play sounds at the appropriate moments:

```python
# When eating food:
if eat_sound:
    eat_sound.play()

# When dying:
if die_sound:
    die_sound.play()
```

### Alternative: Visual Feedback Instead of Sound

If sound doesn't work in your CodeHS environment, add a visual "flash" instead:

```python
# Flash the background briefly when eating
flash_timer = 0

# In eating logic:
flash_timer = 5  # Flash for 5 frames

# In drawing logic:
if flash_timer > 0:
    window.fill((0, 40, 0))  # Dark green flash
    flash_timer = flash_timer - 1
else:
    window.fill(BLACK)
```

### Expected Result
- Short beep when eating food (if audio works)
- Lower tone when dying (if audio works)
- If audio doesn't work, the visual flash provides feedback instead

---

## Extension 6: Themes

### What You'll Build
Multiple visual themes the player can cycle through. Press T to switch themes during gameplay.

### New Concepts
- **Theme dictionaries**: Grouping related colours together
- **Cycling through options**: Using modulo `%` to wrap around

### Implementation

Define themes as a list of dictionaries:

```python
# Visual themes
themes = [
    {
        "name": "Classic",
        "background": (0, 0, 0),
        "snake_head": (0, 200, 0),
        "snake_body": (0, 150, 0),
        "food": (220, 50, 50),
        "text": (255, 255, 255),
    },
    {
        "name": "Ocean",
        "background": (10, 20, 50),
        "snake_head": (0, 200, 255),
        "snake_body": (0, 150, 200),
        "food": (255, 200, 0),
        "text": (200, 200, 255),
    },
    {
        "name": "Retro",
        "background": (20, 20, 20),
        "snake_head": (255, 255, 0),
        "snake_body": (200, 200, 0),
        "food": (255, 0, 255),
        "text": (0, 255, 0),
    },
    {
        "name": "Midnight",
        "background": (15, 0, 30),
        "snake_head": (180, 100, 255),
        "snake_body": (120, 50, 200),
        "food": (255, 100, 100),
        "text": (200, 200, 255),
    },
]

current_theme = 0
```

Add theme switching key (in event handling):

```python
                if event.key == pygame.K_t:
                    current_theme = (current_theme + 1) % len(themes)
```

Update your drawing functions to use theme colours:

```python
def draw_snake_themed(snake, theme):
    """Draw snake using theme colours."""
    for i, segment in enumerate(snake):
        if i == 0:
            colour = theme["snake_head"]
        else:
            colour = theme["snake_body"]
        pygame.draw.rect(window, colour, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
```

In the drawing section:

```python
    theme = themes[current_theme]
    window.fill(theme["background"])
    draw_snake_themed(snake_list, theme)
    pygame.draw.rect(window, theme["food"], (food_position[0], food_position[1], CELL_SIZE, CELL_SIZE))
    score_text = font.render("Score: " + str(score), True, theme["text"])
    window.blit(score_text, (10, 10))
```

### Expected Result
- Press T to cycle through Classic → Ocean → Retro → Midnight → Classic...
- All colours change together for a cohesive look
- Theme name briefly displays when switching (optional bonus)

---

## Extension 7: Power-Ups

### What You'll Build
Special items that spawn occasionally and give temporary effects:
- **Speed Boost (Yellow)**: Makes the snake faster for 5 seconds
- **Slow Motion (Cyan)**: Makes the snake slower for 5 seconds
- **Score Multiplier (Gold)**: Double points for 5 seconds

### New Concepts
- **Timed effects**: Using `pygame.time.get_ticks()` to track duration
- **Random spawning chance**: Deciding whether to spawn a power-up
- **Active effects**: A variable tracking what's currently active

### Implementation

Define power-up colours and variables:

```python
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
GOLD = (255, 200, 0)

# Power-ups
power_up_position = None  # None means no power-up on screen
power_up_type = None       # "speed", "slow", or "double"
power_up_spawn_timer = 0
active_effect = None       # Currently active effect
effect_end_time = 0        # When the effect wears off
```

Function to spawn a power-up:

```python
def spawn_power_up(snake, food, obstacles):
    """Randomly decide to spawn a power-up. Returns position and type, or None."""
    # 20% chance each time it's called
    if random.randint(1, 5) != 1:
        return None, None

    position = spawn_food()
    attempts = 0
    while position in snake or position == food:
        position = spawn_food()
        attempts = attempts + 1
        if attempts > 50:
            return None, None

    power_type = random.choice(["speed", "slow", "double"])
    return position, power_type
```

In your eating logic, try to spawn a power-up after eating:

```python
        if snake_list[0] == food_position:
            score = score + 1
            food_position = spawn_food_safe(snake_list)
            # Maybe spawn a power-up
            if power_up_position is None:
                power_up_position, power_up_type = spawn_power_up(snake_list, food_position, [])
```

Check if the snake picks up the power-up:

```python
        # Check power-up collection
        if power_up_position is not None and snake_list[0] == power_up_position:
            active_effect = power_up_type
            effect_end_time = pygame.time.get_ticks() + 5000  # 5 seconds
            power_up_position = None
            power_up_type = None
```

Check if the effect has expired:

```python
        # Check if active effect has expired
        if active_effect is not None:
            if pygame.time.get_ticks() >= effect_end_time:
                active_effect = None
```

Apply effects to speed:

```python
    # Calculate speed with effects
    current_speed = base_speed + (score // 3)
    if active_effect == "speed":
        current_speed = current_speed + 5
    elif active_effect == "slow":
        current_speed = max(current_speed - 5, 5)
    clock.tick(current_speed)
```

Apply score multiplier:

```python
        if snake_list[0] == food_position:
            if active_effect == "double":
                score = score + 2
            else:
                score = score + 1
```

Draw the power-up:

```python
def draw_power_up(position, power_type):
    """Draw the power-up with a colour based on type."""
    if position is None:
        return
    if power_type == "speed":
        colour = YELLOW
    elif power_type == "slow":
        colour = CYAN
    elif power_type == "double":
        colour = GOLD
    pygame.draw.rect(window, colour, (position[0], position[1], CELL_SIZE, CELL_SIZE))
    # Draw a smaller inner square to distinguish from food
    inner = CELL_SIZE // 4
    pygame.draw.rect(window, BLACK, (position[0] + inner, position[1] + inner, CELL_SIZE - inner * 2, CELL_SIZE - inner * 2))
```

Draw active effect indicator:

```python
    # Show active effect
    if active_effect is not None:
        remaining = (effect_end_time - pygame.time.get_ticks()) // 1000 + 1
        effect_text = font.render(active_effect.upper() + " " + str(remaining) + "s", True, YELLOW)
        window.blit(effect_text, (WINDOW_WIDTH // 2 - effect_text.get_width() // 2, 10))
```

Reset power-ups on restart:

```python
    power_up_position = None
    power_up_type = None
    active_effect = None
```

### Expected Result
- After eating food, a power-up may appear (20% chance)
- Power-ups look different from food (have an inner black square)
- Collecting a power-up activates an effect for 5 seconds
- A timer shows how long the effect lasts
- Yellow = speed up, Cyan = slow down, Gold = double points

---

## Combining Extensions

You can combine multiple extensions! Here are some tips:

- **Themes + everything**: Replace hardcoded colours with theme dictionary lookups
- **Difficulty + high scores**: Track a separate high score for each difficulty
- **Obstacles + power-ups**: Add a power-up that temporarily removes obstacles
- **Sound + power-ups**: Play different tones for different power-up pickups

---

## Review Questions

1. What is a "game state" and how is it different from a simple boolean variable?
2. Why do we use `try/except` around the sound code?
3. How does `(current_theme + 1) % len(themes)` create a cycle?
4. What is `pygame.time.get_ticks()` and why is it useful for timed effects?
5. Why do we check `if power_up_position is not None` before drawing it?

---

## Practice Exercises

### Exercise 1: Your Own Theme
Create a **fifth theme** with your own colour choices. Add it to the `themes` list.

### Exercise 2: Obstacle Patterns
Instead of random obstacles, create a function that places obstacles in a pattern (e.g., a line across the middle of the screen, or a square in the centre).

### Exercise 3: Power-Up Balance
Playtest your power-ups. Are they too frequent? Too rare? Adjust the spawn chance (currently 20%) and the duration (currently 5 seconds) until the game feels fun and balanced.

---

## Final Challenge: Make It Your Own

Now that you have all these tools, create your **ultimate Snake game**. Combine at least 3 extensions and add one feature that is entirely your own invention. Some ideas:

- A "wrap-around" mode where the snake appears on the opposite side instead of dying at walls
- Multiple snakes (multiplayer on one keyboard — WASD and arrow keys)
- Food that runs away from the snake
- A snake that leaves a temporary trail that fades over time
- Levels with different obstacle layouts
- A time limit mode (eat as much as possible in 60 seconds)

---

## Teacher Notes

**Time Estimate**: 2–3 class periods (students choose and implement extensions)

**Differentiation**:
- **Struggling students**: Extensions 1 (Difficulty) and 2 (High Score) are the simplest — they add one variable and some display logic.
- **Average students**: Extensions 3 (Obstacles) and 4 (Animated Food) add moderate complexity.
- **Advanced students**: Extensions 5 (Sound), 6 (Themes with dictionaries), and 7 (Power-ups with timers) are the most challenging.

**Assessment Options**:
- Require all students to complete at least 2 extensions
- Award bonus marks for the Final Challenge
- Have students present their games to the class and explain one extension they're proud of

**Presentation Day Idea**:
Set up a "Game Arcade" where students can play each other's Snake games. Each student puts their game on their screen and classmates rotate around the room trying different versions.

**Extensions that Teach Important Concepts**:
| Extension | CS Concept |
|-----------|-----------|
| Difficulty | User input, program configuration |
| High Score | Persistent state, max/min operations |
| Obstacles | Data structures, spatial reasoning |
| Animated Food | Time-based animation, math functions |
| Sound | Error handling, multimedia |
| Themes | Dictionaries, data-driven design |
| Power-ups | Timers, state machines, random events |

---

## Congratulations!

You have completed the entire Snake Game Tutorial Series! You went from an empty file to a fully-featured game with:

- Smooth grid-based movement
- A growing snake
- Random food generation
- Collision detection (walls and self)
- Score display
- Game Over and restart
- Clean, function-based code
- Pause feature
- Dynamic speed
- And whatever extensions you chose to add!

You now understand the fundamentals of game development:
- **Game loops** that run continuously
- **Event handling** for player input
- **State management** for tracking what's happening
- **Collision detection** for game rules
- **Rendering** to display everything on screen
- **Timing** to control game speed

These skills transfer to any game you want to build next. Keep experimenting, keep coding, and most importantly — keep having fun!

---

[← Back to Lesson 7](Lesson-07-Improving-the-Game.md) | [← Back to Series Overview](README.md)
