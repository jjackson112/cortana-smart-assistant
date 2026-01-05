# What will Cortana do as my assistant?
# She should be a program that can remember and respond

class Cortana:
    def __init__(self, name):
        self.name = name
        self.memory = {}

    def greeting(self):
        print(f"Hi, my name is {self.name}")

if __name__ == "__main__":
    cortana = Cortana("Cortana")
    cortana.greeting()