
# *b is a tuple
def sum(a, *b):

    c=a
    for i in b:
        c= c+i

    print(c)

sum(4,10,2,76)