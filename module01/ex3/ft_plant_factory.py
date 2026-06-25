#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, num_days: int) -> None:
        self.name = name
        self.height = height
        self.num_days = num_days

    def show(self) -> None:
        height = round(self.height, 1)
        print(f"Created: {self.name}: {height}cm, {self.num_days} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)
    print("=== Plant Factory Output ===")
    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()
