from abc import ABC, abstractmethod
from typing import Any, Protocol
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        raise NotImplementedError


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
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
        super().__init__()
        self._storage: list[str] = []
        self._rank: int = 0

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
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
        super().__init__()
        self._storage: list[str] = []
        self._rank: int = 0

    def validate(self, data: Any) -> bool:
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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = ",".join(value for _, value in data)
        print(f"CSV Output:\n{values}")


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = ", ".join(
            f'"item_{rank}": "{value}"' for rank, value in data
        )
        print(f"JSON Output:\n{{{items}}}")


class DataStream():
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []
        self._total: dict[str, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
        self._total[type(proc).__name__] = 0

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    name = type(proc).__name__
                    if isinstance(element, list):
                        self._total[name] += len(element)
                    else:
                        self._total[name] += 1
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - Can't process element "
                      f"in stream: {element}")

    def print_processors_stats(self) -> None:
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = type(proc).__name__
            total = self._total[name]
            remaining = len(proc._storage)
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            collected: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc._storage:
                    collected.append(proc.output())
            if collected:
                plugin.process_output(collected)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")

    stream = DataStream()
    print("Initialize Data Stream...")
    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch = ['Hello world', [3.14, -1, 2.71],
             [{'log_level': 'WARNING',
               'log_message': 'Telnet access! Use ssh instead'},
              {'log_level': 'INFO',
               'log_message': 'User wil is connected'}],
             42, ['Hi', 'five']]

    print(f"\nSend first batch of data on stream: {batch}")
    stream.process_stream(batch)
    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVPlugin())
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    batch2 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
              [{'log_level': 'ERROR', 'log_message': '500 server crash'},
               {'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'}],
              [32, 42, 64, 84, 128, 168], 'World hello']

    print(f"\nSend another batch of data: {batch2}")
    stream.process_stream(batch2)
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONPlugin())
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()
