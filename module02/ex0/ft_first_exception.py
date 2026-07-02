def input_temperature(temp_str: str) -> int:
    print(f"Input data is {temp_str}")
    print(f"Temperature is now {temp_str}°C")
    print()
    return int(temp_str)

def test_temperature() -> None:
    try:
        input_temperature("25")
        input_temperature("abc")
    except:
        print("Caught input_temperature error: invalid literal for int() with base 10: 'abc'")

if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
