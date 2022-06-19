import array as arr

a = arr.array("i",[])

n = int(input("Enter size of array:"))

for i in range(n):
    x= int(input("Enter value:"))
    a.append(x)

print(a)
