import random


PLAYERS = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory", "john", "kevin", "Liam"]


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")

    print(f"Initial list of players: {PLAYERS}")

    players_cap = [name.capitalize() for name in PLAYERS]
    print(f"New list with all names capitalized: {players_cap}")

    players_already_cap = [name for name in PLAYERS if name == name.capitalize()]
    print(f"New list of capitalized names only: {players_already_cap}\n")
