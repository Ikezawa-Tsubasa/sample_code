import random
# カードのスートとランクを定義
suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# カードのデッキを作成
deck = []
for suit in suits:
    for rank in ranks:
        deck.append(rank + suit)
# カードをシャッフル
random.shuffle(deck)
# プレイヤーの人数を入力
num_players = int(input("プレイヤーの人数を入力してください: "))
# プレイヤーごとの手札を格納するリストを作成
hands = [[] for _ in range(num_players)]
# カードを配る
for i in range(len(deck)):
    player = i % num_players
    hands[player].append(deck[i])
# 手札をソート
for i in range(num_players):
    hands[i].sort()
# 手札を表示
for i in range(num_players):
    print(f"プレイヤー{i+1}の手札: {', '.join(hands[i])}")
