# Module __main__.py

from collections import defaultdict
from card import Card
from card_deck import CardDeck
from player import Player
from initialize_players import InitializePlayers
from deal import Deal
from play import Play


def main():
    deck = CardDeck()
    register_players = InitializePlayers()
    players = register_players.get_list_of_players()
    Deal(deck, players)
    play_game = Play(players)
    game_type = input("Automatic Game or turnwise? A/T ")
    if(game_type!="" and game_type[0].lower() == "t"):
        play_game_turnwise(play_game)
    else:
        play_automatically(play_game)


def play_automatically(play_game: Play) -> None:
    """
    This runs a simulation of the game to decide a winner

    Parameters
    ----------
    play_game:Play
        play_game is an object within which we conduct the battles and wars

    Returns
    -------
        None
    """
    game_limit = 0
    while not play_game.final_winner:
        game_limit += 1
        if game_limit < 10000:
            value = play_game.draw_cards()
            play_game.battle()
        else:
            print("\n\nMaximum number of turns reached, Game has ended \n\n")
            break

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