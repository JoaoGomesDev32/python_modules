import random


ACHIEVEMENTS = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
    "Boss Slayer", "Hidden Path Finder"
]


def gen_player_achievements() -> set[str]:
    count = random.randint(3, 8)
    return set(random.sample(ACHIEVEMENTS, count))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    all_achievements = set.union(*players.values())
    print(f"\nAll distinct achievements: {all_achievements}")

    common_achievements = set.intersection(*players.values())
    print(f"\nCommon achievements: {common_achievements}\n")

    for name, achievements in players.items():
        others = set.union(*[ach for n, ach in players.items() if n != name])
        only_has = achievements.difference(others)
        print(f"Only {name} has: {only_has}")

    print()
    for name, achievements in players.items():
        missing = all_achievements.difference(achievements)
        print(f"{name} is missing: {missing}")
