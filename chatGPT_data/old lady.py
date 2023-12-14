import random
# カードの初期化
suits = ['♠', '♥', '♦', '♣']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards = [suit + rank for suit in suits for rank in ranks]
# プレイヤーの初期化
players = []
num_players = int(input("プレイヤーの人数を入力してください: "))
for i in range(num_players):
    name = input("プレイヤー{}の名前を入力してください: ".format(i+1))
    players.append({'name': name, 'hand': []})
# カードをシャッフルして配る
random.shuffle(cards)
for i in range(len(cards)):
    players[i % num_players]['hand'].append(cards[i])
# ゲーム開始
while True:
    # プレイヤーの手札を表示
    for player in players:
        print("{}の手札: {}".format(player['name'], player['hand']))
    # プレイヤーがカードを引く
    for i in range(num_players):
        if len(players[i]['hand']) == 0:
            continue
        target_player = random.choice([j for j in range(num_players) if j != i])
        card = random.choice(players[target_player]['hand'])
        players[i]['hand'].append(card)
        players[target_player]['hand'].remove(card)
        print("{}が{}から{}を引きました".format(players[i]['name'], players[target_player]['name'], card))
    # 手札が0枚になったプレイヤーを探す
    losers = [player['name'] for player in players if len(player['hand']) == 0]
    if len(losers) > 0:
        print("ゲーム終了！")
        print("負けたプレイヤー: {}".format(losers))
        break
