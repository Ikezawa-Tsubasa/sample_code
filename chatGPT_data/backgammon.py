# バックギャモンのプログラム
import random
# 初期化
board = [0 for i in range(24)]
board[0] = 2
board[5] = -5
board[7] = -3
board[11] = -5
board[12] = 5
board[16] = 3
board[18] = 5
board[23] = -2
player = 1
dice = [0, 0]
game_over = False
# 関数定義
def print_board():
    print(" 13 14 15 16 17 18    19 20 21 22 23 24")
    print("+--+--+--+--+--+--+  +--+--+--+--+--+--+")
    for i in range(5):
        row1 = "|"
        row2 = "|"
        for j in range(12):
            if i == 2 and j == 5:
                row1 += "BAR|"
            elif i == 2 and j == 11:
                row2 += "BAR|"
            else:
                if board[j] >= i+1:
                    row1 += "O |"
                else:
                    row1 += "  |"
                if board[j] <= -i-1:
                    row2 += "X |"
                else:
                    row2 += "  |"
        print(row1, " ", i+1)
        print(row2, " ", 24-i)
    row1 = "|"
    row2 = "|"
    for j in range(12):
        if board[j] >= 6:
            row1 += "O |"
        else:
            row1 += "  |"
        if board[j] <= -6:
            row2 += "X |"
        else:
            row2 += "  |"
    print(row1, " 6")
    print(row2, " 19")
    print("+--+--+--+--+--+--+  +--+--+--+--+--+--+")
    print(" 12 11 10  9  8  7     6  5  4  3  2  1")
def roll_dice():
    return [random.randint(1, 6), random.randint(1, 6)]
def check_move(start, end):
    if start < 0 or start > 23 or end < 0 or end > 23:
        return False
    if board[start] == 0 or (board[start] > 0 and player == 2) or (board[start] < 0 and player == 1):
        return False
    if board[end] < -1 and player == 1 or board[end] > 1 and player == 2:
        return False
    if abs(end-start) not in dice:
        return False
    return True
def move(start, end):
    board[start] -= 1
    if board[end] == -1 and player == 1:
        board[end] = 1
        board[24] -= 1
    elif board[end] == 1 and player == 2:
        board[end] = -1
        board[0] += 1
    else:
        board[end] += 1
def check_bear_off():
    if player == 1:
        for i in range(18):
            if board[i] > 0:
                return False
        for i in range(6):
            if board[i] >= 1:
                return False
        return True
    else:
        for i in range(6, 24):
            if board[i] < 0:
                return False
        for i in range(18, 24):
            if board[i] <= -1:
                return False
        return True
def bear_off(start):
    board[start] -= 1
    if player == 1:
        board[24] -= 1
    else:
        board[0] += 1
# ゲームループ
while not game_over:
    # プレイヤーの入力
    print_board()
    print("Player ", player, "のターンです。")
    dice = roll_dice()
    print("ダイスの目は", dice, "です。")
    if all([board[i] <= 0 for i in range(18)]) and player == 1:
        moves = []
        for i in range(18):
            if board[i] > 0 and check_move(i, i+dice[0]):
                moves.append((i, i+dice[0]))
            if board[i] > 0 and check_move(i, i+dice[1]):
                moves.append((i, i+dice[1]))
            if board[i] > 0 and check_move(i, i+dice[0]+dice[1]):
                moves.append((i, i+dice[0]+dice[1]))
        if len(moves) == 0:
            print("動ける場所がありません。")
            continue
        print("動ける場所は", moves, "です。")
        move_start, move_end = moves[int(input("どこからどこに動かしますか？(0-" + str(len(moves)-1) + ") "))]
    elif all([board[i] >= 0 for i in range(6, 24)]) and player == 2:
        moves = []
        for i in range(6, 24):
            if board[i] > 0 and check_move(i, i-dice[0]):
                moves.append((i, i-dice[0]))
            if board[i] > 0 and check_move(i, i-dice[1]):
                moves.append((i, i-dice[1]))
            if board[i] > 0 and check_move(i, i-dice[0]-dice[1]):
                moves.append((i, i-dice[0]-dice[1]))
        if len(moves) == 0:
            print("動ける場所がありません。")
            continue
        print("動ける場所は", moves, "です。")
        move_start, move_end = moves[int(input("どこからどこに動かしますか？(0-" + str(len(moves)-1) + ") "))]
    else:
        moves = []
        for i in range(24):
            if board[i] > 0:
                if check_move(i, i+dice[0]):
                    moves.append((i, i+dice[0]))
                if check_move(i, i+dice[1]):
                    moves.append((i, i+dice[1]))
                if check_move(i, i+dice[0]+dice[1]):
                    moves.append((i, i+dice[0]+dice[1]))
        if len(moves) == 0:
            print("動ける場所がありません。")
            continue
        print("動ける場所は", moves, "です。")
        move_start, move_end = moves[int(input("どこからどこに動かしますか？(0-" + str(len(moves)-1) + ") "))]
    # 移動の実行
    move(move_start, move_end)
    # ベアオフのチェック
    if check_bear_off():
        if player == 1:
            bear_off_start = int(input("どこからベアオフしますか？(1-6) "))
            if board[bear_off_start-1] > 0:
                bear_off(bear_off_start-1)
            else:
                print("そこには駒がありません。")
                continue
        else:
            bear_off_start = int(input("どこからベアオフしますか？(19-24) "))
            if board[bear_off_start-1] < 0:
                bear_off(bear_off_start-1)
            else:
                print("そこには駒がありません。")
                continue
    # 勝敗のチェック
    if all([board[i] <= 0 for i in range(18)]):
        print_board()
        print("Player 1の勝利です！")
        game_over = True
    elif all([board[i] >= 0 for i in range(6, 24)]):
        print_board()
        print("Player 2の勝利です！")
        game_over = True
    # プレイヤーの交代
    else:
        player = 3 - player
