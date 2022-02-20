class Player:
    """
    The Player class is instantiated as soon a player is added
    This class has attributes name and cards
    """

    def __init__(self, name, cards=[]):
        self.name = name
        self.cards = cards