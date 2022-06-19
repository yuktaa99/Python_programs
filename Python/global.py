
# gloabl and local inside same function
a = 20

def abc():

    a = 10

    b = globals()['a']

    print(a)

    globals()['a'] = 15


abc()
print(a)
