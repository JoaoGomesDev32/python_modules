#!/usr/bin/env python3

# Reaproveitando a estrutura do Ex 3
class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        # Lançando erro customizado se o nome não estiver capitalizado
        raise PlantError(f"Invalid plant name to water: {plant_name}")


def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        # O bloco finally é exec OBRIGATORIAMENTE, ocorrendo um erro ou não.
        print("Closing watering system\n")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print("Testing invalid plants...")
    # "tomato" (minúsculo) vai triggar o erro na primeira iteração
    test_watering_system(["tomato", "lettuce", "carrots"])
    print("Cleanup always happens, even with errors!")
