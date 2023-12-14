import pygame
import random
pygame.init()
# ゲーム画面のサイズ
width = 800
height = 600
# 色の定義
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
# ボールのサイズと速度
ball_radius = 10
ball_speed_x = 3
ball_speed_y = 3
# パドルのサイズと速度
paddle_width = 100
paddle_height = 10
paddle_speed = 5
# ブロックのサイズと間隔
block_width = 70
block_height = 20
block_gap = 10
# ブロックの行数と列数
block_rows = 5
block_cols = 10
# ゲーム画面の設定
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pinball Game")
clock = pygame.time.Clock()
def draw_ball(ball_x, ball_y):
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)
def draw_paddle(paddle_x, paddle_y):
    pygame.draw.rect(screen, blue, (paddle_x, paddle_y, paddle_width, paddle_height))
def draw_block(block_x, block_y):
    pygame.draw.rect(screen, white, (block_x, block_y, block_width, block_height))
def game_loop():
    game_over = False
    ball_x = width // 2
    ball_y = height // 2
    ball_dx = ball_speed_x
    ball_dy = ball_speed_y
    paddle_x = (width - paddle_width) // 2
    paddle_y = height - paddle_height - 10
    blocks = []
    for row in range(block_rows):
        for col in range(block_cols):
            block_x = col * (block_width + block_gap)
            block_y = row * (block_height + block_gap)
            blocks.append((block_x, block_y))
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT]:
            paddle_x += paddle_speed
        ball_x += ball_dx
        ball_y += ball_dy
        if ball_x <= ball_radius or ball_x >= width - ball_radius:
            ball_dx *= -1
        if ball_y <= ball_radius:
            ball_dy *= -1
        if ball_y >= height - ball_radius:
            if paddle_x <= ball_x <= paddle_x + paddle_width:
                ball_dy *= -1
            else:
                game_over = True
        if paddle_x < 0:
            paddle_x = 0
        if paddle_x > width - paddle_width:
            paddle_x = width - paddle_width
        screen.fill(black)
        draw_ball(ball_x, ball_y)
        draw_paddle(paddle_x, paddle_y)
        for block in blocks:
            block_x, block_y = block
            draw_block(block_x, block_y)
            if block_x <= ball_x <= block_x + block_width and block_y <= ball_y <= block_y + block_height:
                ball_dy *= -1
                blocks.remove(block)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
game_loop()
