from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)
from ex2.errors import InvalidStrategyError

Opponent = tuple[CreatureFactory, BattleStrategy]


def battle_pair(opponent_a: Opponent, opponent_b: Opponent) -> None:
    factory_a, strategy_a = opponent_a
    factory_b, strategy_b = opponent_b

    creature_a = factory_a.create_base()
    creature_b = factory_b.create_base()

    print("* Battle *")
    print(creature_a.describe())
    print(" vs ")
    print(creature_b.describe())
    print(" now fight!")

    print(strategy_a.act(creature_a))
    print(strategy_b.act(creature_b))


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                battle_pair(opponents[i], opponents[j])
                print()
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    battle([(flame, normal), (healing, defensive)])
    print()

    print("Tournament 1 (error)")
    battle([(flame, aggressive), (healing, defensive)])
    print()

    print("Tournament 2 (multiple)")
    battle([(aqua, normal), (healing, defensive), (transform, aggressive)])


if __name__ == "__main__":
    main()
