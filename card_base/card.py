# card

from dataclasses import dataclass
from enum import Enum


class CardValue(Enum):
    ACE = "Ace"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"


class CardValueInt(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class CardSuit(Enum):
    HEARTS = "♡"
    DIAMONDS = "♢"
    SPADES = "♠"
    CLUBS = "♣"


class Card:
    suit: CardSuit
    value: CardValue
    int_value: CardValueInt

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.int_value = CardValueInt[self.value.name]

    def __str__(self):
        return f"{self.suit.value} {self.value.value}"


if __name__ == "__main__":
    card = Card(CardValue.KING, CardSuit.HEARTS)
    print(card.__dict__)
