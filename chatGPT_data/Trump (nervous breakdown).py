import random
def create_deck():
    suits = ['♠', '♣', '♦', '♥']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [(suit, rank) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck
def play_game():
    deck = create_deck()
    board = []
    matched_pairs = 0
    while matched_pairs < 13:
        print_board(board)
        # プレイヤーにカードを2枚選んでもらう
        index1 = get_card_index(board)
        index2 = get_card_index(board)
        # 選んだ2枚のカードが一致した場合
        if board[index1] == board[index2]:
            print("一致しました！")
            matched_pairs += 1
            board[index1] = None
            board[index2] = None
        else:
            print("一致しませんでした。
        print()
    print("ゲームクリア！おめでとうございます！")
def print_board(board):
    for i, card in enumerate(board):
        if card is None:
            print(f"{i+1}:   ")
        else:
            print(f"{i+1}: {card[0]}{card[1]}")
def get_card_index(board):
    while True:
        try:
            index = int(input("カードの番号を選んでください: ")) - 1
            if index < 0 or index >= len(board) or board[index] is None:
                raise ValueError
            return index
        except ValueError:
            print("無効な入力です。もう一度入力してください。
play_game()
