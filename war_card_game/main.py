import random
from collections import defaultdict


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


class Play:

    final_winner = None
    ongoing_war = False
    battle_cards = {}
    war_chest = defaultdict(list)

    value = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 10,
        "10": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
    }

    def __init__(self, players: str):
        self.players = players

    def draw_cards(self):
        """
        Check if player has enough cards, if yes allow them to draw a card
        for battle, else end the game.

        Returns
        -------
            None
        """
        for i, player in enumerate(self.players):
            if len(player.cards) == 0:
                print("    ********************************")
                print("\n              {} has lost".format(player.name))

                self.players.pop(i)

                if len(self.players) == 1:
                    print("              {} has won    \n".format(self.players[0].name))
                    print("    ********************************")
                    self.final_winner = self.players[0].name
                    return 0
            else:
                self.battle_cards[player] = player.cards.pop()


    def battle(self):
        """
        Conduct a battle between the players,if tie go to war

        Returns
        -------
            None
        """
        if self.final_winner:
            return
        current_winners = set()
        max_card = 0
        for player, card in self.battle_cards.items():
            if self.value[card.rank] >= max_card:
                max_card = self.value[card.rank]
        for player, card in self.battle_cards.items():
            print("    {} drew {} of {}    ".format(player.name, card.rank, card.suit))
            if self.value[card.rank] >= max_card:
                current_winners.add(player)
        print("\n")

        if len(current_winners) == 1:
            winner = current_winners.pop()
            print("\n\n    The winner of this battle is {}    \n\n".format(winner.name))
            for key, values in self.battle_cards.items():
                winner.cards.insert(0, values)

            for player in self.players:
                print(
                    "    {} has {} cards remaining    ".format(
                        player.name, len(player.cards)
                    )
                )
            print("\n")
        else:
            self.ongoing_war = True
            while self.ongoing_war:
                self.prepare_for_war()
        self.battle_cards = {}

    def prepare_for_war(self):
        """
        Check if players have enough cards to participate in war.

        Returns
        -------
            None
        """
        for i, player in enumerate(self.players):
            if len(player.cards) < 4:
                self.ongoing_war = False
                self.players.pop(i)
                self.final_winner = self.players[0]
                print("    ********************************")
                print(
                    "    {} does not have enough cards to enter a WAR, {} is the winner".format(
                        player.name, self.final_winner.name
                    )
                )
                print("    ********************************")
                return
        print("    We are headed to a WAR")
        self.war()

    def war(self):
        """
        Create the decks for the war battle, call war_battle.

        Returns
        -------
            None
        """

        for player in self.players:
            for _ in range(4):
                self.war_chest[player].append(player.cards.pop())
        self.war_battle(3)

    def war_battle(self, turns_left: int) -> None:
        """
        Conduct the war until no more cards are left

        Parameters
        ----------
        turns_left:str
            An integer tracking the turns left in this war.
        Returns
        -------
            None
        """
        if turns_left < 1:
            return
        current_winners = set()
        max_card = 0
        for player, cards in self.war_chest.items():
            if self.value[cards[turns_left].rank] >= max_card:
                max_card = self.value[cards[turns_left].rank]
        for player, cards in self.war_chest.items():
            print(
                "    {} drew {} of {}".format(player.name, cards[turns_left].rank, cards[turns_left].suit)
            )
            if self.value[cards[turns_left].rank] >= max_card:
                current_winners.add(player)
        print("\n")
        if len(current_winners) == 1:
            self.ongoing_war = False
            winner = current_winners.pop()
            print("\n\n    The winner of this WAR is {}    \n\n".format(winner.name))
            for key, values in self.battle_cards.items():
                winner.cards.insert(0, values)
            self.battle_cards = {}
            for key, cards in self.war_chest.items():
                for card in cards:
                    winner.cards.insert(0, card)

            self.war_chest = defaultdict(list)

            for player in self.players:
                print(
                    "    {} has {} cards remaining    ".format(
                        player.name, len(player.cards)
                    )
                )
            print("\n")
            return
        else:
            self.war_battle(turns_left - 1)



def main():
    deck = CardDeck()
    register_players = InitializePlayers()
    players = register_players.get_list_of_players()
    Deal(deck, players)
    play_game = Play(players)
    game_type = input("Automatic Game or turnwise? A/T ")
    if(game_type!="" and game_type[0].lower() == "t"):
        play_game_turnwise(play_game)

def play_game_turnwise(play_game: Play):
    """
    This allows users to play the game turnwise
    Parameters
    ----------
    play_game:Play
        play_game is an object within which we conduct the battles and wars

    Returns
    -------
        None
    """
    round_number = 0
    while not play_game.final_winner:
        round_number += 1
        begin = input("Round {},begin? Y/N ".format(round_number))
        if begin.lower() == "" or begin.lower()[0] == "y":
            value = play_game.draw_cards()
            play_game.battle()
        else:
            print("\n\nGame interrupted,ending game \n\n")
            break

main()