from modules.Searching.BinarySearch import BinarySearch
from modules.Searching.LinearSearch import LinearSearch

arr = list(range(200000))
binarySearch = LinearSearch(arr=arr)
index = binarySearch.search(target=194000)

if index is None:
    print("Not found")
else:
    print(index)
