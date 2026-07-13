import math

def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(parts[0])
            y = float(parts[1])
            z = float(parts[2])
            return (x, y, z)
        except ValueError as e:
            print(f"Error on parameter '{parts[...]}': {e}")


if __name__ == "__main__":
    print(f"=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    get_player_pos()
    print("Get a second set of coordinates")
    get_player_pos()
