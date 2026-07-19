import random
from typing import Generator

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "jump", "swim", "climb", "grab",
           "use", "move", "eat", "sleep", "release"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
        events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while events:
        event = random.choice(events)
        events.remove(event)
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    generator = gen_event()
    for i in range(1000):
        event = next(generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_list = [next(generator) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")
    consumer = consume_event(event_list)
    for event in consumer:
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
