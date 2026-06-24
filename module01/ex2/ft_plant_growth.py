#!/usr/bin/env python3

class Plant:
    def show(self) -> None:
        height = round(self.height, 1)
        print(f"{self.name}: {height}cm, {self.num_days} days old")

    def grow(self) -> None:
        self.height += self.grow_rate

    def age(self) -> None:
        self.num_days += 1


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.num_days = 30
    rose.grow_rate = 0.8
    print("=== Garden Plant Growth ===")
    rose.show()
    initial_height = rose.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.age()
        rose.grow()
        rose.show()
    print(f"Growth this week: {round(rose.height - initial_height, 1)}cm")
