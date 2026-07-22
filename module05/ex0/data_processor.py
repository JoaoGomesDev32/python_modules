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
    
    def validate(self, data):
        return super().validate(data)

    def ingest(self, data: int | float):
        return super().ingest(data)


class TextProcessor(DataProcessor):
    def validate(self, data: str):
        return super().validate(data)

    def ingest(self, data):
        return super().ingest(data)


class LogProcessor(DataProcessor):
    def validate(self, data: bool):
        return super().validate(data)

    def ingest(self, data):
        return super().ingest(data)
