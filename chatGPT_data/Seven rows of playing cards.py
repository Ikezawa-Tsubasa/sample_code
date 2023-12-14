import random
import time
# トランプのカードを表すクラス
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.suit}{self.rank}"
# トランプのデッキを表すクラス
class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["♠", "♥", "♦", "♣"]:
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def deal_card(self):
        return self.cards.pop()
# スピードのゲームを表すクラス
class Speed:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.pile1 = []
        self.pile2 = []
        self.players = [[], []]
        self.finished = False
    def play(self):
        while not self.finished:
            self.print_table()
            self.draw_cards()
            self.play_cards()
            self.check_win()
    def draw_cards(self):
        for i in range(2):
            while len(self.players[i]) < 5:
                card = self.deck.deal_card()
                self.players[i].append(card)
    def play_cards(self):
        for i in range(2):
            print(f"Player {i+1}\'s turn")
            print("Your cards:", \' \'.join(str(card) for card in self.players[i]))
            while True:
                card = input("Enter a card to play (or \'draw\' to draw a card): ")
                if card == "draw":
                    if len(self.deck.cards) == 0:
                        print("No more cards in deck, cannot draw.")
                        continue
                    else:
                        drawn_card = self.deck.deal_card()
                        print(f"Drawn card: {drawn_card}")
                        self.players[i].append(drawn_card)
                        break
                else:
                    try:
                        card = Card(card[0], int(card[1:]))
                    except:
                        print("Invalid card, try again.")
                        continue
                    if card not in self.players[i]:
                        print("You don\'t have that card, try again.")
                        continue
                    if not self.is_valid_move(card):
                        print("Invalid move, try again.")
                        continue
                    self.players[i].remove(card)
                    if i == 0:
                        self.pile1.append(card)
                    else:
                        self.pile2.append(card)
                    break
    def is_valid_move(self, card):
        if len(self.pile1) == 0 and len(self.pile2) == 0:
            return True
        elif len(self.pile1) == 0:
            return card.rank == self.pile2[-1].rank - 1
        elif len(self.pile2) == 0:
            return card.rank == self.pile1[-1].rank - 1
        else:
            return card.rank == self.pile1[-1].rank - 1 or card.rank == self.pile2[-1].rank - 1
    def check_win(self):
        if len(self.players[0]) == 0 and len(self.players[1]) == 0:
            self.finished = True
            print("Game over!")
            if len(self.deck.cards) == 0:
                print("No more cards in deck, game ends in a draw.")
            elif len(self.pile1) == 0 or len(self.pile2) == 0:
                print("One of the piles is empty, game ends in a draw.")
            elif self.pile1[-1].rank == 1 or self.pile2[-1].rank == 1:
                print("One of the piles has a king, game ends in a draw.")
            elif self.pile1[-1].rank == 13 and self.pile2[-1].rank == 13:
                print("Both piles have a king, game ends in a draw.")
            elif self.pile1[-1].rank == 13:
                print("Player 1 wins!")
            elif self.pile2[-1].rank == 13:
                print("Player 2 wins!")
            else:
                print("Game ends in a draw.")
    def print_table(self):
        print("Pile 1:", \' \'.join(str(card) for card in self.pile1))
        print("Pile 2:", \' \'.join(str(card) for card in self.pile2))
        print()
# ゲームを開始する
game = Speed()
game.play()
