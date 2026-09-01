from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self, is_transformed: bool = False) -> None:
        self.is_transformed = is_transformed

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
