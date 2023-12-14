# 盤面を初期化する
def initialize_board():
    board = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]
    return board
# 盤面を表示する
def print_board(board):
    print('  a b c d e f g h')
    print(' ┌───────────────┐')
    for i in range(8):
        print(f'{i+1}│', end='')
        for j in range(8):
            print(board[i][j], end='│')
        print('\
 ├─┼─┼─┼─┼─┼─┼─┼─┤')
    print(' └───────────────┘')
# 指定した座標に駒を移動する
def make_move(board, from_pos, to_pos):
    from_row, from_col = from_pos
    to_row, to_col = to_pos
    piece = board[from_row][from_col]
    board[from_row][from_col] = ' '
    board[to_row][to_col] = piece
# ゲームを実行する
def play_game():
    board = initialize_board()
    while True:
        print_board(board)
        # プレイヤーに移動元と移動先の座標を入力してもらう
        while True:
            try:
                from_pos = input("移動元の座標を入力してください (例: e2): ")
                to_pos = input("移動先の座標を入力してください (例: e4): ")
                from_col = ord(from_pos[0]) - ord('a')
                from_row = int(from_pos[1]) - 1
                to_col = ord(to_pos[0]) - ord('a')
                to_row = int(to_pos[1]) - 1
                if 0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("無効な入力です。もう一度入力してください。
        # 駒を移動する
        make_move(board, (from_row, from_col), (to_row, to_col))
        # ゲーム終了の条件を判定する
        if from_pos == 'e1' and to_pos == 'g1' and board[7][4] == 'K':
            print_board(board)
            print("白の勝ち！")
            break
        elif from_pos == 'e8' and to_pos == 'g8' and board[0][4] == 'k':
            print_board(board)
            print("黒の勝ち！")
            break
play_game()
