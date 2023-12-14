import pygame
import random
# ゲーム画面のサイズを定義
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
# ブロックのサイズを定義
BLOCK_WIDTH = 64
BLOCK_HEIGHT = 32
# パドルのサイズを定義
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 16
# ボールのサイズを定義
BALL_SIZE = 16
# ブロックの色を定義
BLOCK_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
# ゲームオーバーのフラグ
game_over = False
# ブロックのクラス
class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
# パドルのクラス
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
    def move(self, dx):
        self.x += dx
        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_WIDTH - PADDLE_WIDTH:
            self.x = SCREEN_WIDTH - PADDLE_WIDTH
        self.rect.x = self.x
# ボールのクラス
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.choice([-5, -4, -3, 3, 4, 5])
        self.dy = -5
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x + BALL_SIZE // 2, self.y + BALL_SIZE // 2), BALL_SIZE // 2)
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x < 0:
            self.x = 0
            self.dx = -self.dx
        elif self.x > SCREEN_WIDTH - BALL_SIZE:
            self.x = SCREEN_WIDTH - BALL_SIZE
            self.dx = -self.dx
        if self.y < 0:
            self.y = 0
            self.dy = -self.dy
        self.rect.x = self.x
        self.rect.y = self.y
# ブロックを生成する関数
def generate_blocks():
    blocks = []
    for i in range(6):
        for j in range(10):
            x = j * BLOCK_WIDTH
            y = i * BLOCK_HEIGHT + 50
            color = BLOCK_COLORS[i]
            blocks.append(Block(x, y, color))
    return blocks
# メイン処理
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Breaker")
clock = pygame.time.Clock()
blocks = generate_blocks()
paddle = Paddle(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10)
ball = Ball(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2)
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    # パドルを移動する
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move(-5)
    elif keys[pygame.K_RIGHT]:
        paddle.move(5)
    # ボールを移動する
    ball.move()
    # ボールがブロックに当たった場合
    for block in blocks:
        if ball.rect.colliderect(block.rect):
            blocks.remove(block)
            ball.dy = -ball.dy
    # ボールがパドルに当たった場合
    if ball.rect.colliderect(paddle.rect):
        ball.dy = -ball.dy
    # ボールが画面下に落ちた場合
    if ball.y > SCREEN_HEIGHT:
        game_over = True
    # 画面を描画する
    screen.fill((0, 0, 0))
    for block in blocks:
        block.draw(screen)
    paddle.draw(screen)
    ball.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
