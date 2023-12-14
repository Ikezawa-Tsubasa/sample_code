# オセロの盤面を初期化する
def initialize_board():
    board = [[' ' for _ in range(8)] for _ in range(8)]
    board[3][3] = '○'
    board[3][4] = '●'
    board[4][3] = '●'
    board[4][4] = '○'
    return board
# 盤面を表示する
def print_board(board):
    print('  1 2 3 4 5 6 7 8')
    print(' ┌───────────────┐')
    for i in range(8):
        print(f'{i+1}│', end='')
        for j in range(8):
            print(board[i][j], end='│')
        print('\
 ├─┼─┼─┼─┼─┼─┼─┼─┤')
    print(' └───────────────┘')
# 指定した座標に石を置けるかどうかを判定する
def is_valid_move(board, row, col, color):
    if board[row][col] != ' ':
        return False
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for direction in directions:
        dx, dy = direction
        x, y = row + dx, col + dy
        if 0 <= x < 8 and 0 <= y < 8 and board[x][y] != color and board[x][y] != ' ':
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == color:
                    return True
                x += dx
                y += dy
    return False
# 指定した座標に石を置く
def make_move(board, row, col, color):
    if not is_valid_move(board, row, col, color):
        return False
    board[row][col] = color
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for direction in directions:
        dx, dy = direction
        x, y = row + dx, col + dy
        if 0 <= x < 8 and 0 <= y < 8 and board[x][y] != color and board[x][y] != ' ':
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == color:
                    while (x, y) != (row, col):
                        x -= dx
                        y -= dy
                        board[x][y] = color
                    break
                x += dx
                y += dy
    return True
# ゲームを実行する
def play_game():
    board = initialize_board()
    current_color = '●'
    while True:
        print_board(board)
        print(f"現在の手番: {current_color}")
        # プレイヤーに座標を入力してもらう
        while True:
            try:
                row = int(input("行を選んでください (1-8): ")) - 1
                col = int(input("列を選んでください (1-8): ")) - 1
                if 0 <= row < 8 and 0 <= col < 8:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("無効な入力です。もう一度入力してください。
        # 石を置く
        if make_move(board, row, col, current_color):
            # 手番を交代する
            current_color = '●' if current_color == '○' else '○'
        else:
            print("その場所には石を置けません。もう一度選んでください。
        # ゲーム終了の条件を判定する
        if not any(' ' in row for row in board):
            break
    print_board(board)
    print("ゲーム終了！")
play_game()
