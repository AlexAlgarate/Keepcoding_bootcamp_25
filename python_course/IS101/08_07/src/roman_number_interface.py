from abc import ABC, abstractmethod


class IRomanCalculator(ABC):
    @abstractmethod
    def to_roman(self, number: int) -> str:
        pass

    @abstractmethod
    def to_arabic(self, roman: str) -> int:
        pass
