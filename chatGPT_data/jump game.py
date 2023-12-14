import pygame
import random
# ゲーム画面のサイズ
WIDTH = 800
HEIGHT = 600
# 色の定義
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# 蛇のサイズと速度
SNAKE_SIZE = 20
SNAKE_SPEED = 10
# 食べ物のサイズ
FOOD_SIZE = 20
# ゲームの初期化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# 蛇の初期位置と初期移動方向
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_dx = SNAKE_SPEED
snake_dy = 0
# 食べ物の初期位置
food_x = random.randint(0, WIDTH - FOOD_SIZE)
food_y = random.randint(0, HEIGHT - FOOD_SIZE)
# 蛇の体の座標リスト
snake_body = [(snake_x, snake_y)]
# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # キー入力の処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dy != SNAKE_SPEED:
        snake_dx = 0
        snake_dy = -SNAKE_SPEED
    if keys[pygame.K_DOWN] and snake_dy != -SNAKE_SPEED:
        snake_dx = 0
        snake_dy = SNAKE_SPEED
    if keys[pygame.K_LEFT] and snake_dx != SNAKE_SPEED:
        snake_dx = -SNAKE_SPEED
        snake_dy = 0
    if keys[pygame.K_RIGHT] and snake_dx != -SNAKE_SPEED:
        snake_dx = SNAKE_SPEED
        snake_dy = 0
    # 蛇の移動
    snake_x += snake_dx
    snake_y += snake_dy
    # 蛇が画面外に出たらゲームオーバー
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        running = False
    # 蛇が食べ物を食べたら体を伸ばす
    if snake_x < food_x + FOOD_SIZE and snake_x + SNAKE_SIZE > food_x and snake_y < food_y + FOOD_SIZE and snake_y + SNAKE_SIZE > food_y:
        food_x = random.randint(0, WIDTH - FOOD_SIZE)
        food_y = random.randint(0, HEIGHT - FOOD_SIZE)
        snake_body.append((snake_x, snake_y))
    # 蛇の体の更新
    snake_body.insert(0, (snake_x, snake_y))
    if len(snake_body) > 1:
        snake_body.pop()
    # 蛇が自分の体に衝突したらゲームオーバー
    if (snake_x, snake_y) in snake_body[1:]:
        running = False
    # 画面の描画
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (snake_x, snake_y, SNAKE_SIZE, SNAKE_SIZE))
    for body_part in snake_body[1:]:
        pygame.draw.rect(screen, GREEN, (body_part[0], body_part[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(screen, RED, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))
    pygame.display.flip()
    # フレームレートの設定
    clock.tick(15)
# ゲームの終了
pygame.quit()
