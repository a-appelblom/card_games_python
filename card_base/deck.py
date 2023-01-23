from random import shuffle
from typing import List
from card import Card, CardSuit, CardValue


class Deck:
    cards: List[Card] = []

    def __init__(self):
        for suit in CardSuit:
            for value in CardValue:
                self.cards.append(Card(value, suit))

    def pull_card(self):
        return self.cards.pop()

    def shuffle(self):
        shuffle(self.cards)

    def reset_deck(self):
        self.__init__()
