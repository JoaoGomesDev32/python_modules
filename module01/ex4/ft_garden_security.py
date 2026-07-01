#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, num_days: int) -> None:
        self.name = name
        self._height = height if height >= 0 else 0.0
        self._num_days = num_days if num_days >= 0 else 0
        _h = round(self._height, 1)
        print(f"Plant created: {self.name}: {_h:.1f}cm,"
              f" {self._num_days} days old")

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def get_age(self) -> int:
        return self._num_days

    def set_age(self, num_days: int) -> None:
        if num_days < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            print()
        else:
            self._num_days = num_days
            print(f"Age updated: {self._num_days} days")
            print()

    def show(self) -> None:
        _height = round(self._height, 1)
        print(f"Current state: {self.name}: {_height:.1f}cm,"
              f" {self._num_days} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.set_age(-1)
    rose.show()
