import random
# カードのスートを表す定数
SPADES = 'spades'
HEARTS = 'hearts'
DIAMONDS = 'diamonds'
CLUBS = 'clubs'
# カードの数字を表す定数
ACE = 'ace'
TWO = 'two'
THREE = 'three'
FOUR = 'four'
FIVE = 'five'
SIX = 'six'
SEVEN = 'seven'
EIGHT = 'eight'
NINE = 'nine'
TEN = 'ten'
JACK = 'jack'
QUEEN = 'queen'
KING = 'king'
# カードを表すクラス
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)
# ソリティアの盤面を表すクラス
class Board:
    def __init__(self):
        self.stock = []
        self.waste = []
        self.foundations = {
            SPADES: [],
            HEARTS: [],
            DIAMONDS: [],
            CLUBS: []
        }
        self.tableaus = [[] for _ in range(7)]
        self.create_deck()
        self.deal_cards()
    # カードを生成する
    def create_deck(self):
        ranks = [ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING]
        for suit in [SPADES, HEARTS, DIAMONDS, CLUBS]:
            for rank in ranks:
                self.stock.append(Card(suit, rank))
    # カードを配る
    def deal_cards(self):
        random.shuffle(self.stock)
        for i in range(len(self.tableaus)):
            for j in range(i+1):
                card = self.stock.pop()
                if j == i:
                    card_state = 'face_up'
                else:
                    card_state = 'face_down'
                self.tableaus[i].append((card, card_state))
    # ゲームを実行する
    def play(self):
        while True:
            self.display()
            command = input('Enter command (h for help): ')
            if command == 'q':
                break
            elif command == 'h':
                self.display_help()
            elif command == 'r':
                self.reset()
            elif command == 's':
                self.stock_to_waste()
            elif command.startswith('f'):
                self.move_to_foundation(command)
            elif command.startswith('t'):
                self.move_within_tableau(command)
            else:
                print('Invalid command')
            if self.check_win():
                print('You win!')
                break
    # 盤面を表示する
    def display(self):
        print('Stock: {} cards'.format(len(self.stock)))
        print('Waste: {}'.format(self.waste[-1] if self.waste else ''))
        print('Foundations:')
        for suit in [SPADES, HEARTS, DIAMONDS, CLUBS]:
            print('{}: {}'.format(suit.capitalize(), self.foundations[suit]))
        print('Tableaus:')
        for i, tableau in enumerate(self.tableaus):
            print('{}: {}'.format(i+1, [str(card) if state == 'face_up' else 'X' for card, state in tableau]))
    # ヘルプを表示する
    def display_help(self):
        print('Commands:')
        print('h - display help')
        print('q - quit game')
        print('r - reset game')
        print('s - move card from stock to waste')
        print('f <card> - move card to foundation (e.g. f 5 of spades)')
        print('t <tableau> <card> <destination> - move card within tableau (e.g. t 1 5 of spades 2)')
    # ゲームをリセットする
    def reset(self):
        self.__init__()
    # ストックからワーストにカードを移動する
    def stock_to_waste(self):
        if not self.stock:
            self.stock = self.waste[:-1]
            self.waste = [self.waste[-1]]
        else:
            self.waste.append(self.stock.pop())
    # カードをファンデーションに移動する
    def move_to_foundation(self, command):
        parts = command.split()
        if len(parts) != 2:
            print('Invalid command')
            return
        rank, suit = parts[1], parts[2]
        for tableau in self.tableaus:
            if tableau and str(tableau[-1][0]) == '{} of {}'.format(rank, suit):
                card, _ = tableau.pop()
                self.foundations[suit].append(card)
                return
        if self.waste and str(self.waste[-1]) == '{} of {}'.format(rank, suit):
            card = self.waste.pop()
            self.foundations[suit].append(card)
            if not self.waste:
                self.stock_to_waste()
    # カードをテーブル内で移動する
    def move_within_tableau(self, command):
        parts = command.split()
        if len(parts) != 4:
            print('Invalid command')
            return
        source, source_index, dest, dest_index = parts[1], int(parts[2])-1, parts[3], int(parts[4])-1
        source_tableau = self.tableaus[source_index]
        dest_tableau = self.tableaus[dest_index]
        if source_tableau and source_tableau[-1][1] == 'face_down':
            print('Cannot move face-down card')
            return
        if dest_tableau and dest_tableau[-1][1] == 'face_down':
            print('Cannot move to face-down card')
            return
        if source == dest and source_index == dest_index:
            print('Cannot move card to same tableau')
            return
        cards_to_move = []
        for i in range(source_index, len(source_tableau)):
            cards_to_move.append(source_tableau[i])
        if not self.is_valid_move(cards_to_move, dest_tableau):
            print('Invalid move')
            return
        for i in range(source_index, len(source_tableau)):
            dest_tableau.append(source_tableau[i])
        source_tableau[source_index:] = []
        if source_tableau and source_tableau[-1][1] == 'face_down':
            source_tableau[-1] = (source_tableau[-1][0], 'face_up')
    # 移動が有効かどうかをチェックする
    def is_valid_move(self, cards, tableau):
        if not tableau:
            return cards[0][0].rank == KING
        top_card, _ = tableau[-1]
        bottom_card, _ = cards[0]
        if bottom_card.rank == ACE and top_card.rank == KING:
            return False
        if bottom_card.rank != top_card.rank - 1:
            return False
        if bottom_card.suit == top_card.suit:
            return False
        return True
    # 勝利条件をチェックする
    def check_win(self):
        for suit in [SPADES, HEARTS, DIAMONDS, CLUBS]:
            if len(self.foundations[suit]) != 13:
                return False
        return True
# ゲームを開始する
board = Board()
board.play()
