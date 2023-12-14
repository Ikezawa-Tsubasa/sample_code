import pygame
import random
from pprint import pprint
# ゲーム画面のサイズ
SCREEN_WIDTH = 360
SCREEN_HEIGHT = 480
# ブロックのサイズ
BLOCK_SIZE = 20
# ブロックの種類と色
BLOCKS = [
    ([(0, 0), (1, 0), (0, 1), (1, 1)], (255, 0, 0)),  # 赤
    ([(0, 0), (1, 0), (2, 0), (3, 0)], (0, 255, 0)),  # 緑
    ([(0, 0), (1, 0), (2, 0), (2, 1)], (0, 0, 255)),  # 青
    ([(0, 0), (1, 0), (1, 1), (2, 1)], (255, 255, 0)),  # 黄色
    ([(0, 1), (1, 1), (1, 0), (2, 0)], (255, 0, 255)),  # 紫
    ([(0, 0), (1, 0), (2, 0), (1, 1)], (0, 255, 255)),  # 水色
    ([(0, 0), (1, 0), (2, 0), (0, 1)], (255, 128, 0)),  # オレンジ
]
# テトリスのクラス
class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 30)
        self.score = 0
        self.board = [[0] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
        self.current_block = self.get_new_block()
        self.next_block = self.get_new_block()
        self.game_over = False
    # 新しいブロックを取得する
    def get_new_block(self):
        block_type, block_color = random.choice(BLOCKS)
        block = []
        for x, y in block_type:
            block.append((x + SCREEN_WIDTH // BLOCK_SIZE // 2 - 2, y))
        return (block, block_color)
    # ブロックを描画する
    def draw_block(self, block):
        for x, y in block[0]:
            pygame.draw.rect(self.screen, block[1], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    # ブロックを回転する
    def rotate_block(self, block):
        center_x = sum([x for x, y in block]) / len(block)
        center_y = sum([y for x, y in block]) / len(block)
        new_block = []
        for x, y in block:
            new_x = int(center_x + (y - center_y))
            new_y = int(center_y - (x - center_x))
            new_block.append((new_x, new_y))
        return new_block
    # ブロックを移動する
    def move_block(self, block, dx, dy):
        new_block = []
        for x, y in block:
            new_block.append((x + dx, y + dy))
        return new_block
    # ブロックが衝突するかどうかを判定する
    def is_collision(self, block):
        for x, y in block:
            if x < 0 or x >= SCREEN_WIDTH // BLOCK_SIZE or y >= SCREEN_HEIGHT // BLOCK_SIZE:
                return True
            if y >= 0 and self.board[y][x]:
                return True
        return False
    # ブロックを固定する
    def fix_block(self, block):
        for x, y in block:
            self.board[y][x] = 1
    # 行が揃ったら消す
    def clear_lines(self):
        lines = 0
        for y in range(len(self.board)):
            if all(self.board[y]):
                del self.board[y]
                self.board.insert(0, [0] * (SCREEN_WIDTH // BLOCK_SIZE))
                lines += 1
        self.score += lines ** 2
    # ゲームオーバーかどうかを判定する
    def is_game_over(self):
        return any(self.board[0])
    # ゲームを実行する
    def run(self):
        while not self.game_over:
            key_states = pygame.key.get_pressed()
            if key_states[pygame.K_LEFT]:
                new_block = self.move_block(self.current_block[0], -1, 0)
                if not self.is_collision(new_block):
                        self.current_block = (new_block, self.current_block[1])
            elif key_states[pygame.K_RIGHT]:
                new_block = self.move_block(self.current_block[0], 1, 0)
                if not self.is_collision(new_block):
                    self.current_block = (new_block, self.current_block[1])
            elif key_states[pygame.K_DOWN]:
                new_block = self.move_block(self.current_block[0], 0, 1)
                if not self.is_collision(new_block):
                    self.current_block = (new_block, self.current_block[1])
                    
                        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        new_block = self.rotate_block(self.current_block[0])
                        if not self.is_collision(new_block):
                            self.current_block = (new_block, self.current_block[1])
                    elif event.key == pygame.K_a:
                        for b in self.board:
                            print(b)

            self.screen.fill((0, 0, 0))
            # ブロックを落とす
            new_block = self.move_block(self.current_block[0], 0, 1)
            if not self.is_collision(new_block):
                self.current_block = (new_block, self.current_block[1])
            else:
                self.fix_block(self.current_block[0])
                self.clear_lines()
                self.current_block = self.next_block
                self.next_block = self.get_new_block()
                if self.is_collision(self.current_block[0]):
                    self.game_over = True
            # ブロックを描画する
            self.draw_block(self.current_block)
            for i, block in enumerate(self.board):
                for j, b in enumerate(block):
                    if b==1:
                        pygame.draw.rect(self.screen, (255, 0, 0), (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            
            # スコアを表示する
            score_text = self.font.render("Score: {}".format(self.score), True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))
            # 次のブロックを表示する
            next_text = self.font.render("Next:", True, (255, 255, 255))
            self.screen.blit(next_text, (SCREEN_WIDTH - 100, 10))
            self.draw_block(self.next_block)
            pygame.display.update()
            self.clock.tick(8)
        pygame.quit()
if __name__ == "__main__":
    Tetris().run()
