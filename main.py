import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:
    def __init__(self):
        cardsInDeck = []
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        values = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5',
                  '4', '3', '2']
        for suit in suits:
            for value in values:
                cardsInDeck.append(Card(suit, value))

        self.cards = cardsInDeck

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)


class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == 'A':
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def display(self, player_turn=True):
        if self.dealer and player_turn is True:
            print('Dealer\'s Hand is:\nHidden')
            print(self.cards[1])
        elif self.dealer and player_turn is False:
            print('Dealer\'s Hand is:')
            for card in self.cards:
                print(card)
            print(f'Value: {self.get_value()}')
        else:
            print('Your hand is:')
            for card in self.cards:
                print(card)
            print(f'Value: {self.get_value()}')


class Game:
    def __init__(self):
        pass

    def play(self, player_score, dealer_score):
        divider = '*' * 20
        playing = True

        while playing:
            self.player_score = player_score
            self.dealer_score = dealer_score
            self.deck = Deck()
            self.deck.shuffle()
            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)
            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            self.player_hand.display()
            # print(divider)
            self.dealer_hand.display()
            if self.dealer_hand.get_value() == 21:
                print('Game over dealer has 21.')
                self.dealer_score += 1
                menu(self.player_score, self.dealer_score)
            else:
                while self.player_hand.get_value() < 21:
                    hit_me = input('Do you want another card? ')
                    if 'y' in hit_me.lower():
                        self.player_hand.add_card(self.deck.deal())
                        self.player_hand.display()
                        if self.player_hand.get_value() > 21:
                            print('Player busted, dealer wins')
                            self.dealer_score += 1
                            menu(self.player_score, self.dealer_score)
                    else:
                        while self.dealer_hand.get_value() < 21:
                            if self.dealer_hand.get_value() >= self.player_hand.get_value():
                                self.dealer_hand.display(player_turn=False)
                                print('Dealer has better score than player, dealer wins')
                                self.dealer_score += 1
                                menu(self.player_score, self.dealer_score)
                            else:
                                self.dealer_hand.add_card(self.deck.deal())
                                self.dealer_hand.display(player_turn=False)
                                if self.dealer_hand.get_value() > 21:
                                    print('Dealer busted, player wins')
                                    self.player_score += 1
                                    menu(self.player_score, self.dealer_score)
                                elif self.dealer_hand.get_value() >= self.player_hand.get_value():
                                    print('Dealer has better score than player, dealer wins')
                                    self.dealer_score += 1
                                    menu(self.player_score, self.dealer_score)
                                else:
                                    continue


def menu(player_score, dealer_score):
    print('Scoreboard')
    print(f'{player_name.title()}: {player_score}')
    print(f'Dealer: {dealer_score}')
    print('*' * 25)
    play = input('Do you want to play? ')
    if 'y' in play.lower():
        game = Game()
        game.play(player_score, dealer_score)


if __name__ == "__main__":
    print('Welcome to Blackjack. Good Luck!')
    player_name = input('Player Name: ')
    player_score = 0
    dealer_score = 0
    menu(player_score, dealer_score)
