from modules.Sorting.BluePrint import Sorting


class BubbleSort(Sorting):
    # Time complexity O(n^2)

    def __init__(self, arr) -> None:
        self.arr = arr
        self.size = len(self.arr)
        self.isSwapped = False
    
    def sort(self, reverse: bool = False) -> None:
        for i in range(0, self.size):
            self.isSwapped = False

            for j in range(0, self.size-i-1):
                if self.arr[j] < self.arr[j+1] if reverse else self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    self.isSwapped = True

            if not self.isSwapped:
                break

    def items(self) -> list:
        return self.arr
    
    def generator(self) -> GeneratorExit:
        for n in self.arr:
            yield n

    def iterator(self) -> iter:
        return iter(self.arr)
    
    def printArray(self):
        print(self.arr)
