import pygame
import random
# ゲーム画面のサイズ
WIDTH = 800
HEIGHT = 400
# パドルのサイズ
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
# ボールのサイズと速度
BALL_RADIUS = 10
BALL_SPEED_X = 3
BALL_SPEED_Y = 3
# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# ゲームの初期化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()
# パドルの初期位置
paddle1_x = 50
paddle1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_x = WIDTH - 50 - PADDLE_WIDTH
paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
# ボールの初期位置と速度
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = BALL_SPEED_X * random.choice([1, -1])
ball_speed_y = BALL_SPEED_Y * random.choice([1, -1])
# スコアの初期化
score1 = 0
score2 = 0
# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # パドルの移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= 5
    if keys[pygame.K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT:
        paddle1_y += 5
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= 5
    if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - PADDLE_HEIGHT:
        paddle2_y += 5
    # ボールの移動
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    # ボールと壁の衝突判定
    if ball_y > HEIGHT - BALL_RADIUS or ball_y < BALL_RADIUS:
        ball_speed_y *= -1
    if ball_x > WIDTH - BALL_RADIUS or ball_x < BALL_RADIUS:
        ball_speed_x *= -1
    # ボールとパドルの衝突判定
    if ball_x < paddle1_x + PADDLE_WIDTH and paddle1_y < ball_y < paddle1_y + PADDLE_HEIGHT:
        ball_speed_x *= -1
        score1 += 1
    if ball_x > paddle2_x and paddle2_y < ball_y < paddle2_y + PADDLE_HEIGHT:
        ball_speed_x *= -1
        score2 += 1
    # 画面の描画
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (paddle1_x, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    # スコアの表示
    font = pygame.font.Font(None, 36)
    score_text = font.render(str(score1) + " - " + str(score2), True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
