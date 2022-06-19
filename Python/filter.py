#
# def even(n):
#     return n%2==0
from functools import reduce

lst = [3,5,7,2,8,6,4,1]

# evens = list(filter(even,lst))

evens = list(filter(lambda n: n %2 ==0,lst))
square = list(map(lambda n: n *n,lst))
sum = reduce(lambda a,b: a+b,lst)

print(evens)
print(square)
print(sum)
