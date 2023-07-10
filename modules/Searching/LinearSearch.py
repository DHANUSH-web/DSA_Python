from BluePrint import Searching


class LinearSearch(Searching):

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

    def iterator(self) -> iter:
        return iter(self.arr)

    def printArray(self) -> None:
        for i in self.arr:
            print(i, flush=True)
