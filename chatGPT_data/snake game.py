import pygame
import random
# ゲーム画面のサイズ
WIDTH = 800
HEIGHT = 600
# セルのサイズと色
CELL_SIZE = 40
CELL_COLOR = (192, 192, 192)
# 地雷の数
NUM_MINES = 10
# ゲームの初期化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# ゲーム盤のサイズ
board_width = WIDTH // CELL_SIZE
board_height = HEIGHT // CELL_SIZE
# ゲーム盤の初期化
board = [[0] * board_width for _ in range(board_height)]
revealed = [[False] * board_width for _ in range(board_height)]
mines = []
# 地雷の配置
for _ in range(NUM_MINES):
    while True:
        x = random.randint(0, board_width - 1)
        y = random.randint(0, board_height - 1)
        if board[y][x] != -1:
            board[y][x] = -1
            mines.append((x, y))
            break
# 周囲の地雷の数を計算
for x, y in mines:
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if 0 <= x + dx < board_width and 0 <= y + dy < board_height and board[y + dy][x + dx] != -1:
                board[y + dy][x + dx] += 1
# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左クリック
                x, y = event.pos
                cell_x = x // CELL_SIZE
                cell_y = y // CELL_SIZE
                if board[cell_y][cell_x] == -1:
                    running = False
                else:
                    revealed[cell_y][cell_x] = True
    # 画面の描画
    screen.fill(CELL_COLOR)
    for y in range(board_height):
        for x in range(board_width):
            cell_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if revealed[y][x]:
                pygame.draw.rect(screen, (255, 255, 255), cell_rect)
                if board[y][x] != 0:
                    font = pygame.font.Font(None, 30)
                    text = font.render(str(board[y][x]), True, (0, 0, 0))
                    text_rect = text.get_rect(center=cell_rect.center)
                    screen.blit(text, text_rect)
            else:
                pygame.draw.rect(screen, (128, 128, 128), cell_rect)
    pygame.display.flip()
    # フレームレートの設定
    clock.tick(60)
# ゲームの終了
pygame.quit()
