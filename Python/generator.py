def simple():
    yield 1
    yield 2
    yield 3

values = simple()

print(values.__next__())

for i in values:
    print(i)
#
for i in simple():
    print(i)

