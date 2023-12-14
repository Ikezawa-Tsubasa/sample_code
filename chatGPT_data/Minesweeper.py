import random
# マス目の状態を表す定数
HIDDEN = 0
MINE = 1
EMPTY = 2
# マス目の状態を表す文字列
SYMBOLS = {
    HIDDEN: '■',
    MINE: 'x',
    EMPTY: ' '
}
# マス目の状態を表すクラス
class Cell:
    def __init__(self, state=HIDDEN):
        self.state = state
        self.adjacent_mines = 0
    def __str__(self):
        if self.state == HIDDEN:
            return SYMBOLS[HIDDEN]
        elif self.state == MINE:
            return SYMBOLS[MINE]
        else:
            return str(self.adjacent_mines)
# マインスイーパーの盤面を表すクラス
class Board:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.grid = [[Cell() for _ in range(width)] for _ in range(height)]
        self.place_mines()
    # ランダムに地雷を配置する
    def place_mines(self):
        positions = [(x, y) for x in range(self.width) for y in range(self.height)]
        mine_positions = random.sample(positions, self.num_mines)
        for x, y in mine_positions:
            self.grid[y][x].state = MINE
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if (dx, dy) != (0, 0) and 0 <= x+dx < self.width and 0 <= y+dy < self.height:
                        self.grid[y+dy][x+dx].adjacent_mines += 1
    # 盤面を表示する
    def display(self):
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))
    # 指定したマスを開く
    def open_cell(self, x, y):
        cell = self.grid[y][x]
        if cell.state == HIDDEN:
            cell.state = EMPTY
            if cell.adjacent_mines == 0:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if (dx, dy) != (0, 0) and 0 <= x+dx < self.width and 0 <= y+dy < self.height:
                            self.open_cell(x+dx, y+dy)
    # ゲームを実行する
    def play(self):
        while True:
            self.display()
            x = int(input('Enter x coordinate: '))
            y = int(input('Enter y coordinate: '))
            self.open_cell(x, y)
            if self.grid[y][x].state == MINE:
                print('Game over!')
                break
            elif self.check_win():
                print('You win!')
                break
    # 勝利条件をチェックする
    def check_win(self):
        for row in self.grid:
            for cell in row:
                if cell.state == HIDDEN and cell.adjacent_mines != 0:
                    return False
        return True
# ゲームを開始する
board = Board(10, 10, 10)
board.play()