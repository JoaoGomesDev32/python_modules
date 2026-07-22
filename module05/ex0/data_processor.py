from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        pass


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._rank: int = 0

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
        else:
            self._storage.append(str(data))

    def output(self) -> tuple[int, str]:
        value = self._storage.pop(0)
        rank = self._rank
        self._rank += 1
        return (rank, value)


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._rank: int = 0

    def validate(self, data: Any) ->bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data):
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
        else:
            self._storage.append(str(data))

    def output(self) -> tuple[int, str]:
        value = self._storage.pop(0)
        rank = self._rank
        self._rank += 1
        return (rank, value)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._rank: int = 0

    def validate(self, data: Any) ->bool:
        if isinstance(data, dict):
            return all(isinstance(k, str) and isinstance(v, str)
                       for k, v in data.items())
        if isinstance(data, list):
            return all(
                isinstance(x, dict) and
                all(isinstance(k, str) and isinstance(v, str)
                    for k, v in x.items())
                for x in data
            )
        return False

    def ingest(self, data: list[dict[str, str]] | dict[str, str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(
                    f"{item['log_level']}: {item['log_message']}"
                )
        else:
            self._storage.append(
                f"{data['log_level']}: {data['log_message']}"
            )

    def output(self) -> tuple[int, str]:
        value = self._storage.pop(0)
        rank = self._rank
        self._rank += 1
        return (rank, value)


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")

    numeric = NumericProcessor()
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest('foo')  # type: ignore
    except ValueError as e:
        print(f"Got exception: {e}")

    numeric.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f"Numeric value {rank}: {value}")