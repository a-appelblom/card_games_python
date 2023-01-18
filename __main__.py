
from pyramid.game import pyramid
from go_fish.game import go_fish
from higher_lower.game import higher_lower
from memory.game import memory
from typing import List


menu_options: List[str] = [
    "Exit", "Higher Lower", "Go Fish", "Pyramid", "Memory"]


class NonValidOptionError(Exception):
    pass


def menu():
    print_options()
    choice = get_option()
    run_option(choice)
    pass


def print_options():
    for i, option in enumerate(menu_options):
        print(f"{i}: {option} ")
    pass


def get_option():
    try:
        choice_string = input("Enter option: ")
        choice = int(choice_string)
        if not 0 <= choice < len(menu_options):
            raise NonValidOptionError("No such option")
    except ValueError:
        print("Please enter option that is a number")
    except NonValidOptionError:
        print("No such option")
    else:
        return choice


def run_option(option: int):
    if option == 0:
        exit()
    elif option == 1:
        higher_lower()
    elif option == 2:
        go_fish()
    elif option == 3:
        memory()
    elif option == 4:
        pyramid()


if __name__ == "__main__":
    menu()
