import random
# ぷよの種類を定義
PuyoType = ["R", "G", "B", "Y"]
# ぷよのクラス
class Puyo:
    def __init__(self, puyo_type):
        self.type = puyo_type
    def __str__(self):
        return self.type
# ぷよぷよのフィールドクラス
class PuyoField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.field = [[None for _ in range(width)] for _ in range(height)]
        self.current_puyo = None
        self.next_puyo = None
        self.score = 0
    # ぷよを落とす関数
    def drop_puyo(self):
        if self.current_puyo is None:
            self.current_puyo = Puyo(random.choice(PuyoType))
            self.next_puyo = Puyo(random.choice(PuyoType))
        else:
            self.current_puyo = self.next_puyo
            self.next_puyo = Puyo(random.choice(PuyoType))
        # ぷよをフィールドの上部に配置する
        x = self.width // 2
        y = 0
        if self.field[y][x] is not None or self.field[y + 1][x] is not None:
            return False
        self.field[y][x] = self.current_puyo
        self.field[y + 1][x] = Puyo(random.choice(PuyoType))
        return True
    # ぷよを移動する関数
    def move_puyo(self, dx):
        if self.current_puyo is None:
            return False
        # ぷよを移動する
        x = self.width // 2 + dx
        y = 0
        if x < 0 or x > self.width - 1 or self.field[y][x] is not None or self.field[y + 1][x] is not None:
            return False
        self.field[y][x] = self.current_puyo
        self.field[y + 1][x] = Puyo(random.choice(PuyoType))
        self.field[y][self.width // 2] = None
        self.field[y + 1][self.width // 2] = None
        return True
    # ぷよを回転する関数
    def rotate_puyo(self):
        if self.current_puyo is None:
            return False
        # ぷよを回転する
        x = self.width // 2
        y = 0
        if self.current_puyo.type == "R":
            if y + 2 > self.height - 1 or self.field[y + 2][x] is not None:
                return False
            self.field[y][x] = None
            self.field[y + 2][x] = self.current_puyo
            self.field[y + 1][x - 1] = self.field[y][x + 1]
            self.field[y + 1][x + 1] = self.field[y + 1][x]
            self.field[y + 1][x] = self.current_puyo
        elif self.current_puyo.type == "G":
            if x - 1 < 0 or self.field[y + 1][x - 1] is not None or self.field[y + 2][x] is not None:
                return False
            self.field[y][x] = None
            self.field[y + 2][x] = self.current_puyo
            self.field[y + 1][x - 1] = self.current_puyo
            self.field[y + 1][x + 1] = self.field[y][x + 1]
            self.field[y + 1][x] = None
        elif self.current_puyo.type == "B":
            if x + 1 > self.width - 1 or self.field[y + 1][x + 1] is not None or self.field[y + 2][x] is not None:
                return False
            self.field[y][x] = None
            self.field[y + 2][x] = self.current_puyo
            self.field[y + 1][x - 1] = self.field[y][x + 1]
            self.field[y + 1][x + 1] = self.current_puyo
            self.field[y + 1][x] = None
        elif self.current_puyo.type == "Y":
            if y + 2 > self.height - 1 or self.field[y + 2][x] is not None:
                return False
            self.field[y][x] = None
            self.field[y + 2][x] = self.current_puyo
            self.field[y + 1][x - 1] = self.field[y][x + 1]
            self.field[y + 1][x + 1] = self.current_puyo
            self.field[y + 1][x] = None
        return True
    # ぷよを落とす関数
    def drop_puyo_down(self):
        if self.current_puyo is None:
            return False
        # ぷよを落とす
        x = self.width // 2
        y = 0
        while y < self.height - 1 and (self.field[y + 2][x] is None and self.field[y + 1][x] is None):
            y += 1
        self.field[y][x] = self.current_puyo
        self.field[y + 1][x] = Puyo(random.choice(PuyoType))
        self.field[0][x] = None
        self.field[1][x] = None
        # ぷよを消す
        count = 0
        while True:
            erase_list = self.get_erase_list()
            if len(erase_list) == 0:
                break
            count += len(erase_list)
            self.erase_puyo(erase_list)
            self.drop_puyo_after_erase()
        # スコアを加算する
        if count > 0:
            self.score += 10 * (2 ** (count - 1))
        return True
    # 消せるぷよのリストを取得する関数
    def get_erase_list(self):
        erase_list = []
        for i in range(self.height):
            for j in range(self.width):
                if self.field[i][j] is not None:
                    erase_list += self.get_same_color_puyo_list(i, j)
        erase_list = list(set(erase_list))
        return erase_list
    # 同じ色のぷよのリストを取得する関数
    def get_same_color_puyo_list(self, y, x):
        puyo_type = self.field[y][x].type
        same_color_puyo_list = [(y, x)]
        if y > 0 and self.field[y - 1][x] is not None and self.field[y - 1][x].type == puyo_type:
            same_color_puyo_list += self.get_same_color_puyo_list(y - 1, x)
        if y < self.height - 1 and self.field[y + 1][x] is not None and self.field[y + 1][x].type == puyo_type:
            same_color_puyo_list += self.get_same_color_puyo_list(y + 1, x)
        if x > 0 and self.field[y][x - 1] is not None and self.field[y][x - 1].type == puyo_type:
            same_color_puyo_list += self.get_same_color_puyo_list(y, x - 1)
        if x < self.width - 1 and self.field[y][x + 1] is not None and self.field[y][x + 1].type == puyo_type:
            same_color_puyo_list += self.get_same_color_puyo_list(y, x + 1)
        return same_color_puyo_list
    # ぷよを消す関数
    def erase_puyo(self, erase_list):
        for y, x in erase_list:
            self.field[y][x] = None
    # ぷよを落とす関数
    def drop_puyo_after_erase(self):
        for j in range(self.width):
            for i in range(self.height - 1, 0, -1):
                if self.field[i][j] is None:
                    for k in range(i - 1, -1, -1):
                        if self.field[k][j] is not None:
                            self.field[i][j] = self.field[k][j]
                            self.field[k][j] = None
                            break
    # フィールドを表示する関数
    def print_field(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.field[i][j] is None:
                    print(".", end="")
                else:
                    print(str(self.field[i][j]), end="")
            print()
        print("Score:", self.score)
# メイン処理
field = PuyoField(6, 12)
while True:
    if not field.drop_puyo():
        print("Game Over")
        break
    field.print_field()
    command = input("Command (L/R/A/D): ")
    if command == "L":
        field.move_puyo(-1)
    elif command == "R":
        field.move_puyo(1)
    elif command == "A":
        field.rotate_puyo()
    elif command == "D":
        field.drop_puyo_down()
    else:
        print("Invalid command")
