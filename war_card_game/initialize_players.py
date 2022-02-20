from player import Player

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