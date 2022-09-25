from .deck import Deck
from .hand import Hand

class Game:
    def play(self):
        gameNumber = 0
        gamesToPlay = 0

        while gamesToPlay <= 0:
            try:
                gamesToPlay = int(
                    input('How many games do you want to play? \n'))
            except:
                print('You must enter a number.')

        while gameNumber < gamesToPlay:
            gameNumber += 1

            deck = Deck()
            deck.shuffle()

            playerHand = Hand()
            dealerHand = Hand(dealer=True)

            for i in range(2):
                playerHand.addCard(deck.deal(1))
                dealerHand.addCard(deck.deal(1))

            print()
            print('*' * 30)
            print('Game {} of {}'.format(gameNumber, gamesToPlay))
            print('*' * 30)
            playerHand.display()
            dealerHand.display()

            if self.checkWinner(playerHand, dealerHand):
                continue

            choice = ''
            while playerHand.getValue() < 21 and choice not in ['s', 'stand']:
                choice = input('Please choose \'hit\' or \'stand\': ').lower()
                print()
                while choice not in ['h', 's', 'hit', 'stand']:
                    choice = input(
                        'Please choose \'hit\' or \'stand\' (or H/S): ').lower()
                    print()
                if choice in ['hit', 'h']:
                    playerHand.addCard(deck.deal(1))
                    playerHand.display()

            if self.checkWinner(playerHand, dealerHand):
                continue

            playerHandValue = playerHand.getValue()
            dealerHandValue = dealerHand.getValue()

            while dealerHandValue < 17:
                dealerHand.addCard(deck.deal(1))
                dealerHandValue = dealerHand.getValue()

            dealerHand.display(showAllDealerCards=True)

            if self.checkWinner(playerHand, dealerHand):
                continue

            print('Final result')
            print('Your hand: {}'.format(playerHandValue))
            print('Dealer\'s hand: {}'.format(dealerHandValue))

            self.checkWinner(playerHand, dealerHand, True)

        print('\nThanks for playing:')

    def checkWinner(self, playerHand, dealerHand, gameOver=False):
        if not gameOver:
            if playerHand.getValue() > 21:
                print('Dealer wins!')
                return True
            elif dealerHand.getValue() > 21:
                print('You win!')
                return True
            elif playerHand.isBlackjack() and dealerHand.isBlackjack():
                print('It\'s a Tie!')
                return True
            elif playerHand.isBlackjack():
                print('You win!')
                return True
            elif dealerHand.isBlackjack():
                print('Dealer wins!')
                return True
        else:
            if playerHand.getValue() > dealerHand.getValue():
                print('You win!')
            elif playerHand.getValue() == dealerHand.getValue():
                print('It\'s a tie!')
            else:
                print('Dealer wins!')
            return True
        return False
