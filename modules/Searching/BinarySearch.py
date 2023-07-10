from modules.Searching.BluePrint import Searching


class BinarySearch(Searching):

    def __init__(self, arr: list) -> None:
        self.arr = arr.copy()
        self.size = len(self.arr)

    def search(self, target: any) -> int or None:
        left = 0
        right = self.size - 1

        while left <= right:
            middle = (left + right) // 2

            if self.arr[middle] == target:
                return middle
            elif self.arr[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return None
    
    def items(self) -> list:
        return self.arr
    
    def iterator(self) -> iter:
        return iter(self.arr)
    
    def generator(self) -> GeneratorExit:
        for i in self.arr:
            yield i

    def printArray(self):
        print(self.arr)
