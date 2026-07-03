def input_temperature(temp_str: str) -> int:
    print(f"Input data is {temp_str}")
    temp = int(temp_str)
    print(f"Temperature is now {temp}°C")
    print()
    return temp


def test_temperature() -> None:
    try:
        input_temperature("25")
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
