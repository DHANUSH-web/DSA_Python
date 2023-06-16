class LinearSearch:
    # Time complexity: Best -> O(1), Worst -> O(n)

    def __init__(self, arr) -> None:
        self.arr = arr
        self.size = len(self.arr)
    
    def search(self, target):
        for i in range(self.size):
            if self.arr[i] == target:
                return i
        
        return None

    def printArray(self):
        print(self.arr)
