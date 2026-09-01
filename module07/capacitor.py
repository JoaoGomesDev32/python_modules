from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_capability(healing: HealingCreatureFactory):
    print("Testing Creature with healing capability")
    print(" base:")
    base = healing.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    evolved = healing.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform_capability(transform: TransformCreatureFactory):
    print("Testing Creature with transform capability")
    print(" base:")
    base = transform.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    evolved = transform.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing_capability(healing_factory)
    test_transform_capability(transform_factory)


if __name__ == "__main__":
    main()
