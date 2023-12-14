# ゲーム盤の初期化
board = [[" " for _ in range(3)] for _ in range(3)]
# プレイヤーの初期化
current_player = "X"
# ゲームの状態
game_over = False
winner = None
# ゲームループ
while not game_over:
    # ゲーム盤の表示
    for row in board:
        print("|".join(row))
        print("-" * 5)
    # 現在のプレイヤーの入力を受け付ける
    row = int(input("行を選んでください (0-2): "))
    col = int(input("列を選んでください (0-2): "))
    # 入力の妥当性をチェック
    if board[row][col] != " ":
        print("その場所は既に埋まっています。別の場所を選んでください。
        continue
    # プレイヤーのマークをゲーム盤に配置
    board[row][col] = current_player
    # 勝利条件のチェック
    # 行のチェック
    if board[row][0] == board[row][1] == board[row][2] != " ":
        game_over = True
        winner = current_player
    # 列のチェック
    elif board[0][col] == board[1][col] == board[2][col] != " ":
        game_over = True
        winner = current_player
    # 対角線のチェック
    elif board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        game_over = True
        winner = current_player
    # 引き分けのチェック
    elif all(board[i][j] != " " for i in range(3) for j in range(3)):
        game_over = True
    # プレイヤーの交代
    current_player = "O" if current_player == "X" else "X"
# ゲーム結果の表示
for row in board:
    print("|".join(row))
    print("-" * 5)
if winner:
    print(f"{winner}の勝利です！")
else:
    print("引き分けです。
