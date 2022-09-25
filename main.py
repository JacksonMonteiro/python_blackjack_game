import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(self.rank['rank'], self.suit)

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        ranks = [
            {'rank': 'A', 'value': 11},
            {'rank': '2', 'value': 2},
            {'rank': '3', 'value': 3},
            {'rank': '4', 'value': 4},
            {'rank': '5', 'value': 5},
            {'rank': '6', 'value': 6},
            {'rank': '7', 'value': 7},
            {'rank': '8', 'value': 8},
            {'rank': '9', 'value': 9},
            {'rank': '10', 'value': 10},
            {'rank': 'J', 'value': 10},
            {'rank': 'Q', 'value': 10},
            {'rank': 'K', 'value': 10},
        ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if (len(self.cards) > 1):
            random.shuffle(self.cards)

    def deal(self, number):
        cardsDealt = []
        for i in range(number):
            if (len(self.cards) > 1):
                cardsDealt.append(self.cards.pop())
        return cardsDealt

class Hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def addCard(self, cardList):
        self.cards.extend(cardList)
    
    def calculateValue(self):
        self.value = 0
        hasAce = False

        for card in self.cards:
            cardValue = int(card.rank['value'])
            self.value += cardValue
            
            if card.rank['rank'] == 'A':
                hasAce = True
        
        if hasAce and self.value > 21:
            self.value -= 10

    def getValue(self):
        self.calculateValue()
        return self.value

    def isBlackjack(self):
        return self.getValue() == 21
    
    def display(self, showAllDealerCards = False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
                and not showAllDealerCards and not self.isBlackjack():
                print('Hidden')
            else:
                print(card)

        if not self.dealer:
            print('Value: {}'.format(self.getValue()))
