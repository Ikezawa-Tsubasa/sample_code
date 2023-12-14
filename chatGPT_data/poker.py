import random
# ポーカーのカードの種類と数字
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
# ポーカーのカードを表すクラス
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)
# ポーカーのデッキを表すクラス
class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        return self.cards.pop()
# ポーカーの手札を表すクラス
class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)
# ポーカーのゲームを表すクラス
class Poker:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
    def deal_cards(self):
        for i in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())
    def player_turn(self):
        while True:
            print("Your hand: {}".format(self.player_hand))
            choice = input("Do you want to hit or stand? ")
            if choice.lower() == "hit":
                self.player_hand.add_card(self.deck.deal())
                if self.get_hand_value(self.player_hand) > 21:
                    print("Bust! You lose.")
                    return False
            elif choice.lower() == "stand":
                return True
            else:
                print("Invalid choice.")
    def dealer_turn(self):
        while self.get_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.add_card(self.deck.deal())
        print("Dealer\'s hand: {}".format(self.dealer_hand))
    def get_hand_value(self, hand):
        value = 0
        num_aces = 0
        for card in hand.cards:
            if card.rank == "Ace":
                num_aces += 1
                value += 11
            elif card.rank in ["Jack", "Queen", "King"]:
                value += 10
            else:
                value += int(card.rank)
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1
        return value
    def determine_winner(self):
        player_value = self.get_hand_value(self.player_hand)
        dealer_value = self.get_hand_value(self.dealer_hand)
        if player_value > 21:
            print("You lose.")
        elif dealer_value > 21:
            print("You win!")
        elif player_value > dealer_value:
            print("You win!")
        elif player_value < dealer_value:
            print("You lose.")
        else:
            print("Push.")
    def play(self):
        print("Let\'s play poker!")
        self.deal_cards()
        if not self.player_turn():
            return
        self.dealer_turn()
        self.determine_winner()
# ポーカーをプレイする
game = Poker()
game.play()
