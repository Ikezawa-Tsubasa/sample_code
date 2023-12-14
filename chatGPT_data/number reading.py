import random
# 数読の盤面を表すクラス
class Board:
    def __init__(self):
        self.numbers = []
        self.create_board()
    # 盤面を生成する
    def create_board(self):
        numbers = list(range(1, 26))
        random.shuffle(numbers)
        self.numbers = [numbers[i:i+5] for i in range(0, 25, 5)]
        self.numbers[2][2] = 'FREE'
    # 盤面を表示する
    def display(self):
        for row in self.numbers:
            print(' '.join(str(num).rjust(2) for num in row))
    # 数字をマークする
    def mark_number(self, number):
        for i in range(5):
            for j in range(5):
                if self.numbers[i][j] == number:
                    self.numbers[i][j] = 'X'
    # 勝利条件をチェックする
    def check_win(self):
        for row in self.numbers:
            if not all(isinstance(num, str) for num in row):
                return False
        return True
# ゲームを開始する
board = Board()
board.display()
while True:
    number = int(input('Enter number: '))
    board.mark_number(number)
    board.display()
    if board.check_win():
        print('You win!')
        break
