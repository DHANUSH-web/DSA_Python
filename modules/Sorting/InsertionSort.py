class InsertionSort:

    def __init__(self, arr) -> None:
        self.arr = arr
        self.size = len(self.arr)

    def sort(self):
        for i in range(1, self.size):
            current = self.arr[i]
            j = i-1

            while j >= 0 and self.arr[j] > current:
                self.arr[i] = self.arr[j]
                j-=1

            self.arr[i] = current
    
    def printArray(self):
        print(self.arr)
