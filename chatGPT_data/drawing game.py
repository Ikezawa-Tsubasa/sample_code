import pygame
# ゲーム画面のサイズ
WIDTH = 800
HEIGHT = 600
# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# 初期化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("お絵描きゲーム")
# 描画する線の太さ
line_width = 5
# 描画中のフラグ
drawing = False
# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左クリック
                drawing = True
                start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # 左クリック
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                end_pos = pygame.mouse.get_pos()
                pygame.draw.line(screen, BLACK, start_pos, end_pos, line_width)
                start_pos = end_pos
    # 画面を白で塗りつぶす
    screen.fill(WHITE)
    # 画面を更新する
    pygame.display.flip()
# 終了
pygame.quit()
