    # Finished base game (Lessons 1-3). Extensions in Lesson 4 are optional and not included here.
    import os
    import pygame

    os.environ["SDL_AUDIODRIVER"] = "dsp"

    pygame.init()

    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 400
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Space Invaders")

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 200, 0)
    RED = (200, 0, 0)

    PLAYER_WIDTH = 50
    PLAYER_HEIGHT = 20
    player_x = WINDOW_WIDTH // 2 - PLAYER_WIDTH // 2
    player_y = WINDOW_HEIGHT - 40
    PLAYER_SPEED = 6

    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 30
    ENEMY_ROWS = 3
    ENEMY_COLS = 5
    ENEMY_SPACING_X = 20
    ENEMY_SPACING_Y = 20

    enemies = []
    for row in range(ENEMY_ROWS):
        for col in range(ENEMY_COLS):
            enemy_x = 60 + col * (ENEMY_WIDTH + ENEMY_SPACING_X)
            enemy_y = 40 + row * (ENEMY_HEIGHT + ENEMY_SPACING_Y)
            enemies.append([enemy_x, enemy_y])

    enemy_dx = 2
    ENEMY_DROP = 20

    BULLET_WIDTH = 4
    BULLET_HEIGHT = 10
    BULLET_SPEED = 8
    bullets = []

    font = pygame.font.SysFont(None, 36)
    score = 0
    game_over = False
    game_message = ""

    clock = pygame.time.Clock()
    FPS = 60

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_over:
                bullets.append([player_x + PLAYER_WIDTH // 2 - BULLET_WIDTH // 2, player_y])

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= PLAYER_SPEED
            if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - PLAYER_WIDTH:
                player_x += PLAYER_SPEED

            for bullet in bullets:
                bullet[1] -= BULLET_SPEED
            bullets = [b for b in bullets if b[1] > 0]

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

            for enemy in enemies:
                if enemy[1] + ENEMY_HEIGHT >= player_y:
                    game_over = True
                    game_message = "GAME OVER"

            if len(enemies) == 0:
                game_over = True
                game_message = "YOU WIN"

        window.fill(BLACK)

        pygame.draw.rect(window, GREEN, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

        for enemy in enemies:
            pygame.draw.rect(window, RED, (enemy[0], enemy[1], ENEMY_WIDTH, ENEMY_HEIGHT))

        for bullet in bullets:
            pygame.draw.rect(window, WHITE, (bullet[0], bullet[1], BULLET_WIDTH, BULLET_HEIGHT))

        score_text = font.render("Score: " + str(score), True, WHITE)
        window.blit(score_text, (10, 10))

        if game_over:
            message_text = font.render(game_message, True, WHITE)
            window.blit(message_text, (WINDOW_WIDTH // 2 - message_text.get_width() // 2, WINDOW_HEIGHT // 2))

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
