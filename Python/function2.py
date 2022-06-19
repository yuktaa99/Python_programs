
# to pass multiple data
def person(name, **data):

    print(name)
    print(data)

    for i ,j in data.items():
        print(i,j)

person("yukta",age="23",location="blr")