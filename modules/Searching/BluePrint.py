from abc import ABC, abstractmethod


class Searching(ABC):

    @abstractmethod
    def search(self, target: any) -> int or None: ...

    @abstractmethod
    def items(self) -> list: ...

    @abstractmethod
    def iterator(self) -> iter: ...

    @abstractmethod
    def generator(self) -> GeneratorExit: ...

    @abstractmethod
    def printArray(self) -> None: ...
