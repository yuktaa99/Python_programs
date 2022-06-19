from numpy import *

arr1 = array([
    [1,2,3],
    [4,5,6]
])

# 2d into 1d
arr2 = arr1.flatten()

# 1d into 3d
arr3 = arr2.resize(3,2)

print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

print(arr1)
print(arr2)
print(arr3)

m = matrix('1 2 3;4 5 6')

print(m)