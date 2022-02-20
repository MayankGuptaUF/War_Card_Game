from collections import defaultdict
from config  import CARD_VALUE
from config import WAR_MIN_CARDS

class Play:

    final_winner = None
    ongoing_war = False
    battle_cards = {}
    war_chest = defaultdict(list)


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
            if CARD_VALUE[card.rank] >= max_card:
                max_card = CARD_VALUE[card.rank]
        for player, card in self.battle_cards.items():
            print("    {} drew {} of {}    ".format(player.name, card.rank, card.suit))
            if CARD_VALUE[card.rank] >= max_card:
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
        Also, Create the decks for the war battle, call war_battle.

        Returns
        -------
            None
        """
        for i, player in enumerate(self.players):
            if(len(player.cards) < WAR_MIN_CARDS):
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

        for player in self.players:
            for _ in range(WAR_MIN_CARDS):
                self.war_chest[player].append(player.cards.pop())
        self.war_battle(WAR_MIN_CARDS-1)

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
            if CARD_VALUE[cards[turns_left].rank] >= max_card:
                max_card = CARD_VALUE[cards[turns_left].rank]
        for player, cards in self.war_chest.items():
            print(
                "    {} drew {} of {}".format(player.name, cards[turns_left].rank, cards[turns_left].suit)
            )
            if CARD_VALUE[cards[turns_left].rank] >= max_card:
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