from modules.Sorting.BluePrint import Sorting


class QuickSort(Sorting):

    def __init__(self, arr: list) -> None:
        self.arr = arr
        self.size = len(self.arr)

    def sort(self, reverse: bool = False) -> None:
        pass

    def items(self) -> list:
        return self.arr
    
    def generator(self) -> GeneratorExit:
        for n in self.arr:
            yield n

    def iterator(self) -> iter:
        return iter(self.arr)
    
    def printArray(self) -> None:
        print(self.arr, flush=True)
