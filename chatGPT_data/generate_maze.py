import random
# 迷路のサイズを設定
MAZE_SIZE = 10
# 迷路を生成する関数
def generate_maze(size):
    maze = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                row.append(1)
            else:
                row.append(0)
        maze.append(row)
    # 迷路の外周を壁にする
    for i in range(size):
        maze[0][i] = 1
        maze[size - 1][i] = 1
        maze[i][0] = 1
        maze[i][size - 1] = 1
    # 迷路をランダムに生成する
    for i in range(2, size - 2, 2):
        for j in range(2, size - 2, 2):
            maze[i][j] = 1
            while True:
                direction = random.randint(0, 3)
                if direction == 0 and maze[i - 1][j] == 0:
                    maze[i - 1][j] = 1
                    break
                elif direction == 1 and maze[i][j + 1] == 0:
                    maze[i][j + 1] = 1
                    break
                elif direction == 2 and maze[i + 1][j] == 0:
                    maze[i + 1][j] = 1
                    break
                elif direction == 3 and maze[i][j - 1] == 0:
                    maze[i][j - 1] = 1
                    break
    return maze
# 迷路を表示する関数
def print_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 1:
                print("#", end="")
            else:
                print(".", end="")
        print()
# メイン処理
maze = generate_maze(MAZE_SIZE)
print_maze(maze)
