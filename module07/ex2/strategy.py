from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def act(self) -> str:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
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