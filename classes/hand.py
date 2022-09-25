class Hand:
    def __init__(self, dealer=False):
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

    def display(self, showAllDealerCards=False):
        print(f'''{"Dealer's" if self.dealer else 'Your'} hand:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
                    and not showAllDealerCards and not self.isBlackjack():
                print('Hidden')
            else:
                print(card)

        if not self.dealer:
            print('Value: {}'.format(self.getValue()))
        print()
