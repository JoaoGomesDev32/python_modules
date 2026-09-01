from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capability import TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def attack(self) -> str:
        pass

class AggressiveStrategy(BattleStrategy):
    def attack(self) -> str:
        pass

    def revert(self) -> str:
        pass


class DefensiveStrategy(BattleStrategy):
    def attack(self) -> str:
        pass

    def heal(self) -> str:
        pass