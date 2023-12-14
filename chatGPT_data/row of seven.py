# 七ならべのプログラム
# 初期化
board = [[0 for j in range(7)] for i in range(7)]
player = 1
game_over = False
# 関数定義
def print_board():
    for row in board:
        print(row)
def check_win():
    # 横方向のチェック
    for row in board:
        for i in range(4):
            if row[i:i+4] == [1,1,1,1]:
                return True
            elif row[i:i+4] == [2,2,2,2]:
                return True
    # 縦方向のチェック
    for i in range(7):
        for j in range(4):
            if [board[j+k][i] for k in range(4)] == [1,1,1,1]:
                return True
            elif [board[j+k][i] for k in range(4)] == [2,2,2,2]:
                return True
    # 斜め方向のチェック
    for i in range(4):
        for j in range(4):
            if [board[i+k][j+k] for k in range(4)] == [1,1,1,1]:
                return True
            elif [board[i+k][j+k] for k in range(4)] == [2,2,2,2]:
                return True
    for i in range(4):
        for j in range(3,7):
            if [board[i+k][j-k] for k in range(4)] == [1,1,1,1]:
                return True
            elif [board[i+k][j-k] for k in range(4)] == [2,2,2,2]:
                return True
    return False
# ゲームループ
while not game_over:
    # プレイヤーの入力
    print_board()
    print("Player ", player, "のターンです。")
    col = int(input("どの列に置きますか？(1-7) "))
    row = 6
    while row >= 0:
        if board[row][col-1] == 0:
            board[row][col-1] = player
            break
        row -= 1
    if row < 0:
        print("その列は既に埋まっています。")
        continue
    # 勝敗のチェック
    if check_win():
        print_board()
        print("Player ", player, "の勝利です！")
        game_over = True
    # 引き分けのチェック
    elif all([0 not in row for row in board]):
        print_board()
        print("引き分けです。")
        game_over = True
    # プレイヤーの交代
    else:
        player = 3 - player
