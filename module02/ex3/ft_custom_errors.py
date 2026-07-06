class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test_plant_error() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!\n")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error() -> None:
    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!\n")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_garden_errors() -> None:
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise WaterError("Not enough water in the tank!\n")
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_plant_error()
    test_water_error()
    test_garden_errors()
    print("\nAll custom error types work correctly")
