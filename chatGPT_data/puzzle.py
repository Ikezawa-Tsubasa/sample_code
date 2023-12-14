import random
# パズルのクラス
class Puzzle:
    def __init__(self, size):
        self.size = size
        self.board = [[0] * size for _ in range(size)]
        self.empty_row = size - 1
        self.empty_col = size - 1
    
    def shuffle(self):
        # パズルをシャッフルする処理
        nums = list(range(1, self.size**2))
        random.shuffle(nums)
        
        for row in range(self.size):
            for col in range(self.size):
                if row == self.size - 1 and col == self.size - 1:
                    self.board[row][col] = 0
                else:
                    self.board[row][col] = nums.pop()
    
    def move(self, direction):
        # パズルのピースを移動する処理
        if direction == "up" and self.empty_row > 0:
            self.board[self.empty_row][self.empty_col] = self.board[self.empty_row - 1][self.empty_col]
            self.board[self.empty_row - 1][self.empty_col] = 0
            self.empty_row -= 1
        elif direction == "down" and self.empty_row < self.size - 1:
            self.board[self.empty_row][self.empty_col] = self.board[self.empty_row + 1][self.empty_col]
            self.board[self.empty_row + 1][self.empty_col] = 0
            self.empty_row += 1
        elif direction == "left" and self.empty_col > 0:
            self.board[self.empty_row][self.empty_col] = self.board[self.empty_row][self.empty_col - 1]
            self.board[self.empty_row][self.empty_col - 1] = 0
            self.empty_col -= 1
        elif direction == "right" and self.empty_col < self.size - 1:
            self.board[self.empty_row][self.empty_col] = self.board[self.empty_row][self.empty_col + 1]
            self.board[self.empty_row][self.empty_col + 1] = 0
            self.empty_col += 1
    
    def is_solved(self):
        # パズルが解かれているかどうかを判定する処理
        num = 1
        for row in range(self.size):
            for col in range(self.size):
                if row == self.size - 1 and col == self.size - 1:
                    if self.board[row][col] != 0:
                        return False
                elif self.board[row][col] != num:
                    return False
                num += 1
        return True
    
    def print_board(self):
        # パズルの盤面を表示する処理
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    print("  ", end=" ")
                else:
                    print(f"{self.board[row][col]:2d}", end=" ")
            print()
        print()
# パズルの作成
puzzle = Puzzle(4)
puzzle.shuffle()
# ゲームループ
while True:
    # 盤面の表示
    puzzle.print_board()
    
    # プレイヤーの入力
    direction = input("上: u, 下: d, 左: l, 右: r > ")
    
    # パズルのピースを移動
    puzzle.move(direction)
    
    # パズルが解かれたかどうかの判定
    if puzzle.is_solved():
        print("パズルが解かれました！")
        break
