import random
from modules.Sorting.BubbleSort import BubbleSort
from modules.Sorting.InsertionSort import InsertionSort

nums = [random.randint(0, 100) for _ in range(0, 20)]
bubbleSort = BubbleSort(arr=nums)
bubbleSort.sort()
bubbleSort.printArray()

insertionSort = InsertionSort(arr=nums)
insertionSort.sort()
insertionSort.printArray()
