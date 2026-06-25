#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, num_days: int) -> None:
        self.name = name
        self._height = height
        self._num_days = num_days

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

        def show(self) -> None:
            _height = round(self._height, 1)
            print(f"Current state: {self.name}: {_height:.1f}cm,"
                f" {self._num_days} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float,
                num_days: int, color: str) -> None:
        super().__init__(name, height, num_days)
        self.color = color

        def bloom(self) -> None:
            pass


class Tree(Plant):
    def __init__(self, name: str, height: float,
                num_days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, num_days)
        self.trunk_diameter = trunk_diameter

        def produce_shade(self) -> None:
            pass


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                num_days: int, harvest_season: int, nutritional_value: float) -> None:
        super().__init__(name, height, num_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
