from card_base.deck import Deck
from card_base.card import Card


def higher_lower():
    game = HighLowGame()
    game.start_game()
    pass


class HighLowGame:
    def start_game(self):
        print("Welcome to higher lower, lets play")
