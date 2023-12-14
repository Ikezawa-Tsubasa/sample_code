import random
# プレイヤーのクラス
class Player:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
    
    def take_damage(self, damage):
        # ダメージを受ける処理
        actual_damage = max(damage - self.defense, 0)
        self.hp -= actual_damage
    
    def attack_enemy(self, enemy):
        # 敵を攻撃する処理
        damage = random.randint(self.attack - 3, self.attack + 3)
        enemy.take_damage(damage)
        print(f"{self.name}の攻撃！ {enemy.name}に{damage}のダメージを与えた！")
# 敵のクラス
class Enemy:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
    
    def take_damage(self, damage):
        # ダメージを受ける処理
        actual_damage = max(damage - self.defense, 0)
        self.hp -= actual_damage
    
    def attack_player(self, player):
        # プレイヤーを攻撃する処理
        damage = random.randint(self.attack - 3, self.attack + 3)
        player.take_damage(damage)
        print(f"{self.name}の攻撃！ {player.name}に{damage}のダメージを与えた！")
# プレイヤーと敵の作成
player = Player("勇者", 100, 20, 10)
enemy = Enemy("スライム", 50, 10, 5)
# ゲームループ
while player.hp > 0 and enemy.hp > 0:
    # プレイヤーの攻撃
    player.attack_enemy(enemy)
    
    # 敵の攻撃
    enemy.attack_player(player)
    
    # ステータス表示
    print(f"{player.name}: HP {player.hp}")
    print(f"{enemy.name}: HP {enemy.hp}")
    print()
# ゲーム終了時のメッセージ
if player.hp > 0:
    print(f"{player.name}の勝利！")
else:
    print(f"{enemy.name}の勝利！")
