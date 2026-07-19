import random


PLAYERS = ["Alice", "bob", "Charlie", "dylan", "Emma",
           "Gregory", "john", "kevin", "Liam"]


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")

    print(f"Initial list of players: {PLAYERS}")

    players_cap = [name.capitalize() for name in PLAYERS]
    print(f"New list with all names capitalized: {players_cap}")

    players_already_cap = [name for name in PLAYERS
                           if name == name.capitalize()]
    print(f"New list of capitalized names only: {players_already_cap}\n")

    score_dict = {p: random.randint(1, 1000) for p in players_cap}
    print(f"Score dict: {score_dict}")

    score_average = round(sum(score_dict.values()) /
                          len(score_dict.values()), 2)
    print(f"Score average is {score_average}")

    high_scores = {p: s for p, s in score_dict.items() if s > score_average}
    print(f"High scores: {high_scores}")
