#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, "
                  f"{self._show_count} show")

    def __init__(self, name: str, height: float, num_days: int,
                 grow_rate: float = 8.0) -> None:
        self.name = name
        self._height = height
        self._num_days = num_days
        self.grow_rate = grow_rate
        self._stats = Plant.Stats()

    def grow(self) -> None:
        self._height += self.grow_rate
        self._stats._grow_count += 1

    def age(self) -> None:
        self._num_days += 1
        self._stats._age_count += 1

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def get_num_days(self) -> int:
        return self._num_days

    def set_num_days(self, num_days: int) -> None:
        if num_days < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            print()
        else:
            self._num_days = num_days
            print(f"Age updated: {self._num_days} days")
            print()

    def create(self) -> None:
        _height = round(self._height, 1)
        print(f"Plant created: {self.name}: {_height}cm,"
              f" {self._num_days} days old")
        print()

    @staticmethod
    def is_older_than_year(num_days: int) -> bool:
        return num_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        _height = round(self._height, 1)
        print(f"{self.name}: {_height:.1f}cm,"
              f" {self._num_days} days old")
        self._stats._show_count += 1


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 num_days: int, color: str) -> None:
        super().__init__(name, height, num_days)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 num_days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, num_days)
        self.trunk_diameter = trunk_diameter
        self._shade_count: int = 0

    def produce_shade(self) -> None:
        self._shade_count += 1
        height = round(self._height, 1)
        print(f"Tree {self.name} now produces a shade of "
              f"{height}cm long and {self.trunk_diameter}cm wide.")

    def show_shade(self) -> None:
        print(f" {self._shade_count} shade")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, num_days: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, num_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age(self) -> None:
        super().age()

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float, num_days: int,
                 color: str) -> None:
        super().__init__(name, height, num_days, color)
        self.seeds: int = 0

    def bloom(self, seeds: int = 0) -> None:
        super().bloom()
        self.seeds = seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_stats(plant: Plant) -> None:
    plant._stats.display()
    if isinstance(plant, Tree):
        plant.show_shade()


if __name__ == "__main__":
    rose = Flower("Rose", 15, 10, "red")
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()
    print("=== Flower")
    rose.show()
    print(f"[statistics for {rose.name}]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print(f"[statistics for {rose.name}]")
    display_stats(rose)
    print()
    oak = Tree("Oak", 200.0, 365, 5.0)
    print("=== Tree")
    oak.show()
    print(f"[statistics for {oak.name}]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print(f"[statistics for {oak.name}]")
    display_stats(oak)
    print()
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    print("=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow_rate = 30
    sunflower.grow()
    sunflower.age()
    sunflower.bloom(42)
    sunflower.show()
    print(f"[statistics for {sunflower.name}]")
    display_stats(sunflower)
    print()
    anon = Plant.create_anonymous()
    print("=== Anonymous")
    anon.show()
    print(f"[statistics for {anon.name}]")
    display_stats(anon)
