from abc import ABC, abstractmethod
from ex0.creature import Creature
from .errors import InvalidStrategyError
from ex1.capability import TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True # válida pra qualquer Creature

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}'"
                                       f" for this normal strategy")
        return creature.attack()


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