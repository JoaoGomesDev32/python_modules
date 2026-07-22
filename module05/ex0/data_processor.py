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
        try:
            self.validate()
        except ValueError as e:
            print(f"Trying to validate input {e}")



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
            raise ValueError("Improper string data")
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
    def validate(self, data: bool):
        return super().validate(data)

    def ingest(self, data):
        return super().ingest(data)
