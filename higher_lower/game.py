from card_base.deck import Deck
from card_base.card import Card, CardValue


def higher_lower():
    game = HighLowGame()
    game.start_game()
    pass


class HighLowGame:
    deck: Deck() = Deck()
    active_card: Card
    new_card: Card
    score: int = 0
    game_over = False

    def __init__(self):
        self.deck.reset_deck()
        self.deck.shuffle()
        self.active_card = self.deck.pull_card()

    def start_game(self):
        print("Welcome to higher lower, lets play")
        while not self.game_over:
            self.run_round()

    def run_round(self):
        print(f"Current card: {self.active_card}")

        self.new_card = self.deck.pull_card()
        guess = self.make_guess()
        win = self.check_win(guess)
        if win:
            self.win_round()
        else:
            self.lose_round()

    def make_guess(self) -> str:  # h or l
        while True:
            guess = input("Will the card be higher or lower (h/l): ")
            guess = guess.strip().lower()
            if guess == "h" or guess == "l":
                return guess
            else:
                print("Choose either h or l")
                continue

    def check_win(self, guess: str) -> bool:
        if self.active_card.value == CardValue.ACE or self.new_card == CardValue.ACE:
            return True
        elif self.new_card.int_value.value >= self.active_card.int_value.value and guess == "h":
            return True
        elif self.new_card.int_value.value <= self.active_card.int_value.value and guess == "l":
            return True
        else:
            return False

    def win_round(self):
        self.score += 1
        self.active_card = self.new_card
        print(f"Correct, current score: {self.score}")

    def lose_round(self):
        self.game_over = True
        print(
            f"Sorry the card was {self.new_card}, you lost the game at a score of {self.score}")
