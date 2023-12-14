# ゲーム盤の初期化
def initialize_board():
    board = [[0 for i in range(9)] for j in range(9)]
    return board
# ゲーム盤の表示
def print_board(board):
    for row in board:
        print(row)
# 行、列、ブロックに数字が重複していないかを判定
def is_valid(board, row, col, num):
    # 行に数字が重複していないかを判定
    for i in range(9):
        if board[row][i] == num:
            return False
    # 列に数字が重複していないかを判定
    for i in range(9):
        if board[i][col] == num:
            return False
    # ブロックに数字が重複していないかを判定
    block_row = (row // 3) * 3
    block_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[block_row+i][block_col+j] == num:
                return False
    return True
# ナンプレを解く
def solve(board, row, col):
    if row == 9:
        return True
    if col == 9:
        return solve(board, row+1, 0)
    if board[row][col] != 0:
        return solve(board, row, col+1)
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve(board, row, col+1):
                return True
            board[row][col] = 0
    return False
# ゲームのメイン処理
def main():
    board = initialize_board()
    board[0] = [5, 3, 0, 0, 7, 0, 0, 0, 0]
    board[1] = [6, 0, 0, 1, 9, 5, 0, 0, 0]
    board[2] = [0, 9, 8, 0, 0, 0, 0, 6, 0]
    board[3] = [8, 0, 0, 0, 6, 0, 0, 0, 3]
    board[4] = [4, 0, 0, 8, 0, 3, 0, 0, 1]
    board[5] = [7, 0, 0, 0, 2, 0, 0, 0, 6]
    board[6] = [0, 6, 0, 0, 0, 0, 2, 8, 0]
    board[7] = [0, 0, 0, 4, 1, 9, 0, 0, 5]
    board[8] = [0, 0, 0, 0, 8, 0, 0, 7, 9]
    print("Original board:")
    print_board(board)
    if solve(board, 0, 0):
        print("Solved board:")
        print_board(board)
    else:
        print("No solution found")
if __name__ == "__main__":
    main()
