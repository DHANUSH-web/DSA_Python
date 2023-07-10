from modules.Sorting.BluePrint import Sorting
from abc import ABC


class InsertionSort(Sorting, ABC):
    # Time complexity O(n^2)

    def __init__(self, arr: list) -> None:
        self.arr = arr.copy()
        self.size = len(self.arr)

    def sort(self):
        for i in range(1, self.size):
            current = self.arr[i]
            j = i-1

            while j >= 0 and self.arr[j] > current:
                self.arr[j+1] = self.arr[j]
                j -= 1

            self.arr[j+1] = current

    def items(self) -> list:
        return self.arr
    
    def generator(self) -> GeneratorExit:
        for n in self.arr:
            yield n

    def iterator(self) -> iter:
        return iter(self.arr)
    
    def printArray(self):
        print(self.arr)
