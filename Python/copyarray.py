from  numpy import *
from copy import *
arr = [1, 2, [3, 5], 4, 10]

# arr2 = arr.view()
# arr2 = arr.copy()

#shallow copy
arr2 = copy(arr)

#deep copy
arr3 = deepcopy(arr)

arr[1] = 8

arr[2].append(9)

print(arr)
print(arr2)
print(arr3)