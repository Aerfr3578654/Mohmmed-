import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Deck.suits for rank in Deck.ranks]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        card = deck.draw_card()
        self.hand.append(card)
        return card

    def show_hand(self):
        return [str(card) for card in self.hand]


class BasraGame:
    def __init__(self, player1, player2):
        self.deck = Deck()
        self.players = [Player(player1), Player(player2)]
        self.table = []

    def initial_deal(self):
        
        for player in self.players:
            for _ in range(4):
                player.draw(self.deck)
        for _ in range(4):
            self.table.append(self.deck.draw_card())

    def play_round(self):
        for player in self.players:
            print(f"{player.name}'s turn")
            print("Table:", [str(card) for card in self.table])
            print("Your hand:", player.show_hand())

           
            played_card = player.hand.pop(0)
            print(f"{player.name} played {played_card}")
            self.table.append(played_card)

            
            if any(card.rank == played_card.rank for card in self.table):
                print(f"{player.name} makes a Basra!")
                self.table = []  

    def start_game(self):
        self.initial_deal()
        while self.deck.cards:
            self.play_round()


game = BasraGame("Player 1", "Player 2")
game.start_game()