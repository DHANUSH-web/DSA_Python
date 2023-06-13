class BubbleSort:
    # Time complexity O(n^2)

    def __init__(self, arr) -> None:
        self.arr = arr
        self.size = len(self.arr)
    
    def sort(self):
        for i in range(0, self.size):
            for j in range(0, self.size-i-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
    
    def printArray(self):
        print(self.arr)
