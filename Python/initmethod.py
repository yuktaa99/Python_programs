class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is:",self.cpu,self.ram)


comp1 = Computer("i5","16gb")
comp2 = Computer("Ryzen","8gb")

comp1.config()
comp2.config()
