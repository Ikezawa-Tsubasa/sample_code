import random
# カードのデッキを作成する関数
def create_deck():
    suits = ['♠', '♣', '♦', '♥']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [(suit, rank) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck
# カードを表示する関数
def display_card(card):
    suit, rank = card
    print(f'{suit}{rank}', end=' ')
# ゲームを実行する関数
def play_game():
    deck = create_deck()
    player1 = deck[:26]
    player2 = deck[26:]
    pile = []
    while player1 and player2:
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        pile.extend([card1, card2])
        print('Player 1:', end=' ')
        display_card(card1)
        print()
        print('Player 2:', end=' ')
        display_card(card2)
        print()
        if ranks.index(card1[1]) > ranks.index(card2[1]):
            print('Player 1 wins the round!')
            player1.extend(pile)
            pile = []
        elif ranks.index(card1[1]) < ranks.index(card2[1]):
            print('Player 2 wins the round!')
            player2.extend(pile)
            pile = []
        else:
            print('It\'s a tie!')
    if player1:
        print('Player 1 wins the game!')
    else:
        print('Player 2 wins the game!')
# ゲームを実行する
play_game()
