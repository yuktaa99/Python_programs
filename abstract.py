from abc import ABC,abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):

    def process(self):
        print("HP")

comp1 = Laptop()

comp1.process()