class Card:
    """
    The class Card stores two attributes of
    a card. The rank which can be from A,2......J,Q,K
    and the suit which can be of 4 types
    """

    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit