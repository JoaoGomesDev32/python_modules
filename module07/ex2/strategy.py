from abc import ABC, abstractmethod
from ex0.creature import Creature
from .errors import InvalidStrategyError
from ex1.capability import TransformCapability, HealCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}'"
                                       f" for this normal strategy")
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}'"
                                       f" for this aggressive strategy")
        assert isinstance(creature, TransformCapability)
        return (
            f"{creature.transform()}\n{creature.attack()}"
            f"\n{creature.revert()}"
        )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}'"
                                       f" for this defensive strategy")
        assert isinstance(creature, HealCapability)
        return f"{creature.attack()}\n{creature.heal()}"
