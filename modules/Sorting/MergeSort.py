from modules.Sorting.BluePrint import Sorting


class MergeSort(Sorting):

    def __init__(self, arr) -> None:
        self.arr = arr
        self.size = len(self.arr)

    def sort(self) -> None:
        pass

    def iterator(self) -> iter:
        return iter(self.arr)
    
    def generator(self) -> GeneratorExit:
        for n in self.arr:
            yield n

    def items(self) -> list:
        return self.arr

    def printArray(self) -> None:
        print(self.arr, flush=True)
