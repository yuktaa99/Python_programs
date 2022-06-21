
f = open("demo","r")

# f = open("demo","w")
# f = open("demo","a")

f1 = open("demo2","w")

# f.write("bye")

# print(f.read())

for data in f:
    f1.write(data)

# print(f.readline())