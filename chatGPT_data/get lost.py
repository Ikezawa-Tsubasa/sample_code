import random
# 迷路のクラス
class Maze:
    def __init__(self, size):
        self.size = size
        self.maze = [[1] * (size + 2) for _ in range(size + 2)]
        self.visited = [[False] * (size + 2) for _ in range(size + 2)]
        self.start_row = 1
        self.start_col = 1
        self.goal_row = size
        self.goal_col = size
    
    def generate(self, row, col):
        # 迷路を生成する処理
        self.visited[row][col] = True
        directions = ["up", "down", "left", "right"]
        random.shuffle(directions)
        
        for direction in directions:
            if direction == "up":
                if not self.visited[row - 2][col]:
                    self.maze[row - 2][col] = 0
                    self.maze[row - 1][col] = 0
                    self.generate(row - 2, col)
            elif direction == "down":
                if not self.visited[row + 2][col]:
                    self.maze[row + 2][col] = 0
                    self.maze[row + 1][col] = 0
                    self.generate(row + 2, col)
            elif direction == "left":
                if not self.visited[row][col - 2]:
                    self.maze[row][col - 2] = 0
                    self.maze[row][col - 1] = 0
                    self.generate(row, col - 2)
            elif direction == "right":
                if not self.visited[row][col + 2]:
                    self.maze[row][col + 2] = 0
                    self.maze[row][col + 1] = 0
                    self.generate(row, col + 2)
    
    def print_maze(self):
        # 迷路を表示する処理
        for row in range(1, self.size + 1):
            for col in range(1, self.size + 1):
                if self.maze[row][col] == 0:
                    print("  ", end=" ")
                else:
                    print("■", end=" ")
            print()
        print()
# 迷路の作成
maze = Maze(10)
maze.generate(maze.start_row, maze.start_col)
# ゲームループ
while True:
    # 迷路の表示
    maze.print_maze()
    
    # プレイヤーの入力
    direction = input("上: u, 下: d, 左: l, 右: r > ")
    
    # プレイヤーの移動
    if direction == "u" and maze.maze[maze.start_row - 1][maze.start_col] == 0:
        maze.start_row -= 1
    elif direction == "d" and maze.maze[maze.start_row + 1][maze.start_col] == 0:
        maze.start_row += 1
    elif direction == "l" and maze.maze[maze.start_row][maze.start_col - 1] == 0:
        maze.start_col -= 1
    elif direction == "r" and maze.maze[maze.start_row][maze.start_col + 1] == 0:
        maze.start_col += 1
    
    # ゴールに到達したかどうかの判定
    if maze.start_row == maze.goal_row and maze.start_col == maze.goal_col:
        print("ゴールに到達しました！")
        break
