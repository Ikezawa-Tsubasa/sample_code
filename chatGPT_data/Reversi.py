import copy
# ゲーム盤の初期化
def initialize_board():
    board = [[0 for i in range(8)] for j in range(8)]
    board[3][3] = 1
    board[3][4] = -1
    board[4][3] = -1
    board[4][4] = 1
    return board
# ゲーム盤の表示
def print_board(board):
    print("  0 1 2 3 4 5 6 7")
    for i in range(8):
        row = str(i) + " "
        for j in range(8):
            if board[i][j] == 0:
                row += ". "
            elif board[i][j] == 1:
                row += "O "
            else:
                row += "X "
        print(row)
# 石を置ける場所を探す
def find_valid_moves(board, player):
    valid_moves = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        if is_valid_move(board, i, j, di, dj, player):
                            valid_moves.append((i, j))
                            break
    return valid_moves
# 石を置けるかどうかを判定
def is_valid_move(board, i, j, di, dj, player):
    if i + di < 0 or i + di > 7 or j + dj < 0 or j + dj > 7:
        return False
    if board[i+di][j+dj] == -player:
        x = i + 2 * di
        y = j + 2 * dj
        while x >= 0 and x <= 7 and y >= 0 and y <= 7:
            if board[x][y] == 0:
                return False
            if board[x][y] == player:
                return True
            x += di
            y += dj
    return False
# 石を置く
def make_move(board, i, j, player):
    board[i][j] = player
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            if is_valid_move(board, i, j, di, dj, player):
                x = i + di
                y = j + dj
                while board[x][y] == -player:
                    board[x][y] = player
                    x += di
                    y += dj
# ゲームのメイン処理
def main():
    board = initialize_board()
    player = 1
    while True:
        print_board(board)
        valid_moves = find_valid_moves(board, player)
        if len(valid_moves) == 0:
            print("Player", player, "has no valid moves")
            player = -player
            valid_moves = find_valid_moves(board, player)
            if len(valid_moves) == 0:
                print("Game over")
                break
        print("Player", player, "turn")
        print("Valid moves:", valid_moves)
        i, j = map(int, input("Enter move (row, col): ").split())
        if (i, j) not in valid_moves:
            print("Invalid move")
            continue
        make_move(board, i, j, player)
        player = -player
if __name__ == "__main__":
    main()
