import pygame
import random
# ゲーム画面のサイズ
WIDTH = 800
HEIGHT = 600
# 色の定義
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
# プレイヤーのサイズと速度
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5
# ジャンプの力と重力
JUMP_POWER = 10
GRAVITY = 1
# プレイヤーの初期位置
player_x = WIDTH // 2
player_y = HEIGHT - PLAYER_HEIGHT
# 障害物の初期位置と速度
obstacle_x = WIDTH
obstacle_y = HEIGHT - PLAYER_HEIGHT
obstacle_speed = 5
# ゲームの初期化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# プレイヤーの画像を読み込む
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # プレイヤーの移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_x += PLAYER_SPEED
    # プレイヤーのジャンプ
    if keys[pygame.K_SPACE] and player_y == HEIGHT - PLAYER_HEIGHT:
        player_y -= JUMP_POWER
    # プレイヤーの重力
    player_y += GRAVITY
    # 障害物の移動
    obstacle_x -= obstacle_speed
    # 障害物が画面外に出たら新しい位置に再配置
    if obstacle_x < -PLAYER_WIDTH:
        obstacle_x = WIDTH
        obstacle_y = HEIGHT - PLAYER_HEIGHT
        obstacle_speed = random.randint(3, 7)
    # プレイヤーと障害物の衝突判定
    if player_x < obstacle_x + PLAYER_WIDTH and player_x + PLAYER_WIDTH > obstacle_x and player_y < obstacle_y + PLAYER_HEIGHT and player_y + PLAYER_HEIGHT > obstacle_y:
        running = False
    # 画面の描画
    screen.fill(WHITE)
    screen.blit(player_image, (player_x, player_y))
    pygame.draw.rect(screen, BLUE, (obstacle_x, obstacle_y, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.display.flip()
    # フレームレートの設定
    clock.tick(60)
# ゲームの終了
pygame.quit()
