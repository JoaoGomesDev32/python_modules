#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    print(f"Input data is {temp_str}")
    temp = int(temp_str)
    print(f"Temperature is now {temp}°C")
    print()
    return temp


def test_temperature() -> None:
    # Teste 1: Entrada válida
    try:
        input_temperature("25")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    # Teste 2: Entrada inválida (separada para garantir que o fluxo continue)
    try:
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
