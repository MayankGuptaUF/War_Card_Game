import random


class Card:
    """
    The class Card stores two attributes of
    a card. The rank which can be from A,2......J,Q,K
    and the suit which can be of 4 types
    """

    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

class CardDeck:
    """
    The Class CardDeck is used to generate the card_decks which
    will be used by the Deal class to distribute cards amongst the
    players
    """

    card_deck = []

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Spades", "Club"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        # I would have liked to use set in the place of a list. The
        # problem with set is that the value popped though arbitrary, is not
        # random. Since war is a game of chance, randomness is an important
        # element of the game. Instead we will use another method shuffle.
        # This will be using the Python built in library called random.
        for suit in suits:
            for rank in ranks:
                self.card_deck.append(Card(suit, rank))

    def shuffle(self):
        # Refer to __init__
        random.shuffle(self.card_deck)