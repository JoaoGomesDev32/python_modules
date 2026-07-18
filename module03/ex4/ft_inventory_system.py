import sys


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, qty = parts
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            inventory[name] = int(qty)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")

    if not inventory:
        print("No inventory. Usage: python3 ft_inventory_system.py "
              "<item>:<qty> ...")
    else:
        total = sum(inventory.values())
        print(f"Got inventory: {inventory}")
        print(f"Item list: {list(inventory.keys())}")
        print(f"Total quantity of the {len(inventory)} items: {total}")
        for name, quantity in inventory.items():
            print(f"Item {name} represents "
                  f"{round(quantity / total * 100, 1)}%")
        most = max(inventory, key=lambda k: inventory[k])
        least = min(inventory, key=lambda k: inventory[k])
        print(f"Item most abundant: {most} with quantity {inventory[most]}")
        print(f"Item least abundant: {least} with quantity {inventory[least]}")
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")
