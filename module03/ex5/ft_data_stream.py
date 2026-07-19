import random
from typing import Generator

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "jump", "swim", "climb", "grab", 
           "use", "move", "eat", "sleep", "release"]

def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        event = next(gen_event)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")