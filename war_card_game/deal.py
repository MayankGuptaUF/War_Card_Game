class Deal:
    """
    This class takes a deck, shuffles it and deals it among the players
    """

    def __init__(self, deck, players):
        deck.shuffle()
        cards_per_person = len(deck.card_deck) // len(players)
        # This divides the deck in equal parts for each player.
        for i in range(len(players)):
            players[i].cards = deck.card_deck[
                i * cards_per_person : (i + 1) * cards_per_person
            ]