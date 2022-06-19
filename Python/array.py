from array import *
a = array("i",[2,3,4,5])

new_a = array(a.typecode,(i*i for i in a))

for j in new_a:
    print(j)