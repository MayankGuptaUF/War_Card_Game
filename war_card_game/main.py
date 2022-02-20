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


class Player:
    """
    The Player class is instantiated as soon a player is added
    This class has attributes name and cards
    """

    def __init__(self, name, cards=[]):
        self.name = name
        self.cards = cards


class InitializePlayers:
    """
    This class is used to generate a list of players by taking
    inputs from the user.
    """

    players = []

    def __init__(self):
        number_of_players = 2
        # According to wikipedia the number of players in the game
        # are just 2, but this class InitializePlayers has been designed
        # in a way where it can support upto 14 players as seen in
        # some iterations of the game.
        if number_of_players < 2 or number_of_players > 14:
            raise CustomError("    You can only have players between 2 and 14")
        for i in range(number_of_players):
            self.players.append(
                Player(
                    input("Player {} name: ".format(i + 1)) or "Player {}".format(i + 1)
                )
            )
        print("\n           Current Players\n")
        for i in range(number_of_players):
            print("         " + self.players[i].name, end=" ")
        print("\n")

    def get_list_of_players(self) -> str:
        """
        Returns the list of current players

        Returns
        -------
            players:str
        """

        return self.players


class Deal:
    """
    This class takes a deck, shuffles it and deals it among the players
    """

    def __init__(self, deck, players):
        deck.shuffle()
        cards_per_person = len(deck.card_deck) // len(players)
        for i in range(len(players)):
            players[i].cards = deck.card_deck[
                i * cards_per_person : (i + 1) * cards_per_person
            ]

        return self.players


def main():
    deck = CardDeck()
    register_players = InitializePlayers()
    players = register_players.get_list_of_players()
    Deal(deck, players)

main()