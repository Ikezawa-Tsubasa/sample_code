import random
# ゲーム盤の初期化
def initialize_board():
    board = [[0 for i in range(4)] for j in range(4)]
    return board
# ゲーム盤の表示
def print_board(board):
    for row in board:
        print(row)
# 新しい数字をランダムに生成
def generate_new_number():
    if random.randint(0, 9) == 0:
        return 4
    else:
        return 2
# ゲーム盤に新しい数字を追加
def add_new_number(board):
    row = random.randint(0, 3)
    col = random.randint(0, 3)
    while board[row][col] != 0:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
    board[row][col] = generate_new_number()
# ゲーム盤を左にスライド
def slide_left(board):
    for row in board:
        # 0以外の数字を左に詰める
        new_row = [i for i in row if i != 0]
        # 左に詰めた分を0で埋める
        new_row += [0] * (4 - len(new_row))
        # スライド後の行を更新
        row[:] = new_row
# ゲーム盤を右にスライド
def slide_right(board):
    for row in board:
        # 0以外の数字を右に詰める
        new_row = [i for i in row if i != 0]
        # 右に詰めた分を0で埋める
        new_row = [0] * (4 - len(new_row)) + new_row
        # スライド後の行を更新
        row[:] = new_row
# ゲーム盤を上にスライド
def slide_up(board):
    for col in range(4):
        # 列を取り出す
        column = [board[row][col] for row in range(4)]
        # 0以外の数字を上に詰める
        new_column = [i for i in column if i != 0]
        # 上に詰めた分を0で埋める
        new_column += [0] * (4 - len(new_column))
        # スライド後の列を更新
        for row in range(4):
            board[row][col] = new_column[row]
# ゲーム盤を下にスライド
def slide_down(board):
    for col in range(4):
        # 列を取り出す
        column = [board[row][col] for row in range(4)]
        # 0以外の数字を下に詰める
        new_column = [i for i in column if i != 0]
        # 下に詰めた分を0で埋める
        new_column = [0] * (4 - len(new_column)) + new_column
        # スライド後の列を更新
        for row in range(4):
            board[row][col] = new_column[row]
# ゲーム盤が動かせるかどうかを判定
def can_move(board):
    for row in board:
        if 0 in row:
            return True
        for i in range(3):
            if row[i] == row[i+1] and row[i] != 0:
                return True
    for col in range(4):
        column = [board[row][col] for row in range(4)]
        if 0 in column:
            return True
        for i in range(3):
            if column[i] == column[i+1] and column[i] != 0:
                return True
    return False
# ゲームのメイン処理
def main():
    board = initialize_board()
    add_new_number(board)
    add_new_number(board)
    print_board(board)
    while can_move(board):
        move = input("Enter move (left, right, up, down): ")
        if move == "left":
            slide_left(board)
        elif move == "right":
            slide_right(board)
        elif move == "up":
            slide_up(board)
        elif move == "down":
            slide_down(board)
        else:
            print("Invalid move")
            continue
        add_new_number(board)
        print_board(board)
    print("Game over")
if __name__ == "__main__":
    main()
