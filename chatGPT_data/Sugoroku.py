import random
# すごろくのマス目
board = [
    "Start", "Eel", "Bridge", "Fox", "Goose", "Well", "Boar", "Rabbit", "Moon", "Goose",
    "Fox", "Well", "Rabbit", "Eel", "Bridge", "Moon", "Boar", "Goose", "Well", "Fox",
    "Rabbit", "Eel", "Moon", "Boar", "Bridge", "Well", "Goose", "Fox", "Rabbit", "Finish"
]
# プレイヤーを表すクラス
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
    def move(self, steps):
        self.position += steps
        if self.position >= len(board):
            self.position = len(board) - 1
        print("{} moves to {}.".format(self.name, board[self.position]))
# すごろくのゲームを表すクラス
class Sugoroku:
    def __init__(self, num_players):
        self.players = []
        for i in range(num_players):
            name = input("Enter player {}\'s name: ".format(i+1))
            player = Player(name)
            self.players.append(player)
    def play(self):
        print("Let\'s play sugoroku!")
        while True:
            for player in self.players:
                input("{}\'s turn. Press enter to roll the dice.".format(player.name))
                steps = random.randint(1, 6)
                player.move(steps)
                if player.position == len(board) - 1:
                    print("{} wins!".format(player.name))
                    return
# すごろくをプレイする
game = Sugoroku(2)
game.play()
