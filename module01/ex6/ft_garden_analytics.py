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
                 grow_rate: float = 2.1) -> None:
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


if __name__ == "__main__":
    print(Plant.is_older_than_year(30))
    print(Plant.is_older_than_year(400))
    anon = Plant.create_anonymous()
    anon.show()
    lis = Plant("Lis", 12.5, 50)
    for i in range(10):
        lis.grow()
    for i in range(12):
        lis.age()
    for i in range(5):
        lis.show()
    lis._stats.display()