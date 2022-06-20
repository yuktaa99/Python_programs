class Parent:

    def __init__(self,father,mother):
        self.fname =father
        self.mname =mother

    def printname(self):
        print(self.fname,self.mname)

class Child(Parent):
    def __init__(self,father,mother,age,year):
        super().__init__(father,mother)
        self.age = age
        self.year =year

    def printname2(self):
        print(self.fname,self.mname,self.age,self.year)


p = Parent("A","B")
c = Child("C","D","18","2022")

p.printname()

c.printname2()
