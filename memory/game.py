from card_base.deck import Deck
from card_base.card import Card


def memory():
    game = MemoryGame()
    game.start_game()
    pass


class MemoryGame:
    def start_game(self):
        print("Welcome to higher lower, lets play")
