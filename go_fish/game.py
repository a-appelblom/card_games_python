import os
from card_base.card import Card, CardValue, CardSuit
from card_base.deck import Deck
from go_fish.player import Player
from typing import List


def verify_player_count(string: str) -> int:
    if str.isdigit(string) and 1 < int(string) < 5:
        return True
    else:
        return False


def go_fish():
    game = Game()
    player_count: int
    verified = False
    while not verified:
        player_count_inp = input("How many players 2-4: ")
        verified = verify_player_count(player_count_inp)

    player_count = int(player_count_inp)

    for i in range(player_count):
        name = input(f"Player{i + 1}'s name: ")
        game.add_player(Player(name))

    print("Welcome: ")
    game.print_players()
    print("Lets have some fun")

    game.start_game()


class Game:
    deck: Deck
    players: List[Player]
    active_player: int = 0

    def __init__(self):
        self.deck = Deck()
        self.players = []

    def add_player(self, player: Player):
        self.players.append(player)

    def initial_deal(self):
        for player in self.players:
            for i in range(4):
                player.add_card_to_hand(self.deck.pull_card())

    def start_game(self):
        os.system('cls||clear')
        self.deck.shuffle()
        print("Lets play")
        self.initial_deal()
        while self.deck.get_card_count() > 0 or self.players[self.active_player].get_hand_count() > 0:
            self.run_round()

    def run_round(self):
        carry_on = True
        player = self.players[self.active_player]
        print(player.name + "'s Turn")
        while carry_on:
            player.print_hand()
            carry_on = self.ask_for_cards()
        player.print_hand()
        self.check_empty()

        input("Tryck enter när du är klar")
        os.system('cls||clear')
        input("Byt spelare och tryck sen enter")
        os.system('cls||clear')
        self.active_player += 1
        if self.active_player == len(self.players):
            self.active_player = 0

    def check_empty(self):
        for player in self.players:
            if player.get_hand_count() == 0:
                print("Empty hand")
                player.add_card_to_hand(self.deck.pull_card())

    def ask_for_cards(self) -> bool:
        current_player = self.players[self.active_player]
        if len(self.players) == 2:
            asked_player = self.players[self.active_player - 1]
        else:
            asked_player = self.get_opponent()

        asked_value = self.get_asked_value()

        counter = 0
        for card in asked_player.hand:
            if card.value == asked_value:
                current_player.add_card_to_hand(card)
                asked_player.remove_card_from_hand(card)
                counter += 1
        if counter == 0:
            print("Go fish")
            current_player.add_card_to_hand(self.deck.pull_card())
            return False
        else:
            print(f"Moved {counter} card")
            print("Carry on")
            return True

    def get_opponent(self) -> Player:
        while True:
            self.print_players()
            chosen_player = input("Who do you want to ask for cards from?: ")

            for player in self.players:
                if player.name == chosen_player:
                    return player

            print("No such player, try again, the players are: ")
            self.print_players()

    def get_asked_value(self) -> CardValue:
        while True:
            chosen_value = input("What do you want to ask for ?: ")
            for card in self.players[self.active_player].hand:
                if card.value.value.upper() == chosen_value.upper():
                    return card.value

            print("No such value or no such card in hand")

    def print_players(self):
        for player in self.players:
            print(player.name)

    def print_results(self):
        for player in self.players:
            print(f"{player.name}: {len(player.score)}")
        pass
