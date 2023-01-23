from typing import List
from card_base.card import CardValue, Card


class Player:
    name: str
    hand: List[Card]
    score: List[CardValue]

    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.score = []

    def add_card_to_hand(self, card: Card):
        self.hand.append(card)
        self.hand = sorted(self.hand, key=lambda x: x.value.value)
        self.check_for_fours()

    def remove_card_from_hand(self, card: Card):
        self.hand.remove(card)

    def check_for_fours(self):
        hand = self.hand
        for value in CardValue:
            matched = [card for card in self.hand if card.value == value]
            if len(matched) == 4:
                print("New four of a kind")
                self.score.append(matched[0].value)
                for match in matched:
                    hand.remove(match)

    def get_hand_count(self):
        return len(self.hand)

    def print_hand(self):
        string: str = ""
        for card in self.hand:
            string += f" |{card}| "
        print(string)
