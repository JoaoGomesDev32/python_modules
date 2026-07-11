#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, num_days: int,
                 grow_rate: float = 2.1) -> None:
        self.name = name
        self._height = height if height >= 0 else 0.0
        self._num_days = num_days if num_days >= 0 else 0
        self.grow_rate = grow_rate

    def grow(self) -> None:
        self._height += self.grow_rate

    def age(self) -> None:
        self._num_days += 1

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height if height >= 0 else 0.0
            print(f"Height updated: {self._height}cm")

    def get_age(self) -> int:
        return self._num_days

    def set_age(self, num_days: int) -> None:
        if num_days < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            print()
        else:
            self._num_days = num_days if num_days >= 0 else 0
            print(f"Age updated: {self._num_days} days")
            print()

    def create(self) -> None:
        _height = round(self._height, 1)
        print(f"Plant created: {self.name}: {_height}cm,"
              f" {self._num_days} days old")
        print()

    def show(self) -> None:
        _height = round(self._height, 1)
        print(f"{self.name}: {_height:.1f}cm,"
              f" {self._num_days} days old")


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

    def produce_shade(self) -> None:
        height = round(self._height, 1)
        print(f"Tree {self.name} now produces a shade of "
              f"{height}cm long and {self.trunk_diameter}cm wide.")

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


if __name__ == "__main__":
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
