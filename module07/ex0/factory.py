from abc import ABC, abstractmethod
from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass

