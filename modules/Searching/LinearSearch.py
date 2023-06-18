from abc import ABC
from BluePrint import Searching


class LinearSearch(Searching, ABC):

    def __init__(self, arr: list) -> None:
        self.arr = arr
        self.size = len(self.arr)

    def search(self, target: any) -> int or None:
        for i in range(self.size):
            if self.arr[i] == target:
                return i

        return None

    def items(self) -> list:
        return self.arr

    def generator(self) -> GeneratorExit:
        for i in self.arr:
            yield i

    def printArray(self) -> None:
        for i in self.arr:
            print(i, flush=True)
