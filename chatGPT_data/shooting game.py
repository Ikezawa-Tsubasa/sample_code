import pygame
import random
# ゲーム画面のサイズ
WIDTH = 800
HEIGHT = 600
# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# 初期化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("シューティングゲーム")
# プレイヤーの設定
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size * 2]
# 敵の設定
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]
# 弾の設定
bullet_size = 10
bullet_pos = []
bullet_speed = 10
# スコアの初期化
score = 0
# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_pos.append([player_pos[0] + player_size // 2, player_pos[1]])
    # プレイヤーの移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    # 敵の移動
    for enemy in enemy_list:
        enemy[1] += 5
        if enemy[1] > HEIGHT:
            enemy_list.remove(enemy)
            score += 1
    # 弾の移動
    for bullet in bullet_pos:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullet_pos.remove(bullet)
    # 衝突判定
    for enemy in enemy_list:
        if enemy_pos[1] + enemy_size > player_pos[1] and enemy_pos[1] < player_pos[1] + player_size:
            if enemy_pos[0] + enemy_size > player_pos[0] and enemy_pos[0] < player_pos[0] + player_size:
                running = False
        for bullet in bullet_pos:
            if bullet[1] < enemy[1] + enemy_size and bullet[1] > enemy[1]:
                if bullet[0] < enemy[0] + enemy_size and bullet[0] > enemy[0]:
                    enemy_list.remove(enemy)
                    bullet_pos.remove(bullet)
                    score += 1
    # 画面を白で塗りつぶす
    screen.fill(WHITE)
    # プレイヤーを描画
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
    # 敵を描画
    for enemy in enemy_list:
        pygame.draw.rect(screen, BLACK, (enemy[0], enemy[1], enemy_size, enemy_size))
    # 弾を描画
    for bullet in bullet_pos:
        pygame.draw.rect(screen, BLACK, (bullet[0], bullet[1], bullet_size, bullet_size))
    # スコアを表示
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (10, 10))
    # 画面を更新する
    pygame.display.flip()
# 終了
pygame.quit()
